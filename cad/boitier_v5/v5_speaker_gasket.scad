// ============================================================
// S3 Salle de Bain v5 - JOINTS D'ENCEINTE (x4)
// 2 pour les HP actifs (facade) + 2 pour les radiateurs passifs (arriere).
// A imprimer en TPU 95A ; comprimes au montage -> caisson etanche (basses).
// ============================================================
include <params.scad>

gasket_th  = 1.6;
gasket_out = spk_outer + 6;
gasket_in  = spk_cone - 1;

module gasket() {
    difference() {
        cylinder(d = gasket_out, h = gasket_th);
        translate([0,0,-0.1]) cylinder(d = gasket_in, h = gasket_th + 0.2);
        for (a=[45,135,225,315])
            rotate([0,0,a])
                translate([spk_bolt_circle/2,0,-0.1])
                    cylinder(d = spk_screw_d + 0.4, h = gasket_th + 0.2);
    }
}

// 4 joints en grille 2x2
for (ix=[0,1], iy=[0,1])
    translate([(ix-0.5)*(gasket_out+3), (iy-0.5)*(gasket_out+3), 0])
        gasket();
