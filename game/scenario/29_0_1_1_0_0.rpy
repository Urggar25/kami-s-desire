# =============================================================================
# JOUR 29 — Plus que deux
# Noam et Iris comprennent qu'ils sont les deux seuls représentants encore non remplacés.
# Ils se barricadent dans la chambre d'Iris.
# =============================================================================

label _29_0_1_1_0_0_REVEIL:
    $ current_day = 29
    $ day_id = 29
    $ current_period = "Matin"

    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Iris m'attend devant ma porte."

    $ showGroup([
        ("iris", "fatigue", 0.38),
        ("noam", "fatigue", 0.62),
    ])

    iris fatigue "On va manger."

    noam reflexion "À deux ?"

    iris neutre "À deux."

    noam inquiet "T'as vu quelqu'un ?"

    iris reflexion "Elen. Elle m'a demandé si j'avais bien dormi."

    noam neutre "Et ?"

    iris fatigue "Elle souriait."

    noam blase "Elen sourit souvent."

    iris neutre "Pas comme ça."

    "Je pourrais lui dire qu'on est en train de devenir complètement paranoïaques."

    "Je pourrais aussi lui dire que j'ai pensé exactement la même chose de Julian hier."

    noam determine "On reste ensemble."

    iris determine "Oui."

    $ hideGroup()

label _29_0_1_1_0_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7

    "Tout le monde est déjà là."

    $ showGroup([
        ("ryn", "neutre"),
        ("tomas", "sourire"),
        ("nyra", "neutre"),
        ("sael", "calme"),
        ("julian", "sourire"),
        ("elen", "content"),
        ("mara", "taquin"),
        ("elias", "neutre"),
        ("kael", "calme"),
        ("lysa", "blase"),
        ("iris", "inquiet"),
        ("noam", "inquiet"),
    ])

    elen content "Ah ! Vous voilà."

    iris blase "Ouais."

    tomas sourire "On vous a gardé de la place."

    "Deux sièges vides. Côte à côte."

    "Je m'arrête."

    ryn neutre "Quoi ?"

    noam reflexion "Rien."

    mara taquin "Vous faites une entrée très dramatique tous les deux. J'aime bien."

    iris colere "Mara, pas aujourd'hui."

    mara sourire "Comme tu veux."

    "Elle abandonne immédiatement."

    "Mara n'abandonne jamais immédiatement."

    noam inquiet "Tomas, tu dormais où cette nuit ?"

    tomas reflexion "Dans ma chambre."

    noam neutre "Tout le temps ?"

    tomas neutre "Oui. Pourquoi ?"

    iris reflexion "Et Julian ?"

    julian sourire "Même réponse. Ma chambre, mon lit, une nuit atroce. Rien de passionnant."

    sael calme "Vous cherchez encore qui a été remplacé."

    noam neutre "Oui."

    sael raison "Ça sert plus à grand-chose."

    pause 0.3

    iris peur "Pourquoi tu dis ça ?"

    sael calme "Parce que vous avez déjà décidé."

    "Je sens mon estomac se nouer."

    nyra raison "Asseyez-vous. On peut parler calmement."

    iris determine "Non."

    elias neutre "Iris..."

    iris colere "Non."

    kael calme "Personne va vous faire de mal."

    noam peur "C'est exactement le genre de phrase qui donne envie de partir."

    lysa blase "Noam, franchement..."

    "Lysa secoue la tête."

    lysa fatigue "Vous êtes épuisés. Vous voyez des trucs partout."

    noam colere "J'ai vu le corps de Mara."

    "Personne ne réagit."

    "Pas vraiment."

    "Elen baisse les yeux. Ryn soupire. Julian garde ce petit sourire calme."

    iris peur "Tu vois ?"

    noam neutre "Ouais."

    ryn neutre "On voit quoi ?"

    iris colere "Que vous vous en foutez."

    mara triste "On s'en fout pas."

    iris neutre "Alors arrête de parler comme si c'était normal !"

    mara fatigue "Qu'est-ce que tu veux que je fasse, Iris ? Que je hurle chaque fois que tu me rappelles que t'as vu un corps avec ma tête ?"

    "La réponse est trop propre."

    "Trop calme."

    "Iris recule d'un pas."

    noam determine "On y va."

    nyra reflexion "Noam, attends."

    noam neutre "Non."

    elias colere "Vous allez où ?"

    iris determine "Ça te regarde pas."

    "Personne ne nous bloque."

    "C'est presque pire."

    $ hideGroup()

