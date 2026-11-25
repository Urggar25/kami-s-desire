label _11_0_1_1_REVEIL_CHAMBRE:
    $ cafeteria_food_level = "low"
    $ current_period = "Matin"
    $ current_day = 11
    $ noam_has_juliette_drawing = False
    scene black
    play music "music/bgm_fallin_love.mp3" fadein 2.5
    play sound sfx_heartbeat fadeout 3.0

    iris fatigue "Tu comptes dormir jusqu'au prochain vote ?"
    "Quelque chose de froid se pose sur mon front. J'essaie de répondre. Ma langue, elle, a visiblement démissionné."
    iris inquiet "Ah. Ça bouge. Bon signe."

    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 2.0)
    $ showGroup([("noam", "faible", 0.28), ("iris", "fatigue", 0.72)])
    noam faible "Iris... ?"
    iris taquin "Non. Kami dans un nouveau corps. Tu trouves qu'elle a fait du bon boulot ?"
    noam fatigue "T'es moins agréable."
    iris colere "Il EST vivant. Et déjà pénible."

    $ hideGroup()
    scene bg_cg031 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg031")
    "Iris tient un linge humide. Ses cheveux partent dans tous les sens et une marque rouge lui traverse la joue."
    noam hesitation "Qu'est-ce qui s'est passé ?"
    iris fatigue "Tu t'es écroulé au Conclave. Devant tout le monde. Avec le petit bruit de chaise qui va bien."
    noam inquiet "Hier ?"
    iris desaccord "Non, dans six mois. Oui, hier !"
    noam fatigue "Je me rappelle la table. Après... rien."
    iris neutre "Après, t'as essayé d'embrasser le sol. Sael et Elias t'ont rattrapé."

    "Elle essore le linge au-dessus du bol. Une partie de l'eau tombe sur la couverture."
    iris fatigue "Merde."
    noam sourire "Si tu voulais me noyer, fallait prendre un seau."
    iris colere "Tu peux aussi dire merci. C'est un mot qui existe."
    noam sourire "Merci."
    iris gene "... Pas aussi vite."
    noam surpris "Pardon ?"
    iris colere "Rien ! Bois."

    "Je tente de me redresser. La douleur derrière mes yeux me recouche presque toute seule."
    iris inquiet "Hé ! Doucement !"
    noam fatigue "Je m'assois, c'est tout."
    iris determine "Non. Tu te recouches, tu bois, et après on négocie le droit de t'asseoir."
    noam sourire "J'ai perdu tous mes droits civiques ?"
    iris desaccord "Tant que tu continues à tomber dans les pommes, oui."

    "Elle me met un verre dans la main et ne le lâche que lorsqu'elle est sûre que je le tiens."
    noam inquiet "J'ai dormi combien de temps ?"
    iris fatigue "Toute la nuit. Fièvre, sueurs, phrases incompréhensibles... Très bonne ambiance."
    noam reflexion "C'est toi qui m'as soigné ?"
    iris desaccord "Sael. Moi, j'ai changé le linge et empêché Julian de transformer ta chambre en salle d'attente officielle."
    noam sourire "Donc t'es restée."
    iris gene "Quelqu'un devait vérifier que tu t'étouffes pas !"
    noam taquin "Ça arrive souvent ?"
    iris colere "Tu veux vraiment tester ma patience au réveil ?"

    "Je ris. Mon crâne me rappelle aussitôt que c'était une mauvaise idée."
    iris inquiet "Ça va ?"
    noam fatigue "Je viens de regretter une blague. C'est grave."
    iris taquin "Enfin un symptôme encourageant."
    iris fatigue "Ryn est passé. Enfin... il s'est arrêté devant la porte."
    noam inquiet "Il est entré ?"
    iris neutre "Non. Il a demandé si t'étais mort. J'ai dit non. Il a répondu : ‘Bon.’"
    noam sourire "C'est presque affectueux."
    iris neutre "Dans son dialecte, sûrement."

    "Je cherche la fin de la veille. Le couloir de l'infirmerie. Cette peur arrivée avant la fièvre."
    think "Il manque quelque chose. Pas juste les heures après ma chute."
    iris reflexion "Quoi ?"
    noam hesitation "Quoi, quoi ?"
    iris desaccord "Cette tête. Tu viens de retrouver un problème et tu vas le garder jusqu'à ce qu'il t'explose dessus."
    noam fatigue "J'ai une tête spéciale pour ça ?"
    iris taquin "Oui. Elle m'énerve."

    menu:
        "Lui parler de ce qui s'est passé dans le couloir.":
            jump noam_parle_doppelganger_iris
        "Ne rien lui dire pour le moment.":
            jump noam_garde_secret

    # Durée : 2m15


