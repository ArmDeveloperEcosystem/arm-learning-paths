#!/usr/bin/env python3
# ANSI color codes for visual differentiation
COLORS = ['\033[94m', '\033[92m']  # blue, green
RESET = '\033[0m'

import os
import webbrowser
import subprocess
import threading
import tempfile
import sys
from datetime import datetime
import pandas as pd
import textwrap
from io import StringIO
import plotly.graph_objs as go

# == Benchstat Report Utilities ==

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
        inst_a = base_a.split('-')[0]
        inst_b = base_b.split('-')[0]
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

class BenchstatReport:
    """
    Encapsulate benchstat report generation logic.
    """
    def generate_report(self, benchstat_file: str, out_dir: str):
        groups = parse_benchstat(benchstat_file)
        images = []
        for idx, (inst_a, inst_b, metric_name, df) in enumerate(groups):
            img_path = plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx)
            images.append((img_path, metric_name, inst_a, inst_b))
        generate_html(images, out_dir)

# == GCP Helper Functions ==

def get_running_instances():
    """Return a list of names of GCP VMs that are currently RUNNING."""
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter=status=RUNNING",
             "--format=value(name)"],
            universal_newlines=True
        )
        instances = [line.strip() for line in output.splitlines() if line.strip()]
        return instances
    except subprocess.CalledProcessError as e:
        print("Error fetching running instances:", e, file=sys.stderr)
        return []

