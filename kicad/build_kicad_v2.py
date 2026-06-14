# -*- coding: utf-8 -*-
"""
KiCad 8 schematic with REAL standard symbols AND proper wiring.

Strategy for clean, valid, professional output:
  - Standard symbols: Device:R, Device:C, Device:CP, Device:L,
    Device:Q_PMOS_GSD, Device:Speaker, Switch:SW_SPDT, power:GND/+3V3/+5V
  - IC modules: custom rectangular symbols with proper pin labels
  - WIRING: every pin gets a short wire stub. Signal pins get a net LABEL
    (KiCad connects all same-name labels into one net). Power pins get a
    power symbol (GND/+3V3/+5V) wired with a stub.
  - All instances at rotation 0 -> pin endpoints are trivially computable
    -> no rotation math errors.

This is the standard way dense schematics are drawn (labels, not spaghetti).
"""
import uuid, os
from pathlib import Path

OUT = Path(os.path.dirname(os.path.abspath(__file__)))
OUT.mkdir(parents=True, exist_ok=True)

def U(): return str(uuid.uuid4())
GRID = 2.54

# Snap a coordinate to the 1.27mm KiCad grid (avoids endpoint_off_grid ERC)
def gsnap(v): return round(v / 1.27) * 1.27

# Import the EXACT KiCad 10 standard symbols (extracted from installed libs)
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kicad_std_symbols import STD_SYMBOLS as STD_SYMBOLS_REAL

# ============================================================================
# Standard KiCad library symbols (verbatim, self-contained)
# ============================================================================
STD_SYMBOLS = r'''
    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Device:C" (pin_numbers hide) (pin_names (offset 0.254) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
      )
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Device:CP" (pin_numbers hide) (pin_names (offset 0.254) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "CP" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CP_0_1"
        (rectangle (start -2.286 0.508) (end 2.286 1.016) (stroke (width 0) (type default)) (fill (type outline)))
        (rectangle (start -2.286 -1.016) (end 2.286 -0.508) (stroke (width 0) (type default)) (fill (type outline)))
        (polyline (pts (xy -1.524 2.286) (xy -0.508 2.286)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.016 2.794) (xy -1.016 1.778)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "CP_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Device:L" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "L" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "L" (at 1.905 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "L_0_1"
        (arc (start 0 -2.54) (mid 0.6323 -1.905) (end 0 -1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 -1.27) (mid 0.6323 -0.635) (end 0 0) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 0) (mid 0.6323 0.635) (end 0 1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 1.27) (mid 0.6323 1.905) (end 0 2.54) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "L_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Device:Q_PMOS_GSD" (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "Q" (at 5.08 1.27 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "Q_PMOS_GSD" (at 5.08 -1.27 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 5.08 -3.81 0) (effects (font (size 1.27 1.27)) (justify left) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Q_PMOS_GSD_0_1"
        (polyline (pts (xy 0.508 0) (xy 2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -2.54) (xy 2.54 -1.27) (xy 0.762 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 1.27) (xy 2.54 1.27) (xy 2.54 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -2) (xy 0.762 -0.5)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -0.25) (xy 0.762 0.25)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 0.5) (xy 0.762 2)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 0) (xy 0 0) (xy 0 -2.04) (xy 0 -1.95)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.286 -0.508) (xy 1.524 0) (xy 2.286 0.508) (xy 2.286 -0.508)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.397 0) (radius 2.794) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "Q_PMOS_GSD_1_1"
        (pin input line (at -5.08 0 0) (length 5.08)
          (name "G" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54)
          (name "S" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54)
          (name "D" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Device:Speaker" (pin_numbers hide) (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "LS" (at -2.54 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "Speaker" (at -2.54 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Speaker_0_1"
        (rectangle (start -5.08 -3.81) (end -2.54 3.81) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -2.54 -3.81) (xy 2.54 -7.62) (xy 2.54 7.62) (xy -2.54 3.81)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "Speaker_1_1"
        (pin passive line (at -7.62 2.54 0) (length 2.54)
          (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -7.62 -2.54 0) (length 2.54)
          (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Switch:SW_SPDT" (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at -2.54 3.81 0) (effects (font (size 1.27 1.27)) (justify right)))
      (property "Value" "SW_SPDT" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "SW_SPDT_0_1"
        (circle (center -1.524 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type outline)))
        (polyline (pts (xy -1.016 0.254) (xy 1.524 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 2.032 2.54) (radius 0.508) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 2.032 -2.54) (radius 0.508) (stroke (width 0) (type default)) (fill (type outline)))
      )
      (symbol "SW_SPDT_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54)
          (name "A" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 2.54 180) (length 2.54)
          (name "B" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 -2.54 180) (length 2.54)
          (name "C" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "power:GND" (power) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) hide
          (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "power:+3V3" (power) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+3V3_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+3V3_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide
          (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "power:+5V" (power) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+5V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+5V_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide
          (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )
'''

