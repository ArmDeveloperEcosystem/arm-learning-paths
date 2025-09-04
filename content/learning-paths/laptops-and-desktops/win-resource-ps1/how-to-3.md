---
title: Measuring power usage
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Sampling battery status
Querying battery status provides a way to measure power usage without an external power meter. It is also handy in that data collection and logging can be automatic.

A PowerShell script does all the work. It launches the video decoding task, samples battery status, and outputs sampled data to a file with format.

Open your code editor, copy content below and save it as `sample_power.ps1`.
```PowerShell { line_numbers = true }
param (
    [string]$exePath = "path\to\ffplay.exe",
    [string[]]$argList = @("-loop", "150", "-autoexit", "D:\RaceNight_1080p.mp4"),
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

{{% notice Note %}}
Modify the path to `ffplay.exe` on line 2 accordingly.
{{% /notice %}}

The battery data is system based and process agnostic. Full charge the battery. Close any unnecessary applications. Unplug the power cord. And run the script:
```console
.\sample_power.ps1
```
A video starts playing. It ends in 30 minutes. And then you can find the sample results file **watts.csv** in current directory. The test runs for a longer time so you can observe a distinct battery remaining capacity drop.

The script collects battery remaining capacity and discharge rate periodically. You can track the battery remaining capacity to have an understanding of the power consumption.

### View result
Shown below is example sample result from running x86_64 version ffplay.exe:
```output
Timestamp,RemainingCapacity(mWh),DischargeRate(mW)
2025-08-15T14:42:50.5231628+08:00,48438,4347
......
2025-08-15T15:12:38.2028188+08:00,43823,8862
```

Example result from running Arm64 native ffplay.exe:
```output
Timestamp,RemainingCapacity(mWh),DischargeRate(mW)
2025-08-15T15:53:05.8430758+08:00,48438,3255
......
2025-08-15T16:22:55.3163530+08:00,44472,7319
```

The sample result file is in **csv** format. You can open it with spreadsheet applications like Microsoft Excel for a better view and plot lines for data analysis.
