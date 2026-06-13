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

### 3. Le PCB avec **les vraies empreintes**

Le `.kicad_pcb` a été généré via l'**API pcbnew de KiCad 10** : chaque
composant utilise sa **vraie empreinte** chargée depuis les bibliothèques
KiCad installées, placée et connectée aux nets.

| Réf | Composant | Empreinte réelle |
|---|---|---|
| U1 | ESP32-S3 DevKitC-1 | **`Espressif:ESP32-S3-DevKitC`** (empreinte officielle Espressif, 2×22 pins, brochage GPIO exact) |
| U2 | PCM5102 DAC | `PinHeader_2x06` |
| U3 | PAM8403 ampli | `PinHeader_1x07` |
| U4 | INMP441 MEMS | `PinHeader_1x06` |
| U5 | AMS1117-3.3 | `Package_TO_SOT_SMD:SOT-223-3_TabPin2` |
| DS1 | Anneau WS2812 | `PinHeader_1x03` |
| SW1 | Encodeur EC11 | `Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm` |
| SW2 | Switch mute | `Button_Switch_THT:SW_DIP_SPSTx01_Slide` |
| J1 | Jack 3.5 mm | `Connector_Audio:Jack_3.5mm_PJ320E_Horizontal` (avec contact détection R2) |
| J2 | USB-C | `Connector_USB:USB_C_Receptacle_Amphenol_12401610E4-2A` |
| Q1 | AO3401 P-MOS | `Package_TO_SOT_SMD:SOT-23` |
| F1 | Ferrite | `Inductor_SMD:L_0805_2012Metric` |
| R1, R2 | Résistances | `Resistor_SMD:R_0603_1608Metric` |
| C1–C4 | Céramiques | `Capacitor_SMD:C_0603_1608Metric` |
| C5, C6 | Électrolytiques | `Capacitor_SMD:CP_Elec_5x5.3` |
| HP1, HP2 | Haut-parleurs | `PinHeader_1x02` |

**Validé avec `kicad-cli pcb drc` : 0 erreur.** Les 76 « éléments non
connectés » sont le **ratsnest** (liaisons à router) — c'est l'état normal
d'un PCB non encore routé. Ouvre le **PCB Editor**, tu vois les 22 empreintes
placées avec le chevelu (ratsnest) prêt à router.

Le schéma porte les mêmes empreintes (`Footprint` property), donc
`Tools → Update PCB from Schematic (F8)` fonctionne aussi si tu modifies le
schéma.

> **Note** : les modules (ESP32 DevKitC, PCM5102, PAM8403, INMP441, anneau
> WS2812) sont représentés par des **barrettes de connexion** — c'est la
> manière correcte de les intégrer (on les enfiche sur des barrettes femelles).
> La contrainte d'isolation au contour est réglée à 0,25 mm pour l'USB-C
> (connecteur de bord).

Régénérer le PCB : `"C:\Program Files\KiCad\10.0\bin\python.exe" build_pcb.py`

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
