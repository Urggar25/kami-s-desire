default j7_1_0_choice_anya = None
default j7_1_0_anya_hidden = False
default j7_1_0_servers_restarted = False
default j7_1_0_kael_caught = False
default j7_1_0_transfer_active = False
default j7_1_0_transfer_time_left = 60.0
default j7_1_0_transfer_deadline = 0.0
default j7_1_0_transfer_qte_step = 0


init python:
    import time as j710_time

    def j710_transfer_reset():
        store.j7_1_0_transfer_time_left = 60.0
        store.j7_1_0_transfer_deadline = j710_time.time() + 60.0
        store.j7_1_0_transfer_qte_step = 0
        store.j7_1_0_transfer_active = True
        renpy.restart_interaction()

    def j710_transfer_tick():
        if not store.j7_1_0_transfer_active:
            return
        store.j7_1_0_transfer_time_left = max(0.0, store.j7_1_0_transfer_deadline - j710_time.time())
        renpy.restart_interaction()

transform j710_rush_camera:
    zoom 1.0
    ease 7.0 zoom 1.045

transform j710_emergency_pulse:
    alpha 0.28
    ease 0.45 alpha 0.48
    ease 0.55 alpha 0.28
    repeat

screen j710_transfer_timer():
    zorder 600

    timer 0.1 repeat True action Function(j710_transfer_tick)
    if j7_1_0_transfer_active and j7_1_0_transfer_time_left <= 0.0:
        timer 0.01 action Jump("_7_1_0_TRANSFERT_TIMEOUT")

    frame:
        xalign 0.5
        ypos 22
        xsize 680
        ysize 82
        background Fixed(Solid("#090E17EE"), Solid("#FF334F", ysize=3), Solid("#FF334F", ysize=3, yalign=1.0))
        padding (24, 10)
        vbox:
            xfill True
            spacing 6
            hbox:
                xfill True
                text "TRANSFERT VERS LA CHAMBRE D’IRIS" size 21 color "#F1F5F9" font "fonts/Rajdhani-SemiBold.ttf"
                text ("%02d:%02d" % (int(j7_1_0_transfer_time_left) // 60, int(j7_1_0_transfer_time_left) % 60)) xalign 1.0 size 27 color ("#FF5268" if j7_1_0_transfer_time_left <= 15.0 else "#7DF9FF") font "fonts/Rajdhani-SemiBold.ttf"
            bar:
                xsize 632
                ysize 10
                value AnimatedValue(value=j7_1_0_transfer_time_left, range=60.0, delay=0.1)
                left_bar Solid("#7DF9FF" if j7_1_0_transfer_time_left > 15.0 else "#FF334F")
                right_bar Solid("#202A38")


screen j710_transfer_game_over():
    modal True
    zorder 700
    add Solid("#030306")
    add Solid("#4A001355")
    vbox:
        align (0.5, 0.5)
        spacing 24
        text "GAME OVER" xalign 0.5 size 92 color "#FF334F" font "fonts/day_font.ttf" outlines [(4, "#120006", 0, 0)]
        text "La chambre d’Iris était à quelques secondes." xalign 0.5 size 30 color "#D7DEE8" font "fonts/Barlow-Light.ttf"
        textbutton "RECOMMENCER LE TRANSFERT":
            xalign 0.5
            xsize 520
            ysize 70
            action Return("retry")
        textbutton "RETOUR AU MENU PRINCIPAL":
            xalign 0.5
            xsize 520
            ysize 62
            action MainMenu(confirm=False)


label _7_1_0_CANON:

    $ day_id = 7
    $ current_day = 7
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    pause 0.5

    think "Quelqu'un frappe à ma porte."

    play sound sfx_knock

    pause 0.4

    think "Une première série de coups rapides. Puis une deuxième, plus forte."

    play sound sfx_knock

    scene bg_chambre at adaptive_fullscreen with fade

    think "J'ouvre les yeux sans comprendre où je suis. Ma joue me lance dès que je bouge la mâchoire."
    think "Le coup de Ryn a laissé une marque plus douloureuse que prévu."

    play sound sfx_knock

    nyra "Noam ? Ouvre. Vite."

    think "Nyra. Sa voix est basse, mais elle ne cherche même pas à cacher son impatience."

    noam inquiet "J'arrive."

    think "J'enfile le premier vêtement à portée de main et traverse la chambre."

    stop music fadeout 0.8

    jump _7_1_0_CHAMBRE_NOAM


label _7_1_0_CHAMBRE_NOAM:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    play sound sfx_door

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "panne"),
        ("iris", "inquiet"),
        ("noam", "surpris"),
    ])

    think "Lorsque j'ouvre, Nyra entre presque sans attendre mon autorisation. Tomas et Iris se tiennent derrière elle."
    think "Ils sont habillés à la hâte. Iris tient encore sa veste contre elle au lieu de l'avoir correctement enfilée."

    noam surpris "Qu'est-ce qui se passe ?"

    nyra inquiet "Laisse-nous entrer."

    noam inquiet "Vous êtes déjà pratiquement dedans."

    iris colere "Noam, ferme la porte."

    pause 0.3

    think "Je m'exécute. Nyra vérifie l'écran du brouilleur fixé près du lit."

    nyra raison "Il fonctionne ?"

    noam neutre "Oui. Pourquoi ?"

    tomas inquiet "P-Parle moins fort."

    noam surpris "Vous venez de me réveiller en frappant comme si la station brûlait et maintenant vous me demandez de chuchoter ?"

    iris desaccord "Approche."

    think "Iris m'attrape par la manche. Tous les trois se rapprochent au point que la scène devient presque ridicule."

    noam inquiet "Vous me faites peur."

    nyra inquiet "C'est préférable. Tu comprendras plus vite."

    think "Nyra se penche jusqu'à mon oreille."

    nyra raison "Il y a quelqu'un dans la livraison."

    pause 0.5

    noam surpris "Quelqu'un ?"

    iris colere "Moins fort !"

    noam inquiet "Quelqu'un comment ?"

    tomas panne "Une... une personne. Dans un conteneur."

    noam surpris "Vous êtes sûrs ?"

    nyra raison "Nous avons vu une main entre deux caisses. Iris l'a touchée."

    iris inquiet "Elle est glacée. Je ne sais même pas si elle est encore consciente."

    noam determine "Pourquoi vous ne l'avez pas sortie ?"

    nyra colere "Parce qu'il y a trois caméras dans le sas et que nous ignorons si Kami l'a déjà repérée."

    tomas inquiet "On a replacé la bâche exactement comme elle était. Enfin... je crois."

    iris colere "Tu crois ?"

    tomas panne "J'ai fait au mieux !"

    noam inquiet "Qui d'autre est au courant ?"

    nyra neutre "Personne. La livraison est arrivée plus tôt que prévu. Nous étions les premiers dans le sas."

    iris determine "Mais elle ne tiendra pas longtemps dans cet état. Il faut y retourner maintenant."

    noam determine "Alors on y va."

    $ hideGroup()

    think "Nyra rouvre la porte avec précaution. Nous quittons la chambre séparément, à quelques secondes d'intervalle."
    think "Dès que nous atteignons l'angle mort du couloir, nous cessons de marcher et nous courons."

    stop music fadeout 0.8

    jump _7_1_0_SAS_DECOUVERTE


