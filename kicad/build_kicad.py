# -*- coding: utf-8 -*-
"""
Generates a KiCad 8 schematic with VRAIMENT cabled wires (not just labels).

Approach:
  - Components placed on a 1.27mm grid
  - Each pin has a precise absolute position
  - For each net, all sharing pins are connected by physical (wire ...) segments
  - Power nets (GND, +3V3, +5V, +5V_LED) get a horizontal trunk + vertical taps
  - Signal nets get manhattan-routed wires from pin to pin
  - Global labels still added for documentation (nets readable on the schema)
"""
import uuid
import json
import os
from pathlib import Path

OUT = Path(r"C:\Users\hbenm\Documents\s3-salle-de-bain\kicad")
OUT.mkdir(parents=True, exist_ok=True)

def U():
    return str(uuid.uuid4())

GRID = 2.54  # mm

# Snap to grid
def snap(v):
    return round(v / GRID) * GRID

# ============================================================================
# COMPONENT DEFINITIONS - positions on grid (every coord is x*GRID)
# ============================================================================
# x,y in mm. w,h in mm. Pins by side - spacing GRID between each.
COMPONENTS = [
    # ESP32-S3 central
    {
        "ref": "U1", "value": "ESP32-S3-DevKitC-1",
        "footprint": "Module:ESP32-S3-DevKitC-1",
        "x": 140, "y": 100, "w": 40, "h": 70,
        "pins": [
            ("1",  "GPIO1",  "L", "BTN_CENTER"),
            ("2",  "GPIO2",  "L", "MUTE_SW"),
            ("3",  "GPIO4",  "L", "MIC_LRCLK"),
            ("4",  "GPIO5",  "L", "MIC_BCLK"),
            ("5",  "GPIO11", "L", "MIC_DIN"),
            ("6",  "GPIO16", "L", "ENC_A"),
            ("7",  "GPIO17", "L", "JACK_DET"),
            ("8",  "GPIO18", "L", "ENC_B"),
            ("9",  "GPIO7",  "R", "DAC_LRCK"),
            ("10", "GPIO8",  "R", "DAC_BCK"),
            ("11", "GPIO10", "R", "DAC_DIN"),
            ("12", "GPIO21", "R", "LED_DIN_RAW"),
            ("13", "GPIO9",  "R", "LED_PWR_EN"),
            ("14", "GPIO47", "R", "AMP_EN"),
            ("15", "3V3",    "T", "+3V3"),
            ("16", "5V",     "T", "+5V"),
            ("17", "GND",    "B", "GND"),
        ],
    },
    # Microphone MEMS (left of ESP32)
    {
        "ref": "U4", "value": "INMP441",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical",
        "x": 60, "y": 80, "w": 25, "h": 25,
        "pins": [
            ("1", "VDD", "R", "+3V3"),
            ("2", "GND", "R", "GND"),
            ("3", "L/R", "R", "GND"),
            ("4", "WS",  "R", "MIC_LRCLK"),
            ("5", "SCK", "R", "MIC_BCLK"),
            ("6", "SD",  "R", "MIC_DIN"),
        ],
    },
    # Encoder (left)
    {
        "ref": "SW1", "value": "Encodeur EC11",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical",
        "x": 60, "y": 130, "w": 25, "h": 22,
        "pins": [
            ("1", "A",     "R", "ENC_A"),
            ("2", "C",     "R", "GND"),
            ("3", "B",     "R", "ENC_B"),
            ("4", "BTN_A", "R", "BTN_CENTER"),
            ("5", "BTN_B", "R", "GND"),
        ],
    },
    # Mute switch (left)
    {
        "ref": "SW2", "value": "Switch mute SPDT",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
        "x": 60, "y": 160, "w": 25, "h": 15,
        "pins": [
            ("1", "COM", "R", "MUTE_SW"),
            ("2", "NO",  "R", "GND"),
        ],
    },
    # Jack 3.5mm (left)
    {
        "ref": "J1", "value": "Jack 3.5mm",
        "footprint": "Connector_Audio:Jack_3.5mm_PJ320E_Vertical",
        "x": 60, "y": 185, "w": 25, "h": 22,
        "pins": [
            ("T", "Tip",    "R", "AUDIO_L"),
            ("R", "Ring",   "R", "AUDIO_R"),
            ("S", "Sleeve", "R", "GND"),
            ("D", "Det",    "R", "JACK_DET"),
        ],
    },
    # PCM5102 DAC (right of ESP32)
    {
        "ref": "U2", "value": "PCM5102",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical",
        "x": 220, "y": 90, "w": 30, "h": 35,
        "pins": [
            ("1",  "VIN",  "L", "+3V3"),
            ("2",  "GND",  "L", "GND"),
            ("3",  "BCK",  "L", "DAC_BCK"),
            ("4",  "DIN",  "L", "DAC_DIN"),
            ("5",  "LRCK", "L", "DAC_LRCK"),
            ("6",  "SCK",  "R", "GND"),
            ("7",  "FMT",  "R", "GND"),
            ("8",  "FLT",  "R", "GND"),
            ("9",  "DEMP", "R", "GND"),
            ("10", "XSMT", "R", "+3V3"),
            ("11", "LOUT", "R", "AUDIO_L"),
            ("12", "ROUT", "R", "AUDIO_R"),
        ],
    },
    # PAM8403 (right)
    {
        "ref": "U3", "value": "PAM8403",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical",
        "x": 220, "y": 145, "w": 30, "h": 25,
        "pins": [
            ("1", "VCC",   "L", "+5V"),
            ("2", "GND",   "L", "GND"),
            ("3", "SHDN",  "L", "AMP_EN"),
            ("4", "LIN",   "L", "AUDIO_L"),
            ("5", "RIN",   "L", "AUDIO_R"),
            ("6", "LOUT+", "R", "SPK_L+"),
            ("7", "ROUT+", "R", "SPK_R+"),
        ],
    },
    # WS2812 ring (right)
    {
        "ref": "DS1", "value": "WS2812 Ring x12",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
        "x": 280, "y": 90, "w": 25, "h": 15,
        "pins": [
            ("1", "VCC", "L", "+5V_LED"),
            ("2", "GND", "L", "GND"),
            ("3", "DIN", "L", "LED_DIN"),
        ],
    },
    # R2 (LED series)
    {
        "ref": "R2", "value": "330R",
        "footprint": "Resistor_SMD:R_0603_1608Metric",
        "x": 250, "y": 105, "w": 12, "h": 8,
        "pins": [
            ("1", "1", "L", "LED_DIN_RAW"),
            ("2", "2", "R", "LED_DIN"),
        ],
    },
    # Q1 P-MOS (LED gate)
    {
        "ref": "Q1", "value": "AO3401 P-MOS",
        "footprint": "Package_TO_SOT_SMD:SOT-23",
        "x": 280, "y": 130, "w": 22, "h": 18,
        "pins": [
            ("G", "G", "L", "LED_PWR_EN"),
            ("S", "S", "T", "+5V"),
            ("D", "D", "R", "+5V_LED"),
        ],
    },
    # Speakers
    {
        "ref": "HP_L", "value": "HP gauche 40mm 4R 3W",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        "x": 280, "y": 155, "w": 25, "h": 10,
        "pins": [("1", "+", "L", "SPK_L+"), ("2", "-", "L", "GND")],
    },
    {
        "ref": "HP_R", "value": "HP droit 40mm 4R 3W",
        "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        "x": 280, "y": 175, "w": 25, "h": 10,
        "pins": [("1", "+", "L", "SPK_R+"), ("2", "-", "L", "GND")],
    },
    # USB-C
    {
        "ref": "J2", "value": "USB-C",
        "footprint": "Connector_USB:USB_C_Receptacle_USB2.0_16P",
        "x": 100, "y": 35, "w": 25, "h": 15,
        "pins": [
            ("1", "VBUS", "R", "+5V"),
            ("2", "GND",  "R", "GND"),
        ],
    },
    # LDO 3V3
    {
        "ref": "U5", "value": "AMS1117-3.3",
        "footprint": "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
        "x": 170, "y": 35, "w": 25, "h": 15,
        "pins": [
            ("3", "VIN",  "L", "+5V"),
            ("2", "VOUT", "R", "+3V3"),
            ("1", "GND",  "B", "GND"),
        ],
    },
]

