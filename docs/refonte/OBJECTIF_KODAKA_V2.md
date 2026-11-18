# Refonte Kodaka V2 — toutes les routes à partir du jour 4

Date de lancement : 19 novembre 2026. Référence GitHub : 047134bf2377292c42851632c411bc0393d2e2ad.

## Objectif

Réécrire les journées et leurs scènes annexes à partir du jour 4 pour obtenir des conversations orales, vivantes et caractérisées, une cohabitation crédible et une mise en scène expressive. Le périmètre comprend les routes gratuites et le DLC. Les branches incomplètes font partie du chantier ; leur achèvement ne doit pas être confondu avec la réécriture de contenu existant.

La référence d'écriture choisie par l'utilisateur est **prompt_kodaka V2(3).txt**, version fournie le 18 novembre 2026. Elle prime sur les prescriptions stylistiques antérieures incompatibles : faire exister les personnages et laisser vivre les conversations avant de rechercher l'efficacité narrative. Une scène peut rester ordinaire ou comique ; une révélation et un cliffhanger ne sont pas obligatoires.

L'ambition de succéder à Danganronpa est une direction créative. Elle ne constitue pas un résultat mesurable ou garanti. L'identité graphique et narrative reste celle de Kami's Desires.

## État réel

- Accès au dépôt et lecture du prompt V2 : effectués.
- Inventaire structurel : 50 fichiers de journées, 529 labels et 42 122 lignes au départ.
- Lecture éditoriale intégrale du scénario et audit scène par scène : **à faire**.
- Journées dont les dialogues ont été réécrits au titre de ce chantier : **0 sur 50 fichiers**.
- Premier lot visuel proposé : les deux branches du jour 4, **en brouillon**.
- Contrôles statiques : passent ; aucune modification des instructions de continuité suivies par le comparateur.
- Lint Ren'Py et lecture en jeu : **bloqués avant lancement du moteur** par une erreur Windows de repositionnement de DLL ; aucune validation moteur n'est acquise.

Ce document conserve l'objectif et son avancement. Il ne représente pas un service d'exécution en arrière-plan et ne prouve pas qu'une tâche planifiée tourne.

## Ordre de production

| Lot | Périmètre existant | Fichiers | État |
|---|---|---:|---|
| 1 | J4 : vote du commerce refusé et adopté | 2 | Mise en scène proposée ; texte à réécrire ; lint à effectuer |
| 2 | J5–J6 : les deux axes, dont les sorties manquantes | 4 | À faire |
| 3 | J7–J10 : silence de Kami et routes d'Anya | 9 | À faire |
| 4 | J11–J15 : souvenirs, informations et soupçons | 5 | À faire |
| 5 | J16–J20 : M16, conduits, corps et confrontation | 5 | À faire |
| 6 | DLC J20–J24 : fins précoces et prolongement | 7 | À faire |
| 7 | DLC J25–J30 : toutes les variantes d'enquête et de fin | 18 | À faire |

Les scènes annexes et traductions se traitent avec le lot qu'elles accompagnent. Les branches absentes nécessitent leur propre plan de continuité avant écriture.

## Continuité à protéger

- Les jours 0 à 3 restent hors périmètre de réécriture. Un changement partagé ne doit pas leur imposer le nouveau comportement par accident.
- Conserver les labels publics, marqueurs de retour historiques, flags, variables persistantes, récompenses et résultats de mini-jeux. Documenter chaque changement structurel voulu.
- Maintenir les conséquences perceptibles des choix et les divergences réelles des routes.
- Les Commandements sont suspendus à l'intérieur du Conclave. Ne pas inventer une sanction automatique empêchant les violences entre représentants.
- Respecter l'ordre de découverte des indices et distinguer ce que le joueur sait de ce que Noam et chaque interlocuteur savent.
- La source narrative actuelle prime sur les résumés anciens lorsqu'ils divergent. Relire les fiches des personnages présents.
- Préserver les distributions gratuite/DLC et ne pas rendre une branche accessible parce que son seul label d'entrée existe.
- Relire particulièrement les fins : identité de Noam, possession de la tablette, confiance d'Iris, message à Julian et destination choisie doivent être cohérents dans chaque variante.

