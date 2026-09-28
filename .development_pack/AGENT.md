## Ren'Py Script Safety

- Do not replace a called screen with `show text` plus ATL text properties. In Ren'Py, `show text "..."` does not accept text style properties like `size`, `color`, or `font` inside the ATL block. Use `show expression Text("...", size=..., color=..., font=...) as name at truecenter`, a dedicated screen, or an existing screen pattern instead.
- After editing `.rpy` files, run the Ren'Py lint command before reporting completion, and treat syntax warnings/errors as blockers.
- Be careful with screens that contain `Return()` actions. Only use them through `call screen`; persistent overlays shown with `show screen` must not rely on `Return()`.
- Do not open in-game HUD or tablet overlays with `ShowMenu()` if their close button uses `Return()`. Use `Show("screen_name")` and close with `Hide("screen_name")`. Reserve `ShowMenu()`/`Return()` for true Ren'Py menu screens where returning to the menu context is intended.
- Automatic story transitions such as end-of-day cards, free-time cards, and title cards must not be implemented as `call screen` + timer `Return()`. Implement them as normal script flow (`scene black`, `show expression Text(...)`, `pause`, `hide`) so they cannot unwind to the main menu.
- Before adding or changing a screen, check how it is opened. If it is opened by `show screen`, `Show(...)`, or `ShowMenu(...)`, it must close with `Hide(...)`, `ShowMenu(...)`, or an explicit `Jump(...)`, never a bare `Return()`. Use `Return(value)` only for screens that are exclusively reached by `call screen` and whose caller immediately consumes `_return`.

## Exploration Modes

- Keep `free_time_active` and `exploration_libre_active` strictly separate.
- `free_time_active` is for social free-time scenes: character sprites on room screens, relationship interactions, voyeur/free-time events, room activities, and free-time endings.
- `exploration_libre_active` is for story exploration only: the player can choose rooms and click room objects/hotspots, but free-time characters, free-time activities, and `temps_libre_*` events must not appear.
- When a story needs a limited room walk, use `START_EXPLORATION_LIBRE(next_label=..., required_visits=..., allowed_rooms=..., title=...)` instead of `START_FREE_TIME`.
- Room screens may share object hotspots between both modes, but any social character button or free-time-only activity must stay guarded by `social_free_time_active()` rather than raw `free_time_active`.
- Character link progression is persistent through `persistent.character_link_progress` / `persistent.character_link_memories`; new games must sync from persistent progress so completed free-time events are not replayed as fresh progression.
- Codex/profile memory replay must use `link_replay_mode` so reviewing an unlocked memory returns to the Codex and does not consume a free-time slot or lower the current link progression.

## Character Buttons

- Character `imagebutton` sprites built from the registered images in `images.rpy` must follow the day-1 PNC placement convention: use `Transform(character_image(...), zoom=1.00)`, keep the character bottom-anchored with `yalign 1.00`, and adjust horizontal placement with `xalign`. Do not use a middle-screen `yalign` such as `0.30`, which makes the sprite float above the floor. Apply the same placement to both `idle` and `hover`, then verify the feet/lower crop against the bottom edge of the scene.
- This rule is mandatory for every talkable character shown during a story objective, corridor route, room objective, free-time interaction, or PNC screen. Never compensate for placement with a fractional `yalign`, a positive `ypos`, or different idle/hover geometry. Before completing any task that adds or changes a talkable character, audit every affected `character_image(...)` button and confirm both states use `zoom=1.00` and the button uses `yalign 1.00`; the task is incomplete while any legacy floating placement remains in scope.

## Diffusions de Kami

- Ne jamais utiliser `bg_diffusion_neutre` dans un scénario : cette image est le plateau vide de la diffusion, sans Kami. Choisir obligatoirement un `bg_diffusion_EXPRESSION` où Kami est visible.
- Tant qu'un décor `bg_diffusion_*` est actif, chaque personnage parlant autre que Kami doit être affiché avec `$ bc_show("nom", "expression")` avant son bloc de répliques, puis retiré avec `$ bc_hide()` à la fin de ce bloc. Ne pas superposer `showP` ou `showGroup` à une diffusion.
- Ne pas laisser un décor `bg_diffusion_*` derrière un échange prolongé entre représentants. Couper la diffusion, restaurer le décor du lieu et remettre les interlocuteurs en scène avec `showGroup`; ne relancer la diffusion que lorsque Kami reprend effectivement la parole.

## Scènes obscures et lampe torche

- Ne pas remplacer par `scene black` un lieu sombre que le joueur explore avec une lampe. Afficher le décor réel, appeler `$ flashlight_on()` pendant l'exploration, puis `$ flashlight_off()` dès que la lampe ou la scène sombre prend fin.
- L'effet « Image sous lampe » choisit automatiquement entre cinq parcours fermés du faisceau. Ne pas ajouter un mouvement de lampe concurrent dans le scénario ni peindre un faisceau fixe dans le fond utilisé sous cet effet.
- Conserver l'effet actif dans `bg_salle_goumi_cachee` et dans ses CG de révélation tant que la lampe est la source de lumière de la scène.
- Quand Noam explore seul un conduit, ne pas afficher son sprite : le décor est vu depuis son point de vue. Les accompagnateurs présents ou entendus peuvent rester affichés si le dialogue l'exige.

## Rangement des décors et des CG

- Les fonds narratifs non interactifs vont dans `game/images/background/scenes/`.
- Toute illustration spéciale à collectionner va dans `game/images/background/cg/`, suit l'identifiant `bg_cgNNN`, et doit appeler `$ unlock_gallery_image("bg_cgNNN")` lors de sa première apparition.

## Changements de période

- Un passage de matin à après-midi, soir ou nuit se fait par une affectation de `current_period`. Le HUD détecte ce changement et joue sa transition locale en haut à droite.
- Ne pas utiliser `show_custom_title`, `centered`, `show text` ni un écran plein écran pour annoncer uniquement une période de la journée.
