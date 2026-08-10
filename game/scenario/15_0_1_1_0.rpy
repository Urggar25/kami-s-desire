label _15_0_1_1_0_REVEIL_CHAMBRE:
    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 3.0
    "Je me réveille avant même que la lumière ne s’allume."
    "La chambre est grise."
    "Le plafond aussi."
    "Même mon souffle paraît gris."
    think "Jour 15."
    think "Encore un vote."
    think "Encore une façon de choisir qui va souffrir dehors."
    "Je reste immobile sous la couverture."
    "Je n’ai pas faim."
    "Je n’ai pas envie de parler."
    "Je n’ai même pas envie de bouger."
    think "À 14h, ils voteront sur l’ouverture totale des archives d’ARCHIVE."
    think "Un amendement au Commandement V."
    think "Diffuser ce qui était caché."
    think "Rendre public ce qui était réservé."
    think "En théorie, c’est une bonne chose."
    think "En théorie seulement."
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Bonjour, mes chers représentants."
    kami "J’espère que vous êtes tous bien réveillés."
    kami "Ou au moins assez vivants pour m’écouter."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Le vote du jour aura lieu à 14h précises."
    kami "Sujet : ouverture totale des archives d’[codex_dialogue_link('archive', 'ARCHIVE')] aux citoyens des districts."
    kami "Une petite révolution documentaire."
    kami "Un grand moment de transparence."
    kami "Et peut-être quelques crises existentielles au passage."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rappel utile."
    kami "Le Commandement V encadre actuellement toute diffusion d’information."
    kami "Toute donnée non validée par [codex_dialogue_link('archive', 'ARCHIVE')] reste interdite."
    kami "Si l’amendement est adopté, les citoyens auront accès à une partie immense des archives historiques, judiciaires et administratives."
    kami "S’il est refusé, le verrouillage restera total."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je sais."
    kami "C’est lourd."
    kami "Mais vous adorez les décisions impossibles."
    kami "Sinon vous ne seriez pas ici."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Et toi, Noam ?" 
    kami "Tu viendras aujourd’hui ?" 
    kami "Ou tu préfères encore rester derrière ta porte ?" 
    "Mon estomac se serre."
    noam peur "..."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je te taquine."
    kami "Enfin..."
    kami "À moitié."
    kami "À tout à l’heure, mes petits archivistes de l’apocalypse."
    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    "La chambre redevient silencieuse."
    think "Elle l’a fait exprès."
    think "Elle voulait que les autres entendent mon nom."
    think "Elle voulait leur rappeler que je suis encore là."
    think "Et que je peux encore ne pas venir."
    "Je m’assois lentement."
    "Ma tête tourne."
    "La bouche pâteuse."
    "Les yeux lourds."
    think "Ouvrir les archives..."
    think "Les dossiers personnels."
    think "Les rapports des districts."
    think "Les images des votes."
    think "Les conséquences."
    think "Les mensonges."
    think "Les fautes."
    think "Tout."
    "Je tends la main vers la tablette posée sur le bureau."
    "Elle vibre avant même que je la touche."
    noam inquiet "Déjà...?"
    "Un message apparaît."
    kael "Tu es réveillé ?" 
    noam "Oui."
    kael "Tu as entendu l’annonce ?" 
    noam "Oui."
    kael "Tu es bien sûr de ne pas y aller ?" 
    noam "Je ne sais pas."
    kael "Pas le choix, ce sera le meilleur moment pour aller vérifier les caméras."
    noam "Kael..."
    noam "Je comprends."
    noam "C'est le seul moment ou on pourra être au calme durant la journée."
    "Je relis son message deux fois."
    think "Il est devenu comme moi."
    think "Pas par choix."
    think "Par contamination sociale."
    noam "Tu veux qu’on se voie avant le vote ?" 
    kael "Non. Pas avant que les autres ne se rassemblent au Conclave."
    kael "Tout le monde sera dans la Salle du Conclave."
    kael "La salle d’observation sera vide."
    kael "Les archives du huitième jour devraient être accessibles aujourd’hui."
    kael "Le délai de verrouillage est terminé."
    kael "Si quelqu’un a pris la photo de Léa, on le verra."
    noam "Et si on ne voit rien ?"
    noam "Et si quelqu'un a supprimé les images comme quand j'ai été regardé l'autre jour ?"
    kael "Alors je ne sais plus."
    noam "Kael..."
    kael "Je t’attendrai près de la salle d’observation quand l'annonce sera diffusée."
    kael "Si tu viens."
    noam "Je viendrai."
    kael "Tu es sûr ?"
    noam "..."
    noam "Laissons aux autres la responsabilité de changer le monde."
    kael "D’accord."
    "L’écran s’éteint."
    "Je reste assis avec la tablette dans les mains."
    "Si je veux avoir des réponses. C'est la seule manière de faire."
    jump _15_0_1_1_0_RATIONS

