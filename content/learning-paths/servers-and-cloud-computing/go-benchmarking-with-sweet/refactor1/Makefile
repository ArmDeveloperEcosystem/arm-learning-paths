.PHONY: test test-cov install dev clean

# Install the package in development mode
install:
	pip install -e .

# Install development dependencies
dev:
	pip install -e ".[dev]"

# Run tests
test:
	pytest

# Run tests with coverage
test-cov:
	pytest --cov=rexec_sweet tests/

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete