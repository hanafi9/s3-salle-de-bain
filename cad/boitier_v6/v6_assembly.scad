// Vue d'assemblage / eclate (presentation)
include <params.scad>
use <v6_base.scad>
use <v6_top.scad>
explode = 30;
color([0.30,0.43,0.60]) base();
color([0.78,0.81,0.85]) translate([0,0,explode]) top_cap();
