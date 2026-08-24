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

    think "Sas de livraison."
    think "Pourquoi les livraisons auraient-elles besoin de passer par un sas ?"
    think "Comme si les livraisons pouvaient être toxiques ou infectées."

    pause 0.4

    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_349
    scene bg_sas at adaptive_fullscreen with fade

    "La pièce est vaste, froide, presque clinique."
    "Le sol reflète les lumières bleues du plafond."
    "Tout est net."
    "Trop net."

    "Des caisses longent les murs."
    "Des machines de contrôle bourdonnent doucement."
    "Et au fond, il y a cette porte."
    "Impossible à ignorer."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("mara", "mefiant", 0.78),
    ])
    think "Ils ont vraiment pensé à tout."
    think "Même à la façon dont on allait oublier qu’on dépend d’eux."

    "Près de la porte, quelqu’un est déjà là."
    "Une femme."
    "Immobile."
    "Bras croisés."
    "Le regard fixé sur le sas, comme si elle attendait qu’il fasse une erreur."


    noam hesitation "…"
    noam hesitation "Euh…"
    noam hesitation "Salut."

    mara jaloux "Hein ?"
    mara taquin "Putain, c’est toi qui traînes ici ?"
    mara sourire "Salut, le stalker."

    pause 0.2

    noam taquin "Hein ?!"
    noam reflexion "Désolé, je voulais pas te faire peur."
    noam reflexion "C’est juste que…"
    noam reflexion "je pensais pas tomber sur quelqu’un ici."

    mara doute "Ouais…"
    mara doute "Les gens passent, matent la porte deux secondes,"
    mara doute "captent que c’est fermé à double tour,"
    mara doute "et se barrent direct comme des rats."
    mara taquin "Ils ont pas les couilles de rester."

    noam sourire "Et toi ?"

    mara sourire "Moi je reste."
    mara sourire "J’aime bien savoir exactement comment tout peut partir en vrille."
    mara sourire "Rien de tel que de connaître chaque recoin pourri d’un endroit."
    mara taquin "Ça permet de mieux anticiper le moment où ça va chier."

    pause 0.3

    noam neutre "J'imagine que tu viens d'Axiome alors ?"
    noam neutre "Moi c'est Noam."
    noam neutre "District [codex_dialogue_link('harmonie', 'HARMONIE')]."

    mara neutre "Mara."
    $ unlock_character_name("mara")
    mara sourire "Et ouais, bingo : Axiome pur jus."

    noam taquin "Ah."
    noam taquin "D'où le côté un peu professionnel."

    mara rire "Seulement un peu ?"

    pause 0.3

    "Je m’approche d’une caisse."
    "Elle est lourde."
    "Même sans l’ouvrir, on le sent."

    noam reflexion "Tu crois que ce sas sera utile ?"

    mara doute "Euh… ouais."
    mara doute "Normalement, les livraisons tombent une fois par semaine."
    mara reflexion "C’est huilé au millimètre : J7, J14, J21, J28."
    mara reflexion "Toujours pile à la même heure, comme des horloges suisses."
    mara taquin "Très rassurant, hein ?"

    noam surpris "Ils ont déjà prévu tout ça ?"
    noam surpris "Genre…"
    noam surpris "jusqu’à la fin du Conclave ?"

    mara doute "Au moins on est surs d'avoir des livraisons régulièrement."

    pause 0.3

    think "Même la nourriture arrive sous calendrier strict."

    noam sourire "C’est con, mais…"
    noam sourire "savoir que ça arrive toutes les semaines, ça rassure."

    mara stress "Ouais… c’est exactement pour ça que ça me fout les jetons."

    pause 0.3

    noam inquiet "Pourquoi ?"

    mara stress "Parce que si un truc déconne…"
    mara stress "si on a besoin d’un médoc, de bouffe en plus, d’un câble USB ou que sais-je…"
    mara stress "bah on attend sagement le prochain jour J."
    mara doute "Et si c’est pas le bon jour… on crève la dalle ou on crève tout court."
    mara sourire "Super planning, Kami. Vraiment top."
    pause 0.4

    "Je regarde la porte."
    "Puis les combinaisons."
    "Puis les caisses."

    think "Même l’espoir arrive emballé."

    pause 0.4

    think "Je devrais aller voir ailleurs."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_8

    $ hideGroup()
    jump LIVRAISON_TP

# 1m20
# Total : 52m45