# ============================================================================
# Pin absolute coordinate calculation
# ============================================================================
# In KiCad, a pin's connection point (where wires attach) is at the END of the pin
# (the side facing outward from the component body).

PIN_LEN = 2.54  # length of pin stub

def compute_pin_positions(comp):
    """For each pin, return (pin_num, name, side, net, abs_x, abs_y)."""
    cx, cy = comp["x"], comp["y"]
    w, h = comp["w"], comp["h"]
    sides = {"L": [], "R": [], "T": [], "B": []}
    for p in comp["pins"]:
        sides[p[2]].append(p)
    out = []
    for side, plist in sides.items():
        n = len(plist)
        for i, (num, name, _, net) in enumerate(plist):
            if side == "L":
                # Pin emerges from left side
                px = cx - w/2 - PIN_LEN
                py = cy - h/2 + GRID + i*GRID
                py = snap(py)
            elif side == "R":
                px = cx + w/2 + PIN_LEN
                py = cy - h/2 + GRID + i*GRID
                py = snap(py)
            elif side == "T":
                py = cy - h/2 - PIN_LEN
                px = cx - w/2 + GRID + i*GRID
                px = snap(px)
            else:  # B
                py = cy + h/2 + PIN_LEN
                px = cx - w/2 + GRID + i*GRID
                px = snap(px)
            out.append((num, name, side, net, snap(px), py))
    return out

