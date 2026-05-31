# --------------------------------------------------------------------------------------------
# JOUR 8 — Réveil chambre
# Noam se réveille seul, calme. Cherche le dessin de Juliette. Ne le trouve pas.
# Scène PnC : fouille de la chambre. Le dessin est introuvable.
# Résolution : il décide d'aller manger.
# --------------------------------------------------------------------------------------------

label _8_0_1_REVEIL_CHAMBRE:

    scene black

    $ current_day = 8

    play music "music/bgm_calm_not_peace.mp3" fadein 2.5

    $ blink()
    $ blink()

    scene bg_chambre at adaptive_fullscreen with dissolve

    "La lumière filtre sous le rideau."
    "Pas violemment."
    "Juste assez pour dessiner une ligne sur le sol."

    think "Il fait jour."
    think "Et je suis réveillé."
    think "Tout seul."

    $ blink()

    "Je regarde le plafond une seconde."
    "Pas d'annonce."
    "Pas de voix."
    "Rien."

    think "Ce silence-là, c'est le bon."

    pause 0.6

    "Je m'étire."
    "Je reste allongé encore un moment."
    "Juste parce que je peux."

    pause 0.5

    "Et puis je me souviens."

    think "Le dessin."

    "Je me redresse."

    "Je m'assois sur le bord du lit."

    think "Je l'ai posé quelque part hier soir."
    think "Forcément."
    think "Je l'ai toujours quelque part."

    pause 0.4

    think "Juliette."
    think "Elle avait mis du temps à le faire, ce dessin."
    think "Trois semaines. Elle recommençait sans arrêt."
    think "À la fin elle m'avait dit que c'était nul."
    think "Que le nez était raté."
    think "Je lui avais dit que c'était parfait."
    think "C'était vrai."

    pause 0.4

    "Je me lève."
    "Je refais le tour du lit."

    think "Il est quelque part."
    think "Forcément."

    # --- TUTORIEL PnC ---

    tuto "(Fouille la chambre. Le dessin est peut-être encore là.)"

    scene bg_chambre at adaptive_fullscreen with dissolve
    $ pnc_room = "chambre_j8"
    $ pnc_flags = {}
    call screen pnc_chambre_j8()
    return


# -------------------------------------------------------
# SCREEN PnC — Chambre jour 8
# -------------------------------------------------------

screen pnc_chambre_j8():

    modal True
    zorder 200

    add "images/background/bg_chambre.png" at cover_screen

    # Hotspot — Sac / affaires au sol
    imagebutton:
        idle  "images/background/interact/chambre/sac.png"
        hover "images/background/interact/chambre/sac_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_8_PNC_SAC")

    # Hotspot — Vêtements / chaise
    imagebutton:
        idle  "images/background/interact/chambre/chaise.png"
        hover "images/background/interact/chambre/chaise_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_8_PNC_CHAISE")

    # Hotspot — Placard
    imagebutton:
        idle  "images/background/interact/chambre/placard.png"
        hover "images/background/interact/chambre/placard_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_8_PNC_PLACARD")

    # Hotspot — Sol sous le lit
    imagebutton:
        idle  "images/background/interact/chambre/sous_lit.png"
        hover "images/background/interact/chambre/sous_lit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_8_PNC_SOUS_LIT")

    # Hotspot — Écran mural (sortie de scène)
    imagebutton:
        idle  "images/background/interact/chambre/ecran.png"
        hover "images/background/interact/chambre/ecran_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_8_PNC_ECRAN")

    # Hotspot de sortie — aller manger (halo jaune, disponible après avoir fouillé au moins 3 zones)
    if pnc_flags.get("sac") and pnc_flags.get("placard") and pnc_flags.get("sous_lit"):
        imagebutton:
            idle  "images/background/interact/chambre/sortie.png"
            hover "images/background/interact/chambre/sortie_hover.png"
            focus_mask True
            xpos 0
            ypos 0
            at cover_screen
            action Jump("_8_FIN_RECHERCHE")


# -------------------------------------------------------
# LABELS PnC
# -------------------------------------------------------

