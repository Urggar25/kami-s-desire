label _23_0_1_1_0_0_REVEIL:
    $ current_day = 23
    $ day_id = 23
    $ current_period = "Matin"
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2

    "Je me réveille avant l'alarme et tends aussitôt l'oreille."
    "La chambre est calme. Les conduits aussi."

    think "J'ai dormi normalement. Ça faisait longtemps."

    "Le bureau est à sa place. Je lève les yeux vers la grille, trop haute pour que je puisse la bloquer avec un meuble. Mon sac est toujours prêt au pied du lit."
    "Sept jours avant de partir, si Kami tient parole et si personne ne trouve une nouvelle façon de tout faire dérailler."

    "Je m'habille et passe devant le miroir."
    "J'ai mauvaise mine. Rien de nouveau."

    think "Mara morte derrière les conduits. Mara vivante hier soir. Il y a forcément une explication entre les deux."

    "Je vais manger avant de recommencer à tourner en rond."

    # Durée : ~1m00
    # Total : ~1m00


label _23_0_1_1_0_0_PETIT_DEJEUNER:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_28
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "La cafétéria est déjà bien remplie. Elias se plaint du café, Mara parle trop fort et Iris a l'air de regretter d'être réveillée."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "reflexion"),
        ("iris", "fatigue"),
        ("noam", "fatigue"),
    ])

    mara taquin "Tiens, le mort-vivant."

    noam blase "Bonjour Mara."

    mara sourire "T'as une tête affreuse. Et là je suis gentille."

    iris fatigue "Elle a raison. T'as dormi combien de temps ?"

    noam neutre "Assez pour savoir que vous êtes insupportables dès le matin."

    "Je m'assois. Mara sourit. Iris recommence à manger."
    "Sael, elle, me fixe depuis que je suis arrivé."

    noam reflexion "Quoi ?"

    sael neutre "T'as entendu les bruits cette nuit ?"

    "Je baisse légèrement ma fourchette."

    noam desaccord "Non. Rien."

    mara taquin "Le monstre avait peut-être congé."

    iris agace "Tu peux arrêter avec ça ?"

    "Mara lève les mains, mais Sael n'a pas souri."

    sael raison "Noam, j'aimerais vérifier deux ou trois choses. Tu veux bien ?"

    noam surpris "Des examens ?"

    sael neutre "À l'infirmerie."

    noam reflexion "Pourquoi maintenant ?"

    sael raison "Parce que t'as eu de la fièvre, des trous de mémoire, et que maintenant tu vois des choses que personne d'autre ne voit."

    "Mara arrête de jouer avec sa tasse."

    sael raison "Je ne sais pas ce que tu as vu. Je peux au moins vérifier que tu vas bien."

    noam inquiet "Tu penses que je deviens fou ?"

    sael desaccord "J'ai dit l'inverse. Je veux vérifier."

    "Je la regarde, pas vraiment convaincu."

    sael raison "Fatigue extrême. Problème de vision. Manque d'oxygène. Traumatisme. Il y a des dizaines de causes possibles."

    iris reflexion "Et tu sais vraiment vérifier ça ?"

    sael fatigue "Une partie, oui. Pour le reste, il y a l'imagerie."

    noam surpris "L'imagerie ?"

    sael neutre "L'infirmerie est équipée d'une sorte d'IRM."

    noam inquiet "Attends. Tu veux vraiment me mettre dans cette machine ?"

    mara taquin "Moi je veux voir les résultats. Je suis sûre qu'il y a des trucs sales là-dedans."

    iris blase "Toi, tu ne viens pas."

    mara sourire "J'ai rien demandé."

    iris determine "Moi, par contre, je viens."

    sael desaccord "J'ai pas besoin de toi."

    iris colere "La dernière fois que vous avez voulu aider Noam, Ryn l'a plaqué contre un mur et vous l'avez couvert de sel."

    sael colere "J'ai jamais demandé à Ryn de le plaquer contre un mur."

    iris blase "Super. Ça me rassure énormément."

    "Sael souffle par le nez."

    sael fatigue "Tu vas râler pendant tout l'examen."

    iris blase "Oui."

    noam neutre "Je suis ravi que tout le monde ait déjà décidé pour moi."

    sael reflexion "Alors décide."

    "Le ton change. Plus personne ne plaisante."

    call play_stat_dialogue("j23") from _call_play_stat_dialogue_2

    sael raison "Tu veux savoir si ce que t'as vu peut venir de toi ou pas ?"

    "Je regarde Mara. Elle évite mes yeux."

    noam fatigue "Oui."

    "Sael hoche la tête."

    sael raison "Alors on y va après."

    mara taquin "Et moi je reste ici comme une pauvre victime ?"

    iris colere "Exactement."

    "Mara lui adresse un doigt d'honneur. Je souris malgré moi."

    $ hideGroup()

    # Durée : ~3m00
    # Total : ~4m00


label _23_0_1_1_0_0_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_31
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Quelques minutes plus tard, je suis assis sur un lit pendant que Sael prépare son matériel."
    "Iris reste contre le mur, les bras croisés."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "blase", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    noam reflexion "Tu sais vraiment ce que tu fais ?"

    sael desaccord "Oui."

    noam neutre "Tu pourrais développer."

    sael colere "Je pourrais aussi commencer."

    iris taquin "Commence. Sinon il va poser la question dix fois."

    "Sael sort une lampe et vérifie mes pupilles."

    noam colere "Putain ! Préviens !"

    sael neutre "Je viens de te dire que je commençais."

    iris rire "Elle marque un point."

    "Sael enchaîne sans perdre de temps : yeux, force dans les mains, équilibre, réflexes."
    "En moins de cinq minutes, elle a rempli la moitié d'une page."

    sael raison "Tout va bien jusque-là."

    noam reflexion "Tu pourrais avoir l'air plus contente."

    sael neutre "J'ai pas fini."

    "Elle rapproche une chaise."

    sael raison "Fixe mon nez."

    noam surpris "Pourquoi ton nez ?"

    sael colere "Parce qu'il est au milieu."

    "Iris ricane. Je fixe Sael pendant qu'elle bouge les doigts à la limite de mon champ de vision."

    sael raison "Droite."

    noam neutre "Vu."

    sael raison "Gauche."

    noam neutre "Vu."

    "Elle recommence."

    sael raison "Gauche."

    "Je ne vois rien."

    sael reflexion "Et là ?"

    noam inquiet "Là quoi ?"

    "Elle recommence. Toujours rien."

    "Iris décroise les bras."

    iris inquiet "Qu'est-ce qu'il y a ?"

    sael reflexion "Attends."

    "Troisième essai. Cette fois j'aperçois le mouvement, mais très tard."

    noam inquiet "Là."

    "Sael baisse les mains."

    sael reflexion "C'est pas normal."

    "Mon ventre se serre."
    "Et pourtant, pendant une seconde, je ressens presque du soulagement."

    think "Enfin quelque chose."

    noam reflexion "Ça peut expliquer les visions ?"

    sael desaccord "J'ai pas dit ça."

    noam inquiet "Mais ça peut venir du cerveau."

    sael fatigue "Ou de l'œil. Ou de l'éclairage. On recommence."

    "Elle me fait changer de place et ouvre davantage le rideau."

    "Même test. Cette fois je vois tout, à droite comme à gauche."

    "Sael recommence encore deux fois."

    sael fatigue "C'était probablement la lumière."

    noam agace "Probablement."

    iris inquiet "T'avais l'air presque soulagé."

    noam desaccord "N'importe quoi."

    iris desaccord "Si."

    "Je détourne les yeux."

    noam fatigue "Au moins j'aurais eu une explication."

    "Iris ne répond rien."

    sael neutre "Je revérifierai après."

    "Elle passe au test de mémoire, beaucoup plus banal."

    sael raison "Fenêtre. Orange. Cheval. Métal. Pluie."

    noam neutre "Fenêtre, orange, cheval, métal, pluie."

    "Elle vérifie ensuite la date, le lieu et quelques souvenirs récents."

    sael reflexion "Maintenant raconte-moi ce que t'as vu."

    "Iris se redresse légèrement."

    noam inquiet "Pourquoi ?"

    sael raison "Je veux voir ce dont tu te souviens exactement."

    "Je prends quelques secondes."

    noam faible "J'ai trouvé la salle. Il y avait quelqu'un au sol. J'ai reconnu Mara."

    sael reflexion "Comment ?"

    noam reflexion "Son visage. Ses cheveux. Ses vêtements. Je sais pas. C'était elle."

    sael reflexion "Tu l'as touchée ?"

    noam desaccord "Non."

    sael reflexion "Vérifié sa respiration ?"

    noam colere "Non."

    iris colere "Il était paniqué, Sael."

    sael desaccord "Je lui demande pas pourquoi. Je lui demande ce dont il se souvient."

    noam fatigue "Laisse."

    "Je ferme les yeux."

    noam peur "Il y avait du sang. Je me souviens surtout de ça."

    sael reflexion "Où ?"

    noam colere "Je sais plus."

    "Sael arrête d'écrire."

    noam fatigue "Après je suis sorti. Et plus tard je l'ai revue à la cafétéria."

    "Je rouvre les yeux."

    noam faible "Vivante."

    "Sael garde le silence."

    noam reflexion "Tu me crois ?"

    sael fatigue "Je crois que tu te souviens de ça."

    noam neutre "C'est pas pareil."

    sael desaccord "Non."

    "Au moins elle ne ment pas."

    sael raison "Les cinq mots."

    noam surpris "Sérieux ?"

    sael neutre "Oui."

    noam reflexion "Fenêtre. Orange. Cheval. Métal..."

    "Je bloque."

    noam determine "Pluie."

    sael raison "Cinq sur cinq."

    "Elle refait rapidement le champ visuel. Cette fois, aucun problème."

    sael fatigue "Tout ce que j'ai testé est normal."

    "Je regarde la machine derrière la cloison."

    noam neutre "Il reste l'IRM."

    sael neutre "Oui."

    # Durée : ~5m00
    # Total : ~9m00