# Build global pin index
ALL_PINS = {}  # (ref, num) -> (x, y, side, net, name)
PIN_BY_NET = {}  # net -> list of (ref, num, x, y, side, name)

for comp in COMPONENTS:
    for num, name, side, net, px, py in compute_pin_positions(comp):
        ALL_PINS[(comp["ref"], num)] = (px, py, side, net, name)
        PIN_BY_NET.setdefault(net, []).append((comp["ref"], num, px, py, side, name))

# ============================================================================
# Library symbols - generic rectangle with pins
# ============================================================================
SCH_UUID = U()

def render_lib_symbol(comp):
    ref = comp["ref"]
    val = comp["value"]
    w, h = comp["w"], comp["h"]
    body = (
        f'\n      (symbol "{ref}_0_1"\n'
        f'        (rectangle (start {-w/2} {-h/2}) (end {w/2} {h/2})\n'
        f'          (stroke (width 0.254) (type default))\n'
        f'          (fill (type background))\n'
        f'        )\n'
        f'      )'
    )
    sides = {"L": [], "R": [], "T": [], "B": []}
    for p in comp["pins"]:
        sides[p[2]].append(p)
    pin_xml_parts = []
    for side, plist in sides.items():
        n = len(plist)
        for i, (num, name, _, net) in enumerate(plist):
            if side == "L":
                rel_x = -w/2 - PIN_LEN
                rel_y = -h/2 + GRID + i*GRID
                orient = 0
            elif side == "R":
                rel_x = w/2 + PIN_LEN
                rel_y = -h/2 + GRID + i*GRID
                orient = 180
            elif side == "T":
                rel_y = -h/2 - PIN_LEN
                rel_x = -w/2 + GRID + i*GRID
                orient = 270
            else:
                rel_y = h/2 + PIN_LEN
                rel_x = -w/2 + GRID + i*GRID
                orient = 90
            pin_xml_parts.append(
                f'\n        (pin bidirectional line\n'
                f'          (at {rel_x} {-rel_y} {orient})\n'
                f'          (length {PIN_LEN})\n'
                f'          (name "{name}" (effects (font (size 1.0 1.0))))\n'
                f'          (number "{num}" (effects (font (size 1.0 1.0))))\n'
                f'        )'
            )
    body_pins = (
        f'\n      (symbol "{ref}_1_1"' + "".join(pin_xml_parts) + '\n      )'
    )
    return (
        f'\n    (symbol "Local:{ref}"\n'
        f'      (pin_names (offset 0.508))\n'
        f'      (in_bom yes) (on_board yes)\n'
        f'      (property "Reference" "{ref}" (at 0 {h/2+3} 0)\n'
        f'        (effects (font (size 1.2 1.2)) (justify left bottom)))\n'
        f'      (property "Value" "{val}" (at 0 {-h/2-3} 0)\n'
        f'        (effects (font (size 1.0 1.0)) (justify left top)))\n'
        f'      (property "Footprint" "{comp["footprint"]}" (at 0 0 0)\n'
        f'        (effects (font (size 1.27 1.27)) hide))\n'
        f'      (property "Datasheet" "" (at 0 0 0)\n'
        f'        (effects (font (size 1.27 1.27)) hide)){body}{body_pins}\n'
        f'    )'
    )

