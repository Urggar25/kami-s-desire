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
