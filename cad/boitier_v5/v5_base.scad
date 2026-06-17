// ============================================================
// S3 Salle de Bain v5 - BAC (galet integral, caisson etanche)
//   4 ouvertures HP (2 facade +Y actifs / 2 arriere -Y radiateurs passifs)
//   USB-C en bas de la paroi arriere, entretoises PCB, pas d'events.
// ============================================================

include <params.scad>

// place un element (children) sur la paroi +Y (sy=+1) ou -Y (sy=-1)
module on_Ywall(x, sy, z) {
    translate([x, sy*(outer_w/2 - wall - 0.01), z])
        rotate([sy>0 ? -90 : 90, 0, 0])
            children();
}
// anneau de vissage INTERNE : part de la face interieure de la paroi et
// fait saillie vers l'interieur du caisson (rien ne depasse a l'exterieur)
module on_Ywall_in(x, sy, z) {
    translate([x, sy*(inner_w/2 + 2.0), z])    // 2.0mm dans la paroi (fusion solide)
        rotate([sy>0 ? 90 : -90, 0, 0])        // extrude vers l'INTERIEUR
            children();
}

module base() {
    // ---- coque galet creusee + decoupes ----
    difference() {
        intersection() {
            pebble_body(outer_l, outer_w, total_h, corner_r, fillet);
            translate([0,0,-1]) rounded_box(outer_l+4, outer_w+4, base_h+1, corner_r+2);
        }
        // cavite interieure (au-dessus du fond)
        translate([0,0,floor_th])
            rounded_box(inner_l, inner_w, base_h, corner_r - wall);

        // 4 ouvertures HP (facade + arriere)
        for (s = speakers)
            on_Ywall(s[0], s[1], spk_center_z)
                linear_extrude(height = wall + 0.3)
                    if (grille_simple) circle(d = spk_cone);
                    else hex_grille(spk_cone, spk_grille_hole, spk_grille_gap);

        // 4 avant-trous de vissage borgnes par HP (vissage interieur M2.5)
        for (s = speakers)
            for (a = [45,135,225,315])
                translate([s[0] + spk_bolt_circle/2*cos(a),
                           s[1]*(inner_w/2 - 0.5),
                           spk_center_z + spk_bolt_circle/2*sin(a)])
                    rotate([s[1]>0 ? -90 : 90, 0, 0])
                        cylinder(d = spk_screw_d, h = 2.2);   // borgne (0.6mm paroi reste)

        // USB-C (paroi arriere -Y, en bas, sur J2)
        translate([usb_x, -outer_w/2 - 0.1, usb_z])
            rotate([-90,0,0])
                hull() for (sx=[-1,1])
                    translate([sx*(usb_w-usb_h)/2,0,0])
                        cylinder(d=usb_h, h=wall+0.6);

        // Pieds silicone (dessous)
        for (sx=[-1,1], sy=[-1,1])
            translate([sx*(outer_l/2 - foot_inset), sy*(outer_w/2 - foot_inset), -0.01])
                cylinder(d=foot_d, h=foot_recess);

        // Encoche de demontage (paroi laterale -X)
        translate([-outer_l/2 + wall/2, 0, base_h - 3])
            cube([wall+1, 16, 6], center=true);
    }

    // ---- entretoises PCB (4 trous MK reels) ----
    for (p = pcb_mounts)
        translate([p[0], p[1], floor_th - 1])
            difference() {
                cylinder(d = 7, h = pcb_standoff + 1);
                translate([0,0, pcb_standoff + 1 - 5])
                    cylinder(d = pcb_insert_d, h = 5.2);
            }

}

base();
