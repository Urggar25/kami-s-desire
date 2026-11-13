label _15_0_1_1_0_REVEIL_CHAMBRE:

    $ cafeteria_food_level = "medium"
    $ current_period = "Matin"
    $ current_day = 15
    $ noam_has_juliette_drawing = False

    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "Je me réveille avant l’allumage automatique de la chambre, sans vraiment savoir si j’ai dormi ou si j’ai simplement passé la nuit les yeux fermés."
    "La pénombre me convient bien. Tant qu’il fait sombre, je peux encore prétendre que la journée n’a pas commencé."

    think "Jour 15..."
    think "Et encore un vote."

    "Je reste allongé quelques minutes, la couverture remontée jusqu’au ventre, en essayant de ne penser ni au Conclave, ni aux autres, ni à tout ce qui s’est passé depuis le dernier vote."

    think "À 14h, ils voteront sur l’ouverture totale des archives d’ARCHIVE."
    think "Sur le papier, ça ressemble presque à une bonne nouvelle. Rendre les informations accessibles, arrêter de décider à la place des gens de ce qu’ils ont le droit de savoir..."
    think "Mais ici, chaque bonne idée finit toujours par cacher quelque chose."

    play sound "audio/sfx_announce.mp3"
    show screen kami_broadcast_ui
    pause 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Bonjour, mes chers représentants ! J’espère que vous avez tous passé une nuit suffisamment reposante pour prendre une décision capable de bouleverser quelques millions de vies."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Le vote du jour aura lieu à 14h précises et concernera l’ouverture totale des archives d’[codex_dialogue_link('archive', 'ARCHIVE')] aux citoyens des districts."
    kami "Oui, oui, je sais ce que vous pensez : enfin un peu de transparence dans ce monde merveilleux !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Petit rappel pour ceux qui auraient miraculeusement oublié le Commandement V : toute information diffusée doit actuellement être validée par [codex_dialogue_link('archive', 'ARCHIVE')]."
    $ unlock_dossier_arg("p5_validation")
    kami "Si l’amendement passe, une immense partie des archives historiques, judiciaires et administratives deviendra accessible au public. Si vous échouez, le verrouillage actuel restera en place."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Évidemment, certaines personnes découvriront peut-être des choses qu’elles auraient préféré ne jamais savoir. Des mensonges, des décisions honteuses, quelques petits secrets de famille..."
    kami "Mais après tout, vous vouliez donner davantage de liberté aux gens, non ? Ce serait dommage de commencer à avoir peur de la vérité maintenant."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Et toi, Noam ? Tu nous feras l’honneur de venir aujourd’hui ?"
    kami "Ou tu préfères encore rester enfermé dans ta chambre pendant que les autres décident à ta place ?"

    "Mon ventre se noue immédiatement. Elle sait parfaitement ce qu’elle fait, et surtout que tous les autres entendent mon nom au même moment."

    noam inquiet "..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oh, ne prends pas cet air-là. Je te taquine... enfin, pas complètement."
    kami "À tout à l’heure, mes petits archivistes de l’apocalypse !"

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve

    "L’écran s’éteint et la chambre retrouve son silence, mais le calme d’avant a disparu avec lui."

    think "Elle voulait que tout le monde se rappelle que je peux encore ne pas venir."
    think "Comme s’ils avaient besoin de ça pour penser à moi."

    "Je finis par me redresser et attrape la tablette posée près du lit. Elle vibre presque aussitôt dans ma main."

    noam inquiet "Déjà...?"

    "Le nom de Kael s’affiche."

    call messenger_play("kael", "kael", [
        ("kael", "Tu es réveillé ?"),
        ("noam", "Oui. J’ai entendu l’annonce."),
        ("kael", "Tu comptes aller au vote ?"),
        ("noam", "Je ne sais pas encore."),
        ("kael", "Alors décide vite. C’est probablement notre meilleure occasion pour regarder les caméras."),
        ("noam", "Tu veux faire ça pendant que tout le monde est au Conclave ?"),
        ("kael", "Oui. La salle d’observation sera vide et les archives du huitième jour devraient enfin être déverrouillées."),
        ("kael", "Si quelqu’un a pris la photo de Léa, on pourra peut-être le voir."),
        ("noam", "Et si les images ont été supprimées ? On a déjà vu que certaines séquences pouvaient disparaître."),
        ("kael", "Alors on cherchera ce qui reste."),
        ("noam", "Et s’il ne reste rien ?"),
        ("kael", "Je ne sais pas."),
        ("noam", "Tu veux qu’on se retrouve avant ?"),
        ("kael", "Non. Attends l’annonce du rassemblement. Je serai près de la salle d’observation."),
        ("kael", "Viens seulement si tu es sûr."),
        ("noam", "Je viendrai."),
        ("kael", "Tu vas donc manquer le vote."),
        ("noam", "Oui. Pour une fois, je vais laisser aux autres la responsabilité de sauver le monde."),
        ("kael", "D’accord."),
    ]) from _call_messenger_j15_kael_matin

    "La conversation s’arrête là. Je garde pourtant la tablette contre moi encore quelques secondes."

    think "Je pourrais aller voter. Ce serait probablement la chose responsable à faire."
    think "Mais si je veux comprendre ce qui nous arrive, je n’aurai peut-être pas une autre occasion."

    jump _15_0_1_1_0_RATIONS


