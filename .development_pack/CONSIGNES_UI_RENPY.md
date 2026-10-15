# Consignes UI Ren'Py — pièges de positionnement à ne jamais refaire

## Règle d'or : positionnement vs alignement (source du bug)

Dans un écran Ren'Py, ces propriétés **s'excluent** sur le même axe. Les mélanger
provoque `keyword argument 'xalign' is incompatible with 'xpos'`.

Axe horizontal — choisir **UNE seule** approche :

- `xpos` (+ éventuellement `xanchor`)
- `xalign` (raccourci = `xpos` + `xanchor` à la même valeur)
- `xcenter`

Axe vertical — pareil : `ypos`(+`yanchor`) **ou** `yalign` **ou** `ycenter`.

Interdits (erreur immédiate) :

```renpy
text "x" xpos 30 xalign 0.5      # NON : xpos + xalign
text "x" ypos 10 yalign 0.5      # NON : ypos + yalign
```

### Bonnes pratiques

Centrer un texte dans une zone de largeur connue → `xpos` du centre + `xanchor 0.5` :

```renpy
# zone gauge à xpos 30, largeur 140 -> centre = 30 + 70 = 100
text "[pct]%" xpos 100 ypos 140 xanchor 0.5 yanchor 0.5
```

Centrer dans le parent complet → `xalign 0.5` **seul** (sans `xpos`) :

```renpy
text "Titre" xalign 0.5 ypos 20
```

Centrer horizontalement ET verticalement dans le parent → `align (0.5, 0.5)`
(ou `xalign 0.5 yalign 0.5`, jamais avec `xpos`/`ypos`).

Besoin de centrer dans une sous-zone décalée → mettre un conteneur positionné,
puis `xalign 0.5` **à l'intérieur** :

```renpy
fixed:
    xpos 30 ypos 70 xysize (140, 140)
    text "[pct]%" xalign 0.5 yalign 0.5   # centré DANS le fixed
```

## Autres pièges Ren'Py (screen language) à éviter

1. **Chemins d'images** : une string avec `/` doit inclure l'extension
   (`"hud/x/y.png"`), sinon image introuvable au runtime. Pas d'auto-`.png`.

2. **Texte = expression Python** commençant par `{` ou `[` → l'entourer de
   parenthèses, sinon confondu avec un tag/liste :
   `text ({"a": "A"}[k])` et non `text {"a": "A"}[k]`.

3. **Un seul `action` par bouton** (le second écrase le premier).
   Chaîner plusieurs actions avec une liste : `action [A, B]`.

4. **`on hover` / `on idle`** dans un transform ne réagit que sur un displayable
   focusable (button, bar). Sur un `fixed`/`add`, c'est ignoré → appliquer le
   transform au `button`, pas à son contenu.

5. **`Transform(..., size=(w,h))`** et **`xysize (w,h)`** redimensionnent ;
   `size=` accepte un tuple. `crop=(x,y,w,h)` recadre. En cas de doute sur un
   recadrage figé, préférer `im.Scale(im.Crop(...))` (fiable).

6. **Teinte d'un PNG blanc** : `matrixcolor TintMatrix("#RRGGBB")` (ATL) ou
   `Transform(img, matrixcolor=TintMatrix(c))`.

7. **`grid r c`** exige exactement `r*c` enfants ; pour un nombre variable
   utiliser `vpgrid cols N` (accepte un `for`/`if`).

8. **Écrans `tag menu`** : ouvrir via `ShowMenu("nom")`, fermer via `Return()`.
   Écrans overlay/HUD (Show-based) : ouvrir via `Show`, fermer via `Hide`.
   Ne pas mélanger `Return()` avec un écran ouvert par `Show`.

9. **`config.overlay_screens.append("nom")`** dans un `init` pour un HUD
   permanent ; garder l'écran conditionné (`if not main_menu ...`).

10. **`persistent.*`** = partagé entre toutes les sauvegardes ;
    `default var` = par sauvegarde. Choisir selon le besoin.

## Réflexe de vérification avant de livrer un écran

Grep systématique des conflits de positionnement sur les fichiers modifiés :

```bash
grep -nE "(xpos .*xalign|xalign .*xpos|ypos .*yalign|yalign .*ypos)" game/*.rpy
```

Aucun résultat attendu.

## Erreur Ren'Py — `hotspot` en dehors d'une `imagemap` (15 octobre 2026)

**Symptôme réel :** `IndexError: list index out of range` dans `renpy.sl2.slast.py`, sur `imc = renpy.ui.imagemap_stack[-1]`, lorsque le screen exécute un `hotspot` dans un simple `fixed`.

**Cause :** le langage screen de Ren'Py exige que `hotspot` soit enfant d'un bloc `imagemap:` comportant `ground` (et, normalement, `hover`). Un `fixed:` ne crée pas de contexte imagemap.

**Solution impérative :** utiliser un `button:` transparent avec `xpos`, `ypos`, `xsize`, `ysize`, `background None` et `action` pour une zone de clic invisible sur une image `add`. N'utiliser `hotspot` qu'au sein d'un `imagemap:` explicitement défini.