label _8_PNC_SAC:
    $ pnc_flags["sac"] = True
    "Je vide le sac sur le lit."
    "Tout sort d'un coup."
    "Des vêtements. Un bout de papier."
    "Je me jette dessus."
    pause 0.2
    think "Non."
    think "C'est juste un formulaire du Conclave."
    think "Numéro d'identification. Case à cocher."
    "Je le repose."
    think "Je l'aurais pas mis dans le sac de toute façon."
    think "Je savais que c'était précieux."
    think "Je l'aurais pas mis là."
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_CHAISE:
    $ pnc_flags["chaise"] = True
    "Je secoue la veste pendue sur la chaise."
    "Je glisse la main dans chaque poche."
    "La poche intérieure. La poche poitrine."
    think "Rien."
    "Je la retourne."
    "Je regarde sous le siège."
    think "Toujours rien."
    think "Je commence à me demander si je l'avais vraiment hier soir."
    think "Mais oui. Je l'avais. Je me souviens de l'avoir tenu."
    think "Je me souviens du papier entre mes doigts."
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_PLACARD:
    $ pnc_flags["placard"] = True
    "J'ouvre le placard."
    "Trois cintres. Un pull en boule sur l'étagère."

    menu:
        "Déplier le pull.":
            "Je le déplie."
            "Je le secoue."
            think "Il pourrait être tombé dedans, n'importe comment..."
            "Rien ne tombe."
            think "Non."
            think "Évidemment non."
            "Je le replie n'importe comment et je le remets."

        "Regarder derrière les cintres.":
            "Je pousse les cintres sur le côté."
            "Le fond du placard est vide."
            "Parfaitement vide."
            think "C'est tellement vide que ça en devient presque bizarre."

    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_SOUS_LIT:
    $ pnc_flags["sous_lit"] = True
    "Je m'agenouille."
    "Je soulève le bord de la couette pour voir dessous."
    pause 0.3
    think "..."
    think "De la poussière."
    think "Une chaussette."
    think "Pas le dessin."
    "Je reste à genoux une seconde."
    "Juste une seconde."

    menu:
        "Me relever tout de suite.":
            think "Il est ailleurs."
            think "Je continue."

        "Rester là, par terre, un moment.":
            pause 0.6
            think "Je suis en train de chercher un bout de papier sous mon lit."
            think "À genoux."
            think "Sur le sol d'une chambre qui n'est même pas la mienne."
            think "..."
            think "Ok."
            think "Relève-toi."

    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_ECRAN:
    $ pnc_flags["ecran"] = True
    "Je m'arrête devant l'écran."
    "Noir."
    "Aucun reflet. Aucune standby. Rien."
    think "Elle ne s'est pas manifestée cette nuit."
    think "Ni ce matin."
    pause 0.3
    think "Je devrais trouver ça rassurant."
    think "C'est rassurant."
    think "Mais un écran éteint dans cette chambre, ça ressemble quand même à quelque chose qui attend."
    "Je détourne les yeux."
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return


# -------------------------------------------------------
# FIN DE RECHERCHE
# -------------------------------------------------------

label _8_FIN_RECHERCHE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je m'assois sur le lit."
    "Je regarde la chambre."
    "Le sac ouvert."
    "Le tiroir pas tout à fait refermé."
    "Le pull mal replié dans le placard."

    think "Il n'est pas là."

    pause 0.5

    think "Je l'aurais pas perdu."
    think "Je perds pas ce genre de truc."
    think "Je l'aurais posé quelque part de sûr."
    think "Je l'aurais—"

    pause 0.4

    think "Je l'aurais posé quelque part."

    "Je reste là une seconde de trop."

    pause 0.6

    think "Juliette avait mis des semaines à le faire."
    think "Elle m'avait dit que c'était raté."
    think "Le nez, elle disait."
    think "J'avais répondu que c'était parfait."
    think "Elle avait levé les yeux au ciel."
    think "Comme si j'avais dit ça juste pour lui faire plaisir."
    think "Mais c'était vrai."

    pause 0.5

    "Je me lève."

    menu:
        "Refaire un tour rapide de la pièce.":
            "Je regarde encore."
            "Derrière la porte."
            "Sous le matelas cette fois."
            "Dans la doublure du sac."
            pause 0.4
            think "Non."
            think "Il n'est juste pas là."
            "Je m'arrête."
            think "D'accord."

        "Accepter que ce soit fini pour l'instant.":
            think "Je peux pas chercher indéfiniment."
            think "Il est peut-être ailleurs."
            think "Dans une autre affaire."
            think "Quelque part."

    pause 0.3

    think "J'ai faim."

    "Je réalise que ça fait longtemps que je n'ai pas mangé."
    "Mon estomac me le fait comprendre maintenant."
    "Assez clairement."

    think "D'accord."
    think "On regle ça après."
    think "Le dessin réapparaîtra."
    think "Les choses réapparaissent."

    $ journal_entries.append(("Jour 8 — matin", "Le dessin de Juliette a disparu. J'ai fouillé partout. Il n'est plus là. Je ne sais pas si je l'ai égaré ou si quelqu'un l'a pris. Je préfère penser que je l'ai égaré. C'est moins lourd à porter."))

    "Je prends ma veste."

    menu:
        "Laisser la chambre telle quelle.":
            think "Je rangerai en rentrant."
            think "Ou pas."

        "Refermer le sac et le placard avant de sortir.":
            "Je referme le placard."
            "Je tire la fermeture du sac."
            think "Je sais pas pourquoi je fais ça."
            think "Par habitude, sûrement."

    "Je sors."

    stop music fadeout 1.0

    jump _8_0_1_CAFETERIA

