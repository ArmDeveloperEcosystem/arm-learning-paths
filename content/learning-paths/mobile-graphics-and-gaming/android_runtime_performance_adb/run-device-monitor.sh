#!/bin/sh
set -eu

usage() {
    echo "Usage: $0 [--serial WIRELESS_SERIAL] DURATION_SECONDS [OUTPUT_DIRECTORY]" >&2
}

die() {
    echo "$*" >&2
    exit 1
}

# Process script arguments
serial=${ANDROID_SERIAL:-}
while [ "$#" -gt 0 ]; do
    case "$1" in
        --serial)
            [ "$#" -ge 2 ] || { usage; exit 2; }
            serial=$2
            shift 2
            ;;
        --*)
            usage
            exit 2
            ;;
        *) break ;;
    esac
done

[ "$#" -ge 1 ] && [ "$#" -le 2 ] || { usage; exit 2; }
duration_seconds=$1
case "$duration_seconds" in
    ''|*[!0-9]*|0) die "Duration must be a positive integer." ;;
esac

package_name=com.google.aiedge.examples.phototalk # Target application package name
script_directory=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_directory=${2:-"$PWD/data/runtime-perf-$(date +%Y%m%d-%H%M%S)"}
remote_trace="/data/misc/perfetto-traces/aeb-device-monitor-$$.pftrace"
temporary_config=$(mktemp "${TMPDIR:-/tmp}/aeb-device-monitor.XXXXXX")
memory_query=$(mktemp "${TMPDIR:-/tmp}/aeb-monitor-memory.XXXXXX")
power_query=$(mktemp "${TMPDIR:-/tmp}/aeb-monitor-power.XXXXXX")
battery_sysfs_file="$output_directory/.power-fallback.csv"
logcat_pid=
perfetto_pid=
thermal_pid=
power_pid=
trace_processor_path=${PERFETTO_TRACE_PROCESSOR:-}

# Identify and select the wirelessly connected target device
select_wireless_device() {
    devices=$(adb devices -l)
    if [ -n "$serial" ]; then
        if ! printf '%s\n' "$devices" | awk -v target="$serial" '$1 == target && $2 == "device" { found = 1 } END { exit !found }'; then
            case "$serial" in
                *:*) adb connect "$serial" >/dev/null 2>&1 || true ;;
            esac
            devices=$(adb devices -l)
        fi
        line=$(printf '%s\n' "$devices" | awk -v target="$serial" '$1 == target && $2 == "device" { print; exit }')
        [ -n "$line" ] || die "Wireless adb target is not connected: $serial"
        printf '%s\n' "$line" | grep -q ' usb:' && die "USB adb targets are not supported: $serial"
    else
        serials=$(printf '%s\n' "$devices" | awk '$2 == "device" && $0 !~ / usb:/ { print $1 }')
        count=$(printf '%s\n' "$serials" | awk 'NF { count++ } END { print count + 0 }')
        [ "$count" -eq 1 ] || die "Found $count wireless adb targets. Pass --serial with one entry from 'adb devices -l'."
        serial=$(printf '%s\n' "$serials" | awk 'NF { print; exit }')
    fi

    export ANDROID_SERIAL=$serial
    adb get-state >/dev/null
}

# Thermal Hardware Abstraction Layer (HAL) sampling from CPU/GPU sensors
capture_thermal_hal() {
    printf '%s\n' 'timestampUnixMilliseconds,elapsedSeconds,name,type,temperatureCelsius,status'
    while true; do
        timestamp=$(adb shell date +%s%3N 2>/dev/null | tr -d '\r') || true
        case "$timestamp" in
            ''|*[!0-9]*) sleep 1; continue ;;
        esac
        [ "${#timestamp}" -eq 13 ] || { sleep 1; continue; }
        adb shell dumpsys thermalservice 2>/dev/null | awk -v ts="$timestamp" -v start="$monitor_start_unix_milliseconds" '
            /^Current temperatures from HAL:/ { active = 1; next }
            /^Current cooling devices from HAL:/ { active = 0 }
            active && /Temperature{/ {
                value = type = name = status = $0
                sub(/^.*mValue=/, "", value); sub(/,.*/, "", value)
                sub(/^.*mType=/, "", type); sub(/,.*/, "", type)
                sub(/^.*mName=/, "", name); sub(/,.*/, "", name)
                sub(/^.*mStatus=/, "", status); sub(/}.*/, "", status)
                gsub(/"/, "\"\"", name)
                printf "%s,%.3f,\"%s\",%s,%s,%s\n", ts, (ts - start) / 1000.0, name, type, value, status
            }
        '
        sleep 1
    done
}