**Contrôle avant commit :** rechercher chaque `hotspot` ajouté/modifié et vérifier son parent réel ; vérifier également qu'un seul `screen nom_ecran` existe dans tout `game/`, car les définitions en double peuvent masquer l'implémentation voulue.

**Exemple sûr :**

```renpy
fixed:
    add "images/ui/tablette/tablette_4.png"
    button:
        xpos 1200 ypos 700
        xsize 150 ysize 90
        background None
        action Hide("tablet_home")
```

## Tablette : transitions et imagebuttons (15 octobre 2026)

- **Ne pas créer de boutons rectangulaires Solid derrière/sur les icônes** lorsque des fichiers d'icône dédiés existent. Utiliser `imagebutton:` avec `idle`, `hover`, `focus_mask True` et l'asset réel (`images/ui/tablette/exit.png`, `discord.png`). Les clics suivent les pixels opaques, et non un carré recouvrant un autre bouton.
- Pour une animation `tablette_1` à `tablette_4`, **ne jamais effacer le calque précédent avant le fondu** : dessiner l'étape de départ en dessous à opacité 100 %, puis l'étape suivante avec `alpha 0.0; linear duration alpha 1.0` au-dessus. Cette technique est un vrai fondu croisé, aussi à la fermeture.
- Durées demandées : 0,3 s pour les phases normales et 0,2 s pour 3→4 (et 4→3). Synchroniser la durée d'affichage par phase et le transform de fondu.
- Les PNG de tablette restent dans un repère commun 1920×1080 avec `fit "contain"`. Relever la position effective des icônes sur une capture *du jeu* avant de fixer leurs `xpos`/`ypos` : ne jamais déduire les coordonnées de la taille native seule.
- L'écran modal lancé par `Show("tablet_home")` doit déclencher un parcours inverse complet via `closing=True`, puis `Hide("tablet_home")`. La touche Échap et le bouton Exit utilisent la même action.
- Vérifier qu'il n'existe qu'un `screen tablet_home` actif, et tester en Ren'Py : quatre images, fondu continu, Exit cliquable, Échap et Discord.

## Imagebuttons dont les clics ne répondent pas (15 octobre 2026)

- **Erreur avérée sous Ren'Py 8.3.7 :** `focus_mask False` provoque `Exception: Focus_mask must be None, True, a displayable, or a callable.` La valeur `False` n'est jamais valide : supprimer la ligne pour garder `None` par défaut. `focus_mask True` n'est **pas** systématiquement approprié : si le PNG contient des marges transparentes ou un cadrage différent de l'écran, le bouton peut ne jamais capter le clic sur sa zone apparente. Pour les images de boutons d'une tablette, définir explicitement `xsize`/`ysize`, omettre entièrement `focus_mask` (valeur implicite `None`), et conserver les vrais assets `idle`/`hover` sans fonds Solid parasites.
- Les images-boutons et l'image de fond doivent être des enfants du **même conteneur de référence** (1920×1080) et utiliser des dimensions d'affichage cohérentes ; si la phase 4 apparaît via `tablet_phase_fade(0.2)`, appliquer aussi cette entrée aux `imagebutton` affichés à ce moment.
- Ne jamais supposer qu'un `imagebutton` devient cliquable uniquement parce que son PNG est visible : tester la position, le focus, puis le déclenchement de l'action de fermeture et du lien.

## Application Messagerie — habillage intégré (15 octobre 2026)

- Le cadre et la perspective de la tablette proviennent de `images/ui/tablette/tablette_messagerie.png` : placer tous les composants dans le `fixed at messenger_panel_in, messenger_tablet_plane` existant, en conservant son repère 940×560. Ne pas dessiner une fenêtre droite supplémentaire par-dessus l'illustration.
- **Ne pas masquer les emplacements vides** du visuel `tablette_messagerie.png` avec de grands rectangles `Solid`. Le PNG contient déjà les bordures de la colonne gauche : ne remplir que les cases réellement utilisées avec portraits et textes, et laisser les autres cases sans surcouche. Aucun panneau « CONVERSATIONS », compteur ou cartouche de statut inventé sur ces cases.
- Pour une messagerie narrative, afficher les **quatre derniers messages révélés** avec bulles différenciées ; placer leur liste dans un `viewport` borné, avec molette, en réservant une hauteur explicite à chaque ligne de message afin d'empêcher les chevauchements même avec des textes longs. Le viewport commence sous la ligne d'en-tête et s'arrête avant la barre inférieure du PNG.
- Ne pas détruire la mécanique de révélation : `messenger_advance()` reste déclenchée au clic/Entrée/Espace ; une retouche graphique ne doit pas changer les messages ni leur ordre.
- L'écran `messenger_objective_gate` est ouvert via `call screen` : son timer de `Return(True)` doit rester **en dehors** du bloc `if messenger_objective_active`, sinon il peut disparaître précisément quand le statut passe à faux et bloquer la reprise du scénario. La carte d'objectif, elle, doit être masquée pendant l'ouverture de `tablet_home` et `messenger_conversation`.
- Vérifier après retouche : l'image n'est pas déformée, 1 à 4 messages courts, quatre messages longs, plusieurs messages consécutifs du même auteur, fermeture complète et retour au scénario. Exécuter le lint Ren'Py si le SDK est accessible ; ne pas prétendre l'avoir exécuté autrement.