label noam_parle_doppelganger_iris:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5
    $ showGroup([("noam", "fatigue", 0.25), ("iris", "inquiet", 0.75)])
    noam hesitation "Hier, dans le couloir de l'infirmerie... avant l'annonce de Kami."
    iris inquiet "Quoi ? Ton coup de chaud ?"
    noam reflexion "J'ai vu quelqu'un. Enfin, je crois."
    iris desaccord "Tu crois ou tu l'as vu ?"
    noam inquiet "Sur le moment, j'en étais sûr. Maintenant, j'arrive même plus à remettre un visage dessus."
    iris reflexion "Sael t'a trouvé là."
    noam hesitation "Oui, mais avant elle..."
    "Je m'accroche au souvenir. Un fond de couloir. Une silhouette. Puis cette peur absurde."
    noam fatigue "J'ai regardé devant moi et j'ai paniqué. Vraiment. Sans savoir pourquoi."
    iris inquiet "Tu avais déjà de la fièvre."
    noam reflexion "Donc j'ai halluciné ?"
    iris desaccord "J'en sais rien, Noam. Je vais pas choisir une réponse juste pour te rassurer."
    noam fatigue "D'accord."
    iris reflexion "Mais hier, t'as interrogé tout le monde devant tout le monde."
    noam culpabilite "Je voulais juste vérifier."
    iris neutre "Je sais. Eux, ils ont surtout vu un type livide leur demander des alibis."
    "Elle prend le verre vide et se lève."
    iris determine "Si tu cherches, tu le fais quand tu peux marcher droit. Et pas en accusant douze personnes d'un coup."
    noam sourire "Tu me donnes ta bénédiction pour enquêter ?"
    iris colere "Je te donne l'ordre de rester vivant assez longtemps pour réfléchir !"
    noam sourire "Très bien, chef."
    iris gene "Et si ça recommence... tu viens me voir. Tout de suite."
    noam fatigue "Promis."
    iris desaccord "T'as intérêt. Je vais chercher à manger. Tu ne bouges pas."
    jump _11_0_1_1_APRES_REVEIL

    # Durée : 1m05


label noam_garde_secret:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5
    $ showGroup([("noam", "fatigue", 0.25), ("iris", "inquiet", 0.75)])
    noam hesitation "Rien. J'essayais de me rappeler comment je suis tombé."
    iris desaccord "Tu mens mal."
    noam fatigue "Tu dis toujours ça."
    iris taquin "Parce que tu mens toujours pareil."
    "Je bois pour éviter de répondre. Elle attend. Je continue alors que le verre est presque vide."
    iris fatigue "Bon. Je vais pas te l'arracher. Pas aujourd'hui."
    noam fatigue "Merci."
    iris taquin "C'était pas un cadeau."
    "Elle remet le linge en place, puis retire sa main beaucoup trop vite."
    iris neutre "Tu as déjà fait assez peur à tout le monde. Mange au moins quelque chose."
    noam sourire "Petit-déjeuner au lit ?"
    iris desaccord "Ration de survie. Nuance."
    noam taquin "C'est presque romantique."
    iris colere "Ne te fais pas d'idées !"
    call kd_vn_reaction("iris", "colere", "#ff9c55")
    "Elle atteint la porte, s'arrête et garde la main sur la poignée."
    iris gene "Si ton ‘rien’ devient autre chose... tu peux m'en parler. Plus tard."
    noam fatigue "D'accord."
    iris fatigue "Et ne bouge pas. Pour une fois, fais semblant d'être simple."
    jump _11_0_1_1_APRES_REVEIL

    # Durée : 0m50


