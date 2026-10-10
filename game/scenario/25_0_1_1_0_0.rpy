label _25_0_1_1_0_0_REVEIL:

    $ current_day = 25
    $ day_id = 25
    $ current_period = "Matin"

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    $ blink()

    scene bg_chambre at adaptive_fullscreen with dissolve

    "L'alarme n'a pas encore sonné quand j'ouvre les yeux. J'ai dormi sans lumière, sans me relever pour vérifier la porte."
    "Je reste un moment sous la couverture, à profiter de cette absence de problème, puis je tends le bras vers ma tablette. Le nouveau Commandement est toujours affiché."
    "J'ai enfin pu passer une nuit confortable. J'ai enfin pu me reposer."

    think "On a réussi."

    "Hier, Tomas m'a même remercié. Je devrais probablement lui demander de le refaire devant témoins, avant qu'il prétende avoir été mal compris."
    "Je récupère la tablette et me lève. Instinctivement, mes yeux se posent sur la bouche d'aération."
    "Je commence à enfiler mon tee-shirt quand quelque chose frotte dans le conduit."

    play sound sfx_creak volume 0.35

    think "Non, il faut que j'arrête avec ça. On s'en fiche, ok ?!"

    noam fatigue "Ça peut attendre. Dans quelques jours, je ne serai plus ici."

    stop music fadeout 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j25_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Je commence à avoir vraiment faim, direction la cafétéria !"

    jump _25_0_1_1_0_0_CAFETERIA


label _25_0_1_1_0_0_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j25_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "Quand j'entre dans la cafétéria, Elen me fait signe de les rejoindre. Julian raconte sa partie d'hier soir, mais les autres ne semblent pas avoir le même souvenir que lui."

    $ showGroup([
        ("mara", "taquin", 0.05),
        ("elias", "fatigue", 0.18),
        ("iris", "blase", 0.31),
        ("tomas", "fatigue", 0.44),
        ("elen", "content", 0.57),
        ("julian", "sourire", 0.70),
        ("ryn", "neutre", 0.83),
        ("noam", "neutre", 0.96),
    ])

    julian reflexion "J'avais presque remonté. Avec trente secondes de plus, je gagnais."

    elen rire "Mais on a joué jusqu'au bout ! Tu voulais qu'on te laisse continuer tout seul ?"

    mara taquin "Il aurait quand même trouvé le moyen de finir deuxième."

    julian agace "Très bien. La prochaine fois, tu joues contre moi."

    mara sourire "Si tu veux. Mais quand je gagne, tu me laisses aller me coucher."

    "Je récupère mon petit-déjeuner et m'assois près d'Iris. Elen pousse le plat de biscuits vers moi pendant que Julian cherche encore quelqu'un pour confirmer sa version."

    elen content "Tiens, il en reste."

    noam sourire "Merci. Vous êtes là depuis longtemps ?"

    iris blase "Assez pour entendre trois fois pourquoi il a perdu."

    julian agace "Vous me posez des questions et après vous vous plaignez que je réponde."

    elias fatigue "Personne t'a posé de question, Julian."

    "Mara éclate de rire. Julian finit par reprendre son café, et la conversation se calme le temps que je commence à manger."

    mara reflexion "Et toi, t'as réussi à dormir ?"

    noam neutre "Oui, plutôt bien. Je me suis même réveillé avant l'alarme."

    mara sourire "Ah, ça fait plaisir. Hier, on aurait dit que t'allais t'endormir dans ton assiette."

    noam taquin "Ça m'aurait évité une partie du débat."

    tomas fatigue "Vous avez fini de vous plaindre ? Le texte est passé."

    "Je tourne la tête vers Tomas. Il mange en consultant sa tablette, mais relève les yeux en voyant que je le regarde."

    tomas reflexion "Quoi ?"

    noam neutre "Rien. T'as l'air moins fatigué qu'hier."

    tomas neutre "Je le suis. J'ai dormi presque neuf heures."

    ryn reflexion "Donc aujourd'hui, si quelque chose te gêne, tu sauras nous dire quoi ?"

    tomas agace "Si vous me laissez finir mes phrases, ça devrait aider."

    ryn neutre "On t'a laissé parler."

    iris blase "Vous lui demandiez toutes les deux minutes s'il avait terminé."

    ryn fatigue "Bon, d'accord. On va pas refaire le débat."

    "Tomas referme le document sur sa tablette et reprend son petit-déjeuner. Il a encore les traits tirés, mais il suit la conversation et répond sans chercher ses mots."

    "Je me rends compte que j'attendais un oubli, une hésitation, quelque chose qui ressemble à hier. Je baisse les yeux vers mon plateau pour arrêter de le surveiller."

    elen content "Cet après-midi, on pourrait faire autre chose. Un jeu où on joue tous, cette fois."

    julian reflexion "Pourquoi pas. Qu'est-ce que tu proposes ?"

    elen sourire "Je vais regarder ce qu'il y a dans la salle commune. On avait trouvé des cartes, non ?"

    mara neutre "Oui, dans le meuble près du canapé."

    "Ils commencent à discuter des jeux disponibles. Mara se penche pour prendre un biscuit devant moi et je lui rapproche le plat sans y penser."

    "Ce n'est qu'après l'avoir fait que je remarque que sa présence ne m'a pas crispé."

    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Bonjour, mes chers représentants. Après votre belle unanimité d'hier, voyons si vous pouvez recommencer."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "La prochaine proposition tirée au sort est la suivante : toute personne privée de liberté doit être informée du motif de sa détention et disposer d'un moyen de la contester."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu au jour vingt-sept. Vous trouverez le texte sur vos tablettes."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "J'ai hâte de découvrir à qui vous comptez vous plaindre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showGroup([
        ("mara", "neutre", 0.05),
        ("elias", "fatigue", 0.18),
        ("iris", "blase", 0.31),
        ("tomas", "reflexion", 0.44),
        ("elen", "content", 0.57),
        ("julian", "neutre", 0.70),
        ("ryn", "neutre", 0.83),
        ("noam", "reflexion", 0.96),
    ])

    iris agace "Elle est vraiment obligée de nous provoquer à chaque annonce ?"

    tomas reflexion "Pour le coup, c'est une vraie question. Si on conteste une détention décidée par Kami, qui examine la demande ?"

    ryn reflexion "Pas elle, j'espère."

    tomas raison "Justement. Il faudra voir ce que le texte permet."

    elen inquiet "On commence déjà ?"

    noam neutre "On a deux jours. On peut au moins finir de manger."

    tomas neutre "Je vérifiais juste la formulation."

    "Il fait défiler le document une dernière fois, puis pose sa tablette. Elen reprend sa discussion avec Mara pendant que je termine mon verre."

    "En débarrassant mon plateau, je pense à la proposition de Kami et cherche ma tablette dans la poche de ma veste. Je l'ai laissée sur la table de chevet."

    noam fatigue "Je vais chercher ma tablette. Je l'ai oubliée dans ma chambre."

    iris reflexion "Attends-moi, je viens. J'ai quelque chose à récupérer aussi."

    "Elle termine son café pendant que je rapporte mon plateau à Goumi, puis me rejoint près de la porte."

    elen content "Vous revenez après ? Je vais chercher les cartes."

    noam sourire "Oui, on revient."

    "Iris me laisse passer et nous prenons ensemble la direction des dortoirs."

    $ hideGroup()
    jump _25_0_1_1_0_0_BRUIT