label _15_0_1_1_0_RATIONS:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "Une bonne heure passe sans que je quitte réellement le bord du lit. J’ai pris ma décision pour le vote, mais sortir de cette chambre reste une autre histoire."

    play sound "audio/sfx_knock.mp3" volume 0.9

    "Trois coups légers frappent soudain à la porte et me font relever la tête."

    noam inquiet "Oui ? Qui est là ?"

    pause 1.2

    "Personne ne répond."

    noam inquiet "Je sais qu’il y a quelqu’un."

    pause 1.0
    play sound "audio/sfx_knock.mp3" volume 0.7

    "Deux nouveaux coups, plus faibles cette fois, puis le silence revient."

    noam peur "Vous pouvez répondre, au moins !"

    "J’attends encore quelques secondes, suffisamment longtemps pour comprendre que la personne derrière la porte n’a aucune intention de me parler."
    "Je me lève finalement et ouvre d’un coup."

    play sound sfx_door volume 0.8

    "Il n’y a personne dans le couloir. À la place, un gros sac en toile repose contre le mur, rempli de conserves, de barres protéinées, de bouteilles d’eau et de rations emballées."
    "Il y en a beaucoup trop pour un seul repas. Probablement de quoi tenir plusieurs jours sans remettre les pieds à la cafétéria."

    noam hesitation "C’est quoi ce bordel...?"

    "Je jette un regard des deux côtés du couloir, mais celui ou celle qui a déposé le sac a déjà disparu."
    "Sur le dessus, une petite feuille pliée en deux dépasse entre deux paquets."

    "Je la prends."

    "\"Pour que tu puisses rester tranquille.\""

    "Je relis la phrase une seconde fois, puis une troisième, comme si une signature allait finir par apparaître entre les mots."

    think "Rester tranquille..."

    "Je ramène le sac dans la chambre et le pose sur le bureau. Le geste est attentionné, presque gentil, et c’est précisément ce qui me met mal à l’aise."

    think "Quelqu’un a pensé à moi. Quelqu’un s’est dit que je n’avais peut-être pas envie de descendre manger avec les autres."
    think "Mais cette personne n’a pas voulu rester trente secondes devant ma porte."

    "Je tourne la note entre mes doigts. Une partie de moi voudrait y voir une vraie attention ; l’autre n’arrive pas à oublier que personne n’a répondu quand j’ai demandé qui était là."

    noam triste "Vous auriez quand même pu me parler..."

    "Je laisse échapper un rire sans joie et ouvre l’une des barres protéinées."

    think "Peut-être qu’ils ne veulent pas m’éviter. Peut-être qu’ils pensent juste me rendre service."
    think "Et peut-être que je suis devenu tellement méfiant que je transforme tout en rejet."

    "Je prends une bouchée sans vraiment avoir faim, puis replie la note au lieu de la froisser."

    think "Je ne sais même plus quelle interprétation est la pire."

    pause 2.0

    call KD_ROUTE_J15_ELEN from _call_optional_kd_route_j15_elen
    call OFFER_DAILY_EXPLORATION(
        "_15_0_1_1_0_COULOIR", 1,
        ["observation", "archive", "dortoir"],
        _("Rejoindre Kael à l'Observation"), "observation"
    ) from _call_offer_exploration_j15


label _15_0_1_1_0_COULOIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_86
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_tense_meeting.mp3" fadein 2.0

    "Lorsque je sors enfin, des voix résonnent déjà au bout du couloir. Le groupe est en train de se rassembler avant de partir vers le Conclave, exactement comme Kael l’avait prévu."

    "Ma tablette vibre."

    call messenger_play("kael", "kael", [
        ("kael", "Tu es sorti ?"),
        ("noam", "Oui. Ils sont encore devant le couloir principal."),
        ("kael", "Attends qu’ils partent. Je suis déjà près de la salle d’observation."),
        ("noam", "J’arrive dès que je peux."),
    ]) from _call_messenger_j15_kael_couloir

    "Je range la tablette et commence à reculer pour reprendre un autre passage."

    iris inquiet "Noam ?"

    "Je m’arrête aussitôt. Sa voix est trop proche pour faire semblant de ne pas avoir entendu."

    mara agace "Ah bah voilà. Je me demandais combien de temps tu comptais rester caché derrière le mur."
    lysa blase "Technique impressionnante. Encore cinq secondes et on aurait tous oublié qu’il était là."

    "Je reviens lentement dans leur champ de vision."

    $ showGroup([
        ("mara", "colere", 0.08),
        ("iris", "inquiet", 0.23),
        ("lysa", "blase", 0.38),
        ("tomas", "raison", 0.53),
        ("ryn", "colere", 0.68),
        ("sael", "mefiant", 0.84),
    ])
    pause 0.5

    noam hesitation "Salut."

    mara agace "Non, attends, tu peux pas juste sortir d’un coin, dire 'salut' et espérer que tout le monde trouve ça normal."
    noam fatigue "Je n’espérais pas vraiment ça."

    iris inquiet "Tu viens avec nous ?"

    "Je croise son regard. Elle connaît déjà probablement la réponse."

    noam triste "Non."

    "Le groupe se tait aussitôt. Elen, un peu plus loin, baisse les yeux tandis que Ryn se raidit."

    ryn desaccord "Non parce que tu peux pas, ou non parce que t’as décidé qu’on pouvait se démerder sans toi ?"

    noam culpabilite "J’ai décidé de ne pas venir."

    mara colere "Sérieusement ? Aujourd’hui ?"
    mara agace "On vote sur l’accès aux archives du monde entier et toi, tu choisis précisément ce jour-là pour nous faire ta disparition mystérieuse ?"

    iris colere "Mara, tu crois vraiment que lui rentrer dedans va changer quelque chose ?"
    mara colere "J’en sais rien, Iris ! Mais j’en ai un peu marre qu’on fasse tous comme si c’était normal."

    tomas inquiet "Elle n’a pas complètement tort. Sans vouloir te faire la morale, Noam, chaque absence réduit encore nos possibilités de savoir ce que pense réellement le groupe avant le vote."
    tomas raison "Et dans un système où l’unanimité compte... enfin, tu connais déjà le problème. Je vais pas te refaire un cours."
    iris blase "Merci. J'ai eu peur que tu nous ressortes le tableau des abstentions."
    tomas inquiet "Je n'ai pas de tableau des abstentions."
    lysa blase "Tu as dit ça beaucoup trop vite."
    tomas inquiet "J'ai un tableau des votes. C'est différent."
    mara agace "Ah, tout va bien alors. Le jour où Noam disparaît, Tomas nous fait des statistiques."
    noam fatigue "Je suis encore là, je vous signale."
    lysa blase "Pour l'instant. Tu t'entraînes plutôt bien à disparaître."

    noam raison "Je le connais. Et je ne vous demande pas de dire que mon choix est raisonnable."
    noam culpabilite "Je sais très bien ce que ça implique."

    ryn colere "Alors pourquoi ?"

    noam hesitation "Parce qu’il y a quelque chose que je dois vérifier."

    ryn colere "Encore tes histoires de couloir ?"

    iris inquiet "Ryn..."

    ryn colere "Non, je veux comprendre. On a tous des trucs qui nous bouffent depuis des jours, mais on est quand même là."
    ryn desaccord "Alors si lui se barre pendant le vote, j’aimerais au moins savoir pourquoi."

    noam raison "Je ne peux pas tout expliquer maintenant."

    mara rire "Ah, parfait. Donc en plus on a droit au mystère. Ça manquait à l’ambiance."

    lysa blase "À sa décharge, notre quotidien ressemble déjà à une mauvaise émission où personne n’a le droit de connaître le scénario."

    "Une voix calme arrive derrière moi."

    kael fatigue "On devrait y aller."

    "Je me retourne. Kael s’est approché sans bruit et s’arrête à côté de moi. Ryn comprend immédiatement."

    ryn surpris "Ah. D’accord. Vous êtes deux."
    ryn colere "C’est quoi le plan ? Vous disparaissez ensemble pendant que nous on vote et on fait semblant de ne rien voir ?"

    kael calme "Ce n’est pas ton problème."

    ryn colere2 "Si ça peut foutre le vote en l’air, si, ça devient mon problème."

    kael fatigue "Tu veux vraiment qu’on ait cette discussion ici ?"
    ryn colere "Moi, j’ai aucun problème avec ça."

    kael calme "Évidemment."

    "Ryn fait un pas vers lui. Sael lui attrape le bras avant qu’il n’aille plus loin."

    sael mefiant "Ryn. Laisse."
    ryn colere "Il se fout de ma gueule."
    sael raison "Et tu vas faire quoi ? Le frapper avant un vote sur la transparence ? Très cohérent."

    "Ryn serre la mâchoire, puis finit par reculer d’un demi-pas."

    ryn fatigue "Fait chier..."

    nyra raison "Noam, je vais seulement te demander une chose."

    "Nyra s’avance légèrement, sans colère apparente."

    nyra raison "Ne présente pas ça comme quelque chose qui t’arrive. C’est une décision. Tu peux avoir de bonnes raisons, mais elle reste à toi."
    nyra raison "Je ne te demande pas de te justifier devant tout le monde. Mais tu comptes prévenir quelqu'un si tes recherches tournent mal ?"
    noam hesitation "Kael sera avec moi."
    nyra raison "Alors assure-toi qu'il sache quoi faire si vous devez vous séparer."
    ryn colere "Tu viens de lui donner un plan pour sécher le vote ?"
    nyra raison "Je préfère un mauvais plan avec un moyen de revenir qu'une disparition dont personne ne sait rien."
    iris inquiet "Ça ne veut pas dire qu'on approuve."
    noam fatigue "J'avais compris au deuxième reproche."
    mara agace "Seulement au deuxième ? Il s'améliore."

    "Nyra ne hausse jamais le ton. Pourtant, sa question me reste en tête : si quelque chose tourne mal, est-ce que j'ai seulement prévu comment prévenir les autres ?"

    noam determine "D’accord. Je choisis de ne pas venir au vote."
    noam culpabilite "Et si ça a des conséquences, je les assumerai."

    iris inquiet "Tu dis toujours ça comme si tout devait forcément te retomber dessus."
    noam triste "Peut-être que c’est plus simple comme ça."

    lysa blase "Non. C’est juste plus pratique pour culpabiliser ensuite."

    "Je tourne la tête vers elle. Lysa hausse simplement les épaules."

    lysa blase "Quoi ? Tu voulais des échanges sincères."

    mara agace "Pour une fois qu’elle parle comme une personne normale, profite."
    lysa taquin "Merci Mara, ton soutien me bouleverse."

    "Même Iris laisse échapper un bref souffle amusé, mais la tension ne disparaît pas."

    elen inquiet "Noam... Kael... je sais pas ce que vous allez chercher, et j’imagine que vous voulez pas le dire."
    elen triste "Mais revenez, d’accord ? J’ai pas envie qu’on commence à perdre des gens parce qu’on n’arrive plus à se parler."

    kael triste "On reviendra."
    noam triste "Oui."

    iris colere "Et toi, tu manges vraiment quelque chose avant. La barre que t’as dû avaler tout seul dans ta chambre, ça compte pas comme un repas."
    noam hesitation "Comment tu sais que j’ai mangé une barre ?"
    iris taquin "Parce que t’as encore l’emballage qui dépasse de ta poche, Sherlock."

    mara rire "Magnifique. On est au bord d’un nouveau drame collectif et elle vérifie son goûter."
    iris colere "Va te faire foutre, Mara."
    mara rire "Voilà, là je te reconnais."

    "Kael me fait signe de le suivre. Cette fois, personne ne nous retient."
    "Lorsque nous nous éloignons, je sens encore les regards dans mon dos, mais je ne cherche pas à savoir lesquels sont inquiets et lesquels sont en colère."

    think "J’ai choisi de ne pas y aller."
    think "Maintenant, il faut que ce choix serve à quelque chose."

    jump _15_0_1_1_0_RENCONTRE_KAEL


label _15_0_1_1_0_RENCONTRE_KAEL:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_87
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5

    "La salle d’observation est vide comme prévu. Une lumière bleutée tombe des écrans sur les consoles tandis que Kael referme la porte derrière nous."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    "Il se dirige immédiatement vers le terminal, mais je reste debout quelques secondes derrière lui."

    noam hesitation "Kael... pourquoi moi ?"
    kael reflechit "Quoi ?"
    noam raison "Tu sais te servir du terminal tout seul."
    kael fatigue "Ouais. Et si l'écran me montre quelque chose que j'ai pas envie de voir, je fais quoi ? Je m'en parle à moi-même ?"
    noam taquin "Avec moi, tu risques pas d'être mieux servi."
    "Kael s'assoit. Il garde les mains au-dessus du clavier sans y toucher."
    kael triste "Les autres commencent à m'éviter. Je peux pas vraiment leur en vouloir."
    noam inquiet "Tu le sais pas, ça."
    kael fatigue "Si. Mais j'ai pas envie d'en faire une discussion."
    "Il ouvre les archives."
    kael reflechit "J'ai regardé la photo de Léa avant de dormir. J'en suis sûr."
    noam hesitation "La photo que tu gardais sous l'oreiller ?"
    kael calme "Ouais."
    noam raison "D'accord. On regarde."
    kael fatigue "Et si je commence à raconter n'importe quoi, tu me le dis."
    noam taquin "J'avais déjà prévu."


    call play_stat_dialogue("j15") from _call_play_stat_dialogue_14

    kael "Je suis rentré vers 19h30. La photo était encore là."
    "Il affiche les ouvertures de porte. Une liste d'heures défile."
    noam reflexion "Tu comptes vraiment vérifier chaque entrée ?"
    kael reflechit "Ça m'aide à savoir où je suis."
    noam fatigue "On est dans la salle d'observation."
    kael sourire "Merci, Noam."
    "Il parcourt rapidement les données. Les horaires correspondent à ce dont il se souvient, jusqu'au retour du soir."
    kael reflechit "Après 19h28, plus d'ouverture de porte enregistrée."
    noam inquiet "Mais la photo a disparu."
    kael fatigue "Ouais."
    "Une coupure d'image apparaît sur la vidéo."
    noam surpris "Attends. Là."
    kael inquietude "Je l'ai vue."
    "Kael revient en arrière. L'horodatage indique 21h17."
    noam reflexion "T'étais où ?"
    kael fatigue "Avec Elen, je crois. À la salle de repos. J'étais pas seul toute la soirée."
    noam inquiet "On peut lui demander."
    kael inquietude "Après. Regarde d'abord ce qu'il y a là."


    jump _15_0_1_1_0_VIDEO_KAEL


label _15_0_1_1_0_VIDEO_KAEL:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    "Kael repasse la séquence à vitesse normale. Cette fois, nous ne quittons plus l’écran des yeux."
    "À 21h17, la porte de sa chambre s’ouvre."

    "Kael entre."

    tuto "Utilise la timeline, le ralenti et l'avance image par image. Inspecte directement les zones importantes."
    call investigation_video_run("kael_photo", "bg_chambre", False) from _call_investigation_video_kael

    kael surpris "... Quoi ?"
    "Sur l'écran, quelqu'un entre. Il a la même démarche que Kael."
    "Kael pose brusquement la main sur le bouton de pause."
    noam inquiet "Kael ?"
    kael inquietude "Non. Attends..."
    "Il recule de deux images. Le garçon filmé décroche la photo de Léa."
    kael inquietude "TOUCHE PAS À ÇA !"
    "Je sursaute. Il vient de hurler sur son propre visage."
    noam inquiet "C'est une vidéo. Il peut pas t'entendre."
    kael fatigue "Je sais. Je sais, putain..."
    "Il essaie d'éteindre l'écran, puis s'arrête."
    kael inquietude "Relance. Non, attends. Je veux pas..."
    noam hesitation "On peut arrêter."
    kael inquietude "Non !"
    "Le garçon glisse la photo dans sa veste et se tourne vers la caméra."


    play sound "audio/sfx_glitch.mp3" volume 0.9
    with glitch_diss

    scene bg_observation at adaptive_fullscreen with flash_red

    $ showGroup([
        ("noam", "surpris", 0.30),
        ("kael", "surpris", 0.60),
    ])

    kael surpris "Remets-la."
    noam hesitation "T'es sûr ?"
    kael inquietude "Je t'ai dit de remettre la vidéo."
    "Je la relance. Kael ne regarde pas tout de suite. Il attend que le personnage approche de la photo."
    kael triste "C'est ma veste. C'est comme ça que je la tiens."
    noam reflexion "Quelqu'un pourrait avoir copié..."
    kael inquietude "Même ma façon de marcher ?!"
    "Il se lève, recule, puis revient devant le terminal."
    kael triste "J'ai jamais pris cette photo, Noam. Je peux oublier mon dîner, pas ça."
    noam fatigue "D'accord. Je te crois."
    kael inquietude "Alors pourquoi je suis là-dessus ?"
    "Il tape du doigt sur son double jusqu'à laisser une marque sur l'écran."
    noam reflexion "Attends. On dirait qu'il dit quelque chose."
    kael surpris "Quoi ?"
    noam hesitation "Peut-être « désolé ». Je suis pas sûr."
    kael fatigue "Formidable. Je vole ma photo, puis je m'excuse. Tout va bien."
    noam inquiet "Il y a peut-être quelqu'un qui te ressemble. Ou... je sais pas."
    kael triste "Moi non plus."
    "Un silence passe. Kael tire une chaise et s'y laisse tomber."
    kael calme "On vérifie le fichier. Si c'est truqué, j'ai besoin de le savoir."
    noam raison "Ouais. On va commencer par ça."


    jump _15_0_1_1_0_ARCHIVES_CROISEES


label _15_0_1_1_0_ARCHIVES_CROISEES:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.5

    $ showGroup([
        ("noam", "hesitation", 0.30),
        ("kael", "inquietude", 0.60),
    ])

    "Kael ouvre les contrôles du fichier. Je le laisse travailler, jusqu'à ce qu'il se frotte les yeux pour la troisième fois."
    noam inquiet "Kael, t'as mal ?"
    kael fatigue "Non. J'ai juste une vidéo qui me donne envie de jeter le terminal par la fenêtre."
    noam fatigue "On est dans l'espace. Ce serait un gros problème."
    kael calme "J'y ai pensé."
    "Il vérifie la source, l'heure et les traces de modification."
    kael reflechit "Rien. La caméra correspond. Aucune retouche enregistrée."
    noam reflexion "Donc c'est vrai ?"
    kael fatigue "J'ai dit « aucune retouche ». Pas « c'est vrai ». Tu peux me laisser cette différence ?"
    noam hesitation "Ouais. Pardon."
    "Il relance l'image au ralenti. Son double serre la photo exactement comme lui l'avait fait en me la montrant."
    kael triste "Même ça..."
    "Il ferme brusquement la vidéo."
    noam surpris "Kael ?"
    kael fatigue "J'en peux plus de me regarder voler la seule photo de ma sœur."
    noam raison "On peut vérifier les autres caméras."
    kael reflechit "Déjà fait. L'entrée est dans un angle mort."
    noam fatigue "Évidemment."
    "Il reste les yeux fixés sur l'écran noir."
    kael inquietude "La silhouette que t'as vue dans le couloir... tu l'as vraiment vue ?"
    noam hesitation "J'étais malade. J'ai vu un mouvement. Je peux pas te dire si c'était quelqu'un."
    kael fatigue "Alors on a rien."
    noam desaccord "On a la vidéo."
    kael triste "Ouais. Justement."
    "Il récupère sa tablette."
    noam inquiet "Tu vas où ?"
    kael fatigue "Dans ma chambre. J'ai besoin de chercher quelque chose que je peux toucher."
    noam raison "Vas-y doucement. Je te rejoins."
    kael calme "Merci."
    hide kael with dissolve
    "Il sort sans refermer la vidéo. Je reste seul avec le visage figé sur l'écran."


    jump _15_0_1_1_0_CHAMBRE_NOAM_VIDEO


