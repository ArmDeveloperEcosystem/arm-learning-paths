---
title: Installing the Automated Benchmark and Benchstat Runner
weight: 53

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the last section, you learned how to run benchmarks and benchstat manually. Now you'll learn how to run them automatically, with enhanced visualization of the results.

## Introducing rexec_sweet.py

The `rexec_sweet.py` script is a powerful automation tool that simplifies the benchmarking workflow.  This tool connects to your GCP instances, runs the benchmarks, collects the results, and generates comprehensive reports—all in one seamless operation. It provides several key benefits:

- **Automation**: Runs benchmarks on multiple VMs without manual SSH connections
- **Consistency**: Ensures benchmarks are executed with identical parameters
- **Visualization**: Generates HTML reports with interactive charts for easier analysis

The only dependency you are responsible for satisfying before the script runs is completion of the "Installing Go and Sweet" sections of this learning path.  Additional dependencies are dynamically loaded at install time by the install script.

## Setting up rexec_sweet

1. **Create a working directory:** On your local machine, open a terminal, then create and change into a directory to store the `rexec_sweet.py` script and related files:

   ```bash
   mkdir rexec_sweet
   cd rexec_sweet
   ```
   
2. **Clone the repository inside the directory:** Get the `rexec_sweet.py` script from the GitHub repository:

   ```bash
   git clone https://github.com/geremyCohen/go_benchmarks.git
   cd go_benchmarks
   ```

3. **Run the installer:** Copy and paste this command into your terminal to run the installer:

   ```bash
   ./install.sh
   ```

   If the install.sh script detects that you already have dependencies installed, it may ask you if you wish to reinstall them with the following prompt as shown:

   ```output
   pyenv: /Users/gercoh01/.pyenv/versions/3.9.22 already exists
   continue with installation? (y/N)
   ```

   If you see this prompt, enter `N` (not `Y`!) to continue with the installation without modifying the existing installed dependencies.

4. **Verify VM status:** Make sure the GCP VM instances you created in the previous section are running. If not, start them now, and give them a few minutes to come up.

{{% notice Note %}}
The install script will prompt you to authenticate with Google Cloud Platform (GCP) using the gcloud command-line tool at the end of install. If after installing you have issues running the script and/or get GCP authentication errors, you can manually authenticate with GCP by running the following command: `gcloud auth login`
{{% /notice %}}   


Continue on to the next section to run the script and see how it simplifies the benchmarking process.