label _15_0_1_1_0_RATIONS:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 3.0

    "Je suis assis sur le bord du lit depuis plus d’une heure, immobile."
    "Je n’ai toujours pas décidé si je sortirai aujourd’hui."

    "Soudain, trois coups légers résonnent contre la porte."

    play sound sfx_knock volume 0.9

    "Je relève brusquement la tête."

    noam inquiet "... Qui est là ?"

    pause 1.2

    "Aucune réponse."

    "Le silence retombe, lourd et immédiat."

    noam inquiet "Je sais que tu es là."

    pause 1.0

    play sound sfx_knock volume 0.7

    "Deux coups plus faibles."

    "Puis plus rien."

    noam peur "Répondez !"

    "Je reste figé, le regard rivé sur la porte."
    "Pas un mot."
    "Pas un pas qui s’éloigne."
    "Juste le silence."

    think "Ils ne veulent même plus me parler."

    "Je m’approche lentement de la porte."
    "Chaque pas fait grincer le sol."
    "Je colle mon oreille contre le battant."

    "Rien."

    "Je pose la main sur la poignée, hésite, puis ouvre d’un coup."

    play sound sfx_door volume 0.8

    "Un sac en toile épaisse est posé juste devant le seuil."
    "Dedans : des rations militaires, des conserves, des barres protéinées, des bouteilles d’eau."
    "De quoi tenir facilement trois ou quatre jours sans sortir."

    "Je regarde rapidement à gauche, puis à droite dans le couloir."

    "Personne."

    "Pas un bruit de pas."
    "Pas une ombre."
    "Celui ou celle qui a déposé ça est déjà loin."

    "Je tire le sac à l’intérieur et referme aussitôt la porte, comme si j’avais peur qu’on me voie."

    "Sur le dessus du sac, une petite note pliée."

    "Je la déplie."

    "\"Pour que tu puisses rester tranquille.\""

    "Aucune signature."
    "Aucune écriture reconnaissable."

    "Je relis la phrase plusieurs fois."

    think "Ils ne veulent plus me voir à la cafétéria."
    think "Ils ont trouvé la solution idéale : me nourrir sans avoir à croiser mon regard."
    think "Comme un animal qu’on laisse dans sa cage."

    "Je pose le sac sur le bureau."
    "Il est lourd. Bien rempli."
    "Presque attentionné."

    think "Qui a fait ça ?"

    "Je m’assois sur la chaise et fixe le sac."

    think "Ils ont peur que je fasse une scène."
    think "Ou pire : ils ont peur de moi."
    think "Alors ils me déposent de la nourriture devant la porte, comme à un chien enragé qu’on ne veut plus approcher."

    "Je passe une main sur mon visage."

    think "C’est presque pire qu’une insulte."
    think "C’est de la pitié organisée."

    "Je reste un long moment à regarder la note anonyme."

    think "Personne n’a eu le courage de rester devant la porte."
    think "Personne n’a eu le courage de me le dire en face."
    think "Ils préfèrent faire comme si je n’existais plus."

    "Je froisse lentement la note dans mon poing."

    noam murmure "Tranquille…"

    "Le mot a un goût amer."

    pause 2.0


    jump _15_0_1_1_0_COULOIR

