from setuptools import setup, find_packages

setup(
    name="rexec_sweet",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=2.0.0",
        "pandas>=2.3.0",
        "plotly>=5.13.0",
    ],
    entry_points={
        "console_scripts": [
            "rexec-sweet=rexec_sweet.cli:main",
        ],
    },
    python_requires=">=3.8",
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
)