label _29_0_1_1_0_0_CHAMBRE_IRIS:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "On entre dans la chambre d'Iris et on verrouille."

    "Sa grille est toujours condamnée par la plaque métallique posée plusieurs jours plus tôt. Elias n'avait jamais retiré celle-ci : elle faisait partie des premières, des vraies."

    $ showGroup([
        ("iris", "peur", 0.38),
        ("noam", "inquiet", 0.62),
    ])

    iris peur "C'est eux."

    noam neutre "Je sais pas."

    iris colere "Arrête."

    noam inquiet "Je sais pas combien. Je sais pas depuis quand."

    iris neutre "Mais ?"

    noam peur "Mais je crois qu'il reste que nous."

    "Elle s'assoit sur le bord du lit."

    "Cette fois elle ne râle pas."

    iris peur "Tous ?"

    noam faible "Je crois."

    iris triste "Même Elen ?"

    noam neutre "Je sais pas."

    iris colere "Tu viens de dire tous."

    noam peur "Parce que j'en sais rien !"

    "Ma voix monte trop fort."

    "Je me tais immédiatement."

    noam fatigue "Pardon."

    iris triste "Non. C'est moi."

    "Elle se frotte le visage."

    iris fatigue "J'arrive plus à réfléchir. À chaque fois que quelqu'un parle, je cherche ce qui cloche. Même quand y'a rien."

    noam reflexion "C'est peut-être ce qu'ils veulent."

    iris neutre "Ou peut-être qu'on est juste en train de devenir cons."

    noam taquin "Ça, c'était déjà commencé."

    "Elle souffle du nez."

    iris blase "Abruti."

    "Ça me rassure plus que ça devrait."

    $ hideGroup()

label _29_0_1_1_0_0_BARRICADE:
    $ current_period = "Après-midi"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7

    "On pousse le bureau contre la porte, puis la chaise, puis une petite commode."

    "C'est ridicule. Ça ressemble à une cabane d'enfants."

    "Mais la porte ne s'ouvre plus."

    $ showGroup([
        ("iris", "determine", 0.38),
        ("noam", "determine", 0.62),
    ])

    iris determine "La ventilation est bloquée. La porte est bloquée. On tient jusqu'à demain."

    noam reflexion "Le vote à huit heures."

    iris fatigue "On vote d'ici."

    noam neutre "Et après ?"

    iris neutre "Après la navette arrive."

    noam inquiet "Et il faut sortir."

    iris blase "Merci, j'avais oublié cette partie."

    "Quelqu'un frappe."

    pause 0.4

    elen content "Iris ? Noam ?"

    "La voix est douce. Presque normale."

    iris peur "..."

    elen inquiet "On veut juste parler."

    noam inquiet "Qui ça, on ?"

    pause 0.3

    elen neutre "Moi. Julian. Tomas."

    iris colere "Allez-vous-en."

    julian sourire "Iris, sérieusement. Vous pouvez pas rester enfermés jusqu'au départ."

    iris neutre "Regarde-moi."

    noam reflexion "Quoi ?"

    iris determine "Regarde-moi et réponds pas."

    "Je hoche la tête."

    tomas reflexion "Noam, je sais que tu m'entends. Je suis désolé pour hier. Enfin... pas hier, avant-hier. Putain, je sais même plus."

    "Ça ressemble tellement à Tomas que j'ai envie d'ouvrir."

    "C'est précisément pour ça que je n'ouvre pas."

    elias fatigue "On va pas forcer."

    mara taquin "Enfin, pas tout de suite."

    iris colere "MARA !"

    mara rire "Désolée. Celle-là était facile."

    "Je sens Iris trembler à côté de moi."

    noam inquiet "Partez."

    kael calme "On part."

    pause 0.5

    kael calme "Mais demain, vous aurez trente minutes."

    "Des pas s'éloignent."

    "Pas tous."

    "Quelqu'un reste encore un moment derrière la porte."

    "Puis plus rien."

    $ hideGroup()

label _29_0_1_1_0_0_NUIT:
    $ current_period = "Soir"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7

    "On mange ce qu'Iris avait gardé dans un tiroir. Deux biscuits écrasés, une barre, de l'eau tiède."

    $ showGroup([
        ("iris", "fatigue", 0.40),
        ("noam", "fatigue", 0.62),
    ])

    iris fatigue "Le nouveau Commandement sur la nourriture va être ravi."

    noam taquin "On a un toit et de l'eau."

    iris blase "Quelle réussite."

    "Un bruit vient de la porte."

    "Pas un coup."

    "Quelqu'un s'assoit contre de l'autre côté."

    ryn fatigue "Vous dormez ?"

    "Iris serre ma main sans même s'en rendre compte."

    ryn neutre "Je vais pas entrer."

    noam peur "Alors qu'est-ce que tu veux ?"

    ryn fatigue "Que vous arrêtiez de vous battre."

    iris colere "Va te faire foutre."

    ryn neutre "Ouais."

    pause 0.5

    ryn triste "Bonne nuit."

    "Il reste là encore quelques minutes."

    "Puis il part."

    iris peur "C'était pas lui."

    noam neutre "Je sais pas."

    iris colere "C'était pas lui."

    noam fatigue "D'accord."

    "Cette nuit-là, on dort par morceaux, l'un après l'autre."

    "Jamais en même temps."

    call end_day("30", sleeping=True) from _call_j29_stay_end_day_30
    jump _30_0_1_1_0_0_REVEIL
