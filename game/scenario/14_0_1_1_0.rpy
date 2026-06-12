label _14_0_1_1_0_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 3.0

    "Des coups légers mais insistants contre la porte me tirent du sommeil."
    "Je reste immobile un long moment, espérant que la personne finisse par partir."

    nyra inquiet "Noam ? Tu es là ? C’est Nyra."
    nyra inquiet "Je peux entrer ?"

    "Je ne réponds pas."
    "Mon corps est lourd. Mes yeux brûlent."
    "J’ai l’impression d’avoir dormi à peine une heure."

    play sound sfx_knock volume 0.9

    nyra hesitation "Noam… s’il te plaît."
    nyra raison "C’est important."

    "Important."
    "Évidemment."
    "Tout est toujours important ici."

    "Je ferme les yeux et expire lentement."
    "Aucune partie de moi n’a envie de se lever."
    "Encore moins de parler."

    play sound sfx_knock volume 0.8

    nyra inquiet "Je sais que tu es réveillé."

    "Je serre la mâchoire."
    "Elle a raison. Et ça m’énerve."

    noam fatigue "... Entre."

    "Je me lève avec difficulté."
    "Mes jambes répondent mal, comme si elles appartenaient à quelqu’un d’autre."

    "Je déverrouille la porte."
    "Elle s’ouvre doucement."

    "Nyra entre sans précipitation."
    "Toujours droite. Toujours calme."
    "Mais son regard est plus dur que d’habitude."

    $ showGroup([
        ("noam", "fatigue", 0.25),
        ("nyra", "raison", 0.75),
    ])

    nyra neutre "Merci."
    nyra raison "Je ne vais pas te déranger longtemps."

    "Elle referme la porte derrière elle avec soin."
    "Puis elle reste debout, les mains jointes devant elle."

    nyra neutre "Tu n’es pas venu à l’annonce ce matin."

    noam fatigue "Non."

    nyra raison "Tu savais qu’il y en avait une."

    noam hesitation "Je m’en doutais."

    nyra reflexion "Mais tu n’es pas venu."

    noam fatigue "J’avais besoin de dormir."

    nyra neutre "Tout le monde a besoin de dormir, Noam."

    "Je n’ai rien à répondre à ça."

    nyra raison "Tout le monde l’a remarqué."

    noam inquiet "... Tout le monde ?"

    nyra neutre "Oui."

    "Elle marque une pause."
    "Pas pour chercher ses mots."
    "Pour me laisser comprendre."

    nyra raison "Noam… je vais être franche avec toi."

    noam desaccord "Tu vas surtout me dire ce que les autres racontent."

    nyra neutre "Oui."
    nyra raison "Parce que tu dois l’entendre."

    "Sa réponse tombe sans hésitation."
    "Froide. Propre. Impossible à esquiver."

    nyra raison "Ton comportement commence à inquiéter beaucoup de monde."
    nyra reflexion "Et pas seulement pour ton bien."

    "Je sens la colère monter d’un coup."

    noam colere "Inquiéter ?!"
    noam colere "C’est ça que vous racontez dans mon dos ?!"

    "Nyra ne bronche pas."
    "Elle reste parfaitement calme, ce qui m’énerve encore plus."

    nyra raison "Je ne dis pas que c’est vrai. Je te dis ce que les autres pensent."
    nyra raison "Et franchement… vu comment tu te comportes depuis deux jours, je les comprends un peu."

    "Je me mords violemment la lèvre."
    "La colère redescend aussi vite qu’elle est montée, laissant derrière elle un goût amer de regret."

    noam "... Désolé."
    noam fatigue "Je… je suis fatigué. Vraiment fatigué."

    nyra "Je sais."

    "Elle s’approche lentement et s’assoit sur le bord du lit, gardant une distance respectueuse."

    nyra raison "Le prochain vote aura lieu demain, à J15."
    nyra raison "Le sujet est : « Toute information détenue par ARCHIVE devient consultable par tout citoyen. »"
    nyra raison "Autrement dit : plus aucune donnée personnelle ne sera protégée."

    noam inquiet "Tout le monde pourra consulter les archives de tout le monde ?"

    nyra neutre "Oui."

    noam inquiet "Les historiques médicaux ? Les rapports ? Les sanctions ?"

    nyra raison "Oui."

    noam reflexion "Les informations confidentielles des districts ?"

    nyra reflexion "Si ARCHIVE les détient, alors oui."

    "Je reste immobile."
    "Cette fois, la fatigue disparaît presque."
    "Pas parce que je vais mieux."
    "Parce qu’un autre problème vient de prendre toute la place."

    noam inquiet "C’est énorme."

    nyra neutre "C’est catastrophique, selon certains."
    nyra raison "Tomas est farouchement opposé à cette mesure."

    noam reflexion "Évidemment."

    nyra raison "Ce n’est pas seulement une question de pudeur."
    nyra raison "ARCHIVE possède des informations très personnelles sur chacun d’entre nous."
    nyra reflexion "Des choses qui peuvent briser une réputation."
    nyra reflexion "Ou déclencher une vengeance."
    nyra fatigue "Ou juste détruire quelqu’un."

    noam inquiet "Et Kami présente ça comme une simple proposition ?"

    nyra degout "Kami présente toujours les choses proprement."
    nyra raison "C’est nous qui découvrons le sang après."

    "La phrase me glace."
    "Pas parce qu’elle est spectaculaire."
    "Parce qu’elle est vraie."

    noam reflexion "Qui est pour ?"

    nyra reflexion "Difficile à dire."
    nyra raison "Certains pensent que la transparence totale empêchera les mensonges."
    nyra raison "D’autres veulent savoir ce qu’ARCHIVE leur cache depuis des années."
    nyra neutre "Et d’autres voteront selon leur peur du moment."

    noam desaccord "Donc personne ne sait vraiment ce qu’il fait."

    nyra raison "Comme d’habitude."

    "Elle le dit sans ironie."
    "C’est presque pire."

    nyra determine "Mais ce n’est pas la seule raison de ma venue."

    noam inquiet "Je m’en doutais."

    nyra raison "Noam, écoute-moi attentivement."
    nyra raison "Si tu continues comme ça, si tu t’isoles, si tu fais des crises en public, si tu rates les votes…"
    nyra determine "Les gens ne vont plus te voir comme quelqu’un de fatigué."
    nyra neutre "Ils vont te voir comme un danger."
    nyra raison "Et dans un endroit comme celui-ci… les dangers, on finit par les mettre à l’écart."

    "Ses mots sont calmes, presque doux, mais ils portent comme des coups précis."

    noam "... Tu es en train de me menacer ?"

    nyra "Non. Je te mets en garde."
    nyra raison "Parce que je pense encore que tu peux te ressaisir."
    nyra raison "Mais si tu continues à t’enfoncer… personne ne pourra plus te défendre."

    "Je baisse les yeux sur mes mains. Elles tremblent légèrement."

    nyra raison "Réfléchis bien à ce que tu veux faire demain pour le vote."
    nyra raison "Et surtout… arrête de te comporter comme si tu étais déjà seul contre tous."
    nyra neutre "Parce que si tu continues, c’est exactement ce qui va arriver."

    "Elle se lève lentement, lisse sa jupe et se dirige vers la porte."

    nyra "Je te laisse te reposer."
    nyra inquiet "Mais Noam… fais attention à toi."

    "Elle sort sans un bruit supplémentaire."

    "Je reste assis sur mon lit, le regard vide."

    think "Même Nyra… même elle commence à me voir comme un problème."
    think "Et le pire… c’est que je ne peux même pas lui en vouloir."

    "Je me rallonge, fixant le plafond fissuré."

    think "Demain… un vote sur la levée totale du secret des archives."
    think "Tout le monde va pouvoir tout savoir sur tout le monde."

    think "Et moi… je ne sais même plus qui je suis vraiment."

    pause 2.5

    $ renpy.notify("Nyra est venue te parler...")

    jump _14_0_1_1_SUITE_REVEIL