---
# User change
title: "Preparing a Synthetic Sudoku Digit Dataset"

weight: 4

layout: "learningpathall"
---

## Big picture
Our end goal is a camera-to-solution Sudoku app that runs efficiently on Arm64 devices (e.g., Raspberry Pi or Android phones). ONNX is the glue: we’ll train the digit recognizer in PyTorch, export it to ONNX, and run it anywhere with ONNX Runtime (CPU EP on edge devices, NNAPI EP on Android). Everything around the model—grid detection, perspective rectification, and solving—stays deterministic and lightweight.

## Objective
In this step, we will generate a custom dataset of Sudoku puzzles and their digit crops, which we’ll use to train a digit recognition model. Starting from a Hugging Face parquet dataset that provides paired puzzle/solution strings, we transform raw boards into realistic, book-style Sudoku pages, apply camera-like augmentations to mimic mobile captures, and automatically slice each page into 81 labeled cell images. This yields a large, diverse, perfectly labeled set of digits (0–9 with 0 = blank) without manual annotation. By the end, you’ll have a structured dataset ready to train a lightweight model in the next section.

## Why Synthetic Generation?
When building a Sudoku digit recognizer, the hardest part is obtaining a well-labeled dataset that matches real capture conditions. MNIST contains handwritten digits, which differ from printed, grid-aligned Sudoku digits; relying on it alone hurts real-world performance.

By generating synthetic Sudoku pages directly from the parquet dataset, we get:
1. Perfect labeling. Since the puzzle content is known, every cropped cell automatically comes with the correct label (digit or blank), eliminating manual annotation.
2. Control over style. We can render Sudoku pages to look like those in printed books, with realistic fonts, grid lines, and difficulty levels controlled by how many cells are left blank.
3. Robustness through augmentation: By applying perspective warps, blur, noise, and lighting variations, we simulate how a smartphone camera might capture a Sudoku page, improving the model’s ability to handle real-world photos.
4. Scalability. With millions of Sudoku solutions available, we can easily generate tens of thousands of training samples in minutes, ensuring a dataset that is both large and diverse.

This synthetic data generation strategy allows us to create a custom-fit dataset for our Sudoku digit recognition problem, bridging the gap between clean digital puzzles and noisy real-world inputs.

## What we’ll produce
By the end of this step, you will have two complementary datasets:
1. Digit crops for training the classifier. A folder tree structured for torchvision.datasets.ImageFolder, containing tens of thousands of labeled 28×28 images of Sudoku digits (0–9, with 0 meaning blank):

```console
data/
  train/
    0/....png   (blank)
    1/....png
    ...
    9/....png
  val/
    0/....png
    ...
    9/....png
```

These will be used in next step to train a lightweight model for digit recognition.

2. Rendered Sudoku grids for camera simulation. Full-page Sudoku images (both clean book-style and augmented camera-like versions) stored in:
```console
data/
  grids/
    train/
      000001_clean.png
      000001_cam.png
      ...
    val/
      ...
```

These grid images allow us to later test the end-to-end pipeline: detect the board with OpenCV, rectify perspective, classify each cell using the ONNX digit recognizer, and then solve the Sudoku puzzle.

Together, these datasets provide both the micro-level data needed to train the digit recognizer and the macro-level data to simulate the camera pipeline for testing and deployment.

