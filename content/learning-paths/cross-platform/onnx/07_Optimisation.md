---
title: "Model Enhancements and Optimizations"
weight: 8
layout: "learningpathall"
---

## Objective
In this section, we improve the Sudoku system from a working prototype into something that is faster, smaller, and more robust on Arm64-class hardware. We start by measuring a baseline, then apply ONNX Runtime optimizations and quantization, and finally address the most common real bottleneck: image preprocessing. At each step we re-check accuracy and solve rate so performance gains don’t come at the cost of correctness.

## Establish a baseline
Before applying any optimizations, it is essential to understand where time is actually being spent in the Sudoku pipeline. Without this baseline, it is impossible to tell whether an optimization is effective or whether it simply shifts the bottleneck elsewhere.

In the current system, the total latency of processing a single Sudoku image is composed of four main stages:
* Grid detection and warping – locating the outer Sudoku grid and rectifying it using a perspective transform. This step relies entirely on OpenCV and depends on image resolution, lighting, and grid clarity.
* Cell preprocessing – converting each of the 81 cells into a normalized 28×28 grayscale input for the neural network. This includes cropping margins, thresholding, and morphological operations. In practice, this stage is often the dominant cost.
* ONNX inference – running the digit recognizer on all 81 cells as a single batch. Thanks to dynamic batch support, this step is typically fast compared to preprocessing.
* Solving – applying a backtracking Sudoku solver to the recognized board. This step is usually negligible in runtime, unless recognition errors lead to difficult or contradictory boards.

To quantify these contributions, we will add simple timing measurements around each stage of the pipeline using a high-resolution clock (time.perf_counter()). For each processed image, we will print a breakdown:
* warp_ms – time spent on grid detection and perspective rectification
* preprocess_ms – total time spent preprocessing all 81 cells
* onnx_ms – time spent running batched ONNX inference
* solve_ms – time spent solving the Sudoku
* total_ms – end-to-end processing time

## Performance measurements
Open the sudoku_processor.py and add the following import

```python
import time
```

Then, modify the process_image as follows
```python
def process_image(self, bgr: np.ndarray, overlay: bool = True):
        """
        Returns:
        board (9x9 ints with 0 for blank),
        solved_board (9x9 ints, or None if unsolved),
        debug dict (warped, homography, confidence, timing),
        overlay_bgr (optional solution overlay)
        """
        timing = {}

        t_total0 = time.perf_counter()

        # --- Grid detection + warp ---
        t0 = time.perf_counter()
        warped, H, quad = self.detect_and_warp_board(bgr)
        timing["warp_ms"] = (time.perf_counter() - t0) * 1000.0

        # --- Cell splitting ---
        t0 = time.perf_counter()
        cells = self.split_cells(warped)
        timing["split_ms"] = (time.perf_counter() - t0) * 1000.0

        # --- Preprocessing (81 cells) ---
        t0 = time.perf_counter()
        xs = []
        coords = []
        for r, c, cell in cells:
            coords.append((r, c))
            xs.append(self.preprocess_cell(cell))
        X = np.concatenate(xs, axis=0).astype(np.float32)  # [81,1,28,28]
        timing["preprocess_ms"] = (time.perf_counter() - t0) * 1000.0

        # --- ONNX inference ---
        t0 = time.perf_counter()
        logits = self.sess.run([self.output_name], {self.input_name: X})[0]
        timing["onnx_ms"] = (time.perf_counter() - t0) * 1000.0

        # --- Postprocess predictions ---
        probs = softmax(logits, axis=1)
        pred = probs.argmax(axis=1)
        conf = probs.max(axis=1)

        board = [[0 for _ in range(9)] for _ in range(9)]
        conf_grid = [[0.0 for _ in range(9)] for _ in range(9)]
        for i, (r, c) in enumerate(coords):
            p = int(pred[i])
            cf = float(conf[i])
            if cf < self.blank_conf_threshold:
                p = self.blank_class
            board[r][c] = p
            conf_grid[r][c] = cf

        # --- Solve ---
        t0 = time.perf_counter()
        solved = [row[:] for row in board]
        ok = solve_sudoku(solved)
        timing["solve_ms"] = (time.perf_counter() - t0) * 1000.0

        # --- Overlay (optional) ---
        overlay_img = None
        if overlay and ok:
            t0 = time.perf_counter()
            overlay_img = self.overlay_solution(bgr, H, board, solved)
            timing["overlay_ms"] = (time.perf_counter() - t0) * 1000.0
        else:
            timing["overlay_ms"] = 0.0

        timing["total_ms"] = (time.perf_counter() - t_total0) * 1000.0

        debug = {
            "warped": warped,
            "homography": H,
            "quad": quad,
            "confidence": conf_grid,
            "timing": timing,
        }

        return board, (solved if ok else None), debug, overlay_img
```

