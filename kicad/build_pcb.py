# -*- coding: utf-8 -*-
"""
Build a real KiCad PCB using the pcbnew API (run with KiCad's bundled python).

Each component gets its REAL footprint loaded from the installed KiCad
footprint libraries, placed on the board, with nets assigned to pads.

Run:
  "C:\\Program Files\\KiCad\\10.0\\bin\\python.exe" build_pcb.py
"""
import os
import pcbnew

FPBASE = r"C:\Program Files\KiCad\10.0\share\kicad\footprints"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s3-salle-de-bain.kicad_pcb")

def MM(v): return pcbnew.FromMM(v)
def VEC(x, y): return pcbnew.VECTOR2I(MM(x), MM(y))

# (ref, lib, footprint, x, y, rot_deg, value, {pad_number: net_name})
# Modules are represented as pin headers (they plug into female headers).
# Discrete ICs/parts use their real SMD/THT packages.
COMPONENTS = [
    # --- ESP32-S3 DevKitC-1 : official Espressif footprint, real pinout ---
    # Pad numbers map to GPIOs per the Espressif silk:
    #   pad1=3V3, pad4=GPIO4, pad5=GPIO5, pad7=GPIO7, pad9=GPIO16, pad10=GPIO17,
    #   pad11=GPIO18, pad12=GPIO8, pad15=GPIO9, pad16=GPIO10, pad17=GPIO11,
    #   pad21=5V, pad22/23/24/44=GND, pad27=GPIO21, pad28=GPIO47,
    #   pad40=GPIO2, pad41=GPIO1
    ("U1", "Espressif", "ESP32-S3-DevKitC",
     12, 18, 0, "ESP32-S3-DevKitC-1", {
        "1":"+3V3",        # 3V3
        "4":"MIC_LRCLK",   # GPIO4
        "5":"MIC_BCLK",    # GPIO5
        "7":"DAC_LRCK",    # GPIO7
        "9":"ENC_A",       # GPIO16
        "10":"JACK_DET",   # GPIO17
        "11":"ENC_B",      # GPIO18
        "12":"DAC_BCK",    # GPIO8
        "15":"LED_PWR_EN", # GPIO9
        "16":"DAC_DIN",    # GPIO10
        "17":"MIC_DIN",    # GPIO11
        "21":"+5V",        # 5V
        "22":"GND",        # GND
        "27":"LED_DIN_RAW",# GPIO21
        "28":"AMP_EN",     # GPIO47
        "40":"MUTE_SW",    # GPIO2
        "41":"BTN_CENTER", # GPIO1
        "44":"GND",        # GND
     }),
    # --- PCM5102 DAC breakout : 2x06 header ---
    ("U2", "Connector_PinHeader_2.54mm", "PinHeader_2x06_P2.54mm_Vertical",
     72, 38, 0, "PCM5102", {
        "1":"+3V3","2":"GND","3":"DAC_BCK","4":"DAC_DIN","5":"DAC_LRCK","6":"GND",
        "7":"GND","8":"GND","9":"GND","10":"+3V3","11":"AUDIO_L","12":"AUDIO_R",
     }),
    # --- PAM8403 amp module : 1x07 header ---
    ("U3", "Connector_PinHeader_2.54mm", "PinHeader_1x07_P2.54mm_Vertical",
     72, 66, 0, "PAM8403", {
        "1":"+5V","2":"GND","3":"AMP_EN","4":"AUDIO_L","5":"AUDIO_R",
        "6":"SPK_L","7":"SPK_R",
     }),
    # --- INMP441 MEMS mic : 1x06 header ---
    ("U4", "Connector_PinHeader_2.54mm", "PinHeader_1x06_P2.54mm_Vertical",
     48, 35, 0, "INMP441", {
        "1":"+3V3","2":"GND","3":"GND","4":"MIC_LRCLK","5":"MIC_BCLK","6":"MIC_DIN",
     }),
    # --- AMS1117-3.3 LDO : SOT-223 (pin2 = tab = VOUT) ---
    ("U5", "Package_TO_SOT_SMD", "SOT-223-3_TabPin2",
     107, 13, 0, "AMS1117-3.3", {
        "1":"GND","2":"+3V3","3":"+5V",
     }),
    # --- WS2812 ring connector : 1x03 ---
    ("DS1", "Connector_PinHeader_2.54mm", "PinHeader_1x03_P2.54mm_Vertical",
     114, 35, 0, "WS2812-Ring", {
        "1":"+5V_LED","2":"GND","3":"LED_DIN",
     }),
    # --- Rotary encoder EC11 with switch ---
    ("SW1", "Rotary_Encoder", "RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm",
     52, 85, 0, "EC11", {
        "A":"ENC_A","B":"ENC_B","C":"GND","S1":"BTN_CENTER","S2":"GND","MP":"GND",
     }),
    # --- Mute slide switch SPDT ---
    ("SW2", "Button_Switch_THT", "SW_DIP_SPSTx01_Slide_9.78x4.72mm_W7.62mm_P2.54mm",
     75, 92, 0, "Mute-SPDT", {
        "1":"MUTE_SW","2":"GND",
     }),
    # --- Jack 3.5mm with switch detect (PJ-320E) ---
    ("J1", "Connector_Audio", "Jack_3.5mm_PJ320E_Horizontal",
     98, 90, 0, "Jack-3.5mm", {
        "T":"AUDIO_L","R1":"AUDIO_R","R2":"JACK_DET","S":"GND",
     }),
    # --- USB-C receptacle (power only) ---
    ("J2", "Connector_USB", "USB_C_Receptacle_Amphenol_12401610E4-2A",
     55, 13, 0, "USB-C", {
        # VBUS pads -> +5V ; GND + shield -> GND
        "A4":"+5V","B4":"+5V","A9":"+5V","B9":"+5V",
        "A1":"GND","A12":"GND","B1":"GND","B12":"GND","SH":"GND",
     }),
    # --- Discrete passives ---
    ("R1", "Resistor_SMD", "R_0603_1608Metric", 50, 52, 0, "10k",
        {"1":"BTN_CENTER","2":"+3V3"}),
    ("R2", "Resistor_SMD", "R_0603_1608Metric", 100, 33, 0, "330",
        {"1":"LED_DIN_RAW","2":"LED_DIN"}),
    ("C1", "Capacitor_SMD", "C_0603_1608Metric", 80, 12, 0, "10uF",
        {"1":"+5V","2":"GND"}),
    ("C2", "Capacitor_SMD", "C_0603_1608Metric", 85, 12, 0, "100nF",
        {"1":"+5V","2":"GND"}),
    ("C3", "Capacitor_SMD", "C_0603_1608Metric", 90, 12, 0, "10uF",
        {"1":"+3V3","2":"GND"}),
    ("C4", "Capacitor_SMD", "C_0603_1608Metric", 95, 12, 0, "10uF",
        {"1":"+3V3","2":"GND"}),
    ("C5", "Capacitor_SMD", "CP_Elec_5x5.3", 112, 90, 0, "100uF",
        {"1":"+5V","2":"GND"}),
    ("C6", "Capacitor_SMD", "CP_Elec_5x5.3", 130, 13, 0, "470uF",
        {"1":"+5V_LED","2":"GND"}),
    # --- P-MOSFET AO3401 SOT-23 (1=Gate 2=Source 3=Drain) ---
    ("Q1", "Package_TO_SOT_SMD", "SOT-23", 114, 54, 0, "AO3401",
        {"1":"LED_PWR_EN","2":"+5V","3":"+5V_LED"}),
    # --- Ferrite bead ---
    ("F1", "Inductor_SMD", "L_0805_2012Metric", 120, 13, 0, "Ferrite 600R",
        {"1":"+5V","2":"+5V_LED"}),
    # --- Speaker connectors ---
    ("HP1", "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical",
     124, 66, 0, "HP-Left", {"1":"SPK_L","2":"GND"}),
    ("HP2", "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical",
     124, 80, 0, "HP-Right", {"1":"SPK_R","2":"GND"}),
]

BOARD_W, BOARD_H = 135, 100

def main():
    board = pcbnew.BOARD()

    # Relax copper-to-edge clearance to 0.25mm (USB-C is an edge connector
    # whose shield/pads legitimately sit close to the board outline).
    ds = board.GetDesignSettings()
    try:
        ds.m_CopperEdgeClearance = MM(0.25)
    except Exception:
        pass

    # --- Create nets ---
    net_names = set()
    for *_, padmap in [(c[0],c[-1]) for c in COMPONENTS]:
        for n in padmap.values():
            net_names.add(n)
    nets = {}
    for name in sorted(net_names):
        ni = pcbnew.NETINFO_ITEM(board, name)
        board.Add(ni)
        nets[name] = ni

    placed = 0
    pad_assigned = 0
    LOCAL = os.path.dirname(os.path.abspath(__file__))
    for ref, lib, fpname, x, y, rot, value, padmap in COMPONENTS:
        if lib == "Espressif":
            libpath = os.path.join(LOCAL, "Espressif.pretty")
        else:
            libpath = os.path.join(FPBASE, lib + ".pretty")
        fp = pcbnew.FootprintLoad(libpath, fpname)
        if fp is None:
            print(f"  !! footprint not found: {lib}:{fpname} for {ref}")
            continue
        fp.SetReference(ref)
        fp.SetValue(value)
        fp.SetPosition(VEC(x, y))
        if rot:
            fp.SetOrientationDegrees(rot)
        # assign nets to pads
        for pad in fp.Pads():
            pn = pad.GetNumber()
            if pn in padmap:
                pad.SetNet(nets[padmap[pn]])
                pad_assigned += 1
        board.Add(fp)
        placed += 1

    # --- Board outline on Edge.Cuts ---
    for (x1,y1,x2,y2) in [(0,0,BOARD_W,0),(BOARD_W,0,BOARD_W,BOARD_H),
                          (BOARD_W,BOARD_H,0,BOARD_H),(0,BOARD_H,0,0)]:
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(VEC(x1,y1)); seg.SetEnd(VEC(x2,y2))
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(MM(0.15))
        board.Add(seg)

    # --- Title text ---
    txt = pcbnew.PCB_TEXT(board)
    txt.SetText("S3 Salle de Bain v3 - domokami/hanafi09")
    txt.SetPosition(VEC(BOARD_W/2, BOARD_H+5))
    txt.SetLayer(pcbnew.F_SilkS)
    board.Add(txt)

    board.Save(OUT)
    print(f"OK PCB saved : {OUT}")
    print(f"  Footprints placed : {placed}/{len(COMPONENTS)}")
    print(f"  Pads assigned to nets : {pad_assigned}")
    print(f"  Nets : {len(nets)}")

if __name__ == "__main__":
    main()
