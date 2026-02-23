default persistent.pegi18 = False
default stat_physique = 0

default mg_target_reps = 10
default mg_reps = 0
default mg_progress = 0
default mg_energy = 1.0
default mg_value = 0.0
default mg_direction = 1
default mg_speed = 0.9
default mg_done = False
default mg_feedback = ""
default mg_feedback_color = "#f5f5f5"
default mg_time_left = 60.0
default mg_zone_start = 0.40
default mg_zone_end = 0.60
default mg_perfect_margin = 0.05
default mg_skip_scene_pick = False
default mg_was_success = False
default sport_events_pool = [
    "sport_event_001",
    "sport_event_002",
    "sport_event_003",
    "sport_event_004",
    "sport_event_005",
    "sport_event_006",
    "sport_event_007",
    "sport_event_008",
    "sport_event_009",
]
default sport_events_seen = []

default scenes_normales = ["scene_mg_normale_1"]
default scenes_patreon = ["scene_mg_patreon_1"]
default scenes_sexy = ["scene_mg_sexy_1"]

init python:
    def mg_reset():
        store.mg_reps = 0
        store.mg_progress = 0
        store.mg_energy = 1.0
        store.mg_value = 0.0
        store.mg_direction = 1
        store.mg_done = False
        store.mg_feedback = ""
        store.mg_feedback_color = "#f5f5f5"
        store.mg_time_left = 60.0

    def mg_tick(dt=0.02):
        if store.mg_done:
            return

        store.mg_time_left = max(0.0, store.mg_time_left - dt)
        store.mg_value += store.mg_direction * store.mg_speed * dt

        if store.mg_value >= 1.0:
            store.mg_value = 1.0
            store.mg_direction = -1
        elif store.mg_value <= 0.0:
            store.mg_value = 0.0
            store.mg_direction = 1

        if store.mg_time_left <= 0 or store.mg_reps >= store.mg_target_reps or store.mg_energy <= 0:
            store.mg_done = True

    def mg_click():
        if store.mg_done:
            return

        store.mg_reps += 1
        val = store.mg_value
        if store.mg_zone_start <= val <= store.mg_zone_end:
            center = (store.mg_zone_start + store.mg_zone_end) / 2.0
            if abs(val - center) <= store.mg_perfect_margin:
                store.mg_progress += 2
                store.mg_feedback = "Parfait !"
                store.mg_feedback_color = "#5ad45a"
            else:
                store.mg_progress += 1
                store.mg_feedback = "Correct."
                store.mg_feedback_color = "#f2c94c"
        else:
            store.mg_energy = max(0.0, store.mg_energy - 0.15)
            store.mg_feedback = "Raté..."
            store.mg_feedback_color = "#ff6b6b"

        if store.mg_reps >= store.mg_target_reps:
            store.mg_done = True

    def mg_is_successful():
        return store.mg_progress >= store.mg_target_reps

    def sport_events_left_count():
        return len(store.sport_events_pool)

    def pop_random_sport_event():
        if not store.sport_events_pool:
            return None
        picked = renpy.random.choice(store.sport_events_pool)
        store.sport_events_pool.remove(picked)
        store.sport_events_seen.append(picked)
        return picked

    def mg_pick_scene():
        pools = []
        if store.scenes_normales:
            pools.append(store.scenes_normales)
        if store.scenes_patreon:
            pools.append(store.scenes_patreon)
        if persistent.pegi18 and store.scenes_sexy:
            pools.append(store.scenes_sexy)

        if not pools:
            return None
        pool = renpy.random.choice(pools)
        return renpy.random.choice(pool)

