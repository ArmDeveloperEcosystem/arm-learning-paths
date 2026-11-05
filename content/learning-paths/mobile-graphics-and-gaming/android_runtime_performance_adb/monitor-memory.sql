WITH samples AS (
  SELECT counter.ts, process.pid, track.name, counter.value
  FROM counter
  JOIN process_counter_track track ON counter.track_id = track.id
  JOIN process ON track.upid = process.upid
  JOIN package_list package ON package.uid = process.uid
  WHERE package.package_name = 'APP_PACKAGE'
    AND track.name IN (
      'mem.rss', 'mem.rss.anon', 'mem.rss.file', 'mem.rss.shmem',
      'mem.rss.watermark', 'mem.swap', 'mem.virt', 'mem.locked'
    )
), pivoted AS (
  SELECT
    ts, pid,
    max(CASE WHEN name = 'mem.rss' THEN value END) AS rss_bytes,
    max(CASE WHEN name = 'mem.rss.anon' THEN value END) AS rss_anon_bytes,
    max(CASE WHEN name = 'mem.rss.file' THEN value END) AS rss_file_bytes,
    max(CASE WHEN name = 'mem.rss.shmem' THEN value END) AS rss_shared_bytes,
    max(CASE WHEN name = 'mem.rss.watermark' THEN value END) AS rss_high_watermark_bytes,
    max(CASE WHEN name = 'mem.swap' THEN value END) AS swap_bytes,
    max(CASE WHEN name = 'mem.virt' THEN value END) AS virtual_bytes,
    max(CASE WHEN name = 'mem.locked' THEN value END) AS locked_bytes
  FROM samples
  GROUP BY ts, pid
)
SELECT
  cast(round(to_realtime(ts) / 1000000.0) AS integer) AS timestampUnixMilliseconds,
  round((to_realtime(ts) / 1000000.0 - MONITOR_START_MS) / 1000.0, 3) AS elapsedSeconds,
  pid,
  cast(rss_bytes AS integer) AS rssBytes,
  cast(rss_anon_bytes AS integer) AS rssAnonymousBytes,
  cast(rss_file_bytes AS integer) AS rssFileBytes,
  cast(rss_shared_bytes AS integer) AS rssSharedBytes,
  cast(rss_high_watermark_bytes AS integer) AS rssHighWatermarkBytes,
  cast(swap_bytes AS integer) AS swapBytes,
  cast(virtual_bytes AS integer) AS virtualBytes,
  cast(locked_bytes AS integer) AS lockedBytes
FROM pivoted
ORDER BY ts, pid;
