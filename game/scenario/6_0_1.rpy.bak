# 6_0_1.rpy
# Jour 6 - Branche statu quo post-accident café
# Style THL - version dialoguée, rythmée

label _6_0_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 6

    pause 1.0

    $ blink()

    think "J'ouvre les yeux."

    pause 0.4

    think "Pas vraiment réveillé. Juste assez pour savoir que j'allais déjà mal avant d'ouvrir les yeux."

    pause 0.5

    think "Jour six."

    pause 0.3

    think "Le vote."

    think "Je reste accroché au plafond comme s'il pouvait retarder la journée."

    pause 0.5

    think "Hier, Elias a renversé son café et la salle d'observation nous a enfermés."
    think "Pendant quelques minutes, nous avons attendu qu'un système décide à notre place. Une répétition générale."

    pause 0.6

    think "C'était ridicule."
    think "Et ça m'a fait peur."

    pause 0.5

    think "Yeux qui piquent. Gorge sèche. Le corps dépose son rapport."

    pause 0.4

    think "Un poids dans la poitrine. Pas assez douloureux pour m'arrêter, juste assez pour ralentir chaque geste."

    pause 0.5

    think "Aujourd'hui, ça échoue."

    pause 0.4

    think "Je le pense sans colère, comme on lit l'heure."

    pause 0.5

    think "Sael votera contre."
    think "Iris aussi."
    think "Et peut-être d'autres."

    pause 0.4

    think "Donc voilà."

    think "Je me redresse. L'air paraît plus froid aujourd'hui."

    pause 0.6

    think "Se lever. Manger. Parler. Faire semblant qu'un débat peut encore changer quelque chose."

    pause 0.5

    think "Je reste assis. Première étape déjà compromise."

    pause 0.6

    think "Le silence de la chambre n'a pas la même texture."

    pause 0.4

    think "C'est idiot. Un silence n'a pas de texture."

    pause 0.3

    think "Et pourtant."

    pause 0.6

    play sound sfx_announce

    pause 0.8

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.4

    kami "Représentants."

    pause 0.3

    scene bg_diffusion_einstein at adaptive_fullscreen
    with hpunch

    pause 0.1

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Le vote sur la libre circulation entre districts aura lieu aujourd'hui."

    pause 0.3

    kami "Quatorze heures."

    pause 0.4

    "La voix grésille."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen
    with vpunch

    pause 0.1

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Présence recommandée."

    pause 0.3

    kami "Participation recommandée."

    pause 0.3

    kami "Illusion de responsabilité recommandée."

    pause 0.5

    "Un blanc."

    pause 0.6

    scene bg_diffusion_triste at adaptive_fullscreen
    with dissolve

    kami "Vous avez l'air fatigués."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen
    with dissolve

    kami "Enfin."

    pause 0.3

    kami "J'imagine."

    pause 0.4

    scene bg_diffusion_colere at adaptive_fullscreen
    with dissolve

    kami "Mes relevés comportementaux indiquent une baisse notable de votre capacité à produire quelque chose d'intéressant."

    pause 0.5

    kami "C'est contrariant."

    pause 0.4

    scene bg_diffusion_einstein at adaptive_fullscreen
    with hpunch

    pause 0.1

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Les jouets se cassent toujours plus vite lorsqu'on commence à les utiliser correctement."

    pause 0.5

    kami "Cafétéria à huit heures trente."

    pause 0.3

    kami "Ne soyez pas en retard."

    pause 0.4

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    think "L'écran s'éteint. Pas de rire. C'est presque plus inquiétant."

    pause 0.5

    think "Je fixe l'endroit où son visage était apparu."

    pause 0.5

    think "Elle était énervée."

    pause 0.3

    think "Pas comme d'habitude."

    pause 0.4

    think "Kami simule tout : joie, tendresse, colère, même ses silences."

    pause 0.5

    think "Mais là…"

    pause 0.6

    think "Non."
    think "Pas maintenant."

    $ _j601_reveil_trace_score = 0

    think "Je pousse sur le matelas pendant que mon corps cherche encore un amendement."

    call screen trace_qte(path_type="s_curve", time_limit=4.2, wait_time=0.25, tolerance=78, max_errors=4, anchor_x=960, anchor_y=650, start_radius=120)
    if _return["success"]:
        $ _j601_reveil_trace_score = 1

    think "Je me lève. Mes jambes répondent avec un léger retard."

    pause 0.4

    think "Ma veste est par terre, beaucoup trop loin. Je la ramasse, l'enfile et gagne la porte."

    if _j601_reveil_trace_score >= 1:
        think "Ça passe."
        think "Pas bien."
        think "Mais ça passe."
    else:
        think "Je n'y arrive presque pas."
        think "Je bouge quand même."
        think "C'est tout."

    pause 0.5

    think "Cafétéria."
    think "Puis vote."
    think "Puis échec."

    pause 0.4

    think "Une journée simple."

    pause 0.5

    think "Super."

    pause 0.6

    jump _6_0_1_CAFETERIA

