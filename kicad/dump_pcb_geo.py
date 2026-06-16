# -*- coding: utf-8 -*-
# Extrait la geometrie utile du PCB ACTUEL (modifie a la main) pour recaler le boitier.
# Run: "C:\Program Files\KiCad\10.0\bin\python.exe" dump_pcb_geo.py
import os, pcbnew
HERE = os.path.dirname(os.path.abspath(__file__))
b = pcbnew.LoadBoard(os.path.join(HERE, "s3-salle-de-bain.kicad_pcb"))
MM = pcbnew.ToMM

# --- contour (Edge.Cuts) ---
xs, ys = [], []
for d in b.GetDrawings():
    if d.GetLayer() == pcbnew.Edge_Cuts:
        bb = d.GetBoundingBox()
        xs += [MM(bb.GetLeft()), MM(bb.GetRight())]
        ys += [MM(bb.GetTop()),  MM(bb.GetBottom())]
if xs:
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    print("CONTOUR  x:[%.2f..%.2f]  y:[%.2f..%.2f]  =>  %.2f x %.2f mm  origine(%.2f,%.2f)"
          % (x0, x1, y0, y1, x1-x0, y1-y0, x0, y0))
else:
    x0 = y0 = 0; x1 = y1 = 0; print("CONTOUR: aucune Edge.Cuts trouvee")

cx, cy = (x0+x1)/2.0, (y0+y1)/2.0
print("CENTRE PCB (mm): (%.2f, %.2f)\n" % (cx, cy))

print("=== EMPREINTES (ref : pos x,y  rot  | centre-boitier X=px-cx, Y=py-cy) ===")
rows = []
for fp in b.GetFootprints():
    ref = fp.GetReference()
    p = fp.GetPosition()
    px, py = MM(p.x), MM(p.y)
    rows.append((ref, px, py, fp.GetOrientationDegrees(),
                 fp.GetValue(), fp.GetFPIDAsString()))
for ref, px, py, rot, val, fpid in sorted(rows):
    star = "  <<<" if ref.upper().startswith(("MK","J2","SW1","HP","U4","DS1")) else ""
    print("  %-6s %8.2f %8.2f  r%-5.0f  [%.2f, %.2f]  %-14s %s%s"
          % (ref, px, py, rot, px-cx, py-cy, val, fpid, star))

# --- trous de montage explicitement (refs MK* ou empreintes MountingHole) ---
print("\n=== TROUS DE FIXATION (MK* ou MountingHole) ===")
for ref, px, py, rot, val, fpid in sorted(rows):
    if ref.upper().startswith("MK") or "MountingHole" in fpid:
        print("  %-6s  PCB(%.2f, %.2f)  ->  boitier [%.2f, %.2f]"
              % (ref, px, py, px-cx, py-cy))