label _11_0_1_1_APRES_REVEIL:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    "Une fois seul, je pose les pieds au sol. La pièce bascule légèrement. Je les remonte aussitôt."
    noam faible "D'accord. Un point pour Iris."
    "Sur le bureau, l'emplacement du dessin de Juliette est toujours vide."
    think "Je pourrais reprendre mes recherches. Ou m'ouvrir le crâne sur le coin de la table."

    "Des voix arrivent du couloir avec un bruit de vaisselle malmenée."
    julian colere "JE N'AI JAMAIS DIT QU'IL FALLAIT TOUT METTRE !"
    iris colere "C'EST TOI QUI AS PRIS LE PLUS GRAND PLATEAU !"
    sael desaccord "Arrêtez de pousser."
    "La porte s'ouvre."
    $ showGroup([
        ("noam", "fatigue", 0.08), ("iris", "neutre", 0.26),
        ("sael", "neutre", 0.44), ("julian", "neutre", 0.64),
        ("nyra", "neutre", 0.86),
    ])
    julian joie "Messieurs-dames : le service de restauration le plus prestigieux de l'orbite."
    iris colere "Pose le plateau avant de tuer le malade."
    julian agace "Je le pose !"
    play sound "audio/sfx_metal_clank.mp3"
    "Le plateau heurte la table. Un morceau de pain roule jusqu'au bord."
    noam sourire "C'est un repas ou une attaque ciblée ?"
    julian sourire "Les deux restent possibles."
    sael desaccord "Écarte-toi, Julian."
    julian surpris "J'aide !"
    nyra raison "Tu aiderais davantage en libérant le passage."
    julian agace "Une coalition contre les bénévoles. Déjà."
    iris taquin "Et elle est unanime."

    "Sael prend mon poignet, compte les battements, puis pose deux doigts contre mon front."
    sael neutre "La fièvre est tombée. Tu restes au calme aujourd'hui."
    noam fatigue "Au Conclave, rester au calme est une activité à plein temps."
    sael determine "Alors tu as de l'entraînement."
    nyra neutre "J'ai demandé quelque chose de simple. Riz, poulet, légumes."
    julian taquin "La gastronomie du rétablissement. Aucun risque d'y prendre goût."
    iris colere "Tu peux le laisser manger sans critiquer la nourriture ?"
    noam sourire "C'est délicieux."
    julian surpris "Tu n'as encore rien goûté."
    noam taquin "Je voulais voir si ça t'agacerait."
    julian agace "Succès incontestable."
    sael neutre "Mange."

    "Pendant quelques minutes, ils débattent du sel, des desserts et des portions."
    julian joie "Un malade mérite un dessert supplémentaire. C'est une question de morale."
    iris taquin "Tu t'es découvert une maladie ?"
    julian neutre "Le manque de reconnaissance."
    nyra raison "Le traitement risque d'être long."
    "J'avale de travers."
    noam surpris "Nyra !"
    nyra neutre "C'était un diagnostic provisoire."

    noam reflexion "Kael n'est pas venu ?"
    iris inquiet "Il est passé cette nuit. Il ne voulait pas te réveiller."
    sael reflexion "Il a demandé si la fièvre baissait, puis il est reparti."
    julian neutre "Il n'a toujours pas retrouvé la photo de Léa."
    iris desaccord "Julian."
    julian agace "Quoi ? Noam le sait déjà."
    nyra reflechit "Kael a demandé l'accès aux images de sa chambre. Kami ne lui a pas répondu."

    call show_custom_title("Une bonne heure plus tard") from _call_show_custom_title_2
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "neutre", 0.08), ("iris", "neutre", 0.26),
        ("sael", "neutre", 0.44), ("julian", "neutre", 0.64),
        ("nyra", "neutre", 0.86),
    ])
    julian joie "Voilà. Il a mangé. Je réclame une médaille."
    iris fatigue "Tu l'as regardé mâcher."
    julian neutre "J'ai transporté le plateau."
    sael desaccord "Tu as failli le renverser."
    julian agace "La postérité oublie toujours les détails."

    "Je me lève en gardant une main sur le lit."
    sael inquiet "Doucement."
    noam fatigue "J'ai besoin de marcher cinq minutes. Pas de courir autour de la station."
    iris desaccord "Tu veux que je te porte aussi ?"
    noam taquin "Tu pourrais ?"
    iris colere "Essaie pour voir."
    nyra reflechit "La salle d'observation est plus fraîche. Nous pouvons l'accompagner."
    sael neutre "Quelques minutes. Au premier vertige, on revient."

    $ hideGroup()
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Dans le couloir, Julian développe un système complet de répartition des desserts. Iris démonte chaque règle. Sael marche près de moi sans en avoir l'air."
    julian joie "Trois catégories : consolation, victoire et nécessité diplomatique."
    iris desaccord "Tu viens d'inventer trois excuses pour manger du sucre."
    julian sourire "Trois excellentes excuses."
    sael neutre "On arrive."

    "Une voix traverse la porte entrouverte de la salle d'observation."
    stop music fadeout 0.5
    play sound sfx_announce
    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    $ bc_show("kael", "colere")
    kami "Kael, j'aimerais énormément t'aider. Mais même une technologie parfaite ne peut pas accélérer le temps pour tes beaux yeux."
    kael colere "Sept jours. C'est ta réponse ?"
    kami "C'est ma réponse. Tu veux que je la chante ?"
    kael colere "Je veux les images de ma chambre. Celles de la nuit où la photo a disparu."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et moi, je veux un peu de gratitude. Nous allons devoir vivre avec nos déceptions respectives."
    kael colere "KAMI !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Les brouilleurs imposent un délai de sept jours avant l'accès aux enregistrements audio et vidéo de la zone protégée."
    kael doute "Même si le vote échoue ?"
    kami "Même si le vote échoue. Une interdiction future ne recrée pas les données indisponibles aujourd'hui."
    $ bc_hide()
    hide screen kami_broadcast_ui

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_42
    scene bg_observation at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([
        ("noam", "fatigue", 0.05), ("iris", "inquiet", 0.22),
        ("sael", "neutre", 0.39), ("kael", "colere", 0.56),
        ("julian", "neutre", 0.73), ("nyra", "neutre", 0.90),
    ])
    kael colere "Donc celui qui a pris la photo a une semaine. Une semaine où je peux rien vérifier."
    iris inquiet "Kael..."
    kael colere "Vous êtes là depuis combien de temps ?"
    julian taquin "Assez pour confirmer que Kami reste une partenaire administrative remarquable."
    nyra reflechit "Elle a parlé de la zone protégée. Pas de toute la station."
    nyra raison "Le délai vient du brouilleur ou de la base d'archives ?"

    play sound sfx_announce
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    $ bc_show("nyra", "raison")
    kami "Nyra, toujours prête à chercher la petite ligne en bas du contrat."
    nyra raison "Le délai vient du brouilleur ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Oui. Et non, tu n'auras ni le manuel, ni le schéma, ni un joli cours privé."
    nyra taquin "Tu viens de répondre à ma question."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ne prends pas cette habitude."
    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 0.8
    $ showGroup([
        ("noam", "fatigue", 0.05), ("iris", "inquiet", 0.22),
        ("sael", "neutre", 0.39), ("kael", "triste", 0.56),
        ("julian", "neutre", 0.73), ("nyra", "raison", 0.90),
    ])
    sael neutre "Personne ne te demande d'oublier Léa."
    kael triste "J'ai pas dit ça."
    sael reflexion "Je sais."
    iris desaccord "Tu as mangé ?"
    kael colere "Ça n'a rien à voir !"
    iris neutre "Exact. Réponds quand même."
    kael fatigue "... Non."
    iris desaccord "Évidemment."
    kael calme "Si vous trouvez quoi que ce soit sur les chambres, vous me le dites. Même si ça paraît idiot."
    noam fatigue "Oui."

    call play_stat_dialogue("j11") from _call_play_stat_dialogue_10

    "Kael quitte la salle sans attendre."
    julian neutre "Les desserts diplomatiques attendront."
    iris fatigue "Pour une fois, ferme-la sans commentaire."
    nyra reflechit "La distinction reste importante. Les brouilleurs protègent les chambres. Pas les couloirs."
    noam reflexion "Pas les couloirs..."
    sael inquiet "Noam ?"
    "Je me suis appuyé au mur. La salle vient de pencher, ou c'est moi."
    noam fatigue "Je retourne m'allonger."
    iris desaccord "Oui. Maintenant."
    nyra neutre "Tu veux qu'on t'accompagne ?"
    noam fatigue "C'est à côté. Ça va."
    sael determine "Tu marches lentement. Et tu appelles si ça recommence."
    jump _11_0_1_2_CHAMBRE_INTROSPECTION

    # Durée : 4m00


