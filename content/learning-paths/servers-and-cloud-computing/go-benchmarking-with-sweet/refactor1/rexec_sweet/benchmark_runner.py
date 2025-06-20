"""
Benchmark runner module for executing Sweet benchmarks on remote instances.
"""
import os
import subprocess
import sys
import threading
import webbrowser
from typing import Dict, List, Optional, Tuple

from .config import COLORS, Config

class BenchmarkRunner:
    """
    Handles running benchmarks and processing results.
    """
    def __init__(self):
        self.config = Config()
        self.reset = COLORS['reset']
        
    def run_benchstat_report(self, benchstat_file: str, output_dir: str) -> None:
        """
        Run benchstat report generation for the given benchstat_file into output_dir.
        """
        # Strip any '/tmp/tmp...' prefix from filenames when printing
        short_input = os.path.basename(benchstat_file)
        short_outdir = os.path.relpath(output_dir, start=os.getcwd())
        print(f"Generating report for {short_input}…")
        
        from .benchstat_report import BenchstatReport
        reporter = BenchstatReport()
        reporter.generate_report(benchstat_file, output_dir)
        
        print(f"Report generated in {short_outdir}")
        # Automatically open the generated report in the default web browser
        html_path = os.path.join(output_dir, 'report.html')
        abs_path = os.path.abspath(html_path)
        webbrowser.open(f"file://{abs_path}")
        
    def run_remote(self, name: str, zone: str, remote_dir: str, 
                  benchmark_name: str, color_idx: int = 0) -> int:
        """
        SSH to the instance and run the sweet benchmark, streaming output.
        
        Args:
            name: Instance name
            zone: GCP zone
            remote_dir: Remote directory path
            benchmark_name: Name of the benchmark to run
            color_idx: Index for color selection (0 or 1)
            
        Returns:
            Return code (0 for success, non-zero for failure)
        """
        benchmark_cmd = self.config.get_benchmark_command(benchmark_name)
        if not benchmark_cmd:
            print(f"Unknown benchmark: {benchmark_name}")
            return 1
            
        color = list(COLORS.values())[color_idx % 2]  # blue or green
        
        ssh_cmd = [
            "gcloud", "compute", "ssh", name,
            "--zone", zone,
            "--command",
            f"{self.config.env_setup} cd {remote_dir} && {benchmark_cmd}"
        ]
        
        p = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        def reader():
            for line in iter(p.stdout.readline, b""):
                sys.stdout.write(f"{color}[{name}]{self.reset} {line.decode()}")
                
        t = threading.Thread(target=reader, daemon=True)
        t.start()
        p.wait()
        
        if p.returncode != 0:
            print(f"[{name}] ⚠️ exited with code {p.returncode}")
        else:
            print(f"[{name}] ✅ benchmark completed")
            
        return p.returncode
        
    def run_benchmark(self, benchmark_name: str, instance_name: str, 
                     zone: str, remote_dir: str) -> bool:
        """
        Run a specific benchmark on a remote instance.
        
        Args:
            benchmark_name: Name of the benchmark to run
            instance_name: GCP instance name
            zone: GCP zone
            remote_dir: Remote directory path
            
        Returns:
            True if successful, False otherwise
        """
        # Create remote directory if needed
        ssh_cmd = [
            "gcloud", "compute", "ssh",
            instance_name,
            "--zone", zone,
            "--command", f"mkdir -p {remote_dir}"
        ]
        try:
            subprocess.check_call(ssh_cmd)
        except subprocess.CalledProcessError:
            print(f"Failed to create remote directory {remote_dir}")
            return False
            
        # Run the benchmark with Go environment setup
        color_idx = 0 if instance_name.endswith("1") else 1
        return self.run_remote(instance_name, zone, remote_dir, benchmark_name, color_idx) == 0
        
    def collect_results(self, primary: Dict, secondary: Dict, benchmark_name: str, 
                       local_dir: str) -> Optional[str]:
        """
        Collect benchmark results from both instances and run benchstat.
        
        Args:
            primary: Primary instance configuration
            secondary: Secondary instance configuration
            benchmark_name: Name of the benchmark
            local_dir: Local directory to store results
            
        Returns:
            Path to benchstat results file or None if failed
        """
        # Create a remote temp directory on the primary VM
        mktemp_cmd = [
            "gcloud", "compute", "ssh", primary["name"],
            "--zone", primary["zone"],
            "--command", "mktemp -d"
        ]
        try:
            remote_tmp = subprocess.check_output(mktemp_cmd, universal_newlines=True).strip()
            print(f"Created remote temp dir on {primary['name']}: {remote_tmp}")
        except subprocess.CalledProcessError:
            print(f"Failed to create temporary directory on {primary['name']}")
            return None
            
        # Copy result files locally and push back to primary
        try:
            self._transfer_result_files(primary, secondary, remote_tmp, benchmark_name)
        except subprocess.CalledProcessError as e:
            print(f"Failed to transfer result files: {e}")
            return None
            
        # Run benchstat on the primary VM
        try:
            self._run_benchstat(primary, secondary, remote_tmp)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run benchstat: {e}")
            return None
            
        # Pull all results back to local directory
        print(f"Please wait, copying over result files to local directory: {local_dir}")
        
        try:
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
        except subprocess.CalledProcessError as e:
            print(f"Failed to copy results to local directory: {e}")
            return None
            
        # Return path to benchstat results file
        benchstat_file = os.path.join(local_dir, "benchstat.results")
        if os.path.exists(benchstat_file):
            return benchstat_file
        else:
            print(f"Warning: Benchstat results file not found at {benchstat_file}")
            return None
            
    def _transfer_result_files(self, primary: Dict, secondary: Dict, 
                              remote_tmp: str, benchmark_name: str) -> None:
        """
        Transfer result files between instances.
        
        Args:
            primary: Primary instance configuration
            secondary: Secondary instance configuration
            remote_tmp: Remote temporary directory
            benchmark_name: Name of the benchmark
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            # Copy secondary results to local
            local_sec = os.path.join(tmp, f"{secondary['name']}.results")
            print(f"Copying {secondary['name']} results to local: {local_sec}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                f"{secondary['name']}:{secondary['remote_dir']}/results/{benchmark_name}/*.results",
                local_sec,
                "--zone", secondary["zone"]
            ])
            
            # Copy primary results to local
            local_prim = os.path.join(tmp, f"{primary['name']}.results")
            print(f"Copying {primary['name']} results to local: {local_prim}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                f"{primary['name']}:{primary['remote_dir']}/results/{benchmark_name}/*.results",
                local_prim,
                "--zone", primary["zone"]
            ])
            
            # Push secondary results to primary
            print(f"Pushing {secondary['name']} results to {primary['name']}:{remote_tmp}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                local_sec,
                f"{primary['name']}:{remote_tmp}/{secondary['name']}.results",
                "--zone", primary["zone"]
            ])
            
            # Push primary results to primary
            print(f"Pushing {primary['name']} results to {primary['name']}:{remote_tmp}")
            subprocess.check_call([
                "gcloud", "compute", "scp",
                local_prim,
                f"{primary['name']}:{remote_tmp}/{primary['name']}.results",
                "--zone", primary["zone"]
            ])
            
    def _run_benchstat(self, primary: Dict, secondary: Dict, remote_tmp: str) -> None:
        """
        Run benchstat on the primary VM.
        
        Args:
            primary: Primary instance configuration
            secondary: Secondary instance configuration
            remote_tmp: Remote temporary directory
        """
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
                f"{self.config.env_setup} "
                f"{benchstat_cmd} && echo \"Results files:\" && {ls_cmd}"
            )
        ]
        subprocess.check_call(ssh_cmd)