label _15_0_1_1_0_COULOIR:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_debate.mp3" fadein 2.0

    "Le couloir est presque vide."
    "Presque."

    "Je les entends."
    "Tous."

    "Et je comprends que je ne peux pas les rejoindre."

    noam inquiet "..."

    kael inquietude "Tu es là ?"

    "Le message apparaît sur ma tablette."

    noam inquiet "Oui."

    kael inquietude "Ils sont devant le couloir principal ?"

    noam inquiet "Oui."

    kael fatigue "Attends un peu, ils vont rapidement rentrer."
    kael fatigue "Je t’attends."

    "Je range la tablette."
    "Je commence à reculer."

    iris inquiet "Noam ?"

    "Je me fige."
    "Trop tard."

    iris inquiet "Je sais que tu es là."

    mara agace "Oh putain."
    mara colere "Bien sûr qu’il est là."

    lysa blase "Le camouflage par culpabilité, ça ne marche pas."

    "Je sors lentement de l’angle."

    $ showGroup([
        ("mara", "colere", 0.08),
        ("iris", "inquiet", 0.23),
        ("lysa", "blase", 0.38),
        ("tomas", "raison", 0.53),
        ("ryn", "colere", 0.68),
        ("sael", "mefiant", 0.84),
    ])

    noam hesitation "Salut."

    mara colere "Salut ?"
    mara agace "C’est tout ?"

    noam hesitation "Oui."

    iris inquiet "Tu viens au vote ?"

    noam inquiet "Je..."

    ryn colere "Réponds."

    noam triste "Non."

    "Le mot tombe."
    "Personne ne bouge."

    elen inquiet "Noam..."

    noam triste "Je ne peux pas."

    ryn desaccord "Tu ne peux pas ?"
    ryn colere "Ou tu ne veux pas ?"

    noam culpabilite "Les deux."

    mara colere "Putain, c’est pas vrai."
    mara agace "Tu choisis aujourd’hui pour nous faire ton ermite ?"

    tomas inquiet "Mara..."

    mara colere "Non, désolée, mais merde."
    mara colere "On parle d’un amendement mondial."
    mara agace "Pas de savoir si monsieur veut croiser trois regards à la cafèt."

    iris colere "Mara, ça suffit."

    mara colere "Non."
    mara colere "Ça ne suffit jamais, justement."

    ryn fatigue "Pfff, vaut mieux ça qu'une crise comme l'autre fois."

    "La voix de Kael arrive derrière moi."
    "Je me retourne."

    kael fatigue "On y va."

    ryn surpris "Ah."
    ryn colere "Donc c’était ça."
    ryn colere "Les deux fantômes se sauvent ensemble."

    kael inquietude "Ryn."

    ryn desaccord "Quoi ?"
    ryn colere "J’ai tort ?"

    kael calme "Oui."

    ryn colere "Explique."

    kael calme "Non."

    ryn colere "Pratique."

    kael fatigue "Je ne dois rien à ton besoin de cogner sur quelque chose."

    ryn colere2 "Répète."

    sael mefiant "Ryn."

    ryn colere "Non."
    ryn colere "J’en ai marre des types qui fuient et qui appellent ça réfléchir."

    kael inquietude "Et moi j’en ai marre des types qui crient et qui appellent ça protéger."

    "Ryn avance d’un pas."
    "Sael pose une main sur son bras."

    sael mefiant "Pas ici."

    ryn colere "..."

    sael raison "Pas maintenant."

    ryn fatigue "Fait chier."

    noam raison "On ne veut pas bloquer le vote."

    nyra raison "L’intention ne changera pas le résultat."

    noam triste "Je sais."

    nyra raison "Alors assume-le clairement."
    nyra raison "Ne dis pas que tu ne peux pas."
    nyra raison "Dis que tu choisis de ne pas venir."

    "Sa phrase est froide."
    "Elle tombe juste."

    noam determine "Je choisis de ne pas venir."

    iris inquiet "Noam..."

    noam culpabilite "Je suis désolé."

    lysa blase "Il vient de dire d’arrêter avec ça."

    mara agace "Merci, Lysa, j’avais presque oublié d’être énervée."

    kael fatigue "On y va."

    noam fatigue "Oui."

    elen inquiet "Attendez."

    "Elen fait un pas vers nous."

    elen inquiet "S’il vous plaît."
    elen triste "Faites attention."
    elen inquiet "Je ne sais pas ce que vous cherchez."
    elen determine "Mais revenez."

    kael triste "..."

    noam triste "On reviendra."

    iris inquiet "Et mange vraiment."

    noam hesitation "J’ai mangé."

    iris colere "Une barre ne compte pas."

    mara agace "Oh, génial."
    mara agace "On est à deux doigts de l’apocalypse administrative et vous parlez goûter."

    iris colere "La ferme."

    mara rire "Touchée."

    "Kael m’entraîne dans l'angle du couloir, loin d'eux."
    "Je sens leurs regards dans mon dos avant de disparaitre de leur vue."

    think "J'ai choisi de ne pas y aller."
    think "J'en assumerai les conséquences."

    jump _15_0_1_1_0_RENCONTRE_KAEL