# Durée : 2m20


label _6_0_1_CAFETERIA:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    pause 0.8

    think "Ils sont presque tous là."
    think "Ils parlent, mais jamais ensemble."

    $ showP("elias", "fatigue", 0.25)
    $ showP("mara", "neutre", 0.55)
    $ showP("elen", "neutre", 0.85)

    play sound "sfx/glass_spill.mp3"

    "CLAC."
    "Encore."

    elias "Putain—"

    call screen trace_qte(path_type="arc", time_limit=1.8, wait_time=0.1, tolerance=86, max_errors=3, anchor_x=960, anchor_y=650, start_radius=125)
    $ _j601_verre_score = tq_progress

    if _j601_verre_score >= 0.82:
        think "Ma main part avant ma tête. Je redresse le verre ; quelques gouttes seulement."
        $ showP("elias", "inquiet", 0.25)
        elias "Oh putain. Merci. C'était chaud, là."
        $ showP("mara", "agace", 0.55)
        mara "Miracle matinal. On applaudit ou Elias présente enfin ses mains au reste de son corps ?"
    elif _j601_verre_score >= 0.35:
        think "Trop tard. Le verre frappe la table ; ma manche arrête l'eau avant Mara."
        $ showP("elias", "inquiet", 0.25)
        elias "Merde, merde. J'ai fait quoi, là ? C'est chaud."
        $ showP("mara", "agace", 0.55)
        mara "Rien de grave. Juste assez pour me tremper et achever le peu de patience que je gardais pour les grandes occasions."
    else:
        think "Je tends le bras trop lentement. Le verre bascule entièrement."
        $ showP("elias", "inquiet", 0.25)
        elias "Et merde. Fait chier, c'est chaud."
        $ showP("mara", "agace", 0.55)
        mara "Tout le verre. Performance complète. Le jury est traumatisé."

    elias "J’ai pas—"

    mara "Hier, ta maladresse t'a enfermé dans une salle. Aujourd'hui, elle attaque le petit-déjeuner."
    mara "Demain tu fais quoi, tu déclares la guerre à une poignée de porte ?"

    elen "..."

    $ showP("elen", "inquiet", 0.85)
    elen "C'est pas drôle. Il a pas fait exprès, enfin je crois pas qu'on puisse faire exprès de rater une table entière..."

    mara "Je confirme. Heureusement que l'humiliation ne tache pas."

    $ showP("elias", "inquiet", 0.25)
    elias "J'ai glissé. Enfin, ma main. Pas moi. C'est chaud à expliquer."

    $ showP("mara", "neutre", 0.55)
    mara "Comme d'habitude : au mauvais endroit, au pire moment."

    think "Elias regarde le sol comme si le problème, c'était lui tout entier."

    $ showP("elen", "neutre", 0.85)
    elen "Vous avez entendu Kami ? Enfin oui, évidemment, mais vous avez entendu comment elle parlait ?"

    mara "Ouais."
    $ showP("mara", "mefiant", 0.55)
    mara "Et elle avait un problème. Pas son petit théâtre habituel. Un vrai."

    elias "Les problèmes, c'est pas ce qui manque ici."

    mara "Non."
    mara "Là c’était autre chose."

    hide elen
    $ showP("lysa", "blase", 0.85)

    lysa "Elle ne jouait pas."
    $ showP("lysa", "reflexion", 0.85)
    lysa "Ou pas comme d'habitude. Même Dionysos tenait mieux son masque."

    elias "Kami joue toujours son rôle. C'est son truc."

    lysa "Ouais."
    $ showP("lysa", "blase", 0.85)
    lysa "Pas là. C'est précisément ce qui est étrange."

    think "Un blanc. Personne ne veut nommer ce qu'il a entendu."

    hide elias
    $ showP("elen", "inquiet", 0.25)

    elen "Elle avait l'air... agacée. Mais pas agacée-drôle. Agacée qui donne envie de poser son plateau et de partir très loin."

    mara "« Agacée », c'est adorablement léger."
    $ showP("mara", "doute", 0.55)
    mara "Elle avait l'air buggée. Genre bug qui mord."

    lysa "Tu crois qu'il lui est arrivé quelque chose ?"

    mara "Non. Enfin… j'en sais rien."
    $ showP("mara", "mefiant", 0.55)
    mara "C'était bizarre. Même pour elle."

    think "Je m'assois. Personne ne me regarde vraiment."

    think "C’est mort."
    think "On le sait tous."

    think "Pas besoin de débat."
    think "Seulement attendre l'heure officielle de l'échec."

    hide mara
    $ showP("iris", "fatigue", 0.55)

    think "Iris s'assoit à côté de moi."
    iris "Je voterai contre. Décision prise."
    iris "Je préfère une mauvaise frontière à une catastrophe bien intentionnée."

    think "Direct. Pas agressif. Elle est trop fatiguée pour le sarcasme."

    hide elen
    $ showP("sael", "neutre", 0.25)

    sael "Moi aussi."
    sael "On ne force pas une porte parce que la pièce brûle moins vite que prévu."

    think "Sael pose son non comme une pierre. C'est terminé."

    hide lysa
    $ showP("elen", "inquiet", 0.85)

    elen "..."
    $ showP("elen", "inquiet", 0.85)
    elen "On pourrait quand même parler, juste un peu— pas pour changer tout le monde, juste pour... je sais pas, vérifier qu'on est encore ensemble ?"

    iris "Non."
    $ showP("iris", "neutre", 0.55)
    iris "Non. On vit dans des mondes incompatibles et on nous propose de supprimer les frontières sans transition."
    iris intervention "Ce n'est pas du courage. C'est une expérience sociale avec les districts pauvres comme matériau."

    elen "..."

    hide iris
    $ showP("mara", "neutre", 0.55)

    mara "Au moins c'est réglé."
    $ showP("mara", "agace", 0.55)
    mara "On ne perdra pas deux heures à tourner en rond pour le plaisir des caméras."

    hide sael
    $ showP("lysa", "blase", 0.25)

    lysa "On les aurait perdues quand même. Sisyphe, mais avec un planning."

    mara "Ouais."
    $ showP("mara", "neutre", 0.55)
    mara "Mais avec plus de bruit."

    think "Personne ne relève."

    hide lysa
    $ showP("elias", "fatigue", 0.25)

    elias "..."
    $ showP("elias", "neutre", 0.25)
    elias "On y va quand ? Autant arrêter d'attendre."

    hide elen
    $ showP("lysa", "blase", 0.85)

    lysa "L'heure avance, autant y aller maintenant."

    mara "Autant finir vite."

    think "Personne ne proteste."

    think "Ça y est."
    think "On n’essaie même plus."

    think "Je me lève. Les autres suivent au même rythme, avec la même résignation."

    hide elias
    hide mara
    hide lysa

    jump _6_0_1_TRANSITION_CONCLAVE

