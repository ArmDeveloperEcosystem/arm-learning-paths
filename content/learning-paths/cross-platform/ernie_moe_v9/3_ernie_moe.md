---
title: Compare ERNIE model behavior and expert routing
weight: 4
layout: "learningpathall"
---

## Compare ERNIE PT and Thinking model behavior

Now that both ERNIE-4.5 models are installed and verified, you can compare their output behavior on the same task.

In this section, you compare the inference styles of PT and Thinking models, and learn how to inspect internal MoE expert routing behavior during generation.

Both ERNIE-4.5 models share the same MoE architecture and parameter count (around 21 B total, around 3 B activated at runtime), but they're tuned for different objectives:
- PT: general-purpose model trained on multilingual corpora for versatile tasks
- Thinking: tuned for multi-step reasoning, long context, and structured response generation

You can now observe how these different tuning objectives affect output behavior.

### Example task: Product behavior analysis

Using an editor, copy the following prompt into a file named `prompt1.txt`:

```txt
You are a fitness brand strategist.  
User profile: Buys protein powder + dumbbells + gym wear, works out at home 4‑5× per week, shares results online, now exploring recovery nutrition and smart gym gear.  
Task:  
1. Identify their top motivation and one hidden pain point.  
2. Propose one new product line.  
3. Create a short marketing tagline (≤ 15 words).
```

Run the prompt using both models.

Here is the PT variant:

```bash
./bin/llama-cli \
    -m $HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-PT-Q4_0.gguf \
    -f prompt1.txt \
    -c 4096 -t 12 \
    --jinja
```

The output is similar to:

```output
Assistant: 1. **Top Motivation**: Achieving visible results and maintaining progress through efficient recovery nutrition.  
**Hidden Pain Point**: Balancing high-intensity training with optimal recovery nutrition during busy workouts.  
2. **New Product Line**: *Smart Recovery Meal Kits* – Customizable, nutrient-dense, and easy-to-prepare post-workout meals designed for quick consumption and recovery optimization.  
3. **Marketing Tagline**: "Fuel Progress, Recover Faster – Smart Nutrition for the Hard Worker."
```
The answer shows:
- Direct conclusions with minimal reasoning
- Sensible but general product suggestions (such as "Smart Recovery Meal Kits")
- Standard advertising tone in the tagline ("Fuel Progress, Recover Faster")

Here is the Thinking variant:

```bash
./bin/llama-cli \
    -m $HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf \
    -f prompt1.txt \
    -c 4096 -t 12 \
    --jinja
```

The output is similar to:

```output
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
- Deeper layering: the model begins by inferring user motivation, explores multiple product strategies, and then refines the tagline through iteration.
- Transparent reasoning: the model "thinks out loud" with phrases like "let me try again… maybe that's too long…", mimicking human deliberation.
- User-focused messaging: taglines like "Share. Track. Conquer." directly appeal to the user's community sharing and progress motivation.

### Compare the outputs
After execution, review the responses and compare them along the following dimensions:

| **Aspect**           | **PT Model**                                      | **Thinking Model**                                                                   |
|----------------------|---------------------------------------------------|--------------------------------------------------------------------------------------|
| Language Style       | Direct, ad-like tone                              | Layered and natural, mimics human internal reasoning                                 |
| Reasoning Depth      | High-level summarization with minimal exploration | Step-by-step inference with intermediate reflections and multiple alternatives       |
| Suggested Actions    | Pre-packaged idea (for example, meal kits)        | Context-aware concepts (for example, smart gear that integrates with current user behavior) |

## Observe MoE expert routing with debug logs

To look under the hood of the MoE model, you now add debug logging to observe internal MoE behavior and which experts are routed during inference.

Use an editor to open `src/models/ernie4-5-moe.cpp` in the llama.cpp repository and locate the function `build_moe_ffn()`.
Insert a print statement right before calling `build_moe_ffn()`.

```c
printf("---[DEBUG]--- entering build_moe_ffn at layer %d with %d experts (use %d)\n", il, n_expert, n_expert_used);
```

Rebuild llama.cpp:

```bash
cd $HOME/llama.cpp/build
make -j$(nproc)
```

Run inference with the same prompt and monitor the console for lines like this:

```output
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

This output shows that each layer has 64 total experts available. The actual number of experts activated per token (typically 6 for ERNIE-4.5) is determined by the router during inference and isn't directly visible in this debug output.

{{% notice Note %}}
You can also trace the function `llm_graph_context::build_moe_ffn()` in `src/llama-graph.cpp` to see how expert selection works at a deeper level.
{{% /notice %}}

Remove the print statement from `src/models/ernie4-5-moe.cpp` and rebuild llama.cpp before moving to the next section. 

As you review the debug output, observe whether the number of active experts changes between the PT and Thinking models. Look for patterns in routing, such as different token batches routing to differing expert sets. You can also correlate routing behavior with output differences, as deeper routing variety might align with more detailed responses.

## What you've accomplished and what's next

In this section, you:
- Compared ERNIE-4.5 PT and Thinking model outputs on the same task
- Observed how fine-tuning affects reasoning depth and response structure
- Learned how to add debug instrumentation to examine MoE expert routing

This comparison highlights the advantage of MoE fine-tuning. Even with the same architecture, thoughtful tuning can significantly change a model's reasoning behavior. The Thinking model is better suited for applications that need analytical depth, making it ideal for edge AI scenarios like customer profiling or real-time recommendations.

In the next section, you switch focus from model behavior to system-level performance by compiling with Armv9 instruction sets and measuring the impact on inference speed.
