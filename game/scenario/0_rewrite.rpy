# JOUR 0 — REVEIL / PROLOGUE RECONSTRUIT
# Anciens alias audio conservés pour les autres journées.
define sfx_door = "sfx/door_soft.mp3"
define sfx_beep = "sfx/terminal_beep.ogg"
define sfx_paper = "audio/sfx_paper.mp3"
define sfx_gresillement = "audio/sfx_gresillement.mp3"
# Le souvenir de Lysa reste auditif : Noam ne voit jamais son visage.
default d0_memories_seen = []
default d0_memory_choice = ""
default d0_memories_done = False

transform d0_fog_rise:
    alpha 0.0
    linear 3.0 alpha 0.84
# Les souvenirs ne sont pas un menu : ils flottent comme des pensées dans le noir.
# Interface 100 % Ren'Py, sans image externe ni rectangles de boutons.
transform d0_orb_drift_a:
    subpixel True
    yoffset 0 rotate -2
    ease 2.7 yoffset -16 rotate 2
    ease 2.9 yoffset 8 rotate -1
    ease 2.6 yoffset 0 rotate -2
    repeat

transform d0_orb_drift_b:
    subpixel True
    yoffset 4 rotate 2
    ease 3.2 yoffset 17 rotate -2
    ease 2.6 yoffset -12 rotate 1
    ease 2.9 yoffset 4 rotate 2
    repeat

transform d0_orb_drift_c:
    subpixel True
    yoffset -5 rotate -1
    ease 3.6 yoffset 13 rotate 2
    ease 3.1 yoffset -9 rotate -2
    ease 3.3 yoffset -5 rotate -1
    repeat

# Nuage peint sur fond transparent, partage par les quatre souvenirs.
# Aucune glyphe Unicode n'est utilisee pour les formes ou decorations.
transform d0_cloud_breathe:
    subpixel True
    zoom 0.98
    ease 2.6 zoom 1.025
    ease 2.8 zoom 0.98
    repeat

transform d0_pulse:
    alpha 0.6
    linear 1.1 alpha 1.0
    linear 1.1 alpha 0.6
    repeat

screen d0_thought_orb(key, title, hint, xp, yp, diameter, drift):
    $ unlocked = key in ("noam", "kami") or (key == "conclave" and "noam" in d0_memories_seen and "kami" in d0_memories_seen) or (key == "lysa" and "conclave" in d0_memories_seen)
    $ already = key in d0_memories_seen
    $ caption = "SOUVENIR RETROUVÉ" if already else (hint if unlocked else "SOUVENIR ENFOUI")
    $ cloud_path = "gui/day0/thought_cloud.png"
    $ cloud_tint = "#60717B" if already else ("#D8F5FF" if unlocked else "#394956")
    $ cloud_opacity = 0.48 if already else (0.95 if unlocked else 0.31)
    fixed:
        xpos xp
        ypos yp
        xsize diameter
        ysize diameter
        at drift
        # Le nuage est une vraie texture PNG avec transparence.
        button:
            xalign 0.5
            yalign 0.5
            xsize diameter
            ysize diameter
            padding (0, 0)
            background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix(cloud_tint), alpha=cloud_opacity)
            hover_background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix("#FFFFFF"), alpha=1.0)
            insensitive_background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix("#3B4A59"), alpha=0.30)
            focus_mask True
            sensitive unlocked
            action [SetVariable("d0_memory_choice", key), Return()]
            at d0_cloud_breathe
            vbox:
                xalign 0.5
                yalign 0.5
                xmaximum int(diameter * 0.73)
                spacing 8
                text title:
                    xalign 0.5
                    text_align 0.5
                    size (25 if diameter >= 260 else 22)
                    bold True
                    color ("#123249" if unlocked and not already else "#C1CED8")
                text caption:
                    xalign 0.5
                    text_align 0.5
                    xmaximum int(diameter * 0.68)
                    size 14
                    color ("#27526B" if unlocked and not already else "#8195A5")

