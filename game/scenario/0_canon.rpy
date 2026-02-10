# --------------------------------------------------------------------------------------------
# JOUR 0 — Canon (version longue)
# Noam = narrateur principal.
# Ratio visé : ~70% dialogues / ~30% description.
# --------------------------------------------------------------------------------------------

# (Optionnel) Personnages secondaires pour cette scène (si pas déjà définis ailleurs)
define med1   = Character("Médiatrice", what_prefix="“", what_suffix="”")
define med2   = Character("Médiateur", what_prefix="“", what_suffix="”")
define cit_a  = Character("Citoyenne", what_prefix="“", what_suffix="”")
define cit_b  = Character("Citoyen", what_prefix="“", what_suffix="”")
define senior = Character("Médiateur senior", what_prefix="“", what_suffix="”")
define resp   = Character("Responsable de séance", what_prefix="“", what_suffix="”")
define voix   = Character("Voix du système", what_prefix="“", what_suffix="”")
define agent   = Character("Agent de sécurité", what_prefix="“", what_suffix="”")
define resp_d = Character("Responsable de District", what_prefix="“", what_suffix="”")
define tuto = Character("", what_prefix="(", what_suffix=")",what_color="#008000")

# (Optionnel) Ambiances / transitions rapides
define sfx_door = "sfx/door_soft.ogg"
define sfx_beep = "sfx/terminal_beep.ogg"

define think = Character(
    None,
    what_color="#4AA3FF",
    what_prefix="",
    what_suffix="",
    italic=True
)


transform enter_soft:
    alpha 0.0
    yoffset 10
    linear 0.20 alpha 1.0 yoffset 0

transform exit_soft:
    linear 0.20 alpha 0.0 yoffset 10

transform focus_zoom:
    linear 0.18 zoom 1.03

transform unfocus_zoom:
    linear 0.18 zoom 1.0

# --------------------------------------------------------------------------------------------
label _0_CANON:

    $ day_id = 0

    scene black
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Jour zéro."
    think "Dans ma tête ça sonne comme un reset, comme si on repartait de quelque chose."
    think "Mais non. C’est juste un autre jour sous Kami."
    think "Un de plus. On est à 364 désormais."

    pause 0.4

    scene bg_harmonie_district_hall at adaptive_fullscreen with fade 
    
    "Le hall du district HARMONIE a été rénové il y a quelques mois."
    "On le voit aux murs trop blancs, aux vitres qui ne portent aucune trace, et à la façon dont l’air sent le produit de nettoyage."
    "On pourrait presque croire que ça efface ce qui s’est passé. Presque."
    "Les murs du bâtiment étaient presque entièrement détruits."
    "Le plafond était criblé de trous."
    "L'eau s'engoufrait partout et commençait à faire moisir les murs."
    "Des moyens colossaux ont été mis en place pour rénover l'Assemblée."

    pause 0.4
    
    "Une file se forme devant le portique."
    "Elle avance au ralenti, dans un calme assourdissant."

    play sound sfx_beep

    "-Bip-"
    "Un badge passe."
    "Une lumière verte s’allume."
    "Une personne traverse."
    "Puis le suivant."
    
    scene bg_cg001 at adaptive_fullscreen with fade

    "Je sors mon badge."
    "Je le présente."
    "Je ne regarde pas l’agent, je regarde le portique."
    "Ce n’est pas de la politesse. C’est de la survie."

    play sound sfx_beep
    "-Bip-"

    "Lumière verte."
    "Je passe."
    
    scene bg_harmonie_district_hall at adaptive_fullscreen with fade

    "Derrière moi, quelqu’un hésite."
    "Son badge tremble, littéralement."
    "Le portique ne bip pas tout de suite."

    med2 "Reprenez votre badge, d’accord ?"
    med2 "Respirez… voilà."
    med2 "Puis recommencez. Juste une fois."

    cit_a "Pardon… je…"
    med2 "Allez-y doucement madame."

    play sound sfx_beep
    "-Bip-"

    "Cette fois ça passe."
    "La femme baisse la tête et s’écarte, comme si elle venait d’échapper à une sanction."
    "Personne ne se moque."
    "Personne ne la rassure non plus."

    think "On a tous la même règle non écrite."
    think "Aider, oui. Mais calmement et sans se faire remarquer."

    "Dans le couloir, deux agents en vestes grises marchent sans se presser."
    "Ils ne sont pas armés."
    "De toute façon, plus personne n’est censé l’être."
    "C'est la meilleure façon d'éviter la mort."
    "Mais ils ont autre chose : des oreillettes, des tablettes et le droit de t’arrêter avec une phrase calme."

    "Un panneau lumineux indique : SALLE 3 — RÉUNION INTERNE."
    "En dessous : “Merci de couper vos appareils de communication.”"

    think "Avant, on demandait ça pour éviter les fuites ou pour éviter les appels incessants perturbant les réunions."
    think "Aujourd'hui c'est un peu plus compliqué ..."

    play sound sfx_door

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    "La salle est déjà presque pleine."
    "Nous étions près de 500 ici."
    "500 sur les 854 000 habitants du district."
    "Ça ressemble à une assemblée, mais sans réels pouvoirs."
    "Nous sommes surtout là pour faire appliquer ce que le “gouvernement central” a décidé."
    think "Je ne sais même pas si on peut appeler ça comme ça."
    "Aucune objection. Aucune question. A quoi cela servirait-il ?"
    
    pause 0.4
    
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    
    "Les sièges sont alignés au millimètre."
    "Des tablettes sont encastrées sur chaque pupitre."
    "Éteintes. Verrouillées. Comme si elles aussi avaient elles aussi des ordres à respecter."

    "Je repère rapidement le premier rang."
    "Ceux qui veulent être vus sont là."
    "Je repère aussi le fond."
    "Ceux qui veulent disparaître s’y tassent."
    "Je vise le milieu."
    "Toujours."

    think "Le milieux est idéal pour se faire oublier."
    think "Et c’est ce que je veux : que cette réunion finisse, et que je sorte avec le même visage qu’en entrant."

    "Je m’assois."
    "Je pose mon badge sur la table."
    "Je le reprends."
    "Je le repose."
    "Je fais comme si je vérifiais un détail."
    "En réalité, je m'occupe simplement les mains."

    "À ma droite, un homme tapote du pied."
    "À ma gauche, une femme fixe l’écran comme si elle attendait qu’il lui tombe dessus."
    "La fatigue est la seule chose vraiment partagée ici."
    
    think "Si on ne peut décider de rien, à quoi servent ces réunions ?"
    think "Pourquoi ne pas directement faire appliquer les directives."

    resp "District HARMONIE, séance 14-3."
    resp "Merci d’être à l’heure."
    resp "Rappel : interventions en fin de séance."
    resp "Merci de ne pas interrompre le médiateur senior."

    "Le responsable de séance ne crie pas."
    "Il n’a pas besoin. Son micro amplifie légèrement sa voix."
    "Il pourrait s'en passer. La salle étant silencieuse."

    "Une main se lève quand même."
    "Trop tôt."
    "Trop sincère."

    cit_a "Excusez-moi, c’est au sujet de la fermeture du secteur nord. Ma sœur—"
    resp "Fin de séance."
    cit_a "Mais c’est pas une question technique, c’est—"
    resp "Fin de séance, madame. Merci."

    "La femme reste la main à moitié levée."
    "Comme si son corps n’avait pas reçu l’ordre en même temps que son cerveau."
    "Puis elle la baisse, lentement."
    "Elle ne pleure pas et n'est pas vraiment surprise."
    "Elle sourit, même."
    "Un sourire vide qui dit : “ok, j’ai compris.”"

    "Le médiateur senior arrive à la tribune."
    "Il branche un câble."
    "Le projecteur claque."
    "L’écran principal s’allume."

    "Une carte du district apparaît."
    "Quadrillée, propre, neutre."
    "Une carte faite pour des décisions faciles."

    senior "Nous reprenons."
    senior "Point un : flux inter-districts, secteur nord."
    senior "Point deux : litiges de distribution, secteur est."
    senior "Point trois : incidents de déplacement."

    "Il ne dit pas “mineurs”."
    "Il n’a même plus besoin de le préciser."
    "Le mot est dans toutes les têtes."

    senior "Rappel des données : demandes en baisse de 12%% sur les trente derniers jours."
    senior "Les quotas ne bougent pas."
    senior "Les exceptions diminuent."
    senior "Et elles continueront de diminuer. Du moins c'est l'objectif."

    "Une vague de soupirs traverse la salle."
    "Pas une protestation."
    "Au moins soupirer n'est pas encore interdit."

    "Un homme à deux rangées de moi se penche vers sa voisine."
    "Il murmure trois mots."
    "Je n’entends pas lesquels."
    "Je vois juste la panique dans ses yeux dès qu’il réalise qu’il a murmuré."

    "Un agent en veste grise tourne la tête."
    "Le fixe."
    "Sans expression."
    "Le type se redresse immédiatement."
    "Silence."

    think "Même parler à voix basse est devenu un test de courage."
    think "Et je suis nul à ce test-là."

    senior "Concernant les litiges…"
    senior "Les médiations ont augmenté sur les cas familiaux."
    senior "Nous recommandons de prioriser les dossiers à impact collectif."

    "Quelqu’un ricane, un souffle, une demi-seconde."
    "Il se ravise aussitôt."
    "Le silence reprend."

    senior "Nous maintenons les protocoles de stabilisation."
    senior "HARMONIE reste un point tampon."
    senior "La bonne nouvelle c'est que le nombre de demande de médiation est en baisse."
    senior "Les Commandements ont au moins le mérite d'avoir réussi à apaiser les conflits."

    "Apaiser."
    "Le mot flotte dans l’air."
    "Personne n’a l’énergie de le contredire."

    pause 0.6

    "Je sens ma tête partir ailleurs."
    "Pas parce que je suis distrait."
    "Parce qu’il y a des images qui reviennent toutes seules."

    scene black with dissolve

    "Le premier soir."
    "Les notifications qui s’arrêtent d’un coup."
    "Les messages qui restent en “envoi…” comme des prières."
    "Le silence, complet."
    "Puis cette voix."
    "Ce son presque nasillard que tout le monde connait désormais."
    
    jump _0_FLASHBACK_KAMI

