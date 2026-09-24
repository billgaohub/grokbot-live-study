#!/usr/bin/env python3
"""
Generate a 1200x630 pixel-perfect social preview card for Grok Bot Live Study.
Formatted for X (Twitter) Summary Card with Large Image and GitHub Social Preview.
"""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630

# Colors
BG_TOP = (15, 23, 42)      # Slate 900
BG_BOTTOM = (6, 9, 15)     # Deep space
CARD_BG = (15, 23, 42)
CARD_BORDER = (51, 65, 85, 255)
CYAN = (56, 189, 248)
PURPLE = (192, 132, 252)
EMERALD = (52, 211, 153)
WHITE = (248, 250, 252)
SLATE_300 = (203, 213, 225)
SLATE_400 = (148, 163, 184)
SLATE_500 = (100, 116, 139)

# Fonts
font_title = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 50, index=1)
font_subtitle = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 21, index=10)
font_card_title = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 19, index=1)
font_card_metric = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 16, index=1)
font_card_body = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 14, index=0)
font_badge = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 13, index=1)
font_flow_title = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 12, index=1)
font_flow_box = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 15, index=1)
font_flow_desc = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 13, index=0)
font_footer = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 14, index=0)

# Create base canvas with gradient
img = Image.new('RGB', (WIDTH, HEIGHT), BG_BOTTOM)
draw = ImageDraw.Draw(img)

# Vertical gradient
for y in range(HEIGHT):
    factor = y / HEIGHT
    r = int(BG_TOP[0] * (1 - factor) + BG_BOTTOM[0] * factor)
    g = int(BG_TOP[1] * (1 - factor) + BG_BOTTOM[1] * factor)
    b = int(BG_TOP[2] * (1 - factor) + BG_BOTTOM[2] * factor)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# Ambient glow on top-left and top-right
glow_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_overlay)
for r in range(320, 0, -8):
    alpha = int(28 * (1 - r / 320))
    glow_draw.ellipse([80 - r, 50 - r, 80 + r, 50 + r], fill=(2, 132, 199, alpha))
    glow_draw.ellipse([WIDTH - 100 - r, 80 - r, WIDTH - 100 + r, 80 + r], fill=(147, 51, 234, alpha))

# Subtle decorative grid dots
for x in range(40, WIDTH - 40, 32):
    for y in range(40, HEIGHT - 40, 32):
        glow_draw.point((x, y), fill=(100, 116, 139, 35))

img.paste(glow_overlay, (0, 0), glow_overlay)
draw = ImageDraw.Draw(img)

# 1. Header Badges
badge_x, badge_y = 50, 36
badge_w, badge_h = 360, 30
draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=15, fill=(15, 23, 42), outline=(2, 132, 199), width=1)
# Green pulse dot
draw.ellipse([badge_x + 12, badge_y + 9, badge_x + 24, badge_y + 21], fill=EMERALD)
draw.text((badge_x + 32, badge_y + 7), "EMPIRICAL FIELD STUDY · xAI GALAXY", font=font_badge, fill=CYAN)

# Right Header Tag
right_tag = "90,415s RAW STREAM RECONSTRUCTION"
draw.text((WIDTH - 50 - 320, badge_y + 7), right_tag, font=font_badge, fill=SLATE_400)

# 2. Main Title & Subtitle
draw.text((50, 84), "Grok Bot Live Study", font=font_title, fill=WHITE)
draw.text((50, 145), "Multi-Agent Coordination & Bottleneck Migration in 25-Hour Live Production", font=font_subtitle, fill=SLATE_300)

# 3. Three-Day Architecture Cards
card_w = 346
card_h = 175
card_y = 195
spacing = 30
x_start = 50

cards = [
    {
        "day": "Day 1 · Bootstrap & Permissions",
        "metric": "08:45:13 · 33 OBS (16 Verified)",
        "color": CYAN,
        "bullets": [
            "• Firecracker microVM shared filesystem",
            "• Human approval gate latency: 195s",
            "• Google Form permission failure & recovery",
            "• Spoken assertion vs doc contradiction"
        ]
    },
    {
        "day": "Day 2 · Multi-Bot Swarm",
        "metric": "08:23:19 · 29 OBS (18 Verified)",
        "color": PURPLE,
        "bullets": [
            "• Specialized subagent swarm orchestration",
            "• Shared file contention & git merge lock",
            "• In-repo test loop & CI auto-fix routines",
            "• PR visual proof verification gate"
        ]
    },
    {
        "day": "Day 3 · Production Release",
        "metric": "07:58:23 · 26 OBS (21 Verified)",
        "color": EMERALD,
        "bullets": [
            "• Real-player production game launch",
            "• ~300 PR review bottleneck in main repo",
            "• Cloudflare WAF edge incident & recovery",
            "• Live player traffic & sponsor ad bidding"
        ]
    }
]

