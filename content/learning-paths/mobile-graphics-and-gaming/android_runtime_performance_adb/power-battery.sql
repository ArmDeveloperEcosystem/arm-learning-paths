-- Match current and voltage samples captured at the same trace timestamp.
WITH raw_samples AS (
  SELECT
    current.ts,
    current.value AS current_ua,
    voltage.value AS voltage_uv
  FROM counter current
  JOIN counter_track current_track ON current.track_id = current_track.id
  JOIN counter voltage ON current.ts = voltage.ts
  JOIN counter_track voltage_track ON voltage.track_id = voltage_track.id
  WHERE current_track.name = 'batt.current_ua'
    AND voltage_track.name = 'batt.voltage_uv'
),
-- Convert microamps and microvolts to watts, and retain the preceding timestamp
-- so energy can be calculated for each sampling interval.
samples AS (
  SELECT
    ts,
    current_ua,
    voltage_uv,
    -- Android reports discharge current as negative on conforming devices.
    -current_ua * voltage_uv / 1000000000000.0 AS power_watts,
    lag(ts) OVER (ORDER BY ts) AS previous_ts
  FROM raw_samples
),
-- Convert trace time to elapsed wall-clock time and integrate power over each
-- interval. The script replaces MONITOR_START_MS before running this query.
power AS (
  SELECT
    ts,
    (to_realtime(ts) / 1000000.0 - MONITOR_START_MS) / 1000.0 AS elapsed_seconds,
    current_ua,
    voltage_uv,
    power_watts,
    CASE
      WHEN previous_ts IS NULL THEN 0.0
      -- Integrate W*ns into Wh between adjacent samples.
      ELSE power_watts * (ts - previous_ts) / 3600000000000.0
    END AS interval_energy_wh
  FROM samples
)
-- Return instantaneous battery readings and cumulative energy in CSV-ready units.
SELECT
  cast(round(to_realtime(ts) / 1000000.0) AS integer) AS timestampUnixMilliseconds,
  round(elapsed_seconds, 3) AS elapsedSeconds,
  cast(current_ua AS integer) AS currentMicroamps,
  cast(voltage_uv AS integer) AS voltageMicrovolts,
  round(power_watts, 6) AS powerWatts,
  round(sum(interval_energy_wh) OVER (ORDER BY elapsed_seconds), 9) AS cumulativeEnergyWattHours
FROM power
ORDER BY elapsed_seconds;
