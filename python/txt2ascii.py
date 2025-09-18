#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
txt2ascii_plus.py

Written by Ye, LU Lab., Myanmar.
Last updated: 18 Sept 2025

- Converts Myanmar (or any Unicode) text into ASCII art.
- Usage:
    python txt2ascii.py --text "ဘိန်းမုန့်" --font ./noto_fonts/NotoSansMyanmar-Regular.ttf --width 200 --style 28
    python txt2ascii.py --text hello --style 85
    python txt2ascii.py --list-styles
    python txt2ascii.py --preview --text "Test" --font ./noto_fonts/NotoSansMono-Regular.ttf
    python txt2ascii.py --file my.txt --font ./noto_fonts/NotoSansMyanmar-Regular.ttf --width 100 --preview --start 1 --end 70 --delay 500
    
    python txt2ascii.py --text "Love you!" --preview --start 70 --end 100
    python txt2ascii.py --text "ສະບາຍດີ" --font ./noto_fonts/NotoSansLao-Regular.ttf --preview --start 1 --end 70 --width 120
    python txt2ascii.py --text "สบายๆ" --font ./noto_fonts/NotoSansThai-Regular.ttf --preview --start 1 --end 70
    python txt2ascii.py --text "ឣរគុណ" --font ./noto_fonts/NotoSansKhmer-Regular.ttf --preview --start 1 --end 70
    python txt2ascii.py --text "नमस्ते" --font ./noto_fonts/NotoSansDevanagari-Regular.ttf --preview --start 1 --end 70
"""

import argparse
import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Try to import pyfiglet (optional, used for FIGlet/banner styles)
try:
    import pyfiglet
    _PYFIGLET_AVAILABLE = True
except Exception:
    pyfiglet = None
    _PYFIGLET_AVAILABLE = False

# -------------------------
# CORE STYLES (1-50) - keep as your previous list (strings)
# (I include them as-is, they are character ramps / palettes)
# -------------------------
ASCII_STYLES = {
    # 1-64: pixel ramps / custom patterns
    1: " .:-=+*#%@█",               # gradient from light dot to solid block
    2: " `'.,-~:;=!*%$@",             # subtle punctuation ramp, small→dense
    3: " ░▒▓█",                    # block shading from light→dark
    4: " .oO@",                    # small→medium→large circles
    5: " `'.,^\"~:;Il!i><+?][}{1)(|\\tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",  # dense ASCII gradient with letters and symbols
    6: " ░░▒▒▓▓██",                     # repeated blocks for smoother gradient
    7: " -~+*%@#",                  # symbols with increasing visual weight
    8: " .:=*#",                   # minimalistic gradient
    9: " `'-^\":;I!|%$@",            # punctuation + vertical strokes, light→dark
    10: " .:-=+*#%$@",               # smooth light→dark gradient
    11: " .•*+#█@",                   # simple dense dots/blocks
    12: " ⠁⠂⠄⠆⠇⠋⠛⠟⠿", # braille-style density ramp
    13: " `'.,-=*#%@█",                # light punctuation to full block
    14: " ▓▒░ ",                    # inverted block shading
    15: "@%#*+=-:. ",                # descending density of symbols
    16: " ▄▀",                      # half-block vertical gradient
    17: " `'.^,:;Il!i><+?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",  # complex dense ASCII gradient
    18: " ⡀⡄⡆⡇⡏⡟⡿⣿",       # braille-like progressive shading
    19: " .oO0@",                    # small→large circles/numbers
    20: " _▂▃▄▅▆▇█",                  # vertical bar gradient from short→tall
    21: " .:░▒▓█",                     # light→medium→full block
    22: " .°•*oO@",                    # gradient with small/large dots
    23: " `'.-~:;^=+*#%@█",              # mixed punctuation to block
    24: " ▂▃▄▅▆▇█",                      # smooth vertical bar ramp
    25: " .-~=*#%@@",                 # simple high-contrast symbols
    26: " ░▒▓█▓▒░",                  # smooth block gradient, symmetric, dense contrast
    27: " .':;|iIlL#█",                 # light→bold ASCII characters
    28: " ▀▄",                      # half-block vertical shading
    29: " .':=-+*#%@█",                # small→large ASCII symbols gradient
    30: " ░▒▓█▌▐",                    # shaded blocks with half-blocks
    31: " ▖▗▘▙▚▛▜▝▞",                  # quadrant blocks for fine shading
    32: " ▒░▌▐█",                    # high contrast, small→large blocks
    33: " ░▒▓█▌▐▏",                # gradual block shading with small/medium/full blocks
    34: " ╱╲▰▱",                    # diagonal and filled blocks
    35: " +-*/=#%",                     # math symbols, simple high-contrast
    36: " ▀▄ ▂▃▅▆▇█",                  # vertical bars from low→high for stroke clarity
    37: " ▫▪□■▣▤",                    # boxes and squares, alternating outline/filled
    38: " ▞▚▒▓",                    # diagonal/shaded blocks
    39: " +*x#%@&$",                   # symbols with distinct strokes, easy to read
    40: " ▴▵▾▿",                     # triangles, vertical clarity
    41: " ▲△▴▵▼▽▾▿",                # triangles pointing in different directions for visual separation
    42: " ─│┌┐└┘├┤┬┴",                 # line and box-drawing characters for clear spacing
    43: " ❂❃❉❊",                   # decorative floral symbols
    44: "⡀⡄⡆⡇⡏⡟⡿⣿",          # braille-style shading
    45: " ▌▐▍▏▎▍▐",                    # half/quarter blocks, vertical emphasis
    46: " ▏▎▍▌▋▊▉█",                # vertical bar gradient, small→large
    47: " ◰◱◲◳",                    # pie/quadrant blocks
    48: " ─│┌┐└┘",                   # lines/boxes, readable blocks
    49: " ⦁⦾⦿",                     # circles and targets
    50: " ❘❙❚",                     # vertical bar progression

    # 51-70: New creative ASCII ramps/patterns (no emojis)
    51: " .:oO0@",                 # dots/circles small→large
    52: " ░▒▓█",                 # block shading
    53: " .-=+*#%@",                 # simple ASCII symbols
    54: " ⠁⠂⠄⠆⠇⠋⠛⠟⠿",         # braille-style density ramp
    55: " ░·•◦○●",                 # dot symbols, small→large
    56: "  ▂▃▄▅▆▇█",                  # vertical bar gradient
    57: " ⋆☆★✦✧✩✪",                  # star symbols, small→large/filled
    58: " ▖▗▘▝▞▟▜▛",                 # quadrant blocks, fine shading
    59: " ░▒▓█▌▐",                 # denser gradient blocks
    60: " ▂▃▄▅▆▇█▉▊▋",                 # extended vertical bar gradient for smooth shading
    61: " ▪▫▪▫█",                   # alternating filled/empty squares
    62: " «‹‹‹«»››»",                  # chevrons, left→right
    63: " ▬▬▭▮▯",                    # horizontal bar progression
    64: " ☰☱☲☳☴☵☶☷",                 # I Ching-style trigram symbols
    65: " ▓░▒█",                   # checkerboard style, higher contrast
    66: "~^-",                     # wave-like small symbols
    67: " │┃¦┆",                 # vertical lines, readable
    68: "/\\><",                   # diagonal/angle symbols
    69: "◇◆◈◉",                   # geometric diamonds, outline→filled
    70: "┌─┐│└┘",                   # box/line pattern, basic framing

    # 71-100: Figlet fonts (English only)
    71: {"figlet": "standard"},
    72: {"figlet": "slant"},
    73: {"figlet": "big"},
    74: {"figlet": "block"},
    75: {"figlet": "bubble"},
    76: {"figlet": "digital"},
    77: {"figlet": "banner3-D"},
    78: {"figlet": "banner"},
    79: {"figlet": "larry3d"},
    80: {"figlet": "isometric1"},
    81: {"figlet": "starwars"},
    82: {"figlet": "shadow"},
    83: {"figlet": "script"},
    84: {"figlet": "small"},
    85: {"figlet": "doom"},
    86: {"figlet": "dotmatrix"},
    87: {"figlet": "colossal"},
    88: {"figlet": "cosmic"},
    89: {"figlet": "graffiti"},
    90: {"figlet": "chunky"},
    91: {"figlet": "caligraphy"},
    92: {"figlet": "tombstone"},
    93: {"figlet": "pepper"},
    94: {"figlet": "nancyj"},
    95: {"figlet": "3-d"},
    96: {"figlet": "alphabet"},
    97: {"figlet": "eftichess"},
    98: {"figlet": "univers"},
    99: {"figlet": "contessa"},
    100: {"figlet": "poison"},
}

# Optional human-friendly style descriptions (for --list-styles)
STYLE_DESCRIPTIONS = {
    **{i: f"Palette-style (ramp) #{i}" for i in range(1, 71)}, # Adjusted range
    **{i: f"FIGlet font '{ASCII_STYLES[i]['figlet']}'" if isinstance(ASCII_STYLES[i], dict) else f"FIGlet #{i}" for i in range(71, 101)}
}

# -------------------------
# Functions
# -------------------------
def list_styles():
    print("Available styles (1..100):")
    for i in sorted(ASCII_STYLES.keys()):
        desc = STYLE_DESCRIPTIONS.get(i, "")
        print(f"{i:3d}: {desc}")
    print("\nNote: styles 71-100 are FIGlet (banner) fonts — pyfiglet required.")


def render_figlet_text(text, fontname):
    if not _PYFIGLET_AVAILABLE:
        return f"[FIGLET MISSING] pyfiglet not installed. Install with: pip install pyfiglet\n{text}\n"
    # verify font availability
    available = pyfiglet.FigletFont.getFonts()
    chosen = fontname
    if fontname not in available:
        # try some common alternates (loose matching)
        alt = None
        fn_lower = fontname.lower()
        for candidate in available:
            if fn_lower in candidate.lower() or candidate.lower() in fn_lower:
                alt = candidate
                break
        if alt:
            chosen = alt
        else:
            chosen = "standard"
    f = pyfiglet.Figlet(font=chosen)
    try:
        return f.renderText(text)
    except Exception as e:
        # fallback to standard figlet format
        f = pyfiglet.Figlet(font="standard")
        return f.renderText(text)


def image_text_to_ascii(text, font_path, width, chars, invert=False, aspect_ratio=0.45):
    """
    Render `text` with PIL using `font_path` (unicode-capable), rasterize and map
    each pixel to a character from `chars` (ordered from light->dark).
    """
    # Render text into an image using supplied font
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)
    # get bounding box for the text
    bbox = font.getbbox(text)
    w, h = bbox[2], bbox[3]
    if w <= 0 or h <= 0:
        return ""
    img = Image.new("L", (w, h), 255)  # white background
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, fill=0, font=font)

    # Resize to target width while preserving aspect
    new_width = max(1, int(width))
    new_height = max(1, int(new_width * (h / max(w, 1)) * aspect_ratio))
    img = img.resize((new_width, new_height))

    pixels = np.array(img)  # grayscale 0..255
    # normalize 0..1
    normalized = (pixels - pixels.min()) / (pixels.ptp() + 1e-9)
    if invert:
        normalized = 1.0 - normalized

    # map each pixel to a char index (0..len(chars)-1)
    palette = list(chars)
    idx = (normalized * (len(palette) - 1)).astype(np.int32)
    # build lines
    lines = []
    for row in idx:
        lines.append("".join(palette[v] for v in row))
    return "\n".join(lines)


def render_text(text, style, font_path=None, width=80, invert=False):
    """Render text using selected style. style can be int (1..100)."""
    if style not in ASCII_STYLES:
        raise ValueError(f"Style {style} not found (valid 1..100).")

    spec = ASCII_STYLES[style]

    # FIGlet style (dict)
    if isinstance(spec, dict) and "figlet" in spec:
        return render_figlet_text(text, spec["figlet"])

    # character-ramp style (string)
    if isinstance(spec, str):
        if not font_path:
            raise ValueError("font_path required for palette (image-to-ascii) styles.")
        return image_text_to_ascii(text, font_path, width, spec, invert=invert)

    raise ValueError("Unsupported style spec type.")


# -------------------------
# CLI
# -------------------------
def main():
    ap = argparse.ArgumentParser(description="img2ascii_plus — more creative ASCII art styles (1..100).")
    
    # Use a mutually exclusive group for --text and --file
    input_group = ap.add_mutually_exclusive_group()
    input_group.add_argument("--text", type=str, help="Text to convert (Unicode OK).")
    input_group.add_argument("--file", type=str, help="Optional input file (line-by-line).")

    ap.add_argument("--font", type=str, default=None, help="Path to TrueType font (e.g., NotoSansMyanmar-Regular.ttf). Required for palette styles.")
    ap.add_argument("--width", type=int, default=80, help="Target width in chars for palette styles (default 80).")
    ap.add_argument("--style", type=int, default=1, help="Style number (1..100).")
    ap.add_argument("--invert", action="store_true", help="Invert mapping (dark/light swap).")
    ap.add_argument("--list-styles", action="store_true", help="List available styles and exit.")
    ap.add_argument("--preview", action="store_true", help="Preview all styles (or range) for given text. Use --start and --end to limit.")
    ap.add_argument("--start", type=int, default=1, help="Preview start style index (default 1).")
    ap.add_argument("--end", type=int, default=100, help="Preview end style index (default 100).")
    ap.add_argument("--delay", type=int, default=100, help="Delay in milliseconds between preview styles (default 100).")
    args = ap.parse_args()

    if args.list_styles:
        list_styles()
        return

    # preview mode
    if args.preview:
        if not args.text and not args.file:
            print("Preview mode requires either --text or --file to show examples.")
            return

        lines_to_render = []
        if args.text:
            lines_to_render.append(args.text)
        elif args.file:
            if not os.path.exists(args.file):
                print(f"[ERROR] Input file not found: {args.file}")
                return
            with open(args.file, "r", encoding="utf-8") as f:
                lines_to_render = [line.rstrip("\n") for line in f if line.strip()]
            if not lines_to_render:
                print(f"File '{args.file}' is empty or contains no readable text.")
                return

        start = max(1, args.start)
        end = min(100, args.end)
        delay_sec = args.delay / 1000.0 # Convert milliseconds to seconds
        
        for s in range(start, end + 1):
            print("=" * 80)
            print(f"STYLE {s}: {STYLE_DESCRIPTIONS.get(s, '')}")
            for line in lines_to_render:
                try:
                    out = render_text(line, s, font_path=args.font, width=args.width, invert=args.invert)
                    print(out)
                except Exception as e:
                    print(f"[ERROR rendering style {s} on line '{line}'] {e}")
            time.sleep(delay_sec)
        return

    # single style render
    if args.text:
        try:
            out = render_text(args.text, args.style, font_path=args.font, width=args.width, invert=args.invert)
            print(out)
        except Exception as e:
            print("[ERROR]", e)
    elif args.file:
        if not os.path.exists(args.file):
            print("[ERROR] Input file not found:", args.file)
            return
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                try:
                    out = render_text(line, args.style, font_path=args.font, width=args.width, invert=args.invert)
                except Exception as e:
                    out = f"[ERROR rendering style {args.style}] {e}"
                print(out)
                # small pause
                time.sleep(0.5)
    else:
        # This case is now less likely due to the mutually exclusive group
        print("Please provide --text or --file. Use --list-styles to see available styles.")


if __name__ == "__main__":
    main()