# -*- coding: utf-8 -*-
"""
Generate a properly wired schematic in SVG format, showing all 27 nets
as physical wires (manhattan routing) between components.
"""
from pathlib import Path

OUT = Path(r"C:\Users\hbenm\Documents\s3-salle-de-bain\kicad")
OUT.mkdir(parents=True, exist_ok=True)

# Canvas A3 landscape : 1684 x 1190 pt (at 72dpi). Use mm with viewBox.
W, H = 1684, 1190
GRID = 10  # spacing unit

# ============================================================================
# COMPONENTS - layout grid
# ============================================================================
# (ref, value, x, y, w, h, pins=[(name, side, net)])
# side: 'L', 'R', 'T', 'B'

COMPONENTS = [
    # ESP32-S3 central
    {
        "ref": "U1", "value": "ESP32-S3 DevKitC-1",
        "x": 700, "y": 200, "w": 280, "h": 700,
        "pins": [
            ("GPIO1",  "L", "BTN_CENTER"),
            ("GPIO2",  "L", "MUTE_SW"),
            ("GPIO4",  "L", "MIC_LRCLK"),
            ("GPIO5",  "L", "MIC_BCLK"),
            ("GPIO11", "L", "MIC_DIN"),
            ("GPIO16", "L", "ENC_A"),
            ("GPIO17", "L", "JACK_DET"),
            ("GPIO18", "L", "ENC_B"),
            ("GPIO7",  "R", "DAC_LRCK"),
            ("GPIO8",  "R", "DAC_BCK"),
            ("GPIO10", "R", "DAC_DIN"),
            ("GPIO21", "R", "LED_DIN_RAW"),
            ("GPIO9",  "R", "LED_PWR_EN"),
            ("GPIO47", "R", "AMP_EN"),
            ("3V3",    "T", "+3V3"),
            ("5V",     "T", "+5V"),
            ("EN",     "T", "EN"),
            ("GND",    "B", "GND"),
        ],
    },
    # Microphone MEMS (left, near GPIO4/5/11)
    {
        "ref": "U4", "value": "INMP441 / ICS-43434",
        "x": 220, "y": 340, "w": 180, "h": 170,
        "pins": [
            ("VDD",  "R", "+3V3"),
            ("GND",  "R", "GND"),
            ("L/R",  "R", "GND"),
            ("WS",   "R", "MIC_LRCLK"),
            ("SCK",  "R", "MIC_BCLK"),
            ("SD",   "R", "MIC_DIN"),
        ],
    },
    # Encoder (left, near GPIO16/18 + GPIO1)
    {
        "ref": "SW1", "value": "Encodeur EC11",
        "x": 220, "y": 560, "w": 180, "h": 150,
        "pins": [
            ("A",      "R", "ENC_A"),
            ("C",      "R", "GND"),
            ("B",      "R", "ENC_B"),
            ("BTN_A",  "R", "BTN_CENTER"),
            ("BTN_B",  "R", "GND"),
        ],
    },
    # Mute switch (left, near GPIO2)
    {
        "ref": "SW2", "value": "Switch mute SPDT",
        "x": 220, "y": 760, "w": 180, "h": 100,
        "pins": [
            ("COM",  "R", "MUTE_SW"),
            ("NO",   "R", "GND"),
            ("NC",   "R", "NC1"),
        ],
    },
    # Jack 3.5mm (left, near GPIO17)
    {
        "ref": "J1", "value": "Jack 3.5mm (PJ320E)",
        "x": 220, "y": 900, "w": 180, "h": 150,
        "pins": [
            ("Tip",   "R", "AUDIO_L"),
            ("Ring",  "R", "AUDIO_R"),
            ("Sleeve","R", "GND"),
            ("Det",   "R", "JACK_DET"),
            ("DetGnd","R", "GND"),
        ],
    },
    # PCM5102 DAC (right, near GPIO7/8/10)
    {
        "ref": "U2", "value": "PCM5102 DAC",
        "x": 1180, "y": 250, "w": 220, "h": 350,
        "pins": [
            ("VIN",  "L", "+3V3"),
            ("GND",  "L", "GND"),
            ("BCK",  "L", "DAC_BCK"),
            ("DIN",  "L", "DAC_DIN"),
            ("LRCK", "L", "DAC_LRCK"),
            ("SCK",  "R", "GND"),
            ("FMT",  "R", "GND"),
            ("FLT",  "R", "GND"),
            ("DEMP", "R", "GND"),
            ("XSMT", "R", "+3V3"),
            ("LOUT", "R", "AUDIO_L"),
            ("ROUT", "R", "AUDIO_R"),
        ],
    },
    # PAM8403 Amp (right, near GPIO47)
    {
        "ref": "U3", "value": "PAM8403 ampli class-D",
        "x": 1180, "y": 700, "w": 220, "h": 270,
        "pins": [
            ("VCC",   "L", "+5V"),
            ("GND",   "L", "GND"),
            ("SHDN",  "L", "AMP_EN"),
            ("LIN",   "L", "AUDIO_L"),
            ("RIN",   "L", "AUDIO_R"),
            ("LOUT+", "R", "SPK_L+"),
            ("LOUT-", "R", "SPK_L-"),
            ("ROUT+", "R", "SPK_R+"),
            ("ROUT-", "R", "SPK_R-"),
        ],
    },
    # WS2812 ring (right top, near GPIO21)
    {
        "ref": "DS1", "value": "WS2812 Ring 12 LEDs",
        "x": 1450, "y": 240, "w": 180, "h": 130,
        "pins": [
            ("VCC",  "L", "+5V_LED"),
            ("GND",  "L", "GND"),
            ("DIN",  "L", "LED_DIN"),
            ("DOUT", "L", "LED_DOUT"),
        ],
    },
    # Series resistor WS2812
    {
        "ref": "R2", "value": "330 Ω",
        "x": 1290, "y": 290, "w": 80, "h": 50,
        "pins": [
            ("1", "L", "LED_DIN_RAW"),
            ("2", "R", "LED_DIN"),
        ],
    },
    # P-MOSFET for LED power gate
    {
        "ref": "Q1", "value": "P-MOS AO3401",
        "x": 1450, "y": 410, "w": 180, "h": 130,
        "pins": [
            ("G", "L", "LED_PWR_EN"),
            ("S", "T", "+5V"),
            ("D", "R", "+5V_LED"),
        ],
    },
    # Speakers
    {
        "ref": "HP_L", "value": "HP gauche 40mm 4Ω 3W",
        "x": 1450, "y": 720, "w": 180, "h": 90,
        "pins": [("+", "L", "SPK_L+"), ("-", "L", "SPK_L-")],
    },
    {
        "ref": "HP_R", "value": "HP droit 40mm 4Ω 3W",
        "x": 1450, "y": 850, "w": 180, "h": 90,
        "pins": [("+", "L", "SPK_R+"), ("-", "L", "SPK_R-")],
    },
    # Power: USB-C + LDO + ferrite + TVS
    {
        "ref": "J2", "value": "USB-C 5V",
        "x": 700, "y": 70, "w": 130, "h": 60,
        "pins": [
            ("VBUS", "B", "+5V"),
            ("GND",  "B", "GND"),
        ],
    },
    {
        "ref": "U5", "value": "AMS1117-3.3 LDO",
        "x": 880, "y": 70, "w": 130, "h": 60,
        "pins": [
            ("VIN",  "L", "+5V"),
            ("VOUT", "B", "+3V3"),
            ("GND",  "R", "GND"),
        ],
    },
]

