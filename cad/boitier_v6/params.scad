// ============================================================
// S3 Salle de Bain - Boitier v6  "JBL Go/Clip" : plat, large, epure
//  - 2 HP plein-bande actifs en FACADE (+Y), 2 grilles rondes
//  - 2 RADIATEURS PASSIFS sur les 2 BOUTS (+-X) avec logo DOMOKAMI grave
//  - USB-C seul a l'arriere (-Y) -> plus de chevauchement avec un HP
//  - caisson etanche, carte 76,7 x 108 mm (export JLCPCB)
// ============================================================

$fn = 140;

grille_simple = false;   // true (STEP) -> ouvertures circulaires simples

// --- Carte (PCB porteuse KiCad, rotation -90deg) ---
pcb_l = 108.03; pcb_w = 76.69;
pcb_clear = 8; pcb_standoff = 6; pcb_hole_d = 3.2; pcb_insert_d = 4.2;
pcb_mounts = [ [ 46.96, -31.13], [ 46.58,  33.93],
               [-48.55,  33.93], [-47.04, -31.13] ];

// --- Coque (plate & large, bords adoucis) ---
wall = 2.6; corner_r = 24; fillet = 7; floor_th = 5.0;
inner_l = pcb_l + 2*pcb_clear;   // 124.03
inner_w = pcb_w + 2*pcb_clear;   // 92.69
outer_l = inner_l + 2*wall;      // ~129.2  (large, axe X)
outer_w = inner_w + 2*wall;      // ~97.9   (profondeur, axe Y)
base_h = 50; top_h = 8; total_h = base_h + top_h;   // 58 (plat & large)

// --- Molette centrale (encodeur EC11 + anneau LED) ---
enc_bushing_d = 7.4; enc_knob_d = 22; enc_knob_recess = 1.4; enc_pos = [0,0];
led_outer = 44; led_inner = 30; led_groove = 1.8; led_pos = [0,0];

// --- Micro (pinhole au-dessus de l'INMP441) ---
mic_pos = [37.86, 17.58]; mic_hole_d = 0.8; mic_cone_d = 3.0; mic_cone_h = 1.8;

// --- Haut-parleurs 40 mm ---
spk_outer = 40; spk_cone = 33; spk_bolt_circle = 45; spk_screw_d = 2.6;
spk_grille_hole = 2.2; spk_grille_gap = 3.4;
spk_spacing = 52;          // entraxe des 2 HP facade (x = +-26)
spk_center_z = 24;         // hauteur du centre des HP (boitier plat)
// HP actifs facade (paroi +Y) : [x, signe]
front_spk = [ [-spk_spacing/2, +1], [ spk_spacing/2, +1] ];
// radiateurs passifs sur les bouts (parois +-X) : signe X
end_rad   = [ +1, -1 ];

// --- USB-C (arriere -Y, sur J2, SEUL -> aucun chevauchement) ---
usb_w = 9.4; usb_h = 3.6; usb_z = 15; usb_x = -32.95;

// --- Fermeture capot : levre press-fit ---
lip_h = 7; lip_clear = 0.15;

// --- Pieds silicone ---
foot_d = 12; foot_recess = 0.8; foot_inset = 20;

// --- Marquage ---
brand_text = "DOMOKAMI"; brand_version = "S3  v6";
brand_relief = 0.6; brand_depth = 0.6;
brand_font = "Liberation Sans:style=Bold";
brand_top_size = 4.0;      // petite version sur le dessus
brand_end_size = 7.5;      // logo sur les bouts (facon JBL), plus gros
brand_top_pos1 = [0, 26];  // (logo top optionnel)
brand_top_pos2 = [0, 31];

// ============================================================
// Helpers
// ============================================================
module rounded_rect(l, w, r) {
    hull() for (sx=[-1,1], sy=[-1,1])
        translate([sx*(l/2-r), sy*(w/2-r)]) circle(r=r);
}
module rounded_box(l, w, h, r) { linear_extrude(height=h) rounded_rect(l, w, r); }
module pebble_body(l, w, h, rc, fil) {
    minkowski() {
        translate([0,0,fil]) rounded_box(l-2*fil, w-2*fil, h-2*fil, max(0.8, rc-fil));
        sphere(r=fil, $fn=28);
    }
}
// Grille hexagonale : uniquement hexagones ENTIERS (bord net)
module hex_grille(diam, hole_d, gap) {
    R = diam/2 - hole_d/2; rows = ceil(diam/gap)+2;
    for (iy=[-rows:rows]) {
        yo = iy*gap*0.866; xo = (iy%2==0)?0:gap/2;
        for (ix=[-rows:rows]) {
            cx = ix*gap+xo; cy = yo;
            if (cx*cx + cy*cy <= R*R) translate([cx,cy]) circle(d=hole_d, $fn=6);
        }
    }
}
