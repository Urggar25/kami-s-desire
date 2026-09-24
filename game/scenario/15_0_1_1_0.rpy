label _15_0_1_1_0_REVEIL_CHAMBRE:
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

    play sound sfx_announce
    show screen kami_broadcast_ui
    pause 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Bonjour, mes chers représentants ! J’espère que vous avez tous passé une nuit suffisamment reposante pour prendre une décision capable de bouleverser quelques millions de vies."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Le vote du jour aura lieu à 14h précises et concernera l’ouverture totale des archives d’[codex_dialogue_link('archive', 'ARCHIVE')] aux citoyens des districts."
    kami "Oui, oui, je sais ce que vous pensez : enfin un peu de transparence dans ce monde merveilleux !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Petit rappel pour ceux qui auraient miraculeusement oublié le Commandement V : toute information diffusée doit actuellement être validée par [codex_dialogue_link('archive', 'ARCHIVE')]."
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

    kael "Tu es réveillé ?"
    noam "Oui. J’ai entendu l’annonce."
    kael "Tu comptes aller au vote ?"

    "Je laisse mes doigts au-dessus de l’écran sans répondre tout de suite."

    noam "Je ne sais pas encore."
    kael "Alors décide vite. C’est probablement notre meilleure occasion pour regarder les caméras."
    noam hesitation "Tu veux faire ça pendant que tout le monde est au Conclave ?"
    kael "Oui. La salle d’observation sera vide et les archives du huitième jour devraient enfin être déverrouillées."
    kael "Si quelqu’un a pris la photo de Léa, on pourra peut-être le voir."

    "Je relis sa dernière phrase. Depuis qu’il m’a parlé de cette photo, quelque chose a changé chez lui ; il parle encore peu, mais on sent que toute son attention s’est resserrée autour de cette seule question."

    noam reflexion "Et si les images ont été supprimées ? On a déjà vu que certaines séquences pouvaient disparaître."
    kael "Alors on cherchera ce qui reste."
    noam "Et s’il ne reste rien ?"

    pause 1.0

    kael "Je ne sais pas."

    "La réponse est courte, mais elle suffit à me faire comprendre qu’il y pense depuis longtemps."

    noam "Tu veux qu’on se retrouve avant ?"
    kael "Non. Attends l’annonce du rassemblement. Je serai près de la salle d’observation."
    kael "Viens seulement si tu es sûr."

    noam hesitation "Je viendrai."
    kael "Tu vas donc manquer le vote."

    "Je baisse les yeux vers mes mains."

    noam fatigue "Oui. Pour une fois, je vais laisser aux autres la responsabilité de sauver le monde."

    pause 1.0

    kael "D’accord."

    "La conversation s’arrête là. Je garde pourtant la tablette contre moi encore quelques secondes."

    think "Je pourrais aller voter. Ce serait probablement la chose responsable à faire."
    think "Mais si je veux comprendre ce qui nous arrive, je n’aurai peut-être pas une autre occasion."

    jump _15_0_1_1_0_RATIONS


label _15_0_1_1_0_RATIONS:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "Une bonne heure passe sans que je quitte réellement le bord du lit. J’ai pris ma décision pour le vote, mais sortir de cette chambre reste une autre histoire."

    play sound sfx_knock volume 0.9

    "Trois coups légers frappent soudain à la porte et me font relever la tête."

    noam inquiet "Oui ? Qui est là ?"

    pause 1.2

    "Personne ne répond."

    noam inquiet "Je sais qu’il y a quelqu’un."

    pause 1.0
    play sound sfx_knock volume 0.7

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

    jump _15_0_1_1_0_COULOIR


