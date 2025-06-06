import os
import subprocess
import webbrowser
import threading
import sys

# ANSI color codes for visual differentiation
COLORS = ['\033[94m', '\033[92m']  # blue, green
RESET = '\033[0m'

# map benchmark name → sweet command fragment
BENCHMARKS = {
    "biogo-igor":    'sweet run -count 10 -run="biogo-igor" config.toml',
    "biogo-krishna": 'sweet run -count 10 -run="biogo-krishna" config.toml',
    "bleve-index":   'sweet run -count 10 -run="bleve-index" config.toml',
    "cockroachdb":   'sweet run -count 10 -run="cockroachdb" config.toml',
    "esbuild":       'sweet run -count 10 -run="esbuild" config.toml',
    "etcd":          'sweet run -count 10 -run="etcd" config.toml',
    "go-build":      'sweet run -count 10 -run="go-build" config.toml',
    "gopher-lua":    'sweet run -count 10 -run="gopher-lua" config.toml',
    "gvisor":        'sweet run -count 10 -run="gvisor" config.toml',
    "markdown":      'sweet run -count 10 -run="markdown" config.toml',
    "tile38":        'sweet run -count 10 -run="tile38" config.toml',
}

class BenchmarkRunner:
    """
    Handles running benchmarks and processing results.
    """
    def __init__(self):
        self.cached_instances = None
        
    def run_benchstat_report(self, benchstat_file, selected_dir):
        """
        Run benchstat report generation for the given benchstat_file into selected_dir.
        """
        # Strip any '/tmp/tmp...' prefix from filenames when printing
        short_input = os.path.basename(benchstat_file)
        short_outdir = os.path.relpath(selected_dir, start=os.getcwd())
        print(f"Generating report for {short_input}…")
        
        from .benchstat_report import BenchstatReport
        reporter = BenchstatReport()
        reporter.generate_report(benchstat_file, selected_dir)
        
        print(f"Report generated in {short_outdir}")
        # Automatically open the generated report in the default web browser
        html_path = os.path.join(selected_dir, 'report.html')
        abs_path = os.path.abspath(html_path)
        webbrowser.open(f"file://{abs_path}")
        
    def run_remote(self, name, zone, remote_dir, sweet_cmd, color):
        """
        SSH to the instance and run the sweet benchmark, streaming output.
        """
        ssh_cmd = [
            "gcloud", "compute", "ssh", name,
            "--zone", zone,
            "--command",
            f"export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; "
            f"export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
            f"cd {remote_dir} && {sweet_cmd}"
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
        
    def run_benchmark(self, benchmark_name, instance_name, zone, remote_dir):
        """Run a specific benchmark on a remote instance."""
        if benchmark_name not in BENCHMARKS:
            print(f"Unknown benchmark: {benchmark_name}")
            print(f"Available benchmarks: {', '.join(BENCHMARKS.keys())}")
            return False
            
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
        cmd = BENCHMARKS[benchmark_name]
        color_idx = 0 if instance_name.endswith("1") else 1
        color = COLORS[color_idx % len(COLORS)]
        return self.run_remote(instance_name, zone, remote_dir, cmd, color) == 0