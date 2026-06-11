// ============================================================
// S3 Salle de Bain - Boitier voice assistant
// Piece : FOND (USB-C + events + inserts M3)
// Auteur : Hanafi BENMESBAH / domokami
// ============================================================

$fn = 160;

outer_diameter = 110;
thickness = 3.0;
wall = 2.4;

// USB-C port (centre arriere)
usb_w = 9.2;
usb_h = 3.4;
usb_offset = 36;      // decale de l'axe vers l'arriere
usb_angle = 180;

// Pieds silicone
foot_d = 14;
foot_recess_depth = 0.8;
foot_offset = 38;

// Events de refroidissement (anneau de slots)
vent_count = 24;
vent_r = 40;
vent_w = 2.2;
vent_l = 8;

// Inserts filetes M3
insert_d = 4.2;        // insert thermofondu M3
insert_count = 3;
insert_r = 48;
insert_depth = 5.5;

// ============================================================

module bottom_plate() {
    difference() {
        cylinder(d = outer_diameter, h = thickness);

        // USB-C
        rotate([0,0,usb_angle])
            translate([usb_offset, -usb_w/2, -0.1])
                cube([usb_w, usb_w, thickness + 0.2]);
        rotate([0,0,usb_angle])
            translate([usb_offset + usb_w/2, 0, -0.1])
                // chanfrein cosmetique
                cylinder(d = usb_h + 0.6, h = thickness + 0.2);

        // Pieds silicone (4 recess)
        for (a = [45, 135, 225, 315]) {
            rotate([0,0,a])
                translate([foot_offset, 0, -0.01])
                    cylinder(d = foot_d, h = foot_recess_depth);
        }

        // Events cooling
        for (i = [0:vent_count-1]) {
            a = i * (360/vent_count);
            rotate([0,0,a])
                translate([vent_r - vent_l/2, -vent_w/2, -0.1])
                    cube([vent_l, vent_w, thickness + 0.2]);
        }
    }

    // Colonnes d'inserts M3 (3 x 120 deg)
    for (a = [0, 120, 240]) {
        rotate([0,0,a])
            translate([insert_r, 0, 0])
                difference() {
                    cylinder(d = insert_d + 3, h = thickness + insert_depth);
                    translate([0,0,thickness])
                        cylinder(d = insert_d, h = insert_depth + 0.1);
                }
    }
}

bottom_plate();