label _8_0_1_CAFETERIA:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    "La cafétéria est pleine."
    "Enfin."
    "Plus pleine que d'habitude."

    "Ça parle fort."
    "Ça rit parfois."
    "Des vrais rires."
    "Pas des petits souffles nerveux pour éviter les silences."

    think "Deux jours."
    think "Deux jours sans Kami."

    "Et déjà l’endroit ressemble moins à une salle d’attente avant exécution."

    $ showGroup([
        ("iris",   "sourire",      0.08),
        ("julian", "decontracte",  0.25),
        ("lysa",   "neutre",       0.42),
        ("elias",  "detendu",      0.58),
        ("mara",   "rire",         0.75),
        ("tomas",  "fatigue",      0.92)
    ])

    iris sourire "Je commence à croire qu’on a officiellement des vacances."

    julian rire "Franchement ?"
    julian sourire "Je signe tout de suite pour une apocalypse silencieuse comme ça."

    mara rire "Toi tu signerais surtout pour dormir jusqu’à midi tous les jours."

    julian decontracte "Évidemment."
    julian rire "Le confort est une valeur fondamentale de l’humanité."

    elias detendu "Ça explique beaucoup de choses chez toi."

    julian sourire "Merci Elias."
    julian sourire "Ça fait plaisir d’être compris."

    "Je m’installe avec mon plateau."

    lysa neutre "T’as une sale tête."

    noam "Merci."

    lysa taquin "De rien."

    "Elle mange tranquillement."
    "Sans regarder autour toutes les trois secondes."
    "Sans attendre une annonce."

    think "C’est fou comme ça change tout."

    tomas fatigue "Hum."

    "Tomas fixe son écran portable."
    "Encore."

    iris taquin "Attention."
    iris sourire "Le scientifique du groupe va annoncer une catastrophe."

    tomas gene "Ce n’est pas une catastrophe."

    julian rire "Oh non."
    julian sourire "C’est encore pire alors."

    tomas reflechit "J’ai vérifié les statistiques publiques cette nuit."

    mara neutre "Pourquoi tu fais ça pendant ton temps libre ?"

    tomas panne "Je..."
    tomas gene "Je trouve ça reposant."

    iris rire "Il me terrifie."

    tomas reflechit "Depuis le vote du jour six..."
    tomas inquiet "Il n’y a eu aucune exécution."

    "Le bruit baisse légèrement."

    noam "Aucune ?"

    tomas reflechit "Zéro."
    tomas inquiet "Dans tous les districts."

    elias neutre "Attends."
    elias fatigue "Genre vraiment zéro ?"

    tomas "Oui."

    mara doute "C’est possible ça ?"

    tomas reflechit "Techniquement oui."
    tomas fatigue "Statistiquement..."
    tomas inquiet "C’est extrêmement improbable."

    julian decontracte "Donc."

    "Julian se redresse légèrement."

    julian rire "Si je résume bien."

    julian sourire "Elias renverse une pauvre tasse de café."

    julian taquin "Et BOUM."

    julian rire "Plus d’exécutions mondiales."

    iris rire "Putain."

    julian decontracte "Non mais regardez-le."
    julian sourire "Le héros de l’humanité."

    elias detendu "J’ai rien fait."

    julian rire "FAUX."
    julian colere "Tu as vaincu l’intelligence artificielle qui dirige le monde."

    julian sourire "Avec une seule petite tasse."

    mara rire "C’est vraiment ridicule dit comme ça."

    iris sourire "Moi j’aime bien cette version."

    elias fatigue "Vous êtes cons."

    "Mais il sourit quand même un peu."

    think "C’est la première fois que je vois Elias sourire depuis..."
    think "Je sais même plus."

    menu:
        "Rentrer dans la blague.":
            noam "Franchement Elias."
            noam "Respect."

            julian rire "Merci."
            julian sourire "Enfin quelqu’un de lucide."

            elias rire "Je vous déteste tous."

        "Rester prudent.":
            noam "Ou alors quelque chose déconne vraiment."

            "Le ton baisse légèrement."

            mara doute "Ouais."
            mara fatigue "Y’a aussi cette possibilité."

            tomas inquiet "C’est celle que je privilégie personnellement."

    iris taquin "En attendant, moi je profite."

    lysa blase "T’as peur que Kami revienne demain ?"

    iris fatigue "J’ai peur qu’elle revienne dans cinq minutes."

    "Petit silence."

    "Pas lourd."
    "Juste réel."

    julian decontracte "Eh."
    julian sourire "Alors profitons pendant qu’on peut."

    elias detendu "Pour une fois, je suis d’accord avec lui."

    mara rire "Notez la date."

    "Les discussions repartent."

    "Plusieurs conversations en même temps."
    "Des sujets idiots."
    "De la nourriture."
    "Du sommeil."
    "Des souvenirs."

    think "On dirait presque des gens normaux."

    think "Presque."

    "Je baisse les yeux vers mon plateau."

    think "Mon dessin n’était pas dans la chambre."

    think "Et ça me dérange toujours."

    "Mais ici."
    "Avec le bruit."
    "Avec les autres."

    "C’est plus facile de ne pas y penser."

    jump _8_0_1_TEMPS_LIBRE_1