label _15_0_1_1_0_COULOIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_86
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_debate.mp3" fadein 2.0

    "Lorsque je sors enfin, des voix résonnent déjà au bout du couloir. Le groupe est en train de se rassembler avant de partir vers le Conclave, exactement comme Kael l’avait prévu."

    "Ma tablette vibre."

    kael inquietude "Tu es sorti ?"
    noam inquiet "Oui. Ils sont encore devant le couloir principal."
    kael fatigue "Attends qu’ils partent. Je suis déjà près de la salle d’observation."
    noam "J’arrive dès que je peux."

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

    "Sa phrase me fait plus mal que les reproches de Mara ou de Ryn, probablement parce qu’elle ne cherche pas à me blesser."

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

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_87
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5

    "La salle d’observation est vide comme prévu. Une lumière bleutée tombe des écrans sur les consoles tandis que Kael referme la porte derrière nous."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    "Il se dirige immédiatement vers le terminal, mais je reste debout quelques secondes derrière lui."

    noam hesitation "Kael... avant qu’on commence, je peux te demander quelque chose ?"
    kael calme "Vas-y."
    noam "Pourquoi moi ?"

    "Il pose les mains sur le clavier sans taper."

    noam raison "Tu aurais pu faire ça tout seul. Pourquoi tu m’as demandé de venir ?"

    kael reflechit "Parce que si je trouve quelque chose de mauvais, je préfère que quelqu’un d’autre le voie aussi."
    noam "C’est pas exactement ce que je demandais."

    "Kael souffle doucement et regarde l’écran plutôt que moi."

    kael fatigue "Tu es le seul qui ne m’a pas encore regardé comme si j’avais déjà fait quelque chose de travers."
    noam "Les autres ne te détestent pas."
    kael triste "Je sais."
    noam inquiet "Alors qu’est-ce qui te dérange ?"

    kael fatigue "Qu’ils aient tous une bonne raison de rester à distance."
    kael "Je les comprends. C’est justement ça qui me fatigue."

    "Il finit par s’asseoir et déverrouille le terminal."

    kael reflechit "Si on trouve quelqu’un sur la vidéo, au moins on aura un fait. Pas une impression, pas un souvenir bancal."
    noam reflexion "Et si la vidéo est trafiquée ?"
    kael calme "On le vérifiera."
    noam "Tu sais faire ça ?"
    kael sourire "Assez pour repérer une modification grossière. Si quelqu’un a fait mieux, ce sera plus compliqué."

    "Une arborescence d’archives apparaît à l’écran. Kael sélectionne sa chambre, puis le huitième jour."

    kael "Je suis rentré vers 19h30. La photo était encore là."
    noam "Tu en es sûr ?"
    kael calme "Oui. Je la regarde presque tous les soirs."

    "Je tourne légèrement la tête vers lui, surpris."

    noam hesitation "Tu ne m’avais jamais dit ça."
    kael calme "Il n’y avait aucune raison de le dire."

    "Il fait défiler le journal d’accès de la porte."

    kael reflechit "08h12, sortie. 08h17, retour. 09h43, sortie... 13h06, retour."
    noam reflexion "Ça correspond à tes déplacements ?"
    kael "Oui. À 13h, je suis revenu chercher ma tablette. Ensuite je suis ressorti à 14h02."
    noam "Et après ?"
    kael "Retour à 19h28. Puis plus aucune ouverture enregistrée jusqu’à la nuit."

    "Je pointe la ligne du doigt."

    noam inquiet "Donc si quelqu’un est entré après toi, il n’a pas utilisé la porte normalement."
    kael calme "Ou le journal a été modifié."

    "Il lance la vidéo et accélère l’enregistrement. La pièce défile presque vide pendant plusieurs heures."

    noam "Attends."

    "Une micro-coupure vient de traverser l’image. Kael revient immédiatement en arrière."

    kael inquietude "Je l’ai vue aussi."
    noam reflexion "Quelle heure ?"
    kael "21h17."
    noam inquiet "Tu étais où ?"

    "Il réfléchit quelques secondes, les yeux fermés."

    kael fatigue "Probablement à la salle de repos. J’étais avec Elen une partie de la soirée."
    noam "Probablement ?"
    kael fatigue "C’était il y a une semaine, Noam. Je ne peux pas te réciter chaque minute."

    "Je hoche la tête. Il a raison, même si cette imprécision semble l’agacer lui-même."

    kael inquietude "On continue."

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

    kael surpris "... Quoi ?"

    "Le garçon filmé traverse la pièce sans hésiter, se dirige vers le mur et s’arrête devant la photo de Léa."
    "Il la décroche avec précaution, la garde un moment entre ses mains, puis la glisse dans sa veste."

    kael inquietude "Non..."

    "Je tourne la tête vers le vrai Kael. Il ne cligne presque plus des yeux."

    noam inquiet "C’est bien toi ?"
    kael fatigue "Je..."

    "Sur l’écran, son double se tourne vers la caméra et regarde directement l’objectif."

    play sound sfx_glitch volume 0.9
    with hpunch

    centered "{color=#FF0000}FILE DELETED{/color}"

    scene bg_observation at adaptive_fullscreen with vpunch

    $ showGroup([
        ("noam", "surpris", 0.30),
        ("kael", "surpris", 0.60),
    ])

    kael surpris "Remets-la."
    noam "Kael..."
    kael inquietude "Remets la vidéo."

    "Je la relance. La même scène recommence, intacte jusqu’au moment où le regard se pose sur la caméra."

    kael fatigue "C’est moi."
    noam hesitation "Ça te ressemble, oui."
    kael inquietude "Non. C’est pas juste quelqu’un qui me ressemble. C’est ma veste, ma façon de marcher... tout."

    "Il serre les mains contre ses genoux. Sa voix reste basse, mais elle tremble légèrement."

    kael triste "Je n’ai pas pris cette photo."
    noam raison "Tu es sûr de ton souvenir ?"
    kael "Oui."
    noam reflexion "Même après une semaine ?"

    "Kael tourne enfin la tête vers moi."

    kael triste "Je peux oublier où j’étais à 21h17. Je peux oublier ce que j’ai mangé ou à qui j’ai parlé."
    kael triste "Je n’oublierais pas avoir décroché la seule photo de ma sœur."

    "Je n’ai rien à répondre à ça."

    kael inquietude "Relance encore."

    "Je le fais une troisième fois. En ralentissant l’image, je remarque que ses lèvres bougent juste avant qu’il range le cadre."

    noam reflexion "Attends... il parle."
    kael surpris "Tu comprends ce qu’il dit ?"
    noam hesitation "Pas vraiment. Peut-être 'désolé'... ou quelque chose qui ressemble à ça. Je veux pas inventer."

    kael fatigue "Pourquoi je m’excuserais ?"
    noam "Je ne sais pas."
    kael triste "Pourquoi je volerais ma propre photo pour ensuite m’excuser devant une caméra ?"

    "Il se lève, fait deux pas dans la pièce, puis revient aussitôt devant l’écran comme s’il était incapable de s’en éloigner."

    kael inquietude "Soit quelqu’un a trafiqué cette vidéo, soit j’ai un trou de mémoire que je ne peux pas expliquer."
    kael fatigue "Et j’aime aucune des deux options."

    noam raison "Il y en a peut-être une troisième."
    kael "Laquelle ?"

    "Je pense immédiatement à la silhouette croisée dans le couloir, puis au dessin de Juliette disparu de ma chambre. Les éléments se rapprochent dans ma tête sans former quelque chose de cohérent."

    noam hesitation "Je sais pas encore."
    kael inquietude "Tu viens de penser à quelque chose."
    noam "À mon dessin."

    "Il reste silencieux."

    noam reflexion "Le dessin de Juliette a disparu aussi. Et depuis, j’arrête pas de me demander si j’ai raté quelque chose."
    noam fatigue "Si toi tu peux apparaître sur une vidéo sans te souvenir de ce que tu fais... alors je sais même plus ce que je peux considérer comme fiable."

    kael reflechit "Tu crois que tu as pu enlever ton propre dessin ?"
    noam hesitation "J’en sais rien. Et c’est justement ça qui me fait peur."

    "Kael regarde l’écran une nouvelle fois."

    kael calme "On vérifie le fichier avant de conclure quoi que ce soit."
    noam raison "Oui. Pas d’hypothèse avant d’avoir épuisé le plus simple."

    "Pour la première fois depuis le début de la vidéo, il acquiesce sans hésiter."

    jump _15_0_1_1_0_ARCHIVES_CROISEES


