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
    $ unlock_character_name("noam")
    scene black
    call show_chapter_title("Début du chapitre 1", "Chapitre 1 — Le poids d’une voix")
    stop music fadeout 0.3
    pause 0.7
    play sound "audio/sfx_gresillement.mp3"
    "Un claquement métallique me tire du sommeil. J'essaie de me redresser, mais mon front heurte une surface dure avant que je comprenne ce qui m'arrive."
    $ blink()
    think "Aïe... Qu'est-ce que c'est que ce truc ?"
    "Je pose les mains devant moi. Une plaque transparente, glaciale, me barre le passage. Sur les côtés, le métal ne laisse même pas assez de place pour tourner les épaules."
    noam "Hé ! Il y a quelqu'un ?!"
    "Je frappe contre la paroi. Le bruit est sourd, étouffé, et personne ne me répond."
    noam "Ouvrez ! Je suis réveillé, vous pouvez ouvrir !"
    "Je m'arrête pour reprendre mon souffle. Il y a une odeur de plastique neuf, un faible courant d'air sous mon visage, et un voyant vert qui pulse au-dessus de mes genoux."
    think "Un caisson... On m'a enfermé dans un caisson de transport ?"
    "Je cherche un verrou à tâtons, sans en trouver. Le pire, c'est que je suis incapable de me rappeler quand je suis entré ici."
    think "Je m'appelle Noam. Je sais où j'habite, je sais ce que je fais... Alors pourquoi est-ce que les dernières heures sont aussi floues ?"
    "Des images me reviennent sans ordre. Le visage de Juliette. Une voix diffusée sur tous les écrans. Une liste de noms."
    think "Attends... Si je reprends depuis le début, ça va revenir."
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
    think "Lysa. Harmonie. La sélection. Tout s'emboîte enfin."
    think "Ils m'ont emmené de force ? Non... Ils n'en avaient même pas besoin. Refuser un ordre de Kami, c'est signer son arrêt de mort."
    noam "Lysa ? Vous m'entendez ?"
    "Je tends l'oreille. Aucun bruit ne traverse la cloison. Le système de ventilation vient même de s'arrêter."
    play sound "audio/sfx_gresillement.mp3"
    voix "Acheminement confirmé. Protocole de sédation : reprise."
    noam "Quoi ? Non, attendez ! Je suis déjà réveillé !"
    "Un souffle s'échappe juste au-dessus de mon visage. Je retiens instinctivement ma respiration, puis un brouillard blanc se déploie derrière la vitre."
    show screen d0_fog
    "Je frappe une nouvelle fois, beaucoup plus fort, mais mes mains glissent contre la paroi et mes bras deviennent déjà difficiles à soulever."
    think "Non... Pas maintenant. Je ne sais même pas où ils m'emmènent..."
    $ blink()
    "J'essaie de fixer le voyant vert pour rester conscient. Sa lumière se dédouble, puis se perd dans la brume."
    think "Juliette... Il faut que je rentre."
    $ blink()
    pause 1.2
    hide screen d0_fog
    scene black with dissolve
    stop music fadeout 1.2
    pause 0.8
    call end_day("1", sleeping=True)
    jump _1_CANON

label d0_memory_noam:
    scene black with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.6
    think "Juliette. Avant les annonces, avant les agents, il y avait Juliette."
    "Je la revois assise devant notre petite table, occupée à plier soigneusement un dessin pour qu'il entre dans ma poche."
    noam "Tu sais que je peux aussi le garder à la maison ?"
    voix "Et comment tu ferais pour penser à moi pendant tes réunions interminables ?"
    noam "Je ne risque pas de t'oublier."
    voix "C'est ce que tu dis à chaque fois. Montre-moi quand même que tu l'as pris."
    "Je revois sa mine satisfaite lorsque je glisse le papier dans ma veste. Dix ans nous séparent, et pourtant c'est souvent elle qui fait semblant de veiller sur moi."
    think "Depuis la mort de papa, maman passe des journées entières sans nous adresser la parole. Les bons supplémentaires que je rapporte de mes réunions à Harmonie ne règlent pas tout, mais ils nous permettent de tenir."
    think "Je lui ai promis de rentrer après le travail. Je n'aurais pas dû faire une promesse aussi facile."
    $ d0_memories_seen.append("noam")
    stop music fadeout 0.3
    return

