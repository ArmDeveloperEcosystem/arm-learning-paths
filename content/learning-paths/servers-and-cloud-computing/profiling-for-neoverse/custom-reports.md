---
title: Custom reports
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## 4 Custom reports

The Streamline CLI analysis tool, `sl-analyze`, outputs a raw CSV file
containing all of the profiling metrics that were generated. For a complex
application, this is large and difficult to use for manual review.

The `sl-format.py` script provides a method to extract a filtered subset of the
data to an XLSX spreadsheet, including generation of interactive tables and
custom cell formatting. The presentation format is specified using a YAML
configuration file, allowing easy reconfiguration of the visualization.

The script requires a PMU-based profile, and can optionally merge in results
from an SPE-based profile.

### 4.1. Passing a custom configuration

Optionally, you can pass a custom configuration file using the `--config`
argument.

```sh
python3 sl-format.py -o <out.xlsx> <in.csv> [--config <conf.yaml>]
```

If no configuration is specified, a default presentation suitable for a profile
recorded using `-C workflow_topdown_basic` is used.

### 4.2. Configuration syntax

The configuration file is a YAML file containing an ordered list of metrics.
Each metric is presented as a column in the output table, with each identified
application function in the source application as a row.

#### 4.2.1 Basic syntax

Each metric must specify the data `src_name`, which is the column title in the
input CSV file. The metrics can optionally specify the `dst_name`, which is the
column name to use in the XLSX output. If no `dst_name` is specified, the
`src_name` is used.

```yaml
---
- series:
    src_name: symbol
    dst_name: Function
- series:
    src_name: "Metrics: Sample Count"
    dst_name: Samples
...
```

#### 4.2.2 Symbol name series

The raw function names (`src_name: symbol`) in the CSV include full parameter
lists, which can help disambiguating functions in software that makes heavy use
of operator overloading. In many applications this is not necessary and simply
clutters the visualization. You can set `strip_params: true` for the `symbol`
source column to discard parameters.

Arm recommends that the series for the function name, as well as other
string-like columns, include the `dtype: str` property. This property stops
empty cells in these columns being interpreted as a floating point NaN value.

#### 4.2.3 Symbol filtering

The raw data includes all symbols that were sampled during the profile. Many
symbols are often of low significance, with few samples compared to the overall
sample count. The formatted data can discard low significance rows to make the
data easier to use.

To enable filtering for a series, you can add the following options:

* `filter: significance`, and
* `min_row_significance: <val>` with a significance value between 0 and 1.

For example, a minimum significance of 0.01 in the "samples" column indicates
that any function with fewer than 1% of the total samples should be discarded.

#### 4.2.4 Column highlight styles

Data columns can include basic styling rules to help highlight cells with
values that are worth investigating.

##### `style: absolute_ramp_up`

```yaml
- series:
    style: absolute_ramp_up
    min_ramp: 2
    max_ramp: 4
```

This style is based on the absolute value of each cell. It increases from no
highlight for a value below `min_ramp` to a maximum intensity highlight for a
value above `max_ramp`.

##### `style: absolute_ramp_down`

```yaml
- series:
    style: absolute_ramp_down
    min_ramp: 2
    max_ramp: 4
```

This style is based on the absolute value of each cell. It increases from no
highlight for a value above `max_ramp` to a maximum intensity highlight for a
value below `min_ramp`.

##### `style: relative_ramp_up`

```yaml
- series:
    style: relative_ramp_up
    min_ramp: 0.9
    max_ramp: 1.0
```

This style is based on the value of a cell relative to the min/max range of the
column, where a threshold of 0.0 indicates the minimum value of the column and
1.0 indicates the maximum value of the column. The example above highlights
cells in the top 10% of the column range.

It increases from no highlight for a relative value below `min_ramp` to a
maximum intensity highlight for a relative value above `max_ramp`.

##### `style: relative_ramp_down`

```yaml
- series:
    style: relative_ramp_down
    min_ramp: 0.0
    max_ramp: 0.1
```

This style is based on the value of a cell relative to the min/max range of the
column, where a threshold of 0.0 indicates the minimum value of the column and
1.0 indicates the maximum value of the column. The example above highlights
cells in the bottom 10% of the column range.

It increases from no highlight for a relative value above `max_ramp` to a
maximum intensity highlight for a relative value below `min_ramp`.

##### `style: stdev_ramp_up`

```yaml
- series:
    style: stdev_ramp_up
    min_ramp: 0.5
    max_ramp: 1.0
```

This style is based on the value of a cell relative to the number of standard
deviations from the mean. A threshold of N indicates a value that is N standard
deviations from the mean. The example above starts highlighting cells that are
0.5 standard deviations higher than the mean, ramping to full intensity for
cells that are 1 standard deviation higher than the mean.

It increases from no highlight for a value below `min_ramp` standard
deviations, to a maximum intensity highlight for a value above `max_ramp`
standard deviations.

##### `style: stdev_ramp_down`

```yaml
- series:
    style: stdev_ramp_down
    min_ramp: -1.0
    max_ramp: -0.5
```

This style is based on the value of a cell relative to the number of standard
deviations from the mean. A threshold of N indicates a value that is N standard
deviations from the mean. The example above starts highlighting cells that are
0.5 standard deviations lower than the mean, ramping to full intensity for
cells that are 1 standard deviation lower than the mean.

It increases from no highlight for a value above `max_ramp` standard
deviations, to a maximum intensity highlight for a value below `min_ramp`
standard deviations.