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
    think "Si une navette doit nous apporter de la nourriture chaque semaine, elle passera forcément par le sas. Je veux au moins voir à quoi ressemble notre seule porte vers l'extérieur."

    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_349
    scene bg_sas at adaptive_fullscreen with fade

    "La porte blindée est énorme, et des caisses sont alignées le long des murs. Une femme est penchée sur le terminal de contrôle, visiblement en pleine négociation avec la machine."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("mara", "mefiant", 0.78),
    ])

    mara agace "Allez, bordel, y a forcément un menu de maintenance quelque part !"
    noam sourire "Salut. Tu essaies de sortir ?"
    mara surpris "Putain ! Tu pouvais pas faire un peu de bruit en arrivant ? J'ai cru que c'était Kami."
    noam taquin "Désolé. Du coup, ça marche ?"
    mara rire "Bien sûr. Je suis en train de programmer une navette pour aller boire un verre sur Terre."
    noam sourire "Ah, parfait. Tu me prends avec toi ?"
    mara taquin "Seulement si t'arrêtes de poser des questions de merde."

    "Elle tapote un nouveau menu, puis m'indique deux zones tactiles sur le panneau."
    mara neutre "Attends, tu peux m'aider deux secondes ? Je crois qu'il faut maintenir ce bouton pour tester l'autre commande."
    noam hesitation "Tu es sûre de toi ?"
    mara sourire "À peu près. Et puis on va pas casser toute la station avec un bouton."
    noam inquiet "C'est pas exactement ce que j'avais envie d'entendre."
    mara taquin "Allez, fais pas ta chochotte. Tiens celui-là, je m'occupe du reste."

    "Je maintiens la commande. Mara en active une seconde. Une alarme sonore se déclenche aussitôt, accompagnée d'un message rouge sur le terminal."
    play sound sfx_beep
    noam peur "DÉPRESSURISATION EN COURS ?! MARA, C'EST QUOI CE BORDEL ?!"
    mara stress "Hein ?! Mais non, c'est pas possible ! Lâche le bouton !"
    "Je retire ma main. L'alarme continue de retentir tandis qu'un compte à rebours apparaît."
    noam desespoir "ÇA S'ARRÊTE PAS !"
    mara colere "J'AI VU ! Pousse-toi, laisse-moi regarder !"
    "Mara frappe plusieurs fois sur l'écran. Le compte à rebours atteint zéro, puis disparaît brusquement."
    "« SIMULATION TERMINÉE — AUCUNE DÉPRESSURISATION EFFECTUÉE »"

    "Il nous faut plusieurs secondes pour comprendre. Mara relit le message, puis commence à rire."
    mara rire "Ah non, mais quelle bande de cons ! Ils ont mis un simulateur sur le même écran que les commandes !"
    noam desaccord "Tu trouves ça drôle ?! J'ai cru qu'on allait mourir !"
    mara rire "Bah oui, justement ! T'as vu ta tête ? On aurait dit que t'allais traverser le plafond !"
    noam colere "Tu m'as demandé de maintenir le bouton !"
    mara sourire "Ouais, bon, d'accord. C'était pas mon idée du siècle."
    "Elle lève les mains en signe d'excuse, même si son sourire est encore bien trop large."
    mara taquin "Promis, la prochaine fois que je joue avec un sas, je te préviens que je sais pas ce que je fais."
    noam reflexion "C'est censé me donner envie de recommencer ?"
    mara rire "Pas forcément, non."

    "Mara se laisse tomber contre une caisse et finit par reprendre son souffle."
    mara sourire "Moi c'est Mara. Axiome. Et toi, le type qui vient d'avoir la peur de sa vie ?"
    $ unlock_character_name("mara")
    call kd_play_character_intro("mara") from _call_kd_intro_mara_j1
    noam neutre "Noam. Harmonie."
    mara taquin "Harmonie ? Ah, ça explique pourquoi t'as essayé de parler poliment à la porte avant de gueuler."
    noam taquin "C'est sûr que toi, tu as commencé par l'insulter."
    mara rire "Et j'assume. Elle avait qu'à mieux se comporter."

    "Elle me montre l'écran désormais revenu à son calendrier normal."
    mara neutre "Bon, au moins, j'ai réussi à trouver les livraisons. Jour 7, 14, 21 et 28. Toute notre bouffe et nos pièces de rechange devraient passer par là."
    noam inquiet "Et si on manque de quelque chose entre deux livraisons ?"
    mara stress "Ben on sera dans la merde. C'est aussi pour ça que je voulais voir comment la porte marche."
    noam reflexion "Tu pensais pouvoir la rouvrir toute seule ?"
    mara taquin "J'avais peut-être une petite idée derrière la tête. Mais après notre magnifique démonstration, je vais éviter de faire la maligne."
    "Elle se relève et regarde un instant la porte blindée. Son sourire s'atténue, juste assez pour que je le remarque."
    mara stress "C'est con, hein ? On est à quelques mètres du seul endroit qui mène dehors, et on sait même pas comment l'ouvrir."
    noam neutre "On aura peut-être l'occasion d'en apprendre plus à la première livraison."
    mara sourire "Ouais. En attendant, si t'en parles aux autres, dis que c'était un test de sécurité réussi."
    noam taquin "Je dirai surtout que tu m'as presque fait faire une crise cardiaque."
    mara rire "Ça marche aussi !"

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_8
    $ hideGroup()
    jump LIVRAISON_TP