# ============================================================================
# Custom IC modules with proper pin labels
# ============================================================================
# pins: list of (num, name, side)  side in L/R/T/B
ESP32_PINS = [
    ("1","GPIO1","L"),("2","GPIO2","L"),("3","GPIO4","L"),("4","GPIO5","L"),
    ("5","GPIO11","L"),("6","GPIO16","L"),("7","GPIO17","L"),("8","GPIO18","L"),
    ("9","GPIO7","R"),("10","GPIO8","R"),("11","GPIO10","R"),("12","GPIO21","R"),
    ("13","GPIO9","R"),("14","GPIO47","R"),
    ("15","3V3","T"),("16","5V","T"),("17","GND","B"),
]
# GY-PCM5102 / WCMCU module pinout (matches the real board silk)
PCM_PINS = [
    ("1","XMT","L"),("2","FMT","L"),("3","LCK","L"),("4","DIN","L"),
    ("5","BCK","L"),("6","SCL","L"),("7","DMP","L"),
    ("8","FLT","R"),("9","GND","R"),("10","3V3","R"),("11","VCC","R"),
    ("L","Lout","R"),("G","Gout","R"),("R","Rout","R"),
]
PAM_PINS = [
    ("1","VCC","L"),("2","GND","L"),("3","SHDN","L"),("4","LIN","L"),("5","RIN","L"),
    ("6","LOUT+","R"),("7","ROUT+","R"),
]
MIC_PINS = [("1","VDD","R"),("2","GND","R"),("3","L/R","R"),("4","WS","R"),("5","SCK","R"),("6","SD","R")]
WS_PINS = [("1","VCC","L"),("2","GND","L"),("3","DIN","L")]
ENC_PINS = [("1","A","R"),("2","C","R"),("3","B","R"),("4","BTN_A","R"),("5","BTN_B","R")]
JACK_PINS = [("1","Tip","R"),("2","Ring","R"),("3","Sleeve","R"),("4","Det","R")]
USB_PINS = [("1","VBUS","R"),("2","GND","R")]
LDO_PINS = [("3","VIN","L"),("2","VOUT","R"),("1","GND","B")]

CUSTOM = {
    "ESP32-S3": ESP32_PINS, "PCM5102": PCM_PINS, "PAM8403": PAM_PINS,
    "INMP441": MIC_PINS, "WS2812-Ring": WS_PINS, "EC11-Encoder": ENC_PINS,
    "Jack-3.5mm": JACK_PINS, "USB-C": USB_PINS, "AMS1117-3.3": LDO_PINS,
}

IC_W = 25.4  # IC body width (mm)