label _8_0_1_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    call START_FREE_TIME("_8_0_1_APRES_MIDI_KAEL_CRISE") from _call_START_FREE_TIME_8_0_1

# --------------------------------------------------------------------------------------------
# JOUR 8 — Après-midi
# Kael débarque en crise dans l'espace commun.
# Découverte collective : la photo de Léa a disparu.
# Lancement du mini-jeu STABILISATION.
# Suivi : Noam décide de trouver le coupable.
# --------------------------------------------------------------------------------------------


# ============================================================
# LABEL — AMORCE DE LA CRISE
# ============================================================

label _8_0_1_APRES_MIDI_KAEL_CRISE:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    "L'après-midi était calme."
    "Vraiment calme."
    "Le genre de calme où on commence à se demander si c'est normal."

    $ showGroup([
        ("lysa",   "neutre",      0.15),
        ("ryn",    "decontracte", 0.35),
        ("elias",  "fatigue",     0.65),
        ("noam",   "neutre",      0.85),
    ])

    lysa "T'as vu Kael depuis ce matin ?"

    noam hesitation "Non."
    noam "Il était pas à la cafétéria ?"

    lysa "Si. Mais il est parti vite."
    lysa neutre "Il avait l'air… totalement bouleversé."

    noam "Comment ça ?!"

    ryn "Il tournait en rond dans les couloirs."
    ryn "Je l'ai croisé deux fois."
    ryn desaccord "La deuxième fois il m'a même pas vu."

    "Je pose mon verre."

    think "Qu'est ce qu'il foutait ?"

    menu:
        "Aller voir s'il va bien.":
            $ noam_nature_j8 = "proactif"
            think "Quelque chose cloche."
            think "J'y vais."
            noam "Je vais jeter un œil."
            lysa sourire "Bien."

        "Attendre, il est peut-être juste fatigué.":
            $ noam_nature_j8 = "reserve"
            think "On a tous nos moments."
            think "Je reste là."
            noam "Il sait où on est si besoin."
            ryn hesitation "Mouais..."

    $ hideGroup()

    pause 0.5

    # --- La porte s'ouvre ---

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    play sound "sfx/door_slam.mp3" volume 1.2

    with hpunch

    $ showGroup([
        ("kael",   "colere",  0.50),
    ])

    "La porte claque."

    "Kael."

    pause 0.3

    "Il s'arrête au milieu de l'espace commun."
    "Il cherche quelqu'un des yeux."
    "Ou tout le monde."
    "Difficile à dire."

    kael "C'est qui."

    "Ce n'est pas une question."

    pause 0.3

    $ showGroup([
        ("lysa",   "choc",    0.12),
        ("ryn",    "inquiet", 0.28),
        ("kael",   "colere",  0.50),
        ("elias",  "choc",    0.72),
        ("noam",   "inquiet", 0.88),
    ])

    elias "Kael ?"

    kael "C'est qui qui est entré dans ma chambre."

    "Le silence tombe d'un coup."
    "Comme un couvercle."

    pause 0.4

    ryn "Quoi ?"

    kael colere "Ma chambre."
    kael "Quelqu'un y est entré."
    kael "Et a pris quelque chose."

    lysa choc "Comment tu sais que—"

    kael "Parce que je la cherche depuis ce matin."
    kael colere "Parce que je l'ai cherchée partout."
    kael "Parce qu'elle n'est NULLE PART."
    kael "Et que je l'avais mise sous mon oreiller."

    pause 0.3

    think "Sous son oreiller."
    think "Il l'avait cachée."

    "Ryn ouvre la bouche."
    "La referme."

    elias hesitation "Qu'est-ce qui a disparu ?"

    pause 0.4

    kael inquiet "La photo de ma sœur."

    pause 0.6

    "Personne ne dit rien."

    "Lysa ferme les yeux une seconde."
    "Elias recule d'un demi-pas."
    "Ryn regarde le sol."

    pause 0.5

    think "Et là quelqu'un est entré."
    think "A cherché."
    think "Et a pris exactement ça."

    pause 0.3

    "Kael tremble."
    "Pas de rage."
    "Enfin, pas que de rage."

    kael colere "Alors je répète."
    kael "C'est QUI ?!"

    pause 0.4

    stop music fadeout 1.0
    play music "music/bgm_stabilisation_tension.mp3" fadein 0.8

    with vpunch

    # --- Lancement du mini-jeu ---

    call j801_play_stabilisation
    $ j801_stabilisation_result = _return

    jump _8_0_1_APRES_STABILISATION


