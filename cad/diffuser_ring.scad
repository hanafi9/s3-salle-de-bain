// ============================================================
// S3 Salle de Bain - Boitier voice assistant
// Piece : ANNEAU DIFFUSEUR LED (PETG TRANSLUCIDE)
// Auteur : Hanafi BENMESBAH / domokami
// ============================================================

$fn = 256;

outer_d = 82;
inner_d = 62;
height = 2.0;
lip_h = 0.8;
lip_thickness = 0.8;

module ring() {
    difference() {
        union() {
            // Anneau principal
            difference() {
                cylinder(d = outer_d, h = height);
                translate([0,0,-0.1])
                    cylinder(d = inner_d, h = height + 0.2);
            }
            // Levre de maintien interne
            translate([0,0,-lip_h])
                difference() {
                    cylinder(d = inner_d + lip_thickness*2, h = lip_h);
                    translate([0,0,-0.1])
                        cylinder(d = inner_d, h = lip_h + 0.2);
                }
        }
    }
}

ring();
