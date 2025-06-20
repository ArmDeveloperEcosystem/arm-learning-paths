import os
import textwrap
import plotly.graph_objs as go
from io import StringIO
import pandas as pd

def wrap_label(lbl, width=20):
    parts = lbl.split('/')
    wrapped = []
    for part in parts:
        wrapped.extend(textwrap.wrap(part, width=width) or [''])
    return '<br>'.join(wrapped)

def make_bar_chart(x_labels, y1, y2, name1, name2, title, xaxis_title, yaxis_title, out_path):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x_labels,
        y=y1,
        name=name1,
        marker_color='blue',
        hovertemplate="%{x}<br>%{name}: %{y:.4g}<extra></extra>"
    ))
    fig.add_trace(go.Bar(
        x=x_labels,
        y=y2,
        name=name2,
        marker_color='orange',
        hovertemplate="%{x}<br>%{name}: %{y:.4g}<extra></extra>"
    ))
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        barmode='group',
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
    sections = [sec.strip() for sec in content.split('\n\n') if sec.strip()]
    groups = []
    for sec in sections:
        lines = sec.splitlines()
        header_line = lines[0]
        parts = header_line.split(',')
        if len(parts) < 4:
            raise ValueError(f"Unexpected header format: {header_line}")
        raw_a = parts[1]
        raw_b = parts[3] if len(parts) > 3 else 'Unknown'
        # Strip any directory prefix so we only keep the basename
        base_a = os.path.basename(raw_a)
        base_b = os.path.basename(raw_b)
        # Now split on '-' to get just the instance name (e.g. 'c4' from 'c4-96.results')
        inst_a = base_a.split('-')[0] if '-' in base_a else base_a.split('.')[0]
        inst_b = base_b.split('-')[0] if '-' in base_b else base_b.split('.')[0]
        metric_name = lines[1].split(',')[1]
        csv_text = '\n'.join(lines[1:])
        df = pd.read_csv(StringIO(csv_text), engine='python')
        df.rename(columns={df.columns[0]: 'Benchmark'}, inplace=True)
        df['Benchmark'] = df['Benchmark'].str.replace(r'-\d+$', '', regex=True)
        groups.append((inst_a, inst_b, metric_name, df))
    return groups

def plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx):
    benchmarks = df['Benchmark'].unique()
    cols = df.columns.tolist()
    baseline_col = cols[1]
    compare_col = cols[3]
    grouped_data = df.groupby('Benchmark')[[baseline_col, compare_col]].mean()
    x = grouped_data.index.tolist()
    values_a = grouped_data[baseline_col].values
    values_b = grouped_data[compare_col].values
    wrapped_names = [wrap_label(lbl) for lbl in x]
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
    # Only print the path relative to CWD (no /tmp/tmp... prefix)
    rel_html = os.path.relpath(html_path, start=os.getcwd())
    print(f'Generated report at {rel_html}')
    return html_path