# Menus de statistiques J11-J20 : mêmes écrans, pas de mécanique dupliquée.
init 4 python:
    STAT_DIALOGUES.update({
        "j11": {"prompt": "Kael vient d'apprendre que les images seront bloquées une semaine.", "options": [
            _sd_option("pause", "On devrait souffler un peu. Ça sert à rien de s'épuiser maintenant.", "sd_j11_pause"),
            _sd_option("relire", "On peut relire ensemble ce que Kami a dit sur les sept jours.", "sd_j11_relire"),
            _sd_option("aider", "Si tu dois transporter des dossiers, je peux venir avec toi.", "sd_j11_aider"),
            _sd_option("detail", "Tu t'attendais à ce délai, non ?", "sd_j11_detail", requires={"observation": 2}),
        ]},
        "j12": {"prompt": "Le débat sur les brouilleurs s'emballe.", "options": [
            _sd_option("risque", "Faut aussi parler des risques. Si quelqu'un fait une connerie, on le saura trop tard.", "sd_j12_risque"),
            _sd_option("prive", "Je comprends Mara. On devrait pouvoir être tranquilles dans nos chambres.", "sd_j12_prive"),
            _sd_option("franc", "On ferait mieux de demander à chacun ce qu'il veut vraiment.", "sd_j12_franc"),
            _sd_option("nuance", "Attendez. Les images ne disparaissent pas, elles sont juste bloquées sept jours, non ?", "sd_j12_nuance", requires={"observation": 3}),
        ]},
        "j13": {"prompt": "Elen a peur d'être surveillée en permanence.", "options": [
            _sd_option("ecouter", "Je comprends. Moi non plus, ça me plaît pas d'être observé tout le temps.", "sd_j13_ecouter"),
            _sd_option("verifier", "On devrait demander ce que les caméras peuvent vraiment voir.", "sd_j13_verifier"),
            _sd_option("calmer", "Je vais pas te dire que tout va bien, mais on peut essayer de pas paniquer.", "sd_j13_calmer"),
        ]},
        "j14": {"prompt": "Nyra a des réserves sur la publication des données d'ARCHIVE.", "options": [
            _sd_option("donnees", "Il y a aussi des dossiers privés là-dedans. Qui décide ce qui devient public ?", "sd_j14_donnees"),
            _sd_option("respect", "Je veux pas que les dossiers des gens soient publiés sans leur accord.", "sd_j14_respect"),
            _sd_option("soulever", "Alors on devrait poser la question devant tout le monde avant le vote.", "sd_j14_soulever"),
            _sd_option("precision", "Tu as déjà repéré un problème dans le texte, c'est ça ?", "sd_j14_precision", requires={"observation": 3}),
        ]},
        "j15": {"prompt": "Kael et Noam cherchent des indices dans les enregistrements.", "options": [
            _sd_option("horaires", "On peut comparer les heures des portes avec celles de la vidéo.", "sd_j15_horaires"),
            _sd_option("soutien", "Si t'as besoin de souffler, dis-le. Je sais que cette photo compte beaucoup.", "sd_j15_soutien"),
            _sd_option("regarder", "Je vais suivre la vidéo pendant que tu regardes les journaux.", "sd_j15_regarder"),
            _sd_option("journal", "Il y a un journal des consultations, ou seulement des modifications ?", "sd_j15_journal", requires={"logique": 3}),
        ]},
        "j16": {"prompt": "Kael s'est isolé dans sa chambre.", "options": [
            _sd_option("aller", "Je vais passer le voir. S'il veut pas parler, je le laisserai tranquille.", "sd_j16_aller"),
            _sd_option("espace", "On devrait lui laisser un peu d'air au lieu de lui tomber dessus.", "sd_j16_espace"),
            _sd_option("discret", "On peut demander discrètement si quelqu'un l'a vu ce matin.", "sd_j16_discret"),
        ]},
        "j17": {"prompt": "Nyra propose de maintenir le boycott des votes.", "options": [
            _sd_option("plan", "D'accord, mais demain il nous faut un plan. On peut pas juste attendre.", "sd_j17_plan"),
            _sd_option("autres", "On devrait aller voir ceux qui ont l'air le plus mal depuis l'annonce.", "sd_j17_autres"),
            _sd_option("calme", "On garde notre position aujourd'hui. Pas question de décider dans la panique.", "sd_j17_calme"),
            _sd_option("conditions", "Si Kami recommence à nous menacer, on lui demande de répéter les conditions devant tout le monde.", "sd_j17_conditions", requires={"audace": 3}),
        ]},
        "j18": {"prompt": "Mara veut explorer le conduit supérieur.", "options": [
            _sd_option("passer", "Je peux passer en premier. On verra vite si ça se rétrécit.", "sd_j18_passer"),
            _sd_option("attaches", "Attends, on vérifie les fixations avant de grimper.", "sd_j18_attaches"),
            _sd_option("doucement", "On avance doucement. Si c'est trop dangereux, on redescend.", "sd_j18_doucement"),
        ]},
        "j19": {"prompt": "Kael s'inquiète des caméras dans les conduits.", "options": [
            _sd_option("sur", "J'en ai pas vu, mais ça veut pas dire qu'il n'y en a pas.", "sd_j19_sur"),
            _sd_option("comprendre", "Ça me fait peur aussi. On sait même plus si on est tranquilles dans nos chambres.", "sd_j19_comprendre"),
            _sd_option("acces", "Il faudrait repérer les grilles et voir où elles donnent.", "sd_j19_acces"),
            _sd_option("angles", "Tu parles des caméras des portes ou de celles des couloirs ?", "sd_j19_angles", requires={"logique": 3}),
        ]},
        "j20": {"prompt": "Kael hésite à dire quelque chose.", "options": [
            _sd_option("ecouter", "Vas-y. Je t'écoute. Prends ton temps.", "sd_j20_ecouter"),
            _sd_option("direct", "Kael, dis-moi ce qui te tracasse. On peut pas continuer comme ça.", "sd_j20_direct"),
            _sd_option("grille", "T'arrêtes pas de regarder la grille. C'est à cause de ce qu'on a trouvé ?", "sd_j20_grille"),
            _sd_option("seul", "Tu attendais qu'Iris sorte pour me parler, non ?", "sd_j20_seul", requires={"observation": 3}),
        ]},
    })

