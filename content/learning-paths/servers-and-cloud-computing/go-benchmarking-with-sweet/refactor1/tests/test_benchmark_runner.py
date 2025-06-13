"""
Tests for the benchmark_runner module.
"""
import os
import unittest
from unittest import mock
import subprocess
import tempfile

from rexec_sweet.benchmark_runner import BenchmarkRunner

class TestBenchmarkRunner(unittest.TestCase):
    """Test cases for the BenchmarkRunner class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runner = BenchmarkRunner()
        
    def test_init(self):
        """Test initialization."""
        self.assertIsNotNone(self.runner.config)
        
    @mock.patch('subprocess.check_call')
    def test_run_benchmark_success(self, mock_check_call):
        """Test successful benchmark run."""
        # Mock the run_remote method to return success
        with mock.patch.object(self.runner, 'run_remote', return_value=0) as mock_run:
            result = self.runner.run_benchmark("markdown", "instance1", "us-central1-a", "~/benchmarks")
            self.assertTrue(result)
            mock_run.assert_called_once()
            
    @mock.patch('subprocess.check_call')
    def test_run_benchmark_failure_mkdir(self, mock_check_call):
        """Test benchmark run with mkdir failure."""
        mock_check_call.side_effect = subprocess.CalledProcessError(1, "cmd")
        result = self.runner.run_benchmark("markdown", "instance1", "us-central1-a", "~/benchmarks")
        self.assertFalse(result)
        
    @mock.patch('subprocess.check_call')
    def test_run_benchmark_failure_run(self, mock_check_call):
        """Test benchmark run with execution failure."""
        # Mock the run_remote method to return failure
        with mock.patch.object(self.runner, 'run_remote', return_value=1) as mock_run:
            result = self.runner.run_benchmark("markdown", "instance1", "us-central1-a", "~/benchmarks")
            self.assertFalse(result)
            
    @mock.patch('subprocess.Popen')
    def test_run_remote(self, mock_popen):
        """Test remote command execution."""
        # Setup mock process
        mock_process = mock.MagicMock()
        mock_process.returncode = 0
        mock_process.stdout.readline.side_effect = [b"output line 1", b"output line 2", b""]
        mock_popen.return_value = mock_process
        
        # Run the method
        result = self.runner.run_remote("instance1", "us-central1-a", "~/benchmarks", "markdown", 0)
        
        # Verify results
        self.assertEqual(result, 0)
        mock_popen.assert_called_once()
        
    @mock.patch('webbrowser.open')
    @mock.patch('rexec_sweet.benchstat_report.BenchstatReport.generate_report')
    def test_run_benchstat_report(self, mock_generate, mock_browser):
        """Test benchstat report generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a dummy benchstat file
            benchstat_file = os.path.join(tmpdir, "benchstat.results")
            with open(benchstat_file, "w") as f:
                f.write("dummy data")
                
            # Run the method
            self.runner.run_benchstat_report(benchstat_file, tmpdir)
            
            # Verify results
            mock_generate.assert_called_once_with(benchstat_file, tmpdir)
            mock_browser.assert_called_once()
            
    @mock.patch('subprocess.check_output')
    @mock.patch('subprocess.check_call')
    def test_collect_results_success(self, mock_check_call, mock_check_output):
        """Test successful results collection."""
        # Setup mocks
        mock_check_output.return_value = "/tmp/remote_dir\n"
        
        # Setup test data
        primary = {"name": "instance1", "zone": "us-central1-a", "remote_dir": "~/benchmarks"}
        secondary = {"name": "instance2", "zone": "us-central1-b", "remote_dir": "~/benchmarks"}
        
        # Mock the transfer and benchstat methods
        with mock.patch.object(self.runner, '_transfer_result_files') as mock_transfer:
            with mock.patch.object(self.runner, '_run_benchstat') as mock_benchstat:
                with mock.patch('os.path.exists', return_value=True):
                    result = self.runner.collect_results(primary, secondary, "markdown", "/tmp/local_dir")
                    
                    # Verify results
                    self.assertIsNotNone(result)
                    mock_transfer.assert_called_once()
                    mock_benchstat.assert_called_once()

if __name__ == '__main__':
    unittest.main()