# -*- coding: utf-8 -*-
"""
Trouve 4 emplacements de trous de fixation M3 (un par quadrant) sur le PCB
existant, sans collision avec les empreintes. Sortie en coordonnees PCB (mm)
et en coordonnees boitier (centrees, Y inverse).

Run: "C:\\Program Files\\KiCad\\10.0\\bin\\python.exe" find_mount_points.py
"""
import os, pcbnew

HERE = os.path.dirname(os.path.abspath(__file__))
PCB  = os.path.join(HERE, "s3-salle-de-bain.kicad_pcb")
BW, BH = 145.0, 108.0
EDGE_MARGIN = 7.0      # garde au bord (mm)
CLEAR_R     = 4.0      # rayon de garde autour du trou (mm) -> tete M3 + rondelle
STEP        = 1.0

board = pcbnew.LoadBoard(PCB)
boxes = []
for fp in board.GetFootprints():
    bb = fp.GetBoundingBox(True, False)  # include text? no
    x1 = pcbnew.ToMM(bb.GetLeft());  y1 = pcbnew.ToMM(bb.GetTop())
    x2 = pcbnew.ToMM(bb.GetRight()); y2 = pcbnew.ToMM(bb.GetBottom())
    boxes.append((x1, y1, x2, y2, fp.GetReference()))

def clear(px, py):
    # le disque (px,py,CLEAR_R) ne doit toucher aucune bbox (dilatee de CLEAR_R)
    for (x1, y1, x2, y2, ref) in boxes:
        if (px > x1 - CLEAR_R and px < x2 + CLEAR_R and
            py > y1 - CLEAR_R and py < y2 + CLEAR_R):
            return False
    return True

# 4 coins de reference
corners = {
    "BL": (EDGE_MARGIN, EDGE_MARGIN),
    "BR": (BW - EDGE_MARGIN, EDGE_MARGIN),
    "TL": (EDGE_MARGIN, BH - EDGE_MARGIN),
    "TR": (BW - EDGE_MARGIN, BH - EDGE_MARGIN),
}

chosen = {}
import math
for name, (cx, cy) in corners.items():
    best = None; bestd = 1e9
    y = EDGE_MARGIN
    while y <= BH - EDGE_MARGIN:
        x = EDGE_MARGIN
        while x <= BW - EDGE_MARGIN:
            # rester dans le quadrant du coin
            in_quad = ((x < BW/2) == (cx < BW/2)) and ((y < BH/2) == (cy < BH/2))
            if in_quad and clear(x, y):
                d = (x-cx)**2 + (y-cy)**2     # le plus proche du coin
                if d < bestd:
                    bestd = d; best = (round(x,1), round(y,1))
            x += STEP
        y += STEP
    chosen[name] = best

print("=== Trous de fixation M3 trouves (coords PCB mm) ===")
order = ["BL","BR","TR","TL"]
pcb_pts = []
for n in order:
    p = chosen[n]
    pcb_pts.append(p)
    print(f"  {n}: {p}")

print("\n=== Coords boitier (centrees, X = px-72.5, Y = -(py-54)) ===")
for n in order:
    p = chosen[n]
    if p:
        ex = round(p[0]-72.5, 1); ey = round(-(p[1]-54.0), 1)
        print(f"  {n}: [{ex}, {ey}]")