def choose_instance(instances):
    """Prompt user to choose an instance from the list."""
    if not instances:
        print("No running instances found.", file=sys.stderr)
        sys.exit(1)
    print("Select an instance:")
    for idx, name in enumerate(instances, 1):
        print(f"{idx}. {name}")
    while True:
        choice = input(f"Enter number (1-{len(instances)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(instances):
                return instances[idx - 1]
        print("Invalid selection, try again.")

def get_instance_zone(name):
    """Return the zone of the given GCP VM instance."""
    try:
        output = subprocess.check_output(
            ["gcloud", "compute", "instances", "list",
             "--filter", f"name={name}",
             "--format=value(zone)"],
            universal_newlines=True
        )
        zone = output.strip()
        if not zone:
            raise ValueError(f"No zone found for instance {name}")
        return zone
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error fetching zone for instance {name}: {e}", file=sys.stderr)
        sys.exit(1)

def scp_results(name, zone, remote_dir, local_out):
    """
    Copy back all files in remote_dir that match the benchstat inputs.
    Assumes sweet dumps its outputs in remote_dir (or subdir).
    Adjust the glob if needed.
    """
    remote_pattern = f"{remote_dir}/*.txt"
    scp_cmd = [
        "gcloud", "compute", "scp",
        f"{name}:{remote_pattern}",
        local_out,
        "--zone", zone
    ]
    subprocess.check_call(scp_cmd)

# == Benchmark Runner Helpers ==

# Cache for GCP instances list during runtime
cached_instances = None

def select_run_directory():
    """
    Prompt the user to select a benchmark-run subdirectory under ./results
    Returns (selected_dir, benchstat_file), or (None, None) if invalid.
    """
    results_root = os.path.join(os.getcwd(), "results")
    try:
        dirs = [
            d for d in os.listdir(results_root)
            if os.path.isdir(os.path.join(results_root, d))
        ]
    except FileNotFoundError:
        print("No results directory found.")
        return None, None

    if not dirs:
        print("No benchmark runs found in results directory.")
        return None, None

    # Sort directories by last‐modified time, newest first
    dirs.sort(
        key=lambda d: os.path.getmtime(os.path.join(results_root, d)),
        reverse=True
    )

    print("\nSelect a benchmark run to visualize:")
    default_idx = 0
    for idx, dirname in enumerate(dirs):
        default_marker = " (default)" if idx == default_idx else ""
        print(f"  {idx+1}. {dirname}{default_marker}")

    # Prompt the user, default = newest (index 0)
    while True:
        choice = input(f"Enter number (1-{len(dirs)}) [{default_idx+1}]: ").strip()
        if choice == "":
            selection = dirs[default_idx]
            break
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(dirs):
                selection = dirs[num-1]
                break
        print("Invalid selection, try again.")

    selected_dir = os.path.join(results_root, selection)
    benchstat_file = os.path.join(selected_dir, "benchstat.results")
    if not os.path.isfile(benchstat_file):
        print(f"No benchstat.results file found in {selected_dir}")
        return None, None

    return selected_dir, benchstat_file

def run_benchstat_report(benchstat_file, selected_dir):
    """
    Run benchstat report generation for the given benchstat_file into selected_dir.
    """
    # Strip any '/tmp/tmp...' prefix from filenames when printing
    short_input = os.path.basename(benchstat_file)
    short_outdir = os.path.relpath(selected_dir, start=os.getcwd())
    print(f"Generating report for {short_input}…")
    reporter = BenchstatReport()
    reporter.generate_report(benchstat_file, selected_dir)
    print(f"Report generated in {short_outdir}")
    # Automatically open the generated report in the default web browser
    html_path = os.path.join(selected_dir, 'report.html')
    abs_path = os.path.abspath(html_path)
    webbrowser.open(f"file://{abs_path}")

# == Main Execution ==

# map benchmark name → sweet command fragment
BENCHMARKS = {
    "biogo-igor":    'sweet run -count 10 -run="biogo-igor" config.toml',
    "biogo-krishna": 'sweet run -count 10 -run="biogo-krishna" config.toml',
    "bleve-index":   'sweet run -count 10 -run="bleve-index" config.toml',
    "cockroachdb":   'sweet run -count 10 -run="cockroachdb" config.toml',
    "esbuild":       'sweet run -count 10 -run="esbuild" config.toml',
    "etcd":          'sweet run -count 10 -run="etcd" config.toml',
    "go-build":      'sweet run -count 10 -run="go-build" config.toml',
    "gopher-lua":    'sweet run -count 10 -run="gopher-lua" config.toml',
    "gvisor":        'sweet run -count 10 -run="gvisor" config.toml',
    "markdown":      'sweet run -count 10 -run="markdown" config.toml',
    "tile38":        'sweet run -count 10 -run="tile38" config.toml',
}

def choose_benchmark():
    """Prompt user to choose a benchmark from the available list, defaulting to markdown."""
    names = list(BENCHMARKS.keys())
    print("Select a benchmark (default is markdown):")
    for idx, name in enumerate(names, 1):
        default_marker = " (default)" if name == "markdown" else ""
        print(f"{idx}. {name}{default_marker}")
    default_idx = names.index("markdown") + 1
    prompt_text = f"Enter number (1-{len(names)}) [{default_idx}]: "
    while True:
        choice = input(prompt_text).strip()
        if choice == "":
            return names[default_idx - 1]
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(names):
                return names[idx - 1]
        print("Invalid selection, try again.")

def prompt(prompt_text, default=None, validator=None):
    """
    Prompt the user with an optional default value.
    If validator is provided, loop until validator(value) is True.
    """
    while True:
        if default:
            ans = input(f"{prompt_text} [{default}]: ").strip()
            if ans == "":
                ans = default
        else:
            ans = input(f"{prompt_text}: ").strip()
        if validator is None or validator(ans):
            return ans
        print("Invalid value, please try again.")

def run_remote(name, zone, remote_dir, sweet_cmd, color):
    """
    SSH to the instance and run the sweet benchmark, streaming output.
    """
    ssh_cmd = [
        "gcloud", "compute", "ssh", name,
        "--zone", zone,
        "--command",
        f"export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; "
        f"export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
        f"cd {remote_dir} && {sweet_cmd}"
    ]
    p = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def reader():
        for line in iter(p.stdout.readline, b""):
            sys.stdout.write(f"{color}[{name}]{RESET} {line.decode()}")
    t = threading.Thread(target=reader, daemon=True)
    t.start()
    p.wait()
    if p.returncode != 0:
        print(f"[{name}] ⚠️ exited with code {p.returncode}")
    else:
        print(f"[{name}] ✅ benchmark completed")
    return p.returncode

def main():
    global cached_instances
    print("\n=== Benchmark Runner ===\n")

    # Prompt once for benchmark to run on both systems
    bench = choose_benchmark()
    systems = []

    for i in (1, 2):
        print(f"\n--- System {i} ---")
        # Fetch and cache the instance list once
        if cached_instances is None:
            print("Please wait while fetching the instances list...")
            cached_instances = get_running_instances()
        available = list(cached_instances)

        # On the second iteration, remove the instance already chosen
        if i == 2:
            first_choice = systems[0]["name"]
            if first_choice in available:
                available.remove(first_choice)

        # If only one instance remains, select it automatically
        if len(available) == 1:
            name = available[0]
            print(f"Only one instance available: {name}. Selecting it by default.")
        else:
            # Prompt user with the first instance as default
            print("Select an instance:")
            default_idx = 0
            for idx, inst in enumerate(available):
                default_marker = " (default)" if idx == default_idx else ""
                print(f"  {idx+1}. {inst}{default_marker}")
            while True:
                choice = input(f"Enter number (1-{len(available)}) [{default_idx+1}]: ").strip()
                if choice == "":
                    name = available[default_idx]
                    break
                if choice.isdigit():
                    num = int(choice)
                    if 1 <= num <= len(available):
                        name = available[num-1]
                        break
                print("Invalid selection, try again.")

        zone = get_instance_zone(name)
        remote_dir = prompt("Remote directory", default="~/benchmarks/sweet")
        systems.append({
            "name": name,
            "zone": zone,
            "bench": bench,
            "remote_dir": remote_dir,
            "cmd": BENCHMARKS[bench]
        })

    print("\nRunning benchmarks on the selected instances...")
    errors = []
    codes = {}
    threads = []

    for syscfg in systems:
        def run_and_store(syscfg=syscfg):
            idx = systems.index(syscfg)
            color = COLORS[idx % len(COLORS)]
            code = run_remote(
                syscfg["name"],
                syscfg["zone"],
                syscfg["remote_dir"],
                syscfg["cmd"],
                color
            )
            codes[syscfg["name"]] = code

        t = threading.Thread(target=run_and_store, daemon=True)
        t.start()
        threads.append(t)

    # Wait for benchmarks to finish
    for t in threads:
        t.join()

    # Collect failures
    for name, code in codes.items():
        if code != 0:
            errors.append(name)

    if errors:
        print("\n⚠️ Some benchmarks failed. Aborting benchstat step.")
        sys.exit(1)

    # Identify primary and secondary systems
    primary = systems[1]
    secondary = systems[0]

    # Create a remote temp directory on the primary VM
    mktemp_cmd = [
        "gcloud", "compute", "ssh", primary["name"],
        "--zone", primary["zone"],
        "--command", "mktemp -d"
    ]
    remote_tmp = subprocess.check_output(mktemp_cmd, universal_newlines=True).strip()
    print(f"Created remote temp dir on {primary['name']}: {remote_tmp}")

    # Copy result files locally and push back to primary
    with tempfile.TemporaryDirectory() as tmp:
        local_sec = os.path.join(tmp, f"{secondary['name']}.results")
        print(f"Copying {secondary['name']} results to local: {local_sec}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            f"{secondary['name']}:{secondary['remote_dir']}/results/{bench}/*.results",
            local_sec,
            "--zone", secondary["zone"]
        ])

        local_prim = os.path.join(tmp, f"{primary['name']}.results")
        print(f"Copying {primary['name']} results to local: {local_prim}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            f"{primary['name']}:{primary['remote_dir']}/results/{bench}/*.results",
            local_prim,
            "--zone", primary["zone"]
        ])

        print(f"Pushing {secondary['name']} results to {primary['name']}:{remote_tmp}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            local_sec,
            f"{primary['name']}:{remote_tmp}/{secondary['name']}.results",
            "--zone", primary["zone"]
        ])

        print(f"Pushing {primary['name']} results to {primary['name']}:{remote_tmp}")
        subprocess.check_call([
            "gcloud", "compute", "scp",
            local_prim,
            f"{primary['name']}:{remote_tmp}/{primary['name']}.results",
            "--zone", primary["zone"]
        ])

    # Run benchstat on the primary VM
    benchstat_cmd = (
        f"benchstat -format csv "
        f"{remote_tmp}/{secondary['name']}.results "
        f"{remote_tmp}/{primary['name']}.results > {remote_tmp}/benchstat.results"
    )
    ls_cmd = (
        f"ls -al {remote_tmp}/{secondary['name']}.results "
        f"{remote_tmp}/{primary['name']}.results {remote_tmp}/benchstat.results"
    )
    ssh_cmd = [
        "gcloud", "compute", "ssh", primary["name"],
        "--zone", primary["zone"],
        "--command",
        (
            "export GOPATH=$HOME/go; export GOBIN=$GOPATH/bin; "
            "export PATH=$PATH:$GOBIN:/usr/local/go/bin; "
            f"{benchstat_cmd} && echo \"Results files:\" && {ls_cmd}"
        )
    ]
    subprocess.check_call(ssh_cmd)

    # Pull all results back to local 'results' directory
    local_root = os.path.join(os.getcwd(), "results")
    os.makedirs(local_root, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    subdir = f"{secondary['name']}-{primary['name']}-{bench}-{timestamp}"
    local_dir = os.path.join(local_root, subdir)
    os.makedirs(local_dir, exist_ok=True)
    print(f"Copying all result files to local directory: {local_dir}")

    for fname in [
        f"{secondary['name']}.results",
        f"{primary['name']}.results",
        "benchstat.results"
    ]:
        subprocess.check_call([
            "gcloud", "compute", "scp",
            f"{primary['name']}:{remote_tmp}/{fname}",
            local_dir, "--zone", primary["zone"]
        ])

    # After copying benchstat.results locally, use helper to select and generate report
    selected_dir, benchstat_file = select_run_directory()
    if selected_dir and benchstat_file:
        run_benchstat_report(benchstat_file, selected_dir)


if __name__ == "__main__":
    main()