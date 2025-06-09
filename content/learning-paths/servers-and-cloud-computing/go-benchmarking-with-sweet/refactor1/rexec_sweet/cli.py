"""
Command-line interface for rexec_sweet.
"""
import os
import sys
import argparse
import tempfile
import threading
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from .gcp_utils import get_running_instances, choose_instance, get_instance_zone
from .benchmark_runner import BenchmarkRunner
from .config import Config

def parse_args():
    """Parse command line arguments."""
    config = Config()
    parser = argparse.ArgumentParser(description="Run Sweet benchmarks on GCP instances")
    parser.add_argument("--benchmark", choices=config.get_benchmark_names(), 
                        help="Benchmark to run")
    parser.add_argument("--instance1", help="First GCP instance name")
    parser.add_argument("--instance2", help="Second GCP instance name")
    parser.add_argument("--report", help="Generate report from benchstat file")
    parser.add_argument("--output-dir", help="Output directory for results")
    parser.add_argument("--debug", action="store_true", help="Show detailed error messages")
    return parser.parse_args()

def get_remote_path(instance_name: str) -> str:
    """Ask user for remote path, defaulting to ~/benchmarks/sweet"""
    default_path = "~/benchmarks/sweet"
    path = input(f"Enter remote path for {instance_name} [default: {default_path}]: ").strip()
    if not path:
        return default_path
    return path

def select_benchmark(config: Config) -> str:
    """Prompt user to select a benchmark."""
    print("Available benchmarks:")
    benchmark_names = config.get_benchmark_names()
    for idx, name in enumerate(benchmark_names, 1):
        default_marker = " (default)" if name == config.default_benchmark else ""
        print(f"{idx}. {name}{default_marker}")
        
    while True:
        choice = input(f"Enter number (1-{len(benchmark_names)}) [default: {config.default_benchmark}]: ").strip()
        if not choice:  # Default
            return config.default_benchmark
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(benchmark_names):
                return benchmark_names[idx-1]
        print("Invalid selection, try again.")

def select_instance(prompt_text: str, instance_name: Optional[str] = None) -> Tuple[str, str, str]:
    """
    Select an instance and get its zone and remote path.
    
    Args:
        prompt_text: Text to display when prompting for instance selection
        instance_name: Optional pre-selected instance name
        
    Returns:
        Tuple of (instance_name, zone, remote_path)
    """
    if not instance_name:
        print(f"\n{prompt_text}:")
        instances = get_running_instances()
        if not instances:
            print("Error: No running instances found.")
            sys.exit(1)
        instance_name = choose_instance(instances)
    
    # Get remote path and zone
    remote_path = get_remote_path(instance_name)
    zone = get_instance_zone(instance_name)
    
    return instance_name, zone, remote_path

def use_default_instances() -> bool:
    """Ask if user wants to use the first two instances with default directories."""
    choice = input("\nDo you want to run the first two instances found with default install directories? [Y/n]: ").strip().lower()
    return choice == "" or choice == "y"

def get_default_instances() -> List[Tuple[str, str, str]]:
    """Get the first two instances with default directories."""
    instances = get_running_instances()
    if len(instances) < 2:
        print("Error: Need at least two running instances.")
        sys.exit(1)
        
    default_path = "~/benchmarks/sweet"
    result = []
    
    for i in range(2):
        instance_name = instances[i]
        zone = get_instance_zone(instance_name)
        result.append((instance_name, zone, default_path))
        
    print(f"\nUsing instances: {instances[0]} and {instances[1]} with default path: {default_path}")
    return result

def run_benchmarks_parallel(runner: BenchmarkRunner, systems: List[Dict]) -> List[str]:
    """
    Run benchmarks in parallel on multiple systems.
    
    Args:
        runner: BenchmarkRunner instance
        systems: List of system configurations
        
    Returns:
        List of systems that failed
    """
    print("\nRunning benchmarks on the selected instances...")
    errors = []
    codes = {}
    threads = []
    
    for syscfg in systems:
        def run_and_store(syscfg=syscfg):
            code = runner.run_benchmark(
                syscfg["bench"],
                syscfg["name"],
                syscfg["zone"],
                syscfg["remote_dir"]
            )
            codes[syscfg["name"]] = 0 if code else 1
        
        t = threading.Thread(target=run_and_store, daemon=True)
        t.start()
        threads.append(t)
    
    # Wait for benchmarks to finish
    for t in threads:
        t.join()
    
    # Collect failures
    for name, code in codes.items():
        if code != 0:
            errors.append(name)
            
    return errors

def main():
    """Main entry point for the CLI."""
    args = parse_args()
    runner = BenchmarkRunner()
    config = Config()
    
    try:
        # Just generate a report from an existing benchstat file
        if args.report:
            out_dir = args.output_dir or tempfile.mkdtemp()
            runner.run_benchstat_report(args.report, out_dir)
            return 0
        
        # Choose benchmark to run
        benchmark_name = args.benchmark or select_benchmark(config)
        
        # Setup systems for benchmarking
        systems = []
        
        # Check if user wants to use default instances
        if not args.instance1 and not args.instance2 and use_default_instances():
            # Get the first two instances with default directories
            instance_configs = get_default_instances()
            
            for instance_name, zone, remote_path in instance_configs:
                systems.append({
                    "name": instance_name,
                    "zone": zone,
                    "bench": benchmark_name,
                    "remote_dir": remote_path
                })
        else:
            # Get first instance
            instance1_name, zone1, remote_path1 = select_instance(
                "Select FIRST instance", args.instance1)
            
            systems.append({
                "name": instance1_name,
                "zone": zone1,
                "bench": benchmark_name,
                "remote_dir": remote_path1
            })
            
            # Get second instance
            instance2_name, zone2, remote_path2 = select_instance(
                "Select SECOND instance", args.instance2)
            
            systems.append({
                "name": instance2_name,
                "zone": zone2,
                "bench": benchmark_name,
                "remote_dir": remote_path2
            })
        
        # Create output directory
        timestamp = datetime.now().strftime('%Y%m%dT%H%M%S')
        local_dir = config.get_results_dir(systems[0]["name"], systems[1]["name"], benchmark_name, timestamp)
        print(f"Output directory: {local_dir}")
        
        # Run benchmarks in parallel
        errors = run_benchmarks_parallel(runner, systems)
        
        if errors:
            print("\n⚠️ Some benchmarks failed. Aborting benchstat step.")
            return 1
        
        # Identify primary and secondary systems
        primary = systems[1]
        secondary = systems[0]
        
        # Collect results and run benchstat
        benchstat_file = runner.collect_results(primary, secondary, benchmark_name, local_dir)
        
        # Generate report
        if benchstat_file:
            runner.run_benchstat_report(benchstat_file, local_dir)
        
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())