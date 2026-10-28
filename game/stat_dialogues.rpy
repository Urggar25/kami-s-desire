# =============================================================
# CHOIX DE DIALOGUE À STATISTIQUES — JOURS 1 À 9
# =============================================================

init 3 python:
    def _sd_option(option_id, text, target, requires=None):
        return {
            "id": option_id,
            "text": text,
            "target": target,
            "requires": requires or {},
        }

    def stat_dialogue_option(dialogue, option_id):
        for option in dialogue["options"]:
            if option["id"] == option_id:
                return option
        raise ValueError("Choix de statistique inconnu : {}".format(option_id))

    # Chaque échange comporte trois réponses ordinaires et de zéro à deux réponses
    # conditionnelles (exceptionnelles). Éviter deux verrous sauf si les deux
    # approches enrichissent réellement une situation narrative majeure. Les variantes couvrent tous les points d'entrée jouables.
    STAT_DIALOGUES = {
        "d1": {
            "prompt": "Lysa baisse la voix. « Tu crois qu'on peut vraiment se faire confiance ici ? »",
            "options": [
                _sd_option("prudent", "Franchement, j'en sais rien. On vient à peine d'arriver et j'ai déjà l'impression que tout le monde se méfie de tout le monde.", "sd_d1_prudent"),
                _sd_option("solidaire", "Je dis pas qu'on doit se faire confiance les yeux fermés. Mais on peut au moins essayer de s'entraider, non ?", "sd_d1_solidaire"),
                _sd_option("details", "Lysa, je t'ai vue trembler tout à l'heure. Tu vas pas me dire que tout va bien ?", "sd_d1_details", requires={"observation": 2}),
                _sd_option("souffler", "Je vais déjà essayer de reprendre mon souffle. Depuis le réveil, j'ai les jambes en coton, et j'aime pas ça.", "sd_d1_souffler"),
            ],
        },
        "d2": {
            "prompt": "Tomas regarde les autres tables. « Comment tu veux aborder ce premier vote ? »",
            "options": [
                _sd_option("ecouter", "Avant de défendre quoi que ce soit, je veux comprendre ce que chacun risque de perdre avec ce vote.", "sd_d2_ecouter"),
                _sd_option("texte", "Je vais déjà relire la proposition mot par mot. Si on se trompe sur ce qu'on vote, on est mal partis.", "sd_d2_texte"),
                _sd_option("frontal", "Ça suffit de tourner autour du pot. Je vais leur demander directement ce qu'ils comptent voter.", "sd_d2_frontal", requires={"audace": 2}),
                _sd_option("observer", "Avant d'aller leur parler, on pourrait regarder qui s'assoit avec qui. Ça nous donnera peut-être une idée des alliances.", "sd_d2_observer"),
            ],
        },
        "d3": {
            "prompt": "Julian croise les bras. « Une voix peut tout faire échouer. Tu proposes quoi ? »",
            "options": [
                _sd_option("coalition", "On devrait commencer par chercher ce sur quoi tout le monde est d'accord. Après, on verra ce qui bloque.", "sd_d3_coalition"),
                _sd_option("pression", "S'ils veulent voter contre, très bien. Mais je veux qu'ils regardent aussi les conséquences de ce refus.", "sd_d3_pression"),
                _sd_option("peur", "Et si on leur demandait d'abord ce qui leur fait peur ? À mon avis, certains ne disent pas vraiment pourquoi ils hésitent.", "sd_d3_peur", requires={"empathie": 2}),
                _sd_option("garder_tete", "On va éviter de s'énerver avant même d'entrer. Si quelqu'un cherche à nous provoquer, je préfère garder la tête froide.", "sd_d3_garder_tete"),
            ],
        },
        "d4_0": {
            "prompt": "Ryn frappe la table. « On a perdu hier. Tu comptes encore demander gentiment ? »",
            "options": [
                _sd_option("tenir", "Je veux comprendre ce qui a fait échouer le vote. Si on sait pas où on s'est plantés, on va refaire exactement la même erreur.", "sd_d4_0_tenir"),
                _sd_option("relancer", "Oui, et je vais recommencer tant qu'on n'aura pas de vraie réponse. On peut pas juste faire comme si rien ne s'était passé.", "sd_d4_0_relancer"),
                _sd_option("rester_calme", "Je suis aussi énervé que toi, Ryn. Mais si on retourne les voir en hurlant, on va juste se faire claquer la porte au nez.", "sd_d4_0_rester_calme"),
            ],
        },
        "d4_1": {
            "prompt": "Sael me dévisage. « Vous avez gagné le commerce. Cela vous suffit-il ? »",
            "options": [
                _sd_option("consequences", "Je suis content qu'on ait obtenu ce vote, mais je veux voir ce que ça change vraiment. Sinon, on saura jamais si on a eu raison.", "sd_d4_1_consequences"),
                _sd_option("humains", "Non, évidemment. On a réussi à faire circuler les marchandises, mais les gens sont toujours coincés derrière les frontières.", "sd_d4_1_humains"),
                _sd_option("calme", "D'accord. Je ne vais pas essayer de vous convaincre tout de suite. Dites-moi seulement ce qui vous empêche d'accepter.", "sd_d4_1_calme", requires={"sang_froid": 2}),
                _sd_option("regarder", "Je veux surtout voir ce que ça change pour les gens. On a voté le texte, mais on n'a encore rien vu de ses effets.", "sd_d4_1_regarder"),
            ],
        },
        "d5_0": {
            "prompt": "Sael soupire. « Vous savez déjà que je voterai non. Pourquoi insister ? »",
            "options": [
                _sd_option("raison", "Parce que je voudrais comprendre ce qui vous bloque. Je connais déjà votre vote, mais pas vraiment vos raisons.", "sd_d5_0_raison"),
                _sd_option("limite", "Parce que je suis pas convaincu que tout soit non négociable. Il doit bien y avoir quelque chose qu'on peut revoir ensemble.", "sd_d5_0_limite"),
                _sd_option("micro", "Chaque fois qu'on parle des frontières, vous vous arrêtez au milieu de vos phrases. Il y a quelque chose que vous ne nous dites pas ?", "sd_d5_0_micro", requires={"observation": 3}),
                _sd_option("tenir_bon", "Parce que je suis venu vous parler, et je vais pas partir juste parce que la discussion est désagréable. On peut au moins essayer.", "sd_d5_0_tenir_bon"),
            ],
        },
        "d5_1": {
            "prompt": "Kael fixe l'écran éteint. « Si ma sœur est à C-3, je dois faire quoi ? »",
            "options": [
                _sd_option("present", "Attends, Kael. Respire un peu. On va reprendre ce qu'on sait de ta sœur et voir ce qu'on peut faire, sans inventer le pire.", "sd_d5_1_present"),
                _sd_option("agir", "Dis-moi tout ce que tu sais, même les détails qui te semblent inutiles. Après, on trouvera comment bouger.", "sd_d5_1_agir"),
                _sd_option("alerte", "L'alerte ne correspond pas à une rupture totale du complexe.", "sd_d5_1_alerte", requires={"logique": 3}),
                _sd_option("soutenir", "Si tu dois aller chercher quelqu'un ou transporter du matériel, je viens avec toi. On va pas te laisser gérer ça tout seul.", "sd_d5_1_soutenir"),
            ],
        },
        "d6_0_1": {
            "prompt": "Mara observe la porte du Conclave. « On entre malgré le texte incompréhensible ? »",
            "options": [
                _sd_option("procedure", "On entre, mais je veux qu'on exige une explication avant le vote. Impossible de se prononcer sur un texte qu'on comprend pas.", "sd_d6_0_1_procedure"),
                _sd_option("ensemble", "On y va tous ensemble. Si Kami essaie de nous mettre la pression, personne ne doit se retrouver seul à lui répondre.", "sd_d6_0_1_ensemble"),
                _sd_option("refus", "Si elle nous presse, je prends la parole et je refuse le cadre.", "sd_d6_0_1_refus", requires={"audace": 3}),
                _sd_option("reperer", "Attends une seconde. On regarde d'abord les issues et les caméras, histoire de savoir où on met les pieds.", "sd_d6_0_1_reperer"),
            ],
        },
        "d6_1_0": {
            "prompt": "Lysa murmure. « Le vote est perdu d'avance. On joue quand même la scène ? »",
            "options": [
                _sd_option("trace", "Oui. Même si on perd aujourd'hui, il faut qu'on sache précisément ce que chacun nous reproche. Ça servira pour la suite.", "sd_d6_1_0_trace"),
                _sd_option("sael", "Oui. Et je veux surtout que Sael comprenne qu'on ne la considère pas comme une ennemie juste parce qu'elle vote contre.", "sd_d6_1_0_sael"),
                _sd_option("hesitation", "Elle évite mon regard depuis ce matin. Sa décision n'est pas aussi solide qu'elle le dit.", "sd_d6_1_0_hesitation", requires={"observation": 3}),
                _sd_option("oser", "Même si Sael vote contre, j'ai pas envie de rester assis à faire semblant. Je vais lui poser la question devant tout le monde.", "sd_d6_1_0_oser"),
            ],
        },
        "d7_0_1": {
            "prompt": "Tomas tient son rapport contre lui. « Plus aucune exécution. Tu comprends ce que ça signifie ? »",
            "options": [
                _sd_option("verifier", "Que c'est énorme, mais qu'on ferait mieux de vérifier avant de commencer à raconter n'importe quoi.", "sd_d7_0_1_verifier"),
                _sd_option("espoir", "Que, pour une fois, des gens ont peut-être survécu à une journée entière sans craindre d'être exécutés. Rien que ça, c'est immense.", "sd_d7_0_1_espoir"),
                _sd_option("motif", "Le silence de Kami et l'arrêt des exécutions ont commencé ensemble.", "sd_d7_0_1_motif", requires={"logique": 3}),
                _sd_option("se_risquer", "Alors on devrait aller le dire aux autres tout de suite, quitte à se tromper. On ne peut pas garder ça pour nous.", "sd_d7_0_1_se_risquer"),
            ],
        },
        "d7_1_0": {
            "prompt": "Iris bloque la porte. « On cache cette femme ou on prévient Kami ? »",
            "options": [
                _sd_option("soins", "On peut débattre de ce qu'on doit dire à Kami après. Là, il faut surtout vérifier qu'elle va tenir le coup.", "sd_d7_1_0_soins"),
                _sd_option("cacher", "On la cache. Je sais que c'est risqué, mais je refuse de la livrer à Kami alors qu'elle est à peine consciente.", "sd_d7_1_0_cacher"),
                _sd_option("symptomes", "Sa respiration indique qu'on n'a que quelques minutes pour la déplacer.", "sd_d7_1_0_symptomes", requires={"observation": 3}),
                _sd_option("peur", "Tu veux la cacher parce qu'elle te rappelle quelqu'un.", "sd_d7_1_0_peur", requires={"empathie": 3}),
                _sd_option("porter", "On la met à l'abri d'abord. Je peux la porter jusqu'à l'infirmerie si vous me montrez le chemin.", "sd_d7_1_0_porter"),
            ],
        },
        "d7_1_0_1": {
            "prompt": "Nyra fixe la caméra. « Si nous appelons Kami, il faut contrôler les premiers mots. »",
            "options": [
                _sd_option("medical", "On lui dit qu'on a trouvé une femme blessée et qu'elle a besoin de soins. Pas besoin de raconter toute l'histoire d'un coup.", "sd_d7_1_0_1_medical"),
                _sd_option("responsable", "Je vais parler en premier. Si Kami cherche un responsable, elle pourra s'en prendre à moi plutôt qu'aux autres.", "sd_d7_1_0_1_responsable"),
                _sd_option("unite", "On parle au pluriel. Elle ne doit pouvoir isoler personne.", "sd_d7_1_0_1_unite", requires={"sang_froid": 3}),
                _sd_option("tenir_calme", "On va lui parler sans hausser la voix. Si Kami cherche à nous faire paniquer, faut surtout pas lui donner ce plaisir.", "sd_d7_1_0_1_tenir_calme"),
            ],
        },
        "d8": {
            "prompt": "Kael serre sa photo disparue contre son souvenir. « Dis-moi que ce n'est pas quelqu'un d'ici. »",
            "options": [
                _sd_option("promesse", "Je vais pas te mentir, Kael. J'en sais rien. Mais si tu veux chercher qui a fait ça, je viens avec toi.", "sd_d8_promesse"),
                _sd_option("indices", "On devrait reprendre les horaires et voir qui pouvait entrer dans ta chambre. Il doit forcément rester une trace quelque part.", "sd_d8_indices"),
                _sd_option("cible", "Le dessin et la photo ont la même fonction : nous rappeler quelqu'un.", "sd_d8_cible", requires={"logique": 3}),
                _sd_option("garder_calme", "Je sais que t'as peur, Kael. Mais on va commencer par regarder ce qu'on a, sans accuser quelqu'un au hasard.", "sd_d8_garder_calme"),
            ],
        },
        "d9": {
            "prompt": "Ryn regarde les écrans. « Kami est revenue. On suit encore sa procédure ? »",
            "options": [
                _sd_option("temps", "On fait semblant de suivre sa procédure pour l'instant. Chaque minute qu'on gagne peut aider les gens dans les campements.", "sd_d9_temps"),
                _sd_option("prevenir", "On doit prévenir les gens, Ryn. Je préfère prendre le risque de me faire repérer plutôt que de les laisser sans rien savoir.", "sd_d9_prevenir"),
                _sd_option("provoquer", "Je la provoque à l'écran pendant que vous détournez le signal.", "sd_d9_provoquer", requires={"sang_froid": 3}),
                _sd_option("tenir_position", "On reste près des sorties et on se tient prêts à aider les autres si ça dégénère. Je veux pas qu'on se retrouve coincés.", "sd_d9_tenir_position"),
            ],
        },
    }



