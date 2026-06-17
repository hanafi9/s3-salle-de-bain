// Vue d'assemblage / eclate (presentation)
include <params.scad>
use <v5_base.scad>
use <v5_top.scad>
explode = 30;
color([0.30,0.43,0.60]) base();
color([0.78,0.81,0.85]) translate([0,0,explode]) top_cap();
