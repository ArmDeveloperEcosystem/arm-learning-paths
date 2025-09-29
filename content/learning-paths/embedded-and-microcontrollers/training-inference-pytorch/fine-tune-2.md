---
title: Train and Test the Rock-Paper-Scissors Model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the model

Navigate to the Arm examples directory in the ExecuTorch repository:

```bash
cd $HOME/executorch/examples/arm
```

Create a file named `rps_tiny.py` and paste the following code:

```python
#!/usr/bin/env python3
"""
Tiny Rock–Paper–Scissors CNN (PyTorch) + ExecuTorch export + CLI mini-game.

Usage:
  # Train (fast) + export .pte + play
  python rps_tiny.py --epochs 8 --export --play

  # Just train (no export)
  python rps_tiny.py --epochs 8

  # Export previously trained weights to .pte
  python rps_tiny.py --export

  # Play the mini-game (uses the best weights on disk)
  python rps_tiny.py --play

Outputs:
  - rps_best.pt               (best PyTorch weights)
  - rps_labels.json           (label map)
  - rps_tiny.pte              (ExecuTorch program, if --export)
"""

import argparse, json, math, os, random, sys
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np
from PIL import Image,ImageOps,ImageDraw, ImageFont, ImageFilter

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader


# ---------------------------
# Config
# ---------------------------
SEED = 7
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)

LABELS = ["rock", "paper", "scissors"]  # indexes: 0,1,2
IMG_SIZE = 28
TRAIN_SAMPLES_PER_CLASS = 1000
VAL_SAMPLES_PER_CLASS = 200
BATCH = 64
LR = 2e-3
EPOCHS_DEFAULT = 6
WEIGHTS = "rps_best.pt"
LABELS_JSON = "rps_labels.json"
PTE_OUT = "rps_tiny.pte"


# ---------------------------
# Synthetic R/P/S renderer
# ---------------------------
def _rand(a, b):
    return a + random.random()*(b-a)

def render_rps(label: str) -> Image.Image:
    """
    Render a 28x28 grayscale image for 'rock'/'paper'/'scissors'
    using the letters R/P/S with random transforms + noise.
    """
    ch = {"rock":"R","paper":"P","scissors":"S"}[label]
    img = Image.new("L", (IMG_SIZE, IMG_SIZE), color=0)
    d = ImageDraw.Draw(img)

    # Try to get a default truetype; fallback to PIL default bitmap font
    font = None
    try:
        # Use a generic font size that fills the canvas
        font = ImageFont.truetype(font="Arial.ttf", size=int(_rand(18,24)))
    except Exception:
        font = ImageFont.load_default()

    # Random text position
    bbox = d.textbbox((0, 0), ch, font=font)  # (left, top, right, bottom)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (IMG_SIZE - w)//2 + int(_rand(-2, 2))
    y = (IMG_SIZE - h)//2 + int(_rand(-2, 2))

    # Random brightness for foreground
    fg = int(_rand(180, 255))
    d.text((x,y), ch, fill=fg, font=font)

    # Slight blur/rotate/shear
    if random.random()<0.6:
        img = img.filter(ImageFilter.GaussianBlur(radius=_rand(0.0, 0.7)))
    if random.random()<0.8:
        angle = _rand(-18, 18)
        img = img.rotate(angle, resample=Image.BILINEAR, expand=False, fillcolor=0)

    # Add mild elastic-ish jitter by affine
    if random.random()<0.5:
        dx, dy = _rand(-1.0, 1.0), _rand(-1.0, 1.0)
        ax = 1 + _rand(-0.05, 0.05)
        img = img.transform(
            img.size,
            Image.AFFINE,
            (ax, _rand(-0.05,0.05), dx, _rand(-0.05,0.05), 1+_rand(-0.05,0.05), dy),
            resample=Image.BILINEAR,
            fillcolor=0
        )

    # Salt & pepper noise
    if random.random()<0.8:
        arr = np.array(img, dtype=np.float32)
        noise = np.random.randn(*arr.shape)*_rand(3, 12)
        arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
        img = Image.fromarray(arr, mode="L")

    return img


# ---------------------------
# Dataset
# ---------------------------
@dataclass
class RPSItem:
    image: torch.Tensor  # [1,28,28] float32 0..1
    label: int

class RPSDataset(Dataset):
    def __init__(self, n_per_class: int, train: bool):
        self.items: List[RPSItem] = []
        for idx, name in enumerate(LABELS):
            for _ in range(n_per_class):
                img = render_rps(name)
                # Slightly different augments for train vs val
                if train and random.random()<0.15:
                    img = ImageOps.invert(img)
                t = torch.from_numpy(np.array(img, dtype=np.float32)/255.0)[None, ...]
                self.items.append(RPSItem(t, idx))
        random.shuffle(self.items)

    def __len__(self): return len(self.items)
    def __getitem__(self, i):
        it = self.items[i]
        return it.image, torch.tensor(it.label, dtype=torch.long)


# ---------------------------
# Model: Tiny CNN (Ethos-friendly)
# ---------------------------
class TinyRPS(nn.Module):
    """
    Simple ConvNet:
    [B,1,28,28] -> Conv3x3(16) -> ReLU -> Conv3x3(32) -> ReLU
      -> MaxPool2d(2) -> Conv3x3(64) -> ReLU -> MaxPool2d(2)
      -> flatten -> Linear(128) -> ReLU -> Linear(3)
    """
    def __init__(self):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
        )
        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64*7*7, 128), nn.ReLU(inplace=True),
            nn.Linear(128, 3)
        )
    def forward(self, x):  # x: [B,1,28,28]
        return self.head(self.body(x))

# AOT entry points expected by aot_arm_compiler
ModelUnderTest = TinyRPS()
ModelInputs = (torch.zeros(1, 1, IMG_SIZE, IMG_SIZE, dtype=torch.float32),)

# ---------------------------
# Train / Eval
# ---------------------------
def run_epoch(dl, model, crit, opt=None):
    train = opt is not None
    model.train() if train else model.eval()
    totl=totc=cnt=0
    with torch.set_grad_enabled(train):
        for x,y in dl:
            if train: opt.zero_grad(set_to_none=True)
            out = model(x)
            loss = crit(out, y)
            if train:
                loss.backward()
                opt.step()
            totl += float(loss)*x.size(0)
            totc += (out.argmax(1)==y).sum().item()
            cnt  += x.size(0)
    return totl/cnt, totc/cnt


# ---------------------------
# Export to ExecuTorch (.pte)
# ---------------------------
def export_to_pte(model: nn.Module, out_path=PTE_OUT):
    model.eval()
    example = torch.zeros(1,1,IMG_SIZE,IMG_SIZE, dtype=torch.float32)
    exported = None
    try:
        try:
            from torch.export import export
        except Exception:
            import torch._export as _export
            export = _export.export
        exported = export(model, (example,))
    except Exception:
        # Fallback: some older builds expose exir.capture
        from executorch.exir import capture
        exported = capture(model, (example,))
    from executorch import exir
    edge = exir.to_edge(exported)
    prog = edge.to_executorch()
    with open(out_path, "wb") as f:
        f.write(prog.buffer)
    print(f"[export] wrote {out_path}")


# ---------------------------
# CLI mini-game
# ---------------------------
def ascii_show(img: torch.Tensor) -> str:
    """Convert [1,28,28] tensor into tiny ASCII block for fun."""
    chars = " .:-=+*#%@"
    arr = (img.squeeze(0).numpy()*255).astype(np.uint8)
    h, w = arr.shape
    lines=[]
    for y in range(0,h,2):
        row=[]
        for x in range(0,w,1):
            v = arr[y, x]
            row.append(chars[min(len(chars)-1, int(v)*len(chars)//256)])
        lines.append("".join(row))
    return "\n".join(lines)

def beats(a: int, b: int) -> int:
    """Return +1 if a beats b, 0 if tie, -1 if loses."""
    # 0=rock beats 2=scissors, 1=paper beats 0, 2=scissors beats 1
    if a == b: return 0
    if (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1): return +1
    return -1

def play_game(model: nn.Module):
    print("\n=== Rock–Paper–Scissors: Play vs Tiny CNN ===")
    print("Type one of: rock / paper / scissors / quit\n")
    while True:
        s = input("Your move> ").strip().lower()
        if s in ("quit","q","exit"): break
        if s not in LABELS:
            print("Invalid. Try: rock / paper / scissors / quit")
            continue
        # Generate an image of YOUR move and one for OPPONENT
        your_idx = LABELS.index(s)
        your_img = render_rps(s)
        opp_idx  = random.randint(0,2)
        opp_img  = render_rps(LABELS[opp_idx])

        # Classify both with the model on CPU
        def to_tensor(im):
            return torch.from_numpy(np.array(im, dtype=np.float32)/255.0)[None,None,...]
        with torch.no_grad():
            y_logits = model(to_tensor(your_img))
            o_logits = model(to_tensor(opp_img))
            y_pred = int(y_logits.argmax(1).item())
            o_pred = int(o_logits.argmax(1).item())
            y_conf = torch.softmax(y_logits,1)[0,y_pred].item()
            o_conf = torch.softmax(o_logits,1)[0,o_pred].item()

        print("\nYou played:", s)
        print(ascii_show(to_tensor(your_img)[0]))
        print(f"Model thinks you played: {LABELS[y_pred]} ({y_conf*100:.1f}%)")

        print("\nOpponent played (hidden):")
        print(ascii_show(to_tensor(opp_img)[0]))
        print(f"Model thinks opponent played: {LABELS[o_pred]} ({o_conf*100:.1f}%)")

        outcome = beats(y_pred, o_pred)
        if outcome>0: print("\n🎉 You win!")
        elif outcome<0: print("\n😅 You lose!")
        else: print("\n🤝 It's a tie!")
        print("-"*50)


# ---------------------------
# Main
# ---------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epochs", type=int, default=EPOCHS_DEFAULT)
    ap.add_argument("--no-train", action="store_true", help="skip training (use saved weights)")
    ap.add_argument("--export", action="store_true", help="export ExecuTorch .pte after training")
    ap.add_argument("--play", action="store_true", help="play the mini-game after (or without) training")
    args = ap.parse_args()

    # Always save label map for runners
    with open(LABELS_JSON, "w") as f:
        json.dump({"labels": LABELS}, f, indent=2)

    model = TinyRPS()

    if not args.no_train:
        print("== Building synthetic datasets ==")
        tr = RPSDataset(TRAIN_SAMPLES_PER_CLASS, train=True)
        va = RPSDataset(VAL_SAMPLES_PER_CLASS,  train=False)
        train_loader = DataLoader(tr, batch_size=BATCH, shuffle=True, num_workers=0)
        val_loader   = DataLoader(va, batch_size=BATCH, shuffle=False, num_workers=0)

        print(f"Train size: {len(tr)}  |  Val size: {len(va)}")

        crit = nn.CrossEntropyLoss()
        opt = optim.Adam(model.parameters(), lr=LR, weight_decay=1e-4)

        best = -1.0
        for e in range(1, args.epochs+1):
            tl, ta = run_epoch(train_loader, model, crit, opt)
            vl, vaa = run_epoch(val_loader,  model, crit, None)
            print(f"Epoch {e:02d}/{args.epochs} | train {ta*100:5.2f}% | val {vaa*100:5.2f}%")
            if vaa > best:
                best = vaa
                torch.save(model.state_dict(), WEIGHTS)
                print(f"  ↑ saved {WEIGHTS} (val {vaa*100:.2f}%)")
        print("Training done.")
    else:
        print("--no-train: skipping training")

    # Load best weights if present
    if os.path.exists(WEIGHTS):
        model.load_state_dict(torch.load(WEIGHTS, map_location="cpu"))
        model.eval()
        print(f"Loaded weights from {WEIGHTS}")
    else:
        print(f"[warn] No weights file {WEIGHTS}; using random init.")

    if args.export:
        try:
            export_to_pte(model, PTE_OUT)
        except Exception as e:
            print("[export] failed:", e)

    if args.play:
        play_game(model)


if __name__ == "__main__":
    main()
```


