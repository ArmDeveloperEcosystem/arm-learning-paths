---
title: PHP Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## PHP Benchmarking using PHPBench

In this section, we will be focussing on PHP benchmarking using PHPBench, running sample benchmarks, interpreting key metrics like mode time and variation, and analyzing performance results for string and array operations on the GCP Arm VM.

PHPBench is a powerful benchmarking framework for PHP, designed to measure the performance of PHP code and functions. It helps developers identify bottlenecks, compare execution times, and optimize code efficiency by running repeatable, accurate benchmarks. Using PHPBench, you can track performance changes over time and ensure consistent PHP application performance.

### Download Composer Installer

Composer is a tool for managing PHP packages. First, download the installer:

```console
sudo php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
```

This command downloads a PHP script called composer-setup.php, which will install Composer.

### Install the phar extension

Composer requires PHP’s phar extension. You need to install it using following command:

```console
sudo zypper install -y php8-phar
```

`phar` allows PHP to run archive files (.phar) like Composer.

### Install Composer system-wide

Run the installer to make Composer available for all users:

```console
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```

This installs Composer to /usr/local/bin/composer.

### Remove the installer script

```console
sudo php -r "unlink('composer-setup.php');"
```
Delete the installer file after successful installation.

### Verify Composer installation

```console
composer --version
```
You should see output similar to:
```output
Composer version 2.8.12 2025-09-19 13:41:59
PHP version 8.0.30 (/usr/bin/php)
Run the "diagnose" command to get more detailed diagnostics output.
```

### Install PHPBench globally

PHPBench is a benchmarking tool for PHP. Install it globally via Composer:

```console
composer global require phpbench/phpbench
```

This installs `phpbench` in your user’s Composer folder.

### Add Composer global bin to PATH

Make sure PHPBench is accessible:

```console
export PATH="$HOME/.config/composer/vendor/bin:$PATH"
echo 'export PATH=$HOME/.config/composer/vendor/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
This ensures the `phpbench` command works whenever you open a terminal.

### Verify PHPBench installation

```console
phpbench --version
```

You should see output similar to:
```output
phpbench 1.2.14
```

### Create a Benchmark Directory

Create a folder to hold all your benchmark scripts:

```console
mkdir ~/phpbench-tests
cd ~/phpbench-tests
```
### Create a Benchmark Script

Create a new PHP benchmark file using your preferred editor:

```console
vi ExampleBenchmark.php
```
Then, add the following content to define your benchmark tests:
```php
<?php

use PhpBench\Benchmark\Metadata\Annotations\Iterations;
use PhpBench\Benchmark\Metadata\Annotations\Revs;

/**
 * @Revs(1000)
 * @Iterations(5)
 */
class ExampleBenchmark
{
    public function benchStringConcat()
    {
        $str = '';
        for ($i = 0; $i < 1000; $i++) {
            $str .= 'a';
        }
    }

    public function benchArrayPush()
    {
        $arr = [];
        for ($i = 0; $i < 1000; $i++) {
            $arr[] = $i;
        }
    }
}
```
This sets up two basic benchmark tests, string concatenation and array push.

- **@Revs(1000)** → Each benchmark repeats 1000 times per iteration.
- **@Iterations(5)** → The benchmark runs 5 separate iterations and averages results.
- `benchStringConcat` and `benchArrayPush` are sample benchmarks for string and array operations.

### Run the Benchmarks

```console
phpbench run ExampleBenchmark.php
```

You should see an output similar to:

```output
PHPBench (1.2.14) running benchmarks... #standwithukraine
with PHP version 8.0.30, xdebug ❌, opcache ❌

\ExampleBenchmark

    benchStringConcat.......................I4 - Mo13.438μs (±0.82%)
    benchArrayPush..........................I4 - Mo8.487μs (±0.51%)

Subjects: 2, Assertions: 0, Failures: 0, Errors: 0
```

### Understanding PHP benchmark metrics and results with PHPBench

- **benchStringConcat** → Name of the benchmark function; in this case, it measures string concatenation performance.
- **benchArrayPush** → Name of another benchmark function; here, measuring array push performance.
- **xdebug ❌** → Xdebug extension is disabled, which is good because Xdebug slows down execution.
- **opcache ❌** → Opcache is disabled, so you’re measuring raw execution without caching optimizations.
- **I4** → Number of iterations per measurement.  
  - `I4` means 4 iterations of this benchmark were executed for one measurement.
- **Mo13.438μs** → Mode (or mean) execution time for the benchmark.  
  - `Mo` = Mode, showing the most common measured execution time across iterations.  
  - `13.438 μs` = 13.438 microseconds per iteration.
- **(±0.82%)** → Variation or coefficient of variation in the measurements.  
  - Shows consistency of results.  
  - Lower percentage → more stable and reliable benchmark.

### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on a `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

| Benchmark Function   | Iterations | Mode Execution Time (μs) | Variation (%) | Notes                                           |
|---------------------|------------|----------------|---------------|------------------------------------------------|
| benchStringConcat   | I4         | 13.493         | ±1.80%        | Measures performance of string concatenation |
| benchArrayPush      | I4         | 7.395          | ±1.07%         | Measures performance of pushing elements to an array |

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Benchmark Function   | Iterations | Mode Execution Time (μs)| Variation (%) | Notes                                    |
|---------------------|------------|-------------------|-----------|------------------------------------------|
| benchStringConcat    | I4         | 13.438 μs         | ±0.82%    | Measures performance of string concatenation |
| benchArrayPush       | I4          | 8.487 μs          | ±0.51%    | Measures performance of pushing elements to an array|

### PHP performance benchmarking comparison on Arm64 and x86_64
When you compare the benchmarking results, you will notice that on the Google Axion C4A Arm-based instances:

- PHP 8.0.30 benchmarks were run on the GCP Arm VM with Xdebug and Opcache disabled.  
- `benchStringConcat` executed in 13.438 μs per iteration, while `benchArrayPush` took 8.487 μs per iteration.  
- Low variation (±0.82% and ±0.51%) indicates stable and consistent benchmark results.