label _15_0_1_1_0_RENCONTRE_KAEL:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5
    "La salle d’observation est vide."
    "Les écrans projettent une lumière bleue sur le sol."
    "Kael verrouille la porte derrière nous."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    noam "Kael, je peux te poser une question ?"
    kael mefiant "..."
    noam "Pourquoi avec moi ? Pourquoi tu me fais confiance ?"
    kael doute "Je t'ai jamais dis de venir. Mais..." 
    kael "Tu es le seul à ne pas me regarder comme si j’avais tout fait foirer."
    kael calme "Puis... Ta présence de me dérange pas."
    noam "Les autres ne te détestent pas."
    kael "Je sais."
    kael fatigue "C’est presque ça le pire."
    noam fatigue "Comment ça ?" 
    kael inquiet "Ils ne me détestent pas, mais ils m'ont lachés car ils ne voulaient pas se mettre à ma place."
    "Kael s’assoit devant le terminal."
    "Il pose ses doigts sur le clavier."
    "Il ne tape pas."
    kael doute "Si on voit quelqu’un..."
    noam "On saura."
    kael "Sauf si..."
    noam reflexion "Tu penses que les vidéos peuvent être modifiées ?" 
    kael reflechit "C'est possible. Et franchement ce n'est pas si compliqué à faire."
    kael raison "Même si on laisse toujours des traces quand on fait ce genre de choses."
    "Il tape son code."
    "Le terminal s’ouvre."
    "Une liste de dossiers apparaît triée par jour et par lieu."
    kael "Chambre Kael."
    kael "Jour 8."
    kael reflechit "Plage horaire 00h00 à 23h59."
    noam "Tu as dormi quand ?" 
    kael "Il me semble que je n'ai pas été beaucoup dans ma chambre."
    noam triste "Donc n'importe qui aurait pu venir n'importe quand..."
    "Il appuie sur un bouton permettant de voir la vidéo en accéléré."
    "Il pointe du doigt un endroit précis sur les images de surveillance."
    "La photo accrochée au mur."
    noam raison "Oh on a même les logs pour les ouvertures de porte ici !"
    "Je lui montre un endroit spécifique à l'écran."
    noam joie "On peut chercher les ouvertures de porte."
    kael inquiet "Alors, voyons voir ce journal d’accès."
    "Il ouvre une fenêtre secondaire."
    kael "08h12, sortie."
    kael calme "08h17, entrée."
    kael "09h43, sortie."
    kael fatigue "13h06, entrée."
    noam panne "C’est normal ?" 
    kael "Oui."
    kael "Je suis revenu chercher ma tablette."
    noam determine "Ensuite ?" 
    kael "14h02, sortie."
    kael "19h28, entrée."
    noam neutre "Et le vol ?" 
    kael reflechit "La photo était encore là à 19h28."
    noam "Tu en es sûr ?" 
    kael calme "Oui. Je l’ai regardée."
    noam "Pourquoi ?" 
    kael mefiant "Parce que je fais ça tous les soirs."
    noam culpabilite "Tu ne l’avais jamais dit."
    kael "Faut dire que personne n’avait besoin de le savoir."
    noam "Donc après 20h ?" 
    kael "Oui."
    "Il accélère."
    "La chambre vide tremble légèrement sous la compression vidéo."
    "Puis l’image bouge soudainement."
    noam surpris "Attends."
    kael inquiet "J’ai vu un truc."
    noam "Reviens en arrière."
    "Il recule."
    "L’image saute de nouveau."
    kael "C'est quoi ? Un glitch ?!" 
    noam "Peut-être."
    kael peur "A quelle heure ?" 
    noam "21h17."
    kael "Je n’étais pas dans ma chambre."
    noam inquiet "Où étais-tu ?" 
    kael reflechit "En salle de repos je crois."
    noam "Tu crois ?" 
    kael peur "Je ne sais plus. Merde ! C'est déjà vieux d'une semaine..."
    "Il avale difficilement."
    kael "Continue."
    jump _15_0_1_1_0_VIDEO_KAEL

label _15_0_1_1_0_VIDEO_KAEL:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    "Kael relance la vidéo en temps réel, les doigts crispés sur la souris."
    "L’image est nette. Trop nette."

    "La porte de sa chambre s’ouvre. Kael entre."
    "Le Kael à l’écran traverse la pièce d’un pas calme, presque nonchalant."

    kael surpris "… C’est quoi ce bordel ?!"

    "Il s’arrête devant le mur où était accrochée la photo de sa sœur."
    "Il tend la main, décroche le cadre avec une douceur étrange."
    "Il regarde la photo un long moment, un léger sourire aux lèvres."
    "Puis il glisse tranquillement le cadre dans sa poche intérieure."

    kael peur "Non… Non, non, non !"

    "Le Kael filmé se tourne alors vers la caméra."
    "Juste une seconde."
    "Il regarde droit dans l’objectif."

    play sound sfx_glitch volume 0.9
    with hpunch

    centered "{color=#FF0000}FILE DELETED{/color}"

    scene bg_observation at adaptive_fullscreen with vpunch

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("kael", "neutre", 0.60),
    ])

    kael surpris "Qu’est-ce que c’était que ça ?!"
    kael triste "La vidéo a sauté ! Remets-la ! Remets-la tout de suite !"

    noam hesitation "Attends, Kael… calme-toi deux secondes."

    kael colere "Me calmer ?! Tu as vu la même chose que moi ou pas ?!"
    kael "C’était moi ! C’était clairement moi ! Ma veste, ma démarche, tout !"
    kael "Et pourtant je te jure sur la tête de ma sœur que je n’ai jamais touché cette photo !"

    "Il tremble. Ses mains sont serrées si fort sur le bord du bureau que ses articulations blanchissent."

    noam fatigue "Je te crois."
    noam triste "Enfin… je crois que tu crois sincèrement ce que tu dis."

    kael desespoir "Ne me parle pas comme à un fou, Noam."
    kael "Je sais ce que j’ai fait et ce que je n’ai pas fait."
    kael "Oui c'est ça ! Je me souviens parfaitement de cette soirée."
    kael "J’étais avec Elen à la salle de repos, puis j’ai croisé Nyra, puis je suis rentré tard."
    kael "Quand je suis arrivé, la photo n’était plus là."
    kael "Mais je n’ai jamais décroché ce cadre. Jamais."

    "Je relance la vidéo une deuxième fois."

    "Même séquence."
    "Même Kael."
    "Même geste précis."

    kael peur "Remets encore."

    "Troisième lecture."
    "Cette fois je remarque que le Kael à l’écran parle."
    "Aucun son ne sort mais ses lèvres bougent clairement."

    noam inquiet "Il dit quelque chose."

    kael colere "Lis sur ses lèvres ! Qu’est-ce qu’il dit ?!"

    noam panne "Je… je n’arrive pas à tout lire."
    noam reflexion "Quelque chose comme… « Je suis désolé » ou « Il le fallait »… je ne suis pas sûr."

    kael "Pourquoi est-ce que je dirais ça ?!"
    kael desespoir "Pourquoi est-ce que je volerais la seule photo qui me reste de ma sœur et que je m’excuserais devant une caméra ?!"

    "Il se passe les deux mains dans les cheveux, au bord de la crise."

    kael doute "C’est mon visage, Noam."
    kael triste "C’est ma voix dans ma tête qui me dit que ce n’est pas moi."
    kael effondre "Je deviens complètement dingue ou quoi ?"

    noam hesitation "..."

    kael "Dis quelque chose, putain !"

    noam fatigue "Je ne sais pas quoi te dire."
    noam reflexion "C’est toi sur la vidéo. Aucun doute là-dessus."
    noam culpabilite "Mais je te crois quand tu dis que tu ne te souviens pas l’avoir fait."

    "Kael me regarde longuement."
    "Ses yeux sont rouges, hantés."

    kael reflechit "Alors qu’est-ce que ça veut dire ?"
    kael desespoir "Que quelqu’un se fait passer pour moi ?"
    kael peur "Que je fais des black-out ?"
    kael desespoir "Que je suis en train de perdre la tête ?"

    "Je reste silencieux."
    "Dans mon esprit, l’image de la silhouette que j'ai aperçu dans le couloir revient en force."
    "Le dessin décalqué de Juliette."
    "Tout ça tourne, s’imbrique."

    think "Et si c’était la même chose pour moi ?"
    think "Et si j’avais arraché mon propre dessin sans m’en souvenir ?"

    kael "Noam."
    kael mefiant "Tu as pensé à quelque chose. Je le vois sur ton visage."

    noam triste "… Non. Rien de concret."

    kael colere "Ne me mens pas. Pas maintenant."

    noam hesitation "Je me demande si c'est ce qui m'arrive aussi."
    noam fatigue "Pour le dessin de Juliette, ma petite soeur qui a aussi disparu."
    noam reflexion "Peut-être... Peut-être que c'est moi aussi que me le suis enlevé..."
    noam fatigue "Mais... Mais ça n'a aucun sens !"

    "Kael me fixe intensément."

    kael "On est dans la même merde, alors."

    "Un long silence s’installe entre nous."

    kael reflechit "Il faut continuer à chercher."
    kael raison "Peut-être que la vidéo a été modifiée !"

    noam "Oui ! C'est peut-être ça !"

    pause 1.5

    jump _15_0_1_1_0_ARCHIVES_CROISEES

label _15_0_1_1_0_ARCHIVES_CROISEES:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.5

    $ showGroup([
        ("noam", "hesitation", 0.30),
        ("kael", "desespoir", 0.60),
    ])

    "Kael reste penché sur le clavier, les yeux injectés de sang."
    "Il tape frénétiquement, ouvre des menus que je ne comprends pas."

    kael raison "Si la vidéo a été modifiée, il doit y avoir une trace."
    kael "Les métadonnées, les timestamps, l’empreinte numérique… tout est enregistré ici."

    "Il ouvre une fenêtre technique remplie de chiffres et de codes."

    kael reflechit "Date de création… 8ème jour, 23h47."
    kael "Dernière modification… aucune."
    kael "Empreinte d’intégrité… valide."
    kael mefiant "Source… caméra interne chambre Kael-07. Authentifiée."

    "Il relance la vidéo une quatrième fois."

    "Même séquence. Même Kael. Même geste précis pour décrocher la photo."

    kael colere "C’est impossible !"
    kael doute "[codex_dialogue_link('archive', 'ARCHIVE')] n’a pas touché au fichier !"
    kael triste "Aucune compression forcée, aucun montage détecté, aucun artefact !"
    kael peur "C’est une vidéo originale, putain !"

    "Il frappe du poing sur le bureau."

    kael desespoir "C’est moi… C’est vraiment moi sur cette vidéo…"
    kael "Et je ne m’en souviens absolument pas."

    noam inquiet "Kael…"

    kael peur "Ne dis rien."
    kael "Je sais ce que tu penses."
    kael mefiant "Tu te demandes si je suis en train de craquer."
    kael "Si j’ai fait un black-out."
    kael culpabilite "Ou pire… si je mens."

    noam hesitation "Je ne pense pas que tu mentes."

    kael triste "Alors explique-moi."
    kael effondre "Explique-moi comment je peux voir mon propre corps faire quelque chose que mon cerveau refuse de reconnaître."

    "Il relance encore une fois la vidéo, au ralenti cette fois."

    "Le Kael à l’écran décroche la photo avec une douceur presque amoureuse."
    "Il la regarde, passe son pouce sur le visage de sa sœur, puis la range dans sa poche."

    kael culpabilite "Léa…"

    "Sa voix se brise."

    kael desespoir "Je ne ferais jamais ça."
    kael triste "Même dans mes pires moments… je ne ferai jamais disparaitre cette photo."
    kael effondre "C’est tout ce qu’il me reste d’elle."

    "Il se laisse tomber contre le dossier de la chaise, les mains sur le visage."

    kael "Si ce n’est pas une modification…"
    kael "Alors c’est moi."
    kael triste "C’est vraiment moi qui ai fait ça."
    kael effondre "Et je ne m’en souviens pas."
    kael colere "Qu'est ce que j'en a foutu ! Où est-ce que je l'ai mis !"

    "Un long silence s’installe."

    noam fatigue "..."
    noam "On devrait peut-être regarder d’autres caméras."
    noam "Voir si tu étais vraiment seul ce soir-là."

    kael raison "J’ai déjà vérifié."
    kael "Aucune autre caméra ne couvre ce couloir à ce moment précis."

    "Il tourne lentement la tête vers moi."

    kael mefiant "Noam."
    kael "Tu as vu quelque chose toi aussi, pas vrai ?"
    kael "Dans le couloir, avant l’annonce de Kami."
    kael doute "Tu en as parlé lors du dernier vote."

    "Je reste silencieux."

    kael inquiet "Dis-moi la vérité. Dis moi ce que tu as vu."

    noam hesitation "..."
    noam "Je ne sais plus quoi en penser."
    noam peur "Justement, je ne comprends pas ce que j'ai cru voir."

    "Kael me fixe encore un moment, puis retourne vers l’écran."
    "L’image figée montre toujours son propre visage en train de voler la photo de sa sœur."

    kael triste "On est foutus."
    kael "Si ce n’est pas une manipulation…"
    kael "Il faut que je retrouve cette photo !"

    pause 2.0
    hide kael with dissolve 

    "Sur ces mots, Kael quitte la pièce rapidement et part en direction des dortoirs."

    jump _15_0_1_1_0_CHAMBRE_NOAM_VIDEO

