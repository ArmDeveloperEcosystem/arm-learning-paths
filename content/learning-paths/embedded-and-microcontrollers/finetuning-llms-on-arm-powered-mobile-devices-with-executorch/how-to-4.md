---
title: Large Language Model - Inference Benchmarking
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Latency Benchmarking
- Time-to-first-token (TTFT)
- Tokens per second throughput
- End-to-end response time
- Compare across different batch sizes

###### Additional Optimization Techniques
- Create advanced_optimization.py
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def optimize_generation_config(model, tokenizer):
    """Optimize generation parameters for faster inference"""
    
    generation_config = {
        # Use greedy decoding for speed
        "do_sample": False,
        
        # Enable KV cache for efficiency
        "use_cache": True,
        
        # Limit max tokens
        "max_new_tokens": 256,
        
        # Set padding
        "pad_token_id": tokenizer.eos_token_id,
        
        # Early stopping
        "eos_token_id": tokenizer.eos_token_id,
    }
    
    return generation_config

def benchmark_generation_strategies(model, tokenizer):
    """Compare different generation strategies"""
    
    prompt = "What is your return policy?"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    strategies = [
        {"name": "Greedy", "do_sample": False},
        {"name": "Sampling (temp=0.7)", "do_sample": True, "temperature": 0.7},
        {"name": "Top-k", "do_sample": True, "top_k": 50},
        {"name": "Top-p", "do_sample": True, "top_p": 0.9},
    ]
    
    results = []
    
    for strategy in strategies:
        start_time = time.time()
        
        with torch.no_grad():
            outputs = model.generate(
                inputs.input_ids,
                max_new_tokens=100,
                pad_token_id=tokenizer.eos_token_id,
                **{k: v for k, v in strategy.items() if k != "name"}
            )
        
        elapsed = time.time() - start_time
        results.append({
            "strategy": strategy["name"],
            "time": elapsed
        })
        
        print(f"{strategy['name']}: {elapsed:.2f}s")
    
    return results

if __name__ == "__main__":
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        device_map=None
    )
    model.eval()
    
    print("Benchmarking generation strategies...\n")
    results = benchmark_generation_strategies(model, tokenizer)
```

###### Comprehensive Benchmarking
- This is the core module showcasing ARM performance.

```python
import torch
import time
import psutil
import json
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.quantization import quantize_dynamic
from datetime import datetime
import os

