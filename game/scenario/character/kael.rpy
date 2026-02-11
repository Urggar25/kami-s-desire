# -----------------------------------------------------------------------
# LIENS — KAEL
# -----------------------------------------------------------------------

default kael_link = 0

label KAEL_LINK_INTERACT:

    menu:
        "Passer du temps avec Kael ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if kael_link == 0:
        jump kael_link_1
    elif kael_link == 1:
        jump kael_link_2
    elif kael_link == 2:
        jump kael_link_3
    elif kael_link == 3:
        jump kael_link_4
    elif kael_link == 4:
        jump kael_link_5

    if last_room_label:
        jump expression last_room_label
    return

label kael_link_1:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("kael", "reflechit", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Kael est accoudé à la baie vitrée, les bras croisés."
    play sound sfx_beep
    "Au loin, une alarme étouffée coupe le silence, puis s'éteint."

    noam "Tu repenses à la dispute entre Mara et Sael ?"
    kael "Oui. Et au fait que personne n'a rien arrangé."
    noam "Toi non plus."
    $ showP("kael", "calme", 0.70)
    kael "Je sais. Ne pas intervenir, c'est aussi choisir une conséquence."
    noam "Ça sonne froid."
    kael "C'est surtout précis. Si j'entre trop tôt, j'ajoute juste une voix de plus au vacarme."
    noam "Donc tu attends ?"
    kael "J'observe la trajectoire. Quand deux gens veulent gagner, séparer n'aide pas toujours."

    $ kael_link = 1
    jump FREE_TIME_END

label kael_link_2:

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("kael", "neutre", 0.70)
    $ showP("noam", "hesitation", 0.24)

    "Kael fait glisser un dossier dans une fente d'archives."
    play sound sfx_paper

    noam "Tu as déjà regretté de rester à distance ?"
    $ showP("kael", "culpabilite", 0.70)
    kael "Une fois, sur un pont de service. Deux équipes se chauffaient."
    kael "Je me suis dit : ils vont se calmer."
    play sound sfx_drop
    "Le bruit sec d'un classeur qui tombe ponctue sa phrase."
    kael "Ils ne se sont pas calmés. Un gars a fini avec le bras fracassé."
    noam "Tu t'en veux encore ?"
    kael "Je ne cherche pas d'excuse. J'ai lu la scène trop tard, c'est tout."
    noam "Et depuis ?"
    kael "Depuis, je préfère la lucidité au confort d'avoir l'air neutre."

    $ kael_link = 2
    jump FREE_TIME_END

label kael_link_3:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_maintenance at adaptive_fullscreen

    $ showP("kael", "fatigue", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Le bourdonnement des machines remplit la pièce."
    play sound sfx_gresillement

    noam "Tu sais, parfois j'aimerais avoir ton calme."
    $ showP("kael", "rire", 0.70)
    kael "Et moi j'envie ceux qui frappent la table et tranchent en dix secondes."
    noam "Vraiment ?"
    $ showP("kael", "reflechit", 0.70)
    kael "Oui. Ils avancent sans se demander s'ils ont oublié une variable."
    noam "Tu crois que rester en retrait, c'est une force ?"
    kael "Parfois. Parfois c'est une fuite très élégante."
    noam "Et là, pour toi ?"
    kael "Là... j'hésite encore entre les deux."

    $ kael_link = 3
    jump FREE_TIME_END

label kael_link_4:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("kael", "calme", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Kael pose ses mains à plat sur la rambarde, immobile."
    noam "On dirait que rien ne t'atteint."
    kael "C'est l'effet recherché."
    noam "Donc ce n'est pas naturel ?"
    $ showP("kael", "fatigue", 0.70)
    kael "Pas du tout. Mon calme, c'est un entraînement."
    kael "Compter ma respiration, reformuler avant de répondre, attendre une seconde de plus."
    play sound sfx_beep
    noam "Ça doit être épuisant."
    kael "Ça l'est. Mais c'est moins cher que de laisser mes nerfs décider à ma place."
    noam "Je pensais que tu n'avais pas peur de déborder."
    kael "J'ai surtout peur de ce que je ferais si j'arrêtais de me contenir."

    $ kael_link = 4
    jump FREE_TIME_END

label kael_link_5:

    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("kael", "reflechit", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Dans le couloir du Conclave, Kael parle avant même que j'ouvre la bouche."
    kael "Cette fois je ne temporise pas : sur le prochain vote, je soutiens la protection des isolés."
    noam "Sans nuance ?"
    kael "Sans nuance."
    noam "C'est nouveau, venant de toi."
    $ showP("kael", "calme", 0.70)
    kael "J'ai assez observé. Quand la trajectoire est claire, l'inaction devient une faute."
    play sound sfx_announce
    "Une annonce de Kami résonne au-dessus de nous. Kael ne détourne pas le regard."
    kael "Si je dois agir, je le fais entièrement."
    noam "Je crois que je viens de voir ton vrai point d'équilibre."

    $ kael_link = 5
    jump FREE_TIME_END