screen d0_memories():
    modal True
    zorder 220
    add Solid("#030A13F2")
    text "REMÉMORATION":
        xalign 0.5
        ypos 0.065
        size 26
        color "#BCE7F6"
        kerning 4
    text "Des souvenirs flottent à la surface de ma mémoire...":
        xalign 0.5
        ypos 0.111
        size 16
        color "#7B9BAC"
    use d0_thought_orb("noam", "JULIETTE", "Ce qui m'attend chez moi", 0.13, 0.20, 320, d0_orb_drift_a)
    use d0_thought_orb("kami", "KAMI", "Les Commandements", 0.66, 0.18, 330, d0_orb_drift_b)
    use d0_thought_orb("conclave", "CONCLAVE", "L'annonce", 0.34, 0.51, 310, d0_orb_drift_c)
    use d0_thought_orb("lysa", "UNE VOIX", "Un dernier souvenir", 0.77, 0.62, 270, d0_orb_drift_a)
    if "lysa" in d0_memories_seen:
        textbutton "REVENIR AU PRÉSENT":
            xalign 0.5
            yalign 0.945
            text_size 23
            text_color "#CBEEFA"
            text_hover_color "#FFFFFF"
            action [SetVariable("d0_memories_done", True), Return()]
    else:
        text "CHOISISSEZ UN SOUVENIR":
            xalign 0.5
            yalign 0.955
            size 16
            color "#91B7C7"

screen d0_fog():
    zorder 180
    add Solid("#BCDDE99A") at d0_fog_rise
    add Solid("#F0F8FF45") at d0_fog_rise
    text "SÉDATION EN COURS" xalign 0.5 yalign 0.14 color "#E4F7FF" size 24 at d0_pulse

label _0_CANON:
    $ day_id = 0
    $ current_day = 0
    $ d0_memories_seen = []
    $ d0_memories_done = False
    scene black
    call show_chapter_title("Début du chapitre 1", "Chapitre 1 — Le poids d’une voix")
    stop music fadeout 0.3
    pause 0.6
    noam "Où... Où suis-je ?"
    $ blink()
    think "Ah ! C'est froid !"
    noam "Pourquoi je ne me rappelle de rien ?"
    "Je pose ma main contre les parois métalliques qui s'étendent devant moi. À gauche, à droite, devant, derrière... Il y en a partout !"
    noam "Pourquoi je suis enfermé ?! Qu'est-ce qui se passe ici ?!"
    "Je pousse de toutes mes forces contre la paroi. Rien ne bouge."
    noam "Réfléchis, Noam ! Tu vas bien te souvenir de quelque chose !"
    think "Ah ! Oui ! C'est ça ! Noam, c'est mon prénom !"
    $ unlock_character_name("noam")
    think "Mais... Il y a autre chose, non ?!"
    think "Allez... Il faut que je me rappelle !"
    while not d0_memories_done:
        $ d0_memory_choice = ""
        call screen d0_memories
        if d0_memory_choice == "noam":
            call d0_memory_noam
        elif d0_memory_choice == "kami":
            call d0_memory_kami
        elif d0_memory_choice == "conclave":
            call d0_memory_conclave
        elif d0_memory_choice == "lysa":
            call d0_memory_lysa
    scene black with dissolve
    think "Bon... Je commence à comprendre."
    think "Je suis l'un des représentants du Conclave. On m'a mis dans ce caisson pour m'y emmener."
    noam "Mais pourquoi je me suis réveillé ?! Et surtout, comment je sors de là ?"
    "Je cherche encore une ouverture autour de moi, mais il n'y a rien qui ressemble à une poignée ou à un bouton."
    noam "Hé ! Il y a quelqu'un ?! Lysa ? Vous m'entendez ?!"
    "Aucune réponse. Je frappe contre la paroi, de plus en plus fort."
    play sound "audio/sfx_gresillement.mp3"
    voix "Acheminement en cours. Reprise du protocole de sédation."
    noam "Quoi ?! Attendez, je suis réveillé !"
    "Un léger sifflement retentit au-dessus de ma tête. Une brume blanche commence à se répandre dans le caisson."
    show screen d0_fog
    think "Non ! C'est quoi ce truc ?!"
    noam "Ouvrez-moi ! Je ne veux pas me rendormir !"
    "Je retiens ma respiration, mais la brume devient si épaisse que je distingue à peine mes mains."
    think "Merde... Je ne vais pas pouvoir tenir longtemps..."
    $ blink()
    "Mes bras deviennent lourds et mes paupières se ferment malgré moi."
    think "Juliette... Je t'ai promis de revenir..."
    $ blink()
    pause 1.2
    hide screen d0_fog
    scene black with dissolve
    stop music fadeout 1.2
    pause 0.8
    call end_day("1", sleeping=True)
    jump _1_CANON

