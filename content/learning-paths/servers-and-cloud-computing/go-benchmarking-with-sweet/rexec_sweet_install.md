---
title: Installing the Automated benchmark and benchstat runner
weight: 53

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the last section, you learned how to run benchmarks and benchstat manually.  In this section, you'll learn how to run them automatically, with enhanced visualization of the results.


## Introducing rexec_sweet.py

To make running benchmarks and `benchstat` easier, you can use the `rexec_sweet.py` script.  This script automates the process of running benchmarks on both your Arm-based and x86-based VMs, and then running `benchstat` to compare the results.

### Setting up the script

1. On your local machine, open a terminal, and create a directory to store the `rexec_sweet.py` script and related files. For example, you can create a directory called `rexec_sweet`:

```bash
mkdir rexec_sweet
cd rexec_sweet
```
   
2. Clone the `rexec_sweet.py` script from the GitHub repository:

```bash
git clone https://github.com/geremyCohen/go_benchmarks.git  
```

3. Copy and paste this code into your terminal to create the `rexec_sweet.py` file:

```bash
# Detect OS
OS=$(uname -s)

# Install based on detected OS
if [ "$OS" = "Darwin" ]; then
  echo "Detected macOS, installing with Homebrew..."
  
  # Update Homebrew
  brew update

  # Check and install required packages
  for package in pyenv virtualenv pyenv-virtualenv; do
    if which $package &>/dev/null || brew list $package &>/dev/null; then
      echo "$package is already installed"
    else
      echo "Installing $package..."
      brew install $package
    fi
  done
  
elif [ "$OS" = "Linux" ]; then
  echo "Detected Linux, installing with apt-get..."
  
  # Update package lists
  sudo apt-get -y update

  # Install dependencies
  sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git

  # Check if pyenv is already installed
  if which pyenv &>/dev/null; then
    echo "pyenv is already installed"
  else
    echo "Installing pyenv..."
    curl https://pyenv.run | bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
  fi
  
else
  echo "Unsupported operating system: $OS"
  echo "Please install pyenv manually for your system."
  exit 1
fi


# Install Python 3.9.22
pyenv install 3.9.22

# Create a virtualenv for this project
pyenv virtualenv 3.9.22 rexec-sweet-env

# Clone the repository and set the local pyenv version
git clone https://github.com/geremyCohen/go_benchmarks.git
cd go_benchmarks
pyenv local rexec-sweet-env

# Install from the project directory
pip install -e .


gcloud auth login
```

7. Make sure the instances you created in the previous section are running.  If not, start them now.

7. This script calls into the `gcloud` command to communicate with your running GCP instances.  To ensure you are authenticated with GCP so these calls can be authenticated, run the following command to authenticate your local machine with GCP:

Continue on to the next section to run the script.