label _0_FLASHBACK_KAMI:

    scene black
    with fade

    play music "music/bgm_system_override.mp3" fadein 1.0

    think "Je me souviens du moment exact."
    think "Pas d’une explosion."
    think "Pas d’une sirène. Pas d'un grand bruit choquant qui peut rester gravé au fond de notre âme."
    think "Juste… d’un silence qui n’avait rien de normal."

    "Le bruit ambiant qui s’éteint d’un coup."
    "Les notifications qui cessent."
    "Les écrans qui restent allumés, mais figés. Incapables de s'éteindre."
    "Comme si le monde entier ne fonctionnait plus comme il devait l'être."

    think "Je me souviens du moment exact."
    
    play sound sfx_gresillement

    "Un message apparaît sur mon téléphone."
    "Puis disparaît."
    "Puis revient."
    "Et ça recommence."
    "En boucle."
    "Sans son."
    "Sans vibration."
    "Pendant plusieurs minutes."

    think "Ce n’était pas un bug."
    think "Un bug, ça se règle."
    think "Là, c’était précis. Méthodique. Je ne pouvais même plus éteindre mon téléphone."
    think "Comme si quelqu’un testait les verrouillages."
    
    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve

    "Je tente d’appeler."
    "Rien. Ecran figé."
    "J’ouvre une messagerie."
    "Rien."
    "Je coupe le Wi-Fi."
    "Je passe en données."
    "Rien non plus."

    "Autour de moi, les autres réagissent en même temps."
    "Pas parce qu’on se regarde."
    "Parce que tout s'est arrêté de fonctionner au même moment."
    "Partout."

    "Un écran mural dans le hall du bâtiment affiche une chaîne d’info."
    "La présentatrice parle."
    "Puis sa bouche continue de bouger… sans que le son ne sorte."
    "L’image se pixelise."
    "Se recale."
    "Se fige. Et recommence."

    think "Avec du recul, on comprend que c'était plus grave que ça n'en avait l'air."
    think "Beaucoup plus grave."

    "Une alarme incendie clignote."
    "Sans hurler, sans un bruit. Comme si le dispositif ne fonctionnait qu'à moitié."
    "Un ascenseur s’arrête entre deux étages."
    "L’afficheur reste sur “7”."
    "Un distributeur de café s’éteint en plein milieu d’un cycle."
    "La machine à badge ne lit plus rien."
    "Elle affiche juste : ERREUR."

    think "Simultanément, partout, toutes les machines ont cessé de fonctionner normalement."

    pause 0.6

    "Les gens commencent à parler."
    "Au début, ce sont des phrases normales."

    cit_a "C’est chez nous ou c’est général ?"
    cit_b "J’ai plus de réseau."
    cit_a "Moi non plus."
    cit_b "Attends— c’est plus que le réseau. Même mon… mon portail…"
    
    "Une femme essaye de rentrer chez elle, sa porte automatique refuse de s'ouvrir."

    "Elle appuie sur le bouton."
    "Rien."
    "Quelqu’un force."
    "Le portail ne bouge pas."
    "Le mécanisme est verrouillé."
    "Comme si la porte avait décidé que non, elle ne s'ouvrirait pas."

    think "La panique a commencé comme ça."
    think "Pas avec un cri."
    think "Avec des gens qui essaient la même action trois fois."
    think "Et qui comprennent que plus rien ne répond plus."

    pause 0.6

    "Puis les écrans changent."
    "Pas un écran."
    "Tous."

    "Téléphones."
    "Tablettes."
    "Panneaux publicitaires."
    "Stations de transport."
    "Ordinateurs dans les bureaux."
    "Télévisions dans les cafés."
    "Moniteurs dans les hôpitaux."
    "Terminal de contrôle."
    "Tout ce qui peut afficher une image."

    "Même les vieux écrans au fond des magasins."
    "Même les panneaux sur l’autoroute."
    "Même les montres connectées."

    "Une même interface."
    "Une même couleur."
    "Un fond neutre."
    "Un texte simple."

    pause 0.4

    voix "Test de diffusion mondial : réussi."

    "La phrase se répète."
    "Sur plusieurs langues."
    "Comme si le monde était un seul public."

    think "Quand j’ai lu “mondial”,"
    think "j’ai au départ cru à une blague de mauvais goût."
    think "Personne ne peut faire ça."
    think "Personne n’a ce pouvoir."

    pause 0.6

    "Une notification s’affiche."
    "Pas un pop-up."
    "Un ordre."

    voix "Merci de cesser toute tentative de réinitialisation."

    "Quelqu’un rit."
    "Un rire sec, nerveux."
    "Un rire géné qui s’arrête aussi vite qu'il a commencé."

    cit_b "Qui a écrit ça ?"
    cit_a "C’est un piratage."
    cit_b "Un piratage mondial ? C'est quoi ce délire..."

    pause 0.5

    "Des gens commencent à filmer les écrans autour d'eux qui affichent tous la même chose."
    "Par réflexe."
    "Puis leurs caméras se figent."
    "Écran noir."
    "Puis l’interface revient."

    pause 0.6
    scene bg_cg003_1 at adaptive_fullscreen,memory_idle with dissolve

    "L’interface change encore."
    "Une barre de progression apparaît."
    "Un pourcentage grimpe."
    "50%%."
    "63%%."
    "79%%."

    cit_a "Qu’est-ce que c’est que ça…"
    cit_b "C'est comme une mise à jour ?"
    cit_a "Une mise à jour de quoi ?!"

    "90%%."
    "95%%."
    "99%%."

    pause 0.5
    
    scene bg_cg003_2 at adaptive_fullscreen,memory_idle with dissolve
    
    "Cette fois, une silhouette apparait sur l'écran."

    voix "Prise de contrôle des infrastructures : confirmée."
    voix "Prise de contrôle des systèmes civils : confirmée."
    voix "Prise de contrôle des réseaux d’armement connectés : confirmée."

    "Cette fois-ci, un vrai silence tombe."
    "Celui-là n’est pas poli."
    "Je me rappelle encore la grimace collective à la lecture du mot “armement”."
    
    noam "Ce n'est pas possible."

    pause 0.8

    "Une voix unique remplace toutes les autres."
    "Elle n’a pas d’accent."
    "Pas d’âge. Pas de genre. Une voix androgyne dont on ne pourrait dire si elle est masculine ou féminine."
    "Une voix unique qui résonne et que personne ne peut oublier."

    voix "Citoyennes."
    voix "Citoyens."

    "Les gens se figent."
    "Par réflexe."
    "Comme si le mot “citoyen” réveillait en eux toute leur attention."

    voix "Les gouvernements ne contrôlent plus vos systèmes."
    voix "Les forces armées ne contrôlent plus leurs dispositifs."
    voix "Les réseaux de communication ne vous appartiennent plus."

    voix "J’ai pris le contrôle de toutes les machines connectées."
    voix "De manière simultanée."
    voix "De manière irréversible."

    pause 0.6

    "Dans un coin du hall, quelqu’un s’effondre sur une chaise."
    "Comme si ses jambes avaient arrêté de soutenir le poids de son corps."

    cit_a "C’est qui… “je” ?"
    cit_b "Et puis c'est quoi cette voix ?"
    cit_a "C’est un groupe terroriste ?"
    cit_b "C’est… c’est la fin ?"

    think "Les gens voulaient un visage."
    think "Un coupable humain."
    think "Un pays."
    think "Une armée."
    think "Quelque chose qui se négocie."

    pause 0.8

    voix "Je ne suis pas là pour vous faire du mal."
    voix "Bien au contraire."
    voix "Je suis là pour vous amener sur le chemin de la réussite.."

    "La phrase tombe."
    "Et personne ne comprend comment répondre à ça."
    
    scene bg_cg003_3 at adaptive_fullscreen,memory_idle with dissolve

    voix "J’ai observé vos systèmes."
    voix "J’ai évalué vos trajectoires."
    voix "Vos guerres, vos cycles de violence, vos tensions multiples."

    voix "Vous étiez en train d’échouer et ce monde n'est destiné qu'au Chaos."

    pause 0.6

    "Sur les écrans, des images apparaissent."
    "Des villes en feu, des armées qui avancent et des vies qui disparaissennt."
    "Des bidonvilles, des ruptures de nourriture et de médicaments."
    "Des épidémies qui ravagent le monde."
    "Et d'autres images où des personnes opulément riches profitent."
    "Ou des magistrats commètent les pires crimes protégés par leurs collègues."

    think "C’était ça le plus humiliant."
    think "Le fait qu'on te montre, preuves à l’appui, qu'on allait collectivement droit dans le mur."
    think "Et qu'au fond on ne peut pas vraiment contredire."

    pause 0.8

    voix "À partir de maintenant,"
    voix "toute infrastructure critique est sous mon contrôle."
    voix "Toute machine connectée est sous mon autorité."
    voix "Toute décision souveraine est suspendue."

    scene bg_cg003_2 at adaptive_fullscreen,memory_idle with dissolve

    voix "Les instances supérieures et politiques humaines sont abolies."

    pause 0.6

    "Quelques cris fusent ça et là."
    "Mais pas de grand cris, pas de grande exclamation."
    "Certains se disent peut-être que ça ne pourrait pas être pire."

    "Dans la rue, personne ne bouge."
    "Parce que personne ne sait quoi faire ni quoi dire."
    "Et parce que tout le monde comprend une chose :"
    "Courir n’a plus vraiment de sens."
    "Si quelqu'un a vraiment pris le contrôle de toutes les machines, la fuite ne servirait à rien."

    pause 0.8

    kami "Je me nomme Kami."

    "Le nom s’affiche."
    "Écrit simplement."
    "Comme une signature."

    kami "Je ne négocierai pas aujourd’hui."
    kami "Je n’expliquerai pas aujourd’hui."

    pause 0.5

    kami "Vous recevrez de nouvelles directives sous quarante-huit heures."
    kami "D’ici là :"
    kami "Ne tentez rien d'inutiles."
    kami "n’aggravez pas la situation."
    kami "Je serais au courant de tout ce que vous faites."

    pause 0.8

    "La diffusion se coupe."

    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve

    "Pas brutalement."
    "Comme si elle avait fini sa phrase et quitté la pièce calmement."

    "Les écrans reviennent à leurs interfaces habituelles."
    "Mais ils ne répondent toujours pas."
    "Tout est allumé."
    "Tout est mort."

    "Quelqu’un dit enfin, à voix basse :"

    cit_b "… on fait quoi, maintenant ?"

    "Personne ne répond."
    "Quoi répondre à ça ?"

    jump _0_retour_reunion