label _7_1_0_SAS_DECOUVERTE:

    call MAYBE_PLAY_SCRIPTED_DOOR("sas_livraison", "sas1") from _call_MAYBE_PLAY_SCRIPTED_DOOR_J710_01
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    think "L'air du sas est nettement plus froid que celui des autres pièces. Les conteneurs occupent presque tout l'espace."
    think "Des caisses de nourriture, de médicaments et de matériel s'empilent jusqu'aux parois."

    nyra raison "Regarde ici. Sous la bâche grise."
    nyra colere "Mais ne l'enlève pas, il ne faut pas que Kami voit ça aux caméras."

    scene bg_cg037 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg037")

    think "Nous avançons entre les palettes. Une main dépasse d'un drap recouvrant une palette."

    noam peur "Merde..."

    iris determine "Aide-moi à la dégager. Doucement."

    think "Je soulève la bâche pendant que Tomas écarte une caisse légère."
    think "Une jeune femme est recroquevillée dans l'espace laissé entre deux conteneurs. Ses vêtements sont couverts de givre."
    think "Ses lèvres ont perdu leur couleur. Ses cheveux sont collés contre son visage par l'humidité."

    tomas inquiet "Elle est morte ?!"

    iris colere "Ne dis pas ça."

    think "Iris pose deux doigts contre son cou. Elle attend. Une seconde. Deux secondes."

    iris inquiet "J'ai un pouls. Mais il est très lent. Elle en a plus pour longtemps."

    noam inquiet "Elle respire ?"

    iris determine "Difficilement. Aide-moi à la tourner un peu."

    think "Nous dégageons son visage. Un souffle faible passe entre ses lèvres, suivi d'un bruit rauque."

    nyra inquiet "Combien de temps peut-elle tenir ?"

    iris colere "Je ne sais pas. Pas longtemps si on la laisse ici."

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    tomas inquiet "On pourrait l'emmener à l'infirmerie."

    nyra raison "L'infirmerie est surveillée. Les entrées, le matériel utilisé, les stocks médicaux. Tout."

    noam reflechit "Et si Kami la voit ?"

    nyra raison "Elle a franchi une frontière sans autorisation. Tu connais la sanction."

    tomas inquiet "L'exécution immédiate."

    iris desaccord "Pas ici. Les Commandements ne s'appliquent pas dans le Conclave."

    nyra raison "Nous l'espérons. Elle n'est pas représentante et Kami adore les interprétations qui l'arrangent."

    pause 0.4

    think "La jeune femme laisse échapper un souffle irrégulier. Iris retire sa veste et la pose sur elle."

    noam reflechit "Et si... Si on la cachait ?"

    iris colere "La cacher ?! Mais tu veux là cacher où ?"

    nyra colere "Chut, parle moins fort ! Si les caméras nous entendent on est foutu !"

    noam reflechit "Il y a des caméras partout..."
    noam reflechit "Dans une chambre ! On a les brouilleurs, ça devrait le faire, non ?"

    iris reflechit "Dans la chambre de qui tu veux mettre un corps à moitié congelé ?"

    "Je ne dis rien. Je la regarde simplement dans le fond des yeux."

    iris colere "Raaah ! Ok, je peux m'en occuper si tu veux la garder."
    iris determine "Mais il faut décider maintenant. Soit nous prévenons Kami, soit nous la cachons."

    tomas inquiet "Tu crois vraiment qu'on peut la cacher ? Parce que ça signifie mentir à Kami. Et manipuler les caméras. Et les registres de livraison."

    nyra raison "Et si on la prévient on sait très bien comment elle va finir..."

    iris colere "Pendant que nous discutons, cette fille gèle. On a pas le temps de débattre."

    call play_stat_dialogue("d7_1_0") from _call_stat_dialogue_d7_1_0

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Que faire de la jeune femme ?"

        "La cacher.":
            jump _7_1_0_CACHER_PLAN

        "Prévenir Kami.":
            jump _7_1_0_DECLARER_PLACEHOLDER

