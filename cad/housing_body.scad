// ============================================================
// S3 Salle de Bain - Boitier voice assistant
// Piece : CORPS CYLINDRIQUE (avec grilles stereo + mute switch)
// Auteur : Hanafi BENMESBAH / domokami
// ============================================================

$fn = 160;

// --- Parametres ---
outer_diameter = 110;
height = 46;          // corps sans capot ni fond
wall = 2.4;

// Grilles stereo laterales (motif hexagonal)
grille_center_z = height/2;
grille_w = 55;        // largeur arc
grille_h = 28;        // hauteur fenetre
grille_angle = 95;    // ouverture angulaire par cote

// Decoupes hexagones
hex_size = 4.0;       // rayon circonscrit
hex_spacing = 9.0;    // pas

// Interrupteur mute (fente laterale)
mute_angle = 180;     // arriere gauche
mute_w = 9;
mute_h = 4;
mute_z = height - 10;

// Jack 3.5 mm (face avant, bas)
jack_d = 6.5;
jack_z = 10;
jack_angle = 0;       // face avant

// LED indicator
led_ind_d = 2.0;
led_ind_z = 8;
led_ind_angle = 0;
led_ind_offset = 18;  // decale de l'axe

// Clips recess (3 x 120 deg) pour s'emboiter avec capot
clip_slot_w = 6.2;
clip_slot_h = 10.2;
clip_slot_depth = 2.6;

// ============================================================

module hex_cell(size) {
    rotate([0,0,30])
        circle(d = size*2, $fn = 6);
}

module hex_grid_pattern(w, h, s, spacing) {
    rows = ceil(h / (spacing*0.866)) + 1;
    cols = ceil(w / spacing) + 1;
    for (r = [0:rows]) {
        for (c = [0:cols]) {
            x = c*spacing + (r%2)*(spacing/2) - w/2;
            y = r*spacing*0.866 - h/2;
            if (abs(x) < w/2 - s/2 && abs(y) < h/2 - s/2)
                translate([x, y, 0]) hex_cell(s);
        }
    }
}

module stereo_grille(side_angle) {
    rotate([0,0,side_angle]) {
        translate([outer_diameter/2 - wall/2, 0, grille_center_z])
            rotate([0,90,0])
                linear_extrude(height = wall + 2, center = true)
                    hex_grid_pattern(grille_w, grille_h, hex_size, hex_spacing);
    }
}

module body() {
    difference() {
        // Tube principal
        difference() {
            cylinder(d = outer_diameter, h = height);
            translate([0,0,-0.1])
                cylinder(d = outer_diameter - 2*wall, h = height + 0.2);
        }

        // Grilles stereo gauche & droite
        stereo_grille(90);
        stereo_grille(-90);

        // Fente switch mute
        rotate([0,0,mute_angle])
            translate([outer_diameter/2 - wall, -mute_w/2, mute_z])
                cube([wall + 2, mute_w, mute_h]);

        // Jack 3.5 mm face avant
        rotate([0,0,jack_angle])
            translate([outer_diameter/2 - wall - 0.1, 0, jack_z])
                rotate([0,90,0])
                    cylinder(d = jack_d, h = wall + 2);

        // LED indicator
        rotate([0,0,led_ind_angle])
            translate([outer_diameter/2 - wall - 0.1, led_ind_offset, led_ind_z])
                rotate([0,90,0])
                    cylinder(d = led_ind_d, h = wall + 2);

        // Clips superieurs (recess intern pour lugs du capot)
        for (a = [0, 120, 240]) {
            rotate([0,0,a])
                translate([outer_diameter/2 - wall - clip_slot_depth,
                           -clip_slot_w/2,
                           height - clip_slot_h])
                    cube([clip_slot_depth + 0.1, clip_slot_w, clip_slot_h + 0.1]);
        }
    }
}

body();