# Reutilise le meme habillage que le menu de choix natif (screens.rpy).
# Les conditions de statistiques ne changent que l'accessibilite des options.
screen stat_dialogue_choice(dialogue):
    modal True
    zorder 110

    on "show" action Function(minor_choice_suspend_original)
    on "hide" action Function(minor_choice_restore_original)
    on "replaced" action Function(minor_choice_restore_original)

    fixed:
        at minor_choice_screen_fade
        add Solid("#050913b8", xsize=1920, ysize=1080) xpos 0 ypos 0
        add "gui/choice_v6/portrait_shadow.svg" xpos 1218 ypos 229

        fixed:
            xpos 1285
            ypos 139
            xsize 635
            ysize 941
            at minor_choice_face_enter
            add minor_choice_face() xpos 0 ypos 0 at minor_choice_face_idle

        $ stat_count = len(dialogue["options"])
        $ stat_visible = min(max(stat_count, 1), 5)
        $ stat_top = {1: 687, 2: 595, 3: 502, 4: 395, 5: 290}[stat_visible]

        viewport:
            xpos 401
            ypos stat_top
            xsize 1160
            ysize min(145 * stat_count + 20, 778)
            mousewheel True
            draggable True
            vbox:
                spacing 7
                for idx, option in enumerate(dialogue["options"]):
                    $ unlocked = stat_choice_unlocked(option)
                    $ caption = option["text"] if unlocked else "VERROUILLÉ   —   ? ? ?"
                    $ stat_width = minor_choice_width(idx, caption)
                    $ stat_height = minor_choice_height(caption)
                    fixed:
                        xsize 1130
                        ysize stat_height + 10
                        xoffset MINOR_CHOICE_OFFSETS[idx % 4]
                        at minor_choice_enter(0.07 + idx * 0.055)
                        textbutton caption:
                            action Return(option["id"])
                            sensitive unlocked
                            style "choice_button"
                            xsize stat_width
                            ysize stat_height
                            padding (47, 22, 130, 17)
                            background minor_choice_image(idx, False, stat_width, stat_height)
                            hover_background minor_choice_image(idx, True, stat_width, stat_height)
                            insensitive_background minor_choice_image(idx, False, stat_width, stat_height)
                            text_style "choice_button_text"
                            text_size minor_choice_font_size(caption)
                            at minor_choice_hover(MINOR_CHOICE_TILTS[idx % 4])

