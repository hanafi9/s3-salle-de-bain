// Vue d'assemblage / eclate (presentation seulement)
include <params.scad>
use <v4_base.scad>
use <v4_top.scad>

explode = 34;   // ecartement vertical pour l'eclate

color([0.32,0.45,0.62]) base();
color([0.74,0.78,0.83])
    translate([0,0, base_h + explode])
        top_cap();
