# Catalogue des mécaniques et outils de développement

> **Lecture obligatoire avant toute modification du dépôt.** Ce document est la carte des outils déjà disponibles pour construire une nouvelle journée de jeu. Toute nouvelle mécanique, tout nouvel effet ou écran réutilisable doit être ajouté ici dans la même modification.

Dernier audit complet : **30 septembre 2026** — sources Ren'Py actives sous `game/`, hors traductions, sauvegardes `.bak` et écrans internes non destinés à être appelés directement.

## Mode d'emploi

- Les exemples sont des appels Ren'Py d'une ligne, prêts à adapter.
- `call screen` est réservé aux écrans qui renvoient une valeur avec `Return()` ; `show screen` sert aux overlays persistants.
- Les noms précédés de `$` sont des fonctions Python exposées au script Ren'Py.
- Les mini-jeux doivent être lancés par leur **label public**, pas par leurs sous-écrans internes.
- Après toute évolution d'une API ci-dessous, mettre à jour son entrée et la date d'audit.

## Minijeux développés

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Kit commun de mini-jeu | Fournit compte à rebours, tutoriel, aide, défis, retry, rang S–D et records persistants. | `game/minijeu/_kit.rpy` | `call mk_show_results("SYNCHRONISATION", score, 100, mg_id="synchro", retries=mk_get_retries("synchro"))` |
| Débat — phase 1 : ouverture | Recompose une phrase par glisser-déposer sous pression, puis calcule score, Kamyz et rang. | `game/minigame_debat_phase1.rpy` | `call debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY", target=None, with_intro_anim=True)` |
| Débat — phase 2 : contradictions | Fait défiler des déclarations à buzzer et applique les influences du débat selon les objections. | `game/minigame_debat_phase2.rpy` | `$ debat_phase2_dialogues_active = MA_LISTE; call debat_phase2_minigame` |
| Haltères / rythme sportif | Demande de cliquer dans une zone mobile, avec répétitions, chrono, défis et événements sportifs. | `game/minigame_halteres.rpy` | `call minijeu_halteres_run(mg_id="halteres", target_reps=10, duration=60.0, base_speed=0.9)` |
| Tracé QTE générique | QTE réutilisable en trois temps : attendre, maintenir puis suivre un tracé sans trop s'en écarter. | `game/minijeu/trace_qte.rpy` | `call trace_qte_run(mg_id="trace_reveil", path_type="curve_right", time_limit=6.0, tolerance=55)` |
| Séquence cinématique de tracés | Enchaîne plusieurs tracés sans retry, conserve chaque réussite ou échec et zoome cumulativement le fond après chaque succès. | `game/minijeu/trace_qte.rpy` | `call trace_qte_sequence([{"path_type": "arc", "time_limit": 1.2}], "bg_cg052", zoom_step=0.065)` |
| Brouillon d'amendement | Assemble des fragments manuscrits, efface les mots gênants et matérialise l'autosabotage de Noam. | `game/minijeu/amendement_brouillon.rpy` | `call amendement_brouillon_play` |
| Fracture QTE | Enchaîne six touches sous chrono avec trois vies et retourne un booléen de réussite. | `game/minijeu/fracture_qte.rpy` | `call j601_play_fracture` |
| Signal instable | Maintient un curseur dans une zone verte tout en validant des éclats QTE pendant 38 secondes. | `game/minijeu/signal_instable.rpy` | `call j601_play_signal_instable` |
| Signal vivant | Assigne neuf fréquences à quatre slots, équilibre trois jauges, pulse quatre quadrants et détruit des orbes. | `game/minijeu/signal_vivant.rpy` | `call j901_play_signal_vivant` |
| Stabilisation | QTE narratif de stabilisation avec séquences de touches, pression temporelle et résultat booléen. | `game/minijeu/stabilisation.rpy` | `call j801_play_stabilisation` |
| Objection fracturée | Duel verbal où les mots gris passent, les rouges s'esquivent et les bleus se renvoient au clic. | `game/minijeu/objection_fracturee.rpy` | `$ j4_objection_result = renpy.call_screen("day4_objection_fracturee")` |
| Contradiction face à Julian | Repère trois fragments contestables dans huit déclarations et choisit la bonne réplique avant la fin du temps. | `game/minijeu/day3_julian_crossfire.rpy` | `call day3_julian_clash_minigame` |
| Fouille frénétique du bureau | Sélectionne des objets puis suit leur tracé en maintenant le clic sans s'en écarter. | `game/minijeu/fouille_bureau.rpy` | `call fouille_bureau_run` |
| Enquête du jour 7 | Explore cinq pistes parmi dix via lieux point-and-click, fiches d'indices et dossier final. | `game/minijeu/enquete_jour7.rpy` | `call j701_investigation` |
| Tri des livraisons | Trie des colis sur tapis roulant par glisser-déposer avec gravité et cadence adaptative. | `game/minijeu/rangement/rangement.rpy` | `call rangement_play` |
| Hack labyrinthe | Moteur de grille avec sentinelles, dash, pièges, boosts, sens uniques, pare-feu et balises. | `game/minijeu/hack/hack_labyrinthe.rpy` | `call j901_play_hack` |
| Hack labyrinthe bonus | Variante bonus du même moteur avec son propre circuit et sa boucle de retry. | `game/minijeu/hack/hack_labyrinthe.rpy` | `call j710_play_hack_bonus` |
| Les 7 jours oubliés | Relie des indices sur une carte mentale afin de reconstruire une chronologie. | `game/minijeu/7jours_oublies.rpy` | `call _11_0_1_2_MINIJEU_7JOURS` |
| Consultation des caméras | Croise heures et salles dans des archives vidéo et déclenche une révélation spéciale sur la bonne combinaison. | `game/minijeu/consultation_cameras.rpy` | `call _11_0_1_3_MINIJEU_CAMERAS` |
| Les cinq aiguillages | Trolley problem en cinq manches dont chaque décision transforme les suivantes. | `game/minijeu/trolley_problem_j12.rpy` | `call j12_play_trolley_problem` |
| Sept différences — Juliette | Compare deux dessins, mémorise quatre différences et joue une réaction narrative pour chacune. | `game/minijeu/sept_differences_j13.rpy` | `call j13_sept_differences_run` |
| Préparer le plateau | Mini-jeu court de sélection d'objets sous chrono pour la préparation du jour 7. | `game/scenario/7_0_1.rpy` | `call j701_play_plate` |
| Garder son calme | Choix chronométrés successifs qui mesurent la maîtrise de Noam. | `game/scenario/7_0_1.rpy` | `call j701_play_calm` |
| Console instable | Calibre des valeurs d'une console avant verrouillage et révélation. | `game/scenario/7_0_1.rpy` | `call j701_play_console` |
| Nettoyer / chercher le dessin | Balaye des particules et anomalies pour retrouver un élément caché. | `game/scenario/7_0_1.rpy` | `call j701_play_search_drawing` |

## Mécaniques de jeu

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Temps libre social | Annonce la phase par un carton animé, ouvre la carte sociale, propose les scènes disponibles et fait progresser les liens persistants. | `game/scenario/free_time.rpy` | `call START_FREE_TIME(next_label="_JOUR_SUIVANT")` |
| Exploration libre scénarisée | Autorise la visite d'un nombre limité de salles sans personnages ni activités de temps libre. | `game/scenario/free_time.rpy` | `call START_EXPLORATION_LIBRE(next_label="_RETOUR", required_visits=2, allowed_rooms=["archive", "maintenance"], title="Inspection")` |
| Découvertes quotidiennes d'exploration | Lance une traversée libre vers une destination narrative obligatoire, avec détours et observations possibles dans les salles accessibles sur le chemin. | `game/daily_exploration.rpy`, `game/scenario/free_time.rpy`, `game/scenario/map.rpy` | `call OFFER_DAILY_EXPLORATION("_SUITE", 0, ["archive", "cafeteria", "conclave"], "Rejoindre le vote", "conclave")` |
| Interaction de lien | Sélectionne et joue la prochaine scène de lien disponible pour un personnage. | `game/scenario/free_time.rpy` | `call FREE_TIME_CHARACTER_INTERACT("lysa")` |
| Relecture d'un souvenir de lien | Rejoue une mémoire débloquée sans consommer un créneau ni modifier la progression. | `game/scenario/free_time.rpy` | `call REPLAY_CHARACTER_LINK("lysa", 1)` |
| Navigation par couloirs | Fait circuler le joueur entre couloirs, portes et salles du Conclave. | `game/scenario/map.rpy` | `call CORRIDOR_NAVIGATION(start_corridor="dortoir")` |
| Carte du Conclave | Ouvre la carte de déplacement manuel et filtre les salles accessibles. | `game/scenario/map.rpy` | `call OPEN_CONCLAVE_MAP` |
| Salles panoramiques à hotspots | Compose les variantes d'une pièce, expose leurs zones cliquables et peut neutraliser les faux calques d'animation comme celui de `chambre3`. | `game/scene_backgrounds.rpy` | `use room_scene_background("cafeteria"); use room_scene_interactions("cafeteria")` |
| Éclairage automatique des décors | Teinte dynamiquement les scènes et les fonds d'ouverture de porte selon `current_period` sans dupliquer les images. | `game/scene_backgrounds.rpy`, `game/scenario/map.rpy` | `scene bg_cafeteria at adaptive_fullscreen` |
| Affichage individuel de personnage | Affiche, remplace ou repositionne un sprite en mémorisant expression et position. | `game/script.rpy` | `$ showP("lysa", "blase", 0.72)` |
| Affichage de groupe | Place automatiquement un groupe de personnages avec entrées/sorties cohérentes. | `game/transform.rpy` | `$ showGroup([("noam", "neutre", 0.25), ("lysa", "blase", 0.75)])` |
| Caméra cinématique | Déplace et zoome les couches décor/personnages avec restauration de l'état courant. | `game/script.rpy` | `$ cam_move(fx=0.68, fy=0.45, z=1.25, t=0.4)` |
| Autofocus du locuteur | Zoome le personnage qui parle, atténue les autres et floute le décor automatiquement. | `game/script.rpy` | `lysa blase "On n'a pas le temps."` |
| Noms inconnus puis révélés | Affiche un alias tant qu'un nom n'est pas connu et persiste son déblocage. | `game/script.rpy` | `$ unlock_character_name("anya")` |
| Expressions et tenues composées | Génère les sprites animés depuis corps, tenue, bras, bouche, yeux et accessoires équipés. | `game/images.rpy` | `$ showP("noam", "reflexion", 0.50)` |
| Tenue pompom girl d'Iris | Ajoute une tenue de cheerleader complète avec cinq poses de bras détourées sur les textures historiques d'Iris. | `game/images/character/iris/tenue3.png`, `game/images/character/iris/bras_long_corps_tenue3.png`, `game/images.rpy` | `$ unlock_profile_skin("iris", "tenue3")` |
| Personnages inconnus génériques | Produit des portraits homme/femme inconnus avec expressions composées. | `game/unknown_characters.rpy` | `show expression unknown_expression("female", "neutre") as inconnue` |
| Choix critique | Présente 2 à 4 décisions majeures dans un HUD adaptatif avec Noam glitché. | `game/critical_choice.rpy` | `menu (screen="critical_choice", noam_expr="hesitation"):` |
| Statistiques persistantes | Gère niveaux, XP, seuils, gains multiples et affiche une annonce animée à chaque montée de niveau. | `game/stats_system.rpy` | `$ award_stat_xp("logique", 2)` |
| Jet de statistique D10 | Lance un D10 contre une difficulté et renvoie réussite ou échec via un écran de résolution. | `game/stats_system.rpy` | `call screen stat_check("logique", 12, "Déchiffrer le protocole Kami")` |
| Dialogue conditionné par les stats | Affiche des réponses verrouillées selon les stats, joue leur label et attribue l'XP prévue. | `game/stat_dialogues.rpy` | `call play_stat_dialogue("d3")` |
| Arguments globaux | Débloque un argument de débat de manière persistante et compatible avec les anciennes sauvegardes. | `game/script.rpy` | `$ add_argument("Le coût humain")` |
| Notification d'argument | Affiche un panneau animé signalant au joueur qu'un argument vient d'être obtenu. | `game/screens.rpy` | `show screen argument_unlock("Le coût humain")` |
| Dossier de vote | Organise propositions et arguments par chapitre avec progression, jauge et déblocages. | `game/vote_dossier.rpy` | `$ unlock_dossier_arg("id_argument"); show screen vote_dossier` |
| Frise chronologique des preuves | Présente les faits débloqués sur une table d'enquête filtrable, avec fiches papier illustrées, navigation chronologique, détail des connexions et compatibilité des anciennes sauvegardes. | `game/investigation_system.rpy`, `game/images/hud/investigation/evidence/`, `game/images/hud/investigation/ui/`, `game/images/hud/investigation/dossier_quick_access.png` | `$ investigation_add("photo_lea_disparue"); call investigation_open_dossier` |
| Analyse vidéo d'enquête | Fournit timeline, lecture, ralenti, image par image et zones inspectables pour les archives de surveillance. | `game/investigation_system.rpy` | `call investigation_video_run("kael_photo", "bg_chambre", False)` |
| Inspection visuelle d'indice | Permet de zoomer et d'inspecter des zones d'une image jusqu'à identifier un détail narratif requis. | `game/investigation_system.rpy` | `call investigation_image_run("juliette_copy")` |
| Exploration des conduits | Propose des embranchements courts, cartographie la route et garantit une convergence sans softlock. | `game/investigation_system.rpy` | `call investigation_conduit_run("survey")` |
| Inspection de salle | Déclenche zoom, secousse et bulle BD au survol de cinq zones invisibles, puis relie la salle inspectée à un indice du dossier. | `game/investigation_system.rpy` | `call investigation_room_run` |
| Objection Protocol | Confronte une déclaration à un indice du dossier et renvoie `(indice, résultat)` pour distinguer contradiction correcte, preuve insuffisante, erreur ou impossibilité. | `game/investigation_system.rpy` | `call objection_protocol_run("Je n'étais pas là.", "mara_exploration", ("conduits_chambres",)); $ objection_result = _return` |
| Vote final animé | Recueille Pour/Abstention/Contre sous chrono puis dépouille les bulletins avec résultat d'amendement. | `game/vote_phase3_final.rpy` | `call vote_phase3_final` |
| Codex persistant | Débloque des entrées, les regroupe en packs et lie automatiquement les termes des dialogues. | `game/codex.rpy` | `$ unlock_codex_page("id_entree")` |
| Affinité et profils | Modifie l'affinité, débloque les sections de profil et enregistre les alignements de débat. | `game/systems_profiles_codex.rpy` | `$ add_affinity("lysa", 1)` |
| Garde-robe et accessoires | Débloque, équipe et prévisualise tenues et accessoires persistants des personnages. | `game/systems_profiles_codex.rpy` | `$ unlock_profile_skin("lysa", "tenue_02")` |
| Codes promotionnels | Valide un code, marque son usage persistant et accorde son contenu. | `game/systems_profiles_codex.rpy` | `$ promo_result = apply_promo_code("KAMI2026")` |
| Succès | Débloque un succès persistant et affiche automatiquement sa notification. | `game/succes.rpy` | `$ unlock_succes("id_succes")` |
| Éclats de désir | Ajoute une monnaie persistante avec notification et protection contre les doubles récompenses. | `game/kami_shop_events.rpy` | `$ kami_grant_desire_reward("jour_10_fin", 25)` |
| Boutique de Kami | Achète et prévisualise des cosmétiques avec les éclats de désir. | `game/kami_shop_events.rpy` | `textbutton "Boutique" action ShowMenu("kami_shop_menu")` |
| Galerie CG/vidéos | Détecte les CG `bg_cg…` et les anciens identifiants `cg…`, regroupe leurs variantes, gère leur déblocage et les présente dans la galerie. | `game/menu.rpy` | `$ unlock_gallery_image("bg_cg053")` |
| Roadmap interactive | Débloque, complète et affiche les nœuds de progression avec téléportation de développement. | `game/roadmap/roadmap_menu.rpy` | `$ roadmap_unlock("jour_10"); call screen roadmap_menu` |
| Carte narrative | Visualise les branches déjà vues à partir des labels atteints dans les différentes routes. | `game/story_map.rpy` | `call screen story_map_menu` |
| Évènement « Sept Questions » | Gère calendrier, étapes quotidiennes, quiz, scores et récompenses persistantes. | `game/events/seven_questions/event_data.rpy`, `game/events/seven_questions/event_screens.rpy` | `textbutton "Sept Questions" action ShowMenu("seven_questions_event_menu")` |
| Curseur virtuel manette | Convertit stick, boutons et gâchettes en déplacement, clics et molette de souris pour les PnC/drag-and-drop. | `game/gamepad_cursor.rpy` | `show screen gamepad_virtual_cursor` |

## Mécaniques visuelles

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Flashs d'impact | Transitions blanche, rouge ou cyan prêtes pour révélation, coup et signal système. | `game/effects.rpy` | `with flash_red` |
| Coupure et fondus | Fournit coupure noire, dissolution rapide et dissolution douce. | `game/effects.rpy` | `with cut_black` |
| Secousse paramétrable | Secoue décor et personnages avec intensité et durée configurables. | `game/effects.rpy` | `$ shake(18, 0.5)` |
| Impact combiné | Combine flash coloré et secousse en un seul appel. | `game/effects.rpy` | `$ impact(intensity=14, duration=0.35, color="#ffffff")` |
| Bandes cinéma | Anime un letterbox en haut et en bas pour cadrer une séquence dramatique. | `game/effects.rpy` | `$ letterbox_on(h=110, t=0.4)` |
| Interjection plein écran | Projette un texte façon objection/verdict, avec slam, fond graphique et secousse optionnelle. | `game/effects.rpy` | `$ interject("OBJECTION !", color="#5cd3ff")` |
| Vignette de stress périphérique | Fait respirer une ombre diffuse dans les seuls bords et coins, sans masquer le centre ni encadrer l'image en rouge. | `game/effects.rpy`, `game/images/effects/stress_vignette.svg` | `$ danger_on()` |
| Révélation de doppelgänger | Coupe presque tout son et toute lumière, révèle des yeux puis un sourire dans le noir et peut conclure par un screamer sec. | `game/effects.rpy`, `game/images/effects/doppelganger_eyes.svg`, `game/images/effects/doppelganger_smile.svg` | `$ doppelganger_reveal(screamer=True)` |
| Image sous lampe | Plonge presque entièrement décor et personnages dans le noir, puis révèle une zone nette avec un faisceau mobile suivant cinq parcours aléatoires fermés. | `game/effects.rpy`, `game/images/effects/flashlight_vignette.svg`, `game/script.rpy` | `$ flashlight_on(); pause; $ flashlight_off()` |
| Transitions d'horreur | Regroupe fondu rampant, noir instantané/lent, pulsation rouge, glitch, saut de signal, déchirure mnésique, suffocation et pixellisation. | `game/effects.rpy` | `with signal_stutter` |
| Transforms d'angoisse | Applique zoom lent, dérive, flash dur, respiration sombre, rémanence, poussée, progression dans un conduit ou inclinaison. | `game/effects.rpy` | `show bg_conduit_reseau at corridor_crawl` |
| Décors animés | Anime visiblement les fonds calmes, oppressants ou embarqués par dérive, avancée lente ou flottement de navette. | `game/effects.rpy` | `scene bg_observation at adaptive_fullscreen, living_background` |
| Clignement des yeux | Ferme et rouvre des paupières animées sans bloquer durablement la scène. | `game/transform.rpy` | `$ blink()` |
| Transition contextuelle de jour | Rejoue le carton historique plein écran lorsque Noam s'endort, ou anime seulement le compteur HUD lorsqu'il reste éveillé. | `game/transform.rpy`, `game/day1_ui.rpy` | `call end_day("18", sleeping=True)` |
| Transition localisée de période | Détecte automatiquement toute modification de `current_period` et anime uniquement le badge HUD en haut à droite. | `game/day1_ui.rpy` | `$ current_period = "Après-midi"` |
| Carte de chapitre | Affiche pendant cinq secondes le statut et le titre d'un chapitre sur fond noir. | `game/transform.rpy` | `call show_chapter_title("CHAPITRE II", "Les fractures")` |
| Carton de titre libre | Anime l'apparition, la tenue et la disparition d'un titre localisé centré avec alerte Kami. | `game/transform.rpy` | `call show_custom_title("Temps libre")` |
| HUD jour, période et accès rapides | Affiche un panneau sci-fi compact avec progression du cycle et trois boutons iconographiques vers la tablette, le dossier d'enquête et le menu système. | `game/day1_ui.rpy` | `$ current_period = "Soir"; show screen day_period_hud` |
| Réveil trouble | Superpose respiration, scan et mise au point selon un niveau d'éveil. | `game/day1_ui.rpy` | `show screen day1_wakeup_overlay(level="heavy")` |
| Overlay de souvenir | Ajoute teinte violette, vignette et grain filmique autour d'un flashback. | `game/day0_ui.rpy` | `show screen day0_flashback_overlay with d0_flashback_entry` |
| Diffusion portrait de Kami | Cadre un interlocuteur devant un fond expressif de Kami avec portrait dynamique et chrome broadcast. | `game/transform.rpy` | `scene bg_diffusion_taquin; show screen kami_broadcast_ui; $ bc_show("ryn", "colere"); ryn "Non."; $ bc_hide()` |
| Décors narratifs et CG des jours 8 à 21 | Fournit les fonds du réseau, de la cavité, de la salle Goumi et de la navette, ainsi que les CG de révélations `bg_cg040` à `bg_cg059`, dont les confrontations de doubles et les fins alternatives des jours 20 et 21. | `game/scene_backgrounds.rpy`, `game/images/background/scenes/`, `game/images/background/cg/` | `$ unlock_gallery_image("bg_cg058"); scene bg_cg058 at adaptive_fullscreen` |
| Montage chibi | Joue une planche chibi comme une séquence rythmée avec cuts, impacts, particules et SFX synchronisés. | `game/chibi_montage.rpy` | `$ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)` |
| Boîte à outils bande-annonce | Fournit zooms, pans, grades, glitch RGB, titres, citations, letterbox et cartes de fin cinématiques. | `game/version_2_1_trailer_kit.rpy` | `show screen trl_title("LE CONCLAVE", kicker="ILS VOUS REGARDENT", slam=True)` |

## Mécaniques sonores

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Musique d'ambiance | Joue une piste en boucle avec fondus sur le canal musique. | `game/audio/music/` | `play music "audio/music/bgm_low_tension.mp3" fadein 1.0` |
| Effet sonore ponctuel | Joue un SFX sur le canal son sans interrompre la musique. | `game/audio/` | `play sound "audio/sfx_exclamation.mp3"` |
| Doublage court automatique | Déduit l'intention d'une réplique et joue le bark correspondant au personnage. | `game/_dialogue_barks.rpy` | `$ play_dialogue_doublage("lysa", "Ouais. Super.")` |
| Génération des SFX indispensables | Synthétise au premier lancement les sons système manquants afin d'éviter les erreurs d'assets. | `game/_sfx_bootstrap.rpy` | `$ _sfx_bootstrap()` |
| Rupture audio horrifique | Coupe brutalement la musique avec un impact inversé puis restaure son volume de façon progressive. | `game/effects.rpy`, `game/audio/sfx_audio_drop.wav` | `$ horror_audio_cut(duration=0.42, restore_volume=0.75)` |
| Musique horrifique ralentie | Bascule en fondu vers une variante réellement ralentie et assombrie de la musique courante. | `game/effects.rpy`, `game/audio/music/bgm_cold_metadata_slow.mp3` | `$ horror_music_slow()` |
| Couches sonores de bande-annonce | Superpose plusieurs impacts/risers grâce aux canaux dédiés `trl_sfx2`, `trl_sfx3` et `trl_amb`. | `game/version_2_1_trailer_kit.rpy` | `play trl_sfx2 "audio/trailer/trl_impact_deep.wav"` |

### Bibliothèque musicale disponible

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Menu principal | Thème du menu principal. | `game/audio/music/main_menu.mp3` | `play music "audio/music/main_menu.mp3" fadein 1.0` |
| Déclin du monde | Ambiance sombre et ample pour crise ou enquête. | `game/audio/music/bgm_world_decline.mp3` | `play music "audio/music/bgm_world_decline.mp3" fadein 1.0` |
| Distance non dite | Ambiance relationnelle retenue, disponible en deux variantes. | `game/audio/music/bgm_unsaid_distance.mp3`, `game/audio/music/bgm_unsaid_distance2.mp3` | `play music "audio/music/bgm_unsaid_distance.mp3" fadein 1.0` |
| Système outrepassé | Tension technologique, disponible en deux variantes. | `game/audio/music/bgm_system_override.mp3`, `game/audio/music/bgm_system_override2.mp3` | `play music "audio/music/bgm_system_override.mp3" fadein 1.0` |
| Matin néon doux | Ambiance matinale légère, disponible en deux variantes. | `game/audio/music/bgm_soft_neon_morning.mp3`, `game/audio/music/bgm_soft_neon_morning2.mp3` | `play music "audio/music/bgm_soft_neon_morning.mp3" fadein 1.0` |
| Routine calme | Quotidien posé, disponible en deux variantes. | `game/audio/music/bgm_quiet_routine.mp3`, `game/audio/music/bgm_quiet_routine2.mp3` | `play music "audio/music/bgm_quiet_routine.mp3" fadein 1.0` |
| Tension basse | Suspense discret, disponible en deux variantes. | `game/audio/music/bgm_low_tension.mp3`, `game/audio/music/bgm_low_tension2.mp3` | `play music "audio/music/bgm_low_tension.mp3" fadein 1.0` |
| Atmosphère introspective | Fond émotionnel pour réflexion ou débrief. | `game/audio/music/bgm_introspective_atmosphere.mp3` | `play music "audio/music/bgm_introspective_atmosphere.mp3" fadein 1.5` |
| Assemblée fatale | Thème de confrontation et de débat majeur. | `game/audio/music/bgm_fatal_assembly.mp3` | `play music "audio/music/bgm_fatal_assembly.mp3" fadein 1.0` |
| Élan amoureux | Thème romantique ou chaleureux. | `game/audio/music/bgm_fallin_love.mp3` | `play music "audio/music/bgm_fallin_love.mp3" fadein 1.0` |
| Métadonnées froides | Ambiance analytique, distante et technologique. | `game/audio/music/bgm_cold_metadata.mp3` | `play music "audio/music/bgm_cold_metadata.mp3" fadein 1.0` |
| Désir prudent | Intimité hésitante, disponible en deux variantes. | `game/audio/music/bgm_careful_wanting.mp3`, `game/audio/music/bgm_careful_wanting2.mp3` | `play music "audio/music/bgm_careful_wanting.mp3" fadein 1.0` |
| Calme, pas paix | Accalmie ambiguë qui conserve une tension sous-jacente. | `game/audio/music/bgm_calm_not_peace.mp3` | `play music "audio/music/bgm_calm_not_peace.mp3" fadein 1.0` |
| Pulsation horrifique | Variante ralentie et grave pour poursuites dans les conduits et présence invisible. | `game/audio/music/bgm_horror_pulse.mp3` | `play music "audio/music/bgm_horror_pulse.mp3" fadein 1.0` |
| Révélation horrifique | Variante très ralentie du déclin du monde pour découverte d'un corps ou d'un double. | `game/audio/music/bgm_horror_reveal.mp3` | `play music "audio/music/bgm_horror_reveal.mp3" fadein 1.0` |
| Réunion sous tension | Variation resserrée d'Assemblée fatale pour confrontation collective. | `game/audio/music/bgm_tense_meeting.mp3` | `play music "audio/music/bgm_tense_meeting.mp3" fadein 1.0` |
| Épilogue froid | Variation ralentie de Calme, pas paix pour une conclusion faussement apaisée. | `game/audio/music/bgm_epilogue_cold.mp3` | `play music "audio/music/bgm_epilogue_cold.mp3" fadein 2.0` |

### Bibliothèque de SFX disponible

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Alertes et UI | Bips, annonce, alerte Kami, question et exclamations normales ou horrifiques. | `game/audio/sfx_beep.mp3`, `sfx_announce.mp3`, `sfx_kami_alert.wav`, `sfx_question.mp3`, `sfx_exclamation.mp3`, `sfx_exclamation_horror.mp3` | `play sound "audio/sfx_kami_alert.wav"` |
| QTE et mini-jeu | Validation, erreur, démarrage de mini-jeu et victoire. | `game/audio/sfx_qte_hit.wav`, `sfx_qte_miss.wav`, `sfx_minigame_start.mp3`, `sfx_victory.mp3` | `play sound "audio/sfx_qte_hit.wav"` |
| Vote | Sons dédiés aux bulletins Pour, Contre et Abstention. | `game/audio/sfx_vote_pour.wav`, `sfx_vote_contre.wav`, `sfx_vote_abstention.wav` | `play sound "audio/sfx_vote_pour.wav"` |
| Impacts et objets | Balle, coup sourd, métal, papier, porte, coups frappés, laser, chute et craquement. | `game/audio/sfx_balle.mp3`, `sfx_thud.mp3`, `sfx_metal_clank.mp3`, `sfx_paper.mp3`, `sfx_door.mp3`, `sfx_knock.mp3`, `sfx_laser_canon.mp3`, `sfx_drop.mp3`, `sfx_creak.mp3` | `play sound "audio/sfx_metal_clank.mp3"` |
| Corps et mouvement | Respiration, cœur, course, râle, douche et applaudissements. | `game/audio/sfx_breath.mp3`, `sfx_heartbeat.mp3`, `sfx_run.mp3`, `sfx_rale.mp3`, `sfx_shower.mp3`, `sfx_clap.mp3` | `play sound "audio/sfx_heartbeat.mp3"` |
| Glitch et tension | Statique, grésillement, glitch, tambour, cliquetis et mauvaise blague. | `game/audio/sfx_static.mp3`, `sfx_gresillement.mp3`, `sfx_glitch.mp3`, `sfx_tambour.mp3`, `sfx_clim.mp3`, `sfx_bad_joke.mp3` | `play sound "audio/sfx_glitch.mp3"` |
| Horreur sensorielle | Ajoute chute audio inversée, acouphène et frottement métallique ralenti pour les scènes de conduit et de perte de contrôle. | `game/audio/sfx_audio_drop.wav`, `game/audio/sfx_tinnitus.wav`, `game/audio/sfx_duct_scrape.wav` | `play sound "audio/sfx_duct_scrape.wav"` |
| Transition de jour | Ponctue les cartes de jour et de chapitre. | `game/audio/sfx_day_transition.wav` | `play sound "audio/sfx_day_transition.wav"` |
| Kit cinématique | Risers, impacts, braam, drone, heartbeat, glitches, swoosh, ticks et alarmes pour montages. | `game/audio/trailer/` | `play sound "audio/trailer/trl_braam.wav"` |

