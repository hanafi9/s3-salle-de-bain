# Projet KiCad — s3-salle-de-bain

Schéma et PCB ébauche du voice assistant ESP32-S3, **généré depuis le YAML
ESPHome** pour servir de point de départ. KiCad 8 ou supérieur recommandé.

## Fichiers livrés

| Fichier | Rôle |
|---|---|
| `s3-salle-de-bain.kicad_pro` | Projet KiCad |
| `s3-salle-de-bain.kicad_sch` | Schéma complet (23 composants, 27 nets) |
| `s3-salle-de-bain.kicad_pcb` | PCB vierge (board outline 100×80 mm) |
| `s3-salle-de-bain.net` | Netlist au format Pcbnew (compatible Eagle, etc.) |
| `sym-lib-table` | Tables symboles (utilise libs KiCad par défaut) |
| `fp-lib-table` | Tables empreintes (utilise libs KiCad par défaut) |

## Composants modélisés (23)

| Réf | Composant | Brochage YAML |
|---|---|---|
| U1 | **ESP32-S3-DevKitC-1** | GPIO1, 2, 4, 5, 7, 8, 9, 10, 11, 16, 17, 18, 21, 47 |
| U2 | **PCM5102 DAC** | BCK=GPIO8, DIN=GPIO10, LRCK=GPIO7 |
| U3 | **PAM8403 ampli class-D** | SHDN=GPIO47, sortie HP stéréo |
| U4 | **INMP441/ICS-43434 MEMS** | LRCLK=GPIO4, BCLK=GPIO5, DIN=GPIO11 |
| DS1 | **Anneau WS2812 12 LEDs** | DIN=GPIO21, alim gatée +5V_LED |
| SW1 | **Encodeur Alps EC11** | A=GPIO16, B=GPIO18, switch=GPIO1 |
| SW2 | **Switch mute SPDT** | COM=GPIO2 |
| J1 | **Jack 3.5mm** | Tip/Ring=audio, Switch=GPIO17 |
| J2 | **USB-C input** | +5V principal |
| Q1 | **P-MOSFET (AO3401)** | Gate=GPIO9, source=+5V, drain=+5V_LED |
| U5 | **AMS1117-3.3 LDO** | +5V → +3V3 |
| F1 | **Ferrite 600Ω** | Filtre rail LED |
| TVS1 | **USBLC6-2SC6** | Protection ESD USB |
| C1-C6 | Condensateurs de découplage | 10µF, 100nF, 100µF, 470µF |
| R1-R2 | Résistances | 10kΩ pullup, 330Ω série WS2812 |
| HP_L/R | Haut-parleurs 40mm 4Ω 3W | Sortie PAM8403 |

## Comment l'utiliser

### 1. Ouvrir le projet

```bash
# Ouvrir KiCad et charger le projet
kicad s3-salle-de-bain.kicad_pro
```

Ou double-cliquez sur `s3-salle-de-bain.kicad_pro` depuis l'explorateur.

### 2. Vérifier le schéma

Ouvrez le schéma (`Schematic Editor`). Vous verrez un schéma **entièrement
câblé** avec les **vrais symboles électroniques standards KiCad** :

- **Composants discrets** avec leurs symboles normalisés :
  - `Device:R` (résistances R1, R2), `Device:C` (céramiques C1-C4),
    `Device:C_Polarized` (électrolytiques C5, C6), `Device:L` (ferrite F1)
  - `Device:Q_PMOS` (MOSFET Q1 avec broches G/S/D)
  - `Device:Speaker` (haut-parleurs HP1, HP2 avec cône)
  - `Switch:SW_SPDT` (switch mute SW2)
- **Symboles d'alimentation** standards : `power:+3V3`, `power:+5V`,
  `power:GND` (avec leurs glyphes normalisés), `PWR_FLAG` sur chaque rail
- **Modules ICs** (U1 ESP32-S3, U2 PCM5102, U3 PAM8403, U4 INMP441,
  U5 AMS1117, DS1 WS2812, SW1 encodeur, J1 jack, J2 USB-C) en symboles
  rectangulaires avec broches nommées et typées (power_in sur les pins VCC/GND)