label play_stat_dialogue(dialogue_id):
    $ _stat_dialogue = STAT_DIALOGUES[dialogue_id]
    call screen stat_dialogue_choice(_stat_dialogue)
    $ _stat_choice_id = _return
    $ _stat_option = stat_dialogue_option(_stat_dialogue, _stat_choice_id)
    $ _stat_choice_text = _stat_option["text"]
    noam "[_stat_choice_text]"
    $ _stat_xp_results = []
    call expression _stat_option["target"] from _call_expression_6
    $ notify_stat_level_ups(_stat_xp_results)
    return


# =============================================================
# LABELS DES RÉPONSES
# Le prérequis est déclaré dans STAT_DIALOGUES. Le gain exact est écrit ici.
# Les réponses ordinaires donnent de l'XP ; les réponses conditionnelles n'en donnent jamais.
# =============================================================

# JOUR 1 — toujours disponible. Gain : +1 XP Observation.
label sd_d1_prudent:
    lysa "Enfin une réponse raisonnable. Garde les yeux ouverts."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# JOUR 1 — toujours disponible. Gain : +1 XP Empathie.
label sd_d1_solidaire:
    lysa "C'est naïf... mais je préfère encore ça à la panique."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 1 — existe si Observation >= 2. Aucune XP.
label sd_d1_details:
    "Lysa se fige, surprise que j'aie remarqué, puis détourne les yeux."
    lysa gene "Rien... On a beau dire ce qu'on veut, cette situation fait franchement flipper..."
    return


