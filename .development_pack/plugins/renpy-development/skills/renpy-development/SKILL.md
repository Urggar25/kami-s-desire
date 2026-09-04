---
name: renpy-development
description: Use when working on Ren'Py visual novel projects, including `.rpy` scripts, labels, dialogue, choices, screens, ATL transforms, images, audio, builds, lint output, or save-compatible gameplay changes.
---

# Ren'Py Development

## When to use this skill

Use this skill whenever the user asks Codex to create, edit, review, debug, or explain a Ren'Py project. Ren'Py projects usually contain `.rpy` files, a `game/` directory, `script.rpy`, `screens.rpy`, `options.rpy`, `gui.rpy`, and asset folders such as `images/`, `audio/`, or `gui/`.

## Project discovery

1. Locate the Ren'Py project root by looking for a `game/` directory and common files such as `game/script.rpy`, `game/screens.rpy`, `game/options.rpy`, or `game/gui.rpy`.
2. Read nearby `.rpy` files before editing so new code matches existing label names, character definitions, indentation, style prefixes, image naming, and screen patterns.
3. Check for project-specific conventions in `README`, `CONTRIBUTING`, comments near edited code, or custom helper files under `game/`.
4. If the project includes generated or translated files, avoid editing them unless the user specifically asks.

## Editing rules

- Preserve Ren'Py's indentation-sensitive syntax. Do not reformat whole files for unrelated changes.
- Keep labels stable unless the user requests a rename. Label changes can break jumps, calls, saves, translations, and persistent data.
- Avoid changing save-affecting defaults, persistent keys, or variable initialization behavior without calling it out.
- Prefer `default` for save-aware variables and `define` for constants, characters, images, and config values.
- Keep Python blocks small and explicit. Use `init python:` for startup helpers and ordinary `python:` blocks for runtime logic only when needed.
- Add new assets using existing directory and naming conventions. Reference assets with Ren'Py image names or relative paths already used by the project.
- For dialogue and menus, preserve the existing voice, punctuation style, and character identifiers.
- For screens, match the local style system and use predictable `screen`, `use`, `tag`, `modal`, `key`, and `action` patterns.
- For ATL, transforms, and transitions, favor readable timings and named transforms when reused.

## Review checklist

When reviewing or debugging Ren'Py code, check:

- Missing labels, broken `jump` or `call` targets, and call stack issues from missing `return`.
- Variables used before `default` or initialization.
- Incorrect indentation after labels, menus, screens, Python blocks, and ATL blocks.
- Screen actions that reference missing screens, variables, labels, or functions.
- Image, audio, font, and GUI paths that do not exist under `game/`.
- Duplicate labels, duplicate image definitions, or conflicting screen names.
- Python code that may run at init time accidentally.
- Changes that could break old saves or translations.

## Verification

Prefer project-provided checks first. If available, run the repository's scripts or documented commands. Common Ren'Py checks include:

- Ren'Py launcher lint for script, image, screen, and translation issues.
- A Ren'Py SDK command-line lint invocation when the SDK path is known.
- Existing unit tests, smoke tests, or CI commands if the project defines them.

If Ren'Py itself is not installed or its path is unknown, still perform static checks by reading changed `.rpy` files, searching references with `rg`, and reporting that runtime lint was not run.

## Response style

Explain Ren'Py-specific risks plainly, especially save compatibility, missing asset references, and label/screen flow. When a change is complete, mention the files touched and whether lint or runtime verification was possible.
