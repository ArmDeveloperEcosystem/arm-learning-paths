#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from io import StringIO
import mplcursors
import plotly.graph_objs as go
import plotly.io as pio

def parse_benchstat(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    # Split into metric groups separated by blank lines
    sections = [sec.strip() for sec in content.split('\n\n') if sec.strip()]
    groups = []
    for sec in sections:
        lines = sec.splitlines()
        # First line contains instance file paths
        header_line = lines[0]
        parts = header_line.split(',')
        if len(parts) < 4:
            raise ValueError(f"Unexpected header format: {header_line}")
        inst_a = parts[1]
        inst_b = parts[3] if len(parts) > 3 else 'Unknown'
        # Second line names the metric
        metric_name = lines[1].split(',')[1]
        # Build CSV text from header+data lines
        csv_text = '\n'.join(lines[1:])
        df = pd.read_csv(StringIO(csv_text), engine='python')
        # Rename first column to 'Benchmark'
        df.rename(columns={df.columns[0]: 'Benchmark'}, inplace=True)
        # Strip concurrency suffix (e.g. "-96") from benchmark names:
        df['Benchmark'] = df['Benchmark'].str.replace(r'-\d+$', '', regex=True)
        groups.append((inst_a, inst_b, metric_name, df))
    return groups

def plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx):
    benchmarks = df['Benchmark'].unique()
    # Wrap long benchmark names for display
    wrapped_names = [lbl.replace('/', '\n') for lbl in benchmarks]

    # Identify value columns (every odd column after 'Benchmark')
    cols = df.columns.tolist()
    baseline_col = cols[1]
    compare_col = cols[3]

    grouped_data = df.groupby('Benchmark')[[baseline_col, compare_col]].mean()

    x = grouped_data.index.tolist()
    values_a = grouped_data[baseline_col].values
    values_b = grouped_data[compare_col].values

    # wrap long benchmark names at ~20 characters
    wrapped_names = [
        '<br>'.join(textwrap.wrap(lbl, width=20))
        for lbl in x
    ]

    custom_labels = []
    for i, name in enumerate(wrapped_names):
        a = values_a[i]
        b = values_b[i]
        if a == 0:
            comparison = "undefined"
        else:
            pct_diff = ((b - a) / a) * 100
            dir_sym = ">" if pct_diff > 0 else "<"
            comparison = f"{abs(pct_diff):.1f}% {dir_sym}"
        custom_labels.append(
            f"{name}<br><span style='font-size:0.8em'>"
            f"Instance 2: {comparison} Instance 1</span>"
        )

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=custom_labels,
        y=values_a,
        name=f'Instance 1 ({inst_a})',
        marker_color='blue',
        hovertemplate='%{x}<br>Instance 1: %{y:.4g}<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        x=custom_labels,
        y=values_b,
        name=f'Instance 2 ({inst_b})',
        marker_color='orange',
        hovertemplate='%{x}<br>Instance 2: %{y:.4g}<extra></extra>'
    ))

    fig.update_layout(
        title=f"{metric_name} comparison",
        xaxis_title="Benchmark",
        yaxis_title=metric_name,
        barmode='group',
        xaxis_tickfont=dict(size=12),    # smaller font
        xaxis_tickangle=-45,             # rotate labels
        xaxis_tickmode='array',
        xaxis_tickvals=list(range(len(custom_labels))),
        xaxis_ticktext=custom_labels,
        xaxis_automargin=True,           # auto-expand margins
        template='plotly_white',
        margin=dict(t=50, b=250, l=100, r=100)
    )

    html_filename = f"{metric_name}_{idx}.html".replace('/', '_').replace(' ', '_')
    html_path = os.path.join(out_dir, html_filename)
    fig.write_html(html_path)
    return html_path

def plot_overall_metrics(groups, out_dir):
    """
    Plot a combined bar chart of geomean values for each metric type, comparing two instances.
    """
    metric_names = []
    values_a = []
    values_b = []
    inst_a, inst_b = groups[0][0], groups[0][1]
    for _, _, metric_name, df in groups:
        geo = df[df['Benchmark'] == 'geomean']
        if geo.empty:
            continue
        cols = df.columns.tolist()
        val_a = geo.iloc[0][cols[1]]
        val_b = geo.iloc[0][cols[3]]
        metric_names.append(metric_name)
        values_a.append(val_a)
        values_b.append(val_b)

    # wrap & rotate the overall-metric labels too
    wrapped = [
        m.replace('/', '\n')
        for m in metric_names
    ]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=wrapped,
        y=values_a,
        name=inst_a,
        marker_color='blue',
        hovertemplate='%{x}<br>' + inst_a + ': %{y:.4g}<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        x=wrapped,
        y=values_b,
        name=inst_b,
        marker_color='orange',
        hovertemplate='%{x}<br>' + inst_b + ': %{y:.4g}<extra></extra>'
    ))

    fig.update_layout(
        title='Overall Metrics Geomean Comparison',
        xaxis_title='Metric',
        yaxis_title='Value',
        barmode='group',
        xaxis_tickfont=dict(size=12),
        xaxis_tickangle=-45,
        xaxis_tickmode='array',
        xaxis_tickvals=list(range(len(wrapped))),
        xaxis_ticktext=wrapped,
        xaxis_automargin=True,
        template='plotly_white',
        margin=dict(t=50, b=200)
    )

    out_filename = 'overall_metrics.html'
    out_path = os.path.join(out_dir, out_filename)
    fig.write_html(out_path)
    return out_path

def generate_html(images, out_dir):
    html_path = os.path.join(out_dir, 'report.html')
    with open(html_path, 'w') as html:
        html.write('<html><head><meta charset="utf-8"><title>Benchmark Report</title></head><body>\n')
        html.write('<h1>Benchmark Comparison Report</h1>\n')
        for img_path, metric_name, inst_a, inst_b in images:
            html.write(f'<h2>{metric_name} comparison between {inst_a} and {inst_b}</h2>\n')
            html.write(f'<iframe src="{os.path.basename(img_path)}" width="100%" height="600" frameborder="0"></iframe>\n')
            html.write(
                f'<p>This visualization compares <strong>{metric_name}</strong> for benchmark cases '
                f'on instances <em>{inst_a}</em> and <em>{inst_b}</em>. '
                'Each bar represents the metric for a specific benchmark test.</p>\n'
            )
        html.write('</body></html>')
    print(f'Generated report at {html_path}')

def main():
    benchstat_file = '/tmp/benchstat.csv'
    out_dir = '/tmp'
    groups = parse_benchstat(benchstat_file)
    # Create combined geomean metrics chart
    overall_img = plot_overall_metrics(groups, out_dir)
    # Initialize images list with overall chart first
    images = [(overall_img, 'Overall (geomean)', groups[0][0], groups[0][1])]
    for idx, (inst_a, inst_b, metric_name, df) in enumerate(groups):
        img_path = plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx)
        images.append((img_path, metric_name, inst_a, inst_b))
    generate_html(images, out_dir)

if __name__ == '__main__':
    main()