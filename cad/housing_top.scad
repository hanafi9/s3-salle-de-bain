// ============================================================
// S3 Salle de Bain - Boitier voice assistant
// Piece : CAPOT SUPERIEUR
// Auteur : Hanafi BENMESBAH / domokami
// Materiau recommande : ABS blanc mat, couche 0.16 mm, 4 perimeters, 25% gyroid
// ============================================================

$fn = 128;

// --- Parametres globaux ---
outer_diameter = 110;
total_height = 55;
wall = 2.4;
chamfer = 2.0;
top_thickness = 3.0;

// Aperture anneau LED (diffuseur PETG)
led_ring_outer = 82;
led_ring_inner = 62;
led_ring_depth = 1.8;

// Aperture bouton / encodeur central
knob_aperture_d = 26;
knob_recess_d = 34;
knob_recess_depth = 1.2;

// Microphone pinhole (decale a l'avant)
mic_offset = 42;
mic_hole_d = 0.8;
mic_cone_d_outer = 3.0;
mic_cone_depth = 1.8;

// Inserts clips (3 lugs internes a 120 deg)
clip_lug_r = 48.5;
clip_lug_h = 10;
clip_lug_w = 6;

// ============================================================

module top_cap() {
    difference() {
        // Coque principale avec chanfrein
        union() {
            cylinder(d = outer_diameter, h = top_thickness);
            translate([0,0,top_thickness])
                cylinder(d1 = outer_diameter, d2 = outer_diameter - 2*chamfer,
                         h = chamfer);
        }

        // Recess anneau LED
        translate([0,0,top_thickness - led_ring_depth + 0.01])
            difference() {
                cylinder(d = led_ring_outer, h = led_ring_depth + chamfer + 0.1);
                translate([0,0,-0.05])
                    cylinder(d = led_ring_inner, h = led_ring_depth + chamfer + 0.2);
            }

        // Recess bouton / knob (cavite ronde)
        translate([0,0,top_thickness - knob_recess_depth + 0.01])
            cylinder(d = knob_recess_d, h = knob_recess_depth + chamfer + 0.1);

        // Aperture knob traversante
        translate([0,0,-0.1])
            cylinder(d = knob_aperture_d, h = top_thickness + chamfer + 0.2);

        // Canal conique microphone
        translate([mic_offset, 0, -0.1]) {
            cylinder(d1 = mic_cone_d_outer, d2 = mic_hole_d,
                     h = mic_cone_depth + 0.1);
            translate([0,0,mic_cone_depth])
                cylinder(d = mic_hole_d, h = top_thickness + chamfer);
        }
    }

    // 3 lugs internes pour clips
    for (a = [0, 120, 240]) {
        rotate([0,0,a])
            translate([clip_lug_r, -clip_lug_w/2, -clip_lug_h])
                cube([wall, clip_lug_w, clip_lug_h]);
    }
}

top_cap();
