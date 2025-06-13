"""
Tests for the CLI module.
"""
import unittest
from unittest import mock
import argparse
import sys
import tempfile

from rexec_sweet.cli import parse_args, get_remote_path, select_benchmark, select_instance, run_benchmarks_parallel, main

class TestCLI(unittest.TestCase):
    """Test cases for CLI functions."""
    
    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_parse_args(self, mock_parse_args):
        """Test argument parsing."""
        # Setup mock return value
        args = argparse.Namespace(
            benchmark="markdown",
            instance1="instance1",
            instance2="instance2",
            report=None,
            output_dir=None,
            debug=False
        )
        mock_parse_args.return_value = args
        
        # Call the function
        result = parse_args()
        
        # Verify results
        self.assertEqual(result.benchmark, "markdown")
        self.assertEqual(result.instance1, "instance1")
        self.assertEqual(result.instance2, "instance2")
        
    @mock.patch('builtins.input')
    def test_get_remote_path_default(self, mock_input):
        """Test getting remote path with default value."""
        mock_input.return_value = ""
        path = get_remote_path("instance1")
        self.assertEqual(path, "~/benchmarks/sweet")
        
    @mock.patch('builtins.input')
    def test_get_remote_path_custom(self, mock_input):
        """Test getting remote path with custom value."""
        mock_input.return_value = "/custom/path"
        path = get_remote_path("instance1")
        self.assertEqual(path, "/custom/path")
        
    @mock.patch('builtins.input')
    def test_select_benchmark_default(self, mock_input):
        """Test benchmark selection with default."""
        from rexec_sweet.config import Config
        config = Config()
        mock_input.return_value = ""
        
        benchmark = select_benchmark(config)
        self.assertEqual(benchmark, "markdown")
        
    @mock.patch('builtins.input')
    def test_select_benchmark_by_number(self, mock_input):
        """Test benchmark selection by number."""
        from rexec_sweet.config import Config
        config = Config()
        mock_input.return_value = "1"  # First benchmark in sorted list
        
        benchmark = select_benchmark(config)
        self.assertEqual(benchmark, config.get_benchmark_names()[0])
        
    @mock.patch('rexec_sweet.cli.get_running_instances')
    @mock.patch('rexec_sweet.cli.choose_instance')
    @mock.patch('rexec_sweet.cli.get_instance_zone')
    @mock.patch('builtins.input')
    def test_select_instance(self, mock_input, mock_zone, mock_choose, mock_instances):
        """Test instance selection."""
        # Setup mocks
        mock_instances.return_value = ["instance1", "instance2"]
        mock_choose.return_value = "instance1"
        mock_zone.return_value = "us-central1-a"
        mock_input.return_value = ""  # Default path
        
        # Call with no pre-selected instance
        name, zone, path = select_instance("Select instance")
        
        # Verify results
        self.assertEqual(name, "instance1")
        self.assertEqual(zone, "us-central1-a")
        self.assertEqual(path, "~/benchmarks/sweet")
        
        # Call with pre-selected instance
        name, zone, path = select_instance("Select instance", "instance2")
        
        # Verify results
        self.assertEqual(name, "instance2")
        self.assertEqual(zone, "us-central1-a")
        mock_choose.assert_called_once()  # Should only be called in the first test
        
    @mock.patch('threading.Thread')
    def test_run_benchmarks_parallel(self, mock_thread):
        """Test parallel benchmark execution."""
        # Setup mock
        mock_thread_instance = mock.MagicMock()
        mock_thread.return_value = mock_thread_instance
        
        # Setup test data
        runner = mock.MagicMock()
        runner.run_benchmark.return_value = True  # Success
        
        systems = [
            {"name": "instance1", "zone": "us-central1-a", "bench": "markdown", "remote_dir": "~/benchmarks"},
            {"name": "instance2", "zone": "us-central1-b", "bench": "markdown", "remote_dir": "~/benchmarks"}
        ]
        
        # Run the function
        errors = run_benchmarks_parallel(runner, systems)
        
        # Verify results
        self.assertEqual(len(errors), 0)  # No errors
        self.assertEqual(mock_thread.call_count, 2)  # Two threads created
        self.assertEqual(mock_thread_instance.start.call_count, 2)  # Both threads started
        self.assertEqual(mock_thread_instance.join.call_count, 2)  # Both threads joined
        
    @mock.patch('rexec_sweet.cli.parse_args')
    @mock.patch('rexec_sweet.cli.select_benchmark')
    @mock.patch('rexec_sweet.cli.select_instance')
    @mock.patch('rexec_sweet.cli.run_benchmarks_parallel')
    def test_main_success(self, mock_run, mock_select_instance, mock_select_benchmark, mock_parse_args):
        """Test successful main execution."""
        # Setup mocks
        args = argparse.Namespace(
            benchmark=None,
            instance1=None,
            instance2=None,
            report=None,
            output_dir=None,
            debug=False
        )
        mock_parse_args.return_value = args
        mock_select_benchmark.return_value = "markdown"
        mock_select_instance.side_effect = [
            ("instance1", "us-central1-a", "~/benchmarks"),
            ("instance2", "us-central1-b", "~/benchmarks")
        ]
        mock_run.return_value = []  # No errors
        
        # Mock the BenchmarkRunner
        with mock.patch('rexec_sweet.cli.BenchmarkRunner') as mock_runner_class:
            mock_runner = mock.MagicMock()
            mock_runner_class.return_value = mock_runner
            mock_runner.collect_results.return_value = "/tmp/benchstat.results"
            
            # Run main
            result = main()
            
            # Verify results
            self.assertEqual(result, 0)  # Success
            mock_runner.run_benchstat_report.assert_called_once()
            
    @mock.patch('rexec_sweet.cli.parse_args')
    def test_main_report_only(self, mock_parse_args):
        """Test main with report-only mode."""
        # Setup mocks
        args = argparse.Namespace(
            benchmark=None,
            instance1=None,
            instance2=None,
            report="/tmp/benchstat.results",
            output_dir=None,
            debug=False
        )
        mock_parse_args.return_value = args
        
        # Mock the BenchmarkRunner
        with mock.patch('rexec_sweet.cli.BenchmarkRunner') as mock_runner_class:
            mock_runner = mock.MagicMock()
            mock_runner_class.return_value = mock_runner
            
            # Run main
            result = main()
            
            # Verify results
            self.assertEqual(result, 0)  # Success
            mock_runner.run_benchstat_report.assert_called_once()
            # Should not call other methods
            mock_runner.run_benchmark.assert_not_called()
            mock_runner.collect_results.assert_not_called()

if __name__ == '__main__':
    unittest.main()