# Durée : 2m30


label _6_0_1_TRANSITION_CONCLAVE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.6

    think "Nous sortons sans parler. Les pas s'alignent sans les regards."

    think "Une file, pas un groupe."

    think "Le couloir est trop long. Ou trop vide."

    play sound "sfx/glitch_light.mp3"

    think "Les lumières vibrent une seconde, puis reviennent."

    think "Personne ne réagit. Mauvais signe."

    think "Le Conclave est étrange depuis ce matin. Plus étrange."

    show screen kami_broadcast_ui

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Oh."
    scene bg_diffusion_taquin at adaptive_fullscreen with hpunch
    kami "Déjà en mouvement ?"
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "C’est bien."
    kami "C’est très bien."
    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "Nous pouvons… anticiper."
    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch
    kami "Le vote peut commencer plus tôt."
    kami "Immédiatement, même."
    scene bg_diffusion_taquin at adaptive_fullscreen
    kami "Ça m'arrange."
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Beaucoup."
    think "Sa voix saute. Son image aussi."

    scene bg_couloir at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.5

    think "Le couloir reprend comme si rien ne s'était passé. Puis je remarque une absence."

    menu:
        "Sael":
            $ _j601_absent_pick = "sael"
        "Iris":
            $ _j601_absent_pick = "iris"
        "Elias":
            $ _j601_absent_pick = "elias"
        "Kael":
            $ _j601_absent_pick = "kael"

    if _j601_absent_pick == "sael":
        think "Sael."
        think "Tout de suite."
    else:
        think "Non."
        think "Pas elle."
        think "Quelques secondes de trop."
        think "Sael."

    hide all
    $ showP("sael", "neutre", 0.5)

    think "Sael ne bouge plus. Elle fixe un angle vide du couloir."

    noam "Sael ?"
    think "Elle ne répond pas tout de suite."

    sael "..."
    sael "J'ai vu quelqu'un. Là-bas."

    think "Je regarde. Seulement le couloir vide."

    noam "Il n'y a personne. Enfin… je ne vois personne."

    think "Elle plisse les yeux."
    sael "..."
    sael "Oui. Sans doute…"

    think "Elle ne bouge pas. Elle y croyait, sans le moindre doute."

    noam "On y va."

    sael "..."
    sael "Oui."

    think "Elle me dépasse sans me regarder."

    think "Je vérifie encore. Rien."

    think "Je reprends ma place. La file se referme."

    jump _6_0_1_CONCLAVE_START