label _23_0_1_1_0_0_IRM:
    scene infirmerie2 at adaptive_fullscreen with dissolve

    "La machine me paraît plus petite quand je la regarde de loin."

    sael raison "Tout ce qui est métallique dans le bac."

    "Je retire mon badge, mon téléphone et ma ceinture."

    noam reflexion "Ça dure combien de temps ?"

    sael neutre "Une vingtaine de minutes."

    noam surpris "Vingt minutes ?"

    iris taquin "Il a peur."

    noam colere "J'ai pas peur."

    iris taquin "Tu viens de demander combien de temps tu vas rester enfermé."

    noam desaccord "Je me renseigne."

    sael fatigue "Tu as un bouton. Si tu paniques, tu appuies."

    noam reflexion "Et s'il marche pas ?"

    iris rire "D'accord. Là, t'as peur."

    noam agace "Ferme-la."

    "Je m'allonge sur la table."

    "Sael installe le support autour de ma tête. Iris s'approche et me tend la main."

    noam surpris "Sérieux ?"

    iris agace "Prends-la avant que je change d'avis."

    "Je la prends. Elle serre mes doigts une seconde."

    $ hideGroup()
    $ unlock_gallery_image("bg_cg061")
    call kd_vn_cg_impact("#e4f0ff")
    scene bg_cg061 at adaptive_fullscreen with dissolve

    iris blase "Voilà. T'es courageux. On peut avancer ?"

    noam sourire "Merci."

    sael taquin "C'est mignon."

    iris colere "Toi, commence pas."

    scene black with dissolve
    stop music fadeout 0.8

    "La table glisse."

    "Le premier claquement métallique me surprend malgré moi."
    "Puis le rythme change."

    "Trois coups rapides. Une pause. Deux autres."

    think "C'est la machine."

    "Le problème, c'est que ça ressemble beaucoup trop aux bruits des conduits."

    "Je ferme les yeux et compte pour penser à autre chose."

    "À vingt-sept, je perds le fil."

    "Entre deux séquences, j'entends quelque chose de plus doux."

    "Une respiration."

    "Je retiens la mienne."

    "Plus rien."

    think "Ventilation. Machine. Mon propre souffle. Il y a assez d'explications avant d'en inventer une quatrième."

    "Un frottement suit. Mon pouce se pose sur le bouton d'arrêt."

    menu:
        "Appuyer sur le bouton":
            "J'appuie. La machine s'arrête presque aussitôt."

            sael inquiet "Noam ? Qu'est-ce qui se passe ?"

            noam inquiet "J'ai entendu quelqu'un respirer."

            "Un silence passe derrière la vitre."

            iris inquiet "Tu veux qu'on te sorte ?"

            "Je pourrais dire oui. Au lieu de ça, je desserre les doigts."

            noam fatigue "Non. Relance."

            iris determine "Seulement si t'es sûr."

            noam determine "Je suis sûr."

            sael raison "D'accord. Ne bouge plus."

        "Continuer sans interrompre l'examen":
            "Je garde le pouce sur le bouton sans appuyer."

            sael neutre "Noam ? Tu bouges."

            noam fatigue "Désolé."

            iris inquiet "Ça va ?"

            noam desaccord "Oui."

            iris colere "Mens mieux."

            "Je souffle par le nez. Elle m'arrache presque un rire."

    "Le reste de l'examen paraît interminable, mais rien d'autre ne se passe."

    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

    $ showGroup([
        ("sael", "reflexion", 0.22),
        ("iris", "inquiet", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    "Quand la table ressort, Sael récupère immédiatement les images."

    noam reflexion "J'ai encore entendu un bruit."

    iris inquiet "Dans la machine ?"

    noam inquiet "Une respiration. Ou un frottement. J'en sais rien."

    sael raison "On était derrière la vitre. On a rien entendu."

    "Je hoche la tête."

    iris colere "Ça veut pas dire que tout le reste est faux."

    noam neutre "J'ai rien dit."

    iris agace "Tu le pensais."

    "Sael fait défiler les coupes."

    "Elle revient deux fois sur les mêmes images."

    "Le petit espoir idiot du test visuel revient."

    think "Trouve quelque chose."

    noam inquiet "Sael ?"

    sael reflexion "Attends."

    "Quelques secondes de plus."

    sael raison "Je vois rien d'anormal."

    noam surpris "Rien ?"

    sael raison "Pas de lésion visible. Pas d'hémorragie. Aucun signe évident de manque d'oxygène ou de traumatisme."

    iris reflexion "Et ça exclut les hallucinations ?"

    sael fatigue "Non. Ça exclut juste certaines causes."

    noam reflexion "Donc ma mémoire est normale, ma vision est normale et l'IRM est normale."

    sael neutre "Oui."

    noam inquiet "Et j'ai quand même vu Mara morte."

    "Sael ne répond pas."

    "Je laisse retomber ma tête contre le dossier."

    think "Normal. Pour une fois, le mot me fait pas plaisir."

    sael inquiet "Je voulais trouver une explication aussi."

    noam surpris "Sérieux ?"

    sael fatigue "Oui. Pas une maladie grave. Une raison."

    "Elle pose la tablette."

    sael fatigue "La fatigue, le stress ou une hallucination restent possibles. Mais je peux pas te dire : voilà, c'est ça."

    "Je hoche la tête."

    iris determine "Ça suffit. On va manger."

    noam reflexion "Iris..."

    iris colere "Non. Tu vas pas passer l'après-midi à lui faire répéter la même réponse jusqu'à ce qu'elle change."

    sael neutre "Elle a raison."

    noam blase "Formidable."

    $ hideGroup()

    # Durée : ~5m00
    # Total : ~14m00


label _23_0_1_1_0_0_APRES_IRM:
    $ current_period = "Après-midi"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "On retourne manger."

    $ showGroup([
        ("mara", "taquin"),
        ("iris", "fatigue"),
        ("sael", "fatigue"),
        ("noam", "fatigue"),
    ])

    mara taquin "Alors ? Qu'est-ce qu'ils ont trouvé ?"

    noam blase "Rien."

    mara sourire "Donc tout va bien."

    "Je ne réponds pas."

    "Son sourire baisse."

    mara reflexion "C'est pas ça ?"

    noam fatigue "Tout est normal."

    sael neutre "Sur ce qu'on a testé."

    mara reflexion "Ah."

    "Elle cherche une blague, puis renonce."

    mara reflexion "C'est quand même plutôt bien, non ?"

    noam fatigue "Ouais."

    "Mara tend la main vers mon assiette."

    mara taquin "Alors je prends une frite pour fêter ça."

    "Je tends la main pour l'arrêter."

    "Ses doigts touchent mon poignet."

    call kd_vn_reaction("noam", "peur", "#d9edff")

    "Pendant une seconde, ce n'est plus sa main sur mon poignet. C'est celle que j'ai vue au sol, derrière les conduits."

    "Je retire mon bras brutalement."

    mara surpris "Whoa !"

    "Sael et Iris se figent."

    noam peur "Désolé."

    mara reflexion "J'ai fait quoi ?"

    noam fatigue "Rien."

    mara reflexion "Noam, t'as reculé comme si je t'avais frappé."

    noam desaccord "J'ai dit que t'avais rien fait."

    "Mara me fixe."

    "Cette fois, elle ne plaisante pas."

    mara fatigue "D'accord."

    "Elle retire sa main."

    iris inquiet "Mara..."

    mara neutre "Non, c'est bon. Je vais le laisser tranquille."

    noam surpris "Attends."

    mara fatigue "Pourquoi ?"

    "Je pourrais lui dire la vérité. Devant tout le monde, les mots ne sortent pas."

    "Elle récupère son plateau."

    mara taquin "Je survivrai à une frite de moins."

    "Même elle n'y croit pas."

    "Elle s'éloigne."

    hide mara with dissolve

    iris colere "Bravo."

    noam agace "Quoi ?"

    iris colere "Elle sait même pas ce qui vient de se passer."

    noam colere "Moi non plus !"

    "Ma voix monte trop fort."

    "Je baisse les yeux."

    noam fatigue "Moi non plus."

    "Iris garde les bras croisés."

    sael neutre "C'est peut-être plus important que tous les tests de ce matin."

    noam reflexion "Quoi ?"

    sael raison "Ta réaction quand elle t'a touché."

    noam agace "Tu veux faire quoi ? Me la faire toucher dix fois pour voir si je panique ?"

    sael desaccord "Non."

    iris colere "Arrête."

    "Je me tais."

    "Voir Mara vivante ne suffit plus. Mon corps réagit avant que j'aie le temps de réfléchir."

    $ hideGroup()

    # Durée : ~3m00
    # Total : ~17m00


label _23_0_1_1_0_0_IRIS:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je retourne dans ma chambre."

    "Dix minutes plus tard, quelqu'un frappe."

    noam fatigue "Entre."

    $ showGroup([
        ("iris", "blase", 0.40),
        ("noam", "fatigue", 0.62),
    ])

    "Iris entre et referme la porte."

    iris fatigue "Je suis encore énervée."

    noam surpris "Je vois ça."

    iris colere "T'avais pas besoin de parler à Mara comme ça."

    noam agace "Je lui ai rien dit."

    iris colere "Justement."

    "Je la regarde."

    iris colere "Elle te touche, tu bondis, tu refuses de lui expliquer et tu la laisses partir en pensant qu'elle a fait quelque chose."

    noam colere "Tu veux que je lui dise quoi ? Que pendant une seconde j'ai revu son cadavre à la place de sa main ?"

    "Iris se tait."

    noam fatigue "Voilà."

    "Elle s'assoit sur le bord du lit."

    iris inquiet "C'était vraiment ça ?"

    noam fatigue "Oui."

    noam fatigue "Le contact a ramené le souvenir immédiatement. C'était pas une image floue. J'ai eu l'impression de revoir exactement la scène."

    iris desaccord "Une impression, Noam."

    noam colere "Je sais."

    iris desaccord "Alors arrête de la traiter comme une preuve."

    noam agace "Tu crois que je fais quoi depuis ce matin ?"

    "Je me lève."

    noam colere "J'ai accepté tous les tests de Sael parce que j'espérais qu'elle me dise que j'avais un problème. Tu te rends compte à quel point c'est débile ?"

    iris neutre "Oui."

    noam surpris "Merci."

    iris colere "Parce que moi aussi j'espérais qu'elle trouve quelque chose."

    "Je m'arrête."

    iris fatigue "Pas une tumeur. Pas un truc grave. Un manque de sommeil, un problème de pression, une hallucination liée au malaise... n'importe quoi qu'on puisse expliquer."

    noam neutre "Et elle a rien trouvé."

    iris fatigue "Non."

    "Le silence retombe."

    iris reflexion "Mais ça veut toujours pas dire que Mara était morte."

    noam desaccord "J'ai jamais dit que ça le prouvait."

    iris blase "Tu passes chaque nuit à surveiller cette fichue grille."

    noam desaccord "Parce que quelqu'un se balade dans les conduits."

    iris colere "Peut-être. Mais tu mélanges tout."

    noam colere "Et toi tu fais quoi ?"

    iris surpris "Quoi ?"

    noam colere "Tu viens me dire d'arrêter de paniquer et dans la même phrase tu veux que je t'appelle si j'entends un bruit."

    "Iris ouvre la bouche, puis s'arrête."

    noam determine "Donc toi aussi tu crois qu'il y a quelque chose."

    iris agace "Je crois surtout que t'es assez con pour retourner là-dedans tout seul."

    noam desaccord "C'est pas une réponse."

    iris colere "Parce que j'en ai pas !"

    "Le ton monte d'un coup."

    iris colere "J'en sais rien, d'accord ? Je sais pas ce que t'as vu, qui fait du bruit, ni pourquoi tu te souviens de Mara morte alors qu'elle mange avec nous !"

    "Elle reprend son souffle."

    iris fatigue "Et ça me fait chier de pas savoir."

    "Je reste silencieux."

    noam fatigue "Moi aussi."

    "Elle baisse les yeux."

    iris neutre "Alors arrête de faire comme si tu devais trouver tout seul."

    "La phrase sort beaucoup plus calmement."

    "Je me rassois."

    noam reflexion "Je dois m'excuser auprès de Mara."

    iris blase "Oui."

    noam blase "Tu pourrais au moins faire semblant d'hésiter."

    iris blase "Non."

    "Je souris malgré moi."

    iris fatigue "Et si t'entends quelque chose cette nuit, tu viens me chercher."

    noam reflexion "Tu crois aux bruits, alors."

    iris colere "Je viens de te dire que j'en sais rien."

    noam neutre "D'accord."

    iris determine "Mais tu n'y vas pas seul."

    noam neutre "D'accord."

    "Elle se lève."

    iris blase "Bien. Une décision intelligente dans la journée. On progresse."

    $ hideGroup()

    # Durée : ~4m00
    # Total : ~21m00


label _23_0_1_1_0_0_SOIREE:
    $ current_period = "Soir"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "Le soir, Mara est assise avec Elias et Tomas."
    "Je m'assois en face d'elle avant de changer d'avis."

    $ showGroup([
        ("mara", "neutre"),
        ("elias", "fatigue"),
        ("tomas", "reflexion"),
        ("iris", "fatigue"),
        ("noam", "fatigue"),
    ])

    elias fatigue "Alors, le gros tube ?"

    noam neutre "Toujours aussi gros."

    elias fatigue "C'est chaud. J'aime pas ces trucs."

    tomas reflexion "En réalité, une IRM est plutôt sûre si—"

    "Iris tourne lentement la tête vers lui."

    tomas hesitation "Je vais me taire."

    iris neutre "Merci."

    "Mara continue de manger."

    noam reflexion "Mara."

    mara neutre "Hm ?"

    noam fatigue "Désolé pour tout à l'heure."

    mara taquin "Pour la frite ?"

    noam fatigue "Pour le reste."

    "Elle me regarde quelques secondes."

    mara reflexion "J'avais compris que c'était pas contre moi."

    noam fatigue "Ça change rien."

    mara fatigue "Un peu."

    noam fatigue "Quand tu m'as touché, j'ai revu ce que j'avais vu derrière les conduits."

    "Elias et Tomas cessent de manger."

    mara neutre "Mon cadavre."

    noam fatigue "Oui."

    "Mara baisse les yeux vers son assiette."

    mara fatigue "C'est quand même une phrase sacrément bizarre à entendre sur soi."

    noam fatigue "Je sais."

    mara reflexion "T'as encore peur de moi ?"

    "La question me prend de court."

    noam surpris "Non."

    mara reflexion "T'as répondu vite."

    noam desaccord "Parce que c'est vrai."

    "Elle me fixe encore une seconde, puis son sourire revient."

    mara taquin "Bon. Alors je récupère ma frite."

    noam blase "Une."

    mara taquin "Deux."

    noam blase "Une."

    "Elle en prend deux."

    noam colere "Mara !"

    "Elias éclate de rire."

    "Cette fois, je ris aussi."

    "Tomas attend quelques secondes avant de reprendre."

    tomas reflexion "Pour ce que ça vaut... une IRM normale n'exclut pas un épisode hallucinatoire. Le stress, la fatigue et certains phénomènes transitoires peuvent—"

    iris fatigue "Tomas."

    tomas hesitation "Je sais. Mais c'était utile cette fois."

    "Je hausse les épaules."

    noam reflexion "Sael m'a dit la même chose."

    tomas raison "Alors elle a raison."

    elias neutre "Donc on sait toujours rien. On passe à autre chose."

    noam fatigue "Voilà."

    mara taquin "Super journée."

    "Un plateau tombe au fond de la salle."

    "Je sursaute violemment."

    "La conversation s'arrête."

    noam fatigue "Ça va."

    iris blase "Personne n'a demandé."

    noam blase "Je prends de l'avance."

    "Mara ne plaisante pas."

    "Je ramène ma chaise contre la table."

    think "C'est peut-être le seul résultat clair de la journée : tout fonctionne normalement, sauf ma façon de réagir à ce qui m'entoure."

    noam fatigue "Je vais dormir."

    iris inquiet "Tu veux que je vienne ?"

    noam neutre "Non."

    "Je vois son regard."

    noam fatigue "Et je ne vais pas retourner dans les conduits."

    iris neutre "Bien."

    mara taquin "Bonne nuit, cerveau normal."

    noam sourire "Bonne nuit, voleuse."

    $ hideGroup()

    # Durée : ~3m00
    # Total : ~24m00


label _23_0_1_1_0_0_FIN_JOURNEE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je vérifie une dernière fois la grille, bien au-dessus du bureau, puis m'assois sur le lit."

    "Le compte rendu de Sael est toujours ouvert sur ma tablette."

    "Réflexes normaux. Mémoire normale. Champ visuel normal après contrôle. Aucune anomalie visible."

    think "Normal."

    "J'aurais préféré une réponse."

    "Un bruit résonne dans le couloir."

    "Je lève immédiatement la tête."

    "Des pas passent devant ma porte."

    "Puis la voix de Mara, plus loin."

    mara rire "Mais attends-moi !"

    "Son rire s'éloigne."

    "Je reste quelques secondes à écouter."

    think "Si ce que j'ai vu était une hallucination, on ne sait toujours pas pourquoi."

    "Je regarde la grille."

    think "Et si ce n'en était pas une..."

    "Je coupe la pensée avant la fin."

    "Cette nuit, je laisse la lumière allumée."

    stop music fadeout 1.2

    call end_day("24", sleeping=True) from _call_j23_stay_end_day_24
    jump _24_0_1_1_0_0_REVEIL

    # Durée : ~1m30
    # Total : ~25m30
