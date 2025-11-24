---
title: Comparing ERNIE PT vs Thinking and Expert Routing
weight: 4
layout: "learningpathall"
---

## Compare ERNIE PT vs Thinking Model Behavior

Now that both ERNIE-4.5 models are installed and verified, you can compare their output behavior on the same task.

In this module, you’ll compare the inference styles of PT and Thinking models, and learn how to inspect internal MoE expert routing behavior during generation.

With both ERNIE-4.5 models installed and ready, we can now observe how their tuning objectives affect output—even though both share the same MoE architecture and parameter count (~21B total, ~3B activated at runtime):
- PT (Post-Trained): General-purpose, trained on multilingual corpora.
- Thinking: Tuned for multi-step reasoning, long context, and structured response generation.

### Example Task: Product Behavior Analysis
Copy the following prompt into a file named `prompt1.txt`:

```
You are a fitness brand strategist.  
User profile: Buys protein powder + dumbbells + gym wear, works out at home 4‑5× per week, shares results online, now exploring recovery nutrition and smart gym gear.  
Task:  
1. Identify their top motivation and one hidden pain point.  
2. Propose one new product line.  
3. Create a short marketing tagline (≤ 15 words).
```

Run the prompt using both models:

***PT Variant:***
```bash
./bin/llama-cli \
    --jinja \
    -m ~/models/ernie-4.5/ERNIE-4.5-21B-A3B-PT-Q4_0.gguf \
    -f prompt1.txt \
    -c 4096 -t 12 \
    --jinja
```

The answer will looks like:

```
Assistant: 1. **Top Motivation**: Achieving visible results and maintaining progress through efficient recovery nutrition.  
**Hidden Pain Point**: Balancing high-intensity training with optimal recovery nutrition during busy workouts.  
2. **New Product Line**: *Smart Recovery Meal Kits* – Customizable, nutrient-dense, and easy-to-prepare post-workout meals designed for quick consumption and recovery optimization.  
3. **Marketing Tagline**: "Fuel Progress, Recover Faster – Smart Nutrition for the Hard Worker."
```

The answer shows:
- Delivers conclusions directly: motivations and pain points are briefly mentioned with little reasoning.
- Product ideas are sensible but templated: suggestions like “Smart Recovery Meal Kits” are plausible but lack contextual grounding in user behavior.
- Tagline reads like a standard advertisement: e.g., “Fuel Progress, Recover Faster” feels promotional rather than personalized.


***Thinking Variant:***
```bash
./bin/llama-cli \
    --jinja \
    -m ~/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf \
    -f prompt1.txt \
    -c 4096 -t 12 \
    --jinja
```

You will see the more comprehensive answer like:

```
 assistant
 
Let's tackle this user profile. The user buys protein powder, dumbbells, and gym wear. They work out 4-5 times a week at home and share results online. Now they're exploring recovery nutrition and smart gym gear.

First, their top motivation. They're into sharing results online, so maybe they want to inspire others or gain recognition. That's a big motivation. But what's a hidden pain point? They're moving into recovery nutrition and smart gear. Maybe they find it hard to track recovery progress or ensure their nutrition is optimized for recovery. Smart gear could help, but maybe they don't have the right tools to monitor recovery metrics like sleep, nutrition, or muscle soreness. That's a hidden pain point since they're exploring it.

Next, propose a new product line. Since they're into smart gym gear, maybe a smart recovery watch that tracks sleep, activity, and recovery metrics. Or a nutrition tracking device that syncs with their protein powder and dumbbells. Wait, they might need something that integrates with their existing products. Maybe a smart scale that tracks muscle and body composition, connected to their fitness apps. Or a wearable device that monitors recovery parameters like heart rate variability and sleep.

Marketing tagline needs to be concise, under 15 words. Combine motivation and product. For example, "Track Your Recovery, Maximize Your Gains—Smart Gear for Every Workout." But maybe more catchy. "Smarter Recovery, Stronger Results. Your Workout, Tracked." Hmm, not sure. Let me think. Maybe "Track Recovery, Fuel Progress. Smart Gear for Every Muscle." Wait, the user shares results online, so maybe highlight community or shared progress. "Share. Track. Conquer. Smart Gear for Your Recovery Journey." That's 10 words. Or "Your Workout, Tracked. Recovery, Simplified. Smart Gear Now." Maybe too vague. Let me refine. "Track. Recover. Share. Smart Gear for Your Journey." 8 words. Maybe that's better. Or "Recovery Tracked. Gains Shared. Smart Gear for Every Muscle." 9 words. Not sure. Alternatively, focus on the product. "Smart Recovery, Shared Success. Your Gear, Now Smarter." 7 words. Maybe that's better.

Wait, the user is moving into recovery nutrition and smart gear. So the product line could be a smart recovery tracker. The tagline should tie their motivation (sharing results) with the new product. Maybe "Track. Recover. Share. Smart Gear for Your Journey." 8 words. Or "Your Workouts, Tracked. Recovery, Simplified. Smart Gear Now." 9 words. Maybe that works.

So to sum up:

1. Top motivation: Inspiring others through shared results and progress tracking. Hidden pain point: Difficulty tracking recovery metrics and nutrition effectively.

2. Product line: Smart Recovery Tracker (wearable or app integrating with gear) that monitors sleep, nutrition, and recovery metrics, syncing with their existing products.

3. Tagline: "Track. Recover. Share. Smart Gear for Your Journey." (8 words)
</think>

<response>
1. **Top Motivation**: Inspiring others through shared results and progress tracking.  
2. **Hidden Pain Point**: Struggling to track recovery metrics (sleep, nutrition, muscle soreness) effectively.  
3. **Product Line**: **Smart Recovery Tracker** (wearable monitoring sleep/nutrition, syncing with protein powder/dumbbells to optimize recovery).  
4. **Tagline**: *"Track. Recover. Share. Smart Gear for Your Journey."* (8 words)
</response>

```

