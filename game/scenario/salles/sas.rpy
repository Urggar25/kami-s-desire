# -----------------------------------------------------------------------
# SAS DE LIVRAISON — même modèle que CANON
# - 2 persos seulement : Noam + Mara
# - Découverte : logistique, livraisons régulières
# - PNC : porte du sas / caisses / combinaisons / terminal / retour
# -----------------------------------------------------------------------

default decouverte_sas = False



label LIVRAISON_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_348
    scene bg_sas at adaptive_fullscreen

    if not decouverte_sas and day_number() == 1:
        jump decouverte_sas

    $ pnc_room = "pnc_livraison"
    call screen pnc_livraison()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_livraison():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("sas")
    use room_scene_interactions("sas")



    if social_free_time_active() and character_has_available_free_time("sael"):
        imagebutton:
            idle Transform(character_image("sael", "neutre"), zoom=1.00)
            hover Transform(character_image("sael", "raison"), zoom=1.00)
            focus_mask True
            xalign 0.76
            yalign 1.00
            action [SetVariable("last_room_label", "LIVRAISON_TP"), SetVariable("free_time_selected_character", "sael"), Jump("FREE_TIME_CHARACTER_INTERACT")]


label sas1_porte_couloir_sas:
    $ corridor_current = "sas"
    jump EXIT_ROOM_TO_CORRIDOR


label sas1_sas:
    jump LIV_PNC_PORTE


label sas1_digicode_sas:
    "Le digicode commande les verrous de la grande porte du sas."
    "L'écran affiche pression stabilisée, atmosphère confinée et accès extérieur interdit."
    "Aucune touche ne réagit sans autorisation logistique."
    think "Même avec le bon code, Kami saurait qui a essayé de sortir."
    jump LIVRAISON_TP


label sas1_terminal:
    jump LIV_PNC_TERMINAL


label sas2_bouteilles_oxygenes:
    "Quatre bouteilles d'oxygène sont fixées sur leur support."
    "Les manomètres sont au maximum et chaque valve porte un scellé de contrôle."
    think "De quoi respirer dehors. Pas de quoi oublier qu'il faudrait d'abord y arriver."
    jump LIVRAISON_TP


label sas2_tenues:
    "Trois combinaisons pressurisées attendent dans leurs stations de charge."
    "Les casques sont opaques, les joints neufs et les modules dorsaux déjà alimentés."
    "Aucun nom. Aucune taille indiquée."
    think "Elles sont prêtes pour n'importe lequel d'entre nous. Ce n'est pas vraiment rassurant."
    jump LIVRAISON_TP


label LIV_PNC_PORTE:
    window auto

    "La porte du sas occupe tout le mur du fond."
    "Elle est épaisse, renforcée, bardée de verrous et de pictogrammes jaunes."
    "Même fermée, elle donne l’impression d’être en tension."
    "Comme si quelque chose, de l’autre côté, appuyait déjà."

    think "C’est pas une porte qu’on ouvre."
    think "C’est une porte qu’on autorise."

    jump LIVRAISON_TP


label LIV_PNC_CAISSES:
    window auto

    "Les caisses sont disposées avec une précision presque maniaque."
    "Toutes de la même taille."
    "Toutes marquées."
    "Certaines ont des traces d’impact, des coins râpés, des éraflures profondes."
    "D’autres sont encore trop propres pour être honnêtes."

    think "Elles n’ont pas été fabriquées ici."
    think "Elles ont voyagé."
    think "Et elles voyageront encore."

    jump LIVRAISON_TP


label LIV_PNC_COMBIS:
    window auto

    "Trois combinaisons pressurisées sont suspendues dans un renfoncement."
    "Alignées."
    "Silencieuses."
    "Les casques noirs reflètent la lumière bleutée du sas."

    think "On ne montre pas ce genre de choses si on n’envisage pas de s’en servir."
    think "Pas ici."

    jump LIVRAISON_TP


label LIV_PNC_TERMINAL:
    window auto

    "Un terminal logistique est fixé au mur."
    "L’écran est déjà allumé."
    "Pas de mot de passe."
    "Juste une interface froide, directe."

    "Je fais défiler."
    "Dates."
    "Statuts."
    "Réceptions prévues."

    "J7."
    "J14."
    "J21."
    "J28."

    think "Une livraison par semaine."
    think "Même ça, c’est ritualisé."

    jump LIVRAISON_TP


label LIV_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_sas:
    $ decouverte_sas = True
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "Le sas de livraison. C'est peut-être le seul endroit où quelque chose peut entrer ou sortir de cette station."
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_349
    scene bg_sas at adaptive_fullscreen with fade
    "Une énorme porte blindée ferme le fond de la salle. Des caisses sont empilées le long des murs et plusieurs combinaisons attendent dans leurs supports."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("mara", "mefiant", 0.78),
    ])
    "Une femme est plantée devant le terminal, les bras croisés. Elle appuie sur une commande et obtient exactement le même bip d'erreur que la fois précédente."
    mara agace "Allez, ouvre-toi, espèce de saloperie."
    noam hesitation "Tu sais qu'en général, insulter une porte ne suffit pas à l'ouvrir ?"
    mara surpris "Putain, tu m'as fait sursauter ! T'étais obligé d'arriver comme un fantôme ?"
    noam sourire "Désolé. Je pensais pas trouver quelqu'un en train de se battre avec le sas."
    mara taquin "Je me bats pas. Je vérifie juste s'il y a moyen de sortir d'ici sans demander la permission à notre chère Kami."
    noam surpris "Et alors ?"
    mara neutre "Et alors, ça veut pas. Même le menu de maintenance est verrouillé. Ils nous prennent vraiment pour des gosses."
    noam reflexion "Tu comptais faire quoi si ça s'ouvrait ?"
    mara rire "Je sais pas, rentrer chez moi à pied ? Tu poses des questions franchement."
    noam taquin "C'est toi qui essayais d'ouvrir."
    mara sourire "Touché. Moi c'est Mara, d'Axiome."
    $ unlock_character_name("mara")
    noam sourire "Noam, d'[codex_dialogue_link('harmonie', 'HARMONIE')]."
    mara taquin "Harmonie ? Ah, donc t'es le type qui va nous demander de parler calmement quand on commencera à se foutre sur la gueule."
    noam desaccord "J'espère surtout qu'on en arrivera pas là."
    mara rire "Ouais, moi aussi. Ça m'emmerderait de devoir te donner raison."
    "Mara donne un petit coup du plat de la main sur le terminal, puis désigne les caisses derrière elle."
    mara neutre "Au moins, la logistique a l'air prévue. Livraisons aux jours 7, 14, 21 et 28. Nourriture, médocs, pièces de rechange... tout passe par ici."
    noam reflexion "Tu as trouvé ça sur l'écran ?"
    mara sourire "Ouais. L'horaire et les quantités sont affichés. Les codes d'ouverture, bizarrement, beaucoup moins."
    noam inquiet "Si on a un problème urgent entre deux livraisons, on fait comment ?"
    mara stress "Ben on se démerde avec ce qu'on a. C'est ça qui me plaît pas dans leur planning à la con."
    noam neutre "Tu as peur qu'ils oublient de nous approvisionner ?"
    mara taquin "J'ai surtout peur de dépendre d'une machine qui peut décider de nous faire chier pour s'amuser. Nuance."
    "Elle recule enfin du terminal et lève les mains en signe de capitulation."
    mara sourire "Bon, j'ai fait le tour de ma grande carrière de voleuse de vaisseau. Si tu trouves un bouton marqué « sortie », tu m'appelles."
    noam taquin "Promis. Mais je vérifierai d'abord que c'est pas celui qui ouvre la porte sur le vide."
    mara rire "Ah, t'apprends vite. T'es peut-être pas si chiant finalement."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_8
    $ hideGroup()
    jump LIVRAISON_TP