label _25_0_1_1_0_0_BRUIT:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "couloir_dortoir") from _call_j25_door_3
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "neutre", 0.30),
        ("noam", "neutre", 0.60),
    ])

    "En traversant le dortoir, Iris consulte le texte de Kami sur son téléphone."

    noam taquin "Je croyais qu'on attendait avant de commencer."

    iris blase "Je regardais juste s'ils avaient précisé à qui on peut se plaindre."

    noam reflexion "Et alors ?"

    iris fatigue "Non. On aurait dû laisser Tomas poser sa question."

    "Elle range son téléphone pendant que j'ouvre ma porte."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_chambre") from _call_j25_door_4
    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "neutre", 0.30),
        ("noam", "neutre", 0.60),
    ])

    "Je récupère ma tablette sur la table de chevet. Iris lève les yeux vers la grille d'aération, bien au-dessus du bureau, et s'arrête près de la porte."

    iris reflexion "Tu as encore entendu quelque chose là-haut ?"

    noam neutre "Non. Mais je continue à surveiller cette grille."

    iris neutre "T'as réussi à dormir comme ça ?"

    noam sourire "Plutôt bien. J'aimerais continuer."

    "Je glisse la tablette sous mon bras et prends la direction de la porte."

    play sound sfx_creak volume 0.35

    "Le frottement revient derrière moi. Iris tourne aussitôt la tête vers la grille, mais je garde la main sur la poignée."

    iris reflexion "Attends. T'as entendu ?"

    noam neutre "Ça l'a fait ce matin aussi. Il y a quelque chose qui bouge dans la ventilation."

    iris inquiet "Quelque chose comment ?"

    noam fatigue "Une pièce mal fixée, probablement. Ça a tapé deux fois, puis ça s'est arrêté."

    "Un petit choc résonne dans le conduit. Iris s'approche du bureau et se penche vers l'ouverture."

    iris reflexion "Ça vient de juste derrière."

    noam neutre "On pourra demander à Elias de regarder. Elen nous attend."

    iris neutre "Deux secondes. Passe-moi la lampe."

    "Je regarde celle qui est restée près de mon lit, puis la lui tends. Iris essaie d'éclairer entre les lames de la grille, mais le bureau la gêne."

    iris agace "Aide-moi à pousser ça, je vois rien."

    "Je pose ma tablette et tire le meuble avec elle. Je voudrais simplement qu'elle trouve la pièce qui fait du bruit pour qu'on puisse repartir."

    iris reflexion "Là, à gauche. Tu vois ce qui dépasse ?"

    "Je m'accroupis à côté d'elle. Un petit morceau brun est accroché à une languette métallique, juste après la première jointure. Le courant d'air le soulève et fait vibrer le métal contre la paroi."

    play sound sfx_creak volume 0.25

    noam neutre "Voilà. On sait ce que c'est."

    iris reflexion "On dirait du tissu. Comment ça s'est retrouvé là ?"

    noam fatigue "Quelqu'un a accroché son vêtement en passant. Avec tous nos allers-retours..."

    "Elle déplace le faisceau pour mieux regarder le morceau."

    iris neutre "On peut l'enlever, au moins. Sinon ça va continuer à taper toute la journée."

    "Je retire les vis de la grille pendant qu'elle tient la lampe. Une fois l'ouverture dégagée, je passe le bras dans le conduit et décroche le tissu en tirant doucement."

    "Il est plus petit que je ne le pensais, froissé et sale sur une face. Une couture claire longe son bord."

    "Je reconnais la couleur avant d'avoir le temps de me retenir. Mon pouce s'arrête sur la couture, puis je tends le morceau à Iris."

    noam neutre "Tu peux jeter ça ? Je remets la grille."

    "Elle le prend, mais continue de me regarder."

    iris reflexion "Qu'est-ce qu'il y a ?"

    noam fatigue "Rien. Ça m'a rappelé la veste de Mara."

    "Iris baisse les yeux vers le tissu."

    iris inquiet "Celle que tu avais vue dans la salle ?"

    noam neutre "Oui. Mais c'est du tissu brun, Iris. Il doit y en avoir partout."

    "Je reprends la grille et la présente devant l'ouverture. Elle pose une main dessus pour m'arrêter."

    iris reflexion "Tu m'avais dit qu'elle avait quoi, exactement ?"

    noam fatigue "Une veste brune. Avec une couture comme ça sur la manche."

    iris inquiet "Et ce matin, ce morceau se retrouve dans ta chambre."

    noam raison "Dans la ventilation. Ça peut venir de n'importe où."

    iris reflexion "Oui, mais ça vient bien de quelque part."

    "Elle déplie le tissu sous la lampe. Je reste accroupi avec la grille entre les mains, de plus en plus mal à l'aise devant l'attention qu'elle lui porte."

    noam fatigue "Tu fais quoi ?"

    iris reflexion "Je regarde. C'est arraché, pas découpé. Il y a peut-être le reste quelque part."

    noam inquiet "Tu veux retourner dans les conduits ?"

    "Elle relève les yeux vers moi."

    iris neutre "Je voudrais qu'on vérifie."

    "Je pose la grille contre le bureau et me redresse."

    noam desaccord "La dernière fois, on a vérifié. Je vous ai amenés dans la salle et il y avait rien."

    iris raison "Il n'y avait rien sur la table. On n'a pas vraiment fouillé autour."

    noam fatigue "Parce que j'avais ramassé un couteau et que vous essayiez de me faire sortir. Je m'en souviens."

    "Iris baisse un peu la lampe. Je prends ma tablette sur le lit, mais ne la range pas."

    noam raison "Hier, j'ai passé une journée sans retourner là-bas, sans demander à tout le monde si j'étais en train de devenir fou. Ce matin, j'ai entendu ce bruit et je suis quand même allé manger. J'essaie de passer à autre chose."

    iris inquiet "Je sais. Je te demande pas de tout recommencer."

    noam desaccord "C'est pourtant ce qu'on va faire. On va ramper jusqu'à la salle, je vais regarder la table et..."

    "Je m'arrête avant de finir. Iris attend un moment, puis pose la lampe sur le bureau."

    iris neutre "Cette fois, c'est moi qui veux y aller. T'as pas besoin de me convaincre qu'il y a quelque chose."

    "Je regarde le morceau qu'elle tient toujours entre ses doigts."

    noam reflexion "Tu crois que c'est sa veste ?"

    iris inquiet "Je sais pas. Mais quand tu m'as parlé du corps, j'ai pensé que t'étais épuisé, que tu avais pu mal voir. Là, j'ai entendu le bruit aussi, et on vient de sortir ça du conduit."

    iris raison "Ça prouve pas ce que tu as vu. Mais j'ai plus envie de te dire de laisser tomber sans regarder."

    "Je reste près du lit. Une partie de moi attendait ces mots depuis des jours ; maintenant qu'elle les prononce, je voudrais qu'elle reprenne le tissu et le mette à la poubelle."

    noam fatigue "Et si on trouve encore rien ?"

    iris neutre "On ressort. Je vais pas te demander de chercher jusqu'à ce qu'on trouve quelque chose."

    "Elle approche du bureau et regarde dans l'ouverture, puis se tourne de nouveau vers moi."

    iris inquiet "Je peux pas retrouver la salle sans toi. Tu veux bien m'y emmener ?"

    "Je pose lentement la tablette. Iris me laisse le temps de prendre la pochette dans son rangement, puis y glisse le morceau de tissu."

    noam neutre "On regarde autour de la salle. On va pas plus loin."

    iris neutre "D'accord."

    "Elle resserre ses lacets pendant que je reprends la lampe. Devant le conduit ouvert, j'hésite encore."

    iris inquiet "Je reste derrière toi. Et si tu veux qu'on fasse demi-tour, tu me le dis."

    "Je hoche la tête et m'accroupis devant l'ouverture."

    stop music fadeout 0.8
    jump _25_0_1_1_0_0_CONDUITS