label _15_0_1_1_0_CHAMBRE_NOAM_VIDEO:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_sad.mp3" fadein 3.0

    "Kael est parti depuis quelques minutes."
    "Je suis seul dans la salle d’observation, les écrans toujours allumés."
    "Le silence est assourdissant."

    "Je m’assois devant le terminal et tape mon code d’accès."

    think "Si Kael ne se souvient pas avoir volé sa photo…"
    think "Alors je dois voir pour mon dessin."

    "J’accède aux archives de ma chambre."
    "Nuit du 7 au 8."
    "Je remonte jusqu’à 2h10 du matin."

    "La vidéo démarre."

    "Je dors profondément."
    "La porte s’ouvre sans bruit."
    "Kael entre."

    noam murmure "... Kael ?"

    "Il avance droit vers mon bureau, regarde le mur et voit le dessins de Juliette."
    "Il tire d'un coup sec dessus et regarde dans la direction du lit."
    "Il regarde le dessin un instant puis fais demi-tour, il sort rapidement de la pièce."

    "Je reste figé."

    "Je relance la vidéo."

    "Même séquence."

    "Je la relance une troisième fois, puis une quatrième, au ralenti."

    noam colere "C’est lui."
    noam colere "C’est vraiment lui, putain !"

    "Je frappe du poing sur le bureau."

    noam colere "Enfoiré !"
    noam colere "Tu viens piquer mon dessin dans ma propre chambre et tu fais comme si de rien n’était ?!"

    "Je me lève d’un bond, le cœur cognant dans ma poitrine."

    think "Il m’a menti en face."
    think "Il m’a regardé dans les yeux tout à l’heure et n’a rien dit."

    noam colere "Ça ne va pas se passer comme ça."

    "Je quitte la salle d’observation à grands pas."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Le couloir est désert, tout le monde doit encore être au vote."

    "Je tourne à l’angle et le vois au loin, marchant rapidement vers les dortoirs."

    noam colere "Kael !"

    "Il se retourne."

    "Je le rejoins en quelques enjambées et l’attrape violemment par le col."

    noam colere "Toi, tu viens avec moi !"

    kael surpris "Noam ?! Qu’est-ce qui te prend ?!"

    noam colere "Ferme-la !"

    scene bg_observation at adaptive_fullscreen with dissolve

    "Je le traîne de force jusqu’à la salle d’observation."
    "Il se débat à moitié, surpris par ma violence."

    "Une fois à l’intérieur, je le pousse vers le terminal et relance immédiatement la vidéo."

    $ showGroup([
        ("noam", "colere", 0.30),
        ("kael", "surpris", 0.60),
    ])

    noam colere "Regarde."
    noam colere "Regarde bien, enfoiré."

    "Sur l’écran, Kael entre dans ma chambre, prend le dessin de Juliette et repart."

    noam colere "C’était toi !"
    noam colere "Le 7 au 8, à 2h14 du matin !"
    noam colere "Tu as volé mon dessin de Juliette et tu n’as rien dit ?!"

    "Kael fixe l’écran, les yeux écarquillés."

    kael doute "... Ce n’est pas moi."

    noam colere "Arrête de me prendre pour un con !"
    noam colere "C’est toi ! Ton visage, tes vêtements, ta démarche !"
    noam colere "Alors maintenant tu vas t’expliquer !"

    "Je reste planté devant lui, tremblant de rage."

    think "Je lui fais confiance depuis tout à l’heure…"
    think "Et il m’a menti en pleine figure."

    "La vidéo tourne en boucle derrière nous."

    jump _15_0_1_1_0_CONFRONTATION_KAEL

label _15_0_1_1_0_CONFRONTATION_KAEL:

    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    noam colere "Explique-toi ! Tout de suite !"

    kael surpris "Noam, lâche-moi !"

    noam colere "La vidéo, enfoiré ! Tu es entré dans ma chambre et tu as volé mon dessin de Juliette !"

    "Kael me regarde, les yeux écarquillés… puis son expression change lentement."
    "Son regard devient plus froid. Plus calme. Trop calme."

    kael sourire "Ah… Ecoute lâche moi, il faut qu'on parle calmement."

    "Sa voix est légèrement différente. Plus posée."

    noam hesitation "... Quoi ?"

    kael taquin "Suis moi, je vais tout t'expliquer."

    noam "Hein ?!"

    play sound sfx_glitch volume 1.0
    with vpunch

    scene black with dissolve

    pause 2.0

    scene bg_laboratoire at adaptive_fullscreen with vpunch
    pause 0.2

    scene black with dissolve

    "Puis..."

    scene bg_cg033 at adaptive_fullscreen with vpunch
    pause 0.2

    scene black with dissolve
    "Plus rien."

    call end_day("16") from _call_end_day_16
    jump _16_0_1_1_0_REVEIL_CHAMBRE
