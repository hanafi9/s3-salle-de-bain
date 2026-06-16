// ============================================================
// S3 Salle de Bain v4 - BAC (fond + parois + facade enceintes)
// Fermeture par levre du capot (aucune vis sur le dessus).
// Entretoises PCB sur 4 points valides sans collision sur la carte.
// ============================================================

include <params.scad>

// --- Grille hexagonale (zone circulaire) ---
module hex_grille(diam, hole_d, gap) {
    rows = ceil(diam / gap) + 2;
    intersection() {
        circle(d = diam);
        for (iy = [-rows : rows]) {
            yo = iy * gap * 0.866;
            xo = (iy % 2 == 0) ? 0 : gap/2;
            for (ix = [-rows : rows])
                translate([ix*gap + xo, yo]) circle(d = hole_d, $fn = 6);
        }
    }
}

module base() {
    // =========================================================
    // 1) COQUE creusee + decoupes
    // =========================================================
    difference() {
        rounded_box(outer_l, outer_w, base_h, corner_r);
        translate([0,0,floor_th])
            rounded_box(inner_l, inner_w, base_h, corner_r - wall);

        // USB-C (paroi arriere -Y, decale en X pour tomber sur J2 reel)
        translate([usb_x, -outer_w/2 - 0.1, usb_z])
            rotate([-90,0,0])
                hull() for (sx=[-1,1])
                    translate([sx*(usb_w-usb_h)/2,0,0])
                        cylinder(d=usb_h, h=wall+0.4);

        // Grilles HP (face avant +Y) : hex pour l'impression, cercle pour le STEP
        for (sx = [-1,1])
            translate([sx*spk_spacing/2, outer_w/2 - wall - 0.01, spk_center_z])
                rotate([-90,0,0])
                    linear_extrude(height = wall + 0.2)
                        if (grille_simple) circle(d = spk_cone);
                        else hex_grille(spk_cone, spk_grille_hole, spk_grille_gap);

        // Events de ventilation (fond)
        for (i = [0 : vent_count-1])
            translate([-(vent_count-1)*vent_pitch/2 + i*vent_pitch, 0, -0.1])
                hull() for (sy=[-1,1])
                    translate([0, sy*(vent_l-vent_w)/2, 0])
                        cylinder(d=vent_w, h=floor_th+0.2);

        // Pieds silicone (dessous)
        for (sx=[-1,1], sy=[-1,1])
            translate([sx*(outer_l/2 - foot_inset), sy*(outer_w/2 - foot_inset), -0.01])
                cylinder(d=foot_d, h=foot_recess);

        // Encoche de demontage (paroi laterale -X, sous la levre)
        translate([-outer_l/2 + wall/2, 0, base_h - 3])
            cube([wall+1, 16, 6], center=true);
    }

    // =========================================================
    // 2) ENTRETOISES PCB (4 points valides, ajoutees apres cavite)
    // =========================================================
    for (p = pcb_mounts)
        translate([p[0], p[1], floor_th - 1])
            difference() {
                cylinder(d = 7, h = pcb_standoff + 1);
                translate([0,0, pcb_standoff + 1 - 5])
                    cylinder(d = pcb_insert_d, h = 5.2);   // alesage insert M3
            }

    // =========================================================
    // 3) SUPPORTS HP en facade (anneaux de vissage M2.5)
    // =========================================================
    for (sx = [-1,1])
        translate([sx*spk_spacing/2, outer_w/2 - wall + 0.6, spk_center_z])
            rotate([-90,0,0])
                difference() {
                    cylinder(d = spk_outer + 4, h = 4.6);
                    // alesage > ouverture grille pour eviter les surfaces coincidentes
                    translate([0,0,-0.1]) cylinder(d = spk_cone + 1.6, h = 4.8);
                    for (ang=[45,135,225,315])
                        rotate([0,0,ang])
                            translate([spk_bolt_circle/2,0,-0.1])
                                cylinder(d=spk_screw_d, h=4.8);
                }
}

base();