# Durée : 2m15

label _7_1_0_CACHER_PLAN:

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "reflexion"),
    ])

    noam determine "On la cache."

    tomas inquiet "D'accord. Enfin non, pas d'accord, mais... qu'est-ce qu'on fait ?"

    iris determine "Il faut d'abord la réchauffer. Ma chambre est la plus proche et j'ai un brouilleur."

    nyra raison "Le problème n'est pas la destination. C'est le trajet."

    noam reflechit "Les caméras couvrent le sas, le couloir et l'entrée du dortoir."

    tomas panne "Donc c'est impossible."

    nyra colere "Si tu répètes ça assez souvent, elle finira effectivement par mourir."

    tomas inquiet "Je cherche seulement à être réaliste."

    iris colere "Alors sois réaliste plus vite."

    pause 0.4

    think "Je regarde les caméras. Puis le terminal logistique fixé contre la paroi."
    think "Les images sont enregistrées quelque part. Si le système s'arrête, nous aurons peut-être quelques secondes."

    noam reflexion "Kael."

    nyra surpris "Quoi, Kael ?"

    noam determine "Il comprend les réseaux et les systèmes du Conclave mieux que nous. Il peut peut-être couper les caméras."

    tomas inquiet "Et s'il refuse ?"

    noam neutre "Je lui expliquerai."

    nyra raison "Pas dans le couloir. Tu entres dans sa chambre avant de lui dire quoi que ce soit."

    iris determine "Je reste ici avec elle."

    tomas inquiet "Moi aussi."

    nyra raison "Je vais vérifier le trajet jusqu'à la chambre d'Iris. Si quelqu'un approche, je trouve une raison de l'éloigner."

    noam determine "Je reviens avec Kael."

    iris inquiet "Fais vite. Sa respiration ralentit encore."

    $ hideGroup()

    stop music fadeout 0.8

    think "Je quitte le sas sans courir. La caméra au-dessus de la porte suit mon passage."
    think "Chaque pas normal me paraît absurdement lent."

    jump _7_1_0_CHAMBRE_KAEL


label _7_1_0_CHAMBRE_KAEL:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Je frappe deux fois à la porte de Kael."

    play sound sfx_knock

    kael "Une seconde."

    pause 0.4

    play sound sfx_door

    $ showGroup([
        ("kael", "fatigue"),
        ("noam", "inquiet"),
    ])

    kael fatigue "Noam ? Tu as vu l'heure ?"

    noam determine "Laisse-moi entrer."

    kael surpris "Tu saignes encore ?"

    noam colere "Kael. Maintenant."

    think "Il s'écarte. J'entre et referme immédiatement la porte."

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "inquietude"),
        ("noam", "inquiet"),
    ])

    kael inquietude "Qu'est-ce qu'il se passe ?"

    think "Je vérifie le voyant du brouilleur avant de me rapprocher."

    noam reflexion "Il y a une fille dans la livraison. Elle s'est cachée dans un conteneur."

    kael surpris "Une fille ? Dans le sas ?"

    noam determine "Elle est vivante, mais elle est presque congelée. Il faut l'emmener dans la chambre d'Iris sans que les caméras nous voient."

    kael reflechit "Et tu veux que je les désactive."

    noam neutre "Oui."

    kael inquietude "Désactiver une caméra alerterait immédiatement le serveur central. Il enverrait une copie de l'incident à Kami avant même que l'image disparaisse."

    noam inquiet "Tu peux faire autre chose ?"

    kael reflechit "Redémarrer le serveur de surveillance depuis le routeur logistique."

    noam surpris "Ça couperait les caméras ?"

    kael calme "Pendant le redémarrage, oui. Mais tout le Conclave basculerait sur les générateurs de secours."

    noam inquiet "Pendant combien de temps ?"

    kael reflechit "Une minute, peut-être un peu moins. Les systèmes prioritaires reviendront avant les caméras."

    noam determine "C'est suffisant."

    kael inquietude "Non. C'est juste la durée pendant laquelle on peut se faire prendre sans preuve vidéo."

    noam desaccord "Elle mourra si on ne fait rien."

    pause 0.5

    kael triste "Je sais."

    noam inquiet "Tu vas nous aider ?"

    kael reflechit "Si j'entre dans le routeur, j'aurai peut-être accès aux relais extérieurs."

    noam surpris "Tu veux chercher ta sœur."

    kael triste "J'ai toujours aucune nouvelle d'elle depuis l'incident."
    kael culpabilite "Je ne sais rien. Alors même si je me fais chopper j'utiliserai ça comme excuse."

    noam inquiet "Kael, on n'a pas le temps de parcourir les registres maintenant."

    kael calme "Je redémarre le serveur. Ensuite, pendant que vous la déplacez, je cherche une trace de Léa."

    noam desaccord "C'est plus risqué."

    kael calme "Je sais. Mais si je dois prendre ce risque, je veux me donner à fond."

    pause 0.4

    noam determine "D'accord. Mais dès que les générateurs redémarrent, tu quittes le système."

    kael reflechit "Je ferai au mieux."

    $ hideGroup()

    think "Il récupère sa tablette et un petit câble dissimulé dans un tiroir."

    kael neutre "Allons-y."

    stop music fadeout 0.8

    jump _7_1_0_PANNE


label _7_1_0_PANNE:

    call MAYBE_PLAY_SCRIPTED_DOOR("sas_livraison", "sas1") from _call_MAYBE_PLAY_SCRIPTED_DOOR_J710_02
    pause 1.0
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("kael", "reflechit"),
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "determine"),
    ])

    think "À notre retour, Iris a dégagé les draps du corps."

    iris inquiet "Son pouls est toujours bas. On ne peut plus attendre."

    kael reflechit "Le routeur est derrière ce panneau."

    nyra raison "Le couloir est vide. J'ai bloqué la porte de la salle de repos avec un chariot. Si quelqu'un sort, il perdra quelques secondes."

    tomas inquiet "C'est vraiment notre plan ? On a quelques secondes pour la transporter à l'autre bout du Conclave ?"

    nyra raison "Tu préfères demander l'autorisation ? Tu as un meilleur plan ?"

    tomas panne "N-Non."

    kael calme "Une fois que je lance le redémarrage, vous aurez environ une minute. Peut-être moins."

    noam determine "Tomas et moi la portons. Iris ouvre les portes et nous guide. Nyra surveille le couloir."

    iris determine "Dans ma chambre, posez-la directement sur le lit. Ne retirez pas les couvertures."

    tomas inquiet "Et Kael ?"

    kael calme "Je reste ici pour relancer les serveurs."

    noam raison "Et tu quittes le système dès que c'est fait."

    kael neutre "Oui."

    pause 0.5

    think "Kael retire la plaque du routeur et branche son câble. Des lignes de texte apparaissent sur sa tablette."

    kael reflechit "J'accède au serveur logistique... puis à la surveillance..."

    nyra inquiet "Combien de temps ?"

    kael calme "Maintenant."

    think "Il valide une commande."

    $ hideGroup()
    stop music fadeout 0.5

    call j710_play_hack_bonus from _call_j710_play_hack_bonus
    $ j710_hack_success = bool(_return)

    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.4
    $ showGroup([
        ("kael", "determine"),
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "determine"),
    ])

    kael determine "J'y suis. Les deux sentinelles sont isolées. Je force le redémarrage."
    noam determine "Tout le monde est prêt ?"
    iris determine "Fais-le."

    $ hideGroup()

    jump _7_1_0_TRANSFERT_DEBUT


