default decouverte_salle_repos = False
default repos_table_seen = False
default repos_party_active = False

init python:
    REPOS_TABLE_BONUS_CHANCE = 0.20

    def repos_table_bonus_label():
        # La scène sera ajoutée plus tard sous ce label. Tant qu'elle
        # n'existe pas, le repos se termine normalement.
        label_name = "repos_table_bonus_scene"
        if not renpy.has_label(label_name):
            return None
        if renpy.random.random() < REPOS_TABLE_BONUS_CHANCE:
            return label_name
        return None


label REPOS_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_345
    scene bg_repos at adaptive_fullscreen

    if not decouverte_salle_repos and day_number() == 1:
        jump decouverte_salle_repos

    $ pnc_room = "pnc_repos"
    call screen pnc_repos()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_repos():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("repos")
    use room_scene_interactions("repos")

    if social_free_time_active() and character_has_available_free_time("iris"):
        imagebutton:
            idle Transform(character_image("iris", "colere"), zoom=1.00)
            hover Transform(character_image("iris", "taquin"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action [SetVariable("last_room_label", "REPOS_TP"), SetVariable("free_time_selected_character", "iris"), Jump("FREE_TIME_CHARACTER_INTERACT")]




label REPOS_PNC_BABYFOOT:
    "Le babyfoot brille trop."
    "Comme s’il n’avait jamais vu une main humaine."
    think "Ils ont pensé à tout… sauf à la partie où on respire."
    jump REPOS_TP


label REPOS_PNC_FLECHETTES:
    "Un jeu de fléchettes."
    "Aimanté, sécurisé."
    "Même se détendre ici a l’air réglementé."
    jump REPOS_TP


label REPOS_PNC_ARCADE:
    "Une borne d’arcade."
    "Écran intact."
    "Liste de jeux préchargés."
    think "Au moins, ils ne nous demandent pas de voter pour débloquer le niveau 2."
    jump REPOS_TP


label REPOS_PNC_DISTRIBUTEUR:
    "Un distributeur de boissons."
    "Pas de prix."
    "Pas de monnaie."
    "Juste un choix."
    think "La seule chose gratuite, ici : l’illusion du choix."
    jump REPOS_TP


label REPOS_PNC_CANAPE:
    "Le canapé est large."
    "Trop propre."
    "Les coussins sont alignés au millimètre."
    think "Même le confort a un protocole."
    jump REPOS_TP


label repos1_babyfoot:
    jump REPOS_PNC_BABYFOOT


label repos1_flechette:
    jump REPOS_PNC_FLECHETTES


label repos1_distributeur:
    if cafeteria_food_visible_count() <= 0:
        "Le distributeur est vide. Pas même une ration oubliée au fond."
        think "Les stocks de la cafétéria ont donc fini par atteindre jusqu'ici."
    elif cafeteria_food_visible_count() < 5:
        "Le distributeur n'est plus rempli qu'à moitié."
        "Les choix se réduisent au même rythme que les réserves."
    else:
        "Le distributeur est plein. Boissons et rations sont encore soigneusement alignées."
        think "Pour le moment, personne n'a besoin de compter ce qu'il prend."
    jump REPOS_TP


label repos1_porte_couloir_cafeteria:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label repos2_television:
    if day_number() == 6 and social_free_time_active() and not j601_border_news_seen:
        call _6_0_1_TV_FRONTIERES from _call_j601_tv_frontieres_repos
        jump REPOS_TP

    "L'écran occupe une bonne partie du mur."
    "Une sélection de films, de jeux et d'archives tourne silencieusement."
    think "Même les distractions ont été choisies avant notre arrivée."
    jump REPOS_TP


label repos2_table_repos:
    if not repos_table_seen:
        $ repos_table_seen = True
        think "Je pourrai me reposer ici quand j'aurai du temps libre."

    if social_free_time_active():
        menu:
            "Me reposer jusqu'à la fin de ce temps libre ?"
            "Oui":
                $ repos_bonus_label = repos_table_bonus_label()
                if repos_bonus_label:
                    call expression repos_bonus_label from _call_expression_3
                jump FREE_TIME_END
            "Non":
                jump REPOS_TP

    think "Ce n'est pas le moment de m'installer."
    jump REPOS_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label REPOS_PNC_EXIT:
    return
    
label decouverte_salle_repos:

    $ decouverte_salle_repos = True

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "J'entends quelqu'un célébrer une victoire derrière la porte de la salle de repos. Visiblement, certains ont trouvé comment s'occuper."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_346
    scene bg_repos at adaptive_fullscreen with fade
    "Un baby-foot occupe le centre de la pièce. Un garçon se félicite bruyamment devant une fille installée sur le canapé, qui n'a pas l'air de partager son enthousiasme."

    scene bg_cg007 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg007")
    play sound sfx_balle volume 3.0

    julian vide "Et de six ! Je suis vraiment trop bon à ce jeu."
    iris vide "Tu joues tout seul, abruti. Même une chaise ferait un meilleur adversaire."
    noam vide "En même temps, six buts contre personne, c'est une belle régularité."
    julian vide "Ah ! Un public qui comprend le talent. Viens, on va faire une vraie partie."
    noam vide "D'accord, mais je te préviens, j'ai pas beaucoup joué."
    julian vide "Ça tombe bien, moi je suis excellent professeur. Tu ne pouvais pas mieux tomber."
    iris vide "Il va surtout t'expliquer pendant vingt minutes pourquoi chacune de ses erreurs était volontaire."

    "Je prends place de l'autre côté du baby-foot. Julian commence aussitôt à commenter son jeu, ce qui me laisse assez de temps pour récupérer la balle."
    play sound sfx_balle volume 2.0
    noam vide "Ah, c'est bon, j'ai marqué."
    julian vide "Oui, enfin, je te laissais prendre tes marques. Un gentleman ne gagne jamais dès la première minute."
    iris vide "Oh, c'est beau, ça. Tu pourrais le broder sur un coussin."
    julian vide "Riez tant que vous voulez. Vous verrez quand j'aurai repris l'avantage."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_347
    scene bg_repos at adaptive_fullscreen with fade

    $ showGroup([
        ("julian", "sourire", 0.22),
        ("iris", "taquin", 0.50),
        ("noam", "sourire", 0.78),
    ])

    julian sourire "Julian. Je préfère me présenter avant de te battre, histoire que tu puisses raconter l'histoire correctement."
    $ unlock_character_name("julian")
    call kd_play_character_intro("julian") from _call_kd_intro_julian_j1
    noam taquin "Noam. C'est gentil de me laisser préparer ma version des faits."
    iris blase "Iris. Et si tu veux un conseil, ne commence jamais une partie avec lui après le dîner."
    $ unlock_character_name("iris")
    noam sourire "Pourquoi ?"
    iris colere "Parce qu'il refuse d'aller se coucher tant qu'il n'a pas gagné."
    julian taquin "C'est faux ! Je considère simplement qu'une bonne partie mérite une conclusion satisfaisante."

    "Iris se lève du canapé lorsque Julian annonce qu'il est prêt pour sa revanche."
    iris taquin "Allez, pousse-toi. Je vais lui montrer comment on fait."
    julian surpris "Toi ? Tu viens de dire que ce jeu était stupide."
    iris neutre "Il l'est. Mais toi aussi, et je te supporte depuis tout à l'heure."
    "Elle prend ma place, remet la balle en jeu et marque presque immédiatement."
    play sound sfx_balle volume 3.0
    julian surpris "Attends, attends ! J'étais pas prêt !"
    iris taquin "Moi non plus. C'est fou, hein ?"
    "Julian se concentre et cesse enfin de parler. Les deux échangent quelques balles, puis Iris marque de nouveau, avant qu'il puisse reprendre son souffle."
    noam rire "Je crois qu'elle joue mieux que nous deux."
    julian surpris "Je reconnais qu'elle se défend, mais il ne faut pas tirer de conclusions trop rapides."
    iris colere "Tu veux une conclusion ? Regarde le score."

    "Iris gagne la partie sur un dernier tir qui laisse Julian immobile devant les poignées. Elle recule et époussette ses mains avec un air parfaitement satisfait."
    iris sourire "Voilà. Maintenant, je vais pouvoir m'asseoir tranquille."
    julian fatigue "C'est une humiliation organisée. Vous vous êtes ligués contre moi."
    noam taquin "Je te connaissais même pas il y a cinq minutes."
    iris taquin "Et pourtant, vous avez déjà un point commun : vous l'avez battu."
    "Julian tente de trouver une réponse, puis finit par rire malgré lui."
    julian sourire "Bon, d'accord. Une belle victoire, Iris. Mais la prochaine fois, on jouera sur un autre terrain."
    iris blase "Oui, oui. Tu vas encore m'expliquer que tu es champion de quelque chose."

    "Je me frotte les tempes. Iris le remarque immédiatement et son sourire disparaît."
    iris inquiet "Ça va, toi ? T'as une drôle de tête."
    noam hesitation "J'ai encore un peu mal au crâne depuis le réveil, mais rien de grave."
    iris reflexion "Si ça empire, va à l'infirmerie. Ce serait débile de tomber dans les pommes pour avoir voulu faire le malin."
    julian taquin "Tu vois ? Elle tient déjà à toi. C'est touchant."
    iris colere "Julian, je te jure que je vais te refaire manger les poignées de ce baby-foot."
    noam rire "Je crois que je vais partir avant le prochain match."
    julian sourire "Reviens quand tu veux, Noam. Il faudra bien que quelqu'un tente de sauver mon honneur."
    iris taquin "Il est trop tard pour ça. Tu peux plutôt venir prendre un café."
    "Je les laisse se chamailler. Derrière moi, Julian réclame déjà une revanche qu'Iris refuse avec beaucoup trop de satisfaction."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_7
    $ hideGroup()
    jump REPOS_TP
