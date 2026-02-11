# -----------------------------------------------------------------------
# LIENS — NYRA
# -----------------------------------------------------------------------

default nyra_link = 0

label NYRA_LINK_INTERACT:

    menu:
        "Passer du temps avec Nyra ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if nyra_link == 0:
        jump nyra_link_1
    elif nyra_link == 1:
        jump nyra_link_2
    elif nyra_link == 2:
        jump nyra_link_3
    elif nyra_link == 3:
        jump nyra_link_4
    elif nyra_link == 4:
        jump nyra_link_5

    if last_room_label:
        jump expression last_room_label
    return

label nyra_link_1:

    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("nyra", "sourire", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Nyra aligne des pions de vote sur la table, comme un jeu de stratégie."
    play sound sfx_paper

    noam "Tu transformes le Conclave en échiquier ?"
    nyra "Plutôt en jeu d'équilibre. Les alliances tiennent jusqu'au prochain intérêt."
    noam "Et le timing ?"
    nyra "Tout est là. Une bonne idée lancée trop tôt, c'est un cadeau pour l'adversaire."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Une idée moyenne au moment parfait, ça gagne un vote."
    noam "Tu as l'air de t'amuser."
    nyra "Jouer sérieusement, c'est encore jouer."

    $ nyra_link = 1
    jump FREE_TIME_END

label nyra_link_2:

    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    scene bg_stockage at adaptive_fullscreen

    $ showP("nyra", "taquin", 0.70)
    $ showP("noam", "hesitation", 0.24)

    "Nyra me tend une fiche vierge comme si elle attendait une signature."
    noam "C'est quoi ?"
    nyra "Question simple : si ton allié viole une règle mineure pour sauver dix personnes, tu le couvres ?"
    noam "C'est pas une question simple, c'est un piège."
    $ showP("nyra", "rire", 0.70)
    nyra "Exact. Je regarde ta réaction, pas ta morale affichée."
    noam "Et mon score ?"
    nyra "Tu réfléchis avant de répondre. Ça vaut plus que de jolies certitudes."
    play sound sfx_beep
    noam "Je déteste parler avec toi."
    nyra "C'est bon signe."

    $ nyra_link = 2
    jump FREE_TIME_END

label nyra_link_3:

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("nyra", "raison", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Nyra écrit trois colonnes : Commandements, usages, non-dits."
    noam "Tu fais une loi secrète ?"
    nyra "Non. Je note les règles implicites."
    noam "Celles qu'on ne dit pas ?"
    nyra "Oui. Ne pas humilier un pivot en public. Ne pas forcer un vote sans sortie honorable."
    $ showP("nyra", "neutre", 0.70)
    nyra "Ceux qui ignorent ces règles pensent perdre sur le fond... alors qu'ils perdent sur la forme."
    noam "Donc on peut avoir raison et se faire éliminer."
    nyra "C'est même la manière la plus fréquente de disparaître."

    $ nyra_link = 3
    jump FREE_TIME_END

label nyra_link_4:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("nyra", "surpris", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Une secousse traverse la station. Nyra sourit au lieu de paniquer."
    play sound sfx_gresillement

    noam "Tu souris vraiment là ?"
    $ showP("nyra", "sourire", 0.70)
    nyra "Oui. La tension me garde vivante."
    noam "Sans enjeu, tu ferais quoi ?"
    nyra "Je m'ennuierais en une journée."
    noam "C'est dangereux comme carburant."
    nyra "Tous les carburants sont dangereux. Le mien au moins me pousse à avancer."
    noam "Tu ne coupes jamais ?"
    nyra "Je coupe quand c'est fini. Et ici, ce n'est jamais fini."

    $ nyra_link = 4
    jump FREE_TIME_END

label nyra_link_5:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("nyra", "triste", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Cette fois, Nyra ne joue avec rien. Ses mains restent immobiles."
    noam "Tu as l'air... ailleurs."
    nyra "Je vais être honnête : je ne supporte pas l'idée d'être éliminée."
    noam "Tu veux juste gagner ?"
    nyra "Je dois gagner. Sinon je deviens une note de bas de page."
    noam "Tu as peur d'être oubliée."
    $ showP("nyra", "vide", 0.70)
    nyra "Oui. Plus que de perdre un débat, plus que de me faire détester."
    play sound sfx_announce
    $ showP("nyra", "raison", 0.70)
    nyra "Alors non, ce n'est pas un caprice. C'est une nécessité."

    $ nyra_link = 5
    jump FREE_TIME_END
