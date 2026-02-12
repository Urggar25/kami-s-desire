# -----------------------------------------------------------------------
# LIENS — KAEL
# -----------------------------------------------------------------------

default kael_link = 0

label KAEL_LINK_INTERACT:

    menu:
        "Passer du temps avec Kael ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if kael_link == 0:
        jump kael_link_1
    elif kael_link == 1:
        jump kael_link_2
    elif kael_link == 2:
        jump kael_link_3
    elif kael_link == 3:
        jump kael_link_4
    elif kael_link == 4:
        jump kael_link_5

    if last_room_label:
        jump expression last_room_label
    return

label kael_link_1:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("kael", "reflechit", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "La baie vitrée renvoie un reflet tremblant de la salle."
    play sound sfx_beep
    "Un bip lointain pulse, puis disparaît."
    noam "Tu regardes encore la dispute de tout à l'heure dans ta tête ?"
    kael "Oui."
    kael "Mara parlait comme si chaque seconde coûtait un membre de l'équipe."
    kael "Sael répondait comme s'il défendait sa dernière frontière."
    noam "Et toi, tu n'as pas bougé."
    kael "Non."
    noam "Tu aurais pu les couper."
    kael "J'aurais pu, oui."
    kael "Mais parfois, couper une dispute, c'est juste déplacer l'explosion dans le couloir d'à côté."
    "Kael suit du regard un point invisible dans le vide."
    kael "Je les ai observés respirer."
    kael "Quand Mara serre la mâchoire, sa voix monte d'un demi-ton."
    kael "Quand Sael cligne vite, il n'écoute déjà plus."
    noam "Tu analyses les gens comme des trajectoires."
    kael "Parce que c'en est."
    kael "Des angles, des vitesses, des impacts."
    noam "Ça reste des personnes."
    kael "Justement."
    kael "Les personnes mentent, les trajectoires beaucoup moins."
    play sound sfx_gresillement
    "Un léger grésillement traverse les haut-parleurs."
    noam "Tu n'as pas peur qu'on confonde ton silence avec de l'indifférence ?"
    kael "Si."
    kael "On le confond déjà."
    kael "Mais intervenir sans ouvrir d'issue, c'est faire semblant d'aider."
    noam "Donc ne rien faire, c'est agir ?"
    kael "Ne pas agir tout de suite, c'est choisir le terrain."
    kael "C'est accepter que la conséquence existe déjà."
    kael "C'est décider de ne pas ajouter ma panique à la leur."
    noam "Tu appelles ça du contrôle."
    kael "J'appelle ça de l'hygiène."
    kael "Quand deux personnes veulent avoir raison, une troisième voix est souvent un carburant."
    noam "Et le groupe autour ?"
    kael "Le groupe adore croire qu'il est public neutre."
    kael "En réalité, il choisit des champions et attend le choc."
    play sound sfx_clap
    "Un claquement lointain, peut-être une porte, résonne comme un applaudissement malvenu."
    kael "Dès que j'entends ce réflexe-là, je sais que la dispute n'est plus privée."
    noam "Et si ça dégénère ?"
    kael "Alors j'entre."
    kael "Pas pour gagner le débat."
    kael "Pour casser le rythme."
    "Je le vois poser deux doigts sur la rambarde, comme s'il calait sa pensée."
    kael "Le problème, ce n'était pas leur colère."
    kael "Le problème, c'était la salle qui voulait un vainqueur."
    noam "Tu pensais à ça pendant qu'ils criaient ?"
    kael "Je comptais les regards."
    kael "Combien soutenaient Mara par réflexe."
    kael "Combien soutenaient Sael par fatigue."
    kael "Combien attendaient juste une permission de se déchirer aussi."
    noam "Ça fait beaucoup à tenir d'un coup."
    kael "C'est pour ça que je parle peu."
    kael "Une phrase de trop et la pièce bascule."
    noam "Tu dis ça calmement, mais ça sonne lourd."
    kael "Parce que ça l'est."
    kael "L'inaction n'est pas du vide."
    kael "C'est une décision avec des coûts différés."
    noam "Tu assumes ces coûts ?"
    kael "Je les note."
    kael "J'essaie de les payer moi, avant qu'ils tombent sur quelqu'un d'autre."
    play sound sfx_beep
    noam "On dirait presque une doctrine."
    kael "Non."
    kael "Une méthode de survie."
    kael "Dans un endroit où tout le monde est à bout, parler vite est facile."
    kael "Parler juste, c'est plus rare."
    noam "Et toi, tu attends la phrase juste."
    kael "J'attends surtout le moment où elle peut encore servir."
    "Un silence épais se pose entre nous."
    kael "Je n'ai pas pris parti aujourd'hui."
    kael "Mais j'ai pris une décision."
    kael "J'ai choisi de ne pas transformer leur conflit en spectacle."
    noam "Tu penses que c'était la bonne ?"
    kael "Je pense que c'était la moins mauvaise."
    kael "Et parfois, c'est tout ce qu'on a."
    "Au loin, une porte coulisse avec un souffle métallique."
    kael "Demain, si ça recommence, j'entrerai plus tôt."
    kael "Pas pour les faire taire."
    kael "Pour leur rappeler ce qu'ils sont en train de perdre."
    noam "Tu vois."
    noam "Finalement, tu avais un plan."
    kael "J'avais une limite."
    kael "Ce n'est pas la même chose."
    "Il se redresse enfin, le regard clair."
    kael "Observer sans intervenir, ce n'est pas se retirer."
    kael "C'est tenir la ligne quand personne ne veut la voir."

    $ kael_link = 1
    jump FREE_TIME_END

label kael_link_2:

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("kael", "neutre", 0.70)
    $ showP("noam", "hesitation", 0.24)

    "L'archive sent la poussière chaude et le métal froid."
    play sound sfx_paper
    "Kael range des fiches sans regarder les titres."
    noam "Tu as l'air ailleurs."
    kael "Je revis une vieille scène."
    noam "Tu veux en parler ?"
    kael "Oui."
    kael "Pas pour me défendre."
    kael "Juste pour la poser quelque part."
    "Il glisse un dossier dans une fente, doucement."
    kael "Pont de service d'Orbite."
    kael "Quart de nuit."
    kael "Deux équipes se disputaient l'accès aux modules de réparation."
    noam "Une question de ressources ?"
    kael "Oui."
    kael "Et d'ego."
    kael "Toujours un peu des deux."
    noam "Tu étais responsable ce soir-là ?"
    kael "Non."
    kael "J'étais juste le plus calme dans le couloir."
    noam "Et tu as attendu."
    kael "J'ai évalué."
    kael "Le volume."
    kael "Les appuis."
    kael "Le niveau de fatigue."
    kael "J'ai pensé : ils vont craquer verbalement, puis redescendre."
    play sound sfx_drop
    "Un classeur glisse de l'étagère et claque au sol."
    kael "Ils n'ont pas redescendu."
    kael "Un coup est parti."
    kael "Puis un deuxième."
    kael "Ensuite, plus personne n'écoutait plus rien."
    noam "Il y a eu des blessés."
    $ showP("kael", "culpabilite", 0.70)
    kael "Un bras fracturé."
    kael "Une arcade ouverte."
    kael "Et un silence après, pire que la bagarre."
    noam "Tu es intervenu quand ?"
    kael "Trop tard."
    kael "Quand le mal était déjà concret."
    kael "Quand intervenir ne réparait plus, seulement limitait."
    noam "Tu t'en veux encore."
    kael "Je constate encore."
    kael "C'est différent."
    noam "En quoi ?"
    kael "La culpabilité veut une punition."
    kael "Le constat veut une règle pour la prochaine fois."
    noam "Et ta règle ?"
    kael "Ne pas confondre calme apparent et stabilité réelle."
    kael "Quand les regards cherchent un prétexte, la collision est déjà lancée."
    kael "Quand les mains bougent plus vite que les phrases, c'est trop tard pour débattre."
    "Il ramasse le classeur tombé, aligne ses coins avec précision."
    kael "Je n'ai pas d'excuse."
    kael "J'avais les informations."
    kael "J'ai mal lu le tempo."
    noam "Tu étais seul à devoir agir ?"
    kael "Non."
    kael "Mais j'étais là."
    kael "Ça suffit pour que ma part existe."
    noam "Tu n'essaies même pas de minimiser."
    kael "Parce que minimiser ne protège personne ensuite."
    play sound sfx_beep
    "Un signal court ponctue la pièce comme un métronome."
    kael "Le pire, ce n'est pas le souvenir du sang."
    kael "Le pire, c'est la seconde exacte où j'ai su que j'aurais dû parler avant."
    noam "Cette seconde reste ?"
    kael "Oui."
    kael "Elle revient dès que j'entends deux voix se tendre."
    noam "Ça doit peser."
    kael "Ça cadre."
    kael "Le poids peut servir de garde-fou."
    noam "Tu as revu les personnes concernées ?"
    kael "Oui."
    kael "L'un ne m'en voulait pas."
    kael "L'autre ne me regardait plus pareil."
    kael "Les deux avaient raison à leur manière."
    noam "Tu leur as dit quoi ?"
    kael "Que j'avais attendu trop longtemps."
    kael "Rien de plus."
    kael "Pas de grand discours."
    kael "Pas d'habillage."
    "Il ferme le tiroir d'archive avec un clic net."
    kael "Depuis, quand je sens une scène glisser, je coupe tôt."
    kael "Même si je passe pour abrupt."
    kael "Même si on me dit que j'exagère."
    noam "Tu préfères l'inconfort immédiat."
    kael "Toujours."
    kael "L'inconfort se discute."
    kael "Les fractures, non."
    noam "Merci de me l'avoir dit."
    kael "Merci d'avoir écouté sans m'absoudre."
    noam "Je n'allais pas te juger."
    kael "Je ne te demandais pas ça."
    kael "Juste un témoin."
    "La ventilation souffle comme une respiration longue."
    kael "Je n'ai pas agi ce soir-là."
    kael "C'est un fait."
    kael "Et ce fait m'accompagne."

    $ kael_link = 2
    jump FREE_TIME_END

label kael_link_3:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_maintenance at adaptive_fullscreen

    $ showP("kael", "fatigue", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Les turbines ronronnent derrière les cloisons."
    play sound sfx_gresillement
    "Une lampe vacille au plafond, en rythme irrégulier."
    noam "Tu tiens bien ?"
    kael "Assez pour réfléchir."
    noam "Je vais te dire un truc simple : j'envie ton calme."
    $ showP("kael", "rire", 0.70)
    kael "Et moi j'envie les gens qui frappent la table et décident en trois mots."
    noam "Sérieusement ?"
    kael "Très sérieusement."
    kael "Ils n'ont pas l'air de transporter un tribunal intérieur."
    noam "Tu crois qu'ils ne doutent pas ?"
    kael "Ils doutent peut-être après."
    kael "Moi, je doute avant, pendant, et encore en sortant."
    noam "C'est épuisant."
    kael "Oui."
    kael "Mais parfois, leur vitesse casse des choses que personne ne répare."
    noam "Donc tu les envies et tu les crains."
    kael "Exactement."
    "Un outil tombe quelque part dans la salle voisine."
    play sound sfx_drop
    kael "Tu vois ce bruit ?"
    kael "Eux, ils disent : on ramasse et on avance."
    kael "Moi, je me demande d'abord pourquoi c'est tombé."
    noam "Et pendant ce temps, le monde continue."
    kael "Voilà."
    kael "C'est pour ça que je me demande si mon retrait est une force."
    kael "Ou une manière élégante d'éviter le risque."
    noam "Tu appelles ça une fuite ?"
    $ showP("kael", "reflechit", 0.70)
    kael "Parfois, oui."
    kael "Je peux emballer ça dans de beaux mots."
    kael "Prudence."
    kael "Analyse."
    kael "Lecture systémique."
    kael "Mais au fond, il y a aussi la peur de trancher faux."
    noam "Tout le monde a peur de ça."
    kael "Certains agissent quand même."
    kael "Moi, je construis des cartes mentales jusqu'à manquer le départ."
    noam "Tu n'as pas toujours raté le départ."
    kael "Non."
    kael "Mais je connais la sensation de regarder le train partir en expliquant très bien pourquoi."
    noam "Aïe."
    kael "Oui."
    noam "Et l'envie silencieuse, c'est quoi alors ?"
    kael "C'est regarder quelqu'un assumer une décision imparfaite et se dire :"
    kael "j'aimerais avoir ce courage brut."
    kael "Pas l'arrogance."
    kael "Le saut."
    noam "Tu as déjà sauté, pourtant."
    kael "Rarement sans filet conceptuel."
    kael "Eux sautent avec le vide."
    noam "Tu idéalises peut-être."
    kael "Peut-être."
    kael "Mais l'idéal dit quelque chose."
    kael "Il montre l'endroit où on manque d'air."
    play sound sfx_beep
    "Un bip de maintenance confirme un cycle terminé."
    kael "J'ai passé des années à croire que parler fort était une faiblesse."
    kael "Une preuve de fragilité émotionnelle."
    kael "Maintenant, je vois aussi la part de générosité."
    kael "Parler fort, c'est parfois prendre le risque d'être détesté pour débloquer la situation."
    noam "Et toi, tu prends quel risque ?"
    kael "D'être absent au moment clé."
    kael "D'être apprécié pour mon calme et inutile pour le reste."
    noam "Tu n'es pas inutile."
    kael "Je sais."
    kael "Mais je refuse de me raconter une version confortable de moi-même."
    "Il passe une main sur son front, fatigué."
    kael "Rester en retrait peut être une force quand ça protège le groupe du bruit."
    kael "Rester en retrait devient une fuite quand ça protège surtout mon image."
    noam "Comment tu distingues les deux ?"
    kael "Question simple."
    kael "Réponse dure."
    kael "Si je sors de la scène et que la situation s'améliore sans moi, c'était peut-être juste."
    kael "Si je sors et que tout se fracture, je me suis caché."
    noam "Tu te mets une barre haute."
    kael "Sinon je glisse."
    kael "L'auto-indulgence est confortable."
    kael "Elle coûte cher aux autres."
    noam "Tu veux changer quelque chose ?"
    kael "Oui."
    kael "Parler un peu plus tôt."
    kael "Couper un peu moins tard."
    kael "Accepter qu'une décision rapide puisse être imparfaite et quand même utile."
    noam "Ça, c'est déjà une décision."
    kael "Alors note-la."
    kael "Parce que demain, je pourrais encore tenter de la dissoudre dans mes nuances."
    "La lampe cesse de vaciller, enfin stable."
    kael "J'envie les voix qui tranchent."
    kael "Mais je n'ai pas besoin de leur ressembler totalement."
    kael "J'ai juste besoin d'arrêter d'appeler prudence ce qui est parfois de la peur."

    $ kael_link = 3
    jump FREE_TIME_END

label kael_link_4:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("kael", "calme", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Le vitrage laisse entrer une lueur froide sur nos visages."
    noam "J'ai toujours cru que ton calme était naturel."
    kael "Non."
    kael "C'est une architecture."
    noam "Une architecture ?"
    kael "Oui."
    kael "Des routines."
    kael "Des limites."
    kael "Des protocoles intérieurs."
    noam "Tu peux détailler ?"
    kael "Quand quelqu'un m'attaque, je ne réponds jamais sur la première impulsion."
    kael "Je respire quatre temps."
    kael "Je reformule mentalement sa phrase sans l'insulte."
    kael "Je cherche le besoin derrière la menace."
    noam "Tu fais tout ça en quelques secondes ?"
    kael "J'essaie."
    kael "Parfois je rate."
    noam "Et quand tu rates ?"
    $ showP("kael", "fatigue", 0.70)
    kael "Je serre les dents jusqu'à sentir mes tempes battre."
    kael "Je souris pour éviter d'inquiéter."
    kael "Puis je m'isole cinq minutes pour que personne ne paie ma montée."
    noam "Je ne voyais pas ça."
    kael "C'est normal."
    kael "Le contrôle efficace est invisible."
    play sound sfx_beep
    "Un bip sec coupe l'air, presque chirurgical."
    noam "Ça a l'air exténuant."
    kael "Ça l'est."
    kael "Le soir, j'ai la nuque verrouillée."
    kael "Les mains tremblent un peu quand je suis seul."
    kael "Et je dors léger, comme si j'attendais une alarme."
    noam "Pourquoi t'imposer ça ?"
    kael "Parce que l'alternative me fait peur."
    noam "Quelle alternative ?"
    kael "Laisser mes nerfs piloter à ma place."
    kael "Je sais ce que je peux dire quand je suis acculé."
    kael "Je sais aussi ce que je peux casser, même sans le vouloir."
    noam "Tu t'es déjà vu déborder ?"
    kael "Oui."
    kael "Pas souvent."
    kael "Mais assez pour comprendre le prix."
    "Il trace un cercle du pouce sur la rambarde."
    kael "Mon calme n'est pas une vertu tombée du ciel."
    kael "C'est une digue."
    kael "Chaque jour je la renforce un peu."
    noam "Et personne ne remarque les fissures."
    kael "Exact."
    kael "Parce que je les répare avant qu'elles se voient."
    noam "Tu pourrais demander de l'aide."
    kael "Je commence, là."
    noam "Tu as raison."
    kael "Le plus dur, ce n'est pas de se contenir."
    kael "Le plus dur, c'est de rester humain pendant qu'on se contient."
    kael "Ne pas devenir juste une procédure."
    noam "Tu as peur de t'anesthésier."
    kael "Oui."
    kael "Le calme peut devenir une armure trop lourde."
    kael "On survit dedans, mais on ne sent plus grand-chose."
    play sound sfx_gresillement
    "Le haut-parleur crache un souffle granuleux."
    kael "Alors je m'impose des contre-poids."
    noam "Comme quoi ?"
    kael "Dire quand je suis fatigué, au lieu de faire semblant."
    kael "Quitter une salle avant de devenir injuste."
    kael "Boire de l'eau avant de répondre."
    kael "Regarder la personne, pas seulement son argument."
    noam "Ça paraît simple dit comme ça."
    kael "Simple n'est pas facile."
    kael "Surtout quand tout va vite et que chacun veut gagner la phrase."
    noam "Tu donnes l'impression de n'avoir peur de rien."
    kael "Je suis surtout organisé autour de mes peurs."
    noam "Formule honnête."
    kael "Nécessaire."
    kael "Si j'oublie que ce calme me coûte, je commence à juger ceux qui n'y arrivent pas."
    kael "Et ça, je refuse."
    noam "Tu te juges dur, mais pas les autres."
    kael "J'essaie."
    kael "On ne connaît jamais la bataille intérieure de quelqu'un."
    "Une navette passe au loin, laissant un trait lumineux bref."
    kael "Quand tu me vois immobile, ne crois pas que c'est vide."
    kael "C'est du travail en temps réel."
    kael "Choisir les mots qui n'abîment pas."
    kael "Retenir ceux qui humilient."
    kael "Accepter de me taire quand parler servirait juste mon orgueil."
    noam "Je comprends mieux ton silence maintenant."
    kael "Bien."
    kael "Je ne veux pas qu'on romantise ça."
    kael "Ce contrôle me protège."
    kael "Mais il me fatigue plus que je ne le montre."
    noam "Merci de me laisser voir l'envers."
    kael "Merci de ne pas appeler ça de la froideur."
    noam "C'est de la discipline."
    kael "Et un peu de peur."
    kael "Les deux peuvent coexister."

    $ kael_link = 4
    jump FREE_TIME_END

label kael_link_5:

    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("kael", "reflechit", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Le couloir du Conclave bourdonne d'attentes contrariées."
    play sound sfx_announce
    "Une annonce de Kami s'éteint dans un souffle numérique."
    kael "Noam."
    kael "Je vais parler en séance."
    noam "D'accord..."
    noam "Tu as déjà ta formulation ?"
    kael "Oui."
    kael "Et cette fois je ne vais pas l'arrondir."
    noam "Tu m'intrigues."
    kael "Je soutiens la protection immédiate des isolés."
    kael "Pas conditionnelle."
    kael "Pas reportée."
    kael "Immédiate."
    noam "Sans nuance ?"
    kael "Sans nuance."
    $ showP("kael", "calme", 0.70)
    kael "On a passé des jours à découper le problème pour se sentir précis."
    kael "Pendant ce temps, des gens restent exposés."
    kael "Ça suffit."
    noam "Tu sais que certains vont dire que c'est émotionnel."
    kael "Qu'ils le disent."
    kael "Mon avis est construit."
    kael "Il est ferme, pas impulsif."
    "Des pas pressés résonnent au bout du corridor."
    kael "J'ai observé."
    kael "J'ai écouté les objections."
    kael "J'ai relu les chiffres."
    kael "J'ai attendu le bon moment trop de fois."
    noam "Et maintenant ?"
    kael "Maintenant je tranche."
    kael "Ce qui est en jeu ne tolère plus nos demi-mesures."
    noam "Tu vas t'opposer frontalement à Mara et Sael, alors."
    kael "Oui."
    kael "S'ils bloquent, je le dirai clairement."
    kael "S'ils manipulent la peur, je le nommerai."
    noam "Tu n'as pas peur de brûler des ponts ?"
    kael "J'ai peur de laisser brûler des personnes."
    kael "Le reste est secondaire."
    play sound sfx_beep
    "Le verrou de la salle principale clignote en vert."
    noam "C'est radical, venant de toi."
    kael "C'est cohérent, justement."
    kael "On me voit prudent, donc on oublie que la prudence a une frontière."
    kael "Quand cette frontière est franchie, hésiter devient une faute active."
    noam "Tu as choisi ton camp."
    kael "J'ai choisi une ligne."
    kael "Je ne vote pas contre des personnes."
    kael "Je vote contre l'abandon."
    "Je sens sa voix plus basse, mais plus solide que d'habitude."
    kael "Je vais proposer trois mesures."
    kael "Protection physique immédiate des zones fragiles."
    kael "Priorité de ravitaillement pour les isolés."
    kael "Et droit d'alerte direct si un district bloque l'accès."
    noam "Tu as déjà tout préparé."
    kael "Oui."
    kael "Et si on me coupe, je recommencerai depuis le début."
    noam "Tu ne laisseras rien au hasard."
    kael "Pas cette fois."
    kael "J'ai passé trop de temps à espérer qu'un consensus naisse tout seul."
    kael "Le consensus sans courage n'est qu'un délai poli."
    noam "Je te reconnais à peine."
    kael "C'est toujours moi."
    kael "Simplement sans frein supplémentaire."
    "Un écran mural affiche l'ouverture de séance imminente."
    kael "Écoute bien, parce que je veux être clair."
    kael "Si la salle refuse d'agir aujourd'hui, j'irai chercher des soutiens district par district."
    kael "Je mettrai les refus en lumière."
    kael "Je prendrai la responsabilité politique de cette fracture."
    noam "Tu vas te faire des ennemis."
    kael "Peut-être."
    kael "Mais je préfère des ennemis honnêtes à des victimes silencieuses."
    noam "Et si tu perds le vote ?"
    kael "Alors je continuerai demain matin."
    kael "Puis l'après-midi."
    kael "Puis encore."
    kael "Je n'ai plus l'intention de confondre patience et renoncement."
    $ showP("kael", "determine", 0.70)
    noam "Tu ne reculeras pas d'un pas."
    kael "Pas sur ça."
    kael "Je peux négocier les modalités."
    kael "Je ne négocierai pas la dignité de ceux qu'on isole."
    play sound sfx_announce
    "La voix de Kami appelle les représentants à entrer."
    kael "C'est l'heure."
    noam "Un dernier doute ?"
    kael "Non."
    kael "Le doute m'a servi jusqu'ici."
    kael "Maintenant, il m'entraverait."
    noam "Alors vas-y."
    kael "Oui."
    kael "Et quand je décide d'agir, je le fais entièrement."
    "Il avance sans se retourner, chaque pas net, presque sonore."
    "Pour la première fois, son calme ressemble à une lame dégainée."

    $ kael_link = 5
    jump FREE_TIME_END
