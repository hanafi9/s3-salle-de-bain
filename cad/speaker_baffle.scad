// ============================================================
// S3 Salle de Bain - Boitier voice assistant
// Piece : BAFFLE STEREO (support haut-parleurs 40 mm)
// Auteur : Hanafi BENMESBAH / domokami
// ============================================================

$fn = 128;

plate_d = 105;
plate_thickness = 3.5;
speaker_d = 38;        // diametre interieur cone
speaker_flange_d = 42; // diametre exterieur membrane
speaker_tilt = 35;     // degres d'inclinaison
speaker_offset = 28;
screw_d = 2.6;
screw_circle_d = 40;

module speaker_cutout() {
    cylinder(d = speaker_d, h = plate_thickness + 2, center = false);
    // 4 trous de vis
    for (a = [45, 135, 225, 315]) {
        rotate([0,0,a])
            translate([screw_circle_d/2, 0, 0])
                cylinder(d = screw_d, h = plate_thickness + 2);
    }
}

module ribbed_plate() {
    difference() {
        cylinder(d = plate_d, h = plate_thickness);
        // Decoupes speakers inclines gauche et droite
        for (s = [-1, 1]) {
            translate([s*speaker_offset, 0, -0.1])
                rotate([0, s*speaker_tilt, 0])
                    speaker_cutout();
        }
    }

    // Nervures de rigidification (croix)
    for (a = [0, 90]) {
        rotate([0,0,a])
            translate([-plate_d/2 + 6, -1.2, plate_thickness])
                cube([plate_d - 12, 2.4, 4]);
    }
}

ribbed_plate();