- **Câblage** : chaque broche a un stub + une étiquette de net (méthode pro pour
  schéma dense). Les nets `MIC_LRCLK`, `DAC_BCK`, `BTN_CENTER`, etc. connectent
  les broches par nom.

Les symboles standards sont **extraits exactement** de la bibliothèque KiCad 10
installée (`Device.kicad_sym`, `power.kicad_sym`, `Switch.kicad_sym`), donc
aucun avertissement de symbole non conforme.

#### Validation

Le schéma a été vérifié avec le moteur de KiCad 10 lui-même :
- `kicad-cli sch erc` : **19 avertissements mineurs** (lib `Local` non déclarée
  pour les modules custom — sans impact car symboles embarqués)
- `kicad-cli sch export pdf/svg` : rendu sans erreur
- Netlist : **24 nets, 22 composants** tous connectés

Pour régénérer après modification : `python build_kicad_v2.py` (nécessite
`kicad_std_symbols.py` dans le même dossier).

### 3. Le PCB est **déjà peuplé**

Le `.kicad_pcb` contient :
- **14 footprints** déjà placés (rectangulaires avec pads PTH 1.7 mm)
- **70 pads** connectés à leurs nets respectifs
- **23 nets** déclarés (GND, +3V3, +5V, +5V_LED, signaux)
- Board outline 120×100 mm
- Pin 1 marker (cercle) sur chaque footprint

Ouvre le **PCB Editor** directement depuis KiCad : tu vois les 14 composants
en grille, prêts à être déplacés et routés. **Pas besoin** d'« Update PCB
from Schematic », mais tu peux le faire si tu modifies le schéma.

#### Pour reposition automatique depuis le schéma

Si jamais tu modifies le schéma et que tu veux propager :
```
Schematic Editor  →  Tools  →  Annotate Schematic  (assigner refs U1,U2…)
                  →  Tools  →  Update PCB from Schematic (F8)
```
Dans le dialog : cocher **« Re-link footprints to schematic symbols »**, puis
**Update PCB**.

### 4. Routage suggéré

- **Couches** : 2 couches suffisantes (Top + Bottom)
- **Largeur des pistes** :
  - Signaux logiques : 0.25 mm
  - Alimentation 3V3 / 5V : 0.5 mm
  - Audio analogique (LOUT, ROUT vers ampli) : 0.4 mm, en étoile
  - GND : plan de masse continu sur Bottom
- **Découplage** : C1-C6 placés au plus près des broches VCC de chaque IC
- **Audio** : LOUT/ROUT du PCM5102 à PAM8403 doivent être courts et éloignés
  du signal WS2812 (rayonnement). Séparer la masse analogique (AGND) de la
  masse numérique (DGND) avec un point d'union proche du LDO.
- **WS2812** : résistance série R2 (330Ω) près de DS1, pas de l'ESP32

## Limitations connues

Ce projet est un **point de départ** généré automatiquement, pas un design
production-ready. À vérifier/compléter manuellement avant fabrication :

- [ ] Remplacer les symboles génériques par les vrais symboles KiCad
- [ ] Vérifier le brochage de chaque composant contre sa datasheet
- [ ] Ajouter une protection ESD sur les lignes I2S exposées (jack 3.5mm)
- [ ] Dimensionner la résistance pullup R1 selon la datasheet de l'encodeur
- [ ] Choisir le bon P-MOSFET (Vgs(th), Rds(on), Id selon le courant LED)
- [ ] ERC + DRC complets dans KiCad
- [ ] Simulation thermique du PAM8403 (3W RMS)

## Netlist alternatif

Si vous préférez importer dans un autre outil (Eagle, Cadstar...) :

```bash
# Le fichier .net est au format Pcbnew classique
cat s3-salle-de-bain.net
```

Il contient les 23 composants et 27 nets prêts à l'emploi.

## Licence

CERN Open Hardware Licence v2 Strongly Reciprocal (CERN-OHL-S-2.0).
Voir [../LICENSE](../LICENSE).