label _25_0_1_1_0_0_CONDUITS:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    $ flashlight_on(pattern=2)

    $ showGroup([
        ("iris", "neutre", 0.30),
        ("noam", "neutre", 0.60),
    ])

    "Je m'engage dans le conduit et attends qu'Iris me rejoigne. Elle ramène ses jambes dans l'ouverture, vérifie que son téléphone tient dans sa poche, puis me fait signe d'avancer."

    "Au premier virage, la lumière de ma chambre disparaît derrière nous. Je ralentis sans le vouloir ; le frottement de nos vêtements contre le métal suffit à me rappeler mes dernières traversées."

    iris reflexion "La salle est loin ?"

    noam neutre "Il reste quelques embranchements. Je te dirai quand on approche."

    "Elle me suit en faisant attention à garder ses genoux dans les parties lisses du conduit. Je m'arrête à la première bifurcation pour l'attendre."

    "Iris passe la main devant l'ouverture de gauche. Le courant d'air soulève légèrement sa manche."

    iris reflexion "Ça souffle vers ta chambre. C'est de ce côté qu'on va ?"

    noam neutre "Oui. Mais il y a d'autres branches avant la salle."

    iris reflexion "Donc le tissu pourrait venir de là-bas."

    noam fatigue "Il pourrait. On pourra pas suivre son trajet."

    "Elle regarde encore quelques secondes dans la branche, puis retire sa main pour me laisser continuer."

    "Plus loin, je reconnais la plaque enfoncée contre laquelle je m'étais cogné, puis le passage où Kael avait eu du mal à nous suivre. Je dirige la lampe vers le virage suivant, mais reste à genoux sans avancer."

    iris inquiet "Qu'est-ce qu'il y a ?"

    noam fatigue "C'est presque arrivé."

    "Elle se rapproche assez pour regarder par-dessus mon épaule."

    iris reflexion "La grille est après le virage ?"

    noam neutre "Oui."

    "Je voudrais lui donner la lampe et la laisser finir seule. Elle ne connaît pas la salle, pourtant ; c'est moi qui l'ai amenée et je ne peux pas m'arrêter maintenant."

    noam fatigue "La dernière fois, j'étais sûr que vous alliez la voir. J'avais même préparé ce que j'allais vous montrer en premier."

    iris inquiet "Et maintenant, t'as peur de trouver quoi ?"

    "Je regarde le faisceau posé sur le métal."

    noam faible "Je sais plus."

    "Iris reste près de moi sans essayer de répondre à ma place. Quand je reprends la lampe, elle recule juste assez pour me laisser bouger."

    "À l'approche de la grille, je baisse le faisceau et regarde entre les lames. Les deux Goumi de rechange sont toujours près des établis ; au milieu de la pièce, la table est vide."

    "Je laisse échapper un souffle. Pendant un instant, je me sens presque soulagé."

    iris "Tu vois quelque chose ?"

    noam fatigue "C'est comme la dernière fois. La table est vide."

    "Je me décale pour qu'elle puisse regarder. Iris s'approche de la grille et inspecte la partie de la salle qu'on peut voir depuis le conduit."

    iris reflexion "On voit pas derrière les machines."

    noam neutre "On verra mieux en descendant."

    "Elle tourne la tête vers moi, puis prend le bord de la grille pendant que je retire les fixations."

    $ hideGroup()
    jump _25_0_1_1_0_0_SALLE_GOUMI