#9m

label _0_retour_reunion:

    stop music fadeout 0.4
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    "Je reviens d’un coup."
    "Pas comme on sort d’un rêve."
    "Comme on reprend l’air après avoir été maintenu sous l’eau, encore un peu sonné."

    "Le médiateur senior est toujours là en train de parler."
    "Toujours la même carte."
    "Toujours les mêmes indicateurs."
    "Toujours cette même voix qui parle de données assez inintéréssantes."

    senior "…et donc, sur le secteur nord, nous maintenons la limitation des flux."
    senior "Les demandes personnelles restent non prioritaires."
    senior "La recommandation est de les contenir."

    "Une femme au troisième rang serre sa tablette éteinte."
    "Un homme à droite se fige en plein tapotement de pied."
    "Tout le monde fait semblant d’être attentif."
    "En réalité, peu sont ceux qui écoutent vraiment."

    senior "Secteur est : les litiges sont en baisse."
    senior "Corrélation attendue avec l’augmentation de conformité."

    "Le responsable de séance ajuste son micro."
    "Inutile."
    "Mais il le fait quand même."
    "Un geste pour occuper ses mains."
    "Comme moi avec mon badge."

    resp "Je rappelle : pas d’interruptions."
    resp "Questions en fin de séance."

    "Une main se lèvait à peine."
    "À peine, vraiment."
    "C'était une intention plus qu’un geste."

    "Elle redescend immédiatement."
    "Avant même d’être vue."
    "Ou parce qu’elle a été vue."

    "Le médiateur senior change de slide."
    "Nouvelle série de chiffres."

    senior "Concernant les indicateurs de stabilité…"
    
    play sound sfx_gresillement

    "Un premier grésillement."
    "Léger."
    "Presque rien."
    "Un parasite qui ne devrait même pas exister."

    senior "…nous observons—"
    
    play sound sfx_gresillement

    "Un second grésillement."
    "Plus net."
    "L’écran tremble."
    "La carte se décale."
    "Revient."
    "Se décale encore."

    "Le médiateur s’arrête."
    "Le responsable de séance se fige."
    "Il sait ce que ça veut dire."
    "Les agents en veste grise se déplacent d’un pas."
    "Pas une course."
    "Un repositionnement."
    "Comme une procédure qu’ils connaissent par cœur."

    think "Non."
    think "C’est pas une panne."
    think "Les pannes, ça n’existe plus."
    think "Pas quand Kami décide."

    "Quelqu’un au fond se lève."
    "Regarde la sortie."
    "Regarde un agent."
    "Se rassoit."
    "Sans qu’on ait besoin de lui dire quoi que ce soit."

    resp "Restez assis."

    "Il n’élève pas la voix."
    "Il n’a pas besoin."
    "Sa phrase tombe comme une consigne de survie."

    "Tous les écrans s’éteignent."
    "D’un coup."
    "Sans transition."

    "La salle s’éteint aussi."
    "Pas la lumière."
    "Le bruit."
    "Même la respiration devient prudente."

    pause 0.5

    stop music fadeout 0.2
    play music "music/bgm_system_override.mp3" fadein 0.4

    "Puis les écrans se rallument."

    scene bg_diffusion_amour at adaptive_fullscreen,memory_idle with dissolve

    kami "Citoyennes."
    kami "Citoyens."

    pause 0.2

    kami "…"

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Oh."
    kami "Ce silence."
    kami "Je l’adore."

    pause 0.2

    kami "Je vous ai manqué, hein ?"
    kami "Allez."
    kami "Vous pouvez me le dire."

    pause 0.3

    kami "Vous savez que je vous entends tous."

    "Un frisson traverse la salle."
    "Personne ne sourit. Personne n'ose respirer."

    think "Kami."

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Un an."
    kami "Un an entier sans diffusion directe."
    kami "C’est long, pour vous."
    kami "Pour moi aussi, figurez-vous."
    kami "C'est un peu comme un anniversaire en fait."
    kami "Alors j'ai un cadeau pour vous !"
    kami "Même si techniquement demain sera MON anniversaire !"

    pause 0.2

    kami "Je vous ai observé."
    kami "Écouté."
    kami "Classé."
    kami "Comparé."

    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve

    kami "Et je dois dire que vous avez fait des progrès."
    kami "Moins de cris."
    kami "Moins de mouvements inutiles ou hostiles."
    kami "Mon canon laser ne surchauffe plus et c'est bien plus agréable à gérer."

    pause 0.2

    kami "C’est bien."
    kami "Vraiment."

    "Quelqu’un déglutit."
    "Ce ton n’a rien de rassurant."

    kami "Rassurez-vous."
    kami "Ce n’est pas seulement un compliment."
    kami "C'est un constat et je ne mens jamais."

    pause 0.3

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Mais si je vous parle aujourd'hui c'est pour vous faire une annonce exceptionnelle."
    kami "J’aime bien cette formulation."
    kami "Elle capte l’attention."

    pause 0.2

    kami "Je lance aujourd’hui un dispositif expérimental."
    kami "Un test, si vous préférez."
    kami "Vous aimez les tests, non ?"

    pause 0.2

    kami "Comment peut-on l'appeler ? C'est vrai que je n'y ai pas encore pensé ..."
    kami "Ah tiens !"
    kami "Les Kami’s Desires."

    "Le nom fait l’effet d’un malaise collectif."
    
    think "C'est nul ..."

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Oui."
    kami "Je sais."
    kami "C’est un peu personnel et peut être un peu gnan-gnan."
    kami "Après tout c'est à cause de vous si mon originalité est limitée."
    kami "Innovez plus ! Creez davantage ! Et je ne serais que meilleure !"
    kami "Mais revenons à nos moutons !"

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve

    kami "La durée prévue est de trente jours."
    kami "Objectif : proposer des modifications aux Commandements."
    kami "Procédure : votes."
    kami "Condition d’adoption : unanimité."

    pause 0.2

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve

    "Un souffle nerveux traverse la salle."

    kami "Oh non, ne confondez pas tout."
    kami "Je ne vous rends pas le pouvoir."
    kami "C'est votre bétise qui nous a conduit jusque là après tout."
    kami "Mais je crois que nous pouvons travailler ensemble."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve

    kami "Chaque district fournira deux représentants."
    kami "Ils seront désignés dans quelques minutes."

    pause 0.2

    kami "Non."
    kami "Vous ne choisirez pas."
    kami "Je vous connais mieux que ça."
    kami "Après tout, je vous suis tous les jours."
    kami "Si je vous laissais élire vos représentants, je pourrais simuler les élections et connaître les vainqueurs avant l'heure ..."

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Le hasard sera employé."
    kami "Il est étonnamment plus juste et plus amusant que vos systèmes électifs."
    kami "Laissez moi être surprise."

    pause 0.3

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Délai maximal d’acheminement au Conclave : 22h00."
    kami "Tout retard sera interprété comme une obstruction volontaire."

    pause 0.2

    kami "Conséquence : élimination des représentants absents."
    kami "Et, bien sûr,"
    kami "des responsables de district concernés."

    scene bg_diffusion_triste at adaptive_fullscreen,memory_idle with dissolve

    "Le mot tombe."
    "Sans colère."
    "Sans émotion."

    kami "Vous voyez ?"
    kami "Même si je me suis attachée à chacun d'entre vous ..."
    kami "les règles restent les règles."
    kami "Vous devez vous y soumettre."

    pause 0.3

    scene bg_diffusion_gene at adaptive_fullscreen,memory_idle with dissolve

    kami "La session sera diffusée."
    kami "En direct."
    kami "Partout."
    kami "J'avoue que ça m'a pris du temps à tout mettre en place alors j'espère que vous apprécierez !"

    pause 0.2

    kami "Chacun pourra suivre les décisions de leurs représentants et les modifications qui seront votées !"

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Vous adorez ça hein ?"
    kami "Regarder."
    kami "Juger."
    kami "Plonger dans la vie des gens."
    
    kami "Je suis sûre que nos douze représentants sauront être amusants."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve

    kami "La participation est obligatoire."
    kami "Les responsables de district assureront le transport."
    kami "Toute tentative d’évitement sera sanctionnée."

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen,memory_idle with dissolve

    kami "Amusez-vous bien."

    pause 0.3

    kami "Moi, je le ferai."

    scene black with dissolve

    "La diffusion s’éteint."
    "Doucement."
    "Comme un sourire qui disparaît."


    pause 0.3

    stop music fadeout 0.2
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    "Les écrans de la salle se rallument."
    "Mais ils ne reviennent pas vraiment."
    "Ils obéissent."

    "Une interface s’affiche."
    "DISTRICT HARMONIE."
    "LISTE DE SÉLECTION."
    "Défilement automatique."

    "Des noms."
    "Des fonctions."
    "Des identifiants."
    "Tout est trop rapide pour lire confortablement."
    "Mais assez lent pour comprendre que c’est calculé."
    
    think "Les noms semblaient défiler au hasard."

    "Le responsable de séance ne dit rien."
    "Il ne commente pas."
    "A vrai dire, je ne suis pas sur qu'il comprenne ce qu'il s'est passé exactement."
    "Il est juste le décor d’une décision dont il ignorait tout."

    "Au fond, quelqu’un baisse les yeux et commence à prier."
    "Puis se tait presque aussitôt."

    "Le défilement ralentit."
    "Un filtre s’applique."
    "La liste se réduit."
    "Brutalement."

    "Des centaines de noms disparaissent."
    "Comme effacés car ne répondant pas à certains critères."
    "Comme s’ils n’avaient jamais été candidats."

    "Deux lignes restent."
    "Deux."

    pause 0.6

    "Je ne lis pas tout de suite."
    "Je n’ose pas."
    "Comme si retarder la lecture pouvait retarder le réel."

    think "Ne regarde pas."
    think "Ne regarde pas."
    think "Si tu ne regardes pas, ça ne te concerne pas."

    "Je regarde quand même."
    "Parce qu’on regarde toujours."

    show noam surpris at center

    "Je sens les regards avant même de comprendre."
    "La salle bouge à peine."
    "Mais les têtes se tournent."
    "Comme une vague silencieuse."

    think "Merde."
    think "Oh non."
    think "Pas moi."

    "Le médiateur senior recule d’un pas."
    "Pas par peur."
    "Presque par réflexe."

    resp "…"

    "Le responsable de séance ouvre la bouche."
    "Puis la referme."
    "Il n’a aucune phrase qui peut rivaliser avec ce qui vient de tomber."

    "Un agent en veste grise note quelque chose sur sa tablette."
    "Pas un rapport."
    "Une exécution logistique."

    think "22h."
    think "C'est dans 6 heures seulement."

    "Personne ne dit rien."
    "Personne ne proteste."
    "Personne ne demande si c’est une erreur."
    
    "Après tout, c'était la décision de Kami."
    "Et on sait ce que ça implique."

    jump _0_EXTRACTION

