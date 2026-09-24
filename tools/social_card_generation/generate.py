from pathlib import Path
from io import BytesIO
import argparse
import base64
import html

import yaml
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

WIDTH = 1200
HEIGHT = 630

# Rectangle in which the title is allowed to appear.
TITLE_X = 70
TITLE_Y = 205
TITLE_WIDTH = 800
TITLE_HEIGHT = 250

MAX_FONT_SIZE = 60
MIN_FONT_SIZE = 36
FONT_WEIGHT = 500
LINE_HEIGHT = 1.08

TEXT_ALIGN = "left"
VERTICAL_ALIGN = "start"


# ------------------------------------------------------------
# Files
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parents[1]

SVG_PATH = BASE_DIR / "learn-social-og-template.svg"
TITLE_FONT_PATH = BASE_DIR / "fonts" / "Aeonik-Medium.otf"
META_FONT_PATH = BASE_DIR / "fonts" / "AeonikFono-Regular.otf"
OUTPUT_PATH = BASE_DIR / "social_image.webp"

LEARNING_PATH_ROOT = REPO_ROOT / "content" / "learning-paths"
INSTALL_GUIDE_ROOT = REPO_ROOT / "content" / "install-guides"
INSTALL_GUIDE_TITLE_TEMPLATE = "Quickly install the\n{title}\ntool"


def file_to_data_url(path: Path, mime_type: str) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def vertical_alignment_css(value: str) -> str:
    mapping = {
        "start": "flex-start",
        "center": "center",
        "end": "flex-end",
    }

    if value not in mapping:
        raise ValueError(
            f"VERTICAL_ALIGN must be one of {list(mapping)}, got {value!r}"
        )

    return mapping[value]


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Generate a social card from Learning Path or install guide metadata."
        )
    )
    parser.add_argument(
        "content_path",
        help=(
            "Path to a Learning Path directory/_index.md or an install guide .md file."
        ),
    )
    return parser.parse_args()


def resolve_content_path(value: str) -> Path:
    raw_path = Path(value).expanduser()

    if raw_path.is_absolute():
        path = raw_path
    else:
        cwd_path = Path.cwd() / raw_path
        repo_path = REPO_ROOT / raw_path
        path = cwd_path if cwd_path.exists() else repo_path

    if path.is_dir():
        path = path / "_index.md"

    if not path.exists():
        raise FileNotFoundError(f"Content file not found: {path}")

    if path.suffix != ".md":
        raise ValueError(f"Content path must be a Markdown file: {path}")

    return path.resolve()


def content_type_for_path(path: Path) -> str:
    resolved_path = path.resolve()

    try:
        resolved_path.relative_to(LEARNING_PATH_ROOT.resolve())
        return "LEARNING PATH"
    except ValueError:
        pass

    try:
        resolved_path.relative_to(INSTALL_GUIDE_ROOT.resolve())
        return "INSTALL GUIDE"
    except ValueError:
        pass

    raise ValueError(
        "Content path must be under content/learning-paths or content/install-guides: "
        f"{path}"
    )


def read_front_matter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Missing YAML front matter delimiter at start of {path}")

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            front_matter = "\n".join(lines[1:index])
            data = yaml.safe_load(front_matter) or {}

            if not isinstance(data, dict):
                raise ValueError(f"YAML front matter must be a mapping in {path}")

            return data

    raise ValueError(f"Missing closing YAML front matter delimiter in {path}")


def title_for_path(path: Path) -> str:
    front_matter = read_front_matter(path)
    title = front_matter.get("title")

    if title is None or not str(title).strip():
        raise ValueError(f"Missing required title in front matter: {path}")

    return str(title).strip()


def render_title(raw_title: str, content_type: str) -> str:
    if content_type != "INSTALL GUIDE":
        return raw_title

    return INSTALL_GUIDE_TITLE_TEMPLATE.replace("{title}", raw_title)


def font_face_css(path: Path, family: str, weight: int, fallback: str) -> str:
    if not path.exists():
        print(
            f"Warning: {path.name} not found. "
            f"Using system {fallback} fallback."
        )
        return ""

    font_url = file_to_data_url(path, "font/otf")

    return f"""
    @font-face {{
        font-family: "{family}";
        src: url("{font_url}") format("opentype");
        font-style: normal;
        font-weight: {weight};
        font-display: block;
    }}
"""


def main():
    args = parse_args()
    content_path = resolve_content_path(args.content_path)
    raw_title = title_for_path(content_path)
    content_type = content_type_for_path(content_path)
    title = render_title(raw_title, content_type)

    for path in (
        SVG_PATH,
    ):
        if not path.exists():
            raise FileNotFoundError(f"Missing required file: {path}")


    title_font_css = font_face_css(TITLE_FONT_PATH, "Aeonik", 500, "sans-serif")
    meta_font_css = font_face_css(META_FONT_PATH, "Aeonik Fono", 400, "monospace")
    svg_url = file_to_data_url(SVG_PATH, "image/svg+xml")

    safe_title = html.escape(title)
    safe_content_type = html.escape(content_type)

    document = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">

<style>
    {title_font_css}
    {meta_font_css}

    * {{
        box-sizing: border-box;
    }}

    html,
    body {{
        width: {WIDTH}px;
        height: {HEIGHT}px;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}

    body {{
        background: #0d022c;
    }}

    #card {{
        position: relative;
        width: {WIDTH}px;
        height: {HEIGHT}px;
        overflow: hidden;
    }}

    #background {{
        position: absolute;
        inset: 0;
        width: {WIDTH}px;
        height: {HEIGHT}px;
        display: block;
    }}

    #title-box {{
        position: absolute;

        left: {TITLE_X}px;
        top: {TITLE_Y}px;
        width: {TITLE_WIDTH}px;
        height: {TITLE_HEIGHT}px;

        display: flex;
        flex-direction: column;
        justify-content: {vertical_alignment_css(VERTICAL_ALIGN)};

        overflow: hidden;
    }}

    #title {{
        font-family: "Aeonik", Arial, Helvetica, sans-serif;
        font-weight: {FONT_WEIGHT};
        font-synthesis: none; /* Prevent browser from faking bold/italic */
        color: #ffffff;
        font-size: {MAX_FONT_SIZE}px;
        line-height: {LINE_HEIGHT};

        text-align: {TEXT_ALIGN};
        white-space: pre-line;
        text-wrap: pretty; /* options: balance, pretty, none */
        hyphens: none;
        overflow-wrap: break-word;

        margin: 0;
        padding: 0;
    }}



    #content-type {{
        position: absolute;
        left: 70px;
        top: 155px;

        font-family: "Aeonik Fono", Consolas, "Liberation Mono", Menlo, monospace;
        font-weight: 400;
        font-size: 20px;
        line-height: 1;
        letter-spacing: 0.02em;
        color: #C7ADFC;
    }}



</style>
</head>

<body>



    <div id="card">
        <img id="background" src="{svg_url}" alt="">

        <div id="content-type">{safe_content_type}</div>
        <div id="title-box">
            <div id="title">{safe_title}</div>
        </div>

    </div>

<script>
async function fitTitle() {{
    await document.fonts.ready;

    const title = document.getElementById("title");
    const box = document.getElementById("title-box");

    let size = {MAX_FONT_SIZE};

    function fits() {{
        /*
         * scrollHeight catches vertical overflow.
         * scrollWidth catches pathological horizontal overflow.
         */
        return (
            title.scrollHeight <= box.clientHeight &&
            title.scrollWidth <= box.clientWidth
        );
    }}

    while (size > {MIN_FONT_SIZE} && !fits()) {{
        size -= 1;
        title.style.fontSize = size + "px";

        /*
         * Force layout before testing again.
         */
        void title.offsetHeight;
    }}

    window.__TITLE_RESULT__ = {{
        fontSize: size,
        fits: fits(),
        scrollHeight: title.scrollHeight,
        boxHeight: box.clientHeight,
        scrollWidth: title.scrollWidth,
        boxWidth: box.clientWidth
    }};

    window.__READY__ = true;
}}

fitTitle();
</script>
</body>
</html>
"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={
                "width": WIDTH,
                "height": HEIGHT,
            },
            device_scale_factor=4,
        )

        page.set_content(document)

        page.wait_for_function("window.__READY__ === true")

        result = page.evaluate("window.__TITLE_RESULT__")

        if not result["fits"]:
            browser.close()
            raise RuntimeError(
                "Title could not fit inside the configured title box "
                f"even at {result['fontSize']}px. "
                "Increase TITLE_WIDTH/TITLE_HEIGHT, lower MIN_FONT_SIZE, "
                "or shorten the title."
            )

        print(
            f"Title fitted at {result['fontSize']}px "
            f"inside {TITLE_WIDTH}x{TITLE_HEIGHT}px box."
        )

        # Playwright returns PNG bytes directly.
        # No temporary PNG file is required.
        png_bytes = page.locator("#card").screenshot(type="png")

        browser.close()

    with Image.open(BytesIO(png_bytes)) as image:
        image = image.convert("RGB")

        image = image.resize(
            (WIDTH, HEIGHT),
            Image.Resampling.LANCZOS,
        )

        # Very subtle dithering to break up gradient banding.
        noise = Image.effect_noise(
            image.size,
            sigma=1.5, # 0.6  → extremely subtle. 1.0  → my starting point 1.5  → stronger anti-banding 2.0  → probably more grain than you need
        ).convert("RGB")

        dithered = ImageChops.add(
            image,
            noise,
            scale=1.0,
            offset=-128,
        )

        # Only dither darker pixels.
        # White logo/title remain untouched.
        luminance = image.convert("L")

        mask = luminance.point(
            lambda p: 255 if p < 190 else 0
        )

        image = Image.composite(
            dithered,
            image,
            mask,
        )


        image.save(
            OUTPUT_PATH,
            format="WEBP",
            quality=96,
            method=6,
        )

    print(f"Wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