class GravitonBenchmark:
    """Comprehensive benchmarking suite for Graviton3"""
    
    def __init__(self, model_name, use_quantization=False):
        self.model_name = model_name
        self.device = "cpu"
        self.use_quantization = use_quantization
        
        # Load model and tokenizer
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map=None,
            low_cpu_mem_usage=True
        )
        
        if use_quantization:
            print("Applying quantization...")
            self.model = quantize_dynamic(
                self.model,
                {torch.nn.Linear},
                dtype=torch.qint8
            )
        
        self.model.eval()
        print("Model loaded successfully!\n")
    
    def warmup(self, num_iterations=3):
        """Warm up the model"""
        print("Warming up model...")
        prompt = "Hello"
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        for _ in range(num_iterations):
            with torch.no_grad():
                _ = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=10,
                    pad_token_id=self.tokenizer.eos_token_id
                )
        print("Warmup complete\n")
    
    def benchmark_latency(self, prompts, max_new_tokens=128, num_runs=5):
        """Benchmark inference latency"""
        print(f"Running latency benchmark ({num_runs} runs)...")
        
        all_latencies = []
        all_tokens_per_sec = []
        
        for prompt in prompts:
            latencies = []
            tokens_per_sec = []
            
            for run in range(num_runs):
                inputs = self.tokenizer(prompt, return_tensors="pt")
                
                start_time = time.time()
                
                with torch.no_grad():
                    outputs = self.model.generate(
                        inputs.input_ids,
                        max_new_tokens=max_new_tokens,
                        do_sample=False,
                        use_cache=True,
                        pad_token_id=self.tokenizer.eos_token_id
                    )
                
                end_time = time.time()
                elapsed = end_time - start_time
                
                # Calculate tokens generated
                generated_tokens = outputs.shape[1] - inputs.input_ids.shape[1]
                tps = generated_tokens / elapsed
                
                latencies.append(elapsed)
                tokens_per_sec.append(tps)
            
            all_latencies.extend(latencies)
            all_tokens_per_sec.extend(tokens_per_sec)
        
        return {
            "avg_latency_sec": np.mean(all_latencies),
            "std_latency_sec": np.std(all_latencies),
            "min_latency_sec": np.min(all_latencies),
            "max_latency_sec": np.max(all_latencies),
            "p50_latency_sec": np.percentile(all_latencies, 50),
            "p95_latency_sec": np.percentile(all_latencies, 95),
            "p99_latency_sec": np.percentile(all_latencies, 99),
            "avg_tokens_per_sec": np.mean(all_tokens_per_sec),
            "max_tokens_per_sec": np.max(all_tokens_per_sec)
        }
    
    def benchmark_throughput(self, prompts, max_new_tokens=128):
        """Benchmark throughput with multiple queries"""
        print("Running throughput benchmark...")
        
        total_queries = len(prompts)
        total_tokens = 0
        
        start_time = time.time()
        
        for prompt in prompts:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    use_cache=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            total_tokens += outputs.shape[1]
        
        total_time = time.time() - start_time
        
        return {
            "total_queries": total_queries,
            "total_time_sec": total_time,
            "queries_per_sec": total_queries / total_time,
            "avg_time_per_query": total_time / total_queries,
            "total_tokens_generated": total_tokens,
            "tokens_per_sec": total_tokens / total_time
        }
    
    def benchmark_resource_usage(self, prompt, max_new_tokens=128, num_runs=3):
        """Benchmark CPU and memory usage"""
        print("Measuring resource usage...")
        
        process = psutil.Process()
        cpu_percentages = []
        memory_usages = []
        
        for _ in range(num_runs):
            # Measure before
            mem_before = process.memory_info().rss / 1024**3  # GB
            cpu_before = psutil.cpu_percent(interval=0.1)
            
            # Run inference
            inputs = self.tokenizer(prompt, return_tensors="pt")
            
            with torch.no_grad():
                _ = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            # Measure after
            cpu_after = psutil.cpu_percent(interval=0.1)
            mem_after = process.memory_info().rss / 1024**3  # GB
            
            cpu_percentages.append(cpu_after)
            memory_usages.append(mem_after)
        
        return {
            "avg_cpu_percent": np.mean(cpu_percentages),
            "max_cpu_percent": np.max(cpu_percentages),
            "avg_memory_gb": np.mean(memory_usages),
            "max_memory_gb": np.max(memory_usages)
        }
    
    def benchmark_scaling(self, prompt, token_counts=[32, 64, 128, 256]):
        """Benchmark how performance scales with output length"""
        print("Running scaling benchmark...")
        
        results = []
        
        for max_tokens in token_counts:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            
            start_time = time.time()
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=max_tokens,
                    do_sample=False,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            elapsed = time.time() - start_time
            actual_tokens = outputs.shape[1] - inputs.input_ids.shape[1]
            
            results.append({
                "requested_tokens": max_tokens,
                "actual_tokens": actual_tokens,
                "time_sec": elapsed,
                "tokens_per_sec": actual_tokens / elapsed
            })
        
        return results
    
    def run_comprehensive_benchmark(self, save_results=True):
        """Run all benchmarks"""
        print("=" * 60)
        print("COMPREHENSIVE BENCHMARK SUITE")
        print("=" * 60)
        print(f"Model: {self.model_name}")
        print(f"Quantized: {self.use_quantization}")
        print(f"Device: {self.device}")
        print("=" * 60)
        print()
        
        # Warmup
        self.warmup()
        
        # Test prompts (customer support scenarios)
        test_prompts = [
            "I need help tracking my order. It was supposed to arrive yesterday.",
            "How do I return an item I purchased last week?",
            "What is your refund policy for defective products?",
            "I can't log into my account. Can you help me reset my password?",
            "My payment didn't go through. What should I do?"
        ]
        
        results = {
            "metadata": {
                "model_name": self.model_name,
                "quantized": self.use_quantization,
                "device": self.device,
                "timestamp": datetime.now().isoformat(),
                "cpu_count": psutil.cpu_count(),
                "total_memory_gb": psutil.virtual_memory().total / 1024**3
            }
        }
        
        # 1. Latency Benchmark
        results["latency"] = self.benchmark_latency(test_prompts[:3])
        print("\nLatency Results:")
        print(f"  Avg: {results['latency']['avg_latency_sec']:.2f}s")
        print(f"  P95: {results['latency']['p95_latency_sec']:.2f}s")
        print(f"  Throughput: {results['latency']['avg_tokens_per_sec']:.2f} tok/s")
        print()
        
        # 2. Throughput Benchmark
        results["throughput"] = self.benchmark_throughput(test_prompts * 4)
        print("\nThroughput Results:")
        print(f"  Queries/sec: {results['throughput']['queries_per_sec']:.2f}")
        print(f"  Tokens/sec: {results['throughput']['tokens_per_sec']:.2f}")
        print()
        
        # 3. Resource Usage
        results["resources"] = self.benchmark_resource_usage(test_prompts[0])
        print("\nResource Usage:")
        print(f"  CPU: {results['resources']['avg_cpu_percent']:.1f}%")
        print(f"  Memory: {results['resources']['avg_memory_gb']:.2f} GB")
        print()
        
        # 4. Scaling Benchmark
        results["scaling"] = self.benchmark_scaling(test_prompts[0])
        print("\nScaling Results:")
        for item in results["scaling"]:
            print(f"  {item['requested_tokens']} tokens: {item['time_sec']:.2f}s ({item['tokens_per_sec']:.1f} tok/s)")
        print()
        
        # Save results
        if save_results:
            quant_str = "quantized" if self.use_quantization else "base"
            filename = f"benchmark_{quant_str}_{int(time.time())}.json"
            
            with open(filename, "w") as f:
                json.dump(results, f, indent=2)
            
            print(f"\nResults saved to: {filename}")
        
        print("\n" + "=" * 60)
        print("BENCHMARK COMPLETE")
        print("=" * 60)
        
        return results