def custom_geom(pins, w=IC_W):
    """Return (h, pin_rel_coords) where pin_rel_coords[num]=(rel_x, rel_y, side)."""
    sides = {"L":[],"R":[],"T":[],"B":[]}
    for p in pins: sides[p[2]].append(p)
    nL, nR = len(sides["L"]), len(sides["R"])
    h = max(nL, nR, 1)*GRID + 5.08
    coords = {}
    for side, plist in sides.items():
        for i,(num,name,_) in enumerate(plist):
            if side=="L":
                rel_x=-w/2-GRID; rel_y=h/2-GRID-i*GRID
            elif side=="R":
                rel_x=w/2+GRID; rel_y=h/2-GRID-i*GRID
            elif side=="T":
                rel_y=h/2+GRID; rel_x=-w/2+GRID+i*GRID
            else:
                rel_y=-h/2-GRID; rel_x=-w/2+GRID+i*GRID
            coords[num]=(rel_x, rel_y, side)
    return h, coords

CUSTOM_GEOM = {name: custom_geom(pins) for name, pins in CUSTOM.items()}

def custom_symbol_def(name, pins):
    h, coords = CUSTOM_GEOM[name]
    w = IC_W
    body = (f'      (symbol "{name}_0_1"\n'
            f'        (rectangle (start {-w/2} {-h/2}) (end {w/2} {h/2})\n'
            f'          (stroke (width 0.254) (type default)) (fill (type background)))\n'
            f'      )\n')
    PWR_PIN_NAMES = {"VDD","VCC","VIN","GND","3V3","5V","+3V3","+5V","VBUS","VOUT"}
    pin_xml=[]
    for num,pname,side in pins:
        rel_x,rel_y,_ = coords[num]
        orient={"L":0,"R":180,"T":270,"B":90}[side]
        ptype = "power_in" if pname in PWR_PIN_NAMES else "bidirectional"
        pin_xml.append(
            f'        (pin {ptype} line (at {rel_x} {rel_y} {orient}) (length {GRID})\n'
            f'          (name "{pname}" (effects (font (size 1.0 1.0)))) (number "{num}" (effects (font (size 1.0 1.0)))))\n')
    body_pins = f'      (symbol "{name}_1_1"\n' + ''.join(pin_xml) + '      )\n'
    return (f'    (symbol "Local:{name}" (pin_names (offset 0.508)) (in_bom yes) (on_board yes)\n'
            f'      (property "Reference" "U" (at 0 {h/2+3} 0) (effects (font (size 1.2 1.2))))\n'
            f'      (property "Value" "{name}" (at 0 {-h/2-3} 0) (effects (font (size 1.0 1.0))))\n'
            f'      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))\n'
            f'      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))\n'
            f'{body}{body_pins}    )\n')

custom_libs_block = "".join(custom_symbol_def(n, p) for n, p in CUSTOM.items())

# ============================================================================
# Standard symbol pin relative endpoints (rotation 0)
# In lib space +Y up. When placed at rot 0 -> abs = (Ix+relx, Iy-rely)
# ============================================================================
# Parse the REAL pin positions from the extracted standard symbols.
# This guarantees wire endpoints land exactly on the symbol pins.
import re as _re
def _parse_std_pins(std_text):
    out = {}
    # locate each top-level (symbol "Lib:Name" ...) block
    for m in _re.finditer(r'\(symbol\s+"([A-Za-z0-9_+:]+:[A-Za-z0-9_+]+)"', std_text):
        libid = m.group(1)
        # balance parens to get the full block
        start = m.start(); depth = 0; i = start
        while i < len(std_text):
            if std_text[i] == '(': depth += 1
            elif std_text[i] == ')':
                depth -= 1
                if depth == 0: break
            i += 1
        block = std_text[start:i+1]
        pins = {}
        for pm in _re.finditer(
            r'\(pin\s+\w+\s+\w+\s*\(at\s+([\-0-9.]+)\s+([\-0-9.]+)\s+\d+\)'
            r'.*?\(number\s+"([^"]+)"', block, _re.DOTALL):
            x, y, num = float(pm.group(1)), float(pm.group(2)), pm.group(3)
            pins[num] = (x, y)
        out[libid] = pins
    return out

STD_PINS = _parse_std_pins(STD_SYMBOLS_REAL)