screen minijeu_halteres():
    modal True
    zorder 200

    timer 0.02 repeat True action Function(mg_tick, 0.02)
    key "mouseup_1" action Function(mg_click)

    if mg_done:
        timer 0.05 action Return()

    frame:
        style "frame"
        xalign 0.5
        yalign 0.5
        xsize 980
        ysize 560

        vbox:
            spacing 14
            xalign 0.5

            text "ENTRAÎNEMENT AUX HALTÈRES" style "label_text" xalign 0.5
            text "Clique au bon moment pour enchaîner les répétitions." xalign 0.5

            fixed:
                xsize 620
                ysize 240
                xalign 0.5
                add Solid("#1c1c1c") xsize 620 ysize 240 xalign 0.5 yalign 0.5
                $ dumbbell_y = int(160 - (mg_value * 110))
                add Solid("#8f99a3") xpos 140 ypos dumbbell_y-10 xsize 40 ysize 40
                add Solid("#e6e6e6") xpos 180 ypos dumbbell_y xsize 260 ysize 18
                add Solid("#8f99a3") xpos 440 ypos dumbbell_y-10 xsize 40 ysize 40
                add Solid("#2d2d2d") xpos 130 ypos dumbbell_y-14 xsize 60 ysize 48
                add Solid("#2d2d2d") xpos 440 ypos dumbbell_y-14 xsize 60 ysize 48
                add Solid("#3f3f3f") xpos 200 ypos 190 xsize 220 ysize 6
                if renpy.has_image("noam neutre"):
                    add "noam neutre" xpos 30 yalign 1.0 zoom 0.5
                else:
                    text "NOAM" xpos 40 yalign 1.0

            hbox:
                spacing 24
                xalign 0.5
                vbox:
                    spacing 8
                    text "Énergie" xalign 0.0
                    bar value mg_energy range 1.0 xsize 520
                vbox:
                    spacing 8
                    text "Temps" xalign 0.0
                    bar value mg_time_left range 60.0 xsize 200

            text "Rythme" xalign 0.5
            fixed:
                xsize 720
                ysize 30
                add Solid("#2b2b2b") xsize 720 ysize 30
                $ zone_width = (mg_zone_end - mg_zone_start)
                add Solid("#3fa34d") xpos int(mg_zone_start * 720) xsize int(zone_width * 720) ysize 30
                add Solid("#f5f5f5") xpos int(mg_value * 720) xsize 8 ysize 30

            text "⬆   ⬇  (clic ou touche)" xalign 0.5
            text "Répétitions : [mg_reps]/[mg_target_reps]" xalign 0.5

            if mg_feedback:
                text "[mg_feedback]" xalign 0.5 color mg_feedback_color

            textbutton "POUSSER" action Function(mg_click) xalign 0.5


screen physique_gain_anim():

    zorder 260
    modal True

    add Solid("#0008")

    frame at argument_unlock_appear:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        padding (60, 40)
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

        vbox:
            spacing 12
            text "STAT EN HAUSSE" at argument_unlock_pulse size 38 xalign 0.5 color "#be9c36"
            text "Physique +1" size 48 xalign 0.5 color "#000000"

    timer 2.0 action Hide("physique_gain_anim")

label minijeu_halteres:
    $ mg_reset()
    call screen minijeu_halteres

    $ mg_was_success = mg_is_successful()
    $ gained_physique = False
    if renpy.random.random() < 0.30:
        $ stat_physique += 1
        $ gained_physique = True

    if gained_physique:
        show screen physique_gain_anim
        pause 2.0
        hide screen physique_gain_anim
        "Ta statistique Physique augmente."
    else:
        "Tu sens la fatigue, mais tu sais que ça finit par payer."

    if mg_skip_scene_pick:
        $ scene_label = None
        $ mg_skip_scene_pick = False
    else:
        $ scene_label = mg_pick_scene()
    if scene_label:
        call expression scene_label from _call_expression
    return

label scene_mg_normale_1:
    "Iris t'adresse un regard fier, comme si elle voyait les efforts s'accumuler."
    return

label scene_mg_patreon_1:
    "Elias rectifie ta posture d'une main sûre, sans un mot."
    return

label scene_mg_sexy_1:
    "Le contact s'attarde une seconde de trop, et la chaleur monte."
    return

label sport_event_001:
    $ unlock_gallery_image("sport001")

    scene sport001 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Il n’y a plus rien autour d'Elias."
    "Juste la barre et le chrono."

    elias "Quarante-huit secondes."

    "Ses bras tremblent."
    "Il ne cligne presque pas des yeux."

    elias "Pouah ! J'ai assez bien géré l'amplitude aujourd'hui..."

    "La barre descend."
    "Il contrôle la descnte."
    "Pas d’élan."

    elias "Allez ! Encore une."

    "Il pousse."
    "Mâchoire serrée."

    return

label sport_event_002:
    $ unlock_gallery_image("sport002")

    scene sport002 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le bruit de leurs mains résonne dans le gymnase."

    mara "Ha ! J't'avais dit que je tiendrais plus longtemps."

    "Sael ne retire pas sa main tout de suite."
    "Elle observe."
    "Calme."

    sael "Tu parles beaucoup pour quelqu’un qui tremblait à la dernière série."

    mara "Oh ça va."
    mara "Je transpirais, c’est tout."

    "Leurs épaules brillent encore."
    "Respiration haute."
    "Rythme rapide."

    sael "Ta posture était mauvaise."
    sael "Tu compenses avec le bas du dos."

    mara "Tu peux juste dire bravo, tu sais ?"

    "Un sourire discret passe sur le visage de Sael."

    sael "Bravo..."

    mara "Voilà."
    mara "C’était pas si compliqué."

    return