# JOUR 2 — toujours disponible. Gain : +1 XP Empathie.
label sd_d2_ecouter:
    tomas "Les raisons comptent parfois plus que les positions."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 2 — toujours disponible. Gain : +1 XP Logique.
label sd_d2_texte:
    tomas "Bonne méthode. Un seul mot peut devenir une arme."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return


# JOUR 2 — existe si Audace >= 2. Aucune XP.
label sd_d2_frontal:
    "Tomas grimace, puis cède."
    tomas "Brutal... mais au moins ce sera clair."
    return

# JOUR 3 — toujours disponible. Gain : +1 XP Logique.
label sd_d3_coalition:
    julian "Du consensus avant du spectacle. Tu es terriblement raisonnable."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 3 — toujours disponible. Gain : +1 XP Audace.
label sd_d3_pression:
    "Julian sourit."
    julian "Voilà un argument qui a des dents."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return


# JOUR 3 — existe si Empathie >= 2. Aucune XP.
label sd_d3_peur:
    "Le sourire de Julian disparaît."
    julian "D'accord. Parlons à la personne, pas au vote."
    return

# JOUR 4, route refus — toujours disponible. Gain : +1 XP Logique.
label sd_d4_0_tenir:
    ryn "Comprendre ne réparera rien, mais ça évitera peut-être de recommencer."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 4, route refus — toujours disponible. Gain : +1 XP Audace.
