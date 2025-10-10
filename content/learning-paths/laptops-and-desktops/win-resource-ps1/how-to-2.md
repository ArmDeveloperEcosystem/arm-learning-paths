---
title: Tracking system resource
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Sampling video decoding resource usage
A PowerShell script does all the work. It launches the video decoding task, samples CPU and memory usage, and outputs sampled data to a file with format.

Open your code editor, copy content below and save it as `sample_decoding.ps1`.
```PowerShell { line_numbers = true }
param (
    [string]$exePath = "path\to\ffplay.exe",
    [string[]]$argList = @("-loop", "15", "-autoexit", "D:\RaceNight_1080p.mp4"),
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

{{% notice Note %}}
Modify the path to `ffplay.exe` on line 2 accordingly.
{{% /notice %}}

Run the script:
```console
Set-ExecutionPolicy -Scope Process RemoteSigned
.\sample_decoding.ps1
```
A video starts playing. It ends in 3 minutes. And then you can find the sample results file **usage_log.csv** in current directory.

{{% notice Note %}}
Script execution can be blocked due to policy configuration. The `Set-ExecutionPolicy` line allows local script to run during this session.
{{% /notice %}}

### Script explained
The `param` section defines variables including binary path, video playback arguments, sampling interval and result file path.

Line 15 - Line 26 check and modify binary file attribute. The binaries in use are downloaded from the web. They can be blocked to run due to lack of signature. These lines unlock the binaries.

Line 41 gets all the child processes of the main process. The statistic data include resources used by all the processes spawned by the main process.

The `while` setction collects processes' CPU and memory usage periodically until the application exits. The CPU usage is accumulated time length that the process runs on CPU. And the memory usage is size of memory occupation with or without shared spaces accounted.

### View result
Shown below is example sample result from running x86_64 version ffplay.exe:
```output
Timestamp,CPU Sum (s),Memory Sum (MB),Memory Private Sum (MB),CPU0 (s),Memory0 (MB),Memory Private0 (MB),CPU1 (s),Memory1 (MB),Memory Private1 (MB)
2025-08-18T10:40:12.3480939+08:00,3.6875,378.65,342.16,3.671875,366.3515625,340.33984375,0.015625,12.296875,1.82421875
......
2025-08-18T10:43:09.7262439+08:00,396.375,391.71,355.00,396.359375,379.453125,353.2421875,0.015625,12.2578125,1.7578125
```

Example result from running Arm64 native ffplay.exe:
```output
Timestamp,CPU Sum (s),Memory Sum (MB),Memory Private Sum (MB),CPU0 (s),Memory0 (MB),Memory Private0 (MB),CPU1 (s),Memory1 (MB),Memory Private1 (MB)
2025-08-18T10:36:04.3654823+08:00,3.296875,340.51,328.17,3.28125,328.18359375,326.359375,0.015625,12.32421875,1.8125
......
2025-08-18T10:39:01.7856168+08:00,329.109375,352.53,339.96,329.09375,340.23046875,338.20703125,0.015625,12.30078125,1.75390625
```

The sample result file is in **csv** format. You can open it with spreadsheet applications like Microsoft Excel for a better view and plot lines for data analysis.