label _15_0_1_1_0_CHAMBRE_NOAM_VIDEO:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "Je reste seul devant les écrans après son départ. La vidéo de sa chambre est toujours ouverte et son visage figé me regarde depuis le moniteur."

    think "Si je veux éviter de faire exactement ce que je reproche aux autres, je dois vérifier avant de tirer une conclusion."

    "Je ferme son archive et entre mon propre code d’accès."

    think "Nuit du 7 au 8. C’est là que le dessin a disparu."

    "Je remonte l’enregistrement jusqu’à un peu après deux heures du matin. Ma chambre apparaît à l’écran, sombre, avec mon corps endormi sur le lit."

    "À 2h14, la porte s’ouvre."

    tuto "La seconde archive utilise les mêmes commandes. Cette fois, ne suppose rien : vérifie chaque geste."
    call investigation_video_run("noam_room", "bg_cg041", True) from _call_investigation_video_noam

    $ unlock_gallery_image("bg_cg041")
    play sound "audio/sfx_static.mp3" volume 0.45
    scene bg_cg041 at adaptive_fullscreen with signal_stutter
    $ cam_move(fx=0.57, fy=0.42, z=1.13, t=6.0)

    "Kael entre."

    noam surpris "... Kael ?"

    "Je me penche vers l’écran. Il ne regarde presque pas autour de lui ; il va directement vers le bureau, repère le dessin de Juliette accroché au mur et le retire d’un coup sec."
    "Avant de partir, il tourne brièvement la tête vers mon lit, puis replie le dessin et ressort."

    "Je reste immobile devant l’écran, incapable de savoir si je suis surtout surpris, blessé ou simplement épuisé par une nouvelle chose impossible à comprendre."

    noam hesitation "Non... attends."

    "Je relance la séquence. Puis encore une fois, plus lentement."

    "Même heure. Même geste. Même visage."

    $ cam_reset(t=0.25)
    scene bg_observation at adaptive_fullscreen with memory_rip

    noam reflexion "C’est lui."

    "La colère arrive seulement après. D’abord comme une chaleur dans la poitrine, puis comme quelque chose de beaucoup plus brutal."

    think "Il vient de passer une heure à me dire qu’il ne comprend pas comment il peut apparaître sur une vidéo."
    think "Et pendant tout ce temps, il savait peut-être très bien qu’il était venu dans ma chambre."

    noam colere "Putain..."

    "Je repense à sa façon de me demander de lui faire confiance, à sa photo disparue, à sa peur de passer pour un menteur."

    think "Et s’il m’a raconté tout ça pour me faire regarder ailleurs ?"
    think "Non. Attends. Je ne sais pas encore."

    "Je force la vidéo à revenir sur son visage et cherche quelque chose qui prouverait que ce n’est pas lui. Une coupure, un artefact, n’importe quoi."

    "Je ne trouve rien."

    noam colere "Kael..."

    "Cette fois, je me lève."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_92
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Le couloir est presque désert ; le vote doit encore être en cours. Au bout du passage, j’aperçois Kael qui revient vers les dortoirs."

    noam colere "Kael !"

    $ showGroup([
        ("noam", "hesitation", 0.30),
        ("kael", "inquietude", 0.60),
    ])

    "Il se retourne, surpris par mon ton."

    kael surpris "Noam ?"

    "Je le rejoins rapidement. Je m’arrête juste devant lui, les poings serrés, en essayant encore de ne pas laisser la colère décider à ma place."

    noam colere "Je viens de regarder les archives de ma chambre."

    "Son visage se ferme légèrement."

    noam colere "Nuit du 7 au 8. Deux heures quatorze. Tu entres, tu prends le dessin de Juliette et tu repars."

    kael inquietude "Quoi ?"

    noam colere "Ne me réponds pas 'quoi'. Je t’ai vu."
    kael "Noam, je te jure que—"
    noam colere "Tu viens avec moi."

    "Je lui attrape le bras et l’entraîne vers la salle d’observation. Il résiste juste assez pour me faire comprendre qu’il n’apprécie pas le geste, mais il me suit."

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_93
    scene bg_observation at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "colere", 0.30),
        ("kael", "surpris", 0.60),
    ])

    "Je relance immédiatement la séquence et pointe l’écran."

    noam colere "Regarde."

    "Kael entre dans ma chambre, arrache le dessin de Juliette et repart."

    noam colere "Dis-moi que je vois mal. Dis-moi que c’est pas toi, que le fichier est faux, que n’importe quoi explique ça."
    noam colere "Mais ne me demande pas juste de te croire encore sans rien me donner."

    "Kael fixe l’écran sans répondre. Son visage perd progressivement toute couleur."

    kael triste "... Je ne me souviens pas de ça."

    noam colere "Évidemment."
    kael inquietude "Noam, écoute-moi."
    noam colere "Je t’ai écouté pendant une heure !"
    noam colere "Je t’ai défendu dans ma tête, j’ai cherché avec toi comment quelqu’un pouvait avoir trafiqué ta vidéo, et maintenant je découvre que tu es aussi celui qui est entré dans ma chambre !"

    kael fatigue "Je ne savais pas."
    noam colere "Comment je suis censé savoir si c’est vrai ?"

    "Ma voix monte malgré moi. Kael ne répond pas tout de suite, ce qui ne fait qu’alimenter ma colère."

    noam colere "C’était le dessin de ma petite sœur, Kael. Tu sais exactement ce que ça représente, puisque tu viens de passer la journée à chercher une photo de la tienne !"

    "Il baisse les yeux une seconde."

    kael triste "Je sais."

    noam colere "Alors explique-moi."

    jump _15_0_1_1_0_CONFRONTATION_KAEL


