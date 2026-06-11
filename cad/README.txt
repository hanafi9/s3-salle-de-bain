S3 Salle de Bain - Voice Assistant Enclosure
Par Hanafi BENMESBAH / domokami
=============================================

Ce dossier contient les fichiers CAO du boitier 3D imprimable en ABS.

--- CONTENU ---

Sources parametriques (OpenSCAD) - a privilegier :
  housing_top.scad       Capot superieur avec aperture LED et bouton
  housing_body.scad      Corps cylindrique avec grilles stereo
  housing_bottom.scad    Fond avec USB-C, events, inserts M3
  speaker_baffle.scad    Plaque support haut-parleurs inclines
  diffuser_ring.scad     Anneau diffuseur PETG pour LEDs WS2812

STL simplifies (apercu / prototypage) :
  *.stl                  Meshes de volumes externes uniquement

--- RECOMPILER LES STL DEPUIS LES SOURCES ---

Installez OpenSCAD : https://openscad.org
Puis pour chaque piece :

  openscad -o housing_top.stl     housing_top.scad
  openscad -o housing_body.stl    housing_body.scad
  openscad -o housing_bottom.stl  housing_bottom.scad
  openscad -o speaker_baffle.stl  speaker_baffle.scad
  openscad -o diffuser_ring.stl   diffuser_ring.scad

--- PARAMETRES D'IMPRESSION RECOMMANDES ---

Materiau     : ABS blanc mat (PLA+ possible pour prototypage)
Couche       : 0.16 mm
Buse         : 0.4 mm
Remplissage  : 25 % gyroid
Perimeters   : 4
Top/bottom   : 5 couches
Temperature  : buse 245 C / lit 100 C (ABS)
Enceinte     : fortement recommandee pour ABS
Support      : uniquement pour les events du fond si necessaire

Piece diffuser_ring : imprimer en PETG TRANSLUCIDE, paroi 0.8 mm max
pour la diffusion de la lumiere.

--- LICENCE ---

CERN-OHL-S-2.0 / CC-BY-SA 4.0 - reutilisation libre avec attribution.
