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
            "prompt": "Lysa baisse la voix. « Tu crois qu'on peut leur faire confiance ? »",
            "options": [
                _sd_option("prudent", "J'en sais rien. On les connaît pas, et eux non plus. Je préfère rester prudent.", "sd_d1_prudent"),
                _sd_option("solidaire", "On n'est pas obligés de leur faire confiance tout de suite. Mais on peut essayer de se parler, non ?", "sd_d1_solidaire"),
                _sd_option("details", "Je sais pas pour eux... Mais toi, ça va ? Je t'ai vue trembler tout à l'heure.", "sd_d1_details", requires={"observation": 2}),
                _sd_option("souffler", "Là, j'ai encore les jambes en coton. On pourra parler confiance quand j'arriverai à tenir debout.", "sd_d1_souffler"),
            ],
        },
        "d2": {
            "prompt": "Tomas regarde les autres tables. « Comment tu veux aborder ce premier vote ? »",
            "options": [
                _sd_option("ecouter", "Avant de me faire un avis, je veux surtout savoir ce que les autres pensent de cette proposition.", "sd_d2_ecouter"),
                _sd_option("texte", "Attends, je vais déjà ouvrir le dossier sur ma tablette. On n'a même pas lu la formulation exacte.", "sd_d2_texte"),
                _sd_option("frontal", "On va leur demander franchement s'ils comptent voter pour. Autant savoir à quoi s'en tenir.", "sd_d2_frontal", requires={"audace": 2}),
                _sd_option("observer", "Tout le monde a reçu le dossier en même temps. Je vais voir qui réagit en premier.", "sd_d2_observer"),
            ],
        },
        "d3": {
            "prompt": "Julian croise les bras. « Une voix peut tout faire échouer. Tu proposes quoi ? »",
            "options": [
                _sd_option("coalition", "Bon, avant que ça commence, il faudrait savoir sur quoi on est tous d'accord.", "sd_d3_coalition"),
                _sd_option("pression", "On est enfermés ici jusqu'à la décision... Ça met sacrément la pression pour un premier vote.", "sd_d3_pression"),
                _sd_option("peur", "Je me demande surtout qui a peur de voter contre. Ça peut changer toutes les discussions.", "sd_d3_peur", requires={"empathie": 2}),
                _sd_option("garder_tete", "On est enfermés, d'accord, mais ça sert à rien de paniquer. On va essayer de garder la tête froide.", "sd_d3_garder_tete"),
            ],
        },
        "d4_0": {
            "prompt": "Ryn frappe la table. « On a perdu hier. Tu comptes encore demander gentiment ? »",
            "options": [
                _sd_option("tenir", "J'arrête pas de repenser au vote. On doit comprendre ce qui a coincé.", "sd_d4_0_tenir"),
                _sd_option("relancer", "On peut pas laisser cette journée se passer comme si rien n'avait changé.", "sd_d4_0_relancer"),
                _sd_option("rester_calme", "Je suis en colère, mais ça sert à rien de s'en prendre aux autres.", "sd_d4_0_rester_calme"),
            ],
        },
        "d4_1": {
            "prompt": "Sael me dévisage. « Vous avez gagné le commerce. Cela vous suffit-il ? »",
            "options": [
                _sd_option("consequences", "On a voté pour, mais voir des gens repartir les mains vides... Je pensais pas que ce serait aussi rapide.", "sd_d4_1_consequences"),
                _sd_option("humains", "Ça me fait penser aux gens qui sont déjà coincés à Limen. On les aide pas beaucoup avec ça.", "sd_d4_1_humains"),
                _sd_option("calme", "Sael, je comprends que ça t'inquiète. Mais tu crois qu'on aurait pu éviter ça autrement ?", "sd_d4_1_calme", requires={"sang_froid": 2}),
                _sd_option("regarder", "Il faudrait comparer ce qui se passe dans les autres districts. Peut-être qu'ailleurs, ça marche mieux.", "sd_d4_1_regarder"),
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
                _sd_option("present", "Kael, tu pouvais pas prévoir cette alerte. Te reprocher d'avoir dormi va rien changer.", "sd_d5_1_present"),
                _sd_option("agir", "Montre-moi l'alerte. On va regarder ce qu'elle dit exactement.", "sd_d5_1_agir"),
                _sd_option("alerte", "Attends, le message parle d'une alerte, pas de la destruction de toute la zone.", "sd_d5_1_alerte", requires={"logique": 3}),
                _sd_option("soutenir", "Si tu as besoin d'aide pour vérifier les relevés, je suis là.", "sd_d5_1_soutenir"),
            ],
        },
        "d6_0_1": {
            "prompt": "Mara observe la porte du Conclave. « On entre malgré le texte incompréhensible ? »",
            "options": [
                _sd_option("procedure", "On devrait tous demander une explication du texte avant de voter. Là, personne n'a l'air de comprendre.", "sd_d6_0_1_procedure"),
                _sd_option("ensemble", "On est tous là, mais chacun reste dans son coin. On devrait essayer de parler ensemble avant le vote.", "sd_d6_0_1_ensemble"),
                _sd_option("refus", "Si Kami essaie de nous faire voter sans expliquer le texte, je compte bien lui dire non.", "sd_d6_0_1_refus", requires={"audace": 3}),
                _sd_option("reperer", "Tout le monde regarde les autres au lieu de parler. On dirait que chacun attend de voir qui va craquer.", "sd_d6_0_1_reperer"),
            ],
        },
        "d6_1_0": {
            "prompt": "Lysa murmure. « Le vote est perdu d'avance. On joue quand même la scène ? »",
            "options": [
                _sd_option("trace", "Sael a annoncé qu'elle voterait contre. Il faut quand même écouter les autres aujourd'hui.", "sd_d6_1_0_trace"),
                _sd_option("sael", "Sael a ses raisons. Je veux pas que tout le monde lui tombe dessus à cause de son vote.", "sd_d6_1_0_sael"),
                _sd_option("hesitation", "Depuis hier, Sael évite tout le monde. Je crois que ça lui coûte plus qu'elle veut le montrer.", "sd_d6_1_0_hesitation", requires={"observation": 3}),
                _sd_option("oser", "Même si le vote est perdu, je vais pas rester assis à regarder les autres faire.", "sd_d6_1_0_oser"),
            ],
        },
        "d7_0_1": {
            "prompt": "Tomas tient son rapport contre lui. « Plus aucune exécution. Tu comprends ce que ça signifie ? »",
            "options": [
                _sd_option("verifier", "Attends, zéro exécution depuis hier ? Tu es sûr que tes chiffres sont bons ?", "sd_d7_0_1_verifier"),
                _sd_option("espoir", "Ça veut dire que personne n'a été exécuté depuis hier ? C'est énorme, Tomas !", "sd_d7_0_1_espoir"),
                _sd_option("motif", "Le silence de Kami et l'arrêt des exécutions ont commencé au même moment. C'est pas une coïncidence.", "sd_d7_0_1_motif", requires={"logique": 3}),
                _sd_option("se_risquer", "Il faut le dire aux autres. Ça fait peut-être une journée entière sans exécution !", "sd_d7_0_1_se_risquer"),
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
                _sd_option("promesse", "Kael, je comprends pas non plus pourquoi quelqu'un nous ferait ça. Mais on va chercher.", "sd_d8_promesse"),
                _sd_option("indices", "On sait qu'on nous a pris deux objets personnels. On peut peut-être retracer qui est passé dans les chambres.", "sd_d8_indices"),
                _sd_option("cible", "La photo de Léa et mon dessin ont le même point commun : ce sont des souvenirs de nos proches.", "sd_d8_cible", requires={"logique": 3}),
                _sd_option("garder_calme", "Je veux pas qu'on accuse quelqu'un sans preuve. Ça nous aidera pas à retrouver nos affaires.", "sd_d8_garder_calme"),
            ],
        },
        "d9": {
            "prompt": "Ryn regarde les écrans. « Kami est revenue. On suit encore sa procédure ? »",
            "options": [
                _sd_option("temps", "Ryn, je veux éviter le pire, moi aussi. On doit trouver comment obtenir l'unanimité.", "sd_d9_temps"),
                _sd_option("prevenir", "Je comprends que tu sois furieux. Mais si on se menace entre nous, on risque de faire échouer le vote.", "sd_d9_prevenir"),
                _sd_option("provoquer", "Si Kami cherche à nous piéger pendant le vote, je suis prêt à lui répondre devant tout le monde.", "sd_d9_provoquer", requires={"sang_froid": 3}),
                _sd_option("tenir_position", "On a besoin que tout le monde garde son calme, même si on est terrifiés.", "sd_d9_tenir_position"),
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
    lysa blase "Ouais. Pour une fois, on est d'accord. On va éviter de se précipiter."
    $ _stat_xp_results = award_stats_xp({"observation": 1})
    return

# JOUR 1 — toujours disponible. Gain : +1 XP Empathie.
label sd_d1_solidaire:
    lysa taquin "Tu veux déjà te faire des copains ? Bon... c'est toujours mieux que de se regarder de travers."
    $ _stat_xp_results = award_stats_xp({"empathie": 1})
    return

# JOUR 1 — existe si Observation >= 2. Aucune XP.
label sd_d1_details:
    "Lysa glisse ses mains sous la table."
    lysa blase "Quoi ? J'ai froid. Ça arrive."
    noam "Tu regardes aussi la porte toutes les dix secondes."
    lysa blase "Je me réveille avec des inconnus, je sais même pas où on est... Tu veux que je sois détendue ?"
    noam "Non. Je voulais juste savoir si ça allait."
    lysa inquiet "Bah non, pas vraiment. Mais évite d'en parler aux autres, d'accord ?"
    noam "D'accord. Je garde ça pour moi."
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
    tomas "Tu peux leur demander clairement, mais évite de les coincer devant tout le monde."
    noam "On vote bientôt. On peut pas passer la journée à deviner ce qu'ils pensent."
    tomas "Alors commence par leur demander ce qui les inquiète. Ensuite, tu demandes leur position."
    noam "Et s'ils répondent à côté ?"
    tomas "Tu insistes. Mais au moins tu leur auras laissé une chance de s'expliquer."
    noam "Bon. Je vais essayer comme ça."
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
    "Julian cesse de sourire."
    julian "Tu penses à quelqu'un en particulier ?"
    noam "À ceux qui ne disent presque rien. J'ai pas envie de leur prêter des intentions avant de les écouter."
    julian "Et moi qui pensais qu'on allait leur faire un grand discours..."
    noam "Tu pourrais aller voir deux ou trois personnes sans essayer de les impressionner ?"
    julian "Aïe. Tu demandes beaucoup. Mais je peux essayer."
    noam "Alors on se retrouve après et on compare ce qu'ils nous ont dit."
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
    sael "Vous pensez que je vais vous donner toutes mes raisons comme ça ?"
    noam "Non. Mais je peux au moins vous écouter jusqu'au bout."
    sael "Les échanges de marchandises, c'est une chose. Vous ne connaissez pas les gens qui devront vivre avec la suite."
    noam "Les habitants de Limen ?"
    sael "Entre autres. Ils ne sont pas tous aussi pressés que vous de voir les choses changer."
    noam "D'accord. Je ne vais pas décider à leur place de ce qui est bon pour eux."
    sael "Alors nous avons peut-être quelque chose à nous dire."
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
    "Sael s'interrompt encore et jette un œil vers la porte."
    sael "Qu'est-ce que vous insinuez ?"
    noam "Rien. Je remarque juste que vous regardez derrière moi chaque fois qu'on parle des frontières."
    sael "Je regarde où je veux."
    noam "D'accord. Mais si quelqu'un vous empêche de parler, je préfère le savoir."
    sael "Personne ne m'empêche de parler. Ce qui m'inquiète, ce sont ceux qui devront subir votre décision."
    noam "Alors parlons d'eux, plutôt que de revenir sur votre vote."
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
    kael "Attends... Tu veux dire que tout C-3 n'est pas forcément coupé ?"
    noam "L'alerte ne dit pas ça. Elle parle d'un problème localisé, pas d'une destruction totale."
    kael "Mais ma sœur pourrait quand même être dans la zone touchée."
    noam "Oui. Je veux pas te faire croire le contraire."
    kael "Alors qu'est-ce qu'on cherche ?"
    noam "Une information sur son secteur précis. Pour l'instant, on n'en sait pas assez."
    "Kael reprend l'écran et commence à chercher, un peu plus calmement."
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
    mara "Tu vas vraiment dire non devant tout le monde ?"
    noam "Si Kami veut qu'on vote sans comprendre le texte, oui."
    mara "Et si elle décide de s'en prendre à toi ?"
    noam "On sera pas plus en sécurité en acceptant n'importe quoi."
    mara "Peut-être, mais j'aimerais autant que tu sortes de là entier."
    noam "Alors reste à côté. Si je m'emballe, tu m'arrêtes."
    mara "Pas de souci. Ça, je sais faire."
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
    "Lysa observe discrètement Sael."
    lysa "Moi, je pensais qu'elle nous méprisait, c'est tout."
    noam "Elle regarde toujours les autres avant de répondre. Ça ressemble pas à quelqu'un de si sûr de son coup."
    lysa "Ou alors elle cherche juste la meilleure façon de nous envoyer balader."
    noam "Possible. Mais je préfère lui poser la question."
    lysa "Bonne chance. Évite quand même de lui dire que tu l'observes depuis une heure."
    noam "Oui, je vais trouver autre chose."
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
    tomas "Tu penses que les deux événements sont liés ?"
    noam "Ils ont commencé au même moment. Pour moi, ça mérite qu'on vérifie."
    tomas "Ça voudrait dire que Kami n'a peut-être pas choisi d'arrêter les exécutions..."
    noam "On sait pas encore. Et on sait surtout pas si ça va durer."
    tomas "Je vais relever les horaires exacts dans le rapport."
    noam "Et on évite de dire aux autres que le danger est passé."
    tomas "Oui. Ce serait une erreur."
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
    "Iris s'agenouille aussitôt près de la jeune femme."
    iris "Qu'est-ce que t'as remarqué ?"
    noam "Elle respire très vite, puis presque plus du tout pendant une seconde. Ça recommence."
    iris "Merde. Elias, viens voir ça."
    noam "Je fais quoi ?"
    iris "Tu tiens la couverture, tu évites de la secouer et tu fais ce que je te dis. On discutera du reste après."
    noam "Compris. Je bouge pas."
    return

# JOUR 7, route 1-0 — existe si Empathie >= 3. Aucune XP.
label sd_d7_1_0_peur:
    "Iris détourne le regard."
    iris "C'est pas le moment de parler de ça."
    noam "Je te demande pas de m'expliquer. Je voulais juste être sûr que t'allais bien."
    iris "Ben non, ça va pas. Maintenant, tu veux bien m'aider ?"
    noam "Bien sûr. Qu'est-ce qu'il te faut ?"
    iris "Une couverture. Et cinq minutes de tranquillité quand on aura fini."
    noam "Ça marche. Je t'en trouverai une."
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
    nyra "Oui. Personne ne répond seul si Kami cherche à désigner un coupable."
    noam "On explique ce qu'on a trouvé et ce qu'on demande. Pas besoin de se rejeter la faute."
    nyra "Et si elle menace celui qui prend la parole ?"
    noam "On revient aux faits : il y a une femme blessée, elle a besoin de soins."
    nyra "Très bien. Tu gardes cette version, même si elle essaie de te faire sortir de tes gonds."
    noam "Je vais faire de mon mieux."
    nyra "Il faudra faire mieux que ça. On va répéter une fois."
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
    kael "Tu crois que quelqu'un prend ces objets juste pour nous faire du mal ?"
    noam "Je sais pas. Mais la photo et le dessin ont un point commun : ils comptent pour nous. Ils valent pas grand-chose autrement."
    kael "Ça voudrait dire que la personne savait quoi chercher."
    noam "Ou qu'elle a pris le temps de regarder ce qu'on gardait."
    kael "C'est encore pire..."
    noam "On va vérifier les accès avant d'accuser qui que ce soit."
    kael "D'accord. Je peux t'aider pour ça."
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
    ryn "Tu vas discuter avec elle pendant que je touche à la console ?"
    noam "Si elle est occupée à me répondre, elle regardera peut-être moins ce que tu fais."
    ryn "Peut-être ? Super rassurant, ton plan."
    noam "Tu préfères qu'on reste plantés là ?"
    ryn "Non. Mais si elle se tourne vers moi, tu changes de sujet tout de suite."
    noam "D'accord. Et toi, tu prends pas de risques inutiles."
    ryn "Je te promets rien, mais j'ai compris."
    return

# JOUR d1 — nouvelle réponse ordinaire : +1 XP physique.
label sd_d1_souffler:
    lysa taquin "Si tu t'écroules, préviens-moi. J'ai pas très envie de te porter."
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
