#!/usr/bin/env python3
import os
import pandas as pd
import textwrap
from io import StringIO
import plotly.graph_objs as go

import typer

# Central hover template
HOVER_TMPL = "%{{x}}<br>{name}: %{{y:.4g}}<extra></extra>"

# Unified label wrapping
def wrap_label(lbl, width=20):
    parts = lbl.split('/')
    wrapped = []
    for part in parts:
        wrapped.extend(textwrap.wrap(part, width=width) or [''])
    return '<br>'.join(wrapped)


# Helper function for bar chart creation
def make_bar_chart(x_labels, y1, y2, name1, name2, title, xaxis_title, yaxis_title, out_path):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x_labels,
        y=y1,
        name=name1,
        marker_color='blue',
        hovertemplate=HOVER_TMPL.format(name=name1)
    ))
    fig.add_trace(go.Bar(
        x=x_labels,
        y=y2,
        name=name2,
        marker_color='orange',
        hovertemplate=HOVER_TMPL.format(name=name2)
    ))
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        barmode='stack',
        xaxis_tickfont=dict(size=12),
        xaxis_tickangle=-45,
        xaxis_tickmode='array',
        xaxis_tickvals=list(range(len(x_labels))),
        xaxis_ticktext=x_labels,
        xaxis_automargin=True,
        template='plotly_white',
        margin=dict(
            t=50,
            b=250 if xaxis_title == 'Benchmark' else 200,
            l=100,
            r=100
        )
    )
    fig.write_html(out_path)
    return out_path



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
        # Derive hostname from result filenames by taking first token before '-'
        raw_a = parts[1]
        raw_b = parts[3] if len(parts) > 3 else 'Unknown'
        inst_a = raw_a.split('-')[0]
        inst_b = raw_b.split('-')[0]
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

    # Identify value columns (every odd column after 'Benchmark')
    cols = df.columns.tolist()
    baseline_col = cols[1]
    compare_col = cols[3]

    grouped_data = df.groupby('Benchmark')[[baseline_col, compare_col]].mean()

    x = grouped_data.index.tolist()
    values_a = grouped_data[baseline_col].values
    values_b = grouped_data[compare_col].values

    # Wrap benchmark names
    wrapped_names = [wrap_label(lbl) for lbl in x]

    # Build comparison labels
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
            f"{inst_b} is {comparison} {inst_a}</span>"
        )

    html_filename = f"{metric_name}_{idx}.html".replace('/', '_').replace(' ', '_')
    html_path = os.path.join(out_dir, html_filename)
    return make_bar_chart(
        custom_labels,
        values_a,
        values_b,
        inst_a,
        inst_b,
        f"{metric_name} comparison",
        "Benchmark",
        metric_name,
        html_path
    )

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

    # insert HTML line breaks at slashes for metric names
    wrapped = [wrap_label(m) for m in metric_names]

    out_filename = 'overall_metrics.html'
    out_path = os.path.join(out_dir, out_filename)
    return make_bar_chart(
        wrapped,
        values_a,
        values_b,
        inst_a,
        inst_b,
        'Overall Metrics Geomean Comparison',
        'Metric',
        'Value',
        out_path
    )

def generate_html(images, out_dir):
    html_path = os.path.join(out_dir, 'report.html')
    with open(html_path, 'w') as html:
        html.write('<html><head><meta charset="utf-8"><title>Benchmark Report</title></head><body>\n')
        html.write('<h1>Benchmark Comparison Report</h1>\n')
        for img_path, metric_name, inst_a, inst_b in images:
            html.write(f'<h2>{metric_name} comparison between hosts {inst_a} and {inst_b}</h2>\n')
            html.write(f'<iframe src="{os.path.basename(img_path)}" width="100%" height="600" frameborder="0"></iframe>\n')
            html.write(
                f'<p>This visualization compares <strong>{metric_name}</strong> for benchmark cases '
                f'on instances <em>{inst_a}</em> and <em>{inst_b}</em>. '
                'Each bar represents the metric for a specific benchmark test.</p>\n'
            )
        html.write('</body></html>')
    print(f'Generated report at {html_path}')

def main(benchstat_file: str = '/tmp/benchstat.csv', out_dir: str = '/tmp'):
    groups = parse_benchstat(benchstat_file)
    images = []
    for idx, (inst_a, inst_b, metric_name, df) in enumerate(groups):
        img_path = plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx)
        images.append((img_path, metric_name, inst_a, inst_b))
    generate_html(images, out_dir)

if __name__ == '__main__':
    typer.run(main)