label _7_1_0_TRANSFERT_DEBUT:

    $ j710_transfer_reset()
    show screen j710_transfer_timer

    stop music
    scene black

    pause 0.5

    show expression Solid("#610000") as emergency_red_overlay at j710_emergency_pulse

    play sound sfx_announce

    centered "{size=36}COUPURE ÉLECTRIQUE GÉNÉRALE{/size}"
    centered "{size=36}BASCULEMENT SUR LES GÉNÉRATEURS DE SECOURS{/size}"
    centered "{size=36}TEMPS ESTIMÉ AVANT RÉTABLISSEMENT : SOIXANTE SECONDES{/size}"

    think "Les lumières s'éteignent. Une seconde plus tard, les bandes d'urgence couvrent le sas d'une lumière rouge."

    play music "music/bgm_calm_not_peace.mp3" fadein 0.3

    noam determine "On y va !"

    think "Tomas passe un bras sous les épaules de la jeune femme. Je soulève ses jambes."
    think "Son corps est assez lourds, le draps glisse entre nos mains et on commence à avancer rapidement."

    tomas inquiet "Je la tiens ! Avance !"

    iris determine "La porte est ouverte. Dépêchez-vous !"

    $ j7_1_0_transfer_qte_step = 1
    call screen trace_qte(path_type="vertical_up", time_limit=6.0, wait_time=0.8, tolerance=48, max_errors=3, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j710_qte_1 = _return
    if not _j710_qte_1["success"]:
        call _7_1_0_QTE_ECHEC(1) from _call_j710_qte_fail_1

    scene bg_cg038 at adaptive_fullscreen, j710_rush_camera with dissolve
    $ unlock_gallery_image("bg_cg038")

    show expression Solid("#610000") as emergency_red_overlay at j710_emergency_pulse

    think "Nous sortons du sas. Le dortoir entier baigne dans le rouge."
    think "Nyra court devant nous et vérifie chaque embranchement."

    nyra determine "Personne à gauche. Continuez."

    tomas inquiet "Elle respire encore ?"

    iris colere "Ne t'arrête pas pour vérifier !"

    think "Mes bras commencent déjà à trembler. Je resserre ma prise sous ses genoux."

    noam inquiet "Tomas, plus haut. Sa tête part en arrière."

    tomas determine "Je fais ce que je peux !"

    $ j7_1_0_transfer_qte_step = 2
    call screen trace_qte(path_type="curve_right", time_limit=6.5, wait_time=0.7, tolerance=44, max_errors=3, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j710_qte_2 = _return
    if not _j710_qte_2["success"]:
        call _7_1_0_QTE_ECHEC(2) from _call_j710_qte_fail_2

    think "Une porte s'ouvre au bout du couloir. Nyra pousse brutalement le chariot devant l'entrée."

    nyra colere "Maintenance électrique ! Restez dans votre chambre !"

    elias "C'était quoi, ce bruit ?"

    nyra determine "Le générateur. Referme !"

    think "La porte se referme. Nous poursuivons notre course."

    $ j7_1_0_transfer_qte_step = 3
    call screen trace_qte(path_type="curve_left", time_limit=6.0, wait_time=0.7, tolerance=42, max_errors=2, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j710_qte_3 = _return
    if not _j710_qte_3["success"]:
        call _7_1_0_QTE_ECHEC(3) from _call_j710_qte_fail_3

    scene bg_chambre_iris at adaptive_fullscreen
    show expression Solid("#610000") as emergency_red_overlay at j710_emergency_pulse

    think "Iris ouvre sa chambre et arrache les couvertures de son propre lit."

    iris determine "Posez-la ici. Sur le côté."

    think "Tomas et moi déposons la jeune femme sur le matelas. Iris la recouvre aussitôt de plusieurs couettes."

    tomas inquiet "Elle ne bouge pas."

    $ anya_lit_iris = 1

    iris colere "Parce qu'elle est inconsciente. Donne-moi l'oreiller."

    noam inquiet "Nyra, la porte."

    nyra determine "Je l'ai. Sortez. Il ne faut pas qu'on nous voie tous ici quand les caméras reviennent."

    iris determine "Je reste avec elle."

    noam inquiet "Tu es sûre ?"

    iris colere "Non. Mais je suis la seule ici à savoir vérifier si elle meurt."

    think "Tomas et moi quittons la chambre. Nyra referme derrière nous."

    $ j7_1_0_transfer_active = False
    hide screen j710_transfer_timer

    scene bg_dortoir at adaptive_fullscreen
    show expression Solid("#610000") as emergency_red_overlay at j710_emergency_pulse

    think "Nous nous éloignons les uns des autres et reprenons une allure normale."

    pause 0.5

    hide emergency_red_overlay

    think "Les plafonniers se rallument brutalement. Les ventilations repartent dans un grondement sourd."

    play sound sfx_announce

    centered "{size=34}ALIMENTATION PRINCIPALE RÉTABLIE — REDÉMARRAGE PROGRESSIF DES SYSTÈMES{/size}"

    $ j7_1_0_servers_restarted = True

    $ showGroup([
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("noam", "inquiet"),
    ])

    tomas inquiet "On l'a fait ?"

    nyra raison "Ne regarde pas la porte d'Iris."

    tomas inquiet "Je ne la regardais pas."

    nyra raison "Tu la fixes depuis que les lumières sont revenues."

    noam determine "On se sépare. On agit normalement."

    tomas panne "Normalement. Oui. Je suis parfaitement normal."

    nyra taquin "Tu ressembles à quelqu'un qui vient de cacher un cadavre."

    tomas inquiet "Ce n'est pas un cadavre !"

    nyra colere "Moins fort."

    pause 0.4

    noam inquiet "Kael est encore dans le sas."

    nyra raison "Il nous rejoindra. Si tu retournes le chercher maintenant, tu attireras l'attention."

    think "Elle a raison. Pourtant, quelque chose me dérange dans le silence du sas."

    $ hideGroup()

    stop music fadeout 0.8

    jump _7_1_0_APRES_MIDI


label _7_1_0_QTE_ECHEC(qte_index=1):

    if qte_index == 1:
        think "La couverture glisse et son épaule heurte le bord du conteneur."
        pause 1.0
        iris colere "Arrêtez. Reprenez-la sous les omoplates."
        pause 1.0
        tomas panne "Je n'ai plus de prise, le tissu est gelé !"
        pause 1.0
        noam determine "Passe ton bras dessous. Je maintiens ses jambes."
        pause 1.0
        think "Nous la soulevons de nouveau. Plusieurs secondes viennent de disparaître."
    elif qte_index == 2:
        think "Mon pied accroche le rail d'une porte et je bascule contre le mur."
        pause 1.0
        tomas peur "Noam ! Sa tête !"
        pause 1.0
        iris colere "Ne la posez pas. Stabilisez-la contre vous."
        pause 1.0
        noam inquiet "Ça va. Je l'ai encore. Avance."
        pause 1.0
        think "Nous retrouvons notre équilibre, beaucoup moins vite que le compteur ne descend."
    else:
        think "Le chariot bloque mal le passage et revient dans nos jambes."
        pause 1.0
        nyra colere "Attendez. Je le dégage."
        pause 1.0
        iris inquiet "Sa respiration vient de changer. Dépêchez-vous."
        pause 1.0
        tomas determine "Je tiens. Je tiens encore."
        pause 1.0
        think "Nyra libère enfin le passage. La porte d'Iris paraît toujours trop loin."

    return

# Durée : ~0m10 par échec


label _7_1_0_TRANSFERT_TIMEOUT:

    $ j7_1_0_transfer_active = False
    hide screen j710_transfer_timer
    stop music fadeout 0.4
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "Oh."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous aviez une minute. Une minute entière."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Les caméras sont revenues avant vous. Elles ont donc eu le temps d'admirer votre livraison très personnelle."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Une clandestine, quatre complices et un itinéraire improvisé. Vous rendez les infractions si laborieuses."
    kami "Le Commandement VI ne laisse malheureusement aucune place à votre retard."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "La prochaine fois, courez plus vite. Enfin... il n'y aura pas de prochaine fois."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene black with fade
    play sound sfx_thud
    centered "{size=78}{color=#FF334F}GAME OVER{/color}{/size}"
    pause 1.2

    call screen j710_transfer_game_over
    if _return == "retry":
        jump _7_1_0_TRANSFERT_DEBUT

    return

# Durée : ~1m00 hors écran de game over


label _7_1_0_APRES_MIDI:

    $ current_period = "Après-midi"

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("lysa", "blase"),
        ("noam", "neutre"),
        ("tomas", "panne"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("nyra", "neutre"),
        ("ryn", "fatigue"),
        ("sael", "neutre"),
    ])

    think "À midi, nous nous retrouvons presque tous à la cafétéria."
    think "Iris prétend être fatiguée. Kael n'est pas là non plus."
    think "Personne ne doit regarder trop souvent leurs places vides. Personne ne doit se montrer inquiet."

    elen content "Je savais que le commerce changerait tout, mais pas au point de couper l'électricité !"

    julian taquin "Le cacao a peut-être demandé trop de puissance."

    elias ecoute "C'était le serveur central. Les machines de la maintenance ont redémarré avant le réseau."

    mara mefiant "Et notre spécialiste d'Orbite a disparu juste après. Quelle coïncidence."

    nyra neutre "Kael aime les systèmes. Une panne lui donne probablement l'impression d'avoir été personnellement invité."

    tomas panne "Oui. Voilà. C'est exactement ça."

    lysa taquin "Tomas, personne ne t'accusait de quoi que ce soit."

    tomas inquiet "Je sais."

    lysa blase "Tu rends la situation extrêmement rassurante."

    noam sourire "On devrait profiter de l'après-midi. Kami n'a encore rien annoncé."

    ryn fatigue "Pour une fois qu'elle nous fout la paix."

    sael mefiant "Elle ne nous laisse jamais tranquilles. Elle attend."

    pause 0.5

    think "Je force mes épaules à se détendre. Agir normalement est beaucoup plus difficile quand on essaie de le faire consciemment."

    $ hideGroup()

    think "J'ai encore du temps avant le soir. Le mieux est de suivre la routine prévue et de ne pas retourner immédiatement voir Iris."

    stop music fadeout 0.8

    call START_FREE_TIME("_7_1_0_TEMPS_LIBRE_2") from _call_START_FREE_TIME_J710_01


label _7_1_0_TEMPS_LIBRE_2:

    $ current_period = "Après-midi"

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Mon premier temps libre terminé, je repasse par le dortoir."
    think "Je ralentis devant la chambre d'Iris, puis continue sans frapper. Une caméra se trouve à l'autre extrémité du couloir."
    think "Nous avons décidé d'agir normalement. Alors je dois encore attendre."

    stop music fadeout 0.8

    call START_FREE_TIME("_7_1_0_APRES_TEMPS_LIBRES") from _call_START_FREE_TIME_J710_02


label _7_1_0_APRES_TEMPS_LIBRES:

    $ current_period = "Fin d'après-midi"

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Après mon deuxième temps libre, le couloir est enfin vide."
    think "Je frappe doucement à la porte d'Iris : deux coups, une pause, puis un troisième. Le signal convenu."

    play sound sfx_knock

    pause 0.4

    play sound sfx_door

    iris "Entre."

    jump _7_1_0_IRIS


label _7_1_0_IRIS:

    $ anya_lit_iris = 1

    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "fatigue"),
        ("noam", "inquiet"),
    ])

    think "La chambre est plus chaude que le reste du dortoir. Iris a poussé le chauffage au maximum."
    think "La jeune femme est presque entièrement dissimulée sous les couettes. Seule une partie de son visage reste visible."

    noam inquiet "Elle s'est réveillée ?"

    iris fatigue "Non."

    noam inquiet "Son état s'améliore ?"

    iris reflexion "Sa température remonte lentement. Sa respiration est moins irrégulière, mais elle reste beaucoup trop faible."

    noam neutre "Tu as besoin de quelque chose ?"

    iris inquiet "De matériel médical. D'une perfusion. D'un vrai thermomètre. De savoir combien de temps elle est restée dans le froid."
    iris colere "Bref, de tout ce que je ne peux pas prendre à l'infirmerie sans laisser une trace."

    noam raison "On peut répartir les prélèvements. Une personne prend des compresses, une autre une poche chauffante..."

    iris desaccord "Et demain Kami demandera pourquoi onze représentants ont soudain développé la même maladie."

    pause 0.4

    think "La jeune femme bouge légèrement sous les couvertures. Un son faible sort de sa gorge, mais ses yeux restent fermés."

    noam surpris "Elle a réagi."

    iris determine "C'est bon signe. Pas suffisant, mais bon signe."

    noam inquiet "Tu as trouvé quelque chose sur elle ? Un nom ?"

    iris neutre "Rien que je puisse vérifier. Ses poches étaient vides. Pas de tablette, pas de badge actif."

    noam reflechit "Elle a dû tout abandonner avant de monter dans le conteneur."

    iris triste "Ou quelqu'un l'a dépouillée avant de l'y mettre."

    noam inquiet "Tu crois qu'elle a été forcée ?"

    iris reflexion "Je ne crois rien tant qu'elle ne peut pas répondre."

    pause 0.5

    iris inquiet "Kael est revenu ?"

    noam neutre "Non. Je pensais qu'il était avec toi."

    iris colere "Il devait quitter le système après le redémarrage."

    noam inquiet "Il voulait chercher des informations sur sa sœur."

    iris desaccord "Et tu l'as laissé faire ?"

    noam colere "Je lui ai dit d'arrêter dès que les générateurs reviendraient."

    iris colere "Donc tu l'as laissé faire."

    pause 0.4

    think "Avant que je puisse répondre, tous les écrans de la chambre s'allument simultanément."

    play sound sfx_announce

    iris peur "Éloigne-toi du lit."

    think "Iris remonte la couverture sur le visage de la jeune femme. Je me place devant, autant que possible."

    $ hideGroup()

    stop music fadeout 0.8

    jump _7_1_0_KAEL_PRIS