## Méthode pour chaque scène

1. Lire le prompt V2 et les sources requises par les consignes du dépôt, puis le contexte amont et aval de la branche.
2. Identifier les présents, leur activité immédiate, leurs envies personnelles et ce qui peut naturellement terminer la scène.
3. Reconstruire les interactions lorsque la scène est une distribution de prises de parole. Remplacer quelques mots ne suffit pas.
4. Donner des voix distinctes, des hésitations et des réponses ordinaires ; éviter les maximes, les métaphores préparées et le dialogue systématiquement spirituel.
5. Laisser durer les situations intéressantes. Une conversation qui ne fait pas progresser l'intrigue peut être conservée pour son intérêt humain.
6. Mettre en scène le groupe entier, les entrées et sorties, les expressions réelles et les retours après CG ou diffusion.
7. Réutiliser autofocus, cut-ins, réactions et plans rapprochés existants ; réserver les accents aux changements significatifs. Ne pas transformer chaque échange en spectacle.
8. Lire mentalement à voix haute, puis corriger les phrases artificielles et les passages qui répètent une émotion sans action nouvelle.

## Critères de fin d'un lot

- Chaque scène a été évaluée pour son intérêt réel ; la conformité formelle au prompt ne suffit pas.
- Les interlocuteurs ne sont pas interchangeables et la scène ne se contente pas de transmettre les informations du plan.
- Les disputes laissent les traces prévues et une réussite de mini-jeu ne résout pas artificiellement toutes les tensions.
- Les groupes, expressions, portraits de diffusion, CG et effets correspondent aux présences physiques.
- Les choix ont été parcourus dans les deux sens, y compris échecs, reprises et fins alternatives.
- Le parcours du lot jusqu'à la prochaine entrée est jouable sans convergence provisoire déguisée.
- Les traductions anglaises, chinoises et portugaises sont synchronisées ; les nouveaux nœuds de roadmap correspondent à l'état réel.
- Le comparateur structurel a été exécuté et ses écarts expliqués.
- Le lint Ren'Py passe et une lecture en jeu vérifie le rythme, la caméra et la lisibilité.
- Seul un lot qui satisfait ces critères reçoit le statut « terminé ».

## Premier lot visuel proposé

Les fichiers 4_0.rpy et 4_1.rpy corrigent des groupes incomplets, des reprises de scène sans groupe, des positions qui changeaient avec les locuteurs et des overlays de diffusion encore actifs. Les débats utilisent l'ouverture de séance existante, un gros plan de Sael et un cut-in ciblé. Les visages des participants ne sont plus remplacés par un trio pendant le jeu de la bouteille.

Les textes de dialogue, choix et narration restent ceux du commit de départ. Ce lot ne doit donc pas être présenté comme une réécriture narrative du jour 4.

Les chaînes utilisées par l'ouverture de séance existent déjà dans les catalogues anglais, chinois et portugais de kd_staging.rpy.

## Vérification

- python tools/refonte_inventory.py --check : contrôle statique des contrats suivis.
- python -m py_compile tools/refonte_inventory.py : syntaxe de l'outil Python.
- git diff --check : espaces et marqueurs de conflit.
- renpy.sh <projet> lint : obligatoire ; échec de lancement constaté avec les exécutables Windows installés, avant analyse des scripts.
- Lecture en jeu du jour 4 : à effectuer après résolution du lancement du moteur.

Le comparateur ne lit pas toutes les sémantiques Ren'Py et ne remplace pas le moteur. Sa référence initiale figure dans docs/refonte/baseline.json et ne doit pas être régénérée pour masquer une régression.