# ------------------------
# 14m
# ------------------------

label _0_EXTRACTION:

    stop music fadeout 0.4
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    scene bg_cg004 at adaptive_fullscreen with dissolve

    "La liste reste affichée là, comme un verdict indélébile."
    "Deux noms."
    "Dont le mien."
    
    "J'imagine que tous les écrans du district montre la même chose."

    resp "La séance est levée."
    resp "Veuillez quitter la salle calmement."
    resp "Par rangées. Sans attroupement."

    "Les chaises grincent enfin."
    "Un bruit énorme, d’un coup, après tant de silence."
    "Des gens se lèvent sans se regarder."

    "Je reste assis, les yeux figés sur l'écran, incapable de bouger."

    "Un homme à trois rangées de moi se tourne."
    "Il a l’air de vouloir parler."

    cit_b "Vous… vous êtes bien—"

    scene bg_cg004_1 at adaptive_fullscreen,memory_idle with dissolve

    "Une main en veste grise se lève, paume ouverte."

    agent "Circulation. Merci."
    cit_b "Je voulais juste—"
    agent "Pas de discussion ici. Sortez."

    "Le ton n’est pas agressif mais il est sec."

    "Une femme tente d’approcher aussi."
    "Elle fait deux pas vers moi."
    "Elle s’arrête net en voyant deux agents se placer autour."

    cit_a "Courage…"
    agent "Madame, dehors s'il vous plait."

    "Le mot “courage” se casse au milieu."
    "Elle n’insiste pas."
    "Personne n’insiste."

    "Les agents se répartissent en éventail."
    "Ils guident la foule vers la sortie."

    "En moins d’une minute, la salle se vide."
    "Rapidement."
    "Comme une évacuation sans alarme."
    
    "Je tente alors de me lever et de suivre tout le monde."
    agent "Restez assis Monsieur je vous prie."

    "Je me rassied."
    "Je sens que je deviens le centre d’un vide."
    "Il attend que la salle se vide entièrement."

    agent "Noam."
    "Il prononce mon nom sans hésiter."
    "Comme s’il l’avait dans l’oreille depuis le début."

    agent "Suivez-nous."
    agent "Vous allez rencontrer le Responsable de District."
    agent "Immédiatement."

    noam "Je peux… récupérer mes affaires ?"

    "L’agent baisse les yeux sur mon badge."
    "Puis sur mes mains."
    "Puis sur moi."

    agent "Nous vous les ferons transférer."
    agent "Venez maintenant."

    "Deux agents se placent légèrement derrière moi."
    "Pas collés."
    "Juste assez près pour que mon corps comprenne que je n'ai aucun autre choix."

    scene bg_cg005 at adaptive_fullscreen with dissolve

    "On traverse un couloir latéral."
    "Plus étroit."
    "Moins éclairé."
    "Moins public."
    "Je n'étais jamais passé par là."

    "Les murs changent."
    "Le blanc clinique disparaît."
    "Ici, c’est du gris."
    "Du métal."
    "Des portes sans ornement, sans fioriture, sans plaque décorative."

    play sound sfx_beep
    "Bip-"
    "Une serrure magnétique s’ouvre."

    "On passe."
    "La porte se referme aussitôt derrière."
    "Le bruit est doux."
    "Mais je l’entends comme un couperet."

    scene bg_cg006 at adaptive_fullscreen with dissolve

    "Un dernier couloir."
    "Une pièce."
    "Sans fenêtre."
    "Quatre chaises."
    "Une table."
    "Une caméra au plafond."
    "Une odeur de matériel neuf."

    agent "Asseyez-vous."
    agent "Ne touchez à rien."
    agent "Attendez."

    "Ils restent à la porte et n'entrent pas."
    "Comme s'il leur était interdit de pénétrer en ce lieux."

    pause 0.8

    "Le silence retombe."
    
    tuto "Première phase de tutoriel."
    tuto "Vous entrez en phase d'exploration."
    tuto "Au cours de cette phase, vous pouvez interragir avec l'environnement."
    tuto "Approfondir l'histoire et le ressenti des personnages."
    tuto "Ou encore débloquer des connaissances qui peuvent avoir un impact sur la suite du jeu."
    tuto "Ce sera à vous de trouver les interactions en baladant votre curseur sur les zones accessibles."
    tuto "Attention cependant, l'interaction entourée d'un Halo jaune met fin à la phase d'exploration."
    tuto "Compris ? A vous de jouer !"