label _15_0_1_1_0_CONFRONTATION_KAEL:

    $ current_period = "Soir"

    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    $ showGroup([
        ("noam", "colere", 0.30),
        ("kael", "inquietude", 0.60),
    ])

    noam colere "Je veux juste une réponse claire. Est-ce que tu es entré dans ma chambre cette nuit-là ?"

    kael inquietude "Je ne m’en souviens pas."

    noam colere "C’est pas une réponse !"
    kael fatigue "C’est la seule que j’ai."

    noam colere "Alors où est mon dessin ?"
    kael "Je ne sais pas."
    noam colere "Et ta photo ?"
    kael fatigue "Je ne sais pas non plus."

    think "Je revois les images sur ma tablette. Je ne peux pas le laisser s'en sortir avec trois « je ne sais pas »."
    call refutation_run("j15_kael")
    if _return[0] == "success":
        call play_noam_interupt
        noam determine "Kael, j'ai vu la vidéo. Je ne dis pas que je comprends ce qui s'est passé. Mais arrête de faire comme si elle n'existait pas."
    else:
        kael fatigue "Je ne peux pas t'expliquer ce dont je ne me souviens pas."
    "Je fais un pas vers lui. Kael recule légèrement, puis son expression change."
    "Pas brutalement. C’est presque imperceptible : ses épaules se détendent, sa respiration ralentit et quelque chose disparaît de son regard."
    $ horror_audio_cut(duration=0.42, restore_volume=0.78)
    $ horror_music_slow(fadeout=0.25, fadein=0.55)
    $ cam_move(fx=0.60, fy=0.43, z=1.20, t=0.70)

    noam hesitation "... Kael ?"

    "Il relève les yeux vers moi avec un calme qui n’a rien à voir avec celui de quelques secondes plus tôt."
    $ danger_on()

    kael sourire "Noam... lâche un peu prise. Là, tu vas juste te faire du mal."

    "Je fronce les sourcils. Sa voix ressemble à celle de Kael, mais sa manière de poser les mots me donne immédiatement envie de reculer."

    noam inquiet "Qu’est-ce qui te prend ?"

    kael taquin "Rien. Au contraire, je crois qu’il est temps que tu comprennes enfin ce qui se passe."

    noam peur "De quoi tu parles ?"

    "Il sourit un peu plus. Ce n’est pas un sourire que je lui ai déjà vu."
    $ doppelganger_reveal(screamer=False, duration=0.92, restore_volume=0.78)
    $ investigation_add("doppelganger")

    kael sourire "Viens avec moi. Je vais tout t’expliquer."

    noam peur "Kael, arrête."

    play sound "audio/sfx_glitch.mp3" volume 1.0
    $ impact(intensity=14, duration=0.35, color="#5cd3ff")
    $ cam_reset(t=0.0)

    scene black with glitch_diss

    "Je n’ai pas le temps de comprendre ce qui vient de changer."

    pause 2.0

    scene bg_laboratoire at adaptive_fullscreen with flash_white
    $ shake(10, 0.25)
    pause 0.2

    scene black with dissolve

    "Une lumière blanche. Une pièce que je ne reconnais pas."

    $ unlock_gallery_image("bg_cg033")
    scene bg_cg033 at adaptive_fullscreen with flash_red
    $ shake(14, 0.30)
    pause 0.2

    scene black with dissolve
    $ danger_off()

    "Puis plus rien."

    call end_day("16") from _call_end_day_16
    jump _16_0_1_1_0_REVEIL_CHAMBRE