# ============================================================================
# SVG generation
# ============================================================================
GOLD = "#B08D57"
INK = "#1A1612"
INK_SOFT = "#4A4036"
MUTE = "#8A7D6E"
HAIR = "#E5DECF"
BG = "#FAF6EE"
NETCOLOR = {
    "GND": "#1A1612",
    "+3V3": "#C0392B",   # red
    "+5V": "#E67E22",    # orange
    "+5V_LED": "#D68910",
    "EN": "#7D6608",
}
DEFAULT_NET = "#5B7299"  # blue gray signals
AUDIO_NETS = ("AUDIO_L", "AUDIO_R", "SPK_")

def net_color(net):
    if net in NETCOLOR:
        return NETCOLOR[net]
    if any(net.startswith(p) for p in AUDIO_NETS):
        return "#7E5109"  # dark brown for audio
    return DEFAULT_NET

# Compute absolute pin positions on each component
PIN_LEN = 20  # pin stub length

def pin_positions(comp):
    """Return list of (pin_name, x, y, side, net) for each pin."""
    cx, cy = comp["x"], comp["y"]
    w, h = comp["w"], comp["h"]
    sides = {"L": [], "R": [], "T": [], "B": []}
    for name, side, net in comp["pins"]:
        sides[side].append((name, net))
    out = []
    for side, plist in sides.items():
        n = len(plist)
        if side in ("L", "R"):
            # vertical spacing
            spacing = (h - 30) / max(n, 1) if n > 1 else 0
            start = cy - (h-30)/2 + (spacing/2 if n > 1 else h/2-15)
            for i, (name, net) in enumerate(plist):
                py = cy - h/2 + 15 + (h-30) * (i + 0.5) / n
                if side == "L":
                    px = cx - w/2
                else:
                    px = cx + w/2
                out.append((name, px, py, side, net))
        else:
            spacing = (w - 30) / max(n, 1) if n > 1 else 0
            for i, (name, net) in enumerate(plist):
                px = cx - w/2 + 15 + (w-30) * (i + 0.5) / n
                if side == "T":
                    py = cy - h/2
                else:
                    py = cy + h/2
                out.append((name, px, py, side, net))
    return out