def compare_configurations():
    """Compare base vs quantized model"""
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    print("\n" + "=" * 60)
    print("COMPARING BASE VS QUANTIZED MODEL")
    print("=" * 60)
    print()
    
    # Benchmark base model
    print(">>> BENCHMARKING BASE MODEL <<<\n")
    base_bench = GravitonBenchmark(model_name, use_quantization=False)
    base_results = base_bench.run_comprehensive_benchmark()
    
    print("\n" + "=" * 60)
    print()
    
    # Benchmark quantized model
    print(">>> BENCHMARKING QUANTIZED MODEL <<<\n")
    quant_bench = GravitonBenchmark(model_name, use_quantization=True)
    quant_results = quant_bench.run_comprehensive_benchmark()
    
    # Generate comparison report
    print("\n" + "=" * 60)
    print("COMPARISON SUMMARY")
    print("=" * 60)
    
    speedup = base_results["latency"]["avg_latency_sec"] / quant_results["latency"]["avg_latency_sec"]
    memory_reduction = (1 - quant_results["resources"]["avg_memory_gb"] / base_results["resources"]["avg_memory_gb"]) * 100
    throughput_improvement = (quant_results["throughput"]["queries_per_sec"] / base_results["throughput"]["queries_per_sec"] - 1) * 100
    
    print(f"\nSpeedup: {speedup:.2f}x faster")
    print(f"Memory Reduction: {memory_reduction:.1f}%")
    print(f"Throughput Improvement: +{throughput_improvement:.1f}%")
    
    # Save comparison
    comparison = {
        "base_model": base_results,
        "quantized_model": quant_results,
        "comparison": {
            "speedup": speedup,
            "memory_reduction_percent": memory_reduction,
            "throughput_improvement_percent": throughput_improvement
        }
    }
    
    with open("comparison_report.json", "w") as f:
        json.dump(comparison, f, indent=2)
    
    print("\nComparison report saved to: comparison_report.json")
    print("=" * 60)