label _11_0_1_2_CHAMBRE_INTROSPECTION:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_43
    scene bg_chambre at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    "Je ferme la porte, retire mes chaussures et tombe sur le lit."
    noam fatigue "Voilà. J'obéis. Tout le monde peut se détendre."
    "Le silence tient dix secondes. Puis la phrase de Nyra revient."
    think "Les chambres. Pas les couloirs."
    "Je regarde le brouilleur fixé au mur. Son voyant pulse tranquillement."
    noam reflexion "Sept jours pour une zone protégée..."
    "Hier, je n'étais pas dans une chambre. J'étais devant l'infirmerie."
    noam inquiet "Et dans le couloir, il n'y a pas de brouilleur."

    call _11_0_1_2_MINIJEU_7JOURS from _call__11_0_1_2_MINIJEU_7JOURS

    play music "music/bgm_world_decline.mp3" fadein 2.0
    "Les éléments se remettent en place. Le délai ne bloque pas les caméras du couloir."
    noam reflexion "Donc les images devraient être accessibles."
    "Je regarde mes chaussures. Iris m'étranglerait. Sael finirait probablement le travail."
    noam sourire "Et Julian prononcerait un discours à l'enterrement."
    "Je les remets. Lentement."
    think "Si j'ai halluciné, les images me le diront. Si je n'ai pas halluciné..."
    noam fatigue "Je pose une question. Une seule. Après, je reviens."

    call KD_ROUTE_J11_NYRA from _call_optional_kd_route_j11_nyra
    call OFFER_DAILY_EXPLORATION(
        "_11_0_1_3_SALLE_COMMUNICATION", 1,
        ["observation", "archive", "dortoir"],
        _("Rejoindre la salle d'Observation"), "observation"
    ) from _call_offer_exploration_j11

    # Durée : 1m00 + mini-jeu/exploration


