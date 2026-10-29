# DLC « Les autres vies » — route Doppelgänger

Ce dossier contient le contenu additionnel des jours 20 à 30. Ne pas inclure ces fichiers dans la distribution gratuite.

- `pack.rpy` : marqueur d'installation et déclarations des images déplacées.
- `scenario/20_ending_la_peau_des_autres.rpy` : épilogue explicatif du jour 20, retiré de la version gratuite.
- `scenario/21_*.rpy` à `scenario/30_*.rpy` : embranchements et fins payants.
- `stat_dialogues_21_30.rpy`, `doppelganger_character_interludes_21_30.rpy` et `optional_route_encounters_j21_j24.rpy` : scènes complémentaires exclusives.
- `images/cg/` et `images/background/` : CG et décors réservés à cette extension.

## Construction

`game/dlc_build.rpy` classe ce dossier dans la liste `kd_doppelganger_routes` ; les distributions normales `pc`, `win` et `mac` n'embarquent pas ces sources. Le paquet `doppelganger-routes` est généré par le constructeur Ren'Py comme archive DLC. Vérifier le contenu des deux paquets avant publication.

**Important :** effacer les anciens .rpyc compilés de `game/scenario/` et de toute précédente distribution avant la construction. Un ancien `21_*.rpyc` copié avec la base contournerait la séparation du contenu. Ne pas distribuer de build réalisé avec des caches obsolètes.

## Parcours d'essai

1. Sans pack installé, atteindre le choix du couteau J20. « Garder le couteau » est la route gratuite ; « Lâcher le couteau » affiche le verrou.
2. La réussite du QTE J20 débouche sur la fin gratuite « Derrière la grille » : pas de révélation du laboratoire.
3. En cas d'échec du QTE, l'édition gratuite propose de recommencer la séquence ; l'extension permet de poursuivre la branche.
4. Avec pack installé, le choix « Lâcher le couteau » est accessible, de même que les jours 21–30.
5. Après la fin gratuite, les acheteurs peuvent voir l'épilogue « La peau des autres ».
6. Depuis le menu principal, l'entrée « DLC » renseigne l'état de l'extension et ouvre la galerie et les souvenirs lorsqu'elle est présente.

La présence des scripts du pack sert de droit d'accès technique dans la version distribuée : il ne s'agit ni d'une validation serveur ni d'un DRM. Pour Steam ou une boutique imposant la vérification de licence, raccorder `kd_dlc_unlocked` à l'API de licence correspondante et conserver la séparation des fichiers.
