# -----------------------------------------------------------------------
# GYMNASE — même modèle que CANON
# - 2 persos seulement : Noam + Elias
# - Découverte : Elias s'entraîne / discussion légère
# - PNC : tapis / poids / vélo / ballon / retour
# -----------------------------------------------------------------------

default decouverte_gymnase = False



label GYMNASE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_337
    scene bg_gymnase at adaptive_fullscreen

    if not decouverte_gymnase and day_number() == 1:
        jump decouverte_gymnase

    $ pnc_room = "pnc_gymnase"
    call screen pnc_gymnase()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_gymnase():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("gymnase")
    use room_scene_interactions("gymnase")

    if social_free_time_active() and character_has_available_free_time("ryn"):
        imagebutton:
            idle Transform(character_image("ryn", "determine"), zoom=1.00)
            hover Transform(character_image("ryn", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.20
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "ryn"), Jump("FREE_TIME_CHARACTER_INTERACT")]
    if social_free_time_active() and character_has_available_free_time("elias"):
        imagebutton:
            idle Transform(character_image("elias", "neutre"), zoom=1.00)
            hover Transform(character_image("elias", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.90
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "elias"), Jump("FREE_TIME_CHARACTER_INTERACT")]


label gymnase1_douche:
    "Les douches sont impeccables. Trop impeccables."
    "Je lève les yeux et repère plusieurs caméras orientées vers les cabines."
    "Aucun angle mort. Et aucun brouilleur pour couper la surveillance."
    think "Qui irait se doucher là-dedans, à la vue de tous ?!"
    jump GYMNASE_TP


label gymnase1_porte_couloir_infirmerie:
    $ corridor_current = "infirmerie"
    jump EXIT_ROOM_TO_CORRIDOR


label gymnase1_terrain:
    "Les lignes du terrain sont nettes, comme si personne ne les avait encore franchies."
    "Il y a assez de place pour courir, jouer ou simplement oublier les murs pendant quelques minutes."
    think "Même la détente ressemble à une zone soigneusement délimitée."
    jump GYMNASE_TP


label gymnase2_banc:
    jump GYM_BANC_INTERACT

label GYM_BANC_INTERACT:
    if not social_free_time_active():
        jump GYM_PNC_POIDS

    $ events_left = sport_events_left_count()

    if events_left > 0:
        menu:
            "Faire une session de sport ? ([events_left] évènement(s) sport restant(s))"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP
    else:
        menu:
            "Faire une session de sport ? (Tous les évènements sport ont été découverts)"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP


label GYM_SPORT_MINIGAME:
    "Tu t'installes sur le banc et tu commences l'entraînement."

    call minijeu_halteres from _call_minijeu_halteres_free_time

    if mg_was_success:
        $ sport_event_label = pop_random_sport_event()
        if sport_event_label:
            call expression sport_event_label from _call_expression_sport_event
        else:
            "Tu termines ta séance, satisfait de tes progrès."
    else:
        "La série te casse le rythme, mais tu sauras mieux gérer la prochaine fois."

    if social_free_time_active():
        jump FREE_TIME_END

    jump GYMNASE_TP

label GYM_PNC_TAPIS:
    "Le tapis est encore tiède."
    "Quelqu'un a couru récemment."
    "Les réglages sont simples."
    "Vitesse. Inclinaison. Temps."
    think "Même ici, tout est calibré."
    jump GYMNASE_TP