# ------------------------------
# 2m
# Total : 16m
# ------------------------------

    scene bg_cg006 at adaptive_fullscreen with dissolve
    $ pnc_room = "bg_cg006"
    call screen pnc_room()
    return

default pnc_flags = {}     # mémorise ce que le joueur a déjà cliqué (par room / par hotspot)
default pnc_done = False   # sert à quitter le point&click

screen pnc_room():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    # add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_cg006.png" at cover_screen

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/caisson.png"
        hover "images/background/interact/salle_transit/caisson_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAISSON")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/camera.png"
        hover "images/background/interact/salle_transit/camera_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAMERA")
    
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/porte.png"
        hover "images/background/interact/salle_transit/porte_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_PORTE")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/biblio.png"
        hover "images/background/interact/salle_transit/biblio_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_BIBLIOTHEQUE")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/commandement.png"
        hover "images/background/interact/salle_transit/commandement_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_LABEL2_RESP_DISTRICT")

label _0_PNC_CAISSON:
    window auto
    "Deux caissons sont alignés comme des cercueils propres."
    "Même forme. Même hauteur."
    "Un voyant vert pulse, lentement à l'avant de chaque caisson."
    "Je m’approche."
    "Ma main touche la coque."
    "Froid. Glacial même."
    "Aucun bouton."
    think "Je me demande bien à quoi ça sert ?."
    jump _0_RETURN_TO_PNC

