"""
Pytest configuration file.
"""
import os
import pytest
import tempfile

@pytest.fixture
def sample_benchstat_file():
    """Create a sample benchstat file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("name,c4-96.results,±,c4-64.results,±\n")
        f.write("BenchmarkTest1,100,10%,120,5%\n")
        f.write("BenchmarkTest2,200,5%,180,10%\n")
        f.write("\n")
        f.write("name,c4-96.results,±,c4-64.results,±\n")
        f.write("BenchmarkTest1,5,10%,4,5%\n")
        f.write("BenchmarkTest2,10,5%,8,10%\n")
        path = f.name
    
    yield path
    
    # Cleanup
    if os.path.exists(path):
        os.unlink(path)

@pytest.fixture
def temp_output_dir():
    """Create a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir