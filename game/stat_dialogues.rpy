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

    # Chaque échange contient quatre réponses, dont deux verrouillées par les
    # statistiques. Les variantes couvrent tous les points d'entrée jouables.
    STAT_DIALOGUES = {
        "d1": {
            "prompt": "Lysa baisse la voix. « Tu crois qu'on peut vraiment se faire confiance ici ? »",
            "options": [
                _sd_option("prudent", "Franchement, j'en sais rien. On vient à peine d'arriver et j'ai déjà l'impression que tout le monde se méfie de tout le monde.", "sd_d1_prudent"),
                _sd_option("solidaire", "Je dis pas qu'on doit se faire confiance les yeux fermés. Mais on peut au moins essayer de s'entraider, non ?", "sd_d1_solidaire"),
                _sd_option("details", "Lysa, je t'ai vue trembler tout à l'heure. Tu vas pas me dire que tout va bien ?", "sd_d1_details", requires={"observation": 2}),
                _sd_option("rassurer", "Tu sais, t'es pas obligée de faire comme si tout ça te passait au-dessus. Pas avec moi, en tout cas.", "sd_d1_rassurer", requires={"empathie": 2}),
            ],
        },
        "d2": {
            "prompt": "Tomas regarde les autres tables. « Comment tu veux aborder ce premier vote ? »",
            "options": [
                _sd_option("ecouter", "Avant de défendre quoi que ce soit, je veux comprendre ce que chacun risque de perdre avec ce vote.", "sd_d2_ecouter"),
                _sd_option("texte", "Je vais déjà relire la proposition mot par mot. Si on se trompe sur ce qu'on vote, on est mal partis.", "sd_d2_texte"),
                _sd_option("signaux", "Tu vois ceux qui changent de sujet dès qu'on parle du vote ? Je commencerais par aller leur parler.", "sd_d2_signaux", requires={"observation": 2}),
                _sd_option("frontal", "Ça suffit de tourner autour du pot. Je vais leur demander directement ce qu'ils comptent voter.", "sd_d2_frontal", requires={"audace": 2}),
            ],
        },
        "d3": {
            "prompt": "Julian croise les bras. « Une voix peut tout faire échouer. Tu proposes quoi ? »",
            "options": [
                _sd_option("coalition", "On devrait commencer par chercher ce sur quoi tout le monde est d'accord. Après, on verra ce qui bloque.", "sd_d3_coalition"),
                _sd_option("pression", "S'ils veulent voter contre, très bien. Mais je veux qu'ils regardent aussi les conséquences de ce refus.", "sd_d3_pression"),
                _sd_option("contradiction", "Attends. Si on reprend leurs arguments un par un, il y a plusieurs choses qui ne collent pas. On peut partir de là.", "sd_d3_contradiction", requires={"logique": 2}),
                _sd_option("peur", "Et si on leur demandait d'abord ce qui leur fait peur ? À mon avis, certains ne disent pas vraiment pourquoi ils hésitent.", "sd_d3_peur", requires={"empathie": 2}),
            ],
        },
        "d4_0": {
            "prompt": "Ryn frappe la table. « On a perdu hier. Tu comptes encore demander gentiment ? »",
            "options": [
                _sd_option("tenir", "Je compte surtout comprendre pourquoi on a perdu.", "sd_d4_0_tenir"),
                _sd_option("relancer", "Oui. Jusqu'à ce qu'ils soient obligés de répondre.", "sd_d4_0_relancer"),
                _sd_option("colere", "Ryn, je vois bien que t'es en colère. Mais ce vote t'a aussi fait peur, non ? Qu'est-ce qui te travaille autant ?", "sd_d4_0_colere", requires={"empathie": 2}),
                _sd_option("faille", "Ils ont tous voté contre, mais pas pour les mêmes raisons. Si on comprend ce qui a bloqué chacun, on aura peut-être une chance.", "sd_d4_0_faille", requires={"logique": 2}),
            ],
        },
        "d4_1": {
            "prompt": "Sael me dévisage. « Vous avez gagné le commerce. Cela vous suffit-il ? »",
            "options": [
                _sd_option("consequences", "Une victoire ne vaut rien si on refuse d'en surveiller les conséquences.", "sd_d4_1_consequences"),
                _sd_option("humains", "Non. Les marchandises passent, les gens restent enfermés.", "sd_d4_1_humains"),
                _sd_option("interet", "Sael, j'ai l'impression que vous ne refusez pas ce vote par principe. Vous essayez de protéger quelqu'un, c'est ça ?", "sd_d4_1_interet", requires={"observation": 2}),
                _sd_option("calme", "D'accord. Je ne vais pas essayer de vous convaincre tout de suite. Dites-moi seulement ce qui vous empêche d'accepter.", "sd_d4_1_calme", requires={"sang_froid": 2}),
            ],
        },
        "d5_0": {
            "prompt": "Sael soupire. « Vous savez déjà que je voterai non. Pourquoi insister ? »",
            "options": [
                _sd_option("raison", "Parce que je veux entendre votre raison, pas seulement votre vote.", "sd_d5_0_raison"),
                _sd_option("limite", "Parce qu'un refus absolu cache toujours une limite négociable.", "sd_d5_0_limite"),
                _sd_option("micro", "Chaque fois qu'on parle des frontières, vous vous arrêtez au milieu de vos phrases. Il y a quelque chose que vous ne nous dites pas ?", "sd_d5_0_micro", requires={"observation": 3}),
                _sd_option("silence", "On n'est pas obligés de régler ça maintenant. Je peux attendre un peu, si vous avez besoin de réfléchir.", "sd_d5_0_silence", requires={"sang_froid": 2}),
            ],
        },
        "d5_1": {
            "prompt": "Kael fixe l'écran éteint. « Si ma sœur est à C-3, je dois faire quoi ? »",
            "options": [
                _sd_option("present", "D'abord respirer. Ensuite, on rassemble ce qu'on sait vraiment.", "sd_d5_1_present"),
                _sd_option("agir", "Me donner tout ce que tu sais. On trouvera un moyen d'agir.", "sd_d5_1_agir"),
                _sd_option("alerte", "L'alerte ne correspond pas à une rupture totale du complexe.", "sd_d5_1_alerte", requires={"logique": 3}),
                _sd_option("mensonge", "Tu ne me dis pas tout sur la situation de ta sœur.", "sd_d5_1_mensonge", requires={"observation": 2}),
            ],
        },
        "d6_0_1": {
            "prompt": "Mara observe la porte du Conclave. « On entre malgré le texte incompréhensible ? »",
            "options": [
                _sd_option("procedure", "On entre, mais personne ne vote avant une formulation claire.", "sd_d6_0_1_procedure"),
                _sd_option("ensemble", "On entre ensemble et personne ne reste isolé face à Kami.", "sd_d6_0_1_ensemble"),
                _sd_option("glitch", "Les coupures suivent un rythme. Kami ne contrôle pas tout.", "sd_d6_0_1_glitch", requires={"observation": 3}),
                _sd_option("refus", "Si elle nous presse, je prends la parole et je refuse le cadre.", "sd_d6_0_1_refus", requires={"audace": 3}),
            ],
        },
        "d6_1_0": {
            "prompt": "Lysa murmure. « Le vote est perdu d'avance. On joue quand même la scène ? »",
            "options": [
                _sd_option("trace", "Oui. Chaque argument laissera une trace pour le prochain vote.", "sd_d6_1_0_trace"),
                _sd_option("sael", "Oui. Sael doit voir qu'on ne la réduit pas à son non.", "sd_d6_1_0_sael"),
                _sd_option("hesitation", "Elle évite mon regard depuis ce matin. Sa décision n'est pas aussi solide qu'elle le dit.", "sd_d6_1_0_hesitation", requires={"observation": 3}),
                _sd_option("rupture", "On brise le rythme de Kami et on impose notre propre question.", "sd_d6_1_0_rupture", requires={"audace": 3}),
            ],
        },
        "d7_0_1": {
            "prompt": "Tomas tient son rapport contre lui. « Plus aucune exécution. Tu comprends ce que ça signifie ? »",
            "options": [
                _sd_option("verifier", "Que nous devons vérifier avant d'inventer une explication.", "sd_d7_0_1_verifier"),
                _sd_option("espoir", "Que des gens sont vivants aujourd'hui grâce à cette anomalie.", "sd_d7_0_1_espoir"),
                _sd_option("motif", "Le silence de Kami et l'arrêt des exécutions ont commencé ensemble.", "sd_d7_0_1_motif", requires={"logique": 3}),
                _sd_option("publier", "On l'annonce à tout le monde avant que Kami puisse réécrire les faits.", "sd_d7_0_1_publier", requires={"audace": 3}),
            ],
        },
        "d7_1_0": {
            "prompt": "Iris bloque la porte. « On cache cette femme ou on prévient Kami ? »",
            "options": [
                _sd_option("soins", "On commence par ce qui la maintient en vie, puis on décide.", "sd_d7_1_0_soins"),
                _sd_option("cacher", "On la cache. Kami n'a aucun droit sur elle.", "sd_d7_1_0_cacher"),
                _sd_option("symptomes", "Sa respiration indique qu'on n'a que quelques minutes pour la déplacer.", "sd_d7_1_0_symptomes", requires={"observation": 3}),
                _sd_option("peur", "Tu veux la cacher parce qu'elle te rappelle quelqu'un.", "sd_d7_1_0_peur", requires={"empathie": 3}),
            ],
        },
        "d7_1_0_1": {
            "prompt": "Nyra fixe la caméra. « Si nous appelons Kami, il faut contrôler les premiers mots. »",
            "options": [
                _sd_option("medical", "On décrit uniquement l'urgence médicale et on exige des soins.", "sd_d7_1_0_1_medical"),
                _sd_option("responsable", "Je parle le premier et j'assume la découverte.", "sd_d7_1_0_1_responsable"),
                _sd_option("camera", "La caméra a changé d'angle avant notre arrivée. Kami savait déjà.", "sd_d7_1_0_1_camera", requires={"observation": 3}),
                _sd_option("unite", "On parle au pluriel. Elle ne doit pouvoir isoler personne.", "sd_d7_1_0_1_unite", requires={"sang_froid": 3}),
            ],
        },
        "d8": {
            "prompt": "Kael serre sa photo disparue contre son souvenir. « Dis-moi que ce n'est pas quelqu'un d'ici. »",
            "options": [
                _sd_option("promesse", "Je ne peux pas te le promettre. Mais je peux t'aider à chercher.", "sd_d8_promesse"),
                _sd_option("indices", "On reconstitue les accès, les horaires et les objets visés.", "sd_d8_indices"),
                _sd_option("cible", "Le dessin et la photo ont la même fonction : nous rappeler quelqu'un.", "sd_d8_cible", requires={"logique": 3}),
                _sd_option("confronter", "Je vais réunir tout le monde. On a assez perdu de temps à se demander ce qui se passe chacun dans notre coin.", "sd_d8_confronter", requires={"audace": 3}),
            ],
        },
        "d9": {
            "prompt": "Ryn regarde les écrans. « Kami est revenue. On suit encore sa procédure ? »",
            "options": [
                _sd_option("temps", "On suit assez longtemps pour gagner du temps aux campements.", "sd_d9_temps"),
                _sd_option("prevenir", "La priorité est de prévenir les gens, quel qu'en soit le prix.", "sd_d9_prevenir"),
                _sd_option("maintenance", "Sa maintenance a laissé des irrégularités dans le réseau. C'est notre passage.", "sd_d9_maintenance", requires={"observation": 3}),
                _sd_option("provoquer", "Je la provoque à l'écran pendant que vous détournez le signal.", "sd_d9_provoquer", requires={"sang_froid": 3}),
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

# JOUR 1 — existe si Empathie >= 2. Aucune XP.
label sd_d1_rassurer:
    "Son expression se fissure une seconde."
    lysa "Facile à dire. Tu as plus peur que moi."
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

# JOUR 2 — existe si Observation >= 2. Aucune XP.
label sd_d2_signaux:
    "Le regard de Tomas suit le mien."
    tomas "Je n'avais pas vu ce manège."
    return

# JOUR 2 — existe si Audace >= 2. Aucune XP.
label sd_d2_frontal:
    "Tomas grimace, puis cède."
    tomas "Brutal... mais au moins ce sera clair."
    return

# JOUR 3 — toujours disponible. Gain : +1 XP Logique.
label sd_d3_coalition:
    julian "Du consensus avant du spectacle. Tu es terriblement raisonnable."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 3 — toujours disponible. Gain : +1 XP Audace.
label sd_d3_pression:
    "Julian sourit."
    julian "Voilà un argument qui a des dents."
    $ _stat_xp_results = award_stats_xp({"audace": 1})
    return

# JOUR 3 — existe si Logique >= 2. Aucune XP.
label sd_d3_contradiction:
    julian "Chirurgical. J'aime beaucoup quand tu deviens inquiétant."
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

# JOUR 4, route refus — existe si Empathie >= 2. Aucune XP.
label sd_d4_0_colere:
    "Ryn ouvre la bouche pour m'envoyer promener, puis renonce."
    ryn "Que rien ne change jamais."
    return

# JOUR 4, route refus — existe si Logique >= 2. Aucune XP.
label sd_d4_0_faille:
    "Ryn se penche vers moi."
    ryn "Alors on sépare leurs alliances."
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

# JOUR 4, route adoption — existe si Observation >= 2. Aucune XP.
label sd_d4_1_interet:
    "Le silence de Sael confirme que j'ai touché juste, sans me dire qui."
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

# JOUR 5, route refus — existe si Sang-froid >= 2. Aucune XP.
label sd_d5_0_silence:
    "Le duel dure longtemps. C'est Sael qui parle la première."
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

# JOUR 5, route adoption — existe si Observation >= 2. Aucune XP.
label sd_d5_1_mensonge:
    "Kael baisse les yeux."
    kael "Elle n'était pas censée être dans cette section."
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

# JOUR 6, route 0-1 — existe si Observation >= 3. Aucune XP.
label sd_d6_0_1_glitch:
    "Mara écoute le bourdonnement."
    mara "Alors on utilise ses fenêtres de faiblesse."
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

# JOUR 6, route 1-0 — existe si Audace >= 3. Aucune XP.
label sd_d6_1_0_rupture:
    "Le sourire de Lysa est bref."
    lysa "Là, je te reconnais."
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

# JOUR 7, route 0-1 — existe si Audace >= 3. Aucune XP.
label sd_d7_0_1_publier:
    tomas "C'est dangereux."
    noam "Le silence le serait davantage."
    return

# JOUR 7, route 1-0 — toujours disponible. Gain : +1 XP Sang-froid.
label sd_d7_1_0_soins:
    iris "D'accord. Une priorité à la fois."
    $ _stat_xp_results = award_stats_xp({"sang_froid": 1})
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

# JOUR 7, route déclaration — existe si Observation >= 3. Aucune XP.
label sd_d7_1_0_1_camera:
    "Nyra lève les yeux."
    nyra "Alors cet appel est une mise en scène."
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

# JOUR 8 — existe si Audace >= 3. Aucune XP.
label sd_d8_confronter:
    kael "Ils vont te détester."
    noam "Qu'ils commencent par répondre."
    return

# JOUR 9 — toujours disponible. Gain : +1 XP Logique.
label sd_d9_temps:
    ryn "Obéir en apparence. Ça me plaît moins que ça ne devrait."
    $ _stat_xp_results = award_stats_xp({"logique": 1})
    return

# JOUR 9 — toujours disponible. Gain : +1 XP Empathie.
label sd_d9_prevenir:
    "Ryn tend déjà la main vers la console."
    ryn "Enfin une phrase utile."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 9 — existe si Observation >= 3. Aucune XP.
label sd_d9_maintenance:
    ryn "Tu peux les trouver ?"
    noam "Donne-moi une minute."
    return

# JOUR 9 — existe si Sang-froid >= 3. Aucune XP.
label sd_d9_provoquer:
    "Ryn sourit sans joie."
    ryn "Tiens assez longtemps et je fais le reste."
    return
