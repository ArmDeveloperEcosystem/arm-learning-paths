# Social Card Prototype

Prototype generator for learn.arm.com social/Open Graph cards with updated branding and name of the content directly in the image. It reads a Learning Path or install guide Markdown file, pulls the `title` from front matter, applies the content type label, and writes `social_image.webp`. 

To implement this we need to put this script in our CI pipeline for each content (and when its title is updated). Each content needs to generate a unique webp image for each learning path for social sharing, as opposed to the current one social image approach. The Hugo template needs to be updated for each content to source its webp.


You'll need these python files installed:
```bash
pip install playwright Pillow
python -m playwright install --only-shell chromium
```

Test from the repo root:

```bash
python tools/social_card_prototype/generate.py content/install-guides/ambaviz.md
python tools/social_card_prototype/generate.py content/learning-paths/embedded-and-microcontrollers/advanced_soc
```

Open `tools/social_card_prototype/social_image.webp` to inspect the result.

Exact brand rendering still needs a font solution for `fonts/Aeonik-Medium.otf` and `fonts/AeonikFono-Regular.otf`, which I have from our branding team but we are unable to host in the OSS repo on GitHub due to licensing. The current system font fallbacks are near-identical and OK for social sharing.