# ============================================================================
# Build SVG
# ============================================================================
svg_parts = []
svg_parts.append(f'<?xml version="1.0" encoding="UTF-8"?>')
svg_parts.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" font-family="\'Inter\', \'Helvetica\', sans-serif">'
)
# Background
svg_parts.append(f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>')

# Title block
svg_parts.append(f'<g>')
svg_parts.append(
    f'<text x="{W/2}" y="40" text-anchor="middle" font-family="Times" '
    f'font-size="26" font-weight="bold" fill="{GOLD}">'
    f'S3 Salle de Bain — Schema de cablage ESP32-S3</text>'
)
svg_parts.append(
    f'<text x="{W/2}" y="62" text-anchor="middle" font-family="Times" '
    f'font-style="italic" font-size="13" fill="{MUTE}">'
    f'23 composants — 27 nets — genere depuis s3-salle-de-bain.yaml</text>'
)
svg_parts.append(f'</g>')

# ----- Compute all pin positions -----
all_pins = {}  # ref -> list of (name, x, y, side, net)
for comp in COMPONENTS:
    all_pins[comp["ref"]] = pin_positions(comp)

# Group pins by net
nets_pins = {}  # net -> list of (ref, name, x, y, side)
for ref, plist in all_pins.items():
    for name, x, y, side, net in plist:
        if net.startswith("NC"):
            continue
        nets_pins.setdefault(net, []).append((ref, name, x, y, side))

# ----- Draw nets (wires) first so they're under components -----
# Strategy : for each net with N pins, route via a "trunk" line
# Power rails (GND, +3V3, +5V) : use horizontal trunk
# Signal nets : direct manhattan between pairs
import statistics

def draw_wire(svg, x1, y1, x2, y2, color, width=1.6):
    svg.append(
        f'<polyline points="{x1},{y1} {x2},{y1} {x2},{y2}" '
        f'stroke="{color}" stroke-width="{width}" fill="none" '
        f'stroke-linejoin="round"/>'
    )

def draw_stub(svg, x, y, side, color, length=PIN_LEN, width=1.6):
    if side == "L":
        x2, y2 = x - length, y
    elif side == "R":
        x2, y2 = x + length, y
    elif side == "T":
        x2, y2 = x, y - length
    else:
        x2, y2 = x, y + length
    svg.append(
        f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{width}"/>'
    )
    return x2, y2

# Draw stubs and labels
svg_parts.append('<g id="wires">')
for net, pin_list in nets_pins.items():
    color = net_color(net)

    # 1) Draw a stub for each pin
    stub_ends = []  # (x, y)
    for ref, name, x, y, side in pin_list:
        ex, ey = draw_stub(svg_parts, x, y, side, color)
        stub_ends.append((ex, ey, side))

    # 2) For power rails, draw a vertical/horizontal trunk
    if net in ("GND", "+3V3", "+5V", "+5V_LED"):
        # Vertical trunk for power - find median X
        xs = [e[0] for e in stub_ends]
        ys = [e[1] for e in stub_ends]
        # Use a dedicated trunk position
        if net == "GND":
            trunk_y = max(ys) + 30   # bottom rail
            # Horizontal trunk
            xmin, xmax = min(xs), max(xs)
            svg_parts.append(
                f'<line x1="{xmin}" y1="{trunk_y}" x2="{xmax}" y2="{trunk_y}" '
                f'stroke="{color}" stroke-width="2.4"/>'
            )
            # Vertical from each stub to trunk
            for (ex, ey, _side) in stub_ends:
                svg_parts.append(
                    f'<line x1="{ex}" y1="{ey}" x2="{ex}" y2="{trunk_y}" '
                    f'stroke="{color}" stroke-width="1.8"/>'
                )
                # Dot at junction
                svg_parts.append(
                    f'<circle cx="{ex}" cy="{trunk_y}" r="2.5" fill="{color}"/>'
                )
        elif net == "+3V3":
            trunk_y = min(ys) - 30
            xmin, xmax = min(xs), max(xs)
            svg_parts.append(
                f'<line x1="{xmin}" y1="{trunk_y}" x2="{xmax}" y2="{trunk_y}" '
                f'stroke="{color}" stroke-width="2.4"/>'
            )
            for (ex, ey, _side) in stub_ends:
                svg_parts.append(
                    f'<line x1="{ex}" y1="{ey}" x2="{ex}" y2="{trunk_y}" '
                    f'stroke="{color}" stroke-width="1.8"/>'
                )
                svg_parts.append(
                    f'<circle cx="{ex}" cy="{trunk_y}" r="2.5" fill="{color}"/>'
                )
        elif net == "+5V":
            trunk_y = min(ys) - 50
            xmin, xmax = min(xs), max(xs)
            svg_parts.append(
                f'<line x1="{xmin}" y1="{trunk_y}" x2="{xmax}" y2="{trunk_y}" '
                f'stroke="{color}" stroke-width="2.4"/>'
            )
            for (ex, ey, _side) in stub_ends:
                svg_parts.append(
                    f'<line x1="{ex}" y1="{ey}" x2="{ex}" y2="{trunk_y}" '
                    f'stroke="{color}" stroke-width="1.8"/>'
                )
                svg_parts.append(
                    f'<circle cx="{ex}" cy="{trunk_y}" r="2.5" fill="{color}"/>'
                )
        else:  # +5V_LED
            # short - 2 pins only
            if len(stub_ends) >= 2:
                e1 = stub_ends[0]
                e2 = stub_ends[1]
                draw_wire(svg_parts, e1[0], e1[1], e2[0], e2[1], color, 2.0)
    else:
        # 2-pin and N-pin signals: manhattan route from first pin to each next
        if len(stub_ends) >= 2:
            base = stub_ends[0]
            for other in stub_ends[1:]:
                # 3-segment route: from base.x -> mid_x -> other.x
                mid_x = (base[0] + other[0]) / 2
                svg_parts.append(
                    f'<polyline points="{base[0]},{base[1]} {mid_x},{base[1]} '
                    f'{mid_x},{other[1]} {other[0]},{other[1]}" '
                    f'stroke="{color}" stroke-width="1.6" fill="none" '
                    f'stroke-linejoin="round"/>'
                )

svg_parts.append('</g>')

# ----- Draw components -----
svg_parts.append('<g id="components">')
for comp in COMPONENTS:
    cx, cy = comp["x"], comp["y"]
    w, h = comp["w"], comp["h"]
    x = cx - w/2
    y = cy - h/2
    # Body
    svg_parts.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
        f'fill="white" stroke="{INK}" stroke-width="1.6" rx="4"/>'
    )
    # Ref + value
    svg_parts.append(
        f'<text x="{cx}" y="{y+18}" text-anchor="middle" '
        f'font-size="14" font-weight="bold" fill="{GOLD}">{comp["ref"]}</text>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{y+34}" text-anchor="middle" '
        f'font-size="10" fill="{INK_SOFT}">{comp["value"]}</text>'
    )
    # Pins (labels next to body)
    for name, px, py, side, net in pin_positions(comp):
        # Small pin dot
        svg_parts.append(
            f'<circle cx="{px}" cy="{py}" r="3" fill="{INK}"/>'
        )
        # Label inside the box, next to pin
        if side == "L":
            tx, ty, anchor = px + 8, py + 4, "start"
        elif side == "R":
            tx, ty, anchor = px - 8, py + 4, "end"
        elif side == "T":
            tx, ty, anchor = px, py + 14, "middle"
        else:
            tx, ty, anchor = px, py - 6, "middle"
        svg_parts.append(
            f'<text x="{tx}" y="{ty}" text-anchor="{anchor}" '
            f'font-size="9" fill="{INK}" font-family="monospace">{name}</text>'
        )
