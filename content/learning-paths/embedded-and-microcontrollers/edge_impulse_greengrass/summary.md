---
title: 8. Summary/Conclusions
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Summary 

Congratulations!  You have completed this workshop!  Please select "Next" below to read a bit about cleaning up your AWS environment in order to minimize costs/etc (AWS workshop attendees: this will happen automatically for you)

### For More Information

Below is some detailed reference information regarding the Edge Impulse AWS IoT Integration

## Model Metrics

Basic model metrics are now accumulated and published in the integration into IoT Core. The metrics will be published at specified intervals (per the "metrics\_sleeptime\_ms" component configuration parameter) to the following IoT Core topic:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/model/metrics
		
The metrics published are:

* **accumulated mean**: running accumulation of the average confidences from the linux runner while running the current model
* **accumulated standard deviation**: running accumulation of the standard deviation from the linux runner while running the current model

The format of the model metrics output is as follows:

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

## Command Reference

In the 2025 January integration update, the following commands are now available with the Edge Impulse Greengrass Linux Runner Greengrass integration. The following commands are dispatched via the integration's IoT Core Topic as a JSON:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/command/input
		
Results from the command can be found using the following topic:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/command/output

Command JSON structure is defined as follows:

	{
		"cmd": <command verb>, 
		"value": <if command is a "set" command, setting value goes here>
	}

The currently supported commands are described below:

### Initial Invocation

When the runner process is started/restarted, the following JSON will be published to the command output topic above:

		{
		  "result": {
		    "status": "started",
		    "ts": 1736026956853,
		    "id": "5c4e627e-6e9d-4382-bba7-00c0129705c4"
		  }
		}

This JSON can be used to flag a new invocation of the runner service (or a restart of the runner service). If there are any previous runtime changes made (i.e. confidence filter settings for example... see below), those changes can be resent to the newly invoked runtime. 

### Restart Command

##### Command JSON:

		{
		 "cmd": "restart"
		}
		
##### Command Description:

This command directs the integration to "restart" the Edge Impulse linux runner process. In conjunction with the "ei\_shutdown\_behavior" option being set to "wait\_for\_restart", the linux runner process will continue operating after the model has completed its operation. The linux runner process will continue to process input commands and will restart the linux runner via dispatching this command. 

### Enable Threshold Filter Command

##### Command JSON:

		{
		 "cmd": "enable_threshold_filter"
		}
		
##### Command Description:

This command directs the integration to enable the threshold filter.  The filter will control which inferences will get published into IoT Core. By default the filter is disabled so that all inferences reported are sent into IoT Core. 

##### Command Result:

The command output will be published as follows and will include the filter config:

		{
		  "result": {
		    "threshold_filter_config": {
		      "enabled": "yes",
		      "confidence_threshold": 0.7,
		      "threshold_criteria": "ge"
		    }
		  }
		}

### Disable Threshold Filter Command

##### Command JSON:

		{
		 "cmd": "disable_threshold_filter"
		}
		
##### Command Description:

This command directs the integration to disable the threshold filter.  

##### Command Result:

The command output will be published as follows and will include the filter config:

		{
		  "result": {
		    "threshold_filter_config": {
		      "enabled": "no",
		      "confidence_threshold": 0.7,
		      "threshold_criteria": "ge"
		    }
		  }
		}

### Set Threshold Filter Criteria Command

##### Command JSON:

		{
		 "cmd": "set_threshold_filter_criteria",
		 "value": "ge"
		}
		
##### Command Description:

This command directs the integration to set the threshold filter criteria. The available options for the criteria are:

* **"gt"**: publish if inference confidence is "greater than"...
* **"ge"**: publish if inference confidence is "greater than or equal to"...
* **"eq"**: publish if inference confidence is "equal to"...
* **"le"**: publish if inference confidence is "less than or equal to"...
* **"gt"**: publish if inference confidence is "less than"...

##### Command Result:

The command output will be published as follows:

		{
		  "result": {
		    "criteria": "gt"
		  }
		}

### Get Threshold Filter Criteria Command

##### Command JSON:

		{
		 "cmd": "get_threshold_filter_criteria"
		}
		
##### Command Description:

This command directs the integration to get the threshold filter criteria. The currently set threshold criteria is published to the command output topic above. 

##### Command Result:

The command output will be published as follows with the configured criteria:

		{
		  "result": {
		    "criteria": "gt"
		  }
		}


### Set Threshold Filter Confidence Command

##### Command JSON:

		{
		 "cmd": "set_threshold_filter_confidence",
		 "value": 0.756
		}
		
##### Command Description:

This command directs the integration to set the threshold filter confidence bar. The value set must be a value 0 < x <= 1.0

##### Command Result:

The command output will be published as follows with the specified confidence bar:

		{
		  "result": {
		    "confidence_threshold": "0.756"
		  }
		}


### Get Threshold Filter Confidence Command

##### Command JSON:

		{
		 "cmd": "get_threshold_filter_confidence"
		}
		
##### Command Description:

This command directs the integration to get the threshold filter confidence bar. The currently set threshold confidence value is published to the command output topic above. 

##### Command Result:

The command output will be published as follows with the currently configured confidence bar:

		{
		  "result": {
		    "confidence_threshold": "0.756"
		  }
		}

### Get Threshold Filter Config Command

##### Command JSON:

		{
		 "cmd": "get_threshold_filter_config"
		}
		
##### Command Description:

This command directs the integration to retrieve the current threshold filter config. The currently set threshold filter config is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the currently configured filter config:

		{
		  "result": {
		    "threshold_filter_config": {
		      "enabled": "no",
		      "confidence_threshold": "0.756",
		      "threshold_criteria": "gt"
		    }
		  }
		}

### Get Model Info Command

##### Command JSON:

		{
		 "cmd": "get_model_info"
		}
		
##### Command Description:

This command directs the integration to retrieve the currently running model information. The model information is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the current model information:

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

### Reset Model Metrics Command

##### Command JSON:

		{
		 "cmd": "reset_metrics"
		}
		
##### Command Description:

This command directs the integration to reset the model metrics counters.  

##### Command Result:

The command output will be published as follows to indicate the metrics counters are reset:

		{
		  "result": {
		    "metrics_reset": "OK"
		  }
		}
	
### Clear Cache Command

##### Command JSON:

		{
		 "cmd": "clear_cache"
		}
		
##### Command Description:

This command directs the integration to clear the currently configured inference image cache. The entire cache will be cleared. This command is sensitive to the Greengrass component configuration (i.e. which inference caches are enabled/disabled). This command will clear ALL caches that are currently enabled in the component configuration. 

##### Command Result:

The command output will be published as follows with the clear cache results:

		{
		  "result": {
		    "clear_cache": {
		      "local": "OK",
		      "s3": "OK"
		    }
		  }
		}

### Clear Specified File From Cache Command

##### Command JSON:

		{
		 "cmd": "clear_cache_file"
		 "value": <uuid>
		}
		
##### Command Description:

This command directs the integration to clear the specified file (by its uuid) from within the inference cache.  This command is sensitive to the Greengrass component configuration (i.e. which inference caches are enabled/disabled).  This command will clear the specified file from ALL enabled caches per the component configuration. 

##### Command Result:

The command output will be published as follows with the clear cache results for the specified UUID:

		{
		  "result": {
		    "clear_cache_file": {
		      "local": "OK",
		      "s3": "OK",
		      "uuid": "e4faa78b-2a09-40d1-adfd-8e5fc32feb11"
		    }
		  }
		}