label GYM_PNC_POIDS:
    "Des poids libres."
    "Des barres."
    "Des repères au sol comme dans une salle publique."
    "Mais tout est trop propre."
    "Trop rangé."
    think "On dirait un décor de pub."
    jump GYMNASE_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label GYM_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_gymnase:

    $ decouverte_gymnase = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "Il y a aussi un gymnase."
    think "Ils ont vraiment pensé à mettre de nombreuses salles différentes."

    pause 0.4

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_338
    scene bg_gymnase at adaptive_fullscreen with fade

    "Ça sent le caoutchouc."
    "Le produit de nettoyage aussi."
    "Comme partout dans les couloirs mais plus particulièrement là."

    "Un terrain est marqué sur le sol."
    "Il y a des tapis de courses, des machines et des poids parfaitement rangés."

    "Et au fond…"
    "Un type est en train de s'entraîner."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elias", "fatigue", 0.78),
    ])

    "Il fait une série."
    "Sans musique."
    "Sans parler."
    "Juste le bruit de sa respiration."
    "Et du métal."

    noam hesitation "…"
    noam hesitation "Salut."

    "Il termine sa lancée."
    "Repose la barre doucement."
    "Puis enfin, il me regarde."

    elias neutre "Salut, camarade ! Fais gaffe à la barre, elle a essayé de me tomber sur le pied tout à l'heure. Bon, j'avais oublié de la bloquer, aussi."

    noam sourire "Je pensais être seul."
    noam sourire "Visiblement non."

    elias fatigue "Moi, quand j'ai la tête qui chauffe, je viens soulever de la ferraille. Au moins, les haltères me font pas de discours."
    elias fatigue "Enfin... sauf quand je monte un appareil de travers. Mais ça, je m'en rends compte assez vite, en général."

    noam taquin "Ouais... J'imagine que c'est devenu une habitude depuis un an."

    "Il rit de façon courte."

    elias neutre "Oh, j'ai pas attendu Kami pour avoir besoin de me défouler, tu sais."
    elias neutre "Avant, à la Forge, ça pouvait te tomber dessus sans prévenir. Un tir, une bagarre, une machine qui te lâche entre les doigts..."
    elias neutre "Là, c'est pas la joie non plus, mais au moins Kami annonce la couleur. C'est déjà ça, j'imagine."
    elias raison "Faut pas se planter avec ses règles, quoi. C'est moins facile que de revisser un boulon."

    "Il marque une pause un instant."
    
    elias jaloux "Alors, on vit mieux qu'avant ou pas ? Pff... bonne question, ça."
    elias jaloux "Moi, j'en sais foutre rien. J'ai jamais été très doué pour les grandes questions."
    elias jaloux "Du coup, je fais ce que je sais faire : je bosse, je bricole, et quand ça me prend trop la tête, je viens courir. Enfin, j'essaie de courir sans me casser la gueule."

    pause 0.2
    "Je ne sais pas vraiment quoi répondre."
    "D'un côté, il touche juste. Le monde est plus paisible qu'autrefois."
    "Mais d'un autre, la moindre erreur entraine la mort."
    "Pas une simple punition."
    "La mort quoi."

    noam reflexion "Au fait, je m'appelle Noam."
    noam reflexion "Je viens du district [codex_dialogue_link('harmonie', 'HARMONIE')]."

    "Il hoche la tête, comme si ça validait une info dans sa tête."

    elias neutre "Elias ! Si tu cherches un truc à réparer, tu peux venir me voir. Enfin, si c'est moi qui l'ai cassé, je suis probablement déjà dessus."
    $ unlock_character_name("elias")
    elias neutre "AXIOME, quartier bas. La Forge, les ateliers, les mains pleines de cambouis... le grand luxe, quoi."

    noam surpris "AXIOME…"
    noam surpris "La Forge."

    elias content "Ouais, c'est ça."
    elias content "Là-bas, on fabrique tout un tas de trucs pour les autres. Et quand ça tombe en panne, devine qui se tape la réparation ?"

    "Il dit ça sans fierté particulière."
    "Mais il sait dans son timbre de voix que AXIOME est nécessaire à tout le monde."
    "D'un autre côté, chacun des districts est nécessaire aux autres."
    "C'est pour ça qu'ils ont été découpé ainsi. Pour empêcher les tensions et nous rendre tous dépendants des autres."

    noam reflexion "Tu t'entraînes pour quoi ?"

    elias rire "Pour dormir, déjà ! Après une bonne séance, je ronfle comme un compresseur."
    elias rire "Si je peux me faire une séance avant dix-huit heures, je vais pas me gêner. Ça me change de porter des caisses."
    elias rire "Par contre, j'espère qu'ils ont prévu des douches. La dernière fois, j'ai confondu le robinet d'eau chaude et celui de purge... mauvaise soirée."

    noam rire "Ah."
    noam rire "La meilleure raison."

    pause 0.3

    "Je m'approche du terrain."
    "Je regarde les repères au sol."
    "Ça me rappelle l'école."
    "Ça me rappelle avant."

    "Ça me rappelle qi'avant on était innocent et les problèmes nous passaient au dessus de la tête."

    elias ecoute "Et toi, Noam, tu bouges un peu ou t'es plutôt du genre à encourager les autres depuis le banc ?"

    noam hesitation "Avant, oui j'en faisais parfois."
    noam hesitation "Mais ça fait un moment que j'en ai pas fait …"
    noam hesitation "Je sais plus trop ce que je fais, honnêtement."

    elias fatigue "Justement, faut t'y remettre doucement. Si tu commences trop fort, après tu peux plus lever les bras pour manger."
    elias fatigue "Quand tout se barre en cacahuète, au moins t'as ça. Tu comptes tes répétitions, tu souffles et, pendant cinq minutes, t'oublies le reste."
    elias neutre "Enfin, en principe. Moi, j'ai déjà perdu le compte en plein milieu d'une série."

    pause 0.2

    noam taquin "Donc si je veux survivre ici…"
    noam taquin "Je dois courir et soulever des trucs."

    elias content "Et bois de l'eau, hein !"
    elias content "Et respire ! Ça paraît bête, mais faut pas oublier."
    elias content "Sinon, tu vas finir plié en deux. Je te dis ça parce que j'ai déjà essayé de m'entraîner en retenant mon souffle. Très mauvaise idée."

    noam sourire "Merci docteur."

    "Il souffle du nez."
    "Ça ressemble presque à un vrai rire."

    pause 0.3

    elias ecoute "Tu sais ce qui me fait marrer, quand même ?"
    elias ecoute "Ils nous collent un gymnase sur une station spatiale, avec des ballons et tout le bazar."
    elias ecoute "On dirait une colonie de vacances. Y manque plus que les moniteurs et les chansons autour du feu."
    elias ecoute "Bon, ça me dérange pas, moi. J'ai jamais eu les moyens d'aller en colo quand j'étais gosse. Ça compte, si on est prisonniers ?"

    noam reflexion "Ouais. Notre animateur est juste un peu plus cinglé que les autres."

    elias neutre "Voilà ! Par contre, j'irai pas demander à Kami de nous faire chanter."

    "Il regarde la machine de muscu."
    "Puis les lignes au sol."
    "Puis moi."

    elias inquiet "Trente jours enfermés ici... même avec une salle de sport, ça risque d'être coton."
    elias inquiet "Entre les votes et les embrouilles, on va pas beaucoup souffler, je te le dis."
    elias inquiet "Quand t'es crevé, tu fais des bourdes. Moi, j'en fais déjà quand je suis frais, alors imagine."

    noam inquiet "Tu crois que le sport change quelque chose ?"

    elias neutre "Changer le monde ? Non, faut pas rêver."
    elias neutre "Mais ça m'évite de ruminer. Et puis, quand quelqu'un a besoin d'un coup de main pour déplacer un machin lourd, je suis utile."

    pause 0.3

    "Je regarde le tapis puis les poids."

    think "Ils ne me font pas spécialement envie."
    think "Rien que l'idée d'avoir des courbatures me freine déjà."

    noam hesitation "Bon, allez fais moi une démo, Sensei !"
    noam hesitation "Histoire de faire semblant d'être normal dans ce monde chelou."

    elias content "Allez, viens ! Je te montre. Fais juste pas exactement comme moi, j'ai deux ou trois mauvaises habitudes."
    elias content "Regarde surtout où tu mets tes pieds et où tu poses tes mains."
    elias content "J'ai déjà laissé tomber un poids sur mes chaussures en voulant montrer le bon geste. Depuis, j'explique avant de faire le malin."

    noam sourire "Promis."

    pause 0.4

    "Pendant quelques minutes…"
    "Il me montre les postures à adopter, le rythme de respiration à avoir."

    "C'est bête."
    "C'est simple."
    "Et mine de rien, ça fait quand même du bien."

    pause 1.0
    
    "Après une longue série d'exercices."

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_3

    $ hideGroup()
    jump GYMNASE_TP

# Durée : 2m30
# Total : 49m15