Finally, print the timings in the 05_RunSudokuProcessor.py:
```python
def main():
    # Use any image path you like:
    # - a real photo 
    # - a synthetic grid, e.g. data/grids/val/000001_cam.png
    img_path = "data/grids/val/000002_cam.png"
    onnx_path = os.path.join("artifacts", "sudoku_digitnet.onnx")

    bgr = cv.imread(img_path)
    if bgr is None:
        raise RuntimeError(f"Could not read image: {img_path}")

    proc = SudokuProcessor(onnx_path=onnx_path, warp_size=450, blank_conf_threshold=0.65)

    board, solved, dbg, overlay = proc.process_image(bgr, overlay=True)

    print_board(board, "Recognized board")
    if solved is None:
        print("\nSolver failed (board might contain recognition errors).")
    else:
        print_board(solved, "Solved board")

    # Save debug outputs
    cv.imwrite("artifacts/warped.png", dbg["warped"])
    if overlay is not None:
        cv.imwrite("artifacts/overlay_solution.png", overlay)
        print("\nSaved: artifacts/overlay_solution.png")
    print("Saved: artifacts/warped.png")

    tim = dbg["timing"]
    print(
        f"warp={tim['warp_ms']:.1f} ms | "
        f"preprocess={tim['preprocess_ms']:.1f} ms | "
        f"onnx={tim['onnx_ms']:.1f} ms | "
        f"solve={tim['solve_ms']:.1f} ms | "
        f"total={tim['total_ms']:.1f} ms"
    )

if __name__ == "__main__":
    main()
```

The sample output will look as follows:
```output
python3 05_RunSudokuProcessor.py

Recognized board
. . . | 7 . . | 6 . .
. . 4 | . . . | 1 . 9
. . . | 1 5 . | . . .
---------------------
. . . | . 1 . | . . .
. . . | . . . | . . .
3 . . | . . . | . 6 .
---------------------
7 . . | . . . | . . .
. . 9 | . . . | . . .
. . . | . . . | . . .

Solved board
1 2 3 | 7 4 9 | 6 5 8
5 6 4 | 2 3 8 | 1 7 9
8 9 7 | 1 5 6 | 2 3 4
---------------------
2 4 5 | 6 1 3 | 8 9 7
9 1 6 | 4 8 7 | 3 2 5
3 7 8 | 5 9 2 | 4 6 1
---------------------
7 3 1 | 8 2 5 | 9 4 6
4 5 9 | 3 6 1 | 7 8 2
6 8 2 | 9 7 4 | 5 1 3

Saved: artifacts/overlay_solution.png
Saved: artifacts/warped.png
warp=11.9 ms | preprocess=3.3 ms | onnx=1.9 ms | solve=3.1 ms | total=48.2 ms
```

## Folder benchmark
The single-image measurements introduced earlier are useful for understanding the rough structure of the pipeline and for verifying that ONNX inference is not the main computational bottleneck. In our case, batched ONNX inference typically takes less than 2 ms, while grid detection, warping, and preprocessing dominate the runtime. However, individual measurements can be noisy due to caching effects, operating system scheduling, and Python overhead.

To obtain more reliable performance numbers, we extend the evaluation to multiple images and compute aggregated statistics. This allows us to track not only average performance, but also variability and tail latency, which are particularly important for interactive applications.

To do this, we add two helper functions to 05_RunSudokuProcessor.py.

The first function, summarize, computes basic statistics from a list of timing measurements:
* mean – average runtime
* median – robust central tendency
* p90 / p95 – tail latency (90th and 95th percentiles), which indicate how bad the slow cases are

```python
def summarize(values):
    values = np.asarray(values, dtype=np.float64)
    return {
        "mean": float(values.mean()),
        "median": float(np.median(values)),
        "p90": float(np.percentile(values, 90)),
        "p95": float(np.percentile(values, 95)),
    }
```

The second function, benchmark_folder, runs the full Sudoku pipeline on a collection of images and aggregates timing results across multiple runs:

