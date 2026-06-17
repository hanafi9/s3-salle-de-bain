// ============================================================
// S3 Salle de Bain v6 - BAC (JBL Go/Clip : plat & large)
//  facade +Y : 2 HP actifs ; bouts +-X : 2 radiateurs passifs (logo DOMOKAMI)
//  arriere -Y : USB-C seul ; caisson etanche.
// ============================================================
include <params.scad>

// feature sur paroi +-Y (facade/arriere)
module on_Ywall(x, sy, z) {
    translate([x, sy*(outer_w/2 - wall - 0.01), z])
        rotate([sy>0 ? -90 : 90, 0, 0]) children();
}
// feature sur paroi +-X (bouts)
module on_Xwall(y, sx, z) {
    translate([sx*(outer_l/2 - wall - 0.01), y, z])
        rotate([0, sx>0 ? 90 : -90, 0]) children();
}

module base() {
    difference() {
        intersection() {
            pebble_body(outer_l, outer_w, total_h, corner_r, fillet);
            translate([0,0,-1]) rounded_box(outer_l+4, outer_w+4, base_h+1, corner_r+2);
        }
        // cavite
        translate([0,0,floor_th]) rounded_box(inner_l, inner_w, base_h, corner_r - wall);

        // 2 grilles HP facade (+Y)
        for (s = front_spk)
            on_Ywall(s[0], s[1], spk_center_z)
                linear_extrude(height = wall + 0.3)
                    if (grille_simple) circle(d = spk_cone);
                    else hex_grille(spk_cone, spk_grille_hole, spk_grille_gap);
        // avant-trous HP facade
        for (s = front_spk) for (a=[45,135,225,315])
            translate([s[0] + spk_bolt_circle/2*cos(a), s[1]*(inner_w/2 - 0.5),
                       spk_center_z + spk_bolt_circle/2*sin(a)])
                rotate([s[1]>0 ? -90 : 90, 0, 0]) cylinder(d=spk_screw_d, h=2.2);

        // 2 radiateurs passifs sur les bouts (+-X)
        for (sx = end_rad)
            on_Xwall(0, sx, spk_center_z)
                linear_extrude(height = wall + 0.3)
                    if (grille_simple) circle(d = spk_cone);
                    else hex_grille(spk_cone, spk_grille_hole, spk_grille_gap);
        // avant-trous radiateurs
        for (sx = end_rad) for (a=[45,135,225,315])
            translate([sx*(inner_l/2 - 0.5),
                       0 + spk_bolt_circle/2*cos(a),
                       spk_center_z + spk_bolt_circle/2*sin(a)])
                rotate([0, sx>0 ? 90 : -90, 0]) cylinder(d=spk_screw_d, h=2.2);

        // USB-C (arriere -Y, seul)
        translate([usb_x, -outer_w/2 - 0.1, usb_z])
            rotate([-90,0,0])
                hull() for (k=[-1,1]) translate([k*(usb_w-usb_h)/2,0,0]) cylinder(d=usb_h, h=wall+0.6);

        // pieds
        for (sx=[-1,1], sy=[-1,1])
            translate([sx*(outer_l/2 - foot_inset), sy*(outer_w/2 - foot_inset), -0.01])
                cylinder(d=foot_d, h=foot_recess);

        // encoche demontage (arriere -Y, a cote de l'USB-C)
        translate([outer_l/2*0.55, -outer_w/2 + wall/2, base_h - 3])
            cube([16, wall+1, 6], center=true);
    }

    // entretoises PCB
    for (p = pcb_mounts)
        translate([p[0], p[1], floor_th - 1])
            difference() {
                cylinder(d = 7, h = pcb_standoff + 1);
                translate([0,0, pcb_standoff + 1 - 5]) cylinder(d = pcb_insert_d, h = 5.2);
            }

    // logo DOMOKAMI EN RELIEF sur chaque bout (facon logo JBL sur la membrane)
    for (sx = end_rad)
        translate([sx*(outer_l/2 - 0.4), 0, base_h - 7])
            rotate([90, 0, sx>0 ? 90 : -90])
                linear_extrude(height = 0.4 + brand_relief)
                    text(brand_text, size = brand_end_size, halign="center",
                         valign="center", font = brand_font);
}

base();