## Mécaniques de dialogue

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Dialogue personnage | Utilise les personnages dynamiques, guillemets, autofocus, noms révélables et image tags. | `game/script.rpy` | `lysa blase "Ouais. On avance."` |
| Pensée de Noam | Affiche une pensée courte avec le style narratif dédié. | `game/script.rpy` | `think "Je suis épuisé."` |
| Narration / voix off | Réinitialise automatiquement le focus cinématique lorsqu'aucun personnage ne parle. | `game/script.rpy` | `n "Le couloir est vide."` |
| Animation de ponctuation | Détecte question, exclamation et suspense pour animer les bords du dialogue et jouer un son adapté. | `game/dialogue_animations.rpy` | `mara colere "Tu plaisantes ?!"` |
| Choix standard | Affiche le menu Ren'Py stylisé pour deux ou trois perspectives non binaires. | `game/screens.rpy` | `menu: "Observer": $ choix = "observer"` |
| Choix critique | Remplace le menu standard pour une décision majeure de 2 à 4 options. | `game/critical_choice.rpy` | `menu (screen="critical_choice", noam_expr="peur"):` |
| Diffusion de Kami | Affiche Kami sur un fond expressif et réserve `bc_show` aux interlocuteurs qui lui répondent. | `game/transform.rpy` | `scene bg_diffusion_taquin; show screen kami_broadcast_ui; kami "Oh."; $ bc_show("noam", "inquiet")` |
| Codex dans les dialogues | Détecte, débloque et rend cliquables les termes connus à l'intérieur du texte affiché. | `game/codex.rpy` | `noam "Le Conclave a encore changé les règles."` |
| Choix de dialogue à statistiques | Conditionne certaines réponses à un niveau de statistique et distribue les gains associés. | `game/stat_dialogues.rpy` | `call play_stat_dialogue("d8")` |
| Barks vocaux | Sélectionne automatiquement une intention vocale courte à partir du texte et du locuteur. | `game/_dialogue_barks.rpy` | `$ play_dialogue_doublage("mara", "Non mais sérieux.")` |