## Implementation
Start by creating a new file 02_PrepareData.py and modify it as follows:
```python
import os, random, pathlib
import numpy as np
import cv2 as cv
import pandas as pd
from tqdm import tqdm

random.seed(0)

# Parameters
PARQUET_PATH = "train_1.parquet"   # path to your downloaded HF Parquet
OUT_DIR      = pathlib.Path("data")
N_TRAIN      = 1000               # how many puzzles to render for training
N_VAL        = 100                # how many for validation
IMG_H, IMG_W = 1200, 800          # page size (portrait-ish)
GRID_MARGIN  = 60                 # outer margin, px
CELL_SIZE    = 28                 # output crop size for classifier (MNIST-like)
FONT         = cv.FONT_HERSHEY_SIMPLEX
# 

def str_to_grid(s: str):
    """81-char '012345678' string -> 9x9 list of ints."""
    s = s.strip()
    assert len(s) == 81, f"bad length: {len(s)}"
    return [[int(s[9*r+c]) for c in range(9)] for r in range(9)]

def load_puzzles(parquet_path, n_train, n_val):
    """Load puzzles/solutions; return two lists of 9x9 int grids for train/val."""
    df = pd.read_parquet(parquet_path, engine="pyarrow")
    # Shuffle reproducibly
    df = df.sample(frac=1.0, random_state=0).reset_index(drop=True)
    # Keep only needed columns if present
    need_cols = [c for c in ["puzzle", "solution"] if c in df.columns]
    if not need_cols or "puzzle" not in need_cols:
        raise ValueError(f"Expected 'puzzle' (and optionally 'solution') columns; got: {list(df.columns)}")

    # Slice train/val partitions
    df_train = df.iloc[:n_train]
    df_val   = df.iloc[n_train:n_train+n_val]

    puzzles_train = [str_to_grid(p) for p in df_train["puzzle"].astype(str)]
    puzzles_val   = [str_to_grid(p) for p in df_val["puzzle"].astype(str)]

    # Solutions are optional (useful later for solver validation)
    solutions_train = [str_to_grid(s) for s in df_train["solution"].astype(str)] if "solution" in df_train else None
    solutions_val   = [str_to_grid(s) for s in df_val["solution"].astype(str)]   if "solution" in df_val   else None

    return (puzzles_train, solutions_train), (puzzles_val, solutions_val)

def draw_grid(img, size=9, margin=GRID_MARGIN):
    H, W = img.shape[:2]
    step = (min(H, W) - 2*margin) // size
    x0 = (W - size*step) // 2
    y0 = (H - size*step) // 2
    for i in range(size+1):
        thickness = 3 if i % 3 == 0 else 1
        # vertical
        cv.line(img, (x0 + i*step, y0), (x0 + i*step, y0 + size*step), (0, 0, 0), thickness)
        # horizontal
        cv.line(img, (x0, y0 + i*step), (x0 + size*step, y0 + i*step), (0, 0, 0), thickness)
    return (x0, y0, step)

def put_digit(img, r, c, d, x0, y0, step):
    if d == 0:
        return  # blank cell
    text = str(d)
    scale = step / 60.0
    thickness = 2
    (tw, th), base = cv.getTextSize(text, FONT, scale, thickness)
    cx = x0 + c*step + (step - tw)//2
    cy = y0 + r*step + (step + th)//2 - th//4
    cv.putText(img, text, (cx, cy), FONT, scale, (0, 0, 0), thickness, cv.LINE_AA)

def render_page(puzzle9x9):
    page = np.full((IMG_H, IMG_W, 3), 255, np.uint8)
    x0, y0, step = draw_grid(page, 9, GRID_MARGIN)
    for r in range(9):
        for c in range(9):
            put_digit(page, r, c, puzzle9x9[r][c], x0, y0, step)
    return page, (x0, y0, step)

def aug_camera(img):
    """Light camera-like augmentation: perspective jitter + optional Gaussian blur."""
    H, W = img.shape[:2]
    def jitter(pt, s=20):
        return (pt[0] + random.randint(-s, s), pt[1] + random.randint(-s, s))
    src = np.float32([(0, 0), (W, 0), (W, H), (0, H)])
    dst = np.float32([jitter((0,0)), jitter((W,0)), jitter((W,H)), jitter((0,H))])
    M = cv.getPerspectiveTransform(src, dst)
    warped = cv.warpPerspective(img, M, (W, H), flags=cv.INTER_LINEAR, borderValue=(220, 220, 220))
    if random.random() < 0.5:
        k = random.choice([1, 2])
        warped = cv.GaussianBlur(warped, (2*k+1, 2*k+1), 0)
    return warped

def ensure_dirs(split):
    for cls in range(10):  # 0..9 (0 == blank)
        (OUT_DIR / split / str(cls)).mkdir(parents=True, exist_ok=True)

def save_crops(page, geom, puzzle9x9, split, base_id):
    x0, y0, step = geom
    idx = 0
    for r in range(9):
        for c in range(9):
            x1, y1 = x0 + c*step, y0 + r*step
            roi = page[y1:y1+step, x1:x1+step]
            g = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
            g = cv.resize(g, (CELL_SIZE, CELL_SIZE), interpolation=cv.INTER_AREA)
            label = puzzle9x9[r][c]  # 0 for blank, 1..9 digits
            out_path = OUT_DIR / split / str(label) / f"{base_id}_{idx:02d}.png"
            cv.imwrite(str(out_path), g)
            idx += 1

def process_split(puzzles, split_name, n_limit):
    ensure_dirs(split_name)
    grid_dir = OUT_DIR / "grids" / split_name
    grid_dir.mkdir(parents=True, exist_ok=True)

    N = min(n_limit, len(puzzles))
    for i in tqdm(range(N), desc=f"render {split_name}"):
        puzzle = puzzles[i]

        # Clean page
        page, geom = render_page(puzzle)
        save_crops(page, geom, puzzle, split_name, base_id=f"{i:06d}_clean")
        cv.imwrite(str(grid_dir / f"{i:06d}_clean.png"), page)

        # Camera-like
        warped = aug_camera(page)
        save_crops(warped, geom, puzzle, split_name, base_id=f"{i:06d}_cam")
        cv.imwrite(str(grid_dir / f"{i:06d}_cam.png"), warped)

def main():
    (p_train, _s_train), (p_val, _s_val) = load_puzzles(PARQUET_PATH, N_TRAIN, N_VAL)
    process_split(p_train, "train", N_TRAIN)
    process_split(p_val,   "val",   N_VAL)
    print("Done. Output under:", OUT_DIR.resolve())

if __name__ == "__main__":
    main()
```