label _11_0_1_3_SALLE_COMMUNICATION:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_44
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0
    "La Terre tourne sur les écrans. Je m'installe devant une console et attends."
    noam fatigue "Kami ?"
    pause 0.6
    noam taquin "C'est le moment où tu apparais pour dire que j'ai une tête de cadavre."

    play sound sfx_announce
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    $ bc_show("noam", "fatigue")
    kami "Oh, mais je peux le faire ! Tu as une tête épouvantable, Noam. Merci de m'avoir mâché le travail."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je croyais que tu devais te reposer. Iris et Sael vont être très déçues de mon encadrement."
    noam fatigue "Elles sont pas là."
    kami "La désobéissance commence toujours par une phrase aussi intelligente."
    noam reflexion "J'ai besoin des enregistrements d'hier. Couloir de l'infirmerie, juste avant ton annonce."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Nous avons donc un enquêteur. Fiévreux, désobéissant et sans mandat, mais un enquêteur."
    noam colere "Les images sont accessibles ou pas ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Les couloirs ne sont pas protégés par les brouilleurs de vos chambres."
    noam reflexion "Donc oui."
    kami "Donc tu peux consulter le catalogue. Si les images existent encore."
    noam inquiet "Pourquoi elles n'existeraient plus ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Parce que tu poses trop de questions avant même d'avoir regardé."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Heure, secteur, caméra. Je t'ouvre le catalogue. Essaie de ne pas t'évanouir sur la console."
    noam desaccord "Merci pour ta confiance."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Toujours."
    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    "La console se déverrouille. Des dizaines de secteurs et de créneaux apparaissent."
    "Je lance la recherche. Mon cœur bat beaucoup trop vite pour un simple menu d'archives."
    call _11_0_1_3_MINIJEU_CAMERAS from _call__11_0_1_3_MINIJEU_CAMERAS

    # Durée : 1m00 + mini-jeu