### About the script
The script handles the entire workflow: data generation, model training, and a simple command-line game.

- Synthetic Data Generation: the script includes a function `render_rps()` that generates 28x28 grayscale images of the letters 'R', 'P', and 'S' with random rotations, blurs, and noise. This creates a diverse dataset that's used to train the model.
- Model Architecture: the model, a TinyRPS class, is a simple Convolutional Neural Network (CNN). It uses a series of 2D convolutional layers, followed by pooling layers to reduce spatial dimensions, and finally, fully connected linear layers to produce a final prediction. This architecture is efficient and well-suited for edge devices.
- Training: the script generates synthetic training and validation datasets. It then trains the CNN model using the **Adam optimizer** and **Cross-Entropy Loss**. It tracks validation accuracy and saves the best-performing model to `rps_best.pt`.
- ExecuTorch Export: a key part of the script is the `export_to_pte()` function. This function uses the `torch.export module` (or a fallback) to trace the trained PyTorch model and convert it into an ExecuTorch program (`.pte`). This compiled program is highly optimized for deployment on any target hardware, for example Cortex-M or Cortex-A CPUs for embedded devices.
- CLI Mini-Game: after training, you can play an interactive game. The script generates an image of your move and a random opponent's move. It then uses the trained model to classify both images and determines the winner based on the model's predictions.