def pin_abs(lib_id, ix, iy, num):
    """Absolute pin endpoint for instance at (ix,iy) rot 0."""
    if lib_id.startswith("Local:"):
        name = lib_id.split(":")[1]
        _, coords = CUSTOM_GEOM[name]
        rx, ry, _ = coords[num]
    else:
        rx, ry = STD_PINS[lib_id][num]
    return (round(ix+rx, 2), round(iy-ry, 2))

# ============================================================================
# INSTANCES + NET ASSIGNMENT
# ============================================================================
SCH_UUID = U()
instances = []   # dicts
wires = []
labels = []
power_syms = []  # extra power-symbol instances (auto)

def place(ref, lib_id, x, y, value):
    # snap placement to 1.27mm grid so all pin endpoints stay on-grid
    instances.append({"ref":ref,"lib_id":lib_id,"x":gsnap(x),"y":gsnap(y),"value":value})

# --- Layout (all rotation 0) ---
# Left column: micro / encoder / mute / jack
place("U4","Local:INMP441",     70, 70, "INMP441 MEMS")
place("SW1","Local:EC11-Encoder",70, 120,"Encodeur EC11")
place("SW2","Switch:SW_SPDT",   70, 165,"Switch mute")
place("J1","Local:Jack-3.5mm",  70, 200,"Jack 3.5mm")
# Center: ESP32
place("U1","Local:ESP32-S3",    150, 110,"ESP32-S3 DevKitC-1")
# Right: DAC / amp / ring / mosfet / speakers
place("U2","Local:PCM5102",     240, 80, "PCM5102 DAC")
place("U3","Local:PAM8403",     240, 145,"PAM8403")
place("DS1","Local:WS2812-Ring",310, 75, "WS2812 Ring x12")
place("R2","Device:R",          285, 75, "330")
place("Q1","Device:Q_PMOS",     310, 120,"AO3401")
place("HP1","Device:Speaker",   320, 150,"HP G 40mm 4R")
place("HP2","Device:Speaker",   320, 175,"HP D 40mm 4R")
# Power top: USB-C / LDO / ferrite / decoupling
place("J2","Local:USB-C",       110, 40, "USB-C 5V")
place("U5","Local:AMS1117-3.3", 175, 45, "AMS1117-3.3")
place("F1","Device:L",          240, 40, "Ferrite 600R")
place("C1","Device:C",          200, 200,"10uF")
place("C2","Device:C",          212, 200,"100nF")
place("C3","Device:C",          110, 70, "10uF")
place("C4","Device:C",          224, 200,"10uF")
place("C5","Device:C_Polarized",236, 200,"100uF")
place("C6","Device:C_Polarized",280, 50, "470uF")
place("R1","Device:R",          120, 95, "10k")

