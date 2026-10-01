# =============================================================================
# JOUR 27 — Rupture
# Après la prise de parole publique de Noam, les DG n'ont plus intérêt à rester cachés.
# =============================================================================

default j27_attack_started = False
default j27_vote_result = None

label _27_0_1_1_0_0_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Matin"

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je me réveille habillé, assis contre mon lit."

    "Je me suis endormi comme ça sans m'en rendre compte."

    "Le bureau bloque toujours la grille. La porte, elle, est verrouillée."

    "Quelqu'un frappe deux fois."

    pause 0.4

    noam inquiet "Qui c'est ?"

    iris fatigue "Moi. Ouvre avant que je me vexe."

    "Je déverrouille."

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "fatigue", 0.40),
        ("noam", "fatigue", 0.62),
    ])

    iris fatigue "T'as une sale gueule."

    noam blase "Toi aussi."

    iris blase "Merci."

    noam inquiet "Il s'est passé quelque chose ?"

    iris reflexion "J'ai entendu des portes toute la nuit. Des gens qui bougeaient. Je sais pas qui."

    noam neutre "Personne t'a parlé ?"

    iris neutre "Mara a frappé vers quatre heures."

    noam surpris "Et ?"

    iris blase "Je lui ai dit d'aller se faire foutre."

    noam neutre "Elle voulait quoi ?"

    iris inquiet "Elle disait qu'elle voulait parler."

    noam fatigue "À quatre heures."

    iris neutre "Ouais. Très crédible."

    "On se regarde une seconde."

    iris determine "On reste ensemble aujourd'hui."

    noam determine "Ouais."

    $ hideGroup()