# ============================================================
# LABEL — APRÈS LA STABILISATION
# ============================================================

label _8_0_1_APRES_STABILISATION:

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    play music "music/bgm_system_override.mp3" fadein 2.5

    pause 1.0

    "Personne ne parle."

    pause 0.6

    "Kael est assis."
    "Les coudes sur les genoux."
    "La tête baissée."
    "Il respire encore trop vite."
    "Mais il ne crie plus."

    pause 0.5

    $ showGroup([
        ("lysa",  "triste",   0.12),
        ("ryn",   "inquiet",  0.28),
        ("kael",  "effondre", 0.50),
        ("elias", "choc",     0.72),
        ("noam",  "neutre",   0.88),
    ])

    "Lysa pose une main sur l'accoudoir de sa chaise."
    "Pas sur son épaule."
    "Juste là. Près."

    pause 0.4

    ryn hesitation "On peut... vérifier les chambres ?"
    ryn "Pour voir si d'autres trucs ont—"

    kael "Ça changera rien."

    "Ryn se tait."

    kael inquiet "Elle est plus là."
    kael "C'est tout."

    pause 0.6

    elias "Qui aurait fait ça."

    "Ce n'est pas vraiment une question."
    "C'est juste ce que tout le monde pense."
    "Il a été le premier à le dire à voix haute."

    pause 0.4

    think "Qui."
    think "Quelqu'un qui savait où chercher."
    think "Quelqu'un qui connaît nos chambres."
    think "Qui sait ce qu'on y garde."

    pause 0.3

    think "Quelqu'un qui est là."

    pause 0.5

    "Je regarde le groupe."
    "Lysa."
    "Ryn."
    "Elias."
    "Kael."

    "Des visages que je connais depuis des jours."
    "Des gens avec qui j'ai mangé, voté, discuté."

    pause 0.3

    think "Et l'un d'entre eux, peut-être."
    think "..."
    think "Non."
    think "Peut-être pas quelqu'un du groupe."
    think "Peut-être quelqu'un d'autre."
    think "Quelqu'un qu'on ne voit pas."

    pause 0.4

    "Kami ne s'est pas manifestée depuis deux jours."
    "Mais le Conclave existe toujours."
    "Les couloirs sont surveillés."
    "Les chambres ont des serrures."
    "Des serrures que quelqu'un peut ouvrir."

    pause 0.3

    think "Ce silence de Kami."
    think "C'était vraiment un silence."
    think "Ou on regardait ailleurs pendant que quelque chose se passait ?"

    pause 0.6

    noam "Pour tout vous dire..."
    noam "Moi aussi, j'ai perdu quelque chose..."

    "Tout le monde se retourne vers moi."

    pause 0.3

    noam "Un dessin que ma petite soeur m'avait fait..."
    noam hesitation "Il a disparu aussi."
    noam "Ce matin. Je le cherchais depuis le réveil."

    lysa choc "Attends."
    lysa "Toi aussi ?"

    noam "Ouais..."

    pause 1.0

    elias "Donc c'est pas Kael qui a mal rangé."
    elias "C'est... systématique."
    elias "Comme mes outils hier."

    pause 0.3

    kael effondre "Je vous l'avais dit."

    pause 0.5

    think "Deux objets."
    think "Deux chambres."
    think "Deux choses personnelles."
    think "Rien de pratique. Rien d'utile."
    think "Juste ce qui compte pour nous."

    pause 0.5

    menu:
        "C'est un message.":
            $ noam_j8_choix_resolution = "direct"
            noam "C'est un message."
            noam "Quelqu'un veut qu'on sache qu'il peut entrer."
            noam "Qu'il sait ce qu'on a."
            "Lysa croise les bras."
            lysa neutre "Ou quelqu'un qui veut juste qu'on se méfie les uns des autres."
            noam "Ça aussi c'est un message."

        "Ne rien dire.":
            $ noam_j8_choix_resolution = "silencieux"
            think "Pas maintenant."
            think "Kael est encore trop à vif."
            think "Et je ne suis sûr de rien."

    $ hideGroup()

    pause 0.5

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Les minutes passent."
    "Puis, un par un, ils commencent à se lever."
    "Pas forcément pour partir."
    "Juste parce que rester assis à rien faire devient insupportable."

    pause 0.3

    "Je reste."

    think "Il faut trouver qui a fait ça."

    pause 0.3

    if noam_j8_choix_resolution == "direct":
        think "J'ai dit ce que je pensais."
        think "C'est un début."
    else:
        think "J'aurais dû le dire."
        think "Peut-être."
        think "Ou peut-être pas."

    pause 0.2

    think "Ce que je sais :"
    think "Quelqu'un est entré dans nos chambres."
    think "A pris exactement ce qui comptait."
    think "Et on n'a aucun moyen de savoir qui."
    think "Pour l'instant."

    pause 0.4

    think "Pour l'instant."

    pause 0.6

    $ journal_entries.append(("Jour 8 — soir", "La photo de Léa. Le dessin de Juliette. Deux objets. Deux chambres. Quelqu'un sait ce qu'on garde. Ce que ça veut dire, je préfère pas y penser trop longtemps. Mais je vais trouver qui."))

    stop music fadeout 2.0

    scene black with fade

    jump _8_0_1_SOIREE