## Running the Script:

Train the model, export it, and play the game:

```bash
python rps_tiny.py --epochs 8 --export --play
```

You’ll see training progress similar to:

```output
== Building synthetic datasets ==
Train size: 3000  |  Val size: 600
  totl += float(loss)*x.size(0)
Epoch 01/8 | train 80.03% | val 98.67%
  ↑ saved rps_best.pt (val 98.67%)
Epoch 02/8 | train 99.57% | val 100.00%
  ↑ saved rps_best.pt (val 100.00%)
Epoch 03/8 | train 99.83% | val 99.83%
Epoch 08/8 | train 100.00% | val 100.00%
Training done.
Loaded weights from rps_best.pt
[export] wrote rps_tiny.pte
```

After training and export, the game starts. Type rock, paper, or scissors, and review the model’s predictions for you and a random opponent:

```output
=== Rock–Paper–Scissors: Play vs Tiny CNN ===
Type one of: rock / paper / scissors / quit

Your move> rock

You played: rock





       .=##*++=-:.
       :**-:-=++**+:
      .=#+.     :+#=.
      :*%%#*++==+**-.
      -*+::-+#%*+-.
     :+*-.   -*+-
     -*+:     -**:
      ..      .=*+.
               .::.
Model thinks you played: rock (100.0%)

Opponent played (hidden):





        ..:--*###**-
        -#**--. .:+#*.  .
        .+#-       +#+
         -*+.     :+#-
         .+#+=**###+-.  .
          -##=:.   .
    .     .+*:
          .-**
  .        :==
Model thinks opponent played: paper (100.0%)

😅 You lose!
--------------------------------------------------
Your move> paper

You played: paper





        .--:.
       .=*+++***+=:
       :++.     :+*-
       -+-      .-+-
      .=*-..   .=+=.
      :**+++**+++-
      -*-
     .++:
     :+-
Model thinks you played: paper (100.0%)

Opponent played (hidden):


                   .


         .:::::-:::.
        .+*=======+*=
        .**.       +*-     .
 .      .=+.      :++:
        .=*#*###**+=:
        .=+-   :=+-.
        .=*:    .-+=:
    .    -#-.     :=*=
         :*:       .-+-
Model thinks opponent played: rock (100.0%)

🎉 You win!
--------------------------------------------------
Your move>
```

Type `quit` to exit the game. In the next chapter, you'll prepare the model to run on the FVP.