## Correction du positionnement de la Messagerie (15 octobre 2026)

- **Retours de capture** : titre secondaire « CANAL PRIVÉ » traversé par le trait cyan, surcouche sombre de la colonne gauche, doublon de cadre autour de la carte active, bandeau inférieur noir, portraits collés à la bordure et messages pouvant paraître sur la même ligne.
- **Implémentation** : conserver le `fixed` 940×560 transformé unique ; mettre les titres dans la bande haute (y=10 et 37), la seule fiche du correspondant dans sa carte dessinée (y≈69), le portrait d'en-tête dans le cadre du PNG, commencer le `viewport` après l'en-tête (y≈146) et garder sa bordure droite avant la fausse barre dessinée ; laisser toutes les cases inutilisées intactes ; placer l'indication de progression directement dans la zone de pied de page sans rectangle de fond.
- Chaque ligne dans le `vbox` des messages possède un `fixed` de hauteur dimensionnée selon la longueur du texte (`messenger_message_row_height`) pour que des messages successifs ne se superposent pas. C'est une estimation prudente : vérifier en jeu les langues et les messages particulièrement longs, car le reflow exact dépend de la police.
- Avant de déclarer l'interface terminée : vérifier la perspective sur capture réelle, les bulles en début/milieu/fin d'échange, la molette, le dernier message, la touche Entrée et le clic ; effectuer un lint avec le SDK Ren'Py 8.3.7 si accessible.

## Retouche tablette : inclinaison et portraits d'en-tête (15 octobre 2026)

- **Capture réelle** : les bulles et leur texte paraissaient moins inclinés que les bordures cyan déjà dessinées dans `tablette_messagerie.png`. Ajustement ciblé du **transform commun** `messenger_tablet_plane` (rotation de 8° à 9,6°, position verticale ajustée), jamais de rotation individuelle des bulles ou portraits.
- Une rotation 2D est une **approximation** d'une image dessinée en perspective, pas une homographie. Ne pas affirmer que les quatre coins sont parfaitement alignés sans comparaison dans Ren'Py. Si un écart résiduel persiste dans les coins, préparer une vraie transformation projective plutôt que multiplier les décalages individuels.
- Les PNG `images/character/<id>/portrait.png` montrent une portion importante du buste, ce qui rend le visage très petit dans une vignette. Recadrer le haut du portrait via `messenger_header_portrait` (crop carré 72 % de son petit côté, centré horizontalement, proche du haut), puis redimensionner à **68×68** (carte de gauche) et **76×76** (en-tête de discussion). Ne pas appliquer ce recadrage aux petits avatars des bulles.
- Mettre en cache les recadrages pour ne pas rappeler `renpy.image_size` en permanence. En cas d'image absente ou de dimensions invalides, conserver le portrait original via le fallback au lieu de bloquer l'écran.
- Sur chaque nouvelle capture, comparer l'inclinaison d'une bulle à la ligne cyan située **à la même hauteur** et vérifier que les portraits agrandis restent strictement dans les cadres du PNG. Ne pas supprimer l'historique, les fonctions de progression ou l'évènement de fin de conversation pendant ces ajustements.

## Calibrage du flux des messages — correction du 15 octobre 2026

- Ne jamais dimensionner les lignes de conversation avec une estimation de caractères (`messenger_message_row_height`) : les métriques de Rajdhani et les retours à la ligne réels ne coïncident pas avec ce calcul, ce qui crée des écarts imprévisibles entre les bulles. Placer directement les `hbox` dans le `vbox` du `viewport` et laisser Ren'Py calculer leur hauteur naturelle ; conserver `spacing` constant.
- Calibrer les éléments dans le même repère `messenger_tablet_plane` sans transformer les portraits et textes séparément. Sur la dernière capture, rotation ajustée de 9,6° à 9,3° et origine Y de 0,437 à 0,441 ; viewport déplacé au repère (293,147), en-tête légèrement recentré, libellé de pied de page descendu à Y=522.
- Ces changements sont des ajustements **de placement**, pas une transformation projective. Sans capture générée directement par Ren'Py après la modification, ne pas annoncer un alignement géométrique parfait.

## Placement selon flèches de capture (15 octobre 2026)

- Les flèches annotées sur la capture de la messagerie imposent des **déplacements ciblés** et non une nouvelle modification de `rotate` : le plan général reste à 9,3°.
- Recentrer les portraits **dans les cadres dessinés** en haut à gauche et dans l'en-tête ; décaler le nom du correspondant et son statut nettement vers la droite pour leur laisser de l'air.
- Déplacer la zone de bulles légèrement vers la droite et vers le bas, en réduisant sa hauteur pour protéger la zone du pied de page, et décaler également l'instruction de progression vers la droite.
- Conserver le rendu des bulles, leurs dimensions naturelles, la révélation par clic, l'ordre narratif et la barre de défilement. Les marges sont dans le repère local 940×560 **avant** transformation, pas dans les pixels bruts de la capture.
