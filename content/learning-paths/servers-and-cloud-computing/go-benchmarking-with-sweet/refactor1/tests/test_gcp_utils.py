"""
Tests for the gcp_utils module.
"""
import unittest
from unittest import mock
import sys
import subprocess
from io import StringIO

from rexec_sweet.gcp_utils import get_running_instances, choose_instance, get_instance_zone, scp_results

class TestGcpUtils(unittest.TestCase):
    """Test cases for GCP utility functions."""
    
    @mock.patch('subprocess.check_output')
    def test_get_running_instances_success(self, mock_check_output):
        """Test getting running instances when successful."""
        mock_check_output.return_value = "instance1\ninstance2\n"
        instances = get_running_instances()
        self.assertEqual(instances, ["instance1", "instance2"])
        mock_check_output.assert_called_once()
        
    @mock.patch('subprocess.check_output')
    def test_get_running_instances_error(self, mock_check_output):
        """Test getting running instances when command fails."""
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "cmd")
        instances = get_running_instances()
        self.assertEqual(instances, [])
        
    @mock.patch('builtins.input')
    def test_choose_instance(self, mock_input):
        """Test instance selection."""
        instances = ["instance1", "instance2", "instance3"]
        mock_input.return_value = "2"
        selected = choose_instance(instances)
        self.assertEqual(selected, "instance2")
        
    @mock.patch('builtins.input')
    def test_choose_instance_invalid_then_valid(self, mock_input):
        """Test instance selection with initial invalid input."""
        instances = ["instance1", "instance2"]
        mock_input.side_effect = ["3", "abc", "1"]
        selected = choose_instance(instances)
        self.assertEqual(selected, "instance1")
        self.assertEqual(mock_input.call_count, 3)
        
    @mock.patch('subprocess.check_output')
    def test_get_instance_zone(self, mock_check_output):
        """Test getting instance zone."""
        mock_check_output.return_value = "us-central1-a\n"
        zone = get_instance_zone("instance1")
        self.assertEqual(zone, "us-central1-a")
        
    @mock.patch('subprocess.check_output')
    @mock.patch('sys.exit')
    def test_get_instance_zone_error(self, mock_exit, mock_check_output):
        """Test error handling when getting instance zone."""
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "cmd")
        get_instance_zone("instance1")
        mock_exit.assert_called_once_with(1)
        
    @mock.patch('subprocess.check_call')
    def test_scp_results_success(self, mock_check_call):
        """Test successful SCP operation."""
        result = scp_results("instance1", "us-central1-a", "remote/path/*.results", "local/path")
        self.assertTrue(result)
        mock_check_call.assert_called_once()
        
    @mock.patch('subprocess.check_call')
    def test_scp_results_failure(self, mock_check_call):
        """Test failed SCP operation."""
        mock_check_call.side_effect = subprocess.CalledProcessError(1, "cmd")
        result = scp_results("instance1", "us-central1-a", "remote/path/*.results", "local/path")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()