label _11_0_1_1_CONFRONTATION_KAMI:
    scene bg_observation at adaptive_fullscreen with dissolve
    "Je sélectionne le dernier créneau. L'aperçu du couloir apparaît."
    "Mon doigt reste au-dessus de la commande de lecture."
    noam inquiet "Allez..."
    play sound "audio/sfx_glitch.mp3"
    "L'image saute."
    "DONNÉES SUPPRIMÉES — ACCÈS IMPOSSIBLE."
    $ investigation_add("videos_supprimees")
    "Je clique encore. Même message. Une troisième fois. Rien."
    noam colere "Non... Non, putain !"
    noam colere "KAMI !"

    play sound sfx_announce
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    $ bc_show("noam", "colere")
    kami "Oh ! Nous en sommes déjà à l'étape où tu cries mon nom dans une pièce vide."
    noam colere "Les images ont été supprimées !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oui. Je sais lire."
    noam colere "C'est toi ?"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Moi ? Après toute la gentillesse dont je viens de faire preuve ?"
    noam desaccord "Tu pouvais m'ouvrir un faux catalogue."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "La requête d'effacement ne vient pas de moi. Une information gratuite. Profites-en."
    noam reflexion "Une requête ? Qui l'a envoyée ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Un accès autorisé à bord du Conclave."
    noam inquiet "Un représentant ?"
    kami "Je n'ai pas dit ça. Les mots comptent, surtout quand tu t'apprêtes à accuser tes amis."
    noam colere "Tu sais qui c'est."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Peut-être."
    noam colere "Alors dis-le !"
    kami "Non."

    pause 0.6
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Pose une meilleure question. Tout a-t-il été effacé ? Quand ? Qui possédait un accès ?"
    noam reflexion "Seulement ce créneau ?"
    kami "Seulement ce segment. Tu apprends vite quand tu es contrarié."
    noam inquiet "Il y avait quelque chose dessus."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C'est une hypothèse."
    noam colere "Quelqu'un a supprimé exactement le moment que je cherche !"
    kami "Ça, c'est un fait."

    call cutin("noam") from _call_kd_cutin_j11_noam
    noam colere "{shout}ARRÊTE DE JOUER AVEC MOI !{/shout}"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "TU ES VENU ME VOIR ! Tu m'accuses, tu exiges, et tu voudrais décider du ton ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais je vais encore t'aider. Cherche qui pouvait accéder à ce secteur."
    noam inquiet "Les autres..."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Ceux qui te donnent de l'eau. Qui veillent à ton chevet. Quelle adorable petite communauté."
    "Iris endormie au bord du lit. Sael, la main sur mon poignet. Julian et son plateau ridicule."
    think "Elle veut que je transforme chaque geste en mobile."
    noam desaccord "Tu n'as rien prouvé."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Exact. Et toi non plus."
    noam reflexion "Si quelqu'un a effacé les images, il savait ce que j'allais chercher ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Très bonne question."
    noam colere "Réponds."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Toujours non."
    noam fatigue "Tu prends vraiment plaisir à ça."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Énormément."
    noam colere "Va te faire foutre."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "LANGAGE !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Retourne te coucher, mon petit détective. Tu as tenu toute une conversation sans perdre connaissance."
    noam inquiet "Et les images ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Toujours supprimées. Certaines choses restent stables. C'est rassurant, non ?"
    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_observation at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    "Je me lève. L'écran derrière moi se rallume une dernière fois."
    play sound sfx_announce
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    kami "Noam ? Si tu n'avais rien vu d'important... pourquoi quelqu'un aurait-il pris le risque d'effacer ce passage ?"
    hide screen kami_broadcast_ui
    scene black with cut
    think "Une question. Pas une réponse."
    "Je quitte la salle avant qu'elle puisse en ajouter une autre."
    jump _11_0_1_1_RETOUR_CHAMBRE

    # Durée : 2m35


