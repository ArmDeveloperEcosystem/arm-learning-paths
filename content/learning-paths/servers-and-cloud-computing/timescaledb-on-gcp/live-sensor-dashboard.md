---
title: Build a live sensor temperature dashboard
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a live sensor temperature dashboard

In this section, you'll create a Grafana dashboard that visualizes live temperature data stored in TimescaleDB. The dashboard continuously updates to display sensor temperature changes in near real time.

## Prerequisites

Before proceeding, ensure the following are already completed:

- TimescaleDB is installed and running
- Grafana is installed and accessible
- PostgreSQL (TimescaleDB) data source is configured in Grafana
- Live data ingestion into the `sensor_data` table is running

You can verify live ingestion with:

```bash
sudo -u postgres psql sensors -c "SELECT COUNT(*) FROM sensor_data;"
```

The count should increase over time.

## Access Grafana

Open Grafana in your browser:

```bash
http://<GRAFANA_PUBLIC_IP>:3000
```

Log in using your Grafana credentials.

## Create a New Dashboard

- From the left sidebar, select **Dashboards**
- Select **New dashboard**
- Select **New visualization**

You will be redirected to the Edit panel screen.

## Configure the Live Sensor Query

In the Query section:

- **Data source:** PostgreSQL / TimescaleDB
- **Query type:** SQL
- **Format:** Time series

![Grafana time series panel editor showing the visualization configuration screen with the time series panel type selected and panel title field alt-txt#center](images/data-source-visualization.png "Grafana visualization configuration")

Paste the following query after selecting **Code** on the right of the query editor:

```sql
SELECT
  time AS "time",
  temperature
FROM sensor_data
WHERE $__timeFilter(time)
ORDER BY time;
```

![Grafana SQL query editor showing TimescaleDB query with time filter#center](images/timescale-query.png "TimescaleDB SQL query editor")

This query retrieves live sensor temperature data within the selected time range.

Apply the following settings in the right-hand panel:

  - Visualization Settings

    - **Visualization:** Time series
    - **Panel title:** Live Sensor Temperature
    - **Table view:** Disabled

  - Time & Refresh Settings

    - **Time range:** Last 5 minutes
    - **Refresh interval:** 5s

These settings ensure the panel refreshes automatically with new data.

## Validate the Live Sensor Panel

Once configured, the panel should display a continuously updating temperature graph.

![Grafana live sensor temperature time series panel showing a continuous line graph of temperature readings from multiple sensors over the last 5 minutes alt-txt#center](images/live-sensor-temperature.webp "Live sensor temperature panel")

## Save the dashboard

- Select **Save dashboard** (top-right corner)
- Enter a name, for example: Live Sensor Monitoring Dashboard
- Select **Save**

The dashboard is now active.

## What you've accomplished

You've built a complete time-series monitoring pipeline on Google Cloud C4A Axion Arm-based processors. TimescaleDB is running natively on Arm64, ingesting live sensor data through Python, and serving queries to Grafana for real-time visualization. From here you can add more sensors, create additional dashboards, set up alerting rules in Grafana, or tune TimescaleDB for your specific workload.