# Durée : ~1m40


label _6_0_1_CONCLAVE_START:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.5

    pause 0.8

    think "Nous entrons et prenons nos places sans ralentir."
    think "Nos corps connaissent déjà la défaite."

    hide all
    $ showP("ryn", "neutre", 0.2)
    $ showP("iris", "fatigue", 0.5)
    $ showP("sael", "neutre", 0.8)

    think "Ryn s'assoit. Iris croise les bras. Sael regarde droit devant."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "..."

    think "Le silence dure trop longtemps, même pour elle."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Début du débat."

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Proposition : autoriser la libre circulation entre districts."

    scene bg_diffusion_taquin at adaptive_fullscreen

    kami "Vous connaissez déjà."

    kami "Je ne vais pas répéter."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Alors."

    kami "Parlez."

    think "Personne ne parle. Pas une hésitation, pas une tentative."

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "..."

    kami "Intéressant."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Vous êtes déjà au résultat."
    kami "Sans passer par le processus."
    kami "C'est inefficace."

    think "Sa voix accroche sur le mot."

    play sound "sfx/glitch_medium.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Corrigez."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Corrigez."

    kami "Corrigez."

    think "Le mot reste trop longtemps, comme si elle cherchait la suite."

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Engagez-vous."

    kami "Débattez."

    kami "Simulez au moins."

    think "Toujours rien."

    hide all
    $ showP("ryn", "colere", 0.2)
    $ showP("iris", "fatigue", 0.5)
    $ showP("sael", "neutre", 0.8)

    ryn "Ça sert à rien."
    ryn "On sait déjà."

    iris "Non."
    iris "Et je refuse de jouer l'étonnement."

    sael "Non."
    sael "La réponse ne change pas parce qu'on la récite devant toi."

    think "Trois voix. Même réponse. Aucune variation."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen

    kami "..."

    pause 0.2

    play sound "sfx/glitch_heavy.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "Interaction insuffisante."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Ajustement."

    kami "En cours."

    think "Son image tremble plus fort, plus longtemps. Elle ne revient pas tout de suite."

    think "..."

    think "Là."

    think "Ce n'est pas normal."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Maintenez le signal."

    pause 0.3

    jump _6_0_1_SIGNAL_INSTABLE

# Durée : ~1m30


label _6_0_1_SIGNAL_INSTABLE:

    think "L'air ne change pas. La pièce non plus. Quelque chose derrière, si."

    play sound "sfx/glitch_heavy.mp3"

    show screen kami_broadcast_ui
    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "Maintenez."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Le."

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "Signal."

    think "Son image saute en boucle."

    hide all

    scene bg_conclave at adaptive_fullscreen with vpunch

    $ showP("iris", "inquiet", 0.3)
    $ showP("ryn", "colere", 0.6)
    $ showP("lysa", "blase", 0.85)

    iris "C'est quoi, ce cirque—"

    ryn "Elle bugue ?"

    lysa "Non. Elle force quelque chose à tenir."
    lysa "Atlas, mais avec des câbles."

    think "Un parasite traverse la pièce."

    play sound "sfx/glitch_loop.mp3"

    think "Constant. Sale."

    think "Ça ne tient pas. Ou ça tient trop fort."

    think "L'interface s'impose avant que nous comprenions."

    # --- LANCEMENT MINI-JEU ---
    call j601_play_signal_instable from _call_j601_play_signal_instable
    # --------------------------

    stop sound fadeout 0.5

    think "Le bruit coupe net."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "..."

    think "Pas un silence : un trou."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Stabilisation."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Incomplète."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Insuffisante."

    kami "Imprécise."

    think "Sa voix accroche encore."

    play sound "sfx/glitch_light.mp3"

    kami "Corrigez."

    kami "Encore."

    think "Son image reste figée une fraction de trop."

    think "..."

    think "Elle dérape."

    think "Ou elle fait semblant."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    think "Personne ne commente. Nous attendons seulement la suite."

    jump _6_0_1_FRACTURE_QTE

# Durée : ~1m30 (hors mini-jeu)


label _6_0_1_FRACTURE_QTE:

    call j601_play_fracture from _call_j601_play_fracture
    $ j601_fracture_result = _return

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Puisque vous refusez de débattre…"
    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch
    kami "Il est temps maintenant de mour—"
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Voter."
    kami "Voter."
    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "Pardon."
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Correction effectuée."

    play sound "sfx/glitch_heavy.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    kami "Le débat est clos."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    think "Personne ne bouge."

    $ showP("mara", "doute", 0.20)
    $ showP("iris", "peur", 0.50)
    $ showP("ryn", "neutre", 0.80)

    iris "..."
    iris "Elle vient de dire quoi ?"

    ryn "J'en sais rien. J'ai entendu du bruit."

    mara "Si."
    $ showP("mara", "mefiant", 0.20)
    mara "Elle a dit un mot. Et elle l'a corrigé beaucoup trop vite."

    $ showP("iris", "inquiet", 0.50)
    iris "Vous avez entendu la même chose que moi ?"

    ryn "J’ai entendu du bruit."

    mara "Moi, j'ai entendu « mourir »."

    think "Le mot tombe entre nous. Personne ne le ramasse."

    hide ryn
    $ showP("lysa", "blase", 0.80)

    lysa "Elle a aussi dit voter."

    mara "Ouais."
    mara "Après."

    iris "C’est censé nous rassurer ?"

    lysa "Non."
    $ showP("lysa", "fatigue", 0.80)
    lysa "Je constate seulement que l'alternative n'a rien de rassurant."

    think "Personne ne rit. Pas même Mara."

    hide iris
    $ showP("tomas", "inquiet", 0.50)

    tomas "Euh… je n'ai pas compris la totalité du texte."

    mara "Personne n’a compris."

    tomas "Non, je veux dire…"
    $ showP("tomas", "reflechit", 0.50)
    tomas "La proposition, telle qu’elle a été formulée, est peut-être incomplète."
    tomas "Comme la dernière fois…"

    lysa "Peut-être ?"

    tomas "J’ai entendu libre circulation."
    tomas "Visa."
    tomas "Responsables de District."
    tomas "Et ensuite..."
    $ showP("tomas", "panne", 0.50)
    tomas "Ensuite c’était du verre pilé."

    mara "Très juridique, le verre pilé. Même un avocat ivre aurait du mal à travailler avec ça."

    hide mara
    $ showP("elen", "inquiet", 0.20)

    elen "On peut pas voter là-dessus ! On sait même pas ce qu'elle a dit !"

    lysa "Et pourtant, l'oracle exige sa réponse."

    elen "Non, mais vraiment—"
    $ showP("elen", "peur", 0.20)
    elen "Si Kami bugge pendant qu’elle annonce le texte, qu’est-ce qui se passe si on vote pour ?"

    think "Une question simple. Beaucoup trop simple pour le système."

    hide tomas
    $ showP("sael", "neutre", 0.50)

    sael "On ne sait pas."

    elen "Voilà."
    elen "C’est ça le problème."

    lysa "Un des problèmes."

    sael "Non."
    $ showP("sael", "mefiant", 0.50)
    sael "Le seul qui compte. On ne consent pas à ce qu'on ne comprend pas."

    think "Sael regarde l'écran vide, pas nous."

    sael "Si nous votons pour, la modification est appliquée immédiatement."

    elen "Même si le texte était..."
    $ showP("elen", "hesitation", 0.20)
    elen "cassé ?"

    sael "Oui."

    lysa "On ne sait pas."

    sael "Justement."
    sael "Il fallait déjà voter contre. Maintenant, c'est une nécessité. Même les signes refusent ce texte."

    hide elen
    $ showP("kael", "inquiet", 0.20)

    kael "Elle pourrait appliquer autre chose."

    lysa "Ou tout appliquer de travers."

    kael "Ou considérer que nous avons validé une version que nous n’avons pas entendue."

    think "Tomas relève la tête."

    hide lysa
    $ showP("tomas", "raison", 0.80)

    tomas "Ça, c’est possible."

    sael "Donc non."

    kael "Attends."

    sael "Non."

    kael "Je ne dis pas que je suis pour."

    sael "Alors ne parle pas comme s'il restait une marge de manœuvre."

    $ showP("kael", "fatigue", 0.20)
    kael "Je parle parce que j’essaie de comprendre."

    sael "Moi aussi."
    sael "Mais il n'y a plus rien à comprendre."

    think "Silence."

    hide kael
    $ showP("iris", "fatigue", 0.20)

    iris "Super."
    iris "Donc : une IA instable, un texte incompréhensible et un vote traité comme une formalité. Organisation impeccable."

    tomas "Techniquement, ce n’est pas une réunion normale."

    iris "Merci, Tomas. Heureusement que tu es là."
    $ showP("iris", "colere", 0.20)
    iris "Je me sens beaucoup mieux."

    think "Tomas baisse les yeux. Le sarcasme d'Iris vient de choisir une victime trop facile."

    hide sael
    $ showP("mara", "mefiant", 0.50)

    mara "Question bête…"

    iris "J'adore quand tu annonces le programme. Cela dit, ça ne change pas beaucoup de d'habitude."

    mara "Si elle est vraiment instable…"
    $ showP("mara", "doute", 0.50)
    mara "Pourquoi elle insiste pour voter maintenant ?"

    tomas "Parce que c'est dans les règles, on doit voter aujourd'hui."

    mara "Oui, mais pas forcément maintenant."
    mara "Ou parce que ça l’arrange ?"

    think "Je repense au couloir, à sa voix : « Ça m'arrange. Beaucoup. »"

    think "Elle l'a dit. Très clairement."

    hide tomas
    $ showP("ryn", "colere", 0.80)

    ryn "Alors on vote contre."

    iris "C’était déjà prévu."

    ryn "Je veux dire tout le monde."

    mara "Bonne chance pour obtenir l'unanimité maintenant."

    ryn "Putain, Mara."

    mara "Quoi ?"
    $ showP("mara", "agace", 0.50)
    mara "Tu crois que j'aime ça ?"
    mara "Je dis juste que cinq minutes plus tôt, on n’était déjà pas d’accord sur le principe."

    ryn "Le principe vient de disparaître sous une tonne de bugs !"

    iris "Il a pas tort."

    mara "J’ai pas dit qu’il avait tort."

    think "Ryn serre les dents. Sa colère cherche une porte et n'en trouve pas."

    hide iris
    $ showP("lysa", "fatigue", 0.20)

    lysa "On ne sait pas ce qu’on vote."
    lysa "On ne sait pas si Kami contrôle encore ce qui se passe."
    lysa "On ne sait pas ce qui sera appliqué."
    lysa "C'est le chaos absolu. Même Cassandre manquerait de vocabulaire."

    mara "Ça fait beaucoup de choses qu’on ne sait pas."

    lysa "Ouais."

    ryn "Et pendant ce temps, les frontières restent fermées."

    think "Cette fois, personne ne répond vite."

    hide mara
    $ showP("sael", "neutre", 0.50)

    sael "Oui."

    ryn "..."

    sael "Elles resteront fermées."

    ryn "Tu dis ça comme si c’était le mieux à faire."

    sael "Oui. C'est encore le moindre mal."
    $ showP("sael", "fatigue", 0.50)

    think "Ryn ouvre la bouche, puis la referme."

    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "Vous avez terminé ?"

    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Non."
    kami "Question rhétorique."

    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "Le débat était déjà clos."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    kami "Procédure de vote."

    play sound "sfx/glitch_light.mp3"

    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Maintenant."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    "Les écrans latéraux s’allument."
    "Les pupitres aussi."
    "Un par un."
    "Kami semble particulièrement pressée d'en finir."

    $ showP("lysa", "blase", 0.20)
    $ showP("sael", "neutre", 0.50)
    $ showP("ryn", "neutre", 0.80)

    lysa "Elle ne nous laisse même pas finir de parler."

    ryn "Parce qu’on panique maintenant ?"

    lysa "Je ne sais pas."
    $ showP("lysa", "fatigue", 0.20)
    lysa "Moi j’ai coché ça mentalement il y a trois jours."

    hide all

    jump _6_0_1_VOTE