def render_symbol_instance(comp):
    ref = comp["ref"]
    val = comp["value"]
    x, y = comp["x"], comp["y"]
    h = comp["h"]
    uid = U()
    return (
        f'\n  (symbol\n'
        f'    (lib_id "Local:{ref}")\n'
        f'    (at {x} {y} 0) (unit 1)\n'
        f'    (in_bom yes) (on_board yes) (dnp no)\n'
        f'    (uuid "{uid}")\n'
        f'    (property "Reference" "{ref}" (at {x} {y-h/2-4} 0)\n'
        f'      (effects (font (size 1.27 1.27)) (justify left)))\n'
        f'    (property "Value" "{val}" (at {x} {y+h/2+4} 0)\n'
        f'      (effects (font (size 1.0 1.0)) (justify left)))\n'
        f'    (property "Footprint" "{comp["footprint"]}" (at 0 0 0)\n'
        f'      (effects (font (size 1.27 1.27)) hide))\n'
        f'    (property "Datasheet" "" (at 0 0 0)\n'
        f'      (effects (font (size 1.27 1.27)) hide))\n'
        f'    (instances\n'
        f'      (project "s3-salle-de-bain"\n'
        f'        (path "/{SCH_UUID}" (reference "{ref}") (unit 1))\n'
        f'      )\n'
        f'    )\n'
        f'  )'
    )

# ============================================================================
# WIRE GENERATION - the key part
# ============================================================================
# For each net, draw real wires between pins. Strategy:
#   - Power rails (GND, +3V3, +5V, +5V_LED): horizontal trunk at a fixed Y,
#     each pin connects to trunk via a short vertical wire (+ junction)
#   - 2-pin nets: direct manhattan L-shape (3 segments)
#   - N-pin signal nets (rare here): chain them in order

