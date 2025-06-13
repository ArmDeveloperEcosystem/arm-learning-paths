"""
Remote execution tool for Sweet Go benchmarking.
"""
from .benchstat_report import BenchstatReport
from .gcp_utils import get_running_instances, choose_instance, get_instance_zone, scp_results
from .benchmark_runner import BenchmarkRunner
from .visualization import generate_html
from .config import Config

__version__ = "0.1.0"

__all__ = [
    'BenchstatReport',
    'get_running_instances',
    'choose_instance',
    'get_instance_zone',
    'scp_results',
    'BenchmarkRunner',
    'generate_html',
    'Config',
]