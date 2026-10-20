# Social Card Prototype

Prototype generator for learn.arm.com social/Open Graph cards with updated branding and name of the content directly in the image. It reads a Learning Path or install guide Markdown file, pulls the `title` from front matter, applies the content type label, and writes a WebP image under `static/social-images/` matching the content path. A directory's `_index.md` produces an image named after that directory; a standalone Markdown file produces an image named after the file.

The shared deployment workflow runs `--all` before building Hugo for both dev and production. Hugo copies the generated files from `static/social-images/` to the matching `social-images/` paths in the built site, and `hugo deploy` uploads them with the site. Generated images remain ignored by Git.


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

The first two examples write `static/social-images/install-guides/ambaviz.webp` and `static/social-images/learning-paths/embedded-and-microcontrollers/advanced_soc.webp`, respectively. `--default` writes `static/social-images/default.webp` with the site title. `--all` generates that default card plus every Learning Path entry and install guide entry, skipping category pages and example Learning Path directories. It continues after individual failures and reports them at the end.

Exact brand rendering still needs a font solution for `fonts/Aeonik-Medium.otf` and `fonts/AeonikFono-Regular.otf`, which I have from our branding team but we are unable to host in the OSS repo on GitHub due to licensing. The current system font fallbacks are near-identical and OK for social sharing.
