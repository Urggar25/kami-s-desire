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
