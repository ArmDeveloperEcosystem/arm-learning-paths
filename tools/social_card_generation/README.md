# Social Card Prototype

Prototype generator for learn.arm.com social/Open Graph cards with updated branding and name of the content directly in the image. It reads a Learning Path or install guide Markdown file, pulls the `title` from front matter, applies the content type label, and writes a WebP image under `static/social-images/` matching the content path. A directory's `_index.md` produces an image named after that directory; a standalone Markdown file produces an image named after the file.

The shared deployment workflow downloads existing cards and a title manifest from the target S3 bucket, then runs `--all` before building Hugo for both dev and production. The manifest maps each WebP path to the title rendered on its card. `--all` generates cards only when the image is missing or its title has changed. Hugo copies the cards from `static/social-images/` to the matching `social-images/` paths in the built site, and `hugo deploy` uploads new or changed files. After a successful deploy, the workflow uploads the updated manifest to S3. The default card at `static/social-images/default.webp` is committed as a guaranteed fallback; generated Learning Path and install guide cards remain ignored by Git.


You'll need these python files installed:
```bash
python3 -m pip install playwright Pillow PyYAML
python3 -m playwright install --only-shell chromium
```

Test from the repo root:

```bash
python3 tools/social_card_generation/generate.py content/install-guides/ambaviz.md
python3 tools/social_card_generation/generate.py content/learning-paths/embedded-and-microcontrollers/advanced_soc
python3 tools/social_card_generation/generate.py --default
python3 tools/social_card_generation/generate.py --all
```

The first two examples write `static/social-images/install-guides/ambaviz.webp` and `static/social-images/learning-paths/embedded-and-microcontrollers/advanced_soc.webp`, respectively. `--default` writes `static/social-images/default.webp` with the site title. `--all` checks the local ignored `.social-card-manifest.json` by default, or a file passed with `--manifest`. If no manifest exists, it renders all cards once to establish a baseline. Later runs skip cards with an existing image and unchanged title, including the default card. It skips category pages and example Learning Path directories, continues after individual failures, and reports them at the end. Single-card runs overwrite an existing image; the next `--all` run reconciles the manifest.

Exact brand rendering still needs a font solution for `fonts/Aeonik-Medium.otf` and `fonts/AeonikFono-Regular.otf`, which I have from our branding team but we are unable to host in the OSS repo on GitHub due to licensing. The current system font fallbacks are near-identical and OK for social sharing.