svg_parts.append('</g>')

# ----- Net labels at stub ends -----
svg_parts.append('<g id="netlabels">')
for net, pin_list in nets_pins.items():
    if net in ("GND", "+3V3", "+5V", "+5V_LED"):
        # already shown via colored trunk, label once at trunk
        xs = [e[2] for e in pin_list]
        ys = [e[3] for e in pin_list]
        if net == "GND":
            label_y = max(ys) + 30 - 5
        elif net == "+3V3":
            label_y = min(ys) - 30 + 15
        elif net == "+5V":
            label_y = min(ys) - 50 + 15
        else:
            label_y = sum(ys)/len(ys)
        label_x = min(xs) - 5
        color = net_color(net)
        svg_parts.append(
            f'<text x="{label_x}" y="{label_y}" font-size="11" font-weight="bold" '
            f'fill="{color}" text-anchor="end">{net}</text>'
        )
    else:
        # tag each signal net with a small label near first stub end
        ref0, name0, x0, y0, side0 = pin_list[0]
        if side0 == "L":
            lx, ly, anchor = x0 - PIN_LEN - 4, y0 - 4, "end"
        elif side0 == "R":
            lx, ly, anchor = x0 + PIN_LEN + 4, y0 - 4, "start"
        else:
            lx, ly, anchor = x0, y0, "middle"
        color = net_color(net)
        svg_parts.append(
            f'<text x="{lx}" y="{ly}" font-size="8.5" font-style="italic" '
            f'fill="{color}" text-anchor="{anchor}" '
            f'font-family="monospace">{net}</text>'
        )