if __name__ == "__main__":
    # Run single benchmark
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    benchmark = GravitonBenchmark(model_name, use_quantization=True)
    results = benchmark.run_comprehensive_benchmark()
    
  

```
###### Analyze Results

```python
import json
import matplotlib.pyplot as plt
import numpy as np

def load_results(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def create_performance_report(results):
    """Generate a comprehensive performance report"""
    
    print("\n" + "=" * 60)
    print("PERFORMANCE ANALYSIS REPORT")
    print("=" * 60)
    
    # Latency Analysis
    print("\n1. LATENCY METRICS")
    print("-" * 40)
    latency = results["latency"]
    print(f"Average Latency:    {latency['avg_latency_sec']:.3f}s")
    print(f"Median (P50):       {latency['p50_latency_sec']:.3f}s")
    print(f"P95 Latency:        {latency['p95_latency_sec']:.3f}s")
    print(f"P99 Latency:        {latency['p99_latency_sec']:.3f}s")
    print(f"Std Deviation:      {latency['std_latency_sec']:.3f}s")
    print(f"Tokens/sec:         {latency['avg_tokens_per_sec']:.2f}")
    
    # Throughput Analysis
    print("\n2. THROUGHPUT METRICS")
    print("-" * 40)
    throughput = results["throughput"]
    print(f"Queries/sec:        {throughput['queries_per_sec']:.2f}")
    print(f"Avg Query Time:     {throughput['avg_time_per_query']:.3f}s")
    print(f"Total Tokens/sec:   {throughput['tokens_per_sec']:.2f}")
    
    # Resource Usage
    print("\n3. RESOURCE UTILIZATION")
    print("-" * 40)
    resources = results["resources"]
    print(f"Avg CPU Usage:      {resources['avg_cpu_percent']:.1f}%")
    print(f"Max CPU Usage:      {resources['max_cpu_percent']:.1f}%")
    print(f"Avg Memory:         {resources['avg_memory_gb']:.2f} GB")
    print(f"Max Memory:         {resources['max_memory_gb']:.2f} GB")
    
    # Scaling Analysis
    print("\n4. SCALING BEHAVIOR")
    print("-" * 40)
    scaling = results["scaling"]
    for item in scaling:
        efficiency = (item['tokens_per_sec'] / scaling[0]['tokens_per_sec']) * 100
        print(f"{item['requested_tokens']:3d} tokens: {item['time_sec']:6.2f}s | {item['tokens_per_sec']:5.1f} tok/s | {efficiency:5.1f}% efficiency")
    
    # System Info
    print("\n5. SYSTEM INFORMATION")
    print("-" * 40)
    metadata = results["metadata"]
    print(f"Model:              {metadata['model_name']}")
    print(f"Quantized:          {metadata['quantized']}")
    print(f"CPU Cores:          {metadata['cpu_count']}")
    print(f"Total RAM:          {metadata['total_memory_gb']:.1f} GB")
    
    print("\n" + "=" * 60)

def calculate_cost_efficiency(results, instance_cost_per_hour=0.145):
    """Calculate cost per 1000 queries"""
    
    queries_per_sec = results["throughput"]["queries_per_sec"]
    queries_per_hour = queries_per_sec * 3600
    cost_per_1000_queries = (instance_cost_per_hour / queries_per_hour) * 1000
    
    print("\n6. COST EFFICIENCY")
    print("-" * 40)
    print(f"Instance Cost:      ${instance_cost_per_hour}/hour")
    print(f"Queries/hour:       {queries_per_hour:,.0f}")
    print(f"Cost/1K queries:    ${cost_per_1000_queries:.4f}")
    print(f"Monthly (24/7):     ${instance_cost_per_hour * 24 * 30:.2f}")
    
    return cost_per_1000_queries

if __name__ == "__main__":
    # Load most recent benchmark results
    import glob
    
    files = glob.glob("benchmark_*.json")
    if not files:
        print("No benchmark results found. Run benchmark_suite.py first.")
        exit(1)
    
    latest_file = max(files, key=lambda x: os.path.getctime(x))
    print(f"Analyzing: {latest_file}\n")
    
    results = load_results(latest_file)
    create_performance_report(results)
    calculate_cost_efficiency(results)
```