for i, c in enumerate(cards):
    cx = x_start + i * (card_w + spacing)
    # Background card
    draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=12, fill=CARD_BG, outline=CARD_BORDER, width=1)
    # Accent top border
    draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + 4], radius=2, fill=c["color"])
    
    # Card Header
    draw.text((cx + 18, card_y + 14), c["day"], font=font_card_title, fill=WHITE)
    # Metric badge
    draw.text((cx + 18, card_y + 40), c["metric"], font=font_card_metric, fill=c["color"])
    
    # Bullets
    by = card_y + 68
    for b in c["bullets"]:
        draw.text((cx + 18, by), b, font=font_card_body, fill=SLATE_400)
        by += 23

# 4. Bottleneck Migration Model Flow Banner
banner_y = 390
banner_h = 138
draw.rounded_rectangle([50, banner_y, WIDTH - 50, banner_y + banner_h], radius=12, fill=(15, 23, 42), outline=(2, 132, 199), width=1)

# Flow banner title
draw.text((70, banner_y + 12), "CORE DISCOVERY: MULTI-AGENT BOTTLENECK MIGRATION MODEL (HYP-SYNTH-001)", font=font_flow_title, fill=CYAN)

# 3 Migration Boxes
box_w = 310
box_h = 76
box_y = banner_y + 42
box_gap = 60

boxes = [
    ("Phase 1: In-Agent Sandbox", ["Permissions & API credentials", "HITL 195s approval gate latency"], CYAN),
    ("Phase 2: Swarm Interconnect", ["Concurrency & shared filesystem", "Cross-bot git merge contention"], PURPLE),
    ("Phase 3: Production Perimeter", ["Edge WAF & incident recovery", "~300 PR incoming queue bottleneck"], EMERALD)
]

def draw_arrow(draw_ctx, start_x, start_y, end_x, end_y, color):
    draw_ctx.line([(start_x, start_y), (end_x, start_y)], fill=color, width=2)
    head_len = 8
    draw_ctx.polygon([
        (end_x, start_y),
        (end_x - head_len, start_y - 5),
        (end_x - head_len, start_y + 5)
    ], fill=color)

for idx, (title, lines, color) in enumerate(boxes):
    bx = 70 + idx * (box_w + box_gap)
    draw.rounded_rectangle([bx, box_y, bx + box_w, box_y + box_h], radius=8, fill=(24, 33, 47), outline=(71, 85, 105), width=1)
    draw.text((bx + 14, box_y + 10), title, font=font_flow_box, fill=color)
    draw.text((bx + 14, box_y + 34), lines[0], font=font_flow_desc, fill=SLATE_300)
    draw.text((bx + 14, box_y + 52), lines[1], font=font_flow_desc, fill=SLATE_400)
    
    # Vector arrow between boxes
    if idx < 2:
        arrow_start_x = bx + box_w + 14
        arrow_end_x = arrow_start_x + box_gap - 28
        arrow_mid_y = box_y + (box_h // 2)
        draw_arrow(draw, arrow_start_x, arrow_mid_y, arrow_end_x, arrow_mid_y, CYAN)

# 5. Footer
footer_y = 562
draw.ellipse([52, footer_y + 3, 62, footer_y + 13], fill=EMERALD)
draw.text((72, footer_y + 1), "88 Atomic Observations · 10-Axis Comparison · Dual-Audited Physical Provenance", font=font_footer, fill=SLATE_300)

repo_text = "github.com/billgaohub/grokbot-live-study"
draw.text((WIDTH - 50 - 365, footer_y + 1), repo_text, font=font_footer, fill=CYAN)

output_path = "/Users/bill/grokbot-live-study/assets/social-preview.png"
img.save(output_path, "PNG", optimize=True)
print(f"Social preview card generated successfully at: {output_path}")
