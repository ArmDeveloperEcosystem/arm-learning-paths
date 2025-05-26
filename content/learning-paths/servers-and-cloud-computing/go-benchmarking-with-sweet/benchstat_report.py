#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

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
        inst_a = parts[1]
        inst_b = parts[3]
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
    benchmarks = df['Benchmark']
    cols = df.columns.tolist()
    baseline_col = cols[1]
    compare_col = cols[3]
    values_a = df[baseline_col]
    values_b = df[compare_col]
    x = range(len(benchmarks))

    plt.figure()
    plt.bar([i-0.2 for i in x], values_a, width=0.4, label=inst_a)
    plt.bar([i+0.2 for i in x], values_b, width=0.4, label=inst_b)
    plt.xticks(x, benchmarks, rotation=45, ha='right')
    plt.ylabel(metric_name)
    plt.title(f"{metric_name} comparison")
    plt.legend()
    plt.tight_layout()

    img_filename = f"{metric_name}_{idx}.png".replace('/', '_').replace(' ', '_')
    img_path = os.path.join(out_dir, img_filename)
    plt.savefig(img_path)
    plt.close()
    return img_path

def generate_html(images, out_dir):
    html_path = os.path.join(out_dir, 'report.html')
    with open(html_path, 'w') as html:
        html.write('<html><head><meta charset="utf-8"><title>Benchmark Report</title></head><body>\n')
        html.write('<h1>Benchmark Comparison Report</h1>\n')
        for img_path, metric_name, inst_a, inst_b in images:
            html.write(f'<h2>{metric_name} comparison between {inst_a} and {inst_b}</h2>\n')
            html.write(f'<img src="{os.path.basename(img_path)}" alt="{metric_name}">\n')
            html.write(
                f'<p>This visualization compares <strong>{metric_name}</strong> for benchmark cases '
                f'on instances <em>{inst_a}</em> and <em>{inst_b}</em>. '
                'Each bar represents the metric for a specific benchmark test.</p>\n'
            )
        html.write('</body></html>')
    print(f'Generated report at {html_path}')

def main():
    benchstat_file = '/tmp/benchstat.out'
    out_dir = '/tmp'
    groups = parse_benchstat(benchstat_file)
    images = []
    for idx, (inst_a, inst_b, metric_name, df) in enumerate(groups):
        img_path = plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx)
        images.append((img_path, metric_name, inst_a, inst_b))
    generate_html(images, out_dir)

if __name__ == '__main__':
    main()