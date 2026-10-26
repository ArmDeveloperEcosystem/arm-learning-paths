#!/usr/bin/env python3

import argparse
import hashlib
import json
import pickle
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from tensordict.nn.distributions import NormalParamExtractor
from torchrl.modules import TanhNormal


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cfg_get(cfg, key, default=None):
    """Read a setting from a dict-like or attribute-based config object."""
    if isinstance(cfg, dict):
        return cfg.get(key, default)
    getter = getattr(cfg, "get", None)
    if callable(getter):
        try:
            return getter(key, default)
        except (TypeError, AttributeError):
            pass
    return getattr(cfg, key, default)


def class_name(value) -> str:
    if isinstance(value, type):
        return f"{value.__module__}.{value.__qualname__}"
    return str(value)


def find_actor_loss_group(state):
    matches = []
    for key, value in state.items():
        if not isinstance(key, str) or not key.startswith("loss_"):
            continue
        if not hasattr(value, "items"):
            continue
        if any(
            isinstance(item_key, str) and "actor_network_params" in item_key
            for item_key in value.keys()
        ):
            matches.append((key, value))
    if len(matches) != 1:
        raise RuntimeError(
            "Expected exactly one loss group containing actor_network_params; "
            f"found {[name for name, _ in matches]}"
        )
    return matches[0]


def find_actor_tensor(actor_state, suffix):
    matches = [
        value
        for key, value in actor_state.items()
        if isinstance(key, str)
        and "actor_network_params" in key
        and key.endswith(suffix)
        and torch.is_tensor(value)
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one actor tensor ending in {suffix}; found {len(matches)}"
        )
    return matches[0].detach().cpu().to(torch.float32).contiguous()


def fail_if(condition, message):
    if condition:
        raise SystemExit(message)


