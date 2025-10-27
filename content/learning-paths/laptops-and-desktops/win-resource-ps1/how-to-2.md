---
title: Track system resource usage on Windows on Arm with PowerShell
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Analyze resource usage during sample video decoding


To monitor resource usage during video decoding, use the following PowerShell script. This script starts the decoding process, periodically records CPU and memory statistics, and then saves the results to a CSV file for analysis.

Open your code editor, copy the content below, and save it as `sample_decoding.ps1`:

```PowerShell { line_numbers = true }
param (
    [string]$exePath = "ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\bin\ffplay.exe",
    [string[]]$argList = @("-loop", "15", "-autoexit", "RaceNight_1080p.mp4"),
    [int]$interval = 2,
    [string]$outputFile = "usage_log.csv"
)

"" | Out-File -FilePath $outputFile

if (-Not (Test-Path $exePath)) {
    Write-Host "Executable not found at path: $exePath"
    exit 1
}

$zoneIdentifier = "$exePath`:Zone.Identifier"
if (Test-Path $zoneIdentifier) {
    Write-Host "exe is locked. Trying to unlock..."
    try {
        Unblock-File -Path $exePath
        Write-Host "Unlocked exe file."
    } catch {
        Write-Host "Failed to unlock exe: $($_.Exception.Message)"
    }
} else {
    Write-Host "exe is not locked."
}

try {
    $cmdLine = "`"$exePath`" $argList"
    Write-Host "Executing: $cmdLine"
    $process = Start-Process -FilePath $exePath -ArgumentList $argList -PassThru
} catch {
    Write-Host "Failed to start process. Error: $_"
    exit 1
}

$appPid = $process.Id
Write-Host "Parent PID: $appPid"

Start-Sleep -Seconds 2
$childProcess = Get-CimInstance -ClassName Win32_Process | Where-Object { $_.ParentProcessId -eq $appPid }

$index = 1
$outHead = @()
$outHead += "Timestamp,CPU Sum (s),Memory Sum (MB),Memory Private Sum (MB),CPU0 (s),Memory0 (MB),Memory Private0 (MB)"
foreach ($child in $childProcess) {
    $childPid = $child.ProcessID
    Write-Host " - Child: $childPid"
	$outHead += "CPU$index (s),Memory$index (MB),Memory Private$index (MB)"
	$index++
}
$outHead -join "," | Out-File -Encoding utf8 $outputFile

Write-Host "Sampling start..."

while (-not $process.HasExited) {
    $cpu = @()
    $mem = @()
    $memPriv = @()
    $outLine = @()

    $timestamp = Get-Date -Format o
    $outLine += $timestamp
    $proc = Get-Process -Id $appPid -ErrorAction SilentlyContinue
    if ($proc) {
        $cpu += $proc.CPU
        $mem += $proc.WorkingSet64 / 1MB
        $memPriv += $proc.PrivateMemorySize64 / 1MB

        foreach ($child in $childProcess) {
            $procChild = Get-Process -Id $child.ProcessId -ErrorAction SilentlyContinue
            $cpu += $procChild.CPU
            $mem += $procChild.WorkingSet64 / 1MB
            $memPriv += $procChild.PrivateMemorySize64 / 1MB
        }

        $outLine += ($cpu | Measure-Object -Sum).Sum
        $outLine += "{0:F2}" -f ($mem | Measure-Object -Sum).Sum
        $outLine += "{0:F2}" -f ($memPriv | Measure-Object -Sum).Sum
        for ($i = 0; $i -lt $cpu.Count; $i++) {
            $outLine += $cpu[$i]
            $outLine += $mem[$i]
            $outLine += $memPriv[$i]
        }

        $outLine -join "," | Out-File -Append -Encoding utf8 $outputFile
    }

    Start-Sleep -Seconds $interval
    $process.Refresh()
}
```

Before you run the script, modify the path to `ffplay.exe` on line 2 to match your installation location.

Run the script:

```console
Set-ExecutionPolicy -Scope Process RemoteSigned
.\sample_decoding.ps1
```
When you run the script, the video plays for about three minutes. After playback finishes, you'll find the results file named `usage_log.csv` in your current directory. Open this file with a spreadsheet application to review and analyze the recorded resource usage data.

{{% notice Note %}}
Script execution might be blocked due to security policy configuration. The `Set-ExecutionPolicy` command allows local scripts to run during this session.
{{% /notice %}}

## Understand what the script does

The `param` section defines variables including the binary path, video playback arguments, sampling interval, and result file path. You can modify these values as needed.

Lines 15–26 check whether the binary file is blocked by Windows security settings. When you download executables from the web, Windows may prevent them from running if they lack a digital signature. This section attempts to unlock the binary using the `Unblock-File` command, allowing the script to run the application without security restrictions.

Line 41 retrieves all child processes of the main process. The statistical data includes resources used by all processes spawned by the main process.

The `while` section collects CPU and memory usage periodically until the application exits. The CPU usage represents accumulated time that the process runs on the CPU. The memory usage shows the size of memory occupation with or without shared spaces accounted for.

### View the results

The output below shows the results from running the x86_64 version of `ffplay.exe`:

```output
Timestamp,CPU Sum (s),Memory Sum (MB),Memory Private Sum (MB),CPU0 (s),Memory0 (MB),Memory Private0 (MB),CPU1 (s),Memory1 (MB),Memory Private1 (MB)
2025-08-18T10:40:12.3480939+08:00,3.6875,378.65,342.16,3.671875,366.3515625,340.33984375,0.015625,12.296875,1.82421875
......
2025-08-18T10:43:09.7262439+08:00,396.375,391.71,355.00,396.359375,379.453125,353.2421875,0.015625,12.2578125,1.7578125
```

The output below shows the results from running the Arm64 version of `ffplay.exe`:

```output
Timestamp,CPU Sum (s),Memory Sum (MB),Memory Private Sum (MB),CPU0 (s),Memory0 (MB),Memory Private0 (MB),CPU1 (s),Memory1 (MB),Memory Private1 (MB)
2025-08-18T10:36:04.3654823+08:00,3.296875,340.51,328.17,3.28125,328.18359375,326.359375,0.015625,12.32421875,1.8125
......
2025-08-18T10:39:01.7856168+08:00,329.109375,352.53,339.96,329.09375,340.23046875,338.20703125,0.015625,12.30078125,1.75390625
```
The sample result file is in CSV (comma-separated values) format. Open it with a spreadsheet application such as Microsoft Excel to view the data in a table. You can use built-in chart tools to visualize CPU and memory usage over time, making it easier to spot trends and compare performance between Arm64 and x86_64 versions.
