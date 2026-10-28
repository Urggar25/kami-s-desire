# Choix de stats des jours 21-30 : aucune route principale modifiée.
init 4 python:
    STAT_DIALOGUES.update({
        "j21": {"prompt": "Elias vérifie le matériel.", "options": [
            _sd_option("inventaire", "On vérifie les quantités avant de déplacer quoi que ce soit.", "sd_j21_inventaire"),
            _sd_option("caisses", "Je peux porter les caisses les plus lourdes.", "sd_j21_caisses"),
            _sd_option("pause", "T'as l'air crevé. On peut souffler deux minutes.", "sd_j21_pause"),
        ]},
        "j22": {"prompt": "Elias parle des pièces manquantes.", "options": [
            _sd_option("liste", "On devrait noter exactement ce qu'il manque avant de chercher.", "sd_j22_liste"),
            _sd_option("plaques", "Je peux déplacer les plaques qu'on a déjà.", "sd_j22_plaques"),
            _sd_option("chercher", "On peut regarder près des grilles. Elles ont peut-être été laissées là.", "sd_j22_chercher"),
        ]},
        "j23": {"prompt": "Sael propose un examen.", "options": [
            _sd_option("limites", "Qu'est-ce que l'examen peut vraiment nous apprendre ?", "sd_j23_limites"),
            _sd_option("explication", "D'accord, mais tu m'expliques chaque étape avant de commencer.", "sd_j23_explication"),
            _sd_option("faire", "On le fait. J'en ai marre de pas savoir.", "sd_j23_faire"),
            _sd_option("souvenir", "Ça peut vérifier mes souvenirs, ou seulement mon état physique ?", "sd_j23_souvenir", requires={"logique": 3}),
        ]},
        "j24": {"prompt": "Ryn s'inquiète du vote.", "options": [
            _sd_option("agir", "Alors on continue à chercher. Mais il nous faut quelque chose avant le vote.", "sd_j24_agir"),
            _sd_option("avis", "On devrait demander aux autres ce qu'ils accepteraient.", "sd_j24_avis"),
            _sd_option("calme", "On peut chercher sans passer la journée à se crier dessus.", "sd_j24_calme"),
        ]},
        "j25": {"prompt": "Iris examine la salle.", "options": [
            _sd_option("sol", "Attends, je veux regarder le sol avant qu'on avance.", "sd_j25_sol"),
            _sd_option("prudence", "On ne déplace rien tant qu'on sait pas ce qu'on cherche.", "sd_j25_prudence"),
            _sd_option("caisse", "Je peux bouger cette caisse pour que tu voies derrière.", "sd_j25_caisse"),
            _sd_option("poussiere", "Il y a une trace dans la poussière, là. On devrait la prendre en photo.", "sd_j25_poussiere", requires={"observation": 3}),
        ]},
        "j26": {"prompt": "Le double veut parler.", "options": [
            _sd_option("clair", "Alors explique-moi exactement ce que tu veux.", "sd_j26_clair"),
            _sd_option("distance", "Je t'écoute, mais reste là où tu es.", "sd_j26_distance"),
            _sd_option("dur", "Tu te rends compte de ce que tu me demandes ?", "sd_j26_dur"),
            _sd_option("inquiet", "Tu as peur que je refuse, c'est ça ?", "sd_j26_inquiet", requires={"observation": 3}),
        ]},
        "j27": {"prompt": "Tomas demande ce que Noam fera pour son original.", "options": [
            _sd_option("honnette", "Je sais pas encore. Je veux pas promettre quelque chose que je ferai pas.", "sd_j27_honnette"),
            _sd_option("zero", "On devrait d'abord savoir ce que Zero prévoit exactement.", "sd_j27_zero"),
            _sd_option("parler", "Je vais lui parler. Je peux pas laisser les autres décider à ma place.", "sd_j27_parler"),
        ]},
        "j28": {"prompt": "Mara s'inquiète du départ.", "options": [
            _sd_option("peur", "Je comprends que ça te fasse peur. On sait pas vraiment ce qu'on trouvera là-bas.", "sd_j28_peur"),
            _sd_option("infos", "On devrait vérifier ce qu'on sait de cette planète.", "sd_j28_infos"),
            _sd_option("temps", "On peut en parler sans décider tout de suite.", "sd_j28_temps"),
        ]},
        "j29": {"prompt": "Kael prépare l'opération.", "options": [
            _sd_option("voyants", "Je garde un œil sur les voyants. Tu me dis si ça change.", "sd_j29_voyants"),
            _sd_option("porter", "Si tu dois déplacer du matériel, je peux aider.", "sd_j29_porter"),
            _sd_option("doucement", "On va essayer de pas lui faire plus peur qu'il ne l'est déjà.", "sd_j29_doucement"),
            _sd_option("copie", "Tu as une copie de secours si le transfert se passe mal ?", "sd_j29_copie", requires={"logique": 4}),
        ]},
        "j30": {"prompt": "Le double attend la décision.", "options": [
            _sd_option("minute", "Je vais te répondre. J'ai juste besoin d'une minute.", "sd_j30_minute"),
            _sd_option("autres", "Je dois aussi penser à ce que ça change pour les autres.", "sd_j30_autres"),
            _sd_option("decision", "Je sais. C'est à moi de décider, et je vais le faire.", "sd_j30_decision"),
        ]},
    })