label sd_d4_0_relancer:
    "Ryn laisse échapper un rire sec."
    ryn "Au moins, tu ne lâches pas."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return



# JOUR 4, route adoption — toujours disponible. Gain : +1 XP Logique.
label sd_d4_1_consequences:
    sael "Au moins, vous ne confondez pas changement et progrès."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 4, route adoption — toujours disponible. Gain : +1 XP Empathie.
label sd_d4_1_humains:
    "Sael serre la mâchoire."
    sael "Et vous voulez déjà ouvrir une autre brèche."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return


# JOUR 4, route adoption — existe si Sang-froid >= 2. Aucune XP.
label sd_d4_1_calme:
    "Sael hésite, déstabilisée par l'absence d'attaque."
    sael "Très bien. Une fois."
    return

# JOUR 5, route refus — toujours disponible. Gain : +1 XP Empathie.
label sd_d5_0_raison:
    sael "Vous supposez qu'il existe une différence. C'est déjà mieux que les autres."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 5, route refus — toujours disponible. Gain : +1 XP Logique.
label sd_d5_0_limite:
    sael "Toujours ? Votre certitude finira par vous coûter cher."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 5, route refus — existe si Observation >= 3. Aucune XP.
label sd_d5_0_micro:
    "Sael raidit les épaules."
    sael "Vous observez des choses qui ne vous concernent pas."
    return