label _25_0_1_1_0_0_SALLE_GOUMI:

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ flashlight_on(pattern=1)

    "Je descends sur l'établi, puis au sol puis Iris se laisse glisser à son tour ; je lui tiens le bras jusqu'à ce qu'elle trouve un appui."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "reflexion", 0.66),
    ])

    "Une fois debout, je dirige aussitôt le faisceau vers la table. Iris regarde plutôt le mur sous notre point d'entrée."

    iris reflexion "On commence près de l'aération. Il y a peut-être un vêtement accroché quelque part."

    "Je l'accompagne le long des établis. Elle inspecte les angles et les fixations pendant que j'éclaire derrière les bacs, puis sous les rangements."

    "Nous trouvons des câbles, des outils et une épaisse couche de poussière. Iris se baisse pour regarder sous le premier Goumi, mais ne ramasse rien."

    noam fatigue "Tu veux regarder où, après ?"

    iris reflexion "Derrière l'autre. Éclaire le sol, s'il te plaît."

    "Je ramène le faisceau vers le second robot. Une large trace traverse la poussière sous sa base."

    "Iris s'accroupit près de lui et approche la main du sol sans le toucher."

    iris reflexion "Tu te souviens s'il était à cette place ?"

    noam neutre "À peu près. Pourquoi ?"

    iris raison "Regarde la poussière. On l'a déplacé."

    "Je m'approche. Deux marques parallèles prolongent les appuis du robot, comme s'il avait été tiré vers la table avant d'être repoussé contre le mur."

    noam reflexion "Elias a travaillé ici. Ça peut être lui."

    iris neutre "Peut-être. Mais on va regarder derrière."

    "Elle se relève et cherche une prise sur le châssis. Je pose la lampe sur l'établi, orientée vers le mur, puis viens prendre l'autre côté."

    noam raison "On tire vers nous. Pas trop loin, il faut pouvoir le remettre."

    "Le Goumi résiste d'abord, puis glisse brusquement de quelques centimètres. Iris manque de perdre sa prise et nous nous arrêtons le temps qu'elle replace ses mains."

    play sound sfx_creak volume 0.65

    "Au second effort, nous dégageons une plaque de maintenance. Une des attaches n'est pas complètement rabattue."

    "Iris la remarque avant moi et s'approche."

    iris reflexion "Il y a quelque chose de coincé là."

    "Je récupère la lampe. Une bande de tissu brun dépasse entre la plaque et son cadre, retenue près de l'attache."

    "Iris sort la pochette et place notre morceau à côté. Sous le même éclairage, les deux tissus ont la même couleur."

    iris inquiet "Ça ressemble vraiment."

    "Je regarde la plaque assez grande pour laisser passer quelqu'un, puis le robot que nous venons de déplacer. Je comprends ce qu'elle veut ouvrir avant qu'elle pose la main dessus."

    noam inquiet "Iris..."

    iris reflexion "Il faut voir ce qu'il y a derrière."

    "Elle essaie de libérer l'attache, mais le tissu bloque le mécanisme. Je lui passe la lampe et prends sa place."

    "Le métal cède quand j'appuie. Iris défait la seconde fixation, puis nous tirons chacun d'un côté."

    stop music fadeout 0.8

    "La plaque s'écarte du mur. Une odeur nous atteint par l'ouverture et Iris retire aussitôt son visage."

    iris inquiet "C'est quoi cette odeur ?"

    "Je connais déjà la réponse que je ne voulais pas trouver. Je reste accroché au bord de la plaque tandis qu'Iris reprend la lampe pour éclairer l'espace derrière."

    "Le faisceau descend sur une manche, puis remonte vers le visage."

    $ hideGroup()
    scene black with Dissolve(0.25)
    pause 0.5

    $ unlock_gallery_image("bg_cg040")
    scene bg_cg040 at adaptive_fullscreen with signal_stutter
    $ doppelganger_reveal(screamer=False, duration=0.80, restore_volume=0.65)
    play music "music/bgm_horror_pulse.mp3" fadein 0.6
    $ danger_on()

    "Mara est là, repliée derrière la cloison. Sa veste est prise sous son bras et contre le bord de l'ouverture."

    "J'essaie de prononcer son prénom, mais Iris recule en emportant la lampe. Le faisceau traverse le mur, le sol, puis revient sur le corps comme si elle avait besoin de vérifier ce qu'elle vient d'éclairer."

    iris peur "Non... Attends."

    "Elle se rapproche d'un pas, juste assez pour voir le visage. Cette fois, elle reste immobile."

    "Je pose la plaque contre le mur avant qu'elle m'échappe, puis me tourne vers elle."

    scene bg_salle_goumi_cachee at adaptive_fullscreen with memory_rip

    $ showGroup([
        ("noam", "peur", 0.36),
        ("iris", "peur", 0.66),
    ])

    iris peur "C'est elle."

    "Ses yeux passent de l'ouverture à mon visage. Je ne réponds pas assez vite et elle me prend le bras."

    iris peur "Noam, tu la vois aussi ?"

    noam faible "Oui. C'est celle que j'avais trouvée."

    "Elle me lâche et recule jusqu'à l'établi. La lampe tremble dans sa main ; je la récupère doucement avant qu'elle la fasse tomber."

    iris peur "Mais on vient de lui parler. Elle était avec nous, elle..."

    "Elle se retourne vers la grille par laquelle nous sommes entrés, puis revient au corps. Je reste près d'elle, incapable de lui donner une explication qui rendrait la scène moins impossible."

    noam inquiet "Tu veux t'asseoir ?"

    iris colere "L'odeur est infecte, ça pue la mort."
    iris faible "Je veux me barrer de là."

    "Je regarde ses mains agrippées au bord de l'établi. Elle semble lutter pour ne pas tourner de l'oeil."

    iris peur "Tu crois que Mara... Enfin, l'autre Mara est encore à la cafétéria ?!"

    think "Je ne suis pas fou. J'ai vraiment vu ce que j'ai vu..."
    think "Mais alors, qu'est-ce qui se passe ici, bordel ?!"

    noam raison "On va remonter. Mais attends je veux vérifier un truc."

    "Je sors le bout de tissu. La couleur correspond parfaitement à la petite veste qu'elle porte toujours."

    noam reflechit "Je veux voir si ça correspond..."

    iris faible "Tu m'excuseras mais je touche pas à ça moi. Je te laisse fouiller, dis moi quand tu trouves ce que tu veux."

    "Iris s'éloigne de quelques mètres et me laisse près du corps."
    $ hideGroup()
    scene bg_cg040 at adaptive_fullscreen with dissolve
    call j25_examiner_veste from _call_j25_examiner_veste

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflechit", 0.36),
        ("iris", "faible", 0.66),
    ])

    iris faible "... Alors ?"

    "Je cadre le corps en tenant la lampe fermement. Je sors la tablette que je garde sur moi."
    think "Elle a bien une fonction d'appareil photo, non ?"

    $ hideGroup()
    scene bg_cg040 at adaptive_fullscreen with dissolve
    call j25_prendre_photo from _call_j25_prendre_photo

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "faible", 0.36),
        ("iris", "fatigue", 0.66),
    ])

    "Iris se rapproche et regarde par-dessus mon bras. Elle serre les lèvres en voyant la photo et détourne la tête."

    iris fatigue "Je pensais pas qu'on trouverait ça. Je voulais juste savoir d'où venait le tissu."

    noam faible "Ouais, je m'en doute. Mais... Sans ça ce sera comme la dernière fois. Personne ne nous croira."
    noam reflechit "Par contre, il ne manque aucun bout de tissu sur sa tenue. Même si le tissu correspond parfaitement bien..."

    "Je recule et regarde une fois encore la photographie de Mara."

    iris faible "Quand t'as voulu nous montrer la table l'autre fois, elle était déjà cachée ici ?"
    iris colere "Comment on a fait pour pas la voir ?"

    noam fatigue "Je sais pas. On aurait dû fouiller plus..."
    noam colere "Et puis, je comprends qu'avec l'histoire du couteau c'était pas rassurant d'être dans cette pièce..."

    iris inquiet "... O-Ouais, c'est clair. Tu m'avais fait bien flipper ce coup-là."

    "Je regarde le robot devant la cloison. Il nous a suffi de le tirer pour retrouver ce que j'avais fini par douter d'avoir vu."

    iris reflexion "D'ailleurs, en parlant du couteau... On l'avait laissé ici, non ?"
    iris fatigue "C'était pas là, il me semble..."

    "Elle s'abaisse et éclaire le sol à la recherche du couteau."

    iris inquiet "...Hein ? Il n'y a plus rien..."

    noam inquiet "Quoi ?! T'es sûre ?"

    iris colere "O-Ouais... Plus rien du tout."
    iris inquiet "Tu penses que quelqu'un l'a récupéré ?!"

    noam peur "J'en sais rien mais ça commence vraiment à devenir flippant."

    iris fatigue "Oui, sortons d'ici tout de suite. Tu as raison."

    "Nous remettons la plaque en place. Je dégage le tissu de l'attache pour pouvoir la fermer, puis nous repoussons le Goumi devant."

    $ danger_off()
    $ hideGroup()
    $ flashlight_on(pattern=3)

    "Je lui propose de remonter la première. Elle prend appui sur l'établi, mais s'arrête devant la grille et se tourne vers moi."

    iris inquiet "Tu me suis tout de suite, ne me quitte pas d'une semelle."

    noam neutre "Je suis juste derrière, t'inquiète."

    "Je garde la lampe sur l'ouverture pendant qu'elle entre, puis monte à mon tour sans regarder de nouveau vers les Goumi."

    jump _25_0_1_1_0_0_RETOUR