# Map (ref, pin) -> net  (from YAML)
PIN_NET = {
    # ESP32
    ("U1","1"):"BTN_CENTER",("U1","2"):"MUTE_SW",("U1","3"):"MIC_LRCLK",
    ("U1","4"):"MIC_BCLK",("U1","5"):"MIC_DIN",("U1","6"):"ENC_A",
    ("U1","7"):"JACK_DET",("U1","8"):"ENC_B",
    ("U1","9"):"DAC_LRCK",("U1","10"):"DAC_BCK",("U1","11"):"DAC_DIN",
    ("U1","12"):"LED_DIN_RAW",("U1","13"):"LED_PWR_EN",("U1","14"):"AMP_EN",
    ("U1","15"):"+3V3",("U1","16"):"+5V",("U1","17"):"GND",
    # PCM5102 (GY-PCM5102 module pinout: XMT FMT LCK DIN BCK SCL DMP FLT GND 3V3 VCC + L/G/R)
    ("U2","1"):"+3V3",     # XMT (tie high = un-mute)
    ("U2","2"):"GND",      # FMT
    ("U2","3"):"DAC_LRCK", # LCK
    ("U2","4"):"DAC_DIN",  # DIN
    ("U2","5"):"DAC_BCK",  # BCK
    ("U2","6"):"GND",      # SCL (internal PLL)
    ("U2","7"):"GND",      # DMP
    ("U2","8"):"GND",      # FLT
    ("U2","9"):"GND",      # GND
    ("U2","10"):"+3V3",    # 3V3
    ("U2","11"):"+3V3",    # VCC
    ("U2","L"):"AUDIO_L",  # line-out L
    ("U2","G"):"GND",      # line-out G
    ("U2","R"):"AUDIO_R",  # line-out R
    # PAM8403
    ("U3","1"):"+5V",("U3","2"):"GND",("U3","3"):"AMP_EN",("U3","4"):"AUDIO_L",
    ("U3","5"):"AUDIO_R",("U3","6"):"SPK_L",("U3","7"):"SPK_R",
    # INMP441
    ("U4","1"):"+3V3",("U4","2"):"GND",("U4","3"):"GND",("U4","4"):"MIC_LRCLK",
    ("U4","5"):"MIC_BCLK",("U4","6"):"MIC_DIN",
    # WS2812
    ("DS1","1"):"+5V_LED",("DS1","2"):"GND",("DS1","3"):"LED_DIN",
    # Encoder
    ("SW1","1"):"ENC_A",("SW1","2"):"GND",("SW1","3"):"ENC_B",
    ("SW1","4"):"BTN_CENTER",("SW1","5"):"GND",
    # Mute switch SPDT
    ("SW2","1"):"MUTE_SW",("SW2","3"):"GND",
    # Jack
    ("J1","1"):"AUDIO_L",("J1","2"):"AUDIO_R",("J1","3"):"GND",("J1","4"):"JACK_DET",
    # USB-C
    ("J2","1"):"+5V",("J2","2"):"GND",
    # LDO
    ("U5","3"):"+5V",("U5","2"):"+3V3",("U5","1"):"GND",
    # Ferrite
    ("F1","1"):"+5V",("F1","2"):"+5V_LED",
    # R2 series (LED data)
    ("R2","1"):"LED_DIN_RAW",("R2","2"):"LED_DIN",
    # Q1 P-MOS (pin numbers are letters G/S/D)
    ("Q1","G"):"LED_PWR_EN",("Q1","S"):"+5V",("Q1","D"):"+5V_LED",
    # Speakers
    ("HP1","1"):"SPK_L",("HP1","2"):"GND",
    ("HP2","1"):"SPK_R",("HP2","2"):"GND",
    # Decoupling caps
    ("C1","1"):"+5V",("C1","2"):"GND",
    ("C2","1"):"+5V",("C2","2"):"GND",
    ("C3","1"):"+3V3",("C3","2"):"GND",
    ("C4","1"):"+3V3",("C4","2"):"GND",
    ("C5","1"):"+5V",("C5","2"):"GND",
    ("C6","1"):"+5V_LED",("C6","2"):"GND",
    # R1 pullup
    ("R1","1"):"BTN_CENTER",("R1","2"):"+3V3",
}

POWER_NETS = {"GND":"power:GND", "+3V3":"power:+3V3", "+5V":"power:+5V"}
# +5V_LED handled as a normal label (no dedicated power symbol)

# ============================================================================
# Generate stubs + labels + power symbols for each pin
# ============================================================================
STUB = GRID * 3   # 7.62mm - long enough that labels clear the pin names
pwr_counter = [0]

def add_power_symbol(lib_id, x, y):
    pwr_counter[0]+=1
    ref=f"#PWR{pwr_counter[0]:02d}"
    val=lib_id.split(":")[1]
    instances.append({"ref":ref,"lib_id":lib_id,"x":x,"y":y,"value":val,"power":True})