The answer shows:
- Responses show deeper layering: begins with inferring user motivation, iterates through possible product strategies, and only then crafts a refined tagline.
- Transparent reasoning process: the model “thinks out loud” (“let me try again… maybe that’s too long…”), mimicking human deliberation.
- Marketing language reflects user mindset: taglines like “Share. Track. Conquer.” directly appeal to community sharing and progress motivation.


### Compare the Outputs
After execution, review the responses and compare them along the following dimensions:

| **Aspect**           | **PT Model**                                      | **Thinking Model**                                                                   |
|----------------------|---------------------------------------------------|--------------------------------------------------------------------------------------|
| `Language Style`     | Direct, ad-like tone                              | Layered and natural, mimics human internal reasoning                                 |
| `Reasoning Depth`    | High-level summarization with minimal exploration | Step-by-step inference with intermediate reflections and multiple alternatives       |
| `Suggested Actions`  | Pre-packaged idea (e.g., meal kits)               | Context-aware concepts (e.g., smart gear that integrates with current user behavior) |



## Observe MoE Expert Routing with Debug Logs

If you want to look under the hood of the MoE model, you’ll now add debug log to observe internal MoE behavior which experts are routed during inference.

Open `src/models/ernie4‑5‑moe.cpp` in the llama.cpp repository and locate the function build_moe_ffn().
Insert a print statement right after the top‑k expert selection. For example:

```c
printf("---[DEBUG]--- entering build_moe_ffn at layer %d with %d experts (use %d)\n", il, n_expert, n_expert_used); // Odin
```

Rebuild llama.cpp:

```bash
cd ~/llama.cpp
make -j$(nproc)
```

Run inference with the same prompt and monitor the console for lines such as:
```
---[DEBUG]--- entering build_moe_ffn at layer 1 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 2 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 3 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 4 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 5 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 6 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 7 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 8 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 9 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 10 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 11 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 12 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 13 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 14 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 15 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 16 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 17 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 18 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 19 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 20 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 21 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 22 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 23 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 24 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 25 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 26 with 64 experts (use 64)
---[DEBUG]--- entering build_moe_ffn at layer 27 with 64 experts (use 64)
```

This reveals how many experts (e.g., 6) and how many tokens (e.g., 16) were routed at that layer.

{{% notice Note %}}
You can also trace the function `llm_graph_context::build_moe_ffn()` inside the `src/llama-graph.cpp` about how to select the expert.
{{% /notice %}}

What to observe:
- Whether the number of active experts changes between the PT and Thinking models.
- Patterns in routing: e.g., different token batches routing to differing expert sets.
- Correlate routing behaviour with output differences: deeper routing variety may align with more detailed responses.

## Takeaway
This task highlights the advantage of MoE fine-tuning: even under the same architecture, thoughtful tuning can significantly change a model’s reasoning behavior. It also reinforces that Thinking is better suited for applications requiring analytical depth—ideal for edge AI scenarios like customer profiling or real-time recommendations.

In the next section, you’ll switch focus from model behavior to system-level performance — compiling with Armv9 instruction sets and measuring the impact on inference speed.