```python
def benchmark_folder(proc, folder_glob, limit=100, warmup=10, overlay=False):
    paths = sorted(glob.glob(folder_glob))
    if not paths:
        raise RuntimeError(f"No images matched: {folder_glob}")
    paths = paths[:limit]

    # Warmup
    for p in paths[:min(warmup, len(paths))]:
        bgr = cv.imread(p)
        if bgr is None:
            continue
        proc.process_image(bgr, overlay=overlay)

    # Benchmark
    agg = {k: [] for k in ["warp_ms", "preprocess_ms", "onnx_ms", "solve_ms", "total_ms"]}
    solved_cnt = 0
    total_cnt = 0

    for p in paths:
        bgr = cv.imread(p)
        if bgr is None:
            continue

        board, solved, dbg, _ = proc.process_image(bgr, overlay=overlay)
        tim = dbg["timing"]

        for k in agg:
            agg[k].append(tim[k])

        total_cnt += 1
        if solved is not None:
            solved_cnt += 1

    print(f"\nSolved {solved_cnt}/{total_cnt} ({(solved_cnt/total_cnt*100.0 if total_cnt else 0):.1f}%)")

    print("\nTiming summary (ms):")
    for k in ["warp_ms", "preprocess_ms", "onnx_ms", "solve_ms", "total_ms"]:
        s = summarize(agg[k])
        print(f"{k:14s}  mean={s['mean']:.2f}  median={s['median']:.2f}  p90={s['p90']:.2f}  p95={s['p95']:.2f}")
```

Finally, we invoke the benchmark in the main() function:

```python
def main():
    onnx_path = os.path.join("artifacts", "sudoku_digitnet.onnx")
    
    proc = SudokuProcessor(onnx_path=onnx_path, warp_size=450, blank_conf_threshold=0.65)

    benchmark_folder(proc, "data/grids/val/*_cam.png", limit=30, warmup=10, overlay=False)

if __name__ == "__main__":
    main()
```

This evaluates the processor on a representative subset of camera-like validation grids, prints aggregated timing statistics, and reports the overall solve rate.

Aggregated benchmarks provide a much more accurate picture than single measurements, especially when individual stages take only a few milliseconds. By reporting median and tail latencies, you can see whether occasional slow cases exist and whether an optimization truly improves user-perceived performance. Percentiles are particularly useful when a few slow cases exist (e.g., harder solves), because they reveal tail latency. These results form a solid quantitative baseline that you can reuse to evaluate every optimization that follows.

Here is the sample output of the updated script:
```output
python3 05_RunSudokuProcessor.py

Solved 30/30 (100.0%)

Timing summary (ms):
warp_ms         mean=10.25  median=10.27  p90=10.57  p95=10.59
preprocess_ms   mean=3.01  median=2.98  p90=3.16  p95=3.21
onnx_ms         mean=1.27  median=1.24  p90=1.30  p95=1.45
solve_ms        mean=74.76  median=2.02  p90=48.51  p95=74.82
total_ms        mean=89.41  median=16.97  p90=62.95  p95=89.43
```

Notice that solve_ms (and therefore total_ms) has a much larger mean than median. This indicates a small number of outliers where the solver takes significantly longer. In practice, this occurs when one or more digits are misrecognized, forcing the backtracking solver to explore many branches before finding a solution (or failing). For interactive applications, median and p95 latency are more informative than the mean, as they better reflect typical user experience.

## ONNX Runtime session optimizations
Now that you can measure onnx_ms and total_ms, the first low-effort improvement is to enable ONNX Runtime’s built-in graph optimizations and tune CPU threading. These changes do not modify the model, but can reduce inference overhead and improve throughput.

In sudoku_processor.py, update the ONNX Runtime session initialization in __init__ to use SessionOptions:
```python
so = ort.SessionOptions()
so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

self.sess = ort.InferenceSession(onnx_path, sess_options=so, providers=list(providers))
```

Re-run 05_RunSudokuProcessor.py and compare onnx_ms and total_ms to the baseline. 

```output
python3 05_RunSudokuProcessor.py

Solved 30/30 (100.0%)

Timing summary (ms):
warp_ms         mean=10.43  median=10.36  p90=10.89  p95=10.96
preprocess_ms   mean=3.13  median=3.11  p90=3.34  p95=3.42
onnx_ms         mean=1.28  median=1.26  p90=1.37  p95=1.47
solve_ms        mean=78.61  median=2.01  p90=50.15  p95=77.87
total_ms        mean=93.58  median=17.06  p90=65.10  p95=92.55
```