def stub_dir(lib_id, num):
    """Direction the wire stub extends (away from body). Returns (dx,dy)."""
    if lib_id.startswith("Local:"):
        name=lib_id.split(":")[1]
        _,coords=CUSTOM_GEOM[name]
        side=coords[num][2]
        return {"L":(-1,0),"R":(1,0),"T":(0,-1),"B":(0,1)}[side]
    # standard parts
    rx,ry = STD_PINS[lib_id][num]
    # stub continues outward in the pin's pointing direction
    if lib_id in ("Device:R","Device:C","Device:C_Polarized","Device:L"):
        return (0,-1) if num=="1" else (0,1)  # pin1 up, pin2 down (screen)
    if lib_id=="Device:Q_PMOS":
        # G left, S bottom(screen +y), D top(screen -y)
        return {"G":(-1,0),"S":(0,1),"D":(0,-1)}[num]
    if lib_id=="Device:Speaker":
        return (-1,0)
    if lib_id=="Switch:SW_SPDT":
        return {"1":(-1,0),"2":(1,0),"3":(1,0)}[num]
    return (0,0)

# Build wiring for every assigned pin
for (ref,num),net in PIN_NET.items():
    inst = next(i for i in instances if i["ref"]==ref)
    px,py = pin_abs(inst["lib_id"], inst["x"], inst["y"], num)
    px,py = gsnap(px), gsnap(py)
    dx,dy = stub_dir(inst["lib_id"], num)
    ex,ey = gsnap(px+dx*STUB), gsnap(py+dy*STUB)
    # wire stub
    if (dx,dy)!=(0,0):
        wires.append((px,py,ex,ey))
    else:
        ex,ey=px,py
    if net in POWER_NETS:
        # place a power symbol at the stub end, oriented automatically
        add_power_symbol(POWER_NETS[net], ex, ey)
    else:
        # net label at stub end
        # orient label: 0 if extends right, 180 if left, 90 up, 270 down
        ori = 0
        if dx<0: ori=180
        elif dy<0: ori=90
        elif dy>0: ori=270
        labels.append((net, ex, ey, ori))

# ============================================================================
# PWR_FLAG on each rail (tells ERC the net is externally driven)
# ============================================================================
flag_counter = [0]
def add_pwr_flag(net, fx, fy):
    flag_counter[0]+=1
    ref=f"#FLG{flag_counter[0]:02d}"
    instances.append({"ref":ref,"lib_id":"power:PWR_FLAG","x":gsnap(fx),"y":gsnap(fy),
                      "value":"PWR_FLAG","power":True})
    # wire from flag pin (at fx,fy) up to fy-2.54, then label there
    wires.append((gsnap(fx),gsnap(fy),gsnap(fx),gsnap(fy-GRID)))
    if net in POWER_NETS:
        add_power_symbol(POWER_NETS[net], gsnap(fx), gsnap(fy-GRID))
    else:
        labels.append((net, gsnap(fx), gsnap(fy-GRID), 90))

# Place flags in a free area (bottom-left)
add_pwr_flag("+5V",     40, 250)
add_pwr_flag("+3V3",    60, 250)
add_pwr_flag("GND",     80, 250)
add_pwr_flag("+5V_LED",100, 250)

# ============================================================================
# Render
# ============================================================================
# Footprint assignment (must match build_pcb.py so schematic <-> PCB are linked)
FOOTPRINTS = {
    "U1":"Espressif:ESP32-S3-DevKitC",
    "U2":"Modules:GY-PCM5102",
    "U3":"Connector_PinHeader_2.54mm:PinHeader_1x07_P2.54mm_Vertical",
    "U4":"Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical",
    "U5":"Package_TO_SOT_SMD:SOT-223-3_TabPin2",
    "DS1":"Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
    "SW1":"Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm",
    "SW2":"Button_Switch_THT:SW_DIP_SPSTx01_Slide_9.78x4.72mm_W7.62mm_P2.54mm",
    "J1":"Connector_Audio:Jack_3.5mm_PJ320E_Horizontal",
    "J2":"Connector_USB:USB_C_Receptacle_Amphenol_12401610E4-2A",
    "R1":"Resistor_SMD:R_0603_1608Metric","R2":"Resistor_SMD:R_0603_1608Metric",
    "C1":"Capacitor_SMD:C_0603_1608Metric","C2":"Capacitor_SMD:C_0603_1608Metric",
    "C3":"Capacitor_SMD:C_0603_1608Metric","C4":"Capacitor_SMD:C_0603_1608Metric",
    "C5":"Capacitor_SMD:CP_Elec_5x5.3","C6":"Capacitor_SMD:CP_Elec_5x5.3",
    "Q1":"Package_TO_SOT_SMD:SOT-23","F1":"Inductor_SMD:L_0805_2012Metric",
    "HP1":"Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
    "HP2":"Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
}

