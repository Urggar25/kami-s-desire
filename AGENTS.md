# Consignes permanentes du dépôt

## Catalogue des mécaniques — lecture obligatoire

Avant toute modification du dépôt, lire intégralement [`MECANIQUES_JEU.md`](MECANIQUES_JEU.md).

Toute création, suppression, renommage ou modification significative d'une mécanique, d'un mini-jeu, d'un écran réutilisable, d'un effet visuel, d'un effet sonore ou d'un outil de dialogue doit être répercutée dans `MECANIQUES_JEU.md` dans la même modification.

Chaque entrée ajoutée au catalogue doit contenir :

- le nom de la mécanique, de l'effet ou de l'écran ;
- une description en une ligne ;
- le chemin du fichier source ;
- un exemple d'appel en une ligne.

Ne pas documenter comme API publique un sous-écran ou une fonction interne préfixée par `_`, sauf si son usage direct est explicitement prévu par le fichier source.

## Consignes Ren'Py existantes

Lire aussi `.development_pack/AGENT.md` avant toute modification d'un fichier `.rpy`. Pour toute écriture narrative, appliquer en plus `.development_pack/instruction.md`.

## Mise en scène dynamique (obligatoire pour toute scène écrite ou réécrite)

Référence : grammaire « procès » inspirée de Danganronpa / The Hundred Line, implémentée dans `game/kd_staging.rpy` et documentée dans `MECANIQUES_JEU.md` (section « Mise en scène procès »).

- **Rythme** : ne jamais rallonger les transitions standard. `dissolve` (0,2 s) et `fade` sont réglés globalement ; n'utiliser `Dissolve(x)`/`Fade(...)` long que pour une ellipse temporelle assumée (réveil, flash-back, fin de journée).
- **Caméra** : laisser l'autofocus cadrer les répliques. Ne pas remonter `CINEMA_ZOOM_BG` au-dessus de 1.67 (au-delà, sprites et décors 1536×1024 deviennent flous). Ne pas réactiver la caméra pilotée par la souris par défaut.
- **Personnages inactifs** : ils sont assombris par `matrixcolor`, jamais rendus transparents (`alpha` < 1 interdit pour un personnage présent).
- **Confrontations** : dans toute dispute, accusation ou révélation, prévoir au minimum un temps fort visuel toutes les 10 à 20 répliques, choisi dans cet ordre :
  1. `call cutin("tag")` juste avant la réplique d'accusation ou de rupture (réplique optionnelle en majuscules, toujours dans `_()` : `call cutin("mara", _("C'EST FAUX !"))`) ;
  2. `call reactions([...])` juste après une révélation qui touche plusieurs personnes présentes (2 à 4 visages, expressions cohérentes avec leurs répliques suivantes) ;
  3. `$ close_up("tag")` pour une réplique intime ou un aveu (relâché automatiquement au locuteur suivant) ;
  4. `$ punch_in()` ou `$ dutch()` pour une ponctuation ponctuelle.
- **Dosage** : pas plus d'un cut-in toutes les ~30 répliques dans une même scène, jamais deux d'affilée ; jamais de cut-in pendant une diffusion de Kami (`bg_diffusion_*`) ni sur un CG.
- **Ouverture de séance** : chaque nouveau débat ou vote au Conclave commence par `call trial_intro(subtitle=_("JOUR [current_day]")) from _call_...` placé juste après le `scene bg_conclave` et la musique.
- **Ponctuation automatique** : seuls `?!`, `!!`, `!!!` et les répliques criées en majuscules déclenchent secousse et son. Ne pas multiplier les `!` pour forcer un effet : utiliser `{shout}...{/shout}` ou un cut-in.
- **Texte** : mettre en valeur les indices, preuves et termes décisifs avec `{k}...{/k}` (sans en abuser : 1 à 2 par réplique maximum).
- **Nouveaux personnages** : ajouter leur couleur dans `KD_CHARACTER_COLORS` et leur cadrage de visage dans `KD_FACE_BOX` (`game/kd_staging.rpy`).
- **Traductions** : toute chaîne affichée par ces outils (réplique de cut-in, titre de séance) doit être marquée `_()` et ajoutée dans `game/tl/<langue>/kd_staging.rpy` pour l'anglais, le chinois et le portugais.

## Vérification Ren'Py

- Lint obligatoire après modification de `.rpy` : `renpy.sh <projet> lint`. Si le lint signale « Line with id … appears twice » sans que le texte ait été dupliqué, il s'agit de `.rpyc` périmés : lancer « Force Recompile » depuis le launcher (ou `renpy.sh <projet> compile`) puis relancer le lint.
