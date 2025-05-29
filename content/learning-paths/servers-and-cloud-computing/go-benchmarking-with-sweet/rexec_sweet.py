#!/usr/bin/env python3
# ANSI color codes for visual differentiation
COLORS = ['\033[94m', '\033[92m']  # blue, green
RESET = '\033[0m'
import subprocess
import threading
import tempfile
import os
import sys
from datetime import datetime

# Helper: get running GCP VM instances
def get_running_instances():
    """Return a list of names of GCP VMs that are currently RUNNING."""
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter=status=RUNNING",
             "--format=value(name)"],
            universal_newlines=True
        )
        instances = [line.strip() for line in output.splitlines() if line.strip()]
        return instances
    except subprocess.CalledProcessError as e:
        print("Error fetching running instances:", e, file=sys.stderr)
        return []

# Helper: prompt user to choose an instance
def choose_instance(instances):
    """Prompt user to choose an instance from the list."""
    if not instances:
        print("No running instances found.", file=sys.stderr)
        sys.exit(1)
    print("Select an instance:")
    for idx, name in enumerate(instances, 1):
        print(f"{idx}. {name}")
    while True:
        choice = input(f"Enter number (1-{len(instances)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(instances):
                return instances[idx - 1]
        print("Invalid selection, try again.")

def get_instance_zone(name):
    """Return the zone of the given GCP VM instance."""
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter", f"name={name}",
             "--format=value(zone)"],
            universal_newlines=True
        )
        zone = output.strip()
        if not zone:
            raise ValueError(f"No zone found for instance {name}")
        return zone
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error fetching zone for instance {name}: {e}", file=sys.stderr)
        sys.exit(1)

# map benchmark name → sweet command fragment
BENCHMARKS = {
    "biogo-igor":      'sweet run -count 10 -run="biogo-igor" config.toml',
    "biogo-krishna":   'sweet run -count 10 -run="biogo-krishna" config.toml',
    "bleve-index":     'sweet run -count 10 -run="bleve-index" config.toml',
    "cockroachdb":     'sweet run -count 10 -run="cockroachdb" config.toml',
    "esbuild":         'sweet run -count 10 -run="esbuild" config.toml',
    "etcd":            'sweet run -count 10 -run="etcd" config.toml',
    "go-build":        'sweet run -count 10 -run="go-build" config.toml',
    "gopher-lua":      'sweet run -count 10 -run="gopher-lua" config.toml',
    "gvisor":          'sweet run -count 10 -run="gvisor" config.toml',
    "markdown":        'sweet run -count 10 -run="markdown" config.toml',
    "tile38":          'sweet run -count 10 -run="tile38" config.toml',
}

def choose_benchmark():
    """Prompt user to choose a benchmark from the available list, defaulting to markdown."""
    names = list(BENCHMARKS.keys())
    print("Select a benchmark (default is markdown):")
    for idx, name in enumerate(names, 1):
        default_marker = " (default)" if name == "markdown" else ""
        print(f"{idx}. {name}{default_marker}")
    default_idx = names.index("markdown") + 1
    prompt_text = f"Enter number (1-{len(names)}) [{default_idx}]: "
    while True:
        choice = input(prompt_text).strip()
        if choice == "":
            # user hit Enter → default
            return names[default_idx - 1]
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(names):
                return names[idx - 1]
        print("Invalid selection, try again.")

def prompt(prompt_text, default=None, validator=None):
    """
    Prompt the user with an optional default value.
    If validator is provided, loop until validator(value) is True.
    """
    while True:
        if default:
            ans = input(f"{prompt_text} [{default}]: ").strip()
            if ans == "":
                ans = default
        else:
            ans = input(f"{prompt_text}: ").strip()
        if validator is None or validator(ans):
            return ans
        print("Invalid value, please try again.")

def run_remote(name, zone, remote_dir, sweet_cmd, color):
    """
    SSH to the instance and run the sweet benchmark, streaming output.
    """
    ssh_cmd = [
        "gcloud", "compute", "ssh", name,
        "--zone", zone,
        "--command", f"export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; export PATH=$PATH:$GOBIN:/usr/local/go/bin; cd {remote_dir} && {sweet_cmd}"
    ]
    p = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def reader():
        for line in iter(p.stdout.readline, b""):
            sys.stdout.write(f"{color}[{name}]{RESET} {line.decode()}")
    t = threading.Thread(target=reader, daemon=True)
    t.start()
    p.wait()
    if p.returncode != 0:
        print(f"[{name}] ⚠️ exited with code {p.returncode}")
    else:
        print(f"[{name}] ✅ benchmark completed")
    return p.returncode

def scp_results(name, zone, remote_dir, local_out):
    """
    Copy back all files in remote_dir that match the benchstat inputs.
    Assumes sweet dumps its outputs in remote_dir (or subdir).
    Adjust the glob if needed.
    """
    # Change this glob if your sweet run outputs files elsewhere
    remote_pattern = f"{remote_dir}/*.txt"
    scp_cmd = [
        "gcloud", "compute", "scp",
        f"{name}:{remote_pattern}",
        local_out,
        "--zone", zone
    ]
    subprocess.check_call(scp_cmd)

def main():
    print("\n=== Benchmark Runner ===\n")
    # Prompt once for benchmark to run on both systems
    bench = choose_benchmark()
    systems = []
    for i in (1,2):
        print(f"\n--- System {i} ---")
        instances = get_running_instances()
        name = choose_instance(instances)
        zone = get_instance_zone(name)
        remote_dir = prompt("Remote directory", default="~/benchmarks/sweet")
        systems.append({
            "name": name,
            "zone": zone,
            "bench": bench,
            "remote_dir": remote_dir,
            "cmd": BENCHMARKS[bench]
        })

    # run each benchmark in parallel
    errors = []
    codes = {}
    threads = []
    for syscfg in systems:
        def run_and_store(syscfg=syscfg):
            idx = systems.index(syscfg)
            color = COLORS[idx % len(COLORS)]
            code = run_remote(
                syscfg["name"],
                syscfg["zone"],
                syscfg["remote_dir"],
                syscfg["cmd"],
                color
            )
            codes[syscfg["name"]] = code

        t = threading.Thread(target=run_and_store, daemon=True)
        t.start()
        threads.append(t)

    # wait for all benchmarks to finish
    for t in threads:
        t.join()

    # collect any failures
    for name, code in codes.items():
        if code != 0:
            errors.append(name)

    if errors:
        print("\n⚠️ Some benchmarks failed. Aborting benchstat step.")
        sys.exit(1)

    # collect results and run benchstat on the second system
    primary = systems[1]
    secondary = systems[0]

    # create a remote temp directory on primary
    mktemp_cmd = [
        "gcloud", "compute", "ssh", primary["name"],
        "--zone", primary["zone"],
        "--command", "mktemp -d"
    ]
    remote_tmp = subprocess.check_output(mktemp_cmd, universal_newlines=True).strip()
    print(f"Created remote temp dir on {primary['name']}: {remote_tmp}")

    # copy results from both systems locally first
    with tempfile.TemporaryDirectory() as tmp:
        local_sec = os.path.join(tmp, f"{secondary['name']}.results")
        print(f"Copying {secondary['name']} results to local: {local_sec}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            f"{secondary['name']}:{secondary['remote_dir']}/results/{bench}/*.results",
            local_sec,
            "--zone", secondary["zone"]
        ])

        local_prim = os.path.join(tmp, f"{primary['name']}.results")
        print(f"Copying {primary['name']} results to local: {local_prim}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            f"{primary['name']}:{primary['remote_dir']}/results/{bench}/*.results",
            local_prim,
            "--zone", primary["zone"]
        ])

        # push both files to primary's remote temp dir, renamed by hostname
        print(f"Pushing {secondary['name']} results to {primary['name']}:{remote_tmp}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            local_sec,
            f"{primary['name']}:{remote_tmp}/{secondary['name']}.results",
            "--zone", primary["zone"]
        ])

        print(f"Pushing {primary['name']} results to {primary['name']}:{remote_tmp}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            local_prim,
            f"{primary['name']}:{remote_tmp}/{primary['name']}.results",
            "--zone", primary["zone"]
        ])

    # run benchstat on primary and list results
    benchstat_cmd = f"benchstat -format csv {remote_tmp}/{secondary['name']}.results {remote_tmp}/{primary['name']}.results > {remote_tmp}/benchstat.results"
    ls_cmd = f"ls -al {remote_tmp}/{secondary['name']}.results {remote_tmp}/{primary['name']}.results {remote_tmp}/benchstat.results"
    ssh_cmd = [
        "gcloud", "compute", "ssh", primary["name"],
        "--zone", primary["zone"],
        "--command", (
            "export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; "
            "export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
            f"{benchstat_cmd} && echo \"Results files:\" && {ls_cmd}"
        )
    ]
    subprocess.check_call(ssh_cmd)

    # Pull results back to local 'results' directory
    local_root = os.path.join(os.getcwd(), "results")
    os.makedirs(local_root, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    subdir = f"{secondary['name']}-{primary['name']}-{bench}-{timestamp}"
    local_dir = os.path.join(local_root, subdir)
    os.makedirs(local_dir, exist_ok=True)
    print(f"Copying all result files to local directory: {local_dir}")

    # SCP each file from the primary's remote_tmp
    subprocess.check_call([
        "gcloud", "compute", "scp",
        f"{primary['name']}:{remote_tmp}/{secondary['name']}.results",
        local_dir, "--zone", primary["zone"]
    ])
    subprocess.check_call([
        "gcloud", "compute", "scp",
        f"{primary['name']}:{remote_tmp}/{primary['name']}.results",
        local_dir, "--zone", primary["zone"]
    ])
    subprocess.check_call([
        "gcloud", "compute", "scp",
        f"{primary['name']}:{remote_tmp}/benchstat.results",
        local_dir, "--zone", primary["zone"]
    ])

if __name__ == "__main__":
    main()