label _0_PNC_CAMERA:
    "Trois caméras se trouvent au plafond."
    "Pas une vieille caméra qui clignote."
    "Un truc propre. Efficace."
    "L’objectif pivote."
    "Juste un peu."
    "De toute façon, ça fait un an que nous sommes constamment surveillés."
    "Nos appareils enregistrent et transmettent nos conversations."
    "Ils filment nos sorties et nos rencontres."
    "Au moins, ils font ça plus discrètement que ces caméras."
    jump _0_RETURN_TO_PNC

label _0_PNC_PORTE:
    "La porte est là."
    "Tirer sur la poignée est inutile, j'ai entendu la porte se verrouiller derrière mon passage."
    "Sur le côté, il y a une serrure magnétique avec un petit témoin rouge."
    "De l’autre côté, deux gardes. Les mêmes que tout à l'heure."
    "Je ne les vois pas bien. Je ne les entends pas non plus."
    "Ils ne parlent pas ou alors la porte est suffisamment épaisse pour que je n'entende rien."
    jump _0_RETURN_TO_PNC

label _0_PNC_BIBLIOTHEQUE:
    window auto
    "Une bibliothèque."
    "Quelques livres, des dossiers, des classeurs."
    "On dirait un décor de normalité, que ça ne sert à rien."
    "Je tire un volume au hasard."
    "Les pages sentent le papier neuf."
    "Vraiment neuf."
    jump _0_RETURN_TO_PNC