label _25_0_1_1_0_0_RETOUR:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Iris avance devant moi jusqu'au premier embranchement. Là, elle attend que je lui indique le chemin, puis reste à genoux sans repartir."

    iris inquiet "Tu penses que Sael pourrait analyser le corps ?"

    noam raison "Nous, on n'y connaît rien. Mais y'a une chose dont je suis sûr à 100%% : elle est morte de chez morte."
    noam reflexion "Alors à quoi bon autopsier le corps ? Je pense pas que ça nous aidera à comprendre."

    iris reflexion "Oui tu n'as pas tort. Raaah, j'aime pas rester impuissante ! Il faut qu'on fasse quelque chose !!"

    "Elle tourne la tête vers moi. Le faisceau éclaire mal son visage, mais je vois qu'elle attend que j'aille au bout de l'idée."

    noam reflexion "Tu penses à quoi ? A le dire à tout le monde ?"

    iris inquiet "J'ai envie de le dire à tout le monde. De remonter, de les faire venir et qu'ils m'expliquent ce bordel. Mais Mara sera là aussi."
    iris colere "Si Mara est morte, alors QUI est en bas avec nous ?"
    iris triste "QUI nous fait les mêmes blagues beaufs qu'elle ?"

    noam raison "Si seulement on avait le début d'une piste de réponse..."

    "Je baisse la lampe. Iris s'adosse à la paroi, les bras serrés contre elle."

    noam reflexion "Et si quelqu'un ou quelque chose avait pris sa place..."

    iris panne "Ouais, rien ne nous dit qu'on est pas plusieurs concernés."

    "Je relève les yeux. Elle a l'air presque aussi effrayée par sa remarque que moi."

    noam desaccord "Tu penses que les autres..."

    iris peur "J'ai pas dit ça, hein ! Je dis que j'aurais pas cru ça de Mara non plus. Ce matin, j'aurais laissé Mara entrer dans ma chambre sans y penser une seule seconde."
    iris triste "J'ai été bête de ne pas te croire..."

    "Je voudrais lui répondre... Mais je ne sais pas quoi dire. Je me rappelle la main de Mara dans le plat de biscuits et les miettes sur son doigt."
    "Iris reprend avant moi, plus bas."

    iris inquiet "Alors ouais, peut-être qu'elle n'est pas seule... On peut plus faire confiance en personne."

    "Nous restons immobiles jusqu'à ce qu'un souffle plus fort passe dans le conduit. Iris se remet à avancer en accélérant; je la suis en gardant la lampe devant elle."
    "Les derniers mètres me paraissent interminables. Je voudrais retrouver la lumière et une porte que je puisse fermer, mais ma chambre est reliée à cette salle par le chemin que nous venons de prendre."

    jump _25_0_1_1_0_0_CHAMBRE


