// ============================================================
// S3 Salle de Bain - Boitier v5  "galet integral" (bords adoucis)
// Forme galet arrondie sur TOUTES les aretes (minkowski), plus haute
// pour le volume de basses. 4 HP : 2 plein-bande en facade (+Y) +
// 2 radiateurs passifs a l'arriere (-Y) pour la reflexion de basse.
// Caisson ETANCHE (pas d'events). Carte 76,7 x 108 mm (export JLCPCB).
// Auteur : Hanafi BENMESBAH / domokami
// ============================================================

$fn = 140;

grille_simple = false;   // true (STEP) -> ouvertures circulaires simples

// --- Carte (PCB porteuse KiCad, rotation -90deg dans le boitier) ---
pcb_l        = 108.03;
pcb_w        = 76.69;
pcb_clear    = 4;
pcb_standoff = 6;
pcb_hole_d   = 3.2;
pcb_insert_d = 4.2;
// 4 trous M3 reels MK1-MK4 (coords boitier centrees)
pcb_mounts = [ [ 46.96, -31.13], [ 46.58,  33.93],
               [-48.55,  33.93], [-47.04, -31.13] ];

// --- Coque galet ---
wall      = 2.6;
corner_r  = 36;      // rayon des coins (plan) - vrai galet
fillet    = 12;      // arrondi des aretes haut/bas (galet tres rond)
floor_th  = 7.0;     // fond epaissi (suit l'arrondi du bas)

inner_l = pcb_l + 2*pcb_clear;          // 116.03
inner_w = pcb_w + 2*pcb_clear;          // 84.69
outer_l = inner_l + 2*wall;             // ~121.2
outer_w = inner_w + 2*wall;             // ~89.9

base_h  = 54;        // bac : volume de basses + USB-C/radiateurs etages
top_h   = 15;        // capot (galet superieur, > fillet pour un joint propre)
total_h = base_h + top_h;               // 69

// --- Encodeur EC11 + molette centrale ---
enc_bushing_d = 7.4;
enc_knob_d    = 22;
enc_knob_recess = 1.4;
enc_pos       = [0, 0];

// --- Anneau LED WS2812 (cadran reduit : dessus plat plus petit) ---
led_outer  = 44;
led_inner  = 30;
led_groove = 1.8;
led_pos    = [0, 0];

// --- Micro MEMS (pinhole au-dessus de l'INMP441) ---
mic_pos    = [37.86, 17.58];
mic_hole_d = 0.8;
mic_cone_d = 3.0;
mic_cone_h = 1.8;

// --- Haut-parleurs 40 mm ---
// 2 actifs en facade (+Y) + 2 radiateurs passifs a l'arriere (-Y).
spk_outer    = 40;
spk_cone     = 33;
spk_bolt_circle = 45;   // vis a l'exterieur du cadre 40mm (realiste)
spk_screw_d  = 2.6;
spk_spacing  = 52;     // entraxe (x = +-26)
spk_center_z = 31;     // haut (degage l'USB-C en bas de la paroi arriere)
spk_grille_hole = 2.2;
spk_grille_gap  = 3.4;
// liste : [x, signe_paroi_Y(+1 facade / -1 arriere), passif?]
speakers = [ [-spk_spacing/2, +1, false], [ spk_spacing/2, +1, false],   // facade actifs
             [-spk_spacing/2, -1, true ], [ spk_spacing/2, -1, true ] ]; // arriere passifs

// --- USB-C (paroi arriere -Y, en BAS, decale sur J2) ---
usb_w = 9.4;
usb_h = 3.6;
usb_z = 15;          // PCB releve (fond 7 + entretoise 6)
usb_x = -32.95;

// --- Fermeture capot : levre press-fit (caisson etanche, sans vis) ---
lip_h     = 8;
lip_clear = 0.15;

// --- Pieds silicone ---
foot_d = 12;
foot_recess = 0.8;
foot_inset = 20;     // bien rentre sur le fond plat (evite l'arrondi du bas)

// --- Marquage EN RELIEF sur le capot (logo DOMOKAMI + version) ---
brand_text    = "DOMOKAMI";
brand_version = "S3  v5";
brand_size    = 4.5;
brand_ver_size= 2.8;
brand_relief  = 0.6;
brand_font    = "Liberation Sans:style=Bold";
brand_pos1    = [0, 26];
brand_pos2    = [0, 30];

// ============================================================
// Helpers
// ============================================================
module rounded_rect(l, w, r) {
    hull() for (sx=[-1,1], sy=[-1,1])
        translate([sx*(l/2-r), sy*(w/2-r)]) circle(r=r);
}
module rounded_box(l, w, h, r) {
    linear_extrude(height=h) rounded_rect(l, w, r);
}
// Galet plein : faces dessus/dessous plates, TOUTES les aretes arrondies (fillet)
module pebble_body(l, w, h, rc, fil) {
    minkowski() {
        translate([0,0,fil])
            rounded_box(l-2*fil, w-2*fil, h-2*fil, max(0.8, rc-fil));
        sphere(r=fil, $fn=28);
    }
}
// Grille hexagonale sur zone circulaire (ouverture HP)
module hex_grille(diam, hole_d, gap) {
    rows = ceil(diam/gap)+2;
    intersection() {
        circle(d=diam);
        for (iy=[-rows:rows]) {
            yo = iy*gap*0.866; xo = (iy%2==0)?0:gap/2;
            for (ix=[-rows:rows]) translate([ix*gap+xo, yo]) circle(d=hole_d, $fn=6);
        }
    }
}