At the top, you set basic knobs for the generator: where to read the Parquet file, where to write outputs, how many puzzles to render for train/val, page size, grid margin, crop size, and the OpenCV font. Tweaking these lets you control dataset scale, visual style, and classifier input size (e.g., CELL_SIZE=32 if you want a slightly larger digit crop).

The method str_to_grid(s) converts an 81-character Sudoku string into a 9×9 list of integers. Each character represents a cell: 0 is blank, 1–9 are digits. This is the canonical internal representation used throughout the script.

Then, we have load_puzzles(parquet_path, n_train, n_val), which loads the dataset from Parquet, shuffles it deterministically, and slices it into train/val partitions. It returns the puzzles (and, if present, solutions) as 9×9 integer grids. In this step we only need puzzle for rendering and labeling digit crops (blanks included); solution is useful later for solver validation.

Subsequently, draw_grid(img, size=9, margin=GRID_MARGIN) draws a Sudoku grid on a blank page image. It computes the step size from the page dimensions and margin, then draws both thin inner lines and thick 3×3 box boundaries. It returns the top-left corner (x0, y0) and the cell size (step), which are reused to place digits and to locate each cell for cropping.

Next, put_digit(img, r, c, d, x0, y0, step) renders a single digit d at row r, column c inside the grid. The text is centered in the cell using the font metrics; if d == 0, it leaves the cell blank. This mirrors printed-book Sudoku styling so our crops look realistic.

Another method, render_page(puzzle9x9) builds a complete “book-style” Sudoku page: creates a white canvas, draws the grid, loops over all 81 cells, and writes digits using put_digit. It returns the page plus the grid geometry (x0, y0, step) for subsequent cropping.

A method aug_camera(img) applies a light, camera-like augmentation to mimic smartphone captures: a small perspective warp (random corner jitter) and optional Gaussian blur. The warp uses a light gray border fill so any exposed areas look like paper rather than colored artifacts. This produces a second version of each page that’s closer to real-world inputs.

Afterward, ensure_dirs(split) makes the class directories for a given split (train or val) so that crops can be saved in data/{split}/{class}/.... The classes are 0..9 with 0 = blank.

A method save_crops(page, geom, puzzle9x9, split, base_id) slices the page into 81 cell crops using the grid geometry, converts each crop to grayscale, resizes it to CELL_SIZE × CELL_SIZE, and saves it into the appropriate class directory based on the puzzle’s value at that cell (0..9). Using the puzzle for labels ensures we learn to recognize blanks as well as digits.

Then, process_split(puzzles, split_name, n_limit) is the workhorse for each partition. For each puzzle, it (1) renders a clean page, saves its 81 crops, and writes the full page under data/grids/{split}; then (2) generates an augmented “camera-like” version and saves its crops and full page too. This gives you both micro-level training data (crops) and macro-level test images (full grids) for the later camera pipeline.

Finally, main() loads train/val puzzles from Parquet and calls process_split for each. When it finishes, you’ll have:
```console
data/
  train/
    0/… 1/… … 9/…
  val/
    0/… … 9/…
  grids/
    train/  (..._clean.png, ..._cam.png)
    val/    (..._clean.png, ..._cam.png)
```

## Launching instructions
1. Install dependencies (inside your virtual env):
```console
pip install pandas pyarrow opencv-python tqdm numpy
```

2. Download the Sudoku dataset from Hugging Face. This Learning Path uses the `train_1.parquet` file from the [Ritvik19/Sudoku-Dataset](https://huggingface.co/datasets/Ritvik19/Sudoku-Dataset) repository.

Download the dataset file:
```console
wget https://huggingface.co/datasets/Ritvik19/Sudoku-Dataset/resolve/main/train_1.parquet
```

Alternatively, you can download it manually from the [direct link](https://huggingface.co/datasets/Ritvik19/Sudoku-Dataset/blob/main/train_1.parquet) and save it as `train_1.parquet` in your working directory.

The Parquet file should be placed next to the script, or you can update `PARQUET_PATH` in the code to point to its location.

3. Run the generator:
```console
python3 02_PrepareData.py
```

4.	Inspect outputs:
* Digit crops live under data/train/{0..9}/ and data/val/{0..9}/.
* Full-page grids (clean + camera-like) live under data/grids/train/ and data/grids/val/.

Tips
* Start small (N_TRAIN=1000, N_VAL=100) to verify everything, then scale up.
* If you want larger inputs for the classifier, increase CELL_SIZE to 32 or 40.
* To make augmentation a bit stronger (more realistic), slightly increase the perspective jitter in aug_camera, add brightness/contrast jitter, or a faint gradient shadow overlay.

## Summary
After running this step you’ll have a robust, labeled, Sudoku-specific dataset: thousands of digit crops (including blanks) for training and realistic full-page grids for pipeline testing. You’re ready for the next step—training the digit recognizer and exporting it to ONNX.