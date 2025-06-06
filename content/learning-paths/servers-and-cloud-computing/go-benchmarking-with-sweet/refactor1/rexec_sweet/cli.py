import os
import sys
import argparse
import tempfile
import threading
import subprocess
from datetime import datetime

from .gcp_utils import get_running_instances, choose_instance, get_instance_zone
from .benchmark_runner import BenchmarkRunner, BENCHMARKS

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run Sweet benchmarks on GCP instances")
    parser.add_argument("--benchmark", choices=list(BENCHMARKS.keys()), 
                        help="Benchmark to run")
    parser.add_argument("--instance1", help="First GCP instance name")
    parser.add_argument("--instance2", help="Second GCP instance name")
    parser.add_argument("--report", help="Generate report from benchstat file")
    parser.add_argument("--output-dir", help="Output directory for results")
    parser.add_argument("--debug", action="store_true", help="Show detailed error messages")
    return parser.parse_args()

def get_remote_path(instance_name):
    """Ask user for remote path, defaulting to ~/benchmarks/sweet"""
    default_path = "~/benchmarks/sweet"
    path = input(f"Enter remote path for {instance_name} [default: {default_path}]: ").strip()
    if not path:
        return default_path
    return path

def main():
    """Main entry point for the CLI."""
    args = parse_args()
    runner = BenchmarkRunner()
    
    try:
        if args.report:
            # Just generate a report from an existing benchstat file
            out_dir = args.output_dir or tempfile.mkdtemp()
            runner.run_benchstat_report(args.report, out_dir)
            return 0
        
        # Choose benchmark to run
        benchmark_name = args.benchmark
        if not benchmark_name:
            print("Available benchmarks:")
            for idx, name in enumerate(sorted(BENCHMARKS.keys()), 1):
                default_marker = " (default)" if name == "markdown" else ""
                print(f"{idx}. {name}{default_marker}")
            while True:
                choice = input(f"Enter number (1-{len(BENCHMARKS)}) [default: markdown]: ").strip()
                if not choice:  # Default to markdown
                    benchmark_name = "markdown"
                    break
                if choice.isdigit():
                    idx = int(choice)
                    if 1 <= idx <= len(BENCHMARKS):
                        benchmark_name = sorted(BENCHMARKS.keys())[idx-1]
                        break
                print("Invalid selection, try again.")
        
        systems = []
        
        # Get first instance to run on
        instance1_name = args.instance1
        if not instance1_name:
            print("\nSelect FIRST instance:")
            instances = get_running_instances()
            if not instances:
                print("Error: No running instances found.")
                return 1
            instance1_name = choose_instance(instances)
        
        # Get remote path for first instance
        remote_path1 = get_remote_path(instance1_name)
        zone1 = get_instance_zone(instance1_name)
        
        systems.append({
            "name": instance1_name,
            "zone": zone1,
            "bench": benchmark_name,
            "remote_dir": remote_path1,
            "cmd": BENCHMARKS[benchmark_name]
        })
        
        # Get second instance to run on
        instance2_name = args.instance2
        if not instance2_name:
            print("\nSelect SECOND instance:")
            instances = get_running_instances()
            if not instances:
                print("Error: No running instances found.")
                return 1
            instance2_name = choose_instance(instances)
        
        # Get remote path for second instance
        remote_path2 = get_remote_path(instance2_name)
        zone2 = get_instance_zone(instance2_name)
        
        systems.append({
            "name": instance2_name,
            "zone": zone2,
            "bench": benchmark_name,
            "remote_dir": remote_path2,
            "cmd": BENCHMARKS[benchmark_name]
        })
        
        # Create output directory
        timestamp = datetime.now().strftime('%Y%m%dT%H%M%S')
        local_root = os.path.join(os.getcwd(), "results")
        os.makedirs(local_root, exist_ok=True)
        subdir = f"{instance1_name}-{instance2_name}-{benchmark_name}-{timestamp}"
        local_dir = os.path.join(local_root, subdir)
        os.makedirs(local_dir, exist_ok=True)
        print(f"Output directory: {local_dir}")
        
        # Run benchmarks in parallel
        print("\nRunning benchmarks on the selected instances...")
        errors = []
        codes = {}
        threads = []
        
        for syscfg in systems:
            def run_and_store(syscfg=syscfg):
                idx = systems.index(syscfg)
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
        
        if errors:
            print("\n⚠️ Some benchmarks failed. Aborting benchstat step.")
            return 1
        
        # Identify primary and secondary systems
        primary = systems[1]
        secondary = systems[0]
        
        # Create a remote temp directory on the primary VM
        mktemp_cmd = [
            "gcloud", "compute", "ssh", primary["name"],
            "--zone", primary["zone"],
            "--command", "mktemp -d"
        ]
        remote_tmp = subprocess.check_output(mktemp_cmd, universal_newlines=True).strip()
        print(f"Created remote temp dir on {primary['name']}: {remote_tmp}")
        
        # Copy result files locally and push back to primary
        with tempfile.TemporaryDirectory() as tmp:
            local_sec = os.path.join(tmp, f"{secondary['name']}.results")
            print(f"Copying {secondary['name']} results to local: {local_sec}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                f"{secondary['name']}:{secondary['remote_dir']}/results/{benchmark_name}/*.results",
                local_sec,
                "--zone", secondary["zone"]
            ])
            
            local_prim = os.path.join(tmp, f"{primary['name']}.results")
            print(f"Copying {primary['name']} results to local: {local_prim}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                f"{primary['name']}:{primary['remote_dir']}/results/{benchmark_name}/*.results",
                local_prim,
                "--zone", primary["zone"]
            ])
            
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
        
        # Run benchstat on the primary VM
        benchstat_cmd = (
            f"benchstat -format csv "
            f"{remote_tmp}/{secondary['name']}.results "
            f"{remote_tmp}/{primary['name']}.results > {remote_tmp}/benchstat.results"
        )
        ls_cmd = (
            f"ls -al {remote_tmp}/{secondary['name']}.results "
            f"{remote_tmp}/{primary['name']}.results {remote_tmp}/benchstat.results"
        )
        ssh_cmd = [
            "gcloud", "compute", "ssh", primary["name"],
            "--zone", primary["zone"],
            "--command",
            (
                "export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; "
                "export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
                f"{benchstat_cmd} && echo \"Results files:\" && {ls_cmd}"
            )
        ]
        subprocess.check_call(ssh_cmd)
        
        # Pull all results back to local directory
        print(f"Please wait, copying over result files to local directory: {local_dir}")
        
        for fname in [
            f"{secondary['name']}.results",
            f"{primary['name']}.results",
            "benchstat.results"
        ]:
            subprocess.check_call([
                "gcloud", "compute", "scp",
                f"{primary['name']}:{remote_tmp}/{fname}",
                local_dir, "--zone", primary["zone"]
            ])
        
        # Generate report
        benchstat_file = os.path.join(local_dir, "benchstat.results")
        if os.path.exists(benchstat_file):
            runner.run_benchstat_report(benchstat_file, local_dir)
        else:
            print(f"Warning: Benchstat results file not found at {benchstat_file}")
        
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1