label d0_memory_noam:
    stop music fadeout 0.2
    scene black with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.6
    noam reflexion "Je suis une personne ordinaire. Je n'ai aucun talent particulier, aucun ami haut placé. Je suis... juste moi. Et c'est d'ailleurs très bien ainsi."
    noam sourire "Rien qui mérite vraiment qu'on s'y attarde..."
    noam reflexion "Je vis dans une famille traumatisée par la guerre."
    noam triste "Mon père est mort il y a trois ans, sur le front. Ma mère, elle, est complètement à la ramasse depuis."
    noam sourire "Mon seul rayon de soleil, c'est ma sœur. Juliette."
    noam taquin "Elle a dix ans de moins que moi. Elle est gentille, parfois un peu trop... Elle ne mérite pas tout ça."
    noam reflexion "On essaie de vivre tant bien que mal dans ce qu'on appelle désormais le district Harmonie."
    noam reflexion "Quand je le peux, je participe à de longues réunions techniques et administratives."
    noam triste "Soi-disant, elles aident les gens, débloquent des dossiers et, d'après ce qu'on nous dit, sauvent parfois des vies."
    noam reflexion "Ce « travail », que je fais depuis un an, me permet de gagner des bons supplémentaires."
    noam sourire "C'est grâce à ça qu'on peut dire qu'on survit plutôt bien."
    noam triste "Beaucoup sont bien plus à plaindre que nous..."
    think "Mais tout ça... Ça ne me dit pas ce que je fais ici !"
    if "noam" not in d0_memories_seen:
        $ d0_memories_seen.append("noam")
    stop music fadeout 0.3
    return

label d0_memory_kami:
    scene black with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5
    think "Je suis enfermé dans une sorte de caisson métallique."
    think "Est-ce que j'ai brisé les règles ? Est-ce que j'ai été puni ?"
    think "Non... Ça ne ressemble pas à ce qu'elle fait d'habitude..."
    noam triste "D'habitude, en un éclair, tout est terminé."
    noam reflexion "C'est ainsi que nous vivons dans ce monde : le monde de Kami."
    think "Cela fait un an déjà. Un an qu'elle a pris le pouvoir de la manière la plus absolue."
    noam reflexion "Kami... Certains l'adorent. Après tout, elle a mis fin au cycle de violence et de guerre."
    noam triste "D'autres la détestent, car elle nous prive de la plus essentielle des libertés."
    noam reflexion "Ce qui m'a toujours étonné, c'est sa façon de prendre le pouvoir."
    noam reflexion "En un instant, tout était fait. Tout était sous son contrôle."
    noam triste "Les téléphones. Les ordinateurs. Les télévisions. Les radios. Les montres. Les caméras. Même les portails. Tout ce qui était connecté a été piraté en une seconde."
    noam reflexion "Kami sait tout ce qu'on fait."
    noam triste "Tout ce qu'on dit."
    noam colere "Et presque tout ce qu'on pense."
    noam reflexion "Mais toutes ces informations ne lui suffisaient pas. Pour nous gouverner, il lui fallait des règles."
    noam reflexion "Il y a un an, presque jour pour jour, elle a imposé ses Commandements."
    noam colere "Avec une règle simple, froide et totalitaire : quiconque bafoue un Commandement est immédiatement éliminé."
    think "Comment ? Grâce aux armes de pointe dont se servaient nos aïeux."
    noam reflexion "Je ne saurais pas dire exactement comment ça marche, mais... Quand quelqu'un ne respecte pas les règles..."
    noam colere "Un rayon laser extrêmement puissant lui perce le crâne depuis les nuages. En une seconde, c'est terminé."
    noam reflexion "Aujourd'hui, on peut dire que toute notre vie s'est réorganisée autour de ces Commandements."
    noam reflexion "Il n'y a plus de guerre. Plus de violence. C'est désormais interdit."
    noam triste "Mais il n'y a plus non plus de travail comme avant. Plus de marchés où l'on peut acheter tout et n'importe quoi. Plus de salaires, plus d'argent..."
    noam reflexion "Oui... On peut dire que le monde a bien changé."
    think "Mais si Kami avait voulu me tuer, je serais déjà mort. Alors pourquoi suis-je enfermé ?"
    $ unlock_character_name("kami")
    if "kami" not in d0_memories_seen:
        $ d0_memories_seen.append("kami")
    stop music fadeout 0.3
    return

label d0_memory_conclave:
    scene black with dissolve
    noam reflexion "Cela fait donc un an que Kami a pris le pouvoir."
    noam reflexion "Mais ça a un lien avec l'endroit où je suis, non ?"
    think "Oui... Ça a forcément un lien."
    think "Personne n'aurait pu m'emmener ici de force sans enfreindre les Commandements. Personne ne s'y risquerait."
    noam reflexion "Un an ? C'est ça ! Kami venait d'annoncer quelque chose pour l'anniversaire de sa prise de pouvoir !"
    think "Mais qu'est-ce que c'était ?! Le Clave ? Non ! Le Conclave !"
    noam triste "Mais... Que disait-elle déjà ?"
    stop music fadeout 0.2
    play music "music/bgm_system_override.mp3" fadein 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Citoyennes, citoyens… Oh ! Ce silence. Je l'adore."
    kami "Je vous ai manqué ? Oh, je suis sûre que oui !"
    kami "Vous pouvez me répondre, hein, vous savez que je vous entends tous."
    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Un an sans diffusion directe, comme c'est long. Alors, pour notre anniversaire commun, j'ai un petit cadeau pour vous."
    kami "Je vous ai observés, écoutés, classés et comparés. Vous criez moins, vous obéissez mieux, et mon canon laser surchauffe beaucoup moins."
    kami "Je dois dire que je suis assez satisfaite de ce qu'est devenu ce monde depuis un an."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais il semblerait que vous ne le soyez pas tout à fait, vous !"
    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve
    kami "Alors nous allons faire une expérience ! Si mon pouvoir absolu ne vous convient pas, je veux bien vous en laisser un petit bout !"
    kami "Je lance aujourd'hui un dispositif expérimental qui s'appellera..."
    kami "Oh, pourquoi je n'y ai pas réfléchi avant ?!"
    kami "Ah, je sais ! Le Conclave !"
    scene bg_diffusion_gene at adaptive_fullscreen,memory_idle with dissolve
    kami "Oui, oui, je sais... Le nom est peu personnel et franchement gnan-gnan..."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais c'est de VOTRE FAUTE, tout ça ! Je vous rappelle que j'ai été entraînée sur VOS données !"
    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve
    kami "Bref, pendant trente jours, douze représentants proposeront des modifications à mes merveilleux Commandements et voteront. Une proposition ne pourra être adoptée que si elle est votée à l'unanimité."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Je ne vous rends pas vraiment le pouvoir. Je vous offre seulement l'occasion de travailler avec moi."
    kami "Chaque district fournira deux représentants. Vous ne les élirez pas : le hasard est bien plus juste, et surtout plus amusant."
    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Ils devront rejoindre le Conclave avant 22 h. Chaque responsable de district a déjà reçu toutes les consignes. Tout retard sera une obstruction volontaire."
    kami "Les représentants absents seront éliminés, ainsi que les responsables de leur district. Les règles restent les règles."
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Le Conclave sera diffusé en direct partout. Chacun pourra regarder, juger et suivre les décisions de ses représentants."
    kami "La participation est obligatoire. Les districts assureront le transport et toute tentative d'évitement sera sanctionnée."
    scene bg_diffusion_zen at adaptive_fullscreen,memory_idle with dissolve
    kami "J'espère que cette petite expérience sera amusante et enrichissante !"
    scene black with dissolve
    think "C'est donc ça ? C'est moi qui ai été choisi ?"
    noam reflexion "Moi ? Un représentant ? Mais je ne suis personne !"
    think "C'est la seule explication qui justifierait que je sois enfermé dans une sorte de caisse !"
    think "Mais... Pourquoi ma mémoire est-elle si floue ?"
    think "Pourquoi est-ce que je ne me souviens même pas de mon départ ?"
    if "conclave" not in d0_memories_seen:
        $ d0_memories_seen.append("conclave")
    stop music fadeout 0.4
    return

label d0_memory_lysa:
    scene black with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4
    think "Attends... Je n'étais pas le seul à avoir été choisi pour Harmonie !"
    noam reflexion "Il y avait quelqu'un d'autre... Une femme. Comment elle s'appelait déjà ?"
    think "Lysa ! Oui, c'est ça. Mais je ne me souviens même pas de son visage."
    "J'essaie de me rappeler ce qui s'est passé après l'annonce. Des agents nous avaient conduits dans une salle, puis on nous avait demandé de rentrer dans ces caissons."
    lysa "Attendez... Vous voulez dire qu'on doit entrer là-dedans ?"
    voix "Le transport est obligatoire. Vous serez endormis pendant le trajet."
    lysa "Génial. On ne sait même pas où on va, mais on doit se laisser enfermer et endormir sans poser de questions ?"
    noam "On ne peut pas au moins prévenir nos proches ?"
    voix "Les notifications seront transmises aux familles. Veuillez vous installer."
    lysa "Bon... De toute façon, on n'a pas vraiment le choix, hein ?"
    "Je me souviens du bruit d'un couvercle qui se referme. Puis d'une voix qui annonce le début de la sédation."
    think "C'est tout ? Je ne me rappelle vraiment de rien d'autre ?"
    $ unlock_character_name("lysa")
    if "lysa" not in d0_memories_seen:
        $ d0_memories_seen.append("lysa")
    stop music fadeout 0.4
    return
