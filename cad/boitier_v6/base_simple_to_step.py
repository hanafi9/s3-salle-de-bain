# -*- coding: utf-8 -*-
# Bac SIMPLIFIE (grilles circulaires, fn bas) -> v6_base.step :
# solide B-rep VALIDE et leger. Le maillage est d'abord nettoye de ses
# auto-intersections (dues aux recouvrements volontaires d'impression).
# Run via freecadcmd.
import os, FreeCAD, Part, Mesh
HERE = os.path.dirname(os.path.abspath(__file__))
stl  = os.path.join(HERE, "v6_base_step.stl")
step = os.path.join(HERE, "v6_base.step")

m = Mesh.Mesh(stl)
m.removeDuplicatedPoints(); m.removeDuplicatedFacets()
print("mesh : self-int=%s tri=%d" % (m.hasSelfIntersections(), m.CountFacets))

doc = FreeCAD.newDocument("base")
best = None
for tol in (1e-5, 1e-4, 1e-3):
    sh = Part.Shape(); sh.makeShapeFromMesh(m.Topology, tol, False)
    try: sh.sewShape(tol)
    except Exception: pass
    sol = Part.makeSolid(sh)
    try: sol.fix(tol, tol, tol)
    except Exception: pass
    try:
        mg = sol.removeSplitter()
        if mg.Solids: sol = mg
    except Exception: pass
    try: sol.fix(tol, tol, tol)
    except Exception: pass
    print("tol=%g valid=%s closed=%s vol=%.0f faces=%d"
          % (tol, sol.isValid(), sol.isClosed(), sol.Volume, len(sol.Faces)))
    if sol.isValid() and sol.isClosed() and 40000 < sol.Volume < 120000:
        best = sol; break
    if best is None and sol.isClosed():
        best = sol

feat = doc.addObject("Part::Feature", "v6_base"); feat.Shape = best
doc.recompute(); Part.export([feat], step)
print("STEP -> v6_base.step  valid=%s closed=%s faces=%d  (%d Ko)"
      % (best.isValid(), best.isClosed(), len(best.Faces), os.path.getsize(step)//1024))