# Capture battery current and voltage directly when the device exposes the sysfs nodes.
capture_power_fallback() {
    printf '%s\n' 'timestampUnixMilliseconds,elapsedSeconds,currentMicroamps,voltageMicrovolts'
    while true; do
        readings=$(adb shell 'date +%s%3N; cat /sys/class/power_supply/battery/current_now /sys/class/power_supply/battery/voltage_now' 2>/dev/null | tr -d '\r') || true
        timestamp=$(printf '%s\n' "$readings" | sed -n '1p')
        current=$(printf '%s\n' "$readings" | sed -n '2p')
        voltage=$(printf '%s\n' "$readings" | sed -n '3p')
        case "$timestamp:$current:$voltage" in
            *[!0-9:-]*|*::*|:*|*:) ;;
            *) [ "${#timestamp}" -eq 13 ] && awk -v ts="$timestamp" -v start="$monitor_start_unix_milliseconds" -v current="$current" -v voltage="$voltage" 'BEGIN { printf "%s,%.3f,%s,%s\n", ts, (ts - start) / 1000.0, current, voltage }' ;;
        esac
        sleep 1
    done
}

# Cancel active collection processes
stop_collectors() {
    for pid in "$logcat_pid" "$thermal_pid" "$power_pid"; do
        if [ -n "$pid" ]; then
            command kill "$pid" 2>/dev/null || true
            wait "$pid" 2>/dev/null || true
        fi
    done
    logcat_pid= thermal_pid= power_pid=
}

cleanup() {
    trap - EXIT INT TERM
    stop_collectors
    if [ -n "$perfetto_pid" ]; then
        command kill -INT "$perfetto_pid" 2>/dev/null || true
        wait "$perfetto_pid" 2>/dev/null || true
    fi
    rm -f "$temporary_config" "$memory_query" "$power_query"
}

extract_llm_data() {
    printf '%s\n' 'timestampUnixMilliseconds,elapsedSeconds,completionTimestampUnixMilliseconds,requestType,promptCharacters,prefillTokens,decodeTokens,ttftSeconds,prefillTokensPerSecond,decodeMilliseconds,decodeTokensPerSecond' > "$output_directory/llm-perf.csv"
    sed -n 's/^.*LLM_INFERENCE_CSV //p' "$output_directory/logcat.txt" | awk -F, -v start="$monitor_start_unix_milliseconds" '
        NF == 8 {
            decode_ms = $8 > 0 ? $5 / $8 * 1000 : 0
            printf "%s,%.3f,%s,conversation,%s,%s,%s,%s,%s,%.3f,%s\n", $1, ($1 - start) / 1000.0, $2, $3, $4, $5, $6, $7, decode_ms, $8
        }
        NF == 7 {
            decode_ms = $7 > 0 ? $4 / $7 * 1000 : 0
            printf "%s,%.3f,%s,conversation,%s,%s,%s,%s,%s,%.3f,%s\n", $1, ($1 - start) / 1000.0, $1, $2, $3, $4, $5, $6, decode_ms, $7
        }
    ' >> "$output_directory/llm-perf.csv"
}

extract_memory_data() {
    sed -e "s/APP_PACKAGE/$package_name/g" -e "s/MONITOR_START_MS/$monitor_start_unix_milliseconds/g" "$script_directory/sql/monitor-memory.sql" > "$memory_query"
    if ! "$trace_processor_path" query -f "$memory_query" "$output_directory/trace.pftrace" > "$output_directory/memory.csv" 2> "$output_directory/trace-processor-memory.log"; then
        printf '%s\n' 'timestampUnixMilliseconds,elapsedSeconds,pid,rssBytes,rssAnonymousBytes,rssFileBytes,rssSharedBytes,rssHighWatermarkBytes,swapBytes,virtualBytes,lockedBytes' > "$output_directory/memory.csv"
    fi
    memory_samples=$(awk 'END { print (NR > 0 ? NR - 1 : 0) }' "$output_directory/memory.csv")
    printf 'memory_samples=%s\n' "$memory_samples" >> "$output_directory/summary.txt"
}

extract_sysfs_power() {
    awk -F, '
        BEGIN { print "timestampUnixMilliseconds,elapsedSeconds,currentMicroamps,voltageMicrovolts,powerWatts,cumulativeEnergyWattHours" }
        NR > 1 {
            power = $3 * $4 / 1000000000000.0; if (power < 0) power = -power
            if (previous != "") energy += power * ($2 - previous) / 3600.0
            printf "%s,%.3f,%.0f,%.0f,%.6f,%.9f\n", $1, $2, $3, $4, power, energy
            previous = $2
        }
    ' "$battery_sysfs_file" > "$output_directory/power.csv"
}

