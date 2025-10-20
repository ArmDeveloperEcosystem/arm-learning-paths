---
title: Measure power usage
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Sampling battery status

Querying battery status provides a way to measure power usage without an external power meter. Battery monitoring is also convenient because data collection and logging can be automated.

A PowerShell script launches the video decoding task, samples battery status, and outputs the collected data to a CSV formatted file.

Open your code editor, copy the content below, and save it as `sample_power.ps1`:

```PowerShell { line_numbers = true }
param (
    [string]$exePath = "ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\bin\ffplay.exe",
    [string[]]$argList = @("-loop", "15", "-autoexit", "RaceNight_1080p.mp4"),
    [int]$interval = 10,
    [string]$outputFile = "watts.csv"
)

# Clear or create log file
"" | Out-File -FilePath $outputFile

try {
    $cmdLine = "`"$exePath`" $argList"
    Write-Host "Executing: $cmdLine"
    $process = Start-Process -FilePath $exePath -ArgumentList $argList -PassThru
} catch {
    Write-Host "Failed to start process. Error: $_"
    exit 1
}

$appPid = $process.Id
Write-Host "Started application with PID: $appPid"
 
$outHead = @()
$outHead += "Timestamp,RemainingCapacity(mWh),DischargeRate(mW)"
$outHead -join "," | Out-File -Encoding utf8 $outputFile
 
Write-Host "Sampling start..."

while (-not $process.HasExited) {
    $outLine = @()

    $timestamp = Get-Date -Format o
    $outLine += $timestamp
    $proc = Get-Process -Id $appPid -ErrorAction SilentlyContinue
    if ($proc) {
        # Battery status sampling
        $powerConsumption = Get-WmiObject -Namespace "root\wmi" -Class "BatteryStatus"
        $remainingCapacity = $powerConsumption.RemainingCapacity
        $dischargeRate = $powerConsumption.DischargeRate
        $outLine += $remainingCapacity
        $outLine += $dischargeRate

        $outLine -join "," | Out-File -Append -Encoding utf8 $outputFile
    }

    Start-Sleep -Seconds $interval
    $process.Refresh()
}
```

Before you run the script, modify the path to `ffplay.exe` on line 2 to match your installation location.

The battery data is system-based and process-agnostic. Fully charge the battery, close any unnecessary applications, unplug the power cord, and run the script:

```console
.\sample_power.ps1
```

A video starts playing and completes in 30 minutes. When finished, you can find the results file `watts.csv` in the current directory. The test runs for a longer duration so you can observe a distinct drop in battery remaining capacity.

The script collects remaining battery capacity and discharge rate periodically. You can track the battery remaining capacity to understand the power consumption patterns.

### View results

The output below shows the results from running the x86_64 version of `ffplay.exe`:

```output
Timestamp,RemainingCapacity(mWh),DischargeRate(mW)
2025-08-15T14:42:50.5231628+08:00,48438,4347
......
2025-08-15T15:12:38.2028188+08:00,43823,8862
```

The output below shows the results from running the Arm64 version of `ffplay.exe`:

```output
Timestamp,RemainingCapacity(mWh),DischargeRate(mW)
2025-08-15T15:53:05.8430758+08:00,48438,3255
......
2025-08-15T16:22:55.3163530+08:00,44472,7319
```

The sample results file is in CSV format. You can open it with spreadsheet applications like Microsoft Excel for better visualization and to plot data analysis charts.

Battery monitoring provides an effective way to measure power consumption differences between x86_64 and native Arm64 applications. By comparing discharge rates, you can quantify the power efficiency advantages that Arm processors typically demonstrate for video decoding workloads.