label _8_0_1_SOIREE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0

    "Je retourne dans ma chambre après avoir erré dans les couloirs."
    "La porte se referme derrière moi."

    "Je reste debout au milieu de la pièce un long moment."

    think "Deux jours sans Kami."
    think "Et on est déjà en train de se déchirer."

    "Je regarde le lit. Le sac encore ouvert. Le placard mal fermé."
    "J'ai vraiment foutu le bordel ce matin..."

    think "Le dessin n’est toujours pas revenu."

    pause 0.7

    "Je m’assois sur le bord du lit."

    think "Quelqu’un est entré ici."
    think "Quelqu’un sait ce qui compte pour moi."
    think "Et il l’a pris."

    "Je passe une main sur mon visage."

    think "Ce n’est plus un jeu."
    think "Ce n’est plus une expérience de Kami."

    "Je regarde l’écran mural. Toujours noir."

    think "Ou alors… c’est exactement ce qu’elle voulait."
    think "Tout fonctionne peut être selon son plan ?"

    pause 1.0

    "Je me lève et vais bloquer la porte avec une chaise."
    "Personne ne pourra rentrer comme ça."

    "Avant de m’allonger, je jette un dernier regard vers le placard."

    think "Demain, je trouverai qui a fait ça."
    think "Même si c’est l’un de nous."

    $ journal_entries.append(("Jour 8 — conclusion", "Quelqu’un nous observe. Quelqu’un nous connaît et nous vole. Et ce quelqu’un est parmi nous."))

    call end_day("9")
    jump _9_0_1_REVEIL_CHAMBRE