def render_instance(i):
    ref=i["ref"]; lib=i["lib_id"]; x=i["x"]; y=i["y"]; val=i["value"]
    is_power = i.get("power", False)
    hide_ref = ' hide' if is_power else ''
    prop_ref = (f'    (property "Reference" "{ref}" (at {x+3} {y-3} 0) '
                f'(effects (font (size 1.27 1.27)) (justify left){hide_ref}))\n')
    prop_val = (f'    (property "Value" "{val}" (at {x+3} {y+3} 0) '
                f'(effects (font (size 1.0 1.0)) (justify left){hide_ref}))\n')
    fp = FOOTPRINTS.get(ref, "")
    prop_fp = (f'    (property "Footprint" "{fp}" (at {x} {y} 0) '
               f'(effects (font (size 1.27 1.27)) hide))\n')
    return (f'  (symbol (lib_id "{lib}") (at {x} {y} 0) (unit 1)\n'
            f'    (in_bom yes) (on_board yes) (dnp no) (uuid "{U()}")\n'
            f'{prop_ref}{prop_val}{prop_fp}'
            f'    (instances (project "s3-salle-de-bain"\n'
            f'      (path "/{SCH_UUID}" (reference "{ref}") (unit 1))))\n'
            f'  )\n')

def render_wire(w):
    x1,y1,x2,y2=w
    return (f'  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))\n'
            f'    (stroke (width 0) (type default)) (uuid "{U()}"))\n')

def render_label(l):
    net,x,y,ori=l
    return (f'  (label "{net}" (at {x} {y} {ori}) '
            f'(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{U()}"))\n')

instances_block = "".join(render_instance(i) for i in instances)
wires_block = "".join(render_wire(w) for w in wires)
labels_block = "".join(render_label(l) for l in labels)

sch = (f'(kicad_sch\n'
       f'  (version 20231120)\n  (generator "build_kicad_v2_py")\n  (generator_version "8.0")\n'
       f'  (uuid "{SCH_UUID}")\n  (paper "A2")\n'
       f'  (title_block\n'
       f'    (title "S3 Salle de Bain - Voice Assistant ESP32-S3")\n'
       f'    (date "2026-06-11")\n    (rev "v3.1")\n    (company "domokami / hanafi09")\n'
       f'    (comment 1 "Symboles standards KiCad + modules ICs custom")\n'
       f'    (comment 2 "Cablage par labels (nets) + power symbols GND/+3V3/+5V")\n'
       f'    (comment 3 "https://github.com/hanafi09/s3-salle-de-bain")\n'
       f'  )\n'
       f'  (lib_symbols\n{STD_SYMBOLS_REAL}\n{custom_libs_block}  )\n'
       f'{instances_block}{wires_block}{labels_block}'
       f'  (sheet_instances (path "/" (page "1")))\n'
       f')\n')

OUTF = OUT / "s3-salle-de-bain.kicad_sch"
OUTF.write_text(sch, encoding='utf-8')

op,cl = sch.count('('), sch.count(')')
print(f"OK schema : {OUTF}")
print(f"  Size: {len(sch)} bytes  |  Balance delta: {op-cl}")
n_ic = len([i for i in instances if not i.get('power')])
n_pwr = len([i for i in instances if i.get('power')])
print(f"  Composants reels : {n_ic}")
print(f"  Power symbols (GND/+3V3/+5V) : {n_pwr}")
print(f"  Wires (stubs) : {len(wires)}")
print(f"  Net labels : {len(labels)}")
