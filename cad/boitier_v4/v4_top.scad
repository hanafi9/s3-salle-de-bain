// ============================================================
// S3 Salle de Bain v4 - CAPOT (dessus epure, fermeture par levre)
//   molette centree (encodeur EC11 + anneau LED), micro pinhole,
//   chanfrein doux, levre periph. qui plonge dans le bac (sans vis)
// ============================================================

include <params.scad>

lip_outer_l = inner_l - 2*lip_clear;
lip_outer_w = inner_w - 2*lip_clear;
lip_outer_r = corner_r - wall - lip_clear;
lip_wall    = 2.2;

module top_cap() {
    difference() {
        union() {
            // ---- Plateau + chanfrein doux (allure galet) ----
            rounded_box(outer_l, outer_w, top_h - chamfer, corner_r);
            translate([0,0,top_h - chamfer])
                hull() {
                    rounded_box(outer_l, outer_w, 0.01, corner_r);
                    translate([0,0,chamfer])
                        rounded_box(outer_l - 2*chamfer, outer_w - 2*chamfer,
                                    0.01, corner_r - chamfer);
                }
            // ---- Levre periph. qui plonge dans le bac ----
            translate([0,0,-lip_h])
                difference() {
                    rounded_box(lip_outer_l, lip_outer_w, lip_h + 0.6, lip_outer_r);
                    translate([0,0,-0.1])
                        rounded_box(lip_outer_l - 2*lip_wall,
                                    lip_outer_w - 2*lip_wall,
                                    lip_h + 0.8,
                                    max(1, lip_outer_r - lip_wall));
                    // chanfrein d'entree en bas de la levre (camming)
                    translate([0,0,-0.1])
                        difference() {
                            rounded_box(lip_outer_l+1, lip_outer_w+1, 1.2, lip_outer_r);
                            translate([0,0,-0.1])
                                rounded_box(lip_outer_l-2.4, lip_outer_w-2.4, 1.5,
                                            max(1, lip_outer_r-1.2));
                        }
                }
        }

        // ---- Logement anneau LED (gorge annulaire) ----
        translate(concat(led_pos, [top_h - led_groove + 0.01]))
            difference() {
                cylinder(d = led_outer, h = led_groove + chamfer + 0.2);
                translate([0,0,-0.05]) cylinder(d = led_inner, h = led_groove + chamfer + 0.3);
            }

        // ---- Cuvette bouton (depression sous le knob) ----
        translate(concat(enc_pos, [top_h - enc_knob_recess + 0.01]))
            cylinder(d = enc_knob_d + 3, h = enc_knob_recess + chamfer + 0.2);

        // ---- Passage douille encodeur (traversant) ----
        translate(concat(enc_pos, [-lip_h - 0.1]))
            cylinder(d = enc_bushing_d, h = top_h + lip_h + 0.2);

        // ---- Canal conique micro (invisible) ----
        translate(concat(mic_pos, [-0.1])) {
            cylinder(d1 = mic_cone_d, d2 = mic_hole_d, h = mic_cone_h + 0.1);
            translate([0,0,mic_cone_h]) cylinder(d = mic_hole_d, h = top_h);
        }
    }
}

top_cap();
