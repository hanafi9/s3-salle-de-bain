// ============================================================
// S3 Salle de Bain v5 - CAPOT (tranche superieure du galet)
//   molette centrale (encodeur + anneau LED), micro pinhole,
//   levre press-fit, marquage DOMOKAMI + version EN RELIEF.
//   Construit en coords monde (z = base_h .. total) -> mate avec le bac.
// ============================================================

include <params.scad>

lip_outer_l = inner_l - 2*lip_clear;
lip_outer_w = inner_w - 2*lip_clear;
lip_outer_r = corner_r - wall - lip_clear;
lip_wall    = 2.2;
plate_th    = 5;     // epaisseur du plateau superieur (dessous evide)

module top_cap() {
    difference() {
        union() {
            // coque = tranche superieure du galet
            intersection() {
                pebble_body(outer_l, outer_w, total_h, corner_r, fillet);
                translate([0,0,base_h]) rounded_box(outer_l+4, outer_w+4, top_h+1, corner_r+2);
            }
            // levre peripherique qui plonge dans le bac
            translate([0,0, base_h - lip_h])
                difference() {
                    rounded_box(lip_outer_l, lip_outer_w, lip_h + 0.6, lip_outer_r);
                    translate([0,0,-0.1])
                        rounded_box(lip_outer_l - 2*lip_wall, lip_outer_w - 2*lip_wall,
                                    lip_h + 0.8, max(1, lip_outer_r - lip_wall));
                    // chanfrein d'entree en bas de la levre
                    translate([0,0,-0.1])
                        difference() {
                            rounded_box(lip_outer_l+1, lip_outer_w+1, 1.2, lip_outer_r);
                            translate([0,0,-0.1])
                                rounded_box(lip_outer_l-2.4, lip_outer_w-2.4, 1.5,
                                            max(1, lip_outer_r-1.2));
                        }
                }
        }

        // evidement du dessous (clearance encodeur + anneau LED + electronique)
        translate([0,0, base_h - 0.1])
            rounded_box(inner_l - 2, inner_w - 2, top_h - plate_th + 0.1, corner_r - wall);

        // gorge anneau LED (sur le dessus)
        translate(concat(led_pos, [total_h - led_groove + 0.01]))
            difference() {
                cylinder(d = led_outer, h = led_groove + fillet + 0.2);
                translate([0,0,-0.05]) cylinder(d = led_inner, h = led_groove + fillet + 0.3);
            }
        // cuvette bouton
        translate(concat(enc_pos, [total_h - enc_knob_recess + 0.01]))
            cylinder(d = enc_knob_d + 3, h = enc_knob_recess + fillet + 0.2);
        // passage douille encodeur (traversant)
        translate(concat(enc_pos, [base_h - lip_h - 0.1]))
            cylinder(d = enc_bushing_d, h = total_h + 0.2);
        // canal conique micro
        translate(concat(mic_pos, [total_h - plate_th - 0.1])) {
            cylinder(d1 = mic_cone_d, d2 = mic_hole_d, h = mic_cone_h + 0.1);
            translate([0,0,mic_cone_h]) cylinder(d = mic_hole_d, h = plate_th + 0.5);
        }
    }

    // ---- Marquage EN RELIEF : DOMOKAMI + version (sous la molette, cote facade) ----
    for (it = [[brand_text, brand_size, brand_pos1],
               [brand_version, brand_ver_size, brand_pos2]])
        translate([it[2][0], it[2][1], total_h - 0.4])
            rotate([0,0,180])    // lecture depuis la facade (+Y)
                linear_extrude(height = 0.4 + brand_relief)
                    text(it[0], size = it[1], halign = "center",
                         valign = "center", font = brand_font);
}

top_cap();
