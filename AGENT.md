## Ren'Py Script Safety

- Do not replace a called screen with `show text` plus ATL text properties. In Ren'Py, `show text "..."` does not accept text style properties like `size`, `color`, or `font` inside the ATL block. Use `show expression Text("...", size=..., color=..., font=...) as name at truecenter`, a dedicated screen, or an existing screen pattern instead.
- After editing `.rpy` files, run the Ren'Py lint command before reporting completion, and treat syntax warnings/errors as blockers.
- Be careful with screens that contain `Return()` actions. Only use them through `call screen`; persistent overlays shown with `show screen` must not rely on `Return()`.
- Do not open in-game HUD or tablet overlays with `ShowMenu()` if their close button uses `Return()`. Use `Show("screen_name")` and close with `Hide("screen_name")`. Reserve `ShowMenu()`/`Return()` for true Ren'Py menu screens where returning to the menu context is intended.
- Automatic story transitions such as end-of-day cards, free-time cards, and title cards must not be implemented as `call screen` + timer `Return()`. Implement them as normal script flow (`scene black`, `show expression Text(...)`, `pause`, `hide`) so they cannot unwind to the main menu.
- Before adding or changing a screen, check how it is opened. If it is opened by `show screen`, `Show(...)`, or `ShowMenu(...)`, it must close with `Hide(...)`, `ShowMenu(...)`, or an explicit `Jump(...)`, never a bare `Return()`. Use `Return(value)` only for screens that are exclusively reached by `call screen` and whose caller immediately consumes `_return`.