label _25_0_1_1_0_0_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    $ flashlight_off()

    "Iris sort du conduit et s'écarte pour me laisser passer. Je remets la grille pendant qu'elle vérifie la porte, puis nous poussons le bureau contre l'ouverture."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    "Elle s'assoit sur le lit sans retirer sa veste. Je pose la lampe et ma tablette sur le bureau, mais garde encore la pochette dans la main."

    iris fatigue "On aurait dû regarder derrière le Goumi la première fois."

    noam neutre "On savait pas qu'il y avait une ouverture."

    iris inquiet "Elle était peut-être déjà là. Pendant qu'on te disait qu'il n'y avait rien."

    "Je glisse le tissu entre deux feuilles de mon dossier. Iris me regarde le ranger, puis baisse les yeux vers ses mains."

    noam fatigue "Je vous aurais pas crus non plus, à votre place."

    iris neutre "Ça change rien à ce que tu t'es pris après."

    "Je referme le tiroir sans répondre. Elle passe les mains sur son visage, puis se lève presque aussitôt."

    iris agace "Je vais me laver. J'ai l'impression d'avoir encore cette odeur sur moi."

    "Je l'entends faire couler l'eau. Pendant qu'elle se nettoie, j'ouvre la photographie sur ma tablette."

    "Le visage est reconnaissable. Je vérifie aussi qu'on distingue la veste et l'intérieur de la cloison, puis referme l'image avant qu'Iris revienne."

    iris inquiet "Tu l'as bien enregistrée ?"

    noam neutre "Oui. Elle est là."

    iris reflexion "L'envoie pas tout de suite."

    noam inquiet "À qui ? On vient de décider qu'on savait plus à qui parler."

    iris fatigue "Je sais. Je te le dis quand même."

    "Son téléphone vibre avant que je puisse répondre. Elle lit le message et laisse échapper un souffle."

    iris neutre "C'est Elen. Elle demande si on revient."

    noam fatigue "Dis-lui qu'on viendra plus tard."

    iris reflexion "Je lui ai déjà dit qu'on arrivait."

    "Elle commence à écrire, puis efface ce qu'elle vient de taper."

    iris inquiet "Qu'est-ce qu'on lui raconte ?"

    noam neutre "Qu'on a discuté. C'est vrai."

    iris fatigue "Ouais. Et si elle demande de quoi ?"

    "Je m'assois sur la chaise. Il y a moins d'une heure, je voulais retourner à la cafétéria pour qu'on me laisse tranquille avec la ventilation. Maintenant, je cherche une excuse pour ne pas y aller."

    noam inquiet "Mara est sûrement avec eux."

    iris neutre "Sûrement."

    "Iris pose son téléphone sur le lit et regarde la porte."

    iris inquiet "J'ai envie de lui demander. Juste de voir ce qu'elle répond."

    noam raison "Tu lui demanderais quoi ? Pourquoi on vient de trouver son corps ?"

    iris fatigue "Je sais bien que je peux pas. Mais rester ici à attendre, ça me rend folle."

    "Elle ramasse son téléphone et répond enfin à Elen."

    iris neutre "Je lui dis qu'on arrive. Si on reste enfermés tous les deux, quelqu'un va finir par venir."

    noam fatigue "Tu vas réussir à jouer ?"

    iris reflexion "J'en sais rien. Toi ?"

    "Je secoue la tête. Elle regarde ma veste, puis désigne mon épaule."

    iris neutre "Enlève ça, t'as de la poussière partout."

    "Je retire la veste pendant qu'elle essuie ses manches. Elle se regarde dans la petite glace près de la porte et passe un mouchoir humide sur son front."

    noam raison "Si tu veux partir pendant la partie, tu me le dis. Je viens avec toi."

    iris neutre "Toi aussi. Tu restes pas là à te forcer si ça va pas."

    "Je prends ma tablette et la range dans le tiroir avec le dossier. Iris attend près de la porte, la main sur la poignée."

    iris inquiet "On revient tout à l'heure pour réfléchir à ce qu'on fait ?"

    noam neutre "Oui. On va pas garder ça pour nous indéfiniment."

    "Elle ouvre la porte et regarde dans le couloir avant de sortir. Je la suis après un dernier regard vers la grille, trop haute pour être condamnée avec les meubles."

    $ hideGroup()
    jump _25_0_1_1_0_0_APRES_MIDI


