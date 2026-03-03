---
title: Command and metrics reference
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This page is a reference for the MQTT commands and model metrics available in the Edge Impulse Greengrass integration. Use these commands to control the Runner service, manage the confidence threshold filter, retrieve model information, and manage the inference cache — all through AWS IoT Core MQTT topics.

Commands are sent as JSON messages to the device's command input topic and results are published to the command output topic:

```text
/edgeimpulse/device/<device-name>/command/input
/edgeimpulse/device/<device-name>/command/output
```

All commands use the following JSON structure:

```json
{
   "cmd": "<command-verb>",
   "value": "<optional-value>"
}
```

The `value` field is only required for commands that set a value.

## Model metrics

The Runner accumulates and publishes model metrics to IoT Core at the interval specified by the `metrics_sleeptime_ms` configuration parameter. Metrics are published to:

```text
/edgeimpulse/device/<device-name>/model/metrics
```

The published metrics include:

- **mean_confidence**: Running average of inference confidence scores for the current model.
- **standard_deviation**: Running standard deviation of confidence scores.
- **confidence_trend**: Direction the confidence is trending (`incr` or `decr`).

Example metrics output:

```json
{
   "mean_confidence": 0.696142,
   "standard_deviation": 0.095282,
   "confidence_trend": "decr",
   "details": {
      "n": 5,
      "sum_confidences": 3.480711,
      "sum_confidences_squared": 2.468464
   },
   "ts": 1736016142920,
   "id": "e4faa78b-2a09-40d1-adfd-8e5fc32feb11"
}
```

## Startup notification

When the Runner starts or restarts, it publishes the following JSON to the command output topic:

```json
{
   "result": {
      "status": "started",
      "ts": 1736026956853,
      "id": "5c4e627e-6e9d-4382-bba7-00c0129705c4"
   }
}
```

You can use this message to detect service restarts and re-apply any runtime changes (for example, confidence filter settings) to the newly started Runner.

## restart

Restarts the Edge Impulse Runner process. When used with the `ei_shutdown_behavior` option set to `wait_on_restart`, the Runner pauses after the model completes and waits for this command before restarting.

**Command:**

```json
{
   "cmd": "restart"
}
```

## enable_threshold_filter

Enables the confidence threshold filter. When enabled, only inference results that meet the threshold criteria are published to IoT Core. By default, the filter is disabled and all results are published.

**Command:**

```json
{
   "cmd": "enable_threshold_filter"
}
```

**Result:**

```json
{
   "result": {
      "threshold_filter_config": {
         "enabled": "yes",
         "confidence_threshold": 0.7,
         "threshold_criteria": "ge"
      }
   }
}
```

## disable_threshold_filter

Disables the confidence threshold filter. All inference results are published to IoT Core regardless of confidence score.

**Command:**

```json
{
   "cmd": "disable_threshold_filter"
}
```

**Result:**

```json
{
   "result": {
      "threshold_filter_config": {
         "enabled": "no",
         "confidence_threshold": 0.7,
         "threshold_criteria": "ge"
      }
   }
}
```

## set_threshold_filter_criteria

Sets the comparison operator for the confidence threshold filter. The available criteria are:

| Criteria | Description |
|---|---|
| `gt` | Publish if confidence is greater than the threshold |
| `ge` | Publish if confidence is greater than or equal to the threshold |
| `eq` | Publish if confidence is equal to the threshold |
| `le` | Publish if confidence is less than or equal to the threshold |
| `lt` | Publish if confidence is less than the threshold |

**Command:**

```json
{
   "cmd": "set_threshold_filter_criteria",
   "value": "ge"
}
```

**Result:**

```json
{
   "result": {
      "criteria": "gt"
   }
}
```

## get_threshold_filter_criteria

Retrieves the currently configured threshold filter criteria.

**Command:**

```json
{
   "cmd": "get_threshold_filter_criteria"
}
```

**Result:**

```json
{
   "result": {
      "criteria": "gt"
   }
}
```

## set_threshold_filter_confidence

Sets the confidence threshold value. Inference results are filtered against this value using the configured criteria. The value must be between 0 and 100.

**Command:**

```json
{
   "cmd": "set_threshold_filter_confidence",
   "value": 0.756
}
```

**Result:**

```json
{
   "result": {
      "confidence_threshold": "0.756"
   }
}
```

## get_threshold_filter_confidence

Retrieves the currently configured confidence threshold value.

**Command:**

```json
{
   "cmd": "get_threshold_filter_confidence"
}
```

**Result:**

```json
{
   "result": {
      "confidence_threshold": "0.756"
   }
}
```

## get_threshold_filter_config

Retrieves the complete threshold filter configuration, including enabled state, confidence value, and criteria.

**Command:**

```json
{
   "cmd": "get_threshold_filter_config"
}
```

**Result:**

```json
{
   "result": {
      "threshold_filter_config": {
         "enabled": "no",
         "confidence_threshold": "0.756",
         "threshold_criteria": "gt"
      }
   }
}
```

## get_model_info

Retrieves information about the currently running model, including its name, version, input dimensions, labels, and detection type.

**Command:**

```json
{
   "cmd": "get_model_info"
}
```

**Result:**

```json
{
   "result": {
      "model_info": {
         "model_name": "occupant_counter",
         "model_version": "v25",
         "model_params": {
            "axis_count": 1,
            "frequency": 0,
            "has_anomaly": 0,
            "image_channel_count": 3,
            "image_input_frames": 1,
            "image_input_height": 640,
            "image_input_width": 640,
            "image_resize_mode": "fit-longest",
            "inferencing_engine": 6,
            "input_features_count": 409600,
            "interval_ms": 1,
            "label_count": 1,
            "labels": [
               "person"
            ],
            "model_type": "object_detection",
            "sensor": 3,
            "slice_size": 102400,
            "threshold": 0.5,
            "use_continuous_mode": false,
            "sensorType": "camera"
         }
      }
   }
}
```

## reset_metrics

Resets the accumulated model metrics counters to zero.

**Command:**

```json
{
   "cmd": "reset_metrics"
}
```

**Result:**

```json
{
   "result": {
      "metrics_reset": "OK"
   }
}
```

## clear_cache

Clears all inference image caches. This command respects the component configuration — it clears all caches that are currently enabled (local file cache, S3 cache, or both).

**Command:**

```json
{
   "cmd": "clear_cache"
}
```

**Result:**

```json
{
   "result": {
      "clear_cache": {
         "local": "OK",
         "s3": "OK"
      }
   }
}
```

## clear_cache_file

Removes a specific cached inference result by its UUID. Like `clear_cache`, this command clears the file from all enabled caches.

**Command:**

```json
{
   "cmd": "clear_cache_file",
   "value": "<uuid>"
}
```

**Result:**

```json
{
   "result": {
      "clear_cache_file": {
         "local": "OK",
         "s3": "OK",
         "uuid": "e4faa78b-2a09-40d1-adfd-8e5fc32feb11"
      }
   }
}
```