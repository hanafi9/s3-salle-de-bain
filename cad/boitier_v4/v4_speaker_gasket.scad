// ============================================================
// S3 Salle de Bain v4 - JOINT D'ENCEINTE (x2)
// Anneau d'etancheite acoustique entre le HP 40 mm et la facade.
// A imprimer en TPU (Shore 95A) ; comprime au serrage des vis M2.5.
// ============================================================

include <params.scad>

gasket_th   = 1.6;       // epaisseur (compressible)
gasket_out  = spk_outer + 3;
gasket_in   = spk_cone - 1;

module gasket() {
    difference() {
        cylinder(d = gasket_out, h = gasket_th);
        translate([0,0,-0.1]) cylinder(d = gasket_in, h = gasket_th + 0.2);
        // 4 trous de passage vis M2.5
        for (a=[45,135,225,315])
            rotate([0,0,a])
                translate([spk_bolt_circle/2,0,-0.1])
                    cylinder(d = spk_screw_d + 0.4, h = gasket_th + 0.2);
    }
}

// 2 joints cote a cote pour l'impression
translate([-(gasket_out/2+2),0,0]) gasket();
translate([ (gasket_out/2+2),0,0]) gasket();
