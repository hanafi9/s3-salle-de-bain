# Boîtier v4 — « galet rectangulaire arrondi »

Boîtier **conçu pour la carte porteuse KiCad 76,7 × 108 mm** de ce dépôt
(implantation relue directement depuis `s3-salle-de-bain.kicad_pcb`, version
exportée pour JLCPCB). Remplace l'ancien boîtier cylindrique Ø110 mm, désormais
en *legacy* dans `cad/`. Design *classe & épuré* : galet compact à coins
arrondis, molette centrée, haut-parleurs en façade, **dessus sans vis**.

![Aperçu](boitier_v4_apercu.png)

## Pièces

| Fichier | Rôle | Matière conseillée |
|---|---|---|
| `v4_base.stl` / `.step` | Bac (parois, façade HP, USB-C, entretoises PCB) | PA-CF |
| `v4_top.stl` / `.step` | Capot (molette, anneau LED, micro, lèvre) | PA-CF |
| `v4_speaker_gasket.stl` / `.step` | 2 joints d'enceinte (compression) | TPU 95A |

Les `.scad` sont paramétriques : tout est piloté par **`params.scad`**.
`v4_assembly.scad` (éclaté) et `v4_section.scad` (coupe) sont des vues de
contrôle, pas des pièces à imprimer.

### Fichiers STEP (CAO / partage fabricant)

OpenSCAD **n'exporte pas le STEP** (géométrie maillée, pas de B-rep). Les `.step`
fournis sont des **solides B-rep facettés** reconstruits depuis les STL via
FreeCAD (`stl_to_step.py`). Ils sont valides et fermés (un solide chacun, sauf
le joint = 2 solides), donc importables dans tout MCAD ou chez un fabricant.

> ⚠️ `v4_base.step` est volumineux (~22 Mo) : les grilles hexagonales génèrent
> ~24 000 faces planes. `v4_top.step` (~3 Mo) et `v4_speaker_gasket.step`
> (~2,4 Mo) sont légers. Pour ré-générer : `freecadcmd stl_to_step.py`.
> Pour de l'édition paramétrique, **privilégier les `.scad`**.

## Caractéristiques

- **Encombrement** : 121 × 90 × 57 mm — **carte** : 76,7 × 108 mm
- **Paroi / fond** : 2,6 / 3,0 mm · **rayon des coins** : 22 mm
- **Haut-parleurs** : 2 × 40 mm *front-firing*, grilles hexagonales + anneaux M2.5
- **Encodeur** : EC11 **monté sur le capot** (douille M7), relié par fil aux
  connecteurs `SW1` / `DS1` de la carte. *(Un EC11 soudé sur le PCB ne pourrait
  pas atteindre le dessus situé ~50 mm plus haut.)*
- **Anneau LED** WS2812 : Ø 60 / 44 mm, gorge diffuseur
- **Micro** : pinhole conique Ø 0,8 mm, placé **au-dessus du module INMP441**
- **USB-C** : découpe alignée sur le connecteur `J2` réel de la carte
- **Fermeture** : lèvre périphérique en **press-fit** (jeu 0,15 mm), aucune vis
  visible + encoche de démontage latérale
- **Fixation PCB** : 4 × M3 sur entretoises, alignées sur les **4 trous réels
  `MK1`–`MK4`** de la carte. Positions relues via `kicad/dump_pcb_geo.py` :
  PCB (73.37, 43.90) · (138.43, 44.28) · (138.43, 139.41) · (73.37, 137.90)

> Le boîtier est obtenu par **rotation −90°** de la carte (HP en façade +Y,
> USB-C à l'arrière −Y) ; le mapping carte→boîtier est documenté en tête de
> `params.scad`.

## Impression (RatRig V-Core 3 400, buse 0,4)

PA-CF, couche 0,2 mm, 4 périmètres, 5 couches dessus / dessous, remplissage
25 % gyroïde, **sans support** (lèvre et grilles auto-portées), bord (brim)
auto 8 mm. Buse 290 °C, plateau 100 °C, ventilation 10–30 %.

> Le projet OrcaSlicer prêt à trancher est fourni dans
> `cad/boitier_v4/boitier_v4.3mf` (mêmes réglages PA-CF que `boitier_base_optimise`).