# Durée : ~3m10 hors mini-jeu

label _6_0_1_VOTE:

    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    scene black with dissolve

    $ _vote_result = renpy.call_screen("vote_screen")

    if _vote_result == "pour":
        scene Solid("#0AFF8844")
        with Dissolve(0.12)
    elif _vote_result == "contre":
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene Solid("#AAB0BF44")
        with Dissolve(0.12)

    # Résultats imposés pour le vote J6_0_1
    # Pour : Julian, Tomas + éventuellement Noam
    # Abstention : Elias + éventuellement Noam
    # Contre : tous les autres + éventuellement Noam

    $ player_vote = vote_phase3_player_choice if vote_phase3_player_choice in ("pour", "contre", "abstention") else "abstention"

    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    $ vote_phase3_results = [
        ("Julian", "pour"),
        ("Tomas", "pour"),
        ("Elias", "abstention"),
        ("Ryn", "contre"),
        ("Nyra", "contre"),
        ("Kael", "contre"),
        ("Mara", "contre"),
        ("Lysa", "contre"),
        ("Iris", "contre"),
        ("Elen", "contre"),
        ("Sael", "contre"),
        ("Noam", player_vote),
    ]

    $ renpy.random.shuffle(vote_phase3_results)

    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    pause 0.8

    $ amendement_passe = False

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    think "Le résultat reste affiché quelques secondes de trop."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Résultat du vote."
    $ interject("REJETÉ", color="#FF4D6D")
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Ab— Absence d'unanimité."
    kami "Amendement rejeté."

    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "La libre circulation entre… demeure interdite."

    scene bg_diffusion_taquin at adaptive_fullscreen
    kami "Statu quo maintenu."

    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Prévis—ble."
    kami "Décevant."
    kami "Mais prévisible."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showP("ryn", "colere", 0.20)
    $ showP("sael", "neutre", 0.50)
    $ showP("iris", "fatigue", 0.80)

    ryn "..."

    iris "Bon."
    iris "Voilà. Le monde reste absurde, mais au moins il reste cohérent."

    sael "C'était nécessaire."
    sael "Les morts de Limen auraient compris."

    ryn "Ne dis pas ça."

    sael "Je le pense."

    ryn "C'est bien ça le problème."

    hide iris
    $ showP("mara", "doute", 0.80)

    mara "On a voté contre un texte qu'on n'a même pas eu le luxe de comprendre."

    ryn "On a voté contre parce que Kami était en train de péter les plombs en direct."
    ryn "Pas parce que la proposition était mauvaise."

    mara "Je sais."
    mara "Ce n'est pas censé me rassurer."

    hide sael
    $ showP("tomas", "inquiet", 0.50)

    tomas "Je… je maintiens mon vote."

    mara "Évidemment."

    tomas "Je ne dis pas que c'était prudent."
    $ showP("tomas", "raison", 0.50)
    tomas "Je dis que le principe restait correct."
    tomas "Même si le contexte était... catastrophique."

    ryn "Ouais, mais trop risqué avec tout ça."

    think "Personne ne répond. Il a raison et cela ne change rien."

    hide ryn
    $ showP("julian", "sourire", 0.20)

    julian "Nous aurions pu défendre le principe malgré la panne. Nous avons choisi le retrait."

    mara "Julian."

    julian "Quoi ?"

    mara "Pas maintenant. Garde le discours pour quand personne n'a envie de te frapper."

    $ showP("julian", "decu", 0.20)

    julian "..."
    julian "D'accord. Julian saura se taire. Pour l'instant."

    hide mara
    $ showP("elias", "fatigue", 0.80)

    elias "De toute façon, on savait comment ça finirait."
    elias "Les bugs ont juste rendu le choix encore plus chaud."

    think "Elias ne défend même pas son choix. Il est vidé."

    hide julian
    $ showP("lysa", "fatigue", 0.20)

    lysa "On sort ?"

    elias "Oui."

    tomas "Kami n'a pas encore—"

    lysa "Elle a fini."

    tomas "Techniquement, non."

    lysa "Tomas."
    lysa "Tomas. L'écran ne se rallumera pas."

    think "L'écran reste éteint depuis la fin avortée de l'annonce."

    $ showP("tomas", "panne", 0.50)

    tomas "..."
    tomas "Oui. Peut-être…"

    think "Les pupitres s'éteignent un à un."

    hide elias
    $ showP("sael", "fatigue", 0.80)

    sael "Ryn."

    think "Ryn ne répond pas et ne la regarde pas."

    hide tomas
    $ showP("ryn", "colere", 0.50)

    ryn "Pas maintenant."

    sael "..."

    sael "D'accord."

    think "Sael détourne les yeux et s'éloigne."

    think "C'est terminé."
    think "Mais rien n'est réglé."

    hide lysa
    hide ryn
    hide sael
    with moveinright

    jump _6_0_1_FIN_JOURNEE