# Chaque réponse ordinaire rapporte 1 XP. Les bonus verrouillés ne rapportent aucune XP.

label sd_j11_pause:
    kael triste "Ouais. J'ai la tête en vrac."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j11_relire:
    kael calme "Oui. Je veux être sûr de pas avoir mal compris."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j11_aider:
    kael calme "Merci. Mais repose-toi, Noam. T'as vraiment pas l'air bien."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

# Bonus j11 : observation 2, sans XP.
label sd_j11_detail:
    kael triste "J'avais vu passer un truc dessus. Je pensais avoir mal compris."
    noam "Tu peux me montrer ?"
    kael "Ouais. Si je retrouve le fichier."
    noam "D'accord. On vérifiera ça ensemble."
    return

label sd_j12_risque:
    tomas "Oui. On peut pas ignorer ce problème."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j12_prive:
    mara "Merci ! Enfin quelqu'un qui comprend !"
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j12_franc:
    tomas "Oui. Mais laissez au moins les autres finir de parler."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# Bonus j12 : observation 3, sans XP.
label sd_j12_nuance:
    tomas "Oui. C'est ce que Kami a dit."
    kael triste "Sept jours, c'est déjà énorme quand on cherche quelqu'un."
    noam "Je sais. Mais il faut que tout le monde comprenne ce qu'on vote."
    tomas "Je vais le rappeler avant de continuer."
    return