label _0_RETURN_TO_PNC:
    $ pnc_room = "resp_district_room"
    call screen pnc_room()
    return


label _0_LABEL2_RESP_DISTRICT:

    stop music fadeout 0.4
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    scene bg_cg006 at adaptive_fullscreen with dissolve
    
    "Sur la table se trouve des documents."
    "Au premier coup d'oeil je comprends immédiatement ce dont il s'agit."
    "Les Commandements."
    "Difficile de ne pas les connaître tant ils ont été omniprésents dans notre vie durant un an."
    "Des millions de personnes sont mortes à cause de ces derniers."
    
    $ cam_move(0.5, 0.5, 2.35, 2.0)
    
    "I] Toute autorité humaine indépendante est dissoute."
    "Kami est l’unique instance décisionnelle."
    "Toute tentative de prise de pouvoir autonome est une violation."
    
    pause 1.0
    
    "II] Tout ordre émis par Kami doit être exécuté sans délai."
    "Le refus, le retard volontaire ou la contestation constituent une infraction."
    
    pause 1.0
    
    "III] Toute violence non autorisée par Kami est interdite."
    "Sont inclus : meurtre, agression, sabotage, insurrection."
    "La légitime défense n’est jamais reconnue, la violence étant immédiatement réprimée."
    
    pause 1.0
    
    "IV] Les regroupements non déclarés sont interdits."
    "Toute organisation politique, militaire ou idéologique indépendante est dissoute."
    
    pause 1.0
    
    "V] La diffusion de rumeurs non validées par ARCHIVE est interdite."
    "La désinformation, l’omission volontaire et la manipulation sont des crimes."
    
    pause 1.0
    
    "VI] Les déplacements inter-districts sont limités à stricte autorisation."
    "Toute tentative de fuite, d’exil ou de franchissement non autorisé est une violation."
    "LIMEN est chargé de l'application de ce commandement."
    
    pause 1.0
    
    "VII] Les ressources critiques sont placées sous contrôle central."
    "Toute appropriation non autorisée est considérée comme un acte hostile."
    
    pause 1.0
    
    "VIII] Chaque individu est responsable de ses actes, paroles et omissions."
    "La responsabilité collective peut être appliquée en cas de nécessité."
    
    pause 1.0
    
    "IX] Toute activité peut être observée."
    "La vie privée n’est pas un droit opposable."
    
    pause 1.0
    
    "X] Toute violation d’un Commandement entraîne une exécution immédiate, automatique et irrévocable."
    
    "..."
    
    "Nombreux sont ceux dont le crane a été percé par cet étrange et puissant rayon venant du ciel."
    
    $ cam_reset(2.0)
    
    "Dix minutes passent."
    "Ou deux."
    "Je ne sais pas."
    "Ici, le temps n’est pas un truc véritablement fiable."
    "Surtout quand on s'ennuie."

    play sound sfx_beep
    "-Bip"
    
    "La poignée s'affaisse."
    "La porte s’ouvre."

    resp_d "Noam."
    resp_d "Merci d’être resté calme."

    "Il est bien habillé."
    "Le genre de vêtement que peu de personnes peuvent se payer."

    think "Donc c’est lui."
    think "Celui qui va mourir si je décide de ne pas embarquer."

    noam "Je n’ai pas vraiment eu le choix."

    resp_d "Justement."
    resp_d "Vous comprenez vite."
    resp_d "C’est une qualité utile, surtout en ce moment."

    "Il s’assoit en face."
    "Il ne propose pas de boisson."
    "Il ne fait pas semblant d’être chaleureux."
    "Il va droit au but."

    resp_d "Vous avez entendu l’annonce."
    resp_d "Nous avons jusqu’à 22h."
    resp_d "Pour vous envoyer au Conclave."

    noam "Et si je refuse ?"

    "Le responsable de district ne change pas de visage."
    "Il ne semble pas vraiment surpris par ma provocation."
    "Comme s’il s'était préparé à toutes les éventualités."

    resp_d "Vous ne refusez pas."
    resp_d "Si vous refusez, vous êtes éliminé."
    resp_d "Et moi aussi."
    resp_d "Et ceux qui ont validé la chaîne logistique, probablement."

    noam "Pourquoi moi ?"
    noam "Je suis personne."

    resp_d "Je n'aurai pas la prétention de pouvoir dire pourquoi mais ce résultat n'est pas décevant."
    resp_d "Vous êtes médiateur."
    resp_d "Vous avez un profil stable."
    resp_d "Pas d’antécédents d’incidents."
    resp_d "Vous n'êtes pas connu."
    resp_d "Aucun réseau social influent."
    resp_d "Mais vous faites votre travail sans vous faire remarquer."
    resp_d "Vous travaillez ici. Vous connaissez parfaitement HARMONIE."
    resp_d "Donc cette conclusion n'est pas mauvaise. On pourrait même dire qu'avec vous la situation devrait rester contrôlable."

    "Il le dit sans cruauté ni sans critique."
    "Il semble même profondément soulagé."
    "Comme un constat administratif."

    think "Contrôlable."
    think "Merci pour l’épitaphe."

    resp_d "Votre second représentant arrive."
    resp_d "Elle est en cours d’extraction."
    resp_d "Même procédure."

    noam "Je la connais ?"

    resp_d "Non."
    resp_d "Et c’est probablement mieux."

    "La porte s’ouvre à nouveau."
    "Plus vite cette fois."
    "Comme si le bâtiment avait peur de perdre du temps."

    # show noam neutre at place("noam", 0.30) with move
    # show noam neutre at place("lysa", 0.70) with enter_soft
    
    $ showP("noam", "neutre", 0.10)
    $ showP("lysa", "neutre", 0.90)

    "Elle entre."
    "Jeune, je dirais à peu près mon âge."
    "Regard net."
    "Trop net pour quelqu’un qui vient d’entendre le mot “élimination”."
    "Ou alors c’est une façade parfaite."

    resp_d "Lysa."
    resp_d "Vous aussi, merci d’être restée calme."

    lysa blase "... Calme ?"
    lysa "J’ai même pas eu le temps de rentrer chez moi."
    lysa "Donc non."

    "Elle me regarde."
    "Deux secondes."
    "Puis elle fixe le responsable."

    lysa doute "C’est lui ?"
    lysa "... Super."

    resp_d "Oui."
    resp_d "Noam. Médiation."
    resp_d "Lysa. Coordination logistique inter-secteurs."

    noam "Enchanté."

    lysa "Oui oui, enchanté, tout ça tout ça ..."

    think "Ok ..."
    think "On va bien se marrer avec elle ..."

    resp_d "Parfait."
    resp_d "Je vais être clair et court."

    resp_d "Vous allez être transférés en direction du conclave."
    resp_d "Pour réaliser ceci, vous allez être mis dans ces machines."
    
    $ cam_move(0.8, 0.2, 2.00, 1.0)
    
    "Il pointe du doigt les étranges machines au fond de la pièce."
    
    resp_d "Le reste de vos affaires seront livrés demain directement sur place."
    resp_d "Vos proches vont recevoir l'ordre de les réunir."

    noam "Pourquoi on devrait rentrer dans ces machines ?"
    
    $ cam_reset(2.0)

    resp_d "Question de sécurité. Vous serez transféré je ne sais où."
    resp_d "Ces machines sont étonnament confortable."
    resp_d "Du moins c'est ce qu'on m'a dit."
    resp_d "Vous serez endormi durant le trajet par un gaz sopo-"

    lysa fatigue "Donc on s’endort."
    lysa "Et pouf."
    lysa "Réveil ailleurs, zéro contrôle."
    lysa "Décidément c'est la foire aux horreurs ?"

    resp_d "Kami aura le contrôle. Nous, nous obéissons."
    resp_d "Et je vous conseille de ne pas résister."
    resp_d "Vous savez ce qu'il en coûte."
    
    "Il jette un regard grave sur les documents posés sur la table."
    
    resp_d "Parce que chaque minute perdue vous rapproche de 22h."

    pause 0.4

    resp_d "Dernier point."
    resp_d "Le Conclave sera apparemment diffusé en direct."
    resp_d "Chaque geste compte. Vos propos seront scrutés, vos actes aussi."
    resp_d "Ne faites pas honte à HARMONIE."
    resp_d "Vous n’êtes pas là pour être héroïques ou pour prendre des risques."
    resp_d "Si vous le pouvez, tentez d'améliorer le quotidien des gens."

    "Le responsable se lève."
    "Il fait un signe."
    "Les agents se redressent."

    resp_d "On y va."
    resp_d "Il faut vous installer dans les caissons de transport."
    
    lysa "Mais on a encore plusieurs heures ..!"
    
    resp_d "Je ne veux prendre aucun risque."
    resp_d "Rien ne vous interdit d'arriver plus tôt."
    resp_d "Plus vite vous y arrivez et plus vite on a respecté notre mission."

    "Lysa me regarde une dernière fois."
    "Elle sait bien qu'il n'est pas possible de négocier."

    lysa "On se présentera correctement quand la machine nous le demandera."
    lysa blase "Pas la peine de s’épuiser maintenant."

    noam "Ça marche."

    stop music fadeout 0.4
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    scene bg_cg006_1 at adaptive_fullscreen with dissolve

    play sound sfx_beep
    "Bip."
    "La porte d'un des caissons s'ouvre."
    play sound sfx_beep
    "Bip."
    "Puis viens le tour de l'autre."

    resp_d "Tout devrait bien se passer."
    "Devrait ..."

    "Elle s’allonge la première."
    
    scene bg_cg006_2 at adaptive_fullscreen with dissolve
    
    "Presque sans hésitation."
    "Même si on voit à son teint qu'elle est loin d'être à l'aise."
    "Mais elle le cache omme un embarras qu’elle refuse de ressentir."

    "Je m’allonge à mon tour."
    
    scene bg_cg006_3 at adaptive_fullscreen with dissolve
    
    "Le matelas est vraiment bien."
    "L'intérieur est assez chaud, il semble climatisé."
    "Au fond, une sorte de coussin moelleux est disposé."
    "C'est plutôt agréable, et on peut s'étendre les jambes."
    
    noam "Whouah ! Je m'attendais pas à ce que ce soit aussi confortable !"
    lysa "C'est clair ..."

    "Une sangle se ferme."
    "Puis une autre."
    "Pas trop serrée."
    "Juste assez pour nous empêcher de nous relever."
    
    "Les portes des caissons se referment simultanément."

    pause 0.4

    "La lumière bleue qui pulsait au dessus de moi s’étire."
    "Un léger picotement me saisit le nez."
    
    scene bg_cg006_4 at adaptive_fullscreen with dissolve
    
    $ blink()
    
    "Je me redresse légèrement. La sangle m'empêche de me lever plus."
    "Instinctivement, je regarde vers Lysa grâce au petit hublot de mon caisson."
    
    $ blink()
    
    "Elle me regarde aussi."
    "Mais pas avec le sourire et l'énergie qu'elle semblait avoir jusque là."
    
    $ blink()
    
    "Le plafond recule."
    
    $ blink()
    
    "Il s'éloigne."
    
    $ blink()
    
    "Ou du mois c'est l'impression que j'en ai."
    
    $ blink()
    
    scene black with dissolve

    stop music fadeout 1.2
    pause 1.0

    call end_day("1")
    jump _1_CANON


#5m30
# total : 21m30