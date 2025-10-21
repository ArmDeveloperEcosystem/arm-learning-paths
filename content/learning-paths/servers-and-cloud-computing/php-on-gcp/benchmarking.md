---
title: PHP Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## PHP benchmarking using PHPBench

In this section, you will learn how to benchmark PHP performance using PHPBench, a modern and extensible benchmarking framework for PHP applications. You will install PHPBench, run sample tests, and interpret key metrics such as mode time, variance, and throughput. You will then analyze the results to understand how your Google Cloud C4A (Axion Arm64) virtual machine performs on common operations like string manipulation and array processing.

PHPBench is a flexible micro-benchmarking tool designed to measure PHP code performance precisely and repeatably. 

With PHPBench, you can:
  * Measure the execution time of PHP functions or code blocks
  * Identify performance regressions between versions
  * Automate performance testing across CI/CD pipelines
  * Track results over time to detect optimizations or slowdowns
  * Track results over time to detect optimizations or slowdowns

## Download Composer installer

Before installing PHPBench, you need Composer, which is PHP's dependency manager. Composer handles library installations, versioning, and autoloading, ensuring tools like PHPBench run consistently across environments.

Download the Composer installer script using PHP:
```console
sudo php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
```

This command downloads a PHP script called `composer-setup.php`, which will install Composer.

## Install the phar extension

Composer requires PHP's phar (PHP Archive) extension to run. This extension allows PHP to execute .phar archive files, self-contained PHP applications like Composer and PHPBench are distributed in this format.

Install the extension with:
```console
sudo zypper install -y php8-phar
```

## Install Composer system-wide

Now, install Composer globally so it is available for all users and can be executed from any directory:

```console
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```
The output should look like:

```output
All settings correct for using Composer
Downloading...

Composer (version 2.8.12) successfully installed to: /usr/local/bin/composer
Use it: php /usr/local/bin/composer
```
Composer is now installed system-wide at /usr/local/bin/composer and ready to manage PHP dependencies.

## Remove the installer script

After successfully installing Composer, remove the installer file to keep your environment clean:

```console
sudo php -r "unlink('composer-setup.php');"
```
Since Composer is now installed system-wide, the installer file is no longer needed.

## Verify Composer installation
To confirm that Composer was installed correctly and is accessible globally, run:

```console
composer --version
```
You should see output similar to:
```output
Composer version 2.8.12 2025-09-19 13:41:59
PHP version 8.0.30 (/usr/bin/php)
Run the "diagnose" command to get more detailed diagnostics output.
```

Composer is now successfully installed and you can proceed to installing PHPBench.

## Install PHPBench globally

PHPBench is a powerful benchmarking tool for measuring the performance of PHP code. Install it globally using Composer so you can access it from any directory:

```console
composer global require phpbench/phpbench
```

This installs `phpbench` in your user's global Composer directory, typically located under `$HOME/.config/composer/`

## Add Composer global bin to PATH

To make `phpbench` accessible from any terminal session, add Composer's global binary path to your system's environment PATH:
```console
export PATH="$HOME/.config/composer/vendor/bin:$PATH"
echo 'export PATH=$HOME/.config/composer/vendor/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Verify PHPBench installation
Once installed, verify that PHPBench is working correctly:
```console
phpbench --version
```

You should see output similar to:
```output
phpbench 1.2.14
```
PHPBench is now installed and ready to run.

## Create a benchmark directory

Create a new PHP benchmark file using your preferred text editor:

```console
mkdir ~/phpbench-tests
cd ~/phpbench-tests
```
## Create a benchmark script

Create a new PHP benchmark file using your preferred editor:

```console
vi ExampleBenchmark.php
```
Add the following code to define your benchmark tests:

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

- @Revs(1000): Each benchmark repeats 1000 times per iteration.
- @Iterations(5): The benchmark runs 5 separate iterations and averages results.
- `benchStringConcat` and `benchArrayPush`: Sample benchmarks for string and array operations.

## Run the benchmarks

Execute the benchmark suite you created using the `phpbench run` command:

```console
phpbench run ExampleBenchmark.php
```
You should see output similar to:

```output
PHPBench (1.2.14) running benchmarks... #standwithukraine
with PHP version 8.0.30, xdebug ❌, opcache ❌

\ExampleBenchmark

    benchStringConcat.......................I4 - Mo13.438μs (±0.82%)
    benchArrayPush..........................I4 - Mo8.487μs (±0.51%)

Subjects: 2, Assertions: 0, Failures: 0, Errors: 0
```

## Understanding PHP benchmark metrics and results with PHPBench

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


## Benchmark summary on Arm64

Results from the benchmark suite executed on a Google Cloud c4a-standard-4 (Arm64) instance with 4 vCPUs and 16 GB memory, running SUSE Linux:
| Benchmark Function   | Iterations | Mode Execution Time (μs)| Variation (%) | Notes                                    |
|---------------------|------------|-------------------|-----------|------------------------------------------|
| benchStringConcat    | I4         | 13.438 μs         | ±0.82%    | Measures performance of string concatenation |
| benchArrayPush       | I4          | 8.487 μs          | ±0.51%    | Measures performance of pushing elements to an array|


## Benchmark summary on x86_64
For comparison, the same PHPBench test suite was executed on a Google Cloud c4-standard-4 (x86_64) instance with 4 vCPUs and 15 GB memory, running SUSE Linux:

| Benchmark Function   | Iterations | Mode Execution Time (μs) | Variation (%) | Notes                                           |
|---------------------|------------|----------------|---------------|------------------------------------------------|
| benchStringConcat   | I4         | 13.493         | ±1.80%        | Measures performance of string concatenation |
| benchArrayPush      | I4         | 7.395          | ±1.07%         | Measures performance of pushing elements to an array |

## PHP performance benchmarking comparison on Arm64 and x86_64

When comparing benchmark results between Google Cloud Axion C4A (Arm64) and x86-based C4 (x86_64) instances, you will see:

The results show that both architectures deliver nearly identical execution times for typical PHP operations, with Arm64 showing slightly lower variation (more stable performance). The Arm64 instance performs within ~15% of x86_64, showing strong memory throughput and cache performance for dynamic array allocation workloads.
Low variance (±0.82% / ±0.51: Indicates that the Axion-based Arm cores on C4A provide stable, repeatable performance, ideal for predictable PHP application behavior in production.

These results show that PHP performs consistently across both architectures, and that Google Cloud Axion C4A Arm64 VMs deliver competitive, reliable performance for PHP-based web and backend applications.