# JOUR 5, route adoption — toujours disponible. Gain : +1 XP Sang-froid.
label sd_d5_1_present:
    "Kael suit mon rythme, difficilement, mais ses mains cessent de trembler."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR 5, route adoption — toujours disponible. Gain : +1 XP Audace.
label sd_d5_1_agir:
    kael "Même si Kami nous bloque ?"
    noam "Même là."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR 5, route adoption — existe si Logique >= 3. Aucune XP.
label sd_d5_1_alerte:
    "Kael relève la tête."
    kael "Donc certaines zones peuvent encore tenir."
    return


# JOUR 6, route 0-1 — toujours disponible. Gain : +1 XP Logique.
label sd_d6_0_1_procedure:
    mara "Une ligne commune. Bien. Je peux tenir là-dessus."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 6, route 0-1 — toujours disponible. Gain : +1 XP Empathie.
label sd_d6_0_1_ensemble:
    "Mara hoche la tête."
    mara "Ça, je peux le promettre."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return


# JOUR 6, route 0-1 — existe si Audace >= 3. Aucune XP.
label sd_d6_0_1_refus:
    mara "Tu vas attirer tout le feu."
    noam "C'est précisément l'idée."
    return

# JOUR 6, route 1-0 — toujours disponible. Gain : +1 XP Logique.
label sd_d6_1_0_trace:
    lysa "Penser à long terme dans cet endroit... il fallait oser."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 6, route 1-0 — toujours disponible. Gain : +1 XP Empathie.
label sd_d6_1_0_sael:
    "Lysa me scrute, puis acquiesce."
    lysa "Alors parle-lui comme à une personne."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 6, route 1-0 — existe si Observation >= 3. Aucune XP.
label sd_d6_1_0_hesitation:
    lysa "J'avais pris ça pour du mépris. Tu as peut-être raison."
    return


# JOUR 7, route 0-1 — toujours disponible. Gain : +1 XP Logique.
label sd_d7_0_1_verifier:
    tomas "Merci. J'avais besoin que quelqu'un dise ça."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 7, route 0-1 — toujours disponible. Gain : +1 XP Empathie.
label sd_d7_0_1_espoir:
    "Les épaules de Tomas retombent un peu."
    tomas "Oui. Commençons par ça."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 7, route 0-1 — existe si Logique >= 3. Aucune XP.
label sd_d7_0_1_motif:
    "Tomas blêmit."
    tomas "Ce n'est donc probablement pas un choix politique."
    return


# JOUR 7, route 1-0 — toujours disponible. Gain : +1 XP Sang-froid.
label sd_d7_1_0_soins:
    iris "D'accord. Une priorité à la fois."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 7, route 1-0 — toujours disponible. Gain : +1 XP Audace.
label sd_d7_1_0_cacher:
    "Iris saisit déjà une couverture."
    iris "C'est la réponse que j'espérais."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR 7, route 1-0 — existe si Observation >= 3. Aucune XP.
label sd_d7_1_0_symptomes:
    "Iris cesse de discuter."
    iris "Alors guide-nous."
    return

# JOUR 7, route 1-0 — existe si Empathie >= 3. Aucune XP.
label sd_d7_1_0_peur:
    "Iris vacille."
    iris "Plus tard. Sauve-la d'abord."
    return

# JOUR 7, route déclaration — toujours disponible. Gain : +1 XP Logique.
label sd_d7_1_0_1_medical:
    nyra "Des faits précis. Aucun espace pour son théâtre."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 7, route déclaration — toujours disponible. Gain : +1 XP Audace.
label sd_d7_1_0_1_responsable:
    "Nyra refuse d'abord, puis comprend."
    nyra "Alors nous restons derrière toi."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return


# JOUR 7, route déclaration — existe si Sang-froid >= 3. Aucune XP.
label sd_d7_1_0_1_unite:
    nyra "Nous avons trouvé. Nous demandons. Nous refusons. Compris."
    return

# JOUR 8 — toujours disponible. Gain : +1 XP Empathie.
label sd_d8_promesse:
    "Kael ferme les yeux."
    kael "C'est mieux qu'un mensonge."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 8 — toujours disponible. Gain : +1 XP Logique.