label sport_event_003:
    $ unlock_gallery_image("sport003")

    scene sport003 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La barre repose sur ses épaules."
    "Beaucoup trop lourde."

    tomas "Charge vérifiée."
    tomas "Amplitude correcte."

    "Ses jambes tremblent déjà."

    iris "Impressionnant."
    iris "Mais je te jure que si tu te fais mal tu te débrouilleras pour aller à l'infirmerie."

    "Il descend."
    "Lentement."

    nyra "Allez ! Maintenant il faut remonter !"

    tomas "Silence."

    "Il pousse."
    "Les dents serrées."
    "Un souffle brutal."

    "La barre remonte."

    iris "Acceptable."

    nyra "C'est vraiment pas mal !"

    tomas "O-Ouai..."

    return

label sport_event_004:
    $ unlock_gallery_image("sport004")

    scene sport004 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Elen et Ryn sont là. Ils ne parlent pas."
    "Ils tiennent."

    ryn "Alors t'abandonnes toujours pas ?"

    elen "Même pas en rêve."

    "Leurs bras tremblent."
    "Le sol est froid."
    "Le chrono tourne."

    ryn "T’as déjà les épaules qui lâchent."

    elen "C’est toi qui parle ?"

    "Une goutte tombe."
    "Puis une autre."

    ryn "Tu respires trop vite."

    elen "Et alors ?! J'en ai bien le droit !"

    "Silence."
    "Juste leurs souffles."

    "Ils tiennent encore."
    "Mais je ne vais pas rester là pour voir qui gagnera."

    return

label sport_event_005:
    $ unlock_gallery_image("sport005")

    scene sport005 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le gymnase est devenu… autre chose."

    julian "Bienvenue au Tournoi Nexus Extrême !"

    iris "Pourquoi il y a des cônes partout…"

    elen "Et pourquoi il y a une échelle au sol ?"

    julian "Parce que c’est un parcours multi-dimensionnel."

    nyra "Ça ne veut rien dire."

    tomas "Quel est l’objectif précis ?"

    julian "Coordination."
    julian "Endurance."

    iris "On voulait juste courir un peu…"

    "Julian déplie son tableau."
    "Flèches. Cercles. Points d’exclamation."

    tomas "Il y a une phase chantée. E-Euh, je suis pas très à l'aise !"

    julian "Oui ! C'est de la motivation sonore."

    elen "On doit vraiment passer dans le pneu là ?!"

    julian "Absolument."

    iris "Je déteste déjà."

    julian "C’est ça l’esprit du tournoi !"

    return

label sport_event_006:
    $ unlock_gallery_image("sport006")

    scene sport006 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le gymnase est presque vide maintenant. Juste elle."
    "Elen pose sa gourde. Respire profondément. Puis commence à s’étirer."
    "Bras levés haut, dos cambré, le tissu mouillé colle à sa peau comme une seconde peau."
    "Elle penche le buste sur le côté, une main glisse le long de sa hanche."
    "Le silence amplifie chaque souffle, chaque froissement de tissu."

    elen "…ah, ça tire bien là…"

    "Elle change de côté. La lumière bleue des néons trace des reflets sur ses abdos luisants."
    "Ses doigts effleurent le creux de sa taille, puis descendent un instant sur la sangle de son short."
    "Elle se redresse lentement, roule les épaules, fait craquer sa nuque."
    "Un sourire fatigué, mais satisfait."

    elen "Bon… séance terminée."

    "Elle attrape sa serviette, s’essuie le front, le cou… descend un peu plus bas entre ses seins."
    "Tu ne peux pas détourner les yeux. Elle est… magnétique."
    "La sueur qui perle encore sur son ventre plat. Les muscles qui roulent sous la peau quand elle bouge."
    "Canon. Vraiment canon."
    "Elle te remarque enfin. Un sourcil se lève."

    elen "Quoi ? Tu comptes rester planté là toute la journée ?"

    return