def mk_wire(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return ""
    return (
        f'\n  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))\n'
        f'    (stroke (width 0) (type default))\n'
        f'    (uuid "{U()}")\n'
        f'  )'
    )

def mk_junction(x, y):
    return (
        f'\n  (junction (at {x} {y}) (diameter 0)\n'
        f'    (color 0 0 0 0)\n'
        f'    (uuid "{U()}")\n'
        f'  )'
    )

def mk_glabel(net, x, y, orient=0):
    return (
        f'\n  (global_label "{net}" (shape input)\n'
        f'    (at {x} {y} {orient})\n'
        f'    (effects (font (size 1.27 1.27)) (justify left))\n'
        f'    (uuid "{U()}")\n'
        f'  )'
    )

def route_net(net, pins):
    """Generate wires for a net. pins = list of (ref, num, x, y, side, name)."""
    out_wires = []
    out_juncs = []
    n = len(pins)
    if n < 1:
        return ""

    # Power nets - horizontal trunk
    if net in ("GND", "+3V3", "+5V", "+5V_LED"):
        xs = [p[2] for p in pins]
        ys = [p[3] for p in pins]
        # Choose trunk y
        if net == "GND":
            trunk_y = snap(max(ys) + 5)
        elif net == "+3V3":
            trunk_y = snap(min(ys) - 8)
        elif net == "+5V":
            trunk_y = snap(min(ys) - 16)
        else:  # +5V_LED
            trunk_y = snap(min(ys) - 5)
        # Horizontal trunk
        xmin, xmax = min(xs), max(xs)
        out_wires.append(mk_wire(xmin, trunk_y, xmax, trunk_y))
        # Vertical taps from each pin to trunk
        for (_ref, _num, px, py, _side, _name) in pins:
            out_wires.append(mk_wire(px, py, px, trunk_y))
            out_juncs.append(mk_junction(px, trunk_y))
        # Net label at one end of trunk
        out_wires.append(mk_glabel(net, xmax + 2, trunk_y, 0))
        return "".join(out_wires + out_juncs)

    # 2-pin nets: direct route
    if n == 2:
        (r1, n1, x1, y1, s1, _) = pins[0]
        (r2, n2, x2, y2, s2, _) = pins[1]
        # Choose intermediate point based on sides
        if y1 == y2:
            out_wires.append(mk_wire(x1, y1, x2, y2))
        else:
            mid_x = snap((x1 + x2) / 2)
            out_wires.append(mk_wire(x1, y1, mid_x, y1))
            out_wires.append(mk_wire(mid_x, y1, mid_x, y2))
            out_wires.append(mk_wire(mid_x, y2, x2, y2))
        # net label at midpoint
        midx = snap((x1+x2)/2)
        midy = snap((y1+y2)/2)
        out_wires.append(mk_glabel(net, midx, midy, 0))
        return "".join(out_wires)

    # N-pin signal nets: chain
    sorted_pins = sorted(pins, key=lambda p: (p[2], p[3]))
    for i in range(len(sorted_pins) - 1):
        (r1, n1, x1, y1, s1, _) = sorted_pins[i]
        (r2, n2, x2, y2, s2, _) = sorted_pins[i+1]
        mid_x = snap((x1 + x2) / 2)
        out_wires.append(mk_wire(x1, y1, mid_x, y1))
        out_wires.append(mk_wire(mid_x, y1, mid_x, y2))
        out_wires.append(mk_wire(mid_x, y2, x2, y2))
    return "".join(out_wires)

# Generate all wiring
wires_block = ""
for net, pins in PIN_BY_NET.items():
    if net.startswith("NC"):
        continue
    wires_block += route_net(net, pins)

# ============================================================================
# Schematic header / footer
# ============================================================================
lib_symbols = "".join(render_lib_symbol(c) for c in COMPONENTS)
sym_instances = "".join(render_symbol_instance(c) for c in COMPONENTS)

sch_content = f'''(kicad_sch
  (version 20231120)
  (generator "build_kicad_py")
  (generator_version "8.0")
  (uuid "{SCH_UUID}")
  (paper "A2")
  (title_block
    (title "S3 Salle de Bain - Voice Assistant ESP32-S3")
    (date "2026-06-11")
    (rev "v3")
    (company "domokami / Hanafi BENMESBAH")
    (comment 1 "Schema cable depuis s3-salle-de-bain.yaml")
    (comment 2 "Power rails : +3V3 (LDO AMS1117), +5V (USB-C), +5V_LED (gated GPIO9)")
    (comment 3 "27 nets - 14 composants principaux")
    (comment 4 "https://github.com/hanafi09/s3-salle-de-bain")
  )
  (lib_symbols{lib_symbols}
  ){sym_instances}{wires_block}
  (sheet_instances
    (path "/" (page "1"))
  )
)
'''

(OUT / "s3-salle-de-bain.kicad_sch").write_text(sch_content, encoding='utf-8')
print(f"OK .kicad_sch ({len(sch_content)} bytes)")

# ============================================================================
# Project file (.kicad_pro)
# ============================================================================
pro = {
    "board": {"design_settings": {"defaults": {}, "rules": {}}, "layer_presets": [], "viewports": []},
    "boards": [],
    "cvpcb": {"equivalence_files": []},
    "erc": {"erc_exclusions": [], "meta": {"version": 0}, "rule_severities": {}},
    "libraries": {"pinned_footprint_libs": [], "pinned_symbol_libs": []},
    "meta": {"filename": "s3-salle-de-bain.kicad_pro", "version": 1},
    "net_settings": {
        "classes": [{"bus_width": 12, "clearance": 0.2, "diff_pair_gap": 0.25,
                     "diff_pair_via_gap": 0.25, "diff_pair_width": 0.2,
                     "line_style": 0, "microvia_diameter": 0.3, "microvia_drill": 0.1,
                     "name": "Default", "pcb_color": "rgba(0, 0, 0, 0.000)",
                     "schematic_color": "rgba(0, 0, 0, 0.000)",
                     "track_width": 0.25, "via_diameter": 0.8, "via_drill": 0.4,
                     "wire_width": 6}],
        "meta": {"version": 3}, "net_colors": None, "netclass_assignments": None, "netclass_patterns": []
    },
    "pcbnew": {"last_paths": {"gencad": "", "idf": "", "netlist": "", "plot": "",
                              "pos_files": "", "specctra_dsn": "", "step": "", "svg": "", "vrml": ""},
               "page_layout_descr_file": ""},
    "schematic": {"annotate_start_num": 0, "drawing": {},
                  "legacy_lib_dir": "", "legacy_lib_list": [],
                  "meta": {"version": 1}, "net_format_name": "",
                  "page_layout_descr_file": "", "plot_directory": "",
                  "spice_current_sheet_as_root": False, "spice_external_command": "spice \"%I\"",
                  "spice_model_current_sheet_as_root": True, "spice_save_all_currents": False,
                  "spice_save_all_voltages": False, "subpart_first_id": 65, "subpart_id_separator": 0},
    "sheets": [["00000000-0000-0000-0000-000000000000", "Root"]],
    "text_variables": {}
}
(OUT / "s3-salle-de-bain.kicad_pro").write_text(json.dumps(pro, indent=2), encoding='utf-8')
print("OK .kicad_pro")

# PCB minimal (board outline only)
PCB_UUID = U()
W_BOARD, H_BOARD = 100, 80
pcb = f'''(kicad_pcb
  (version 20240108)
  (generator "build_kicad_py")
  (generator_version "8.0")
  (general (thickness 1.6))
  (paper "A4")
  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (44 "Edge.Cuts" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
  )
  (setup (pad_to_mask_clearance 0))
  (net 0 "")
  (gr_rect (start 0 0) (end {W_BOARD} {H_BOARD})
    (stroke (width 0.15) (type default))
    (fill none)
    (layer "Edge.Cuts")
    (uuid "{U()}")
  )
)
'''
(OUT / "s3-salle-de-bain.kicad_pcb").write_text(pcb, encoding='utf-8')
print("OK .kicad_pcb")

# Empty lib tables
(OUT / "sym-lib-table").write_text("(sym_lib_table\n)\n", encoding='utf-8')
(OUT / "fp-lib-table").write_text("(fp_lib_table\n)\n", encoding='utf-8')

# Count
n_wires = wires_block.count("(wire ")
n_junctions = wires_block.count("(junction ")
n_labels = wires_block.count("(global_label ")
print(f"\n=== STATS ===")
print(f"Composants : {len(COMPONENTS)}")
print(f"Nets : {len(PIN_BY_NET)}")
print(f"Fils tires : {n_wires}")
print(f"Jonctions : {n_junctions}")
print(f"Etiquettes net : {n_labels}")
