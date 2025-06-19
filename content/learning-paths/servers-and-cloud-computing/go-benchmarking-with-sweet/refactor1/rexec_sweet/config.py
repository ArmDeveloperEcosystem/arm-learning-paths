"""
Configuration management for rexec_sweet.
"""
import os
from typing import Dict, List, Optional

# ANSI color codes for visual differentiation
COLORS = {
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'reset': '\033[0m'
}

# Default benchmark configurations
DEFAULT_BENCHMARKS: Dict[str, str] = {
    "biogo-igor":    'sweet run -count 10 -run="biogo-igor" config.toml',
    "biogo-krishna": 'sweet run -count 10 -run="biogo-krishna" config.toml',
    "bleve-index":   'sweet run -count 10 -run="bleve-index" config.toml',
    "cockroachdb":   'sweet run -count 10 -run="cockroachdb" config.toml',
    "esbuild":       'sweet run -count 10 -run="esbuild" config.toml',
    "etcd":          'sweet run -count 10 -run="etcd" config.toml',
    "go-build":      'sweet run -count 10 -run="go-build" config.toml',
    "gopher-lua":    'sweet run -count 10 -run="gopher-lua" config.toml',
    "markdown":      'sweet run -count 10 -run="markdown" config.toml',
    "tile38":        'sweet run -count 10 -run="tile38" config.toml',
}

# Default remote directory for benchmarks
DEFAULT_REMOTE_DIR = "~/benchmarks/sweet"

# Default environment setup for remote execution
DEFAULT_ENV_SETUP = (
    "export GOPATH=$HOME/go; "
    "export GOBIN=$GOPATH/bin; "
    "export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
)

class Config:
    """Configuration manager for rexec_sweet."""
    
    def __init__(self):
        self.benchmarks = DEFAULT_BENCHMARKS.copy()
        self.default_benchmark = "markdown"
        self.results_dir = os.path.join(os.getcwd(), "results")
        self.env_setup = DEFAULT_ENV_SETUP
        
    def get_benchmark_command(self, benchmark_name: str) -> Optional[str]:
        """Get the command for a specific benchmark."""
        return self.benchmarks.get(benchmark_name)
        
    def get_benchmark_names(self) -> List[str]:
        """Get a sorted list of available benchmark names."""
        return sorted(self.benchmarks.keys())
        
    def get_results_dir(self, instance1: str, instance2: str, benchmark: str, timestamp: str) -> str:
        """Generate the results directory path."""
        os.makedirs(self.results_dir, exist_ok=True)
        subdir = f"{instance1}-{instance2}-{benchmark}-{timestamp}"
        result_dir = os.path.join(self.results_dir, subdir)
        os.makedirs(result_dir, exist_ok=True)
        return result_dir