"""
Tests for the config module.
"""
import os
import unittest
from unittest import mock

from rexec_sweet.config import Config

class TestConfig(unittest.TestCase):
    """Test cases for the Config class."""
    
    def test_init_default_values(self):
        """Test that Config initializes with default values."""
        config = Config()
        self.assertEqual(config.default_benchmark, "markdown")
        self.assertTrue("markdown" in config.benchmarks)
        self.assertTrue("go-build" in config.benchmarks)
        self.assertEqual(len(config.benchmarks), 11)  # Check all benchmarks are loaded
        
    def test_get_benchmark_command(self):
        """Test retrieving benchmark commands."""
        config = Config()
        # Test valid benchmark
        cmd = config.get_benchmark_command("markdown")
        self.assertEqual(cmd, 'sweet run -count 10 -run="markdown" config.toml')
        
        # Test invalid benchmark
        cmd = config.get_benchmark_command("nonexistent")
        self.assertIsNone(cmd)
        
    def test_get_benchmark_names(self):
        """Test getting sorted benchmark names."""
        config = Config()
        names = config.get_benchmark_names()
        self.assertEqual(len(names), 11)
        self.assertEqual(names[0], "biogo-igor")  # Should be alphabetically sorted
        self.assertEqual(names[-1], "tile38")
        
    def test_get_results_dir(self):
        """Test results directory creation."""
        config = Config()
        with mock.patch('os.makedirs') as mock_makedirs:
            result_dir = config.get_results_dir("inst1", "inst2", "bench", "20250101")
            # Check directory structure
            self.assertTrue(result_dir.endswith("inst1-inst2-bench-20250101"))
            # Check that makedirs was called twice (once for results dir, once for subdir)
            self.assertEqual(mock_makedirs.call_count, 2)

if __name__ == '__main__':
    unittest.main()