label _27_0_1_1_0_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "La cafétéria est pleine mais personne ne parle normalement."

    "Les conversations meurent quand on entre."

    $ showGroup([
        ("ryn", "neutre"),
        ("tomas", "stress"),
        ("nyra", "inquiet"),
        ("sael", "mefiant"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("kael", "calme"),
        ("iris", "neutre"),
        ("noam", "inquiet"),
    ])

    ryn neutre "Vous voilà."

    noam neutre "Ça veut dire quoi ?"

    ryn colere "Ça veut dire que j'ai dormi deux heures parce que maintenant je sais plus qui ferme quelle porte."

    tomas stress "J'ai essayé de noter les déplacements. Enfin... ceux que j'ai vus. C'est nul comme méthode, je sais, mais..."

    nyra raison "C'est mieux que rien."

    mara neutre "Vous êtes sérieusement en train de faire des listes sur nous ?"

    iris blase "Sur tout le monde."

    mara agace "Super ambiance."

    kael calme "Ça peut pas continuer comme ça."

    ryn colere "Tu proposes quoi ?"

    kael reflexion "Qu'on arrête de paniquer."

    iris taquin "Bonne idée. J'y avais pas pensé."

    elias fatigue "Vous avez parlé au monde entier hier. Vous vouliez quoi, exactement ? Que tout le monde reste calme ?"

    noam determine "Je voulais qu'on puisse pas sortir d'ici avec nos visages sans que personne pose de question."

    "La phrase change quelque chose."

    "Mara regarde Elias."

    "Elias regarde Kael."

    "Une seconde. Pas plus."

    "Mais je la vois."

    iris inquiet "Noam..."

    noam peur "Ouais."

    mara fatigue "Bon."

    "Elle repose lentement sa tasse."

    mara neutre "On va arrêter de faire semblant."

    elen peur "Quoi ?"

    ryn determine "Mara, bouge pas."

    mara colere "Oh ferme-la, Ryn."

    kael fatigue "Ça sert plus à rien."

    tomas peur "Qu'est-ce qui sert plus à rien ?"

    elias mefiant "De vous convaincre."

    pause 0.4

    noam peur "Vous êtes trois."

    mara taquin "Au moins."

    "Elen recule si vite que sa chaise tombe."

    elen peur "Non... non, c'est pas drôle."

    mara triste "Je sais."

    "Et c'est ça qui me terrifie le plus. Elle a l'air sincère."

    ryn colere "Tout le monde derrière moi."

    elias colere "Arrête de jouer au héros."

    ryn neutre "Essaie de m'en empêcher."

    nyra colere "RYN !"

    "Tout part trop vite."

    "Kael attrape Tomas par le bras. Tomas hurle. Iris me tire en arrière. Ryn se jette entre Elias et Elen."

    $ j27_attack_started = True

    tomas neutre "LÂCHE-MOI !"

    kael colere "Arrête de te débattre !"

    tomas peur "TU ME TRAÎNES OÙ ?!"

    noam colere "KAEL !"

    kael peur "Je veux pas lui faire mal !"

    iris colere "Alors lâche-le !"

    mara colere "On n'a plus le temps !"

    "Nyra renverse une table entre eux. Tomas se dégage."

    nyra determine "Courez."

    $ hideGroup()

label _27_0_1_1_0_0_FUITE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4

    "On court sans savoir où aller."

    $ showGroup([
        ("ryn", "colere"),
        ("tomas", "peur"),
        ("nyra", "inquiet"),
        ("sael", "determine"),
        ("julian", "peur"),
        ("elen", "peur"),
        ("iris", "colere"),
        ("noam", "peur"),
    ])

    julian peur "Attendez, attendez ! Ils nous suivent ?"

    ryn colere "Avance !"

    elen peur "Mara... elle a dit au moins."

    tomas stress "Ça veut dire quoi, au moins ?!"

    sael determine "Ça veut dire qu'on compte pas."

    iris colere "Personne se sépare."

    noam neutre "Nyra ?"

    nyra inquiet "On va au Conclave. Les portes sont plus épaisses."

    ryn neutre "Et le vote."

    iris surpris "Tu penses vraiment au vote maintenant ?"

    ryn agace "Kami, elle, y pensera."

    $ hideGroup()

label _27_0_1_1_0_0_VOTE:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7

    "On verrouille derrière nous."

    "Quelques secondes plus tard, le signal de Kami retentit."

    play sound sfx_announce
    stop music fadeout 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Eh bien."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Je vois que la campagne a pris une tournure plus... physique."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Mais nous avons un calendrier."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Le vote aura lieu."

    hide screen kami_broadcast_ui
    stop music fadeout 0.5
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.6

    $ showGroup([
        ("ryn", "colere"),
        ("tomas", "stress"),
        ("nyra", "inquiet"),
        ("sael", "mefiant"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("iris", "colere"),
        ("noam", "inquiet"),
    ])

    iris colere "Elle se fout de nous."

    tomas stress "On n'est même pas tous là."

    nyra raison "Les absents ne comptent pas dans les suffrages exprimés."

    noam reflexion "Le texte sur la détention."

    ryn agace "Maintenant c'est presque une blague."

    sael raison "On vote quand même."

    julian inquiet "Pourquoi ?"

    sael neutre "Parce qu'on n'abandonne pas tout ce qu'on faisait juste parce qu'ils ont décidé de nous chasser."

    "Julian la regarde, puis souffle."

    julian determine "D'accord."

    "Le vote se fait à huit."

    "Pour."

    "Pour."

    "Pour."

    "Personne n'a vraiment la tête à célébrer."

    $ j27_vote_result = "adopted"

    play sound sfx_announce
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "Adopté."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous voyez ? Même poursuivis dans les couloirs, vous restez capables de faire de la politique."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je suis presque fière."

    hide screen kami_broadcast_ui
    stop music fadeout 0.5
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "colere"),
        ("tomas", "stress"),
        ("nyra", "inquiet"),
        ("sael", "mefiant"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("iris", "colere"),
        ("noam", "inquiet"),
    ])

    "Quelque chose frappe contre la porte."

    elen peur "Ils sont là."

    ryn determine "Alors on bouge."

    noam neutre "Par où ?"

    nyra reflexion "Porte secondaire."

    iris determine "On y va."

    $ hideGroup()

label _27_0_1_1_0_0_FIN:
    $ current_period = "Soir"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je finis la journée enfermé dans ma chambre, Iris dans celle d'à côté."

    "On a convenu de frapper trois fois, puis deux, si l'un de nous doit ouvrir."

    "À vingt-trois heures, quelqu'un frappe."

    "Trois fois."

    pause 0.5

    "Puis deux."

    pause 0.5

    noam inquiet "Iris ?"

    "Silence."

    "Je n'ouvre pas."

    "Une minute plus tard, mon téléphone vibre."

    iris inquiet "C'était pas moi."

    "Je ne dors presque pas."

    call end_day("28", sleeping=True) from _call_j27_stay_end_day_28
    jump _28_0_1_1_0_0_REVEIL