label sd_d8_indices:
    kael "Une enquête. Oui. Quelque chose de concret."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 8 — existe si Logique >= 3. Aucune XP.
label sd_d8_cible:
    "Kael pâlit."
    kael "Donc le voleur ne prend pas des objets. Il prend nos attaches."
    return


# JOUR 9 — toujours disponible. Gain : +1 XP Logique.
label sd_d9_temps:
    ryn "Obéir en apparence. Ça me plaît moins que ça ne devrait."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR 9 — toujours disponible. Gain : +1 XP Empathie.
label sd_d9_prevenir:
    "Ryn tend déjà la main vers la console."
    ryn "Enfin une phrase utile."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return


# JOUR 9 — existe si Sang-froid >= 3. Aucune XP.
label sd_d9_provoquer:
    "Ryn sourit sans joie."
    ryn "Tiens assez longtemps et je fais le reste."
    return

# JOUR d1 — nouvelle réponse ordinaire : +1 XP physique.
label sd_d1_souffler:
    lysa "Si tu comptes t'effondrer dès le premier jour, préviens-moi. J'ai pas envie de te porter."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

# JOUR d2 — nouvelle réponse ordinaire : +1 XP observation.
label sd_d2_observer:
    tomas "C'est une bonne piste. Les places autour de cette table ne doivent pas toutes être le fruit du hasard."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# JOUR d3 — nouvelle réponse ordinaire : +1 XP sang_froid.
label sd_d3_garder_tete:
    julian "Pas très spectaculaire, mais je reconnais que ça pourrait nous éviter un désastre."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR d4_0 — nouvelle réponse ordinaire : +1 XP sang_froid.
label sd_d4_0_rester_calme:
    ryn "Ouais, bon. J'ai pas dit que j'allais cogner quelqu'un. Enfin, pas encore."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR d4_1 — nouvelle réponse ordinaire : +1 XP observation.
label sd_d4_1_regarder:
    sael "Au moins, vous admettez qu'un vote ne règle pas tout. C'est déjà cela."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# JOUR d5_0 — nouvelle réponse ordinaire : +1 XP audace.
label sd_d5_0_tenir_bon:
    sael "Vous avez de la suite dans les idées. C'est parfois un défaut, vous savez."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR d5_1 — nouvelle réponse ordinaire : +1 XP physique.
label sd_d5_1_soutenir:
    kael "Merci. Mais attends qu'on sache au moins où aller, d'accord ?"
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

# JOUR d6_0_1 — nouvelle réponse ordinaire : +1 XP observation.
label sd_d6_0_1_reperer:
    mara "Charmant. Même la salle du vote me donne envie de chercher une sortie de secours, maintenant."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# JOUR d6_1_0 — nouvelle réponse ordinaire : +1 XP audace.
label sd_d6_1_0_oser:
    lysa "Ça va être pénible à regarder... mais au moins, on saura ce qu'elle répond."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR d7_0_1 — nouvelle réponse ordinaire : +1 XP audace.
label sd_d7_0_1_se_risquer:
    tomas "Je préférerais vérifier deux fois... Mais je comprends pourquoi tu ne veux pas attendre."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR d7_1_0 — nouvelle réponse ordinaire : +1 XP physique.
label sd_d7_1_0_porter:
    iris "Tu la soulèves doucement, compris ? Si tu la secoues, je te fais regretter de m'avoir proposé ton aide."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return

# JOUR d7_1_0_1 — nouvelle réponse ordinaire : +1 XP sang_froid.
label sd_d7_1_0_1_tenir_calme:
    nyra "C'est la seule façon d'avoir une conversation utile avec elle. Ne sortons pas de ce cadre."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR d8 — nouvelle réponse ordinaire : +1 XP sang_froid.
label sd_d8_garder_calme:
    kael "D'accord. Je vais essayer. J'ai juste besoin qu'on ne laisse pas tomber."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
    return

# JOUR d9 — nouvelle réponse ordinaire : +1 XP physique.
label sd_d9_tenir_position:
    ryn "Là, au moins, on parle concret. Je vais vérifier le couloir."
    $ _stat_xp_results = award_stats_xp({"physique": 1})
    return