label sd_j13_ecouter:
    elen triste "Merci. J'avais l'impression d'être la seule à y penser."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j13_verifier:
    iris inquiet "Oui. On sait même pas ce qu'elle garde."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j13_calmer:
    elen triste "Ouais... je vais essayer."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j14_donnees:
    nyra raison "Voilà. Le texte ne le précise pas."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j14_respect:
    nyra neutre "Moi non plus. Il faut le dire clairement."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j14_soulever:
    nyra raison "Oui. C'est ce que je compte faire."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# Bonus j14 : observation 3, sans XP.
label sd_j14_precision:
    nyra reflexion "Il manque deux choses : qui consulte les données personnelles et comment on les retire."
    noam "Et si une information est fausse ?"
    nyra "Avec ce texte, rien ne garantit qu'on puisse la corriger."
    noam "Alors il faut le demander avant de voter."
    nyra raison "Exactement."
    return

label sd_j15_horaires:
    kael reflechit "Oui. Je vais ouvrir les deux fichiers."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j15_soutien:
    kael triste "Merci. Mais je préfère continuer."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j15_regarder:
    kael calme "Ça m'aidera. J'ai peur de rater un détail."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# Bonus j15 : logique 3, sans XP.
label sd_j15_journal:
    kael reflechit "Attends... oui, il y en a un."
    noam "Ça prouve qu'on a touché aux images ?"
    kael "Non. Juste que le fichier a été ouvert."
    noam "C'est déjà une piste. Mais on accuse personne avec ça."
    kael calme "Ouais."
    return

label sd_j16_aller:
    nyra reflexion "D'accord. N'insiste pas s'il refuse."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

label sd_j16_espace:
    iris inquiet "Oui. Ça risque de le braquer sinon."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j16_discret:
    nyra raison "Je peux vérifier ça."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j17_plan:
    nyra raison "C'est prévu. On fait le point demain."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j17_autres:
    elen inquiet "Je peux m'en occuper."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j17_calme:
    nyra neutre "Oui. Personne ne cède sous la pression."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# Bonus j17 : audace 3, sans XP.
label sd_j17_conditions:
    nyra reflexion "Pour éviter qu'elle change de version ?"
    noam "Oui. Au moins, tout le monde aura entendu la même chose."
    ryn "Et si elle nous envoie balader ?"
    noam "On aura au moins essayé."
    nyra raison "D'accord. Mais pas de provocation inutile."
    return

label sd_j18_passer:
    mara rire "Te coince pas. J'ai pas envie de te tirer par les pieds."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

label sd_j18_attaches:
    mara reflexion "Pas con. J'ai pas envie de finir le cul par terre."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

label sd_j18_doucement:
    mara "Ouais. On reste à portée de voix."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

label sd_j19_sur:
    kael inquietude "Ouais. On sait pas encore."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

label sd_j19_comprendre:
    kael triste "C'est exactement ça."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j19_acces:
    nyra raison "Je peux aider à faire la liste."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# Bonus j19 : logique 3, sans XP.
label sd_j19_angles:
    kael reflechit "Les deux. Mais les angles sont pas les mêmes."
    noam "On pourrait donc sortir d'une grille sans passer devant celle de la porte ?"
    kael "Peut-être. Faudrait les plans."
    noam "Alors vérifions avant de dire que tout le monde peut entrer partout."
    return

label sd_j20_ecouter:
    kael doute "Ouais... attends une seconde."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

label sd_j20_direct:
    kael doute "Je sais. C'est compliqué."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

label sd_j20_grille:
    kael doute "Pas seulement. J'essaie encore de comprendre."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# Bonus j20 : observation 3, sans XP.
label sd_j20_seul:
    kael doute "Je voulais savoir si tu comptais retourner dans les conduits."
    noam "Pas tout seul, en tout cas."
    kael "Tant mieux. J'ai pas envie de revivre ce qui s'est passé."
    noam "Tu sais autre chose ?"
    kael "Pas assez pour t'en parler comme si j'étais sûr."
    return
