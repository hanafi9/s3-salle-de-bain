// Coupe de controle : capot pose sur le bac, demi-section (verifie la levre)
include <params.scad>
use <v4_base.scad>
use <v4_top.scad>

difference() {
    union() {
        color([0.32,0.45,0.62]) base();
        color([0.74,0.78,0.83]) translate([0,0, base_h]) top_cap();
    }
    // coupe le quart avant-droit
    translate([0,0,-2]) cube([200,200, total_h+20]);
}