# Durée : ~3m00


label _6_0_1_FIN_JOURNEE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    think "Nous quittons le Conclave ni ensemble ni séparés : assez proches pour entendre les pas, assez loin pour éviter les mots."

    $ showP("lysa", "fatigue", 0.25)
    $ showP("mara", "doute", 0.55)
    $ showP("elen", "inquiet", 0.85)

    elen "On a bien fait ?"

    mara "Non."

    elen "..."

    mara "Enfin."
    $ showP("mara", "fatigue", 0.55)
    mara "Si."
    mara "Peut-être."
    mara "J'en sais trop rien."

    lysa "Ainsi décident les représentants du monde : avec la certitude d'Œdipe et deux fois moins d'informations."

    elen "C'est pas drôle."

    lysa "Je sais. Mais c'est vrai."
    lysa blase "Nous sommes pathétiques."

    hide mara
    $ showP("kael", "fatigue", 0.55)

    kael "Voter pour aurait été dangereux."

    elen "Et voter contre ?"

    kael "Au moins, aucune variable nouvelle."

    elen "Super."

    lysa "C'est déjà ça."

    hide elen
    $ showP("iris", "fatigue", 0.85)

    iris "Je veux prendre une douche."
    $ showP("iris", "colere", 0.85)
    iris "Et je veux que ce cirque s'arrête. Nous ne changerons rien tant que l'arbitre se désintègre en direct."

    kael "Le deuxième point risque d'être compliqué."

    iris "Merci, Kael."
    iris "Toujours là pour piétiner mes rêves les plus modestes."

    $ showP("kael", "inquiet", 0.55)

    kael "Désolé."

    iris "C'était une blague."

    kael "Ah."

    lysa "Elle était mauvaise. Même pour toi."

    iris "Je suis fatiguée, te moque pas de mon inspiration."

    think "Cette fois, personne n'ajoute rien."

    hide lysa
    $ showP("tomas", "inquiet", 0.25)

    tomas "Je vais vérifier les retranscriptions."

    iris "Là ?"

    tomas "Oui."

    iris "Tomas."

    tomas "Je veux être sûr que Kami n'a pas appliqué une pénalité par rapport à ce vote..."

    kael "Tu crois qu'elle le ferait ?"
    kael "Quoique tout semble possible aujourd'hui."

    $ showP("tomas", "panne", 0.25)

    tomas "..."
    tomas "J'espère que non…"

    think "Il part avant qu'on puisse l'arrêter ou l'aider. Je ne sais pas laquelle des deux options l'effraie le plus."

    hide tomas
    hide kael
    $ showP("sael", "fatigue", 0.55)

    think "Sael marche derrière nous sans regarder personne."

    noam "Sael."

    sael "Pas maintenant."

    think "La même phrase que Ryn."

    noam "D'accord."

    $ showP("sael", "neutre", 0.55)

    hide all

    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showP("julian", "decu", 0.25)
    $ showP("elias", "fatigue", 0.55)
    $ showP("ryn", "colere", 0.85)

    julian "On va vraiment faire comme si rien ne s'était passé ?"

    ryn "Non."

    julian "Alors on fait quoi ?"

    ryn "Rien."

    julian "Remarquable stratégie collective."

    ryn "Tu veux applaudir ?"

    $ showP("julian", "sourire", 0.25)

    julian "J'hésite."

    $ showP("ryn", "colere2", 0.85)

    ryn "Essaie pour voir."

    elias "Stop. Vous deux."
    elias "On n'est pas des gamins. C'est chaud, arrêtez."

    think "Un mot. Cela suffit presque."

    $ showP("elias", "neutre", 0.55)

    elias "Ne vous battez pas ici."

    julian "Où alors ?"
    $ showP("julian", "decu", 0.25)
    julian "Parce que je commence à manquer d'endroits où on peut encore parler."

    elias "Dans ta chambre, à la limite. Là au moins, vous casserez que vos trucs."

    julian "Très drôle."
    julian "À quoi bon si personne ne voit la correction historique que Julian lui inflige ?"

    ryn colere "Ah ouais ? Essaie."

    elias "Bon !"
    elias colere "J'ai dit stop !"

    think "Julian détourne les yeux. Ryn aussi. Elias reste surpris d'avoir été entendu."

    hide julian
    hide elias
    hide ryn

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    think "La porte de ma chambre se referme. Le calme revient. Il m'avait manqué."

    think "J'ai voté."
    think "Ils ont voté."
    think "Kami a déliré toute la journée…"

    think "Je laisse tomber ma veste et reste debout sans raison."

    think "Qu'est-ce qui s'est passé ?"

    think "Pourquoi la machine qui dirige le monde s'est-elle mise à dérailler ?"
    think "L'incident d'hier ? Elias aurait-il endommagé quelque chose dont Kami dépend ?"

    think "Rien n'avait de sens dans ce qu'elle disait..."
    think "Un lapsus."
    think "Une menace."
    think "Un bug."

    think "Lapsus, menace ou panne. Trois réponses, aucune utile."

    think "Je sens encore la chaleur artificielle du Conclave et ses grésillements."

    think "Quelque chose a changé."

    think "Je l'ai pensé ce matin. Maintenant, je ne peux plus appeler ça une impression."

    play sound "sfx/glitch_light.mp3"

    think "L'écran mural clignote une fois. Je me retourne."

    think "J'attends. Rien."

    think "Bien sûr."

    think "Je passe de l'eau froide sur mon visage. Pas assez froide. Le miroir me rend celui du matin, un peu plus fatigué."

    think "Voilà."
    think "C'est tout."

    think "Je retourne au lit sans me changer complètement."

    think "Le plafond est encore là. Lui au moins reste stable."

    think "Demain, ça ira mieux."

    think "Je n'y crois pas une seconde."

    think "Tant pis."

    think "Mes paupières deviennent lourdes. Derrière le silence, très loin ou très près, la voix de Kami recommence."

    think "Voter. Voter. Puis presque rien."

    think "Mourir..."

    $ blink()

    call end_day("7") from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE

# Durée : ~4m00

# NOTE:
# Ce fichier est volontairement condensé ici.
# Version complète 800+ lignes peut être étendue avec variantes dialogues, réactions variables,
# et branches supplémentaires selon variables d'affinité et de confiance.