## Écrans et interfaces réutilisables

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Tablette — accueil | Hub Conclave OS donnant accès aux statistiques, vote et autres cartes système. | `game/stats_system.rpy` | `call screen tablet_home(clock="08:00", show_vote=True)` |
| Tablette — statistiques | Présente les cinq stats et leur progression en jauges segmentées. | `game/stats_system.rpy` | `show screen tablet_stats` |
| Tablette narrative du jour 1 | Interaction terminal scénarisée propre au réveil et à l'amendement. | `game/day1_ui.rpy` | `call screen day1_tablet_interaction` |
| Timer dynamique | Compte à rebours persistant, modifiable en direct, avec saut optionnel à expiration. | `game/day0_ui.rpy` | `$ day0_timer_init(m=5, end_label="_TEMPS_ECOULE"); show screen day0_countdown_overlay` |
| Scanner de badge | Séquence interactive de scan d'identité et de validation de sécurité. | `game/day0_ui.rpy` | `call screen day0_security_badge_scan` |
| Téléphone compromis | Écran de téléphone narratif avec messages et prise de contrôle. | `game/day0_ui.rpy` | `call screen day0_phone_override` |
| Registre des commandements | Interface de consultation des règles/commandements du système. | `game/day0_ui.rpy` | `call screen day0_commandments_registry` |
| Sélection des représentants | Écran de sélection et confirmation des représentants. | `game/day0_ui.rpy` | `call screen day0_representative_selection` |
| Formulaire d'amendement | Interface à cartes pour composer et valider un amendement. | `game/day1_ui.rpy` | `call screen day1_amendment_form` |
| Confirmation d'urne | Écran de confirmation dramatique avant dépôt du vote. | `game/day1_ui.rpy` | `call screen day1_urn_confirmation` |
| Codex | Menu de packs, cartes d'entrée, détails, liens et scènes bonus. | `game/codex.rpy` | `call screen codex_menu` |
| Profils | Menu des personnages, affinités, histoire, relations et accès à la garde-robe. | `game/systems_profiles_codex.rpy` | `call screen profiles_menu` |
| Garde-robe | Prévisualise et équipe une tenue et des accessoires pour un profil donné. | `game/systems_profiles_codex.rpy` | `show screen profile_wardrobe("lysa")` |
| Codes promotionnels | Écran de saisie et de validation des codes promotionnels. | `game/systems_profiles_codex.rpy` | `textbutton "Codes promo" action ShowMenu("promo_codes_menu")` |
| Succès | Grille des succès, états verrouillés et détails des récompenses obtenues. | `game/succes.rpy` | `call screen succes_menu` |
| Menu système | Panneau pause dédié : sauvegarde, chargement, préférences, codex et sortie. | `game/screens.rpy` | `call screen system_menu` |
| Écran de fin | Affiche une conclusion KAMI.CORE animée avec le nom de la fin atteinte et un retour au menu principal. | `game/ending_screen.rpy` | `call screen kd_ending_reached("Les Remplaçants", "ENDING 01 // JOUR 20")` |
| Galerie | Affiche CG et vidéos débloquées avec filtres et variantes. | `game/menu.rpy` | `textbutton "Galerie" action ShowMenu("gallery_menu")` |
| Sélection de scènes | Lance les scènes bonus ou relectures disponibles. | `game/menu.rpy` | `textbutton "Scènes" action ShowMenu("scene_select_menu")` |
| Boutique temporaire | Liste les objets, prix, possessions et accès à leur prévisualisation. | `game/kami_shop_events.rpy` | `textbutton "Boutique" action ShowMenu("kami_shop_menu", initial_page=0)` |
| Hub évènements | Centralise l'évènement actif, son statut et l'accès à ses écrans dédiés. | `game/events/seven_questions/event_screens.rpy` | `textbutton "Évènement" action ShowMenu("kami_event_menu")` |
| Roadmap | Carte zoomable des nœuds du projet et de la progression narrative. | `game/roadmap/roadmap_menu.rpy` | `call screen roadmap_menu` |
| Carte des routes | Graphe des branches narratives déjà vues par le joueur. | `game/story_map.rpy` | `call screen story_map_menu` |

## Effets divers et infrastructure

| Nom | Description en une ligne | Fichier source | Exemple d'appel en une ligne |
|---|---|---|---|
| Plein écran adaptatif | Recadre un décor en mode cover quelle que soit la résolution. | `game/script.rpy` | `scene bg_cafeteria at adaptive_fullscreen` |
| Flou de décor | Remplace le fond courant par sa version floutée sans toucher aux sprites. | `game/script.rpy` | `$ bg_set_blur(True, blur_radius=2.0)` |
| Focus manuel de personnage | Force focus, atténuation du groupe et caméra sur un personnage hors callback de dialogue. | `game/script.rpy` | `$ cinematic_focus("lysa", t=0.30)` |
| Période de la journée | Pilote HUD et éclairage automatique avec une valeur Matin/Après-midi/Soir/Nuit. | `game/day1_ui.rpy`, `game/scene_backgrounds.rpy` | `$ current_period = "Nuit"` |
| Verrouillage NSFW | Mémorise le choix de contenu adulte et permet de forcer le verrouillage. | `game/script.rpy` | `$ lock_nsfw_content()` |
| Compatibilité anciennes sauvegardes | Conserve des labels, migrations et synchronisations de données persistantes lors des évolutions. | `game/script.rpy`, `game/codex.rpy`, `game/scenario/free_time.rpy` | `$ migrate_known_character_names_from_save()` |
| Localisation des textes système | Traduit les libellés dynamiques via le helper commun utilisé par les interfaces. | `game/gui.rpy` | `$ titre_localise = kd_tr("Temps libre")` |

## Procédure de maintenance obligatoire

Pour chaque ajout ou modification future :

1. Lire ce document avant de toucher au dépôt.
2. Chercher d'abord si un outil existant couvre le besoin.
3. Si une mécanique, un effet, un écran ou un point d'entrée public change, mettre à jour son entrée ici.
4. Si un nouvel outil est créé, l'ajouter dans la bonne catégorie avec les quatre champs obligatoires.
5. Vérifier que l'exemple appelle bien l'API publique et que le chemin existe.
6. Mettre à jour la date du dernier audit lorsqu'un recensement complet est refait.