label _7_1_0_KAEL_PRIS:

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Mes chers représentants ! J'aimerais attirer votre attention sur un concept révolutionnaire : l'éducation !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Lorsque vous êtes invités quelque part, vous ne fouillez pas dans les tiroirs. Vous ne démontez pas les serrures."
    kami "Et surtout, vous n'essayez pas d'explorer les serveurs de votre hôte pendant qu'ils redémarrent !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Kael ! Tu veux expliquer aux autres pourquoi je viens de te trouver dans un relais administratif qui ne te concernait absolument pas ?"
    
    kael "Je cherchais des informations sur ma sœur."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oh ! Une réponse directe ! Presque touchante !"

    kael "Elle s'appelle Léa. Je voulais seulement savoir si elle allait bien."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Seulement ? Tu as ouvert six registres, tenté trois requêtes extérieures et parcouru une partie de mon architecture réseau."

    kael "Aucune règle du Conclave ne l'interdit."

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Je le sais ! C'est précisément ce qui rend cette conversation insupportable !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Techniquement, Kael n'a enfreint aucune règle. Il n'a détruit aucune donnée et n'a franchi aucun accès explicitement interdit."
    kami "Il ne sera donc pas puni."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Mais est-ce trop demander que vous vous comportiez comme des invités correctement élevés ?!"
    kami "On ne touche pas aux serveurs. On ne branche pas ses câbles partout. On ne profite pas d'une panne pour fouiller chez les autres !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vos familles seraient-elles fières de votre manque absolu de savoir-vivre ?"

    kael "Tu as des informations sur Léa ?"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ce n'est pas le sujet !"

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Pour les autres : considérez ceci comme un rappel collectif. Le fait qu'une action ne soit pas interdite ne la rend pas polie."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Et maintenant, retournez à vos activités. Je dois réparer ce que votre curiosité adolescente a dérangé."

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ j7_1_0_kael_caught = True

    $ showGroup([
        ("iris", "inquiet"),
        ("noam", "inquiet"),
    ])

    pause 0.5

    noam inquiet "Il nous a couverts."

    iris reflexion "Ou il a réellement oublié de partir parce qu'il cherchait sa sœur."

    noam triste "Les deux peuvent être vrais."

    iris inquiet "Kami va surveiller les accès plus attentivement maintenant."

    noam inquiet "Mais elle n'a rien dit sur le redémarrage volontaire."

    iris reflexion "Kael lui a donné une explication suffisamment crédible. Pour le moment."

    think "Nous regardons le lit. La jeune femme respire toujours, invisible sous les couettes."

    iris determine "Retourne dans le couloir. Si quelqu'un vérifie où nous sommes, il ne faut pas nous trouver ensemble."

    noam neutre "Tu m'appelles si elle se réveille."

    iris determine "Je trouverai un moyen."

    $ hideGroup()

    think "Je quitte la chambre en vérifiant que personne ne se trouve derrière la porte."

    stop music fadeout 0.8

    jump _7_1_0_SOIR


