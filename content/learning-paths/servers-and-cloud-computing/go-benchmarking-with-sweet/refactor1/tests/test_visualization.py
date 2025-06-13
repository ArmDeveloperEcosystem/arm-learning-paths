"""
Tests for the visualization module.
"""
import os
import unittest
import tempfile
import pandas as pd
from unittest import mock
from io import StringIO

from rexec_sweet.visualization import (
    wrap_label, make_bar_chart, parse_benchstat, 
    plot_metric_group, generate_html
)

class TestVisualization(unittest.TestCase):
    """Test cases for visualization functions."""
    
    def test_wrap_label(self):
        """Test label wrapping function."""
        # Test simple label
        result = wrap_label("simple")
        self.assertEqual(result, "simple")
        
        # Test label with slashes
        result = wrap_label("category/subcategory/name")
        self.assertEqual(result, "category<br>subcategory<br>name")
        
        # Test long label that needs wrapping
        result = wrap_label("this_is_a_very_long_label_that_needs_wrapping", width=10)
        self.assertTrue("<br>" in result)
        self.assertTrue(len(result.split("<br>")[0]) <= 10)
    
    @mock.patch('plotly.graph_objs.Figure.write_html')
    def test_make_bar_chart(self, mock_write_html):
        """Test bar chart generation."""
        output_path = "/tmp/chart.html"
        
        # Create a simple chart
        result = make_bar_chart(
            x_labels=["Test1", "Test2"],
            y1=[1.0, 2.0],
            y2=[1.5, 2.5],
            name1="System A",
            name2="System B",
            title="Test Chart",
            xaxis_title="Tests",
            yaxis_title="Values",
            out_path=output_path
        )
        
        # Verify mock was called
        mock_write_html.assert_called_once()
        self.assertEqual(result, output_path)
    
    def test_parse_benchstat(self):
        """Test parsing benchstat CSV output."""
        # Use the mock data file
        mock_file = os.path.join(os.path.dirname(__file__), "mock_data", "benchstat.csv")
        
        # Parse the file
        groups = parse_benchstat(mock_file)
        
        # Verify results
        self.assertEqual(len(groups), 2)  # Two groups
        inst_a, inst_b, metric_name, df = groups[0]
        self.assertEqual(inst_a, "c4")
        self.assertEqual(inst_b, "c4")
    
    @mock.patch('rexec_sweet.visualization.make_bar_chart')
    def test_plot_metric_group(self, mock_make_bar_chart):
        """Test plotting a metric group."""
        # Create test data with the correct column name
        df = pd.DataFrame({
            'name': ['Test1', 'Test2'],  # This should be 'name' not 'Benchmark'
            'c4-96.results': [100, 200],
            '±': ['10%', '5%'],
            'c4-64.results': [120, 180],
            '±.1': ['5%', '10%']
        })
        
        # Rename 'name' to 'Benchmark' as the function expects
        df = df.rename(columns={'name': 'Benchmark'})
        
        mock_make_bar_chart.return_value = "/tmp/chart.html"
        
        # Plot the data
        result = plot_metric_group("c4-96", "c4-64", "time/op", df, "/tmp", 0)
        
        # Verify results
        self.assertEqual(result, "/tmp/chart.html")
        mock_make_bar_chart.assert_called_once()
    
    def test_generate_html(self):
        """Test HTML report generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test data
            images = [
                (os.path.join(tmpdir, "chart1.html"), "time/op", "c4-96", "c4-64"),
                (os.path.join(tmpdir, "chart2.html"), "alloc/op", "c4-96", "c4-64")
            ]
            
            # Create dummy image files
            for img_path, _, _, _ in images:
                with open(img_path, "w") as f:
                    f.write("<html></html>")
            
            # Generate the report
            result = generate_html(images, tmpdir)
            
            # Verify results
            self.assertTrue(os.path.exists(result))
            self.assertEqual(result, os.path.join(tmpdir, "report.html"))
            
            # Check content
            with open(result, "r") as f:
                content = f.read()
                self.assertTrue("<h1>Benchmark Comparison Report</h1>" in content)
                self.assertTrue("time/op" in content)
                self.assertTrue("alloc/op" in content)

if __name__ == '__main__':
    unittest.main()