label _11_0_1_1_RETOUR_CHAMBRE:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_47
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0
    "Une dispute déborde de la salle commune."
    julian colere "J'AI DIT QUE C'ÉTAIT UNE MÉDAILLE HONORIFIQUE !"
    iris colere "T'AS DESSINÉ TON PROPRE VISAGE DESSUS !"
    "Il y a quelques heures, j'aurais ri. Maintenant, je calcule le temps qu'ils ont passé ensemble et les portes auxquelles ils ont accès."
    think "Non. C'est exactement ce que Kami veut."

    "Au croisement du dortoir, une porte s'ouvre. Lysa passe la tête dans le couloir."
    $ showGroup([("noam", "fatigue", 0.25), ("lysa", "neutre", 0.75)])
    lysa neutre "Noam ?"
    noam fatigue "Salut."
    lysa reflechit "Tu tiens debout. C'est mieux qu'hier."
    noam sourire "Vous avez préparé des remarques sur mon malaise ?"
    lysa sourire "Concours collectif. Julian en avait dix-sept. On a abandonné."
    noam fatigue "Ça lui ressemble."
    "Elle me regarde vraiment. Pas comme les autres, qui vérifient si je vais tomber."
    lysa reflechit "Tu vas bien ?"
    noam fatigue "Je suis crevé."
    lysa blase "C'était pas la question."
    noam hesitation "Je cherche encore le dessin. Et... autre chose."
    lysa reflechit "Tu trouves ?"
    noam fatigue "Surtout des questions."
    lysa neutre "D'accord."
    "Elle ne me demande pas lesquelles. Ça rend le silence plus difficile."
    lysa taquin "Si tu veux parler, évite de t'écrouler avant d'atteindre ma porte. C'est mauvais pour ma réputation."
    noam sourire "Je vais faire un effort."
    lysa neutre "Fais ça."
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_48
    scene bg_chambre at adaptive_fullscreen with fade
    "Je verrouille la porte et m'assieds devant le bureau."
    "La photo de Léa. Le dessin de Juliette. Les batteries cherchées par Elias. Maintenant, un segment vidéo."
    noam reflexion "Des objets disparaissent. Des données aussi."
    "Sur ma tablette, je note trois expressions : ‘accès autorisé’, ‘segment supprimé’, ‘sept jours’."
    think "Aucune ne prouve qu'un représentant a fait quoi que ce soit."
    "J'ajoute une quatrième ligne, puis je l'efface : ‘Quelqu'un savait.’"
    noam fatigue "Pas encore."

    "Des pas passent devant ma porte. Je me fige, la main sur la tablette."
    pause 0.8
    "Ils continuent jusqu'au bout du couloir."
    noam taquin "Très bien. Demain, j'interroge le sol."
    "La blague ne sort pas comme une blague."
    "Je me couche, puis me relève pour vérifier le verrou."
    think "Fermé."
    "Trois secondes plus tard, je vérifie encore."

    scene black with fade
    stop music fadeout 4.0
    call end_day("12", sleeping=True) from _call_end_day_2
    jump _12_0_1_1_REVEIL_CHAMBRE

    # Durée : 1m25
    # Total estimé : 12m55 + mini-jeux et exploration