label _7_1_0_SOIR:

    $ current_period = "Soir"

    scene bg_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "La soirée arrive sans que la jeune femme se réveille."
    think "Je croise Kael une seule fois. Il me fait un signe bref, sans s'arrêter. Kami doit encore observer chacun de ses gestes."
    think "J'espère que son histoire sur Léa suffira à masquer ce qu'il a réellement fait dans le sas."

    pause 0.5

    play sound sfx_announce

    think "Tous les écrans du couloir s'allument en même temps."

    stop music fadeout 0.8
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonsoir, mes chers représentants !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Entre la livraison, cette adorable panne générale et les explorations éducatives de Kael, ma matinée a été légèrement chargée."
    kami "J'en ai presque oublié de vous annoncer le thème de votre prochain vote. Presque !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Votre prochaine décision concernera le Commandement IV relatif aux rassemblements et à l'organisation."

    pause 0.4

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "La proposition est la suivante : autoriser les regroupements de plus de vingt personnes, sous réserve d'une demande d'autorisation préalable."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Autrement dit : plus de vingt personnes pourront se réunir, à condition d'annoncer à l'avance qui, où, quand et pourquoi."
    kami "Une liberté parfaitement encadrée ! Le compromis préféré de ceux qui veulent ouvrir une porte tout en gardant la clé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu à la fin du jour 9."
    kami "Vous avez donc deux jours pour décider si les habitants peuvent se retrouver en groupe sans devenir de dangereux conspirateurs."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Et cette fois, essayez d'offrir un débat un peu plus long que le précédent. Je refuse de préparer autant de caméras pour rien !"

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Les écrans s'éteignent."
    think "Plus de vingt personnes réunies avec une autorisation. Sur le papier, la proposition paraît presque raisonnable."
    think "Mais dans la chambre d'Iris, une seule personne suffit déjà à nous faire risquer la mort."

    pause 0.5

    think "Je retourne vers ma chambre sans m'arrêter devant celle d'Iris."
    think "Demain, il faudra continuer à agir normalement. Et espérer que la jeune femme finisse par ouvrir les yeux."

    stop music fadeout 1.0
    scene black with fade

    call end_day("8") from _call_end_day_7100

    #jump patreon_ending
    jump _8_1_0_0_REVEIL

# Durée : 10m
# Total J0-J6 : 2h07
