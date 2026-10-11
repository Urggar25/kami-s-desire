# Critical choices & Story Packs (prototype)

## L'Origine

Story Pack 01: **L'Origine** — story content from day 5 to day 30, with seven advertised endings. Its main-menu button starts `origine_story_pack_teaser`, an in-engine, approximately 30-second cinematic assembled from existing game images. It is **not an encoded MP4**.

## Route metadata

Each `menu (screen="critical_choice", ...)` can pass `cc_targets`, a dictionary from the untranslated choice caption to `{"label": "label_name", "pack": "origine"}`.

- `cc_option_status` checks an explicit unfinished-label list and `renpy.has_label`.
- Missing/unwritten routes appear greyed out with a vector padlock; selecting them has no effect.
- Owned routes retain a discreet Story Pack badge.
- Unowned, implemented pack routes show a modal with the pack name, story span, endings and teaser information.
- Future DLC should get its own ID and metadata; do not assign unimplemented routes to a live DLC.

**Commercial warning:** `cc_owned_packs` defaults to including `origine` in the current development build so existing testers do not lose access. A value set in `persistent` is not a secure purchase record. Before charging money, integrate a platform entitlement check and gate entry to premium narratives (not just their internal decisions). The teaser is playable in Ren'Py but a separate MP4 export has not been produced.

## Maintenance

Update `CC_UNFINISHED_LABELS` whenever a placeholder route is created or completed. Label existence is **not** sufficient evidence a route is finished. Audit every new critical menu and add its `cc_targets`. Re-test save/load, translations and menus in Ren'Py before release.