label _15_0_1_1_0_ARCHIVES_CROISEES:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.5

    $ showGroup([
        ("noam", "hesitation", 0.30),
        ("kael", "inquietude", 0.60),
    ])

    "Kael ouvre plusieurs fenêtres de contrôle et compare les informations du fichier avec les données conservées par le système. Je le laisse travailler quelques minutes sans l’interrompre."

    noam reflexion "Tu trouves quelque chose ?"
    kael reflechit "Rien d’évident."
    noam "Ça veut dire quoi, rien d’évident ?"

    kael calme "Le fichier a été créé au bon moment. La source correspond à la caméra de ma chambre. L’empreinte est valide et je ne vois aucune modification enregistrée après coup."
    noam inquiet "Donc la vidéo est authentique ?"
    kael reflechit "Je dis seulement que je ne vois pas de trace de montage. C’est pas exactement la même chose."

    "Il vérifie encore une fois les données, puis s’arrête."

    kael fatigue "Mais si quelqu’un l’a trafiquée, il a fait ça proprement. Beaucoup trop proprement."

    "Il relance l’image au ralenti. Sur l’écran, son propre visage se penche sur la photo de Léa avec une douceur qui rend la scène encore plus difficile à regarder."

    kael triste "Je reconnais même la façon dont je la tiens."
    noam inquiet "Kael..."
    kael triste "C’est ça le pire. Je pourrais me raconter que quelqu’un s’est déguisé, que l’image est fausse, que j’ai mal vu... mais plus je regarde, plus je me reconnais."

    "Il se frotte le visage et reste quelques secondes comme ça, les coudes sur les genoux."

    kael culpabilite "Et si c’était vraiment moi ?"
    noam raison "Alors il faut comprendre pourquoi tu ne t’en souviens pas. Ça ne prouve pas que tu as voulu la faire disparaître."
    kael triste "Ça change pas le fait qu’elle a disparu."

    noam "Non."

    "Je ne cherche pas à le rassurer davantage. Rien de ce que je pourrais dire ne rendrait la photo moins absente."

    kael reflechit "On pourrait regarder les autres caméras autour du couloir."
    noam "Bonne idée."

    "Il secoue la tête presque aussitôt."

    kael fatigue "J’ai déjà essayé. Il y a un angle mort à cet endroit et aucune autre caméra ne couvre l’entrée de ma chambre assez clairement."
    noam desaccord "Donc on n’a que ça."
    kael "Oui."

    "Un silence s’installe. Puis Kael tourne lentement la tête vers moi."

    kael inquietude "Quand tu as parlé de la silhouette dans le couloir l’autre jour... tu avais vu quoi exactement ?"

    noam hesitation "Je ne sais pas."
    kael "Tu l’as vue ou pas ?"
    noam inquiet "J’ai vu quelque chose. Une silhouette, un mouvement... mais j’étais fiévreux et j’ai commencé à douter dès le lendemain."
    noam fatigue "Je pourrais te dire que c’était quelqu’un, sauf que je serais incapable de te dire qui. Et je pourrais te dire que j’ai halluciné, sauf que j’en suis pas sûr non plus."

    kael reflechit "Donc on a deux souvenirs qu’on ne peut pas vérifier et une vidéo qui montre quelque chose qui ne devrait pas exister."
    noam taquin "Dit comme ça, c’est très rassurant."

    "Kael laisse échapper un souffle qui ressemble presque à un rire, mais il disparaît aussitôt."

    kael triste "Je dois retrouver la photo."
    noam raison "On va la retrouver. Mais pars pas seul en courant sans réfléchir."
    kael calme "Je vais juste vérifier ma chambre."
    noam "Kael..."
    kael fatigue "Noam, j’ai besoin de chercher quelque chose de concret. Là, je suis juste assis à regarder mon propre visage me dire que ma mémoire vaut rien."

    "Je comprends trop bien ce qu’il veut dire pour insister."

    noam fatigue "D’accord. Je te rejoins après."
    kael "Merci."

    hide kael with dissolve

    "Il quitte la salle rapidement, sans courir, mais avec cette façon de marcher qui dit clairement qu’il ne pense déjà plus à rien d’autre."

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

    "Kael entre."

    noam surpris "... Kael ?"

    "Je me penche vers l’écran. Il ne regarde presque pas autour de lui ; il va directement vers le bureau, repère le dessin de Juliette accroché au mur et le retire d’un coup sec."
    "Avant de partir, il tourne brièvement la tête vers mon lit, puis replie le dessin et ressort."

    "Je reste immobile devant l’écran, incapable de savoir si je suis surtout surpris, blessé ou simplement épuisé par une nouvelle chose impossible à comprendre."

    noam hesitation "Non... attends."

    "Je relance la séquence. Puis encore une fois, plus lentement."

    "Même heure. Même geste. Même visage."

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

    "Je fais un pas vers lui. Kael recule légèrement, puis son expression change."
    "Pas brutalement. C’est presque imperceptible : ses épaules se détendent, sa respiration ralentit et quelque chose disparaît de son regard."

    noam hesitation "... Kael ?"

    "Il relève les yeux vers moi avec un calme qui n’a rien à voir avec celui de quelques secondes plus tôt."

    kael sourire "Noam... lâche un peu prise. Là, tu vas juste te faire du mal."

    "Je fronce les sourcils. Sa voix ressemble à celle de Kael, mais sa manière de poser les mots me donne immédiatement envie de reculer."

    noam inquiet "Qu’est-ce qui te prend ?"

    kael taquin "Rien. Au contraire, je crois qu’il est temps que tu comprennes enfin ce qui se passe."

    noam peur "De quoi tu parles ?"

    "Il sourit un peu plus. Ce n’est pas un sourire que je lui ai déjà vu."

    kael sourire "Viens avec moi. Je vais tout t’expliquer."

    noam peur "Kael, arrête."

    play sound sfx_glitch volume 1.0
    with vpunch

    scene black with dissolve

    "Je n’ai pas le temps de comprendre ce qui vient de changer."

    pause 2.0

    scene bg_laboratoire at adaptive_fullscreen with vpunch
    pause 0.2

    scene black with dissolve

    "Une lumière blanche. Une pièce que je ne reconnais pas."

    scene bg_cg033 at adaptive_fullscreen with vpunch
    pause 0.2

    scene black with dissolve

    "Puis plus rien."

    call end_day("16") from _call_end_day_16
    jump _16_0_1_1_0_REVEIL_CHAMBRE
