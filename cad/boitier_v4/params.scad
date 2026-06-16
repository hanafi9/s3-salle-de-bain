// ============================================================
// S3 Salle de Bain - Boitier v4  "galet rectangulaire arrondi"
// Parametres partages (inclus par base / top / baffle)
// Auteur : Hanafi BENMESBAH / domokami
// Design : classe & epure, facade enceintes, encodeur + anneau LED
// ADAPTE A LA CARTE MODIFIEE : 76.69 x 108.03 mm (export JLCPCB)
//   Implantation reelle relue depuis s3-salle-de-bain.kicad_pcb (dump_pcb_geo.py)
//   Rotation -90deg appliquee : HP en facade +Y, USB-C a l'arriere -Y.
//   Mapping :  encl X = -(py - 90.86) ,  encl Y = (px - 104.50)
// ============================================================

$fn = 160;

// --- Carte (PCB porteuse KiCad, apres rotation -90deg dans le boitier) ---
pcb_l        = 108.03;  // dimension carte le long de X boitier (= 108 PCB)
pcb_w        = 76.69;   // dimension carte le long de Y boitier (= 76.7 PCB)
pcb_clear    = 4;       // jeu autour de la carte
pcb_standoff = 6;       // hauteur entretoises sous la carte
pcb_hole_d   = 3.2;     // trou de passage M3 (vis dans insert)
pcb_insert_d = 4.2;     // alesage insert thermofondu M3 dans l'entretoise
// 4 trous M3 REELS de TA carte (MK1-MK4), en coords boitier (centrees) :
//   MK1 PCB(73.37,43.90) MK2(138.43,44.28) MK3(138.43,139.41) MK4(73.37,137.90)
pcb_mounts = [ [ 46.96, -31.13],   // MK1
               [ 46.58,  33.93],   // MK2
               [-48.55,  33.93],   // MK3
               [-47.04, -31.13] ]; // MK4

// --- Coque ---
wall         = 2.6;     // epaisseur paroi
corner_r     = 22;      // rayon des coins arrondis (allure galet, boite compacte)
floor_th     = 3.0;     // epaisseur du fond
chamfer      = 2.2;     // chanfrein superieur cosmetique

inner_l = pcb_l + 2*pcb_clear;          // 116.03
inner_w = pcb_w + 2*pcb_clear;          // 84.69
outer_l = inner_l + 2*wall;             // ~121.2
outer_w = inner_w + 2*wall;             // ~89.9

base_h  = 46;           // hauteur du bac (loge un HP 40 mm en facade)
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
led_outer    = 60;      // reduit pour le capot compact (largeur ~90 mm)
led_inner    = 44;
led_groove   = 1.8;     // profondeur logement diffuseur
led_pos      = [0, 0];  // concentrique a l'encodeur

// --- Micro MEMS (pinhole conique invisible) -> au-dessus de U4 (INMP441) ---
mic_pos      = [37.86, 17.58];   // = position reelle du micro sur la carte
mic_hole_d   = 0.8;
mic_cone_d   = 3.0;
mic_cone_h   = 1.8;

// --- Haut-parleurs 40 mm en facade +Y (front-firing) ---
spk_outer    = 40;      // cadre exterieur HP
spk_cone     = 33;      // ouverture cone (grille)
spk_bolt_circle = 33.5; // entraxe vis de fixation
spk_screw_d  = 2.6;     // vis M2.5
spk_spacing  = 52;      // entraxe entre les 2 HP (gauche/droite, le long de X)
spk_center_z = 23;      // hauteur du centre des HP / fond du bac
spk_grille_hole = 2.2;  // diametre des trous de grille
spk_grille_gap  = 3.4;  // pas de la grille hexagonale

// --- USB-C (paroi arriere -Y, decale en X pour tomber sur J2) ---
usb_w = 9.4;
usb_h = 3.6;
usb_z = 14;             // hauteur du centre du port
usb_x = -32.95;         // position le long de la paroi -Y (= J2 reel)

// --- Events de ventilation (fond) ---
vent_count = 5;
vent_w = 2.4;
vent_l = 22;
vent_pitch = 5;

// --- Fermeture capot : levre en press-fit (aucune vis sur le dessus) ---
lip_h       = 7;        // hauteur de la levre du capot qui plonge dans le bac
lip_clear   = 0.15;     // interference press-fit levre / paroi (PA-CF)

// --- Pieds silicone ---
foot_d = 12;
foot_recess = 0.8;
foot_inset = 15;

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