label _25_0_1_1_0_0_APRES_MIDI:

    $ current_period = "Après-midi"
    call show_custom_title("Un peu plus tard") from _call_show_custom_title_j25_1

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j25_door_6
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Elen a installé les cartes sur une table de la cafétéria. Mara est assise près d'Elias, occupée à lire les règles pendant que Julian lui parle."

    $ showGroup([
        ("mara", "neutre", 0.10),
        ("elias", "fatigue", 0.24),
        ("elen", "content", 0.38),
        ("julian", "reflexion", 0.52),
        ("tomas", "neutre", 0.66),
        ("iris", "neutre", 0.80),
        ("noam", "neutre", 0.94),
    ])

    elen joie "Vous voilà ! On commençait à se demander si vous aviez oublié."

    iris neutre "Désolée. On a mis plus longtemps que prévu."

    mara reflexion "Pour récupérer une tablette ? Vous faisiez quoi ?"

    "Iris regarde Mara et blémit à vue d'oeil."

    elen triste "Qu'est-ce qui t'arrive, Iris ? T'es encore plus blanche que d'habitude."

    mara rire "Naaan, sérieux ?! Me dis pas que Noam a tenté sa chance ?!"

    noam surpris "Hein ?! Qu'est-ce que j'ai à voir avec ça; moi ?!"

    mara triste "Non mais tu sais que si tu veux, tu p..."

    iris colere "Non mais stop ! Noam ne m'a rien fait qu'est-ce que tu vas t'imaginer ?!"
    iris triste "J'ai juste... Un peu mal à la tête c'est tout..."

    tomas sourire "Qu'est-ce que vous avez fait alors ?"

    noam neutre "On a parlé du vote, c'est tout."

    tomas reflexion "Vous avez trouvé quelque chose ?!"

    "Je tire une chaise pour gagner quelques secondes. Iris s'assoit à côté de moi."

    noam fatigue "Non. On tournait un peu en rond."

    tomas neutre "On en reparlera demain, alors."

    elen content "Oui, aujourd'hui on joue ! Allez on a perdu assez de temps comme ça ! Je vous explique !"

    "Elle prend une carte et nous montre la liste imprimée sous le mot à deviner."

    elen neutre "Il faut faire trouver le mot à son partenaire, sans dire ceux qui sont en dessous. Si vous en dites un, on passe à la carte suivante."
    elias fatigue "C'est interdit de dire les noms en dessous, et interdit de dire aussi des noms propres ! Voilà, c'est à peu près tout !"

    "Elen distribue les rôles sans leur laisser le temps de continuer. Iris et moi jouons ensemble ; Mara fait équipe avec Elias, Julian avec Tomas."

    elen content "Qui veut commencer ?"

    iris neutre "On peut essayer, je crois avoir compris les règles."

    "Elle me tend le paquet. Je prends la première carte, mais mes yeux reviennent aussitôt vers Mara."
    "Elle rapproche sa chaise de celle d'Elias et lui demande de poser sa tasse ailleurs pour ne pas mouiller les cartes. Sa voix n'a pas changé. Elle s'agace exactement comme ce matin."

    iris reflexion "Noam ? T'es... Tu es prêt ?"

    noam fatigue "Oui, attends. Je relis."

    "Je baisse les yeux vers la carte. Le mot est simple, mais les premières explications qui me viennent contiennent toutes un mot interdit."

    noam reflexion "C'est un endroit où tu vas acheter de quoi déjeuner. La personne qui travaille là se lève très tôt."

    iris reflexion "Une boulangerie ?"

    noam neutre "Oui."

    "Je passe à la suivante. Iris répond vite, se trompe une fois, puis trouve lorsque je reprends mon explication. Au bout de quelques cartes, je commence enfin à écouter ce qu'elle dit."

    elen joie "C'est fini ! Vous en avez quatre."

    "Je pose le paquet. Mara le récupère et attend qu'Elen retourne le sablier."

    mara reflexion "T'as deux roues, un guidon, et faut pédaler."

    elias neutre "Un vélo."

    tomas raison "Non ça va pas, le mot pédaler était interdit."

    mara agace "Ah, merde. Je l'avais pas vu."

    "Elle met la carte de côté et continue. Elias cherche, propose trois réponses qui n'ont rien à voir, puis lui demande de reprendre depuis le début."

    mara fatigue "Tu m'écoutes au moins ?"

    elias agace "Oui ! Mais tu passes d'un truc à l'autre, je sais plus ce que je dois trouver, moi."

    "Mara se tourne vers moi en levant les yeux au ciel. Je baisse aussitôt le regard vers le sablier."
    "À côté de moi, Iris a cessé de sourire. Elle regarde Mara, puis ses propres mains, et se force à revenir à la partie lorsque Elen nous adresse la parole."
    "Nous jouons encore plusieurs manches. Je réponds quand on me demande quelque chose, je compte les points et je retourne le sablier, mais chaque fois que Mara bouge, je relève la tête."

    julian reflexion "Noam, c'est terminé ou pas ?"

    "Le sable a fini de couler. Julian tient encore sa carte, penché vers Tomas."

    noam surpris "Oui. Désolé, j'ai pas fait attention."

    julian neutre "On compte la dernière ? Il l'avait presque."

    tomas fatigue "J'avais pas trouvé."

    julian agace "Raaah ! Tu pouvais attendre avant de le dire."

    "Elen note le score pendant que Mara rassemble les cartes. L'une d'elles est restée près de mon verre ; elle se penche pour la récupérer."
    "Sa manche frôle mon poignet. Je retire la main trop vite et heurte le verre, qui se renverse sur la table."

    mara surpris "Attention aux cartes ! Faut pas les mouiller !"

    "Iris ramasse le paquet pendant qu'Elen écarte la feuille de scores. Je redresse le verre et attrape une serviette, mais Mara essuie déjà l'eau devant moi."

    noam inquiet "Laisse, je vais le faire."

    mara neutre "Qu'est-ce qui a ? Tu as renversé du soda sur ton pantalon ?"

    "Elle me tend deux serviettes. Je les prends en évitant ses doigts, puis commence à essuyer mon côté de la table."

    elen inquiet "Hein ? T'en as sur toi ?"

    noam fatigue "Non. Ça va."

    mara reflexion "T'es sûr ? T'as fait un de ces bonds."

    "Je continue de regarder la table. Iris pose une serviette sur la flaque près de mon coude."

    iris neutre "Il t'avait pas vue arriver."

    mara neutre "D'accord... Je voulais juste prendre la carte."

    "Elle la montre avant de la remettre dans le paquet. Je hoche la tête, mais je n'arrive pas à reprendre ma place."

    noam fatigue "Je vais me laver les mains. J'en ai un peu sur les bras."

    iris neutre "Je viens aussi."

    $ hideGroup()
    call show_custom_title("Quelques minutes plus tard") from _call_show_custom_title_j25_2

    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    "Nous sortons des lavabos et nous arrêtons à l'écart de la porte de la cafétéria. Iris regarde derrière nous avant de parler."

    iris inquiet "Elle est là ! Qu'est-ce qu'on fait ?! Tu veux qu'on parte ?"

    noam fatigue "Ouais je voudrais bien. Mais si on revient pas, elle va se demander pourquoi."

    iris reflexion "Elle a déjà remarqué que tu la regardais. Elle peut croire que c'est encore à cause de l'autre fois."

    noam inquiet "C'est aussi ce que j'ai pensé. Mais je peux pas continuer comme ça. En sachant ça..."

    "Iris s'appuie contre le mur. Elle garde les yeux sur l'entrée de la cafétéria, d'où nous entendons Julian contester un nouveau point."

    iris fatigue "Moi non plus. Quand elle parle, j'arrive presque à oublier. Et après je me rappelle ce qu'on vient de voir."

    noam reflexion "Il faut prévenir les autres."

    iris inquiet "Pas devant elle."

    noam raison "On peut leur demander de venir séparément. Mais ça va finir par se remarquer, et on sait même pas à qui commencer par parler."

    "Je regarde la caméra fixée dans le couloir. Iris suit mon regard."

    noam reflexion "Et si..."

    iris inquiet "...T'es sérieux ?! Tu veux l'annoncer à tout le monde ?"

    noam raison "La dernière fois, le corps avait disparu quand je suis revenu. Personne ne m'a cru."
    noam reflexion "Là, on a une preuve. On peut prévenir tout le monde de ce qui se passe ici !"

    iris raison "Si Kami laisse passer les images. C'est elle qui contrôle la diffusion."

    noam reflexion "Je sais. Mais elle a toujours dit que tout était diffusé, non ?"

    iris colere "Ça veut pas dire qu'elle va te laisser annoncer ce qu'on vient de trouver ! Et si elle coupe, Mara saura quand même qu'on est retournés là-bas."

    "Je quitte la caméra des yeux. Iris baisse la voix, mais reste tournée vers moi."

    iris inquiet "Elle nous a regardés entrer, tout à l'heure. Je veux pas qu'elle nous attende quand on sortira."

    noam fatigue "On peut pas faire comme si on avait rien vu non plus..."

    iris raison "Je te demande pas de te taire. Faut qu'on y réflechisse encore un peu."
    iris triste "D'ici là, faisons comme si on avait rien vu... Enfin, essayons..."

    "Je passe une main sur mon visage. J'ai envie de retourner dans la pièce, de poser la tablette sur la table et de les obliger à regarder. Je sais aussi que je n'ai aucune idée de ce qui arriverait ensuite."

    noam neutre "Demain matin. On se retrouve avant le petit-déjeuner et on décide comment leur dire."

    iris inquiet "Tu me promets que tu vas pas commencer ce soir ?"

    noam fatigue "Je vais rien dire sans toi."

    "Elle me regarde encore un moment, puis se redresse."

    iris neutre "Bon. On retourne finir la partie. Après, on pourra dire qu'on est fatigués."

    "Je la suis vers la cafétéria. Avant d'entrer, elle se retourne pour vérifier que je suis toujours derrière elle."

    $ hideGroup()
    jump _25_0_1_1_0_0_SOIR