extract_power_data() {
    power_source=unavailable

    sed "s/MONITOR_START_MS/$monitor_start_unix_milliseconds/g" "$script_directory/sql/power-battery.sql" > "$power_query"
    if "$trace_processor_path" query -f "$power_query" "$output_directory/trace.pftrace" > "$output_directory/power.csv" 2> "$output_directory/trace-processor-power.log" &&
        [ "$(wc -l < "$output_directory/power.csv")" -gt 1 ]; then
        power_source=perfetto_battery
    elif [ -s "$battery_sysfs_file" ]; then
        extract_sysfs_power
        [ "$(wc -l < "$output_directory/power.csv")" -gt 1 ] && power_source=battery_sysfs_fallback
    fi

    [ "$power_source" != unavailable ] ||
        printf '%s\n' 'timestampUnixMilliseconds,elapsedSeconds,currentMicroamps,voltageMicrovolts,powerWatts,cumulativeEnergyWattHours' > "$output_directory/power.csv"

    power_samples=$(awk 'END { print (NR > 0 ? NR - 1 : 0) }' "$output_directory/power.csv")
    printf 'power_source=%s\npower_samples=%s\n' "$power_source" "$power_samples" >> "$output_directory/summary.txt"

    rm -f "$battery_sysfs_file"
}

finalize() {
    status=$1
    stop_collectors
    adb pull "$remote_trace" "$output_directory/trace.pftrace" >/dev/null 2>&1 || true
    adb shell rm -f "$remote_trace" >/dev/null 2>&1 || true
    extract_llm_data
    end_time=$(date +%s)
    inference_count=$(awk 'END { print (NR > 0 ? NR - 1 : 0) }' "$output_directory/llm-perf.csv")
    thermal_samples=$(awk 'END { print (NR > 0 ? NR - 1 : 0) }' "$output_directory/thermal-hal.csv")
    {
        printf 'status=%s\n' "$status"
        printf 'requested_duration_seconds=%s\n' "$duration_seconds"
        printf 'actual_duration_seconds=%s\n' "$((end_time - start_time))"
        printf 'device_serial=%s\n' "$serial"
        printf 'device_model=%s\n' "$device_model"
        printf 'package_name=%s\n' "$package_name"
        printf 'monitor_start_unix_milliseconds=%s\n' "$monitor_start_unix_milliseconds"
        printf 'inference_count=%s\n' "$inference_count"
        printf 'thermal_samples=%s\n' "$thermal_samples"
    } > "$output_directory/summary.txt"
    extract_memory_data
    extract_power_data
}

abort() {
    trap - INT TERM
    echo "Stopping device monitoring..." >&2
    if [ -n "$perfetto_pid" ]; then
        command kill -INT "$perfetto_pid" 2>/dev/null || true
        wait "$perfetto_pid" 2>/dev/null || true
        perfetto_pid=
    fi
    finalize interrupted
    exit 130
}

trap cleanup EXIT
trap abort INT TERM

select_wireless_device
[ -n "$trace_processor_path" ] || die "PERFETTO_TRACE_PROCESSOR is not set. Export it to the trace_processor executable."

battery_state=$(adb shell dumpsys battery | tr -d '\r')
printf '%s\n' "$battery_state" | grep -Eq 'AC powered: true|USB powered: true|Wireless powered: true|Dock powered: true' && die "Disconnect external power before monitoring."
device_model=$(adb shell getprop ro.product.model | tr -d '\r')

mkdir -p "$output_directory"
duration_ms=$((duration_seconds * 1000))
sed "s/DURATION_MS/$duration_ms/" "$script_directory/device-monitor-perfetto.cfg" > "$temporary_config"
monitor_start_unix_milliseconds=$(adb shell date +%s%3N | tr -d '\r')
case "$monitor_start_unix_milliseconds" in
    ''|*[!0-9]*) die "The device did not provide a Unix timestamp in milliseconds." ;;
esac
[ "${#monitor_start_unix_milliseconds}" -eq 13 ] || die "The device did not provide a 13-digit Unix timestamp in milliseconds."
start_time=$(date +%s)

# Clear the buffer immediately before capture so CSV extraction cannot include an older run
adb logcat -c
adb logcat -v epoch > "$output_directory/logcat.txt" & logcat_pid=$!
adb shell perfetto --txt -c - -o "$remote_trace" < "$temporary_config" & perfetto_pid=$!
capture_thermal_hal > "$output_directory/thermal-hal.csv" & thermal_pid=$!
if adb shell 'cat /sys/class/power_supply/battery/current_now /sys/class/power_supply/battery/voltage_now' >/dev/null 2>&1; then
    capture_power_fallback > "$battery_sysfs_file" & power_pid=$!
fi

echo "Monitoring $package_name on $serial for $duration_seconds seconds. Use the application normally." >&2
if wait "$perfetto_pid"; then
    perfetto_pid=
    finalize completed
else
    perfetto_pid=
    finalize incomplete
    die "Perfetto monitoring ended before completing. Partial results were preserved."
fi

echo "Results written to $output_directory"