label sport_event_007:
    $ unlock_gallery_image("sport007")

    scene sport007 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Nyra est encore sur le banc, torse bombé, respiration lourde. La séance l’a vraiment cuite."
    "Elle attrape sa bouteille, la dévisse d’un geste fatigué."

    nyra "Putain… j’ai l’impression d’être un radiateur ambulant."

    "Sans réfléchir, elle penche la tête en arrière et renverse la bouteille au-dessus d’elle."
    "L’eau jaillit en filet large. Elle coule d’abord sur son front, glisse sur ses tempes, puis descend en cascade sur son visage, sa gorge, entre ses seins."
    "Le tissu noir ultra-fin devient instantanément transparent. Chaque goutte trace une ligne brillante sur sa peau rougie par l’effort."
    "Elle ferme les yeux, un petit soupir de soulagement lui échappe."

    nyra "…aaaaah, ça fait du bien…"

    "L’eau continue de ruisseler : sur son ventre contracté, le long des côtes, jusqu’à disparaître dans le creux de son nombril et plus bas."
    "Ses cuisses gainées de noir luisent maintenant. Quelques gouttes perlent sur le banc en dessous d’elle."
    "Elle rouvre les yeux, passe une main dans ses cheveux trempés pour les rejeter en arrière."
    "Un sourire paresseux, presque sensuel, apparaît sur ses lèvres."

    nyra "Bon… au moins je suis réveillée maintenant."

    "Elle pose la bouteille vide à côté d’elle, s’étire légèrement, le tissu collant soulignant chaque courbe."
    "Tu ne bouges pas. Difficile de détourner le regard."

    return
label sport_event_008:
    $ unlock_gallery_image("sport008")

    scene sport008 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le tapis s’est enfin arrêté. Lysa descend, jambes encore tremblantes de l’effort."
    "Elle pose les mains sur les hanches, inspire profondément, puis lève les bras haut au-dessus de la tête."
    "Dos cambré, poitrine qui se soulève, elle s’étire longuement comme pour évacuer toute la fatigue accumulée."
    "La sueur coule en filets réguliers : du front aux tempes, le long du cou, entre les seins, sur les abdos qui se contractent à chaque respiration."
    "Elle penche la tête d’un côté, puis de l’autre, fait craquer sa nuque avec un petit soupir satisfait."

    lysa "…ouf. Ça faisait longtemps que j’avais pas poussé comme ça."

    "Bras toujours en l’air, elle roule lentement les épaules, fait passer le poids d’une jambe sur l’autre."
    "Le tissu du crop top colle à sa peau, transparent par endroits. Les gouttes glissent sur son ventre, disparaissent sous la ceinture du short."
    "Elle descend les bras, attrape ses coudes derrière le dos et tire pour ouvrir la poitrine."
    "Un sourire fatigué illumine son visage. Elle a l’air épuisée… mais heureuse."

    lysa "Bon, je crois que j’ai mérité une bonne douche."

    "Elle secoue légèrement la tête pour chasser les gouttes de ses cheveux, puis me jette un regard en coin."

    lysa "T’as couru combien de km toi aujourd’hui ? Ou t’as juste regardé ?"

    return

label sport_event_009:
    $ unlock_gallery_image("sport009")

    scene bg_gymnase_douche at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La séance est finie. J'ai le corps lourd, muscles chauds. Je range les affaires en silence."
    "Direction les douches. Le couloir est désert, juste le bruit lointain de l’eau qui tombe."
    "Je pousse la porte entrouverte. La vapeur flotte déjà dans l’air."
    "Et là, elle est là."

    scene sport009 at adaptive_fullscreen with dissolve

    "De loin. Dos tourné. Sous le jet principal. L'eau cascade sur son dos, sur ses hanches, sur ses fesses rondes et luisantes."
    "Les cheveux blancs collés à la peau, les gouttes qui glissent le long de sa colonne et disparaissent dans le creux de ses reins."
    "Elle ne bouge presque pas. Juste les épaules qui se soulèvent doucement au rythme de sa respiration."
    "L’eau ruisselle partout."
    "Je reste immobile. À l’entrée. Sans un bruit. Sans un mot."
    "Mon cœur bat un peu plus fort. La vapeur rend tout ça un peu irréel."
    "Elle passe une main dans ses cheveux, rejette la tête en arrière un instant. Un soupir à peine audible."
    "Puis l’eau ralentit. Le jet devient filet. Puis gouttes. Puis rien."
    "Elle tend la main vers le robinet, coupe le débit."
    "On recule d’un pas. Puis d’un autre. La porte se referme doucement derrière nous sans un claquement."
    "Il ne faut pas qu'on me voit ici."
    "On s’éloigne dans le couloir. Pouls encore rapide. Image gravée."

    return