svg_parts.append('</g>')

# Legend
legend_y = H - 70
svg_parts.append('<g id="legend">')
svg_parts.append(
    f'<text x="40" y="{legend_y}" font-size="11" font-weight="bold" '
    f'fill="{GOLD}">Legende</text>'
)
items = [
    ("GND",      NETCOLOR["GND"]),
    ("+3V3",     NETCOLOR["+3V3"]),
    ("+5V",      NETCOLOR["+5V"]),
    ("+5V_LED",  NETCOLOR["+5V_LED"]),
    ("Audio",    "#7E5109"),
    ("Signaux",  DEFAULT_NET),
]
x_leg = 40
for i, (label, color) in enumerate(items):
    yy = legend_y + 20 + (i // 3) * 20
    xx = x_leg + (i % 3) * 200
    svg_parts.append(
        f'<line x1="{xx}" y1="{yy}" x2="{xx+25}" y2="{yy}" '
        f'stroke="{color}" stroke-width="2.4"/>'
    )
    svg_parts.append(
        f'<text x="{xx+30}" y="{yy+3}" font-size="10" fill="{INK_SOFT}">{label}</text>'
    )
svg_parts.append('</g>')

# Bottom credit
svg_parts.append(
    f'<text x="{W-40}" y="{H-30}" text-anchor="end" font-size="9" '
    f'fill="{MUTE}" font-style="italic">'
    f'github.com/hanafi09/s3-salle-de-bain · Hanafi BENMESBAH · domokami</text>'
)

svg_parts.append('</svg>')

# Write
SVG_PATH = OUT / "s3-salle-de-bain-schema.svg"
SVG_PATH.write_text("\n".join(svg_parts), encoding='utf-8')
print(f"OK SVG : {SVG_PATH}")
print(f"  Composants : {len(COMPONENTS)}")
print(f"  Nets : {len(nets_pins)}")
print(f"  Pins total : {sum(len(p) for p in all_pins.values())}")