This result is expected for such a small model: ONNX inference is already efficient, and the dominant costs lie in image preprocessing and occasional solver backtracking. This highlights why system-level profiling is essential before focusing on model-level optimizations.

## Quantize the model (FP32 -> INT8)
Quantization is one of the most impactful optimizations for Arm64 and mobile deployments because it reduces both model size and compute cost. The simplest approach is dynamic quantization, which requires no calibration dataset and is quick to apply.

Create a small script 06_QuantizeModel.py:

```python
import os, glob
import numpy as np
import cv2 as cv

from onnxruntime.quantization import (
    quantize_static, CalibrationDataReader, QuantFormat, QuantType
)

ARTI_DIR = "artifacts"
FP32_PATH = os.path.join(ARTI_DIR, "sudoku_digitnet.onnx") 
INT8_PATH = os.path.join(ARTI_DIR, "sudoku_digitnet.int8.onnx")

# ---- Calibration data reader ----
class SudokuCalibReader(CalibrationDataReader):
    def __init__(self, folder_glob="data/train/0/*.png", limit=500, input_name="input", input_size=28):
        self.input_name = input_name
        self.input_size = input_size

        paths = sorted(glob.glob(folder_glob))[:limit]
        self._iter = iter(paths)

    def get_next(self):
        try:
            p = next(self._iter)
        except StopIteration:
            return None

        g = cv.imread(p, cv.IMREAD_GRAYSCALE)
        if g is None:
            return self.get_next()

        g = cv.resize(g, (self.input_size, self.input_size), interpolation=cv.INTER_AREA)
        x = g.astype(np.float32) / 255.0
        x = (x - 0.5) / 0.5
        x = x[None, None, :, :]  # [1,1,28,28]
        return {self.input_name: x}

# ---- Run quantization ----
reader = SudokuCalibReader(folder_glob="data/train/*/*.png", limit=1000)

print("Quantizing (QDQ static INT8)...")
quantize_static(
    model_input=FP32_PATH,
    model_output=INT8_PATH,
    calibration_data_reader=reader,
    quant_format=QuantFormat.QDQ,          # key: keep Conv as Conv with Q/DQ wrappers
    activation_type=QuantType.QInt8,
    weight_type=QuantType.QInt8,
    per_channel=True                       # usually helps conv accuracy
)

print("Saved:", INT8_PATH)
```

Run python 06_QuantizeModel.py

Then update the runner script to point to the quantized model:

```python
onnx_path = os.path.join("artifacts", "sudoku_digitnet.int8.onnx")
```

Re-run the processor and compare:
* onnx_ms (should improve or remain similar)
* total_ms
* solve success (should remain stable)

Also compare file sizes:
```console
ls -lh artifacts/sudoku_digitnet.onnx artifacts/sudoku_digitnet.int8.onnx
```
Even when inference time changes only modestly, size reduction is typically significant and matters for Android packaging. 

In this pipeline, quantization primarily reduces model size and improves deployability, while runtime speedups may be modest because inference is already a small fraction of the total latency.

## Preprocessing-focused optimizations (highest impact)
The measurements above show that ONNX inference accounts for only a small fraction of the total runtime. In practice, the largest performance gains come from optimizing image preprocessing.

The most effective improvements include:
- Converting the rectified board to grayscale **once**, instead of converting each cell independently.
- Adding an early “blank cell” check to skip expensive thresholding and morphology for empty cells.
- Using simpler thresholding (e.g., Otsu) on clean images, and reserving adaptive thresholding for difficult lighting conditions.
- Reducing or conditionally disabling morphological operations when cells already appear clean.

These changes typically reduce `preprocess_ms` more than any model-level optimization, and therefore have the greatest impact on end-to-end latency.

## Summary
In this section, we transformed the Sudoku solver from a functional prototype into a system with measurable, well-understood performance characteristics. By instrumenting the pipeline with fine-grained timing, we identified where computation is actually spent and established a quantitative baseline.

We showed that:
- Batched ONNX inference is already efficient (≈1–2 ms per board).
- Image preprocessing dominates runtime and offers the largest optimization potential.
- Solver backtracking introduces rare but significant tail-latency outliers.
- ONNX Runtime optimizations and INT8 quantization improve deployability, even when raw inference speed gains are modest.

Most importantly, we demonstrated a systematic optimization workflow: **measure first, optimize second, and always re-validate correctness**. With performance, robustness, and accuracy validated, the Sudoku pipeline is now ready for its final step—deployment as a fully on-device Android application.