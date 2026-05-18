---
title: Inspect with Performix
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect the particle data structure

Start by inspecting the baseline particle model in `src/baseline/particle.hpp`.

{{% notice Tip %}}

If you are using an IDE or editor with an LLM-based coding assistant, the `AGENT.md` file can improve your learning experience. This file provides repository context and helps guide the agent to give more useful assistance.

![Screenshot showing the AGENT.md file in the repository, highlighting the context file your coding assistant uses to provide more relevant guidance during this task.#center](./agent_screen_shot.png "Screenshot of GitHub Copilot in VSCode using AGENTS.md as a system prompt to act as a learning assistant.")

{{% /notice %}}

The baseline implementation stores every property for one particle in a single structure:

```cpp
struct Particle {
    float x, y, z;                   // position      (12 bytes)
    float vx, vy, vz;                // velocity      (12 bytes)
    float mass, charge, temperature; // properties    (12 bytes)
    float pressure, energy, density; //               (12 bytes)
    float spin_x, spin_y, spin_z;    //               (12 bytes)
    float pad;                       // padding        (4 bytes)
};
```

The ownership container in the same file is:

```cpp
class ParticleOwner {
    // Stores particle references used by the simulation.
    std::vector<Particle*> particles_;
};
```

The update loop in `src/baseline/baseline.cpp` repeatedly updates particle positions:

```cpp
for (int iter = 0; iter < iters; ++iter) {
    update_positions(particles.data(), NUM_PARTICLES, dt);
}
```

This baseline design can create avoidable memory overhead:

- `ParticleOwner` stores pointers to separately allocated `Particle` objects, so the hot loop must follow an extra level of indirection.
- Each `Particle` is 64 bytes, but the position update only uses `x`, `y`, `z`, `vx`, `vy`, and `vz`.
- Loading whole particle objects can waste cache capacity and memory bandwidth when the loop only needs a subset of fields.

Before you optimize anything, profile and measure.

## Run the Performix Memory Access Recipe

Open the Performix GUI on your local machine and select the **Memory Access** recipe.

Configure the recipe to launch the baseline workload on your remote Arm target:

- Select the configured remote target.
- Set **Workload type** to **Launch a new process**.
- Set **Workload** to the baseline executable:

```output
<path to build directory>/baseline
```

Keep the default profiling duration so Performix records until the workload exits.

![Performix Memory Access recipe setup showing the selected remote Arm target and the workload path field populated with the baseline binary, which confirms the run configuration before profiling starts.#center](./setup.png "Configure the Performix Memory Access recipe")

Start the recipe and wait for the results to load.

## Assess Performance

![Performix Memory Access results for the baseline binary showing update_positions with about 66 percent L1C load hits and around 26-cycle average L1C latency, indicating weak cache locality in the hot path.#center](./performix_before_optimizations.png "Baseline memory access results before optimization")

Look at the memory access results for the baseline binary. Most samples are associated with the `update_positions()` function. The `L1C % Loads` value shows that only about two thirds of loads hit in L1 cache, and the average L1 cache load latency is about 26 cycles. A cache-friendly hot loop should have a much higher L1 hit rate and lower average latency.

To investigate further, check the TLB walk data. As described in the background section, the TLB caches virtual-to-physical address translations. As per the image below, the `TLB Walk Breakdown` tab shows no significant TLB walks. That means address translation is not the main issue.

![Performix Memory Access results show 0% TLB walks across all functions in the baseline binary, indicating that TLB pressure and costly address translation misses are not contributing to the performance issue.#center](./no_tlb_walks.png "TLB walk results showing 0 page table walks for all functions in baseline implementation")

In summary:

- Average load latency is about 26 cycles, indicating frequent accesses beyond L1 cache.
- SPE samples are concentrated in `update_positions()`, confirming this loop dominates execution.
- TLB misses are not significant, so page walks are not the source of the slowdown.

Double-click the `update_positions()` row to open the source code view. The source view shows that the samples concentrate on the per-particle position updates.

![Performix source code view for update_positions showing sample concentration on the x, y, and z update statements, helping you confirm that this loop is the main optimization target.#center](./source_code.png "Baseline source-level samples in update_positions")

Given that the majority of samples are associated with accessing the `Particle` data structure and that we fall back to L2 cache ~1/3 of the time, to improve the execution time of this example we will need to focus on more efficient ways, if any, of accessing the `Particle` member variables. For example, there may be an alternative data structure that has better cache utilization.

In the next section, you use this evidence to guide optimization.
