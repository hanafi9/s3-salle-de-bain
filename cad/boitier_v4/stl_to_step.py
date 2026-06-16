# -*- coding: utf-8 -*-
# Conversion STL (maillage OpenSCAD) -> STEP (solide B-rep facette), via FreeCAD 1.1.
# OpenSCAD n'exporte pas le STEP (geometrie maillee, pas de B-rep) : on reconstruit
# un solide a partir du maillage. Tolerance de couture FINE (1e-5) pour ne pas
# fusionner les fines parois des grilles hexagonales.
#
# Run:  & "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" stl_to_step.py
import os, FreeCAD, Part, Mesh

HERE  = os.path.dirname(os.path.abspath(__file__))
# (nom, volume matiere attendu min, max) -- garde-fou anti solide malforme
PARTS = [("v4_base", 50000, 200000),
         ("v4_top",  80000, 300000),
         ("v4_speaker_gasket", 500, 6000)]

def to_solid(m, tol):
    sh = Part.Shape()
    sh.makeShapeFromMesh(m.Topology, tol, False)
    try: sh.sewShape(tol)
    except Exception: pass
    sol = Part.makeSolid(sh)
    try: sol.fix(tol, tol, tol)
    except Exception: pass
    return sol

for name, vmin, vmax in PARTS:
    stl  = os.path.join(HERE, name + ".stl")
    step = os.path.join(HERE, name + ".step")
    if not os.path.exists(stl):
        print("SKIP (stl absent):", name); continue
    m = Mesh.Mesh(stl)
    doc = FreeCAD.newDocument(name)
    chosen = None
    for tol in (1e-5, 1e-4, 1e-3):
        try: sol = to_solid(m, tol)
        except Exception: continue
        if sol.isValid() and sol.isClosed() and vmin < sol.Volume < vmax:
            chosen = (sol, tol); break
    if chosen is None:                     # repli : exporte la meilleure tentative
        sol = to_solid(m, 1e-5); chosen = (sol, 1e-5)
    sol, tol = chosen
    feat = doc.addObject("Part::Feature", name); feat.Shape = sol
    doc.recompute(); Part.export([feat], step)
    print("%-20s valid=%s closed=%s vol=%.0f mm3 faces=%d tol=%g -> %d Ko"
          % (name, sol.isValid(), sol.isClosed(), sol.Volume, len(sol.Faces),
             tol, os.path.getsize(step)//1024))
    FreeCAD.closeDocument(doc.Name)
print("DONE")