label _25_0_1_1_0_0_SOIR:

    $ current_period = "Soir"

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Après le repas, Iris reste avec Elen pendant que je retourne à ma chambre. Nous avons convenu de nous retrouver demain avant que les autres se lèvent."

    "J'arrive devant ma porte quand Mara m'appelle depuis l'autre bout du couloir."

    mara "Noam, attends."

    "Je me retourne avec la main sur la poignée. Elle s'approche, une bouteille d'eau à la main, et s'arrête à quelques pas de moi."

    $ showGroup([
        ("mara", "neutre", 0.38),
        ("noam", "inquiet", 0.64),
    ])

    mara reflexion "Il y a un problème entre nous ?"

    noam surpris "Quoi ? Non. Pourquoi tu dis ça ?"

    mara fatigue "Parce que tu passes ton temps à me regarder et que tu sursautes quand je m'approche. Tout à l'heure, j'ai cru que je t'avais fait mal."

    "Je regarde vers la cafétéria. J'entends encore des voix, mais personne ne vient dans le couloir."

    noam neutre "Tu m'as pas fait mal. J'avais la tête dans les nuages."

    mara reflexion "Ouais, j'avais remarqué."

    "Elle attend une explication. Je pourrais lui dire que je suis fatigué, mais c'est elle qui m'a demandé ce matin si j'avais bien dormi."

    noam fatigue "J'ai juste hâte qu'on puisse rentrer chez nous."

    "Mara baisse les yeux vers sa bouteille et en dévisse le bouchon."

    mara rire "Ouais, même si les soirées qu'on passe tous ensemble me manqueront un peu."

    noam faible "Ouais sans doute un peu quand même."

    "Elle boit une gorgée, puis referme la bouteille sans reprendre immédiatement la parole."

    mara reflexion "Tu veux une goutte ? Je suis d'humeur partageuse ce soir."
    mara sourire "Peut-être même que... Enfin si tu veux, on peut aller boire un verre ensemble."

    noam panique "Hein ? Je me sens un peu patraque ce soir, mais... On peut sans doute se faire ça à l'occas ?"

    "Elle a l'air vexée, et je ne sais pas quoi faire de cette expression."

    noam fatigue "Je suis désolé, on se rattrapera. C'est pas du tout contre toi."

    mara agace "Tss, un peu quand même. Mais bon tant pis."
    mara triste "D'accord. Bonne nuit, essaye de bien te reposer."
    mara sourire "Je préfère quand tu es en forme."

    noam neutre "O-Ouais, bonne nuit."

    "Je la regarde rejoindre sa chambre. Elle ouvre la porte, entre et la referme sans se retourner."
    "Je reste quelques secondes dans le couloir, à me demander si elle est blessée ou si elle vient d'obtenir la réponse qu'elle cherchait."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_chambre") from _call_j25_door_5
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Une fois à l'intérieur, je ferme la porte et lève les yeux vers la grille d'aération. Elle reste inaccessible sans grimper et rien dans la chambre ne permet de la condamner."
    "Je prends ma tablette dans le tiroir. La photographie est toujours là ; je la regarde assez longtemps pour me rappeler que le corps derrière la cloison porte bien le même visage que la fille qui vient de me parler."
    "Le morceau de tissu est rangé dans le dossier, juste à côté. Je le sors de sa pochette et le déplie sur une feuille."
    "La couleur ressemble à celle de la veste. Pourtant, je n'ai trouvé aucune déchirure sur les parties du vêtement que j'ai pu examiner."
    "Je remets le morceau dans la pochette avant de recommencer à tourner autour de cette question."
    "Mon téléphone vibre. Iris demande si je suis rentré."
    "Je lui réponds que oui, puis lui raconte la conversation avec Mara. Elle m'appelle presque aussitôt."

    iris inquiet "Quoi ?! Elle t'a demandé quoi, exactement ?"

    noam neutre "Elle se doute de quelque chose, elle m'a..."

    iris reflexion "Elle t'a parlé des conduits ?"

    noam neutre "Non. Elle m'a proposé de venir boire un verre avec elle."

    iris colere "Hein ?! Mais pour qui elle se prend !"
    iris inquiet "Je sais que je devrais pas te dire ça, mais... Tu peux venir."

    noam fatigue "Hein ? Venir où ?"

    iris neutre "Bah dans ma chambre."

    noam faible "Je suis épuisé, si c'est pas important je préfère me coucher."

    iris neutre "T'es vraiment bête quand tu t'y mets. Tu vas vraiment dormir dans ta chambre alors que ta bouche d'aération est toujours ouverte ?!"
    iris inquiet "Mara pourrait très bien entrer dans ta chambre cette nuit !"
    iris colere "Imagine qu'elle te veuille du mal !"

    noam neutre "Oh putain tu as raison."

    iris neutre "Evidemment que j'ai raison. Embarque 2-3 affaires et toque précisément cinq fois à ma porte. Trois coups rapides, deux coups lents."
    iris colere "Et traine pas ! Sinon tu te débrouilles."

    "Après avoir raccroché, j'embarque ma tablette et quelques affaires de rechange."

    think "Si je dormais là, je pourrais très bien me faire tuer ce soir."

    "Je lève les yeux vers la caméra au-dessus de la porte. J'ai toujours détesté la savoir là ; ce soir, je voudrais être certain que quelqu'un regarde."

    think "Est-ce qu'il faut que je l'annonce à tout le monde ?!"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_dortoir")

    think "La chambre d'Iris est là. Quel était le mot de passe, déjà ?"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    call j25_toquer_iris from _call_j25_toquer_iris

    "Le verrou se déclenche. Iris entrouvre la porte et s'écarte pour me laisser passer."

    stop music fadeout 1.5

    call end_day("26", sleeping=True) from _call_j25_stay_end_day_26
    jump _26_0_1_1_0_0_REVEIL
