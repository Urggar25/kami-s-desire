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
