---

title: Performance

weight: 8

### FIXED, DO NOT MODIFY

layout: learningpathall

---

## Benchmarking

The Voice Assistant application also provides a benchmark mode so you can easily test out the performance of an LLM model with a sample number of input and output tokens.

![welcome image alt-text#center](voice_assistant_welcome.png "Welcome Screen")

Tap **Benchmark** to navigate to benchmark screen.

![Benchmark image alt-text#center](voice_assistant_benchmark_1.png "Benchmark Screen")

## Benchmark controls

You can use application controls to enable extra functionality or gather performance data.

|Setting|Default|Description|
|---|---|---|
|Input tokens|128|Number of prompt (input) tokens fed to the model before generation starts.|
|Output tokens|128|Number of new tokens the model should generate after the prompt.|
|Threads|4|Number of CPU threads used for inference.|
|Iterations|5|Number of measured benchmark runs to collect stable, averaged measurements.|
|Warmup|1|Number of warmup iterations which are not counted in benchmarking, these eliminate one-time overheads before measuring.|

## Example performance with a Vivo X300 Android phone

The table table shows the measurements (in tokens per second) measured on a Vivo X300 android phone:

| LLM Framework     | Model                                     | Without SME2   | With SME2 | Uplift  |
|-------------------|-------------------------------------------|----------------|-----------|---------|
| mnn               | llama-3.2-1B                              | 187.06         | 334.57    | 78.87%  |
|                   | qwen25vl-3b                               | 73.5           | 132.46    | 80.22%  |



{{% notice Note %}}
The Android system enforces throttling, so your own results may vary slightly.
{{% /notice %}}

As shown, SME2 brings a dramatic performance improvement.

