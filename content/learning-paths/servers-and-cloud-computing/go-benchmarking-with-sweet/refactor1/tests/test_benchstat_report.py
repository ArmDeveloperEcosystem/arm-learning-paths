"""
Tests for the benchstat_report module.
"""
import os
import unittest
from unittest import mock
import tempfile

from rexec_sweet.benchstat_report import BenchstatReport

class TestBenchstatReport(unittest.TestCase):
    """Test cases for the BenchstatReport class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.reporter = BenchstatReport()
        
    def test_generate_report_success(self):
        """Test successful report generation."""
        with tempfile.TemporaryDirectory() as output_dir:
            # Create a real test file
            test_file = os.path.join(output_dir, "benchstat.csv")
            with open(test_file, "w") as f:
                f.write("name,c4-96.results,±,c4-64.results,±\n")
                f.write("BenchmarkTest1,100,10%,120,5%\n")
                f.write("BenchmarkTest2,200,5%,180,10%\n")
            
            # Mock the functions that would process the file
            with mock.patch('rexec_sweet.benchstat_report.parse_benchstat') as mock_parse, \
                 mock.patch('rexec_sweet.benchstat_report.plot_metric_group') as mock_plot, \
                 mock.patch('rexec_sweet.benchstat_report.generate_html') as mock_generate_html:
                
                # Setup mock return values
                mock_parse.return_value = [
                    ("c4-96", "c4-64", "time/op", mock.MagicMock()),
                    ("c4-96", "c4-64", "alloc/op", mock.MagicMock())
                ]
                mock_plot.side_effect = [
                    os.path.join(output_dir, "chart1.html"),
                    os.path.join(output_dir, "chart2.html")
                ]
                
                # Run the method with the real file
                result = self.reporter.generate_report(test_file, output_dir)
                
                # Verify the length of the result matches the number of charts
                self.assertEqual(len(result), 2)
            
    def test_generate_report_file_not_found(self):
        """Test report generation with missing file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Use a non-existent file
            benchstat_file = os.path.join(tmpdir, "nonexistent.results")
            
            # Run the method
            result = self.reporter.generate_report(benchstat_file, tmpdir)
            
            # Verify results
            self.assertEqual(result, [])  # Empty result

if __name__ == '__main__':
    unittest.main()