label d0_memory_kami:
    scene black with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5
    think "Kami. Impossible d'oublier ce nom, même avec la tête encore pleine de sédatif."
    "Une place publique me revient en mémoire. Un homme, devant un écran, s'était mis à hurler que les Commandements n'avaient aucune légitimité."
    voix "On ne peut pas vivre toute notre vie en demandant la permission !"
    "Quelqu'un l'avait supplié de se taire. L'homme avait levé le bras pour répondre, puis une lumière avait traversé la place."
    "Il était tombé avant que nous ayons le temps de comprendre."
    think "Les Commandements. Kami les a imposés après avoir pris le contrôle des réseaux, des infrastructures et des armes connectées. Depuis, une désobéissance suffit pour mourir."
    think "Il n'y a plus de guerre ouverte, c'est vrai. Mais personne n'ose même parler trop fort lorsque son nom apparaît sur un écran."
    "Dans mon souvenir, personne ne s'approche du corps. Nous restons immobiles, comme si le rayon pouvait encore revenir."
    $ unlock_character_name("kami")
    $ d0_memories_seen.append("kami")
    stop music fadeout 0.3
    return

label d0_memory_conclave:
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.4
    kami "Citoyennes, citoyens… Oh ! Ce silence. Je l'adore. Vous pouvez me répondre, hein, je vous entends tous !"
    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Voilà un an que nous vivons ensemble. Vous criez moins, vous obéissez mieux et, croyez-moi, mon canon laser me coûte bien moins cher en entretien."
    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais je vous sens frustrés. Vous aimeriez décider de quelque chose par vous-mêmes, pour changer ? Alors je vais vous faire un cadeau : le Conclave !"
    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve
    kami "Douze représentants, deux par district, trente jours pour proposer des modifications à mes Commandements. Une seule condition : chaque proposition devra obtenir l'unanimité."
    kami "Vous ne les élirez pas. Le hasard choisira pour vous, et je suis absolument certaine que personne n'y verra le moindre problème !"
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Les personnes sélectionnées devront se présenter avant vingt-deux heures. Un refus, un retard volontaire ou une tentative de fuite sera sanctionné. Le responsable du district aussi, si nécessaire."
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Ah, et tout sera diffusé en direct ! Faites-moi plaisir : soyez intéressants."
    scene black with dissolve
    "Puis viennent les noms. Je suis au milieu d'une salle bondée d'Harmonie, entouré de personnes qui fixent le même écran."
    voix "Représentants du district Harmonie : Lysa. Noam."
    think "Noam... C'est mon nom. Pas celui d'un autre."
    "Une chaise grince derrière moi. Personne ne vient me féliciter. Deux agents s'avancent dans l'allée, et je comprends que je ne rentrerai pas dîner."
    think "Juliette attend toujours que je revienne..."
    $ d0_memories_seen.append("conclave")
    stop music fadeout 0.4
    return

label d0_memory_lysa:
    scene black with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4
    "Un dernier souvenir revient, plus près du caisson. La salle de transit. Des pas, le frottement d'un vêtement et quelqu'un qui proteste derrière moi."
    voix "Deux représentants, deux boîtes métalliques... C'est une façon comme une autre de voyager. Vous auriez pu mettre un hublot, au moins."
    noam "Vous êtes Lysa ?"
    voix "Et toi, c'est Noam. Très bien, on a résolu le grand mystère des prénoms. Maintenant, quelqu'un peut m'expliquer pourquoi on doit dormir pendant le trajet ?"
    noam "J'aimerais bien le savoir aussi."
    lysa "Formidable. Deux représentants et pas une information utile à se partager."
    "Je me souviens de l'avoir entendue s'installer dans un autre caisson. Je n'ai jamais vu son visage."
    voix "Fermeture des unités. Sédation automatique."
    noam "Attendez ! On peut au moins prévenir nos familles ?"
    "La réponse est un claquement de serrure. Puis une odeur étrange, et le noir."
    $ unlock_character_name("lysa")
    $ d0_memories_seen.append("lysa")
    stop music fadeout 0.4
    return