# Réponses normales : 1 XP. Réponses conditionnelles : bonus sans XP.

label sd_j21_inventaire:
    elias fatigue "Ouais. Parce que s'il en manque encore, on est mal."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j21_caisses:
    elias fatigue "Vas-y. Mais fais gaffe au coin."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

label sd_j21_pause:
    elias fatigue "Après. Je veux juste finir."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j22_liste:
    elias reflexion "Ouais. Ça sera plus simple."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j22_plaques:
    elias fatigue "D'accord. Pose-les contre le mur."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

label sd_j22_chercher:
    elias fatigue "Ça vaut le coup de vérifier."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j23_limites:
    sael neutre "Pas tout. Mais on aura au moins des éléments."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j23_explication:
    sael neutre "C'est prévu."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j23_faire:
    sael neutre "D'accord. On prépare ça."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# Bonus verrouillé : logique >= 3.
label sd_j23_souvenir:
    sael neutre "L'état physique. Ça ne dira pas si ton souvenir est vrai."
    noam "Donc si tout est normal, ça prouve pas que j'ai inventé la scène."
    sael "Non. Je ne te dirai pas le contraire."
    return

label sd_j24_agir:
    ryn "Là-dessus, on est d'accord."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

label sd_j24_avis:
    tomas raison "Ça éviterait de découvrir les problèmes au dernier moment."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j24_calme:
    ryn desaccord "Ouais, bon. J'ai compris."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j25_sol:
    iris neutre "D'accord. Mais touche à rien."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j25_prudence:
    iris neutre "Oui. On fait ça dans l'ordre."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j25_caisse:
    iris neutre "Vas-y doucement, je t'éclaire."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

# Bonus verrouillé : observation >= 3.
label sd_j25_poussiere:
    iris reflexion "Où ça ?"
    noam "Près du bord. Je sais pas quand ça a bougé."
    iris inquiet "D'accord. On photographie avant de toucher."
    noam "Oui. J'ai pas envie de perdre une autre preuve."
    return

label sd_j26_clair:
    dg_noam neutre "D'accord. Je vais essayer."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j26_distance:
    dg_noam calme "OK. Je bouge pas."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j26_dur:
    dg_noam fatigue "Oui. Je sais que c'est pas juste."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# Bonus verrouillé : observation >= 3.
label sd_j26_inquiet:
    dg_noam fatigue "Ouais. Je sais pas ce que je ferai si tu refuses."
    noam "Merci de me le dire au moins."
    dg_noam calme "J'ai pas envie de te mentir."
    return

label sd_j27_honnette:
    tomas fatigue "Au moins, c'est honnête."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j27_zero:
    tomas raison "Oui. Ça aiderait."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j27_parler:
    tomas raison "C'est probablement la bonne chose à faire."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

label sd_j28_peur:
    mara fatigue "Ouais. C'est exactement ça."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j28_infos:
    tomas raison "C'est ce que j'essaie de faire."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j28_temps:
    mara agace "Ouais. Mais pas au dernier moment."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j29_voyants:
    kael raison "OK. Mais touche à rien."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j29_porter:
    kael raison "Merci. Pour l'instant, reste là."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

label sd_j29_doucement:
    kael calme "Oui. Faisons ça calmement."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# Bonus verrouillé : logique >= 4.
label sd_j29_copie:
    kael reflechit "Oui. Mais je préfère ne pas devoir l'utiliser."
    noam "Tu me le dis si ça bloque, d'accord ?"
    kael raison "D'accord."
    return

label sd_j30_minute:
    dg_noam neutre "D'accord. Je t'écoute."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j30_autres:
    dg_noam fatigue "Ouais. Je sais."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j30_decision:
    dg_noam neutre "D'accord. C'est tout ce que je te demande."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return