def validate_numpy_export(output, torch_weights, scale_mapping):
    """Validate tensor serialization and deterministic TanhNormal semantics."""
    generator = torch.Generator(device="cpu").manual_seed(1234)
    observations = torch.randn((16, 18), generator=generator, dtype=torch.float32)

    W1_t, b1_t, W2_t, b2_t, W3_t, b3_t = torch_weights

    with torch.no_grad():
        hidden1 = torch.tanh(F.linear(observations, W1_t, b1_t))
        hidden2 = torch.tanh(F.linear(hidden1, W2_t, b2_t))
        raw_torch = F.linear(hidden2, W3_t, b3_t)

    with np.load(output, allow_pickle=False) as exported:
        obs_np = observations.numpy()
        hidden1_np = np.tanh(obs_np @ exported["W1"].T + exported["b1"])
        hidden2_np = np.tanh(hidden1_np @ exported["W2"].T + exported["b2"])
        raw_numpy = hidden2_np @ exported["W3"].T + exported["b3"]

    max_raw_error = float(np.max(np.abs(raw_numpy - raw_torch.numpy())))
    if not np.allclose(raw_numpy, raw_torch.numpy(), rtol=1e-5, atol=1e-6):
        raise RuntimeError(
            "Exported NumPy actor does not match the checkpoint actor MLP. "
            f"Maximum raw-output error: {max_raw_error}"
        )

    extractor = NormalParamExtractor(scale_mapping=scale_mapping)
    with torch.no_grad():
        loc, scale = extractor(raw_torch)
        distribution = TanhNormal(loc, scale, low=-1.0, high=1.0)
        torchrl_action = distribution.deterministic_sample
        lightweight_action = torch.tanh(raw_torch[..., :2])

    max_action_error = float(
        torch.max(torch.abs(torchrl_action - lightweight_action)).item()
    )
    if not torch.allclose(
        torchrl_action, lightweight_action, rtol=1e-5, atol=1e-6
    ):
        raise RuntimeError(
            "tanh(loc) does not match TorchRL TanhNormal deterministic_sample. "
            f"Maximum action error: {max_action_error}"
        )

    return max_raw_error, max_action_error


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Export the validated shared BenchMARL MAPPO VMAS-navigation actor "
            "to a lightweight NumPy .npz artifact."
        )
    )
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output", help="Exact .npz output path")
    parser.add_argument(
        "--output-dir",
        default=str(Path.home() / "mappo_actor_exports"),
        help="Output directory used when --output is omitted",
    )
    args = parser.parse_args()

    checkpoint = Path(args.checkpoint).expanduser().resolve()
    requested_output = (
        Path(args.output).expanduser().resolve() if args.output else None
    )
    output_dir = Path(args.output_dir).expanduser().resolve()

    fail_if(not checkpoint.is_file(), f"Checkpoint not found: {checkpoint}")

    experiment_dir = checkpoint.parent.parent
    config_file = experiment_dir / "config.pkl"
    fail_if(not config_file.is_file(), f"config.pkl not found: {config_file}")

    # config.pkl is a trusted BenchMARL artifact from the matching training run.
    with config_file.open("rb") as file:
        _task = pickle.load(file)
        task_config = pickle.load(file)
        algorithm_config = pickle.load(file)
        model_config = pickle.load(file)
        _seed = pickle.load(file)
        experiment_config = pickle.load(file)

    n_agents_value = cfg_get(task_config, "n_agents")
    fail_if(n_agents_value is None, "Task configuration does not contain n_agents")
    n_agents = int(n_agents_value)

    collisions = bool(cfg_get(task_config, "collisions", True))
    observe_all_goals = bool(cfg_get(task_config, "observe_all_goals", False))
    n_lidar_rays = int(cfg_get(task_config, "n_lidar_rays", 12))

    fail_if(not collisions, "This exporter expects navigation collisions=true")
    fail_if(
        observe_all_goals,
        "This exporter expects observe_all_goals=false; the observation layout would differ",
    )
    fail_if(
        n_lidar_rays != 12,
        f"This exporter expects 12 LiDAR rays; found {n_lidar_rays}",
    )

    fail_if(
        not bool(getattr(experiment_config, "share_policy_params", False)),
        "This exporter expects share_policy_params=true",
    )
    fail_if(
        not bool(getattr(algorithm_config, "use_tanh_normal", False)),
        "This exporter expects MAPPO use_tanh_normal=true",
    )

    scale_mapping = str(
        getattr(algorithm_config, "scale_mapping", "biased_softplus_1.0")
    )

    num_cells = list(getattr(model_config, "num_cells", []))
    activation_class = getattr(model_config, "activation_class", None)
    layer_class = getattr(model_config, "layer_class", None)
    norm_class = getattr(model_config, "norm_class", None)

    fail_if(
        num_cells != [256, 256],
        f"This exporter expects hidden layers [256, 256]; found {num_cells}",
    )
    fail_if(
        class_name(activation_class) != "torch.nn.modules.activation.Tanh",
        "This exporter expects torch.nn.Tanh hidden activations; "
        f"found {class_name(activation_class)}",
    )
    fail_if(
        class_name(layer_class) != "torch.nn.modules.linear.Linear",
        "This exporter expects torch.nn.Linear layers; "
        f"found {class_name(layer_class)}",
    )
    fail_if(
        norm_class is not None,
        "This exporter expects no normalization layer in the actor MLP",
    )

    state = torch.load(checkpoint, map_location="cpu", weights_only=True)
    loss_group_name, actor_state = find_actor_loss_group(state)

    W1_t = find_actor_tensor(actor_state, "mlp.params.0.weight")
    b1_t = find_actor_tensor(actor_state, "mlp.params.0.bias")
    W2_t = find_actor_tensor(actor_state, "mlp.params.2.weight")
    b2_t = find_actor_tensor(actor_state, "mlp.params.2.bias")
    W3_t = find_actor_tensor(actor_state, "mlp.params.4.weight")
    b3_t = find_actor_tensor(actor_state, "mlp.params.4.bias")

    expected_shapes = {
        "W1": (256, 18),
        "b1": (256,),
        "W2": (256, 256),
        "b2": (256,),
        "W3": (4, 256),
        "b3": (4,),
    }
    torch_tensors = {
        "W1": W1_t,
        "b1": b1_t,
        "W2": W2_t,
        "b2": b2_t,
        "W3": W3_t,
        "b3": b3_t,
    }
    actual_shapes = {name: tuple(value.shape) for name, value in torch_tensors.items()}
    fail_if(
        actual_shapes != expected_shapes,
        "Unexpected actor architecture. "
        f"Expected {expected_shapes}, found {actual_shapes}",
    )

    training_frames = int(state.get("state", {}).get("total_frames", 0))
    agent_group = loss_group_name.removeprefix("loss_")

    output = (
        requested_output
        if requested_output is not None
        else output_dir / f"mappo_actor_{n_agents}agent_{training_frames}.npz"
    )
    fail_if(output.suffix != ".npz", "Actor output file must use the .npz suffix")

    lidar_range = cfg_get(task_config, "lidar_range", 0.35)
    agent_radius = cfg_get(task_config, "agent_radius", 0.1)
    max_steps = cfg_get(task_config, "max_steps")

    metadata = {
        "format": "mappo_shared_actor_numpy_v2",
        "source_checkpoint_name": checkpoint.name,
        "source_checkpoint_path": str(checkpoint),
        "source_checkpoint_sha256": sha256_file(checkpoint),
        "source_config_path": str(config_file),
        "training_frames": training_frames,
        "training_n_agents": n_agents,
        "agent_group": agent_group,
        "share_policy_params": True,
        "actor_input_dim": 18,
        "actor_hidden_dims": [256, 256],
        "actor_raw_output_dim": 4,
        "deterministic_action_dim": 2,
        "activation": "tanh",
        "policy_distribution": "TanhNormal",
        "normal_scale_mapping": scale_mapping,
        "action_bounds": [-1.0, 1.0],
        "deterministic_action": "TanhNormal.deterministic_sample == tanh(loc)",
        "observation_layout": [
            "x_vmas",
            "y_vmas",
            "vx_vmas",
            "vy_vmas",
            "agent_x_minus_goal_x_vmas",
            "agent_y_minus_goal_y_vmas",
            "lidar_proximity_0",
            "lidar_proximity_1",
            "lidar_proximity_2",
            "lidar_proximity_3",
            "lidar_proximity_4",
            "lidar_proximity_5",
            "lidar_proximity_6",
            "lidar_proximity_7",
            "lidar_proximity_8",
            "lidar_proximity_9",
            "lidar_proximity_10",
            "lidar_proximity_11",
        ],
        "lidar_encoding": "lidar_range_vmas - measured_range_vmas",
        "training_n_lidar_rays": n_lidar_rays,
        "training_lidar_range_vmas": lidar_range,
        "training_agent_radius_vmas": agent_radius,
        "training_max_steps": max_steps,
        "training_collisions": collisions,
        "training_observe_all_goals": observe_all_goals,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        output,
        W1=W1_t.numpy(),
        b1=b1_t.numpy(),
        W2=W2_t.numpy(),
        b2=b2_t.numpy(),
        W3=W3_t.numpy(),
        b3=b3_t.numpy(),
        metadata_json=np.array(json.dumps(metadata)),
    )

    max_raw_error, max_action_error = validate_numpy_export(
        output,
        (W1_t, b1_t, W2_t, b2_t, W3_t, b3_t),
        scale_mapping,
    )

    print(f"Actor export:              {output}")
    print(f"Agents:                    {n_agents}")
    print(f"Frames:                    {training_frames}")
    print(f"Actor group:               {agent_group}")
    print(f"Input:                     {W1_t.shape[1]}")
    print(f"Hidden:                    {W1_t.shape[0]}, {W2_t.shape[0]}")
    print(f"Raw output:                {W3_t.shape[0]}")
    print("Deterministic action:      2-D TanhNormal deterministic_sample")
    print(f"NumPy raw parity max err:  {max_raw_error:.3e}")
    print(f"Action parity max err:     {max_action_error:.3e}")
    print("Validation:                PASS")


if __name__ == "__main__":
    main()
