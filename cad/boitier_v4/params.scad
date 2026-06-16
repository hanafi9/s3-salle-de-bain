// ============================================================
// S3 Salle de Bain - Boitier v4  "galet rectangulaire arrondi"
// Parametres partages (inclus par base / top / baffle)
// Auteur : Hanafi BENMESBAH / domokami
// Design : classe & epure, facade enceintes, encodeur + anneau LED
// Adapte a la carte 145 x 108 mm + HP 40 mm + encodeur EC11 (cotes standard)
// ============================================================

$fn = 160;

// --- Carte (PCB porteuse KiCad) ---
pcb_l        = 145;     // longueur carte
pcb_w        = 108;     // largeur carte
pcb_clear    = 4;       // jeu autour de la carte
pcb_standoff = 6;       // hauteur entretoises sous la carte
pcb_hole_d   = 3.2;     // trou de passage M3 (vis dans insert)
pcb_insert_d = 4.2;     // alesage insert thermofondu M3 dans l'entretoise
// 4 points de fixation REELS, valides sans collision sur le PCB KiCad.
// Coords boitier (centrees) :  X = px-72.5 , Y = py-54  (USB-C bord bas -> paroi -Y)
//   PCB (7,7)   (138,44)   (104,101)  (7,101)
pcb_mounts = [ [-65.5, -47],   // MK1
               [ 65.5, -10],   // MK2 (decale pour degager C6 470uF)
               [ 31.5,  47],   // MK3
               [-65.5,  47] ]; // MK4

// --- Coque ---
wall         = 2.6;     // epaisseur paroi
corner_r     = 28;      // rayon des coins arrondis (allure galet)
floor_th     = 3.0;     // epaisseur du fond
chamfer      = 2.2;     // chanfrein superieur cosmetique

inner_l = pcb_l + 2*pcb_clear;          // 153
inner_w = pcb_w + 2*pcb_clear;          // 116
outer_l = inner_l + 2*wall;             // ~158.2
outer_w = inner_w + 2*wall;             // ~121.2

base_h  = 42;           // hauteur du bac (paroi)
top_h   = 11;           // hauteur du capot (bombe + chanfrein)
total_h = base_h + top_h;

// --- Encodeur EC11 (cotes standard) ---
enc_bushing_d = 7.4;    // douille filetee M7 (passage)
enc_body_w    = 13.6;   // corps (jeu)
enc_knob_d    = 22;     // bouton aluminium
enc_knob_recess = 1.4;  // legere cuvette sous le bouton
// Encodeur + anneau = sous-ensemble monte SUR LE CAPOT (panneau, douille M7),
// relie par fil aux connecteurs SW1/DS1 du PCB. Donc cadran CENTRE = epure max.
enc_pos        = [0, 0];   // cadran centre sur le capot

// --- Anneau LED WS2812 (diffuseur PETG) ---
led_outer    = 82;
led_inner    = 62;
led_groove   = 1.8;     // profondeur logement diffuseur
led_pos      = [0, 0];  // concentrique a l'encodeur

// --- Micro MEMS (pinhole conique invisible) ---
mic_pos      = [58, -40];   // rejete dans un coin, invisible
mic_hole_d   = 0.8;
mic_cone_d   = 3.0;
mic_cone_h   = 1.8;

// --- Haut-parleurs 40 mm en facade (front-firing) ---
spk_outer    = 40;      // cadre exterieur HP
spk_cone     = 33;      // ouverture cone (grille)
spk_bolt_circle = 33.5; // entraxe vis de fixation
spk_screw_d  = 2.6;     // vis M2.5
spk_spacing  = 52;      // entraxe entre les 2 HP (gauche/droite)
spk_center_z = 22;      // hauteur du centre des HP / fond du bac
spk_grille_hole = 2.2;  // diametre des trous de grille
spk_grille_gap  = 3.4;  // pas de la grille hexagonale

// --- USB-C (face arriere) ---
usb_w = 9.4;
usb_h = 3.6;
usb_z = 14;             // hauteur du centre du port

// --- Events de ventilation (fond) ---
vent_count = 5;
vent_w = 2.4;
vent_l = 26;
vent_pitch = 5;

// --- Fermeture capot : levre en press-fit (aucune vis sur le dessus) ---
lip_h       = 7;        // hauteur de la levre du capot qui plonge dans le bac
lip_clear   = 0.15;     // interference press-fit levre / paroi (PA-CF)

// --- Pieds silicone ---
foot_d = 12;
foot_recess = 0.8;
foot_inset = 16;

// ============================================================
// Helpers
// ============================================================

// Rectangle a coins arrondis (extrusion d'un profil 2D)
module rounded_rect(l, w, r) {
    hull() {
        for (sx = [-1, 1], sy = [-1, 1])
            translate([sx*(l/2 - r), sy*(w/2 - r)])
                circle(r = r);
    }
}

// Prisme a coins arrondis
module rounded_box(l, w, h, r) {
    linear_extrude(height = h)
        rounded_rect(l, w, r);
}
