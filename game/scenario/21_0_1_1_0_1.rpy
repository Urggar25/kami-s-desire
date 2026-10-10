# =============================================================================
# JOUR 21 — Route 0_1_1_0_1
# Réponse à Kael : "Je monte dans la navette."
#
# Les Doppelgängers choisissent de ne pas prolonger le Conclave.
# Ceux qui ont déjà pris la place de leur original partiront aujourd'hui.
# Le Doppelgänger de Noam n'a, lui, toujours pas remplacé Noam.
# =============================================================================

default j21_leave_qte_success = False

define dg_noam = Character("Noam ?", image="noam")

transform j21_dg_noam_approach(z=1.0):
    xpos 0.5
    xanchor 0.5
    ypos 0.26
    yanchor 0.18
    zoom z


label _21_0_1_1_0_1_REVEIL:

    $ cafeteria_food_level = "null"
    $ current_period = "Matin"
    $ current_day = 21
    $ day_id = 21
    $ j20_kael_depart_choice = "leave"
    $ noam_has_juliette_drawing = False

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Je me réveille avant l'annonce de Kami."

    "Pendant quelques secondes, je reste allongé sans bouger, les yeux ouverts dans le noir."

    think "Aujourd'hui."

    "C'est la première pensée qui me vient."

    "Pas Mara. Pas la salle des Goumi. Pas M16."

    "Aujourd'hui, on rentre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je me redresse lentement et regarde la grille d'aération au fond de la chambre."

    "Elle est exactement comme hier."

    "Enfin... je crois."

    "Je la fixe encore quelques secondes avant de détourner les yeux."

    noam fatigue "Non."

    "Pas aujourd'hui."

    "Je me lève."

    play sound sfx_announce
    stop music fadeout 0.6

    scene bg_diffusion_amour at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Ooooh... Regardez-moi ces petites têtes."
    kami "Vous avez presque l'air heureux ce matin."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je me demande bien pourquoi."
    kami "Ah oui ! C'est vrai."
    kami "Aujourd'hui, vous rentrez chez vous."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Votre merveilleux taxi spatial s'amarrera au Conclave à quatorze heures."
    kami "Et à seize heures..."

    pause 0.4

    kami "Pouf."
    kami "Plus de Conclave. Plus de votes. Plus de moi."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Enfin... pour vous."
    kami "Je vais essayer de survivre à cette séparation."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Alors profitez bien de vos dernières heures ensemble."
    kami "Rangez vos petites affaires. Faites vos adieux aux murs. Vérifiez deux fois vos badges si ça peut vous rassurer."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Et surtout, ne perdez rien."
    kami "Je ne ferai PAS demi-tour parce que l'un de vous a oublié une chaussette sous son lit."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Seize heures. Soyez prêts."
    kami "Ce serait vraiment dommage de rater votre propre départ."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je reste debout au milieu de ma chambre."

    think "Seize heures."

    "Quelques heures."

    "C'est tout ce qu'il reste."

    stop music fadeout 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j21_leave_door_chambre_couloir
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Quand je sors, plusieurs portes sont déjà ouvertes."

    "Pour la première fois depuis longtemps, le couloir ressemble presque à celui d'un hôtel le matin d'un départ."

    "Des gens passent d'une chambre à l'autre. On parle de sacs, de vêtements oubliés, de ce qu'on fera une fois en bas."

    "Personne ne parle de vote."

    "Rien que ça me paraît irréel."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_soft_neon_morning.mp3" fadein 1.2

    $ showGroup([
        ("noam", "fatigue", 0.12),
        ("iris", "blase", 0.28),
        ("elen", "joie", 0.44),
        ("tomas", "reflexion", 0.60),
        ("kael", "calme", 0.76),
        ("mara", "neutre", 0.92),
    ])

    elen joie "J'ai officiellement décidé que mon premier repas sur Terre serait tellement gras que Sael fera un malaise juste en le regardant."

    tomas reflexion "Tu sais qu'après trois semaines de rationnement, ton estomac va probablement—"

    elen rire "Tomas."

    tomas surpris "Quoi ?"

    elen "Ne ruine pas mon rêve avec de la science."

    mara sourire "Laisse-la se détruire l'estomac en paix. C'est beau, une jeune femme qui a encore des projets."

    iris blase "Ses projets tiennent dans une friteuse."

    elen "Vous êtes juste jaloux parce que j'ai déjà organisé ma vie après seize heures."

    noam fatigue "Moi, j'aimerais déjà arriver à seize heures."

    "Je m'assois avec eux."

    "Mara est juste en face, bien vivante, en train de voler quelque chose dans l'assiette de Tomas pendant qu'il proteste."

    tomas colere "H-Hé !"

    mara taquin "Trop lent."

    "Je la fixe une seconde de trop."

    mara mefiant "Quoi ?"

    noam surpris "Rien."

    mara "Non, ça c'est la tête de quelqu'un qui a un truc à dire."

    noam fatigue "J'ai juste mal dormi."

    mara taquin "Ah. Donc maintenant quand tu dors mal tu me regardes comme si j'étais revenue d'entre les morts ? Charmant."

    "Mon estomac se serre."

    iris colere "Mara."

    mara "Quoi ?"

    iris determine "Lâche-le un peu."

    mara mefiant "Je plaisantais."

    iris "Bah plaisante ailleurs."

    "Mara hausse les épaules, mais elle arrête."

    "Iris pousse ensuite une tasse vers moi sans même me regarder."

    iris fatigue "Tiens. Bois."

    noam surpris "C'est quoi ?"

    iris blase "Un grille-pain."

    noam "Je vois bien que c'est du café. Je demandais pourquoi tu me le donnes."

    iris "Parce que t'as une tête de cadavre et que j'aimerais éviter d'en avoir un deuxième à gérer."

    "Elle réalise ce qu'elle vient de dire et ferme les yeux une demi-seconde."

    iris gene "Enfin... merde. Tu m'as compris."

    noam fatigue "Ouais."

    "Je prends la tasse."

    noam "Merci."

    iris blase "Ne rends pas ça gênant."

    "Je bois une gorgée. Elle attend quand même de me voir avaler avant de reprendre son propre verre."

    kael doute "Noam..."

    "Je tourne la tête vers lui."

    kael inquietude "Pour hier soir. La question que je t'ai posée..."

    noam reflexion "Celle où tu m'as demandé si j'abandonnais quelqu'un sur la station ?"

    iris surpris "Attends, quoi ?"

    kael doute "C'était pas exactement—"

    iris colere "Non mais Kael, sérieusement ? Vous aviez pas un sujet plus léger ? Genre la famine, les lasers, je sais pas ?"

    kael sourire "J'y penserai la prochaine fois."

    iris blase "Il y aura pas de prochaine fois. On se casse aujourd'hui."

    "Kael sourit à peine. Puis son regard revient vers moi."

    kael inquietude "Je voulais juste dire que... enfin..."

    "Il frotte son pouce contre le bord de son verre."

    kael doute "Je crois que t'avais raison."

    noam reflexion "Sur le fait de partir ?"

    kael "Ouais. Quand une sortie existe, si rester change rien..."

    "Il s'arrête."

    noam "Tu pars."

    kael inquietude "Tu pars."

    "Il répète mes mots doucement, comme s'il voulait voir ce qu'ils donnent à voix haute."

    iris reflexion "Vous êtes vraiment bizarres tous les deux aujourd'hui."

    noam fatigue "Ça fait vingt jours qu'on est bizarres."

    iris "Non. Toi t'es bizarre depuis vingt jours. Lui, c'est nouveau."

    kael sourire "Merci."

    "La blague tombe, mais quelque chose dans son expression reste fermé."

    "Iris tape deux fois du doigt sur la table."

    iris determine "Bon. Nouvelle règle pour la journée."

    noam blase "Je sens que ça va me plaire."

    iris "Tu ne fais rien de stupide."

    noam "C'est très large comme définition."

    iris colere "Très bien. Pas de conduit, pas de salle cachée, pas de cadavre, pas de couteau, et si jamais une idée commence par 'je vais juste vérifier', tu viens me voir avant."

    noam surpris "Le couteau..."

    iris inquiet "Quoi, le couteau ?"

    noam reflexion "Je l'ai laissé en bas."

    iris blase "Je sais. J'étais là quand, pour une fois, t'as fait un choix intelligent."

    noam "Je devrais peut-être le récupérer avant de partir."

    iris colere "Non."

    noam "C'est quand même mon couteau."

    iris determine "Et hier c'était quand même ton couteau quand t'étais à deux secondes de faire une connerie avec."

    noam colere "Je t'ai dit que je voulais pas—"

    iris "Je sais !"

    "Elle me coupe net."

    iris fatigue "Je sais que tu voulais pas me faire de mal. C'est pas le sujet."

    "Sa voix redescend."

    iris inquiet "Je veux juste qu'aujourd'hui, pendant quelques heures, t'arrêtes de chercher un problème à résoudre. Laisse-moi au moins ça."

    "Je reste silencieux."

    noam fatigue "D'accord."

    iris "D'accord quoi ?"

    noam "Je vais pas chercher le couteau."

    "Elle souffle enfin."

    iris fatigue "Merci."

    "Au bout de la table, Kael relève très légèrement les yeux."

    "Puis il recommence à boire."

    $ hideGroup()

    jump _21_0_1_1_0_1_MILIEU_JOURNEE


label _21_0_1_1_0_1_MILIEU_JOURNEE:

    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 1.0

    "Le reste de la matinée passe beaucoup trop vite."

    "Tout le monde récupère ses affaires."

    "Kami fait vérifier les badges une première fois, puis une deuxième, parce qu'elle considère apparemment que nous sommes incapables de garder un morceau de plastique sur nous pendant quatre heures."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_fier at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.7

    kami "Bonne nouvelle, mes petits voyageurs."
    kami "Votre navette est bien arrivée."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous pouvez arrêter de regarder les plafonds en vous demandant si je vais changer d'avis à la dernière seconde."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Départ dans deux heures."
    kami "Deux. Heures."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Ça devrait être largement suffisant pour douze adultes responsables."
    kami "Donc, naturellement, je m'attends à une catastrophe."

    hide screen kami_broadcast_ui
    stop music fadeout 0.7
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Deux heures."

    "Je devrais être soulagé."

    "Je le suis."

    "Mais quelque chose continue de me gratter derrière le crâne."

    play sound "audio/sfx_duct_scrape.wav" volume 0.42

    "Un bruit métallique résonne au-dessus de moi."

    "Je m'arrête."

    noam inquiet "..."

    "Le couloir est vide."

    "Je lève les yeux vers la grille la plus proche."

    "Rien."

    think "Pas aujourd'hui."

    "Je repars."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Quand je rentre dans ma chambre, je m'arrête sur le seuil."

    "La grille d'aération est légèrement ouverte."

    noam panne "..."

    "Quelques millimètres."

    "Peut-être un centimètre."

    "Je pourrais jurer qu'elle était fermée ce matin."

    "Je pose mon sac sur le lit."

    think "Ou peut-être pas."

    think "M16."

    "Je déteste immédiatement cette pensée."

    "Avant, quand quelque chose n'allait pas, je pouvais au moins faire confiance à mes propres yeux."

    "Maintenant, même une grille mal fermée suffit à me faire douter de ma tête."

    play sound sfx_door

    show iris neutre at center with dissolve

    iris "T'es prêt ?"

    noam "Presque."

    "Elle suit mon regard jusqu'à la grille entrouverte."

    iris inquiet "Tu vas pas y retourner."

    noam fatigue "Non."

    iris "Même si t'es persuadé qu'elle était fermée ce matin ?"

    "Je la regarde."

    noam "Même là."

    "Elle reste silencieuse une seconde, puis hoche la tête."

    iris fatigue "D'accord."

    noam surpris "C'est tout ?"

    iris blase "Tu voulais que je t'attache au lit ?"

    noam "Vu les derniers jours, j'exclus plus rien."

    iris "Tente pas le diable."

    "Je ferme mon sac."

    iris inquiet "J'ai encore deux trucs à récupérer. Je reviens dans cinq minutes."

    noam "Je bouge pas."

    iris reflexion "J'allais justement te dire de pas me promettre ça."

    noam surpris "Pourquoi ?"

    iris fatigue "Parce qu'hier j'ai passé mon temps à te dire quoi faire, quoi pas toucher, où aller... et ça nous a presque explosé à la gueule."

    "Elle s'approche et remet machinalement le col de ma veste en place."

    iris gene "Alors aujourd'hui... fais juste pas le con."

    noam "Ça, je peux essayer."

    iris colere "Non."

    "Je souris."

    noam "D'accord. Je ferai pas le con."

    "Elle garde les doigts sur mon col une seconde de trop avant de retirer sa main."

    iris fatigue "Bien."

    "Elle se dirige vers la porte, puis s'arrête."

    iris "Noam."

    noam "Hm ?"

    iris inquiet "Si quelque chose te paraît bizarre... viens me chercher."

    noam "Promis."

    "Cette fois, elle accepte la réponse."

    iris taquin "Cinq minutes. Essaie de survivre jusque-là."

    noam blase "Je vais faire un effort."

    hide iris with dissolve
    play sound sfx_door

    "La porte se referme."

    "Et, d'un coup, la chambre paraît beaucoup plus vide."

    pause 0.8

    "Je reste seul."

    jump _21_0_1_1_0_1_DOPPELGANGER


label _21_0_1_1_0_1_DOPPELGANGER:

    scene bg_chambre at adaptive_fullscreen
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.2
    $ danger_on()

    "Je range un dernier vêtement dans mon sac."

    play sound "audio/sfx_duct_scrape.wav" volume 0.62

    "Le bruit revient."

    "Cette fois, juste derrière moi."

    "Je ferme les yeux."

    noam fatigue "Iris va me tuer..."

    "Je me retourne vers la grille."

    "Elle bouge."

    noam panne "..."

    "Pas un souvenir."

    "Pas une impression."

    "Elle bouge vraiment."

    play sound "audio/sfx_metal_open.mp3"

    "La plaque bascule vers l'extérieur."

    "Deux mains apparaissent dans l'ouverture."

    "Puis une tête."

    pause 0.8

    noam peur "..."

    "Mon cerveau refuse l'image avant même que je comprenne pourquoi."

    "Quelqu'un sort du conduit et retombe lourdement dans ma chambre."

    "Il se redresse."

    $ doppelganger_reveal(screamer=False, duration=0.85, restore_volume=0.65)

    show noam fatigue at j21_dg_noam_approach(0.96) with creep_diss

    "Je me regarde."

    noam panne "..."

    "Même visage, même taille, mêmes cheveux. Il respire vite, les épaules trop hautes, comme quelqu'un qui vient de courir longtemps."

    "Et dans sa main, il y a mon couteau."

    noam peur "C'est..."

    "Je reconnais les petites rayures sur le manche."

    noam "C'est mon couteau."

    dg_noam fatigue "Ouais."

    "Ma voix sort de sa bouche. Pas exactement comme je l'entends quand je parle ; plutôt comme dans un enregistrement qu'on n'aime pas réécouter."

    noam desespoir "T'es quoi ?"

    dg_noam inquiet "Bouge pas. S'il te plaît, bouge pas."

    noam colere "Tu débarques dans ma chambre avec MA gueule et MON couteau et tu me demandes de pas bouger ?!"

    dg_noam "J'ai pas le temps de t'expliquer tout ça."

    noam "Alors commence par poser le couteau."

    dg_noam fatigue "Je peux pas."

    "Sa main tremble tellement que la pointe bouge avec elle."

    noam inquiet "Pourquoi tu me ressembles ?"

    dg_noam "Parce que je suis..."

    "Il bloque."

    dg_noam doute "Enfin... je sais pas comment te le dire sans que ça sonne complètement dingue."

    noam colere "Essaie."

    dg_noam "J'ai tes souvenirs."

    noam "Non."

    dg_noam "Si."

    noam "Non, t'as peut-être copié des trucs, je sais pas, mais—"

    dg_noam "Je me souviens de notre mère qui nous criait dessus quand on rentrait trop tard."

    noam colere "Ferme-la."

    dg_noam "Je me souviens de la maison. De l'escalier qui grinçait au milieu. De la poignée de la salle de bain qu'il fallait relever sinon—"

    noam "FERME-LA."

    "Il s'arrête, mais juste une seconde."

    dg_noam inquiet "Je me souviens de Juliette."

    "Tout mon corps se fige."

    noam peur "Ne parle pas d'elle."

    dg_noam "Pourquoi ? Parce que c'est ta sœur ?"

    noam colere "Oui. MA sœur."

    dg_noam colere "Et tu crois que moi, quand je pense à elle, je pense à quoi ? À un fichier ? À une photo ?"

    noam "T'as volé mes souvenirs."

    dg_noam "Je les ai pas volés ! Je me suis réveillé avec !"

    "Sa voix monte d'un coup, puis il jette un regard paniqué vers la porte."

    dg_noam fatigue "Je les ai. C'est tout. Je sais pas comment te dire ça autrement."

    noam inquiet "Et tu veux quoi de moi ?"

    show noam inquiet at j21_dg_noam_approach(1.05) with dissolve

    "Il fait un pas."

    dg_noam "Je veux partir."

    noam "Alors pars."

    dg_noam fatigue "Je peux pas."

    "Il lève à peine le couteau, comme s'il avait honte de me montrer la réponse."

    dg_noam "Pas tant que t'es là."

    noam panne "..."

    "Je comprends avant qu'il le dise."

    noam peur "Tu veux prendre ma place."

    dg_noam "Je dois prendre ta place."

    noam colere "Non. Tu veux. C'est pas pareil."

    dg_noam colere "Tu crois que j'ai envie de faire ça ?!"

    show noam colere at j21_dg_noam_approach(1.14) with dissolve

    "Il avance encore. Cette fois je recule."

    dg_noam "La navette part aujourd'hui. Eux, ils ont déjà leur place. Moi non."

    noam reflexion "Eux ?"

    dg_noam "..."

    "Kael me revient immédiatement en tête : sa question d'hier, son hésitation, puis sa phrase de ce matin."

    noam panne "Kael..."

    "Il baisse les yeux une demi-seconde."

    "C'est suffisant."

    noam desespoir "Putain... C'était pour ça."

    dg_noam fatigue "Il voulait savoir ce que tu ferais."

    noam "Et vous avez décidé quoi ?"

    dg_noam "De partir."

    noam colere "En me tuant."

    dg_noam inquiet "Je veux pas te tuer."

    noam "Arrête. T'as un couteau dans la main."

    dg_noam "Parce que si je viens sans rien, tu fais quoi ? Tu m'offres ton badge et ta place ?"

    noam "Évidemment que non !"

    dg_noam "Voilà !"

    "Sa voix se brise presque sur le mot."

    show noam desespoir at j21_dg_noam_approach(1.24) with dissolve

    dg_noam "Si tu montes dans cette navette, moi je reste ici. C'est fini. J'ai même pas une autre identité, pas un autre endroit où aller. Rien."

    noam colere "Et moi alors ?!"

    dg_noam "Je sais !"

    noam "Non, tu sais pas !"

    dg_noam "SI !"

    "On se tait tous les deux, à bout de souffle alors qu'aucun de nous n'a encore bougé assez pour justifier ça."

    dg_noam fatigue "Tu l'as dit hier."

    noam reflexion "Quoi ?"

    dg_noam "Quand t'as une sortie, tu la prends. Si rester change rien, tu pars."

    noam colere "Ça n'a rien à voir et tu le sais."

    dg_noam "Pourquoi ?"

    noam "Parce que dans ton scénario, la personne que tu laisses derrière, c'est moi !"

    dg_noam colere "PARCE QUE MOI AUSSI JE VEUX VIVRE !"

    pause 0.5

    "Sa voix remplit la chambre puis retombe d'un coup."

    "Ses yeux brillent."

    show noam desespoir at j21_dg_noam_approach(1.34) with dissolve

    dg_noam "Moi aussi je veux serrer Juliette dans mes bras ! Moi aussi je veux rentrer, ouvrir cette putain de porte et la voir me sauter dessus comme si j'étais parti trois ans !"

    noam panne "..."

    dg_noam "Tu crois que ça me fait rien ? Tu crois que parce que je suis arrivé après toi, tout ce que j'ai là-dedans compte moins ?"

    noam peur "T'es pas moi."

    dg_noam fatigue "Je sais."

    "Il avale difficilement."

    dg_noam "Je sais que je suis pas toi. Mais j'ai peur comme toi. Je l'aime comme toi. Et dans une heure, si j'échoue, je reste tout seul ici pendant que toi tu repars avec tout."

    noam "Tu me demandes quoi, exactement ? Que je me laisse tuer parce que t'es triste ?"

    dg_noam colere "NON !"

    "Il serre les dents, cherche ses mots, puis secoue la tête."

    dg_noam fatigue "Je te demande rien. C'est justement ça le problème."

    show noam inquiet at j21_dg_noam_approach(1.46) with dissolve

    "Il s'approche encore."

    noam peur "Reste où tu es."

    dg_noam "Désolé."

    noam "Noam—"

    "Le prénom sort tout seul. Il nous fait hésiter tous les deux."

    noam peur "Attends."

    show noam colere at j21_dg_noam_approach(1.60) with Dissolve(0.18)

    "Il avance."

    jump _21_0_1_1_0_1_QTE


label _21_0_1_1_0_1_QTE:

    scene bg_chambre at adaptive_fullscreen with vpunch

    "Je recule au moment où il se jette sur moi."

    play sound "audio/sfx_thud.mp3" volume 0.95
    call impact_fx("hard", direction="right")

    "Son épaule me percute en plein torse."

    "Je lui attrape le poignet avant que la lame descende."

    noam colere "LÂCHE ÇA !"

    dg_noam "ARRÊTE DE BOUGER !"

    noam "T'ES SÉRIEUX ?!"

    "Nos mains tremblent entre nous."

    "Le couteau descend lentement."

    $ unlock_gallery_image("bg_cg057")
    scene bg_cg057 at adaptive_fullscreen with vpunch

    "Je pousse de toutes mes forces."

    dg_noam "J'AI PAS LE TEMPS !"

    noam "ALORS CASSE-TOI !"

    dg_noam "OÙ ?!"

    $ j21_leave_qte_success = False

    python:
        j21_leave_trace_steps = [
            {"path_type": "curve_right", "time_limit": 1.15, "wait_time": 0.24, "tolerance": 29, "max_errors": 1, "anchor_x": 750, "anchor_y": 625, "start_radius": 68},
            {"path_type": "s_curve", "time_limit": 1.02, "wait_time": 0.20, "tolerance": 27, "max_errors": 1, "anchor_x": 1110, "anchor_y": 610, "start_radius": 64},
            {"path_type": "arc", "time_limit": 0.92, "wait_time": 0.18, "tolerance": 25, "max_errors": 1, "anchor_x": 840, "anchor_y": 640, "start_radius": 62},
            {"path_type": "curve_left", "time_limit": 0.84, "wait_time": 0.16, "tolerance": 23, "max_errors": 1, "anchor_x": 1080, "anchor_y": 625, "start_radius": 60},
            {"path_type": "s_curve", "time_limit": 0.76, "wait_time": 0.14, "tolerance": 21, "max_errors": 1, "anchor_x": 920, "anchor_y": 610, "start_radius": 56},
        ]

    call trace_qte_sequence(
        j21_leave_trace_steps,
        "bg_chambre",
        start_zoom=1.0,
        zoom_step=0.055,
        show_tutorial=False
    ) from _call_trace_qte_sequence_j21_leave
    $ j21_leave_trace_result = _return

    if j21_leave_trace_result["success"]:
        $ j21_leave_qte_success = True
        jump _21_0_1_1_0_1_QTE_REUSSITE

    jump _21_0_1_1_0_1_QTE_ECHEC


label _21_0_1_1_0_1_QTE_ECHEC:

    scene bg_chambre at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 1.0
    call impact_fx("brutal", direction="left", blood="spray")

    "Mon pied glisse."

    "Ça suffit."

    "Mon dos heurte le bord du lit et ma prise lâche une fraction de seconde."

    noam peur "Non—"

    play sound "audio/sfx_tinnitus.wav" volume 0.60
    call impact_fx("critical", direction="right", blood="screen")

    "La lame entre sous mes côtes."

    noam panne "..."

    "Je ne sens presque rien au début."

    "Juste un choc."

    "Puis la douleur arrive."

    "Mes jambes lâchent."

    "L'autre Noam me retient avant que je tombe complètement."

    dg_noam peur "Merde... Non, non, non..."

    "Il me rattrape avant que je m'effondre et me descend lentement jusqu'au sol, comme si me laisser tomber maintenant pouvait encore changer quelque chose."

    noam peur "Iris..."

    dg_noam "Chut. Bouge pas."

    noam "Va... la chercher..."

    dg_noam desespoir "Je peux pas."

    noam colere "Va la chercher, putain..."

    "J'essaie de repousser son bras, mais ma main glisse presque aussitôt."

    dg_noam "Je suis désolé. Je voulais pas que ça..."

    noam desespoir "Ferme-la."

    "Il se tait."

    noam "Juliette..."

    "Son visage se déforme immédiatement."

    dg_noam fatigue "Je sais."

    noam colere "Non... tu sais rien."

    dg_noam "Je sais qu'elle déteste qu'on touche à ses cheveux quand elle vient de se lever. Je sais qu'elle fait semblant de pas aimer les câlins quand elle est énervée. Je sais—"

    noam desespoir "ARRÊTE..."

    "Le mot sort à peine."

    dg_noam peur "Désolé."

    noam "T'approche pas d'elle..."

    dg_noam "Je lui ferai jamais de mal."

    noam colere "T'es pas..."

    "Ma voix disparaît avant la fin."

    "Je sais exactement ce que je voulais dire."

    "Lui aussi."

    scene black with suffocation_cut
    stop music fadeout 1.5
    $ danger_off()

    "Je pense à Juliette."

    "Puis plus rien."

    pause 2.0

    jump _21_0_1_1_0_1_FIN_A_MA_PLACE


label _21_0_1_1_0_1_FIN_A_MA_PLACE:

    # La narration quitte Noam : l'original est mort.
    scene bg_chambre at adaptive_fullscreen with creep_diss
    play music "audio/music/bgm_epilogue_cold.mp3" fadein 2.0

    "Noam reste assis au sol pendant plusieurs secondes."

    "Il regarde le corps devant lui."

    "Son propre visage."

    "Ses propres mains."

    "Du sang sur ses doigts."

    "Il ferme les yeux."

    play sound "audio/sfx_duct_scrape.wav" volume 0.58

    "Un mouvement vient du conduit."

    show kael doute at left with dissolve
    show noam fatigue at right with dissolve

    "Kael sort à son tour."

    "Il comprend immédiatement."

    kael doute "T'as réussi."

    "Noam ne répond pas."

    kael inquietude "On a moins d'une heure."

    dg_noam "Je sais."

    "Kael regarde le corps."

    kael "Il faut le bouger."

    "Noam baisse les yeux vers ses vêtements tachés."

    dg_noam "Iris va revenir."

    kael "Alors dépêche-toi."

    scene black with dissolve

    "Quelques minutes plus tard, le corps disparaît dans le conduit."

    "Les vêtements aussi."

    "Le sang est nettoyé comme il peut l'être."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Noam récupère le badge."

    "Le téléphone."

    "Le sac."

    "Tout ce qui appartient à Noam."

    "Tout ce qui lui appartient maintenant."

    "L'écran du téléphone s'allume."

    "Une photo de Juliette apparaît."

    pause 0.7

    dg_noam "..."

    "Il passe son pouce sur l'écran."

    dg_noam "J'arrive."

    play sound sfx_door

    show iris inquiet at left with dissolve

    iris "Noam ?"

    "Il verrouille immédiatement le téléphone."

    dg_noam "Ouais."

    iris "J'ai entendu un truc."

    dg_noam "J'ai fait tomber mon sac."

    "Elle regarde la chambre."

    "Puis son visage."

    iris reflexion "Ça va ?"

    "Il hésite une fraction de seconde."

    dg_noam "Oui."

    iris blase "T'as encore cette tête bizarre."

    dg_noam "Quelle tête ?"

    iris "Celle où t'essaies de me convaincre que tout va bien."

    "Noam sourit faiblement."

    dg_noam "On rentre, Iris."

    "Elle le fixe encore une seconde."

    iris fatigue "Ouais."

    iris "On rentre."

    scene black with dissolve

    play sound sfx_announce
    scene bg_diffusion_taquin at adaptive_fullscreen with signal_stutter
    show screen kami_broadcast_ui

    kami "Dix minutes avant fermeture du sas."
    kami "Dix petites minutes. Je sais, le temps passe vite quand on s'amuse."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Alors bougez-vous."

    hide screen kami_broadcast_ui

    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with fade

    "Les représentants prennent place à bord."

    "Noam s'assoit."

    "Iris juste en face de lui."

    "Kael quelques sièges plus loin."

    "La navette se détache du Conclave."

    "La Terre grandit derrière les hublots."

    "Noam sort discrètement son téléphone."

    "La photo de Juliette est toujours là."

    "Cette fois, son sourire n'a rien de victorieux."

    "Il a seulement l'air terrifié."

    dg_noam "Encore un peu..."

    scene black with signal_stutter
    stop music fadeout 0.25

    pause 1.0

    call screen kd_ending_reached(
        "À ma place",
        "ENDING 03 // JOUR 21"
    )
    $ _ending_screen_closed = _return

    return


label _21_0_1_1_0_1_QTE_REUSSITE:

    scene bg_chambre at adaptive_fullscreen with vpunch

    "Je pousse son poignet sur le côté au dernier moment."

    play sound sfx_drop

    "Le couteau m'échappe presque, mais je réussis à frapper sa main contre le bord du lit."

    "La lame tombe au sol."

    dg_noam "NON !"

    "Il se jette sur moi à mains nues."

    play sound "audio/sfx_thud.mp3" volume 0.92
    call impact_fx("hard", direction="left")

    "On s'écrase tous les deux contre le mur."

    noam colere "ARRÊTE !"

    dg_noam "JE PEUX PAS !"

    "Il essaie de me faire tomber."

    "Je l'attrape par le col."

    "Pendant une seconde, j'ai mon propre visage à quelques centimètres du mien."

    "Même peur."

    "Même rage."

    "Même envie de sortir d'ici."

    play sound sfx_door
    scene bg_chambre at adaptive_fullscreen with vpunch

    iris colere "NOAM ?!"

    "On se fige tous les deux."

    "Iris reste dans l'encadrement, une main encore sur la poignée. Son sac lui échappe et tombe lourdement."

    $ unlock_gallery_image("bg_cg058")
    scene bg_cg058 at adaptive_fullscreen with signal_stutter

    iris panne "..."

    "Elle me regarde, puis lui, puis revient vers moi comme si ses yeux refusaient de garder les deux images en même temps."

    iris peur "Non... Non, c'est quoi ce bordel ?!"

    dg_noam inquiet "Iris, attends, je peux—"

    noam desespoir "IL A MON COUTEAU !"

    dg_noam colere "Parce qu'il allait pas gentiment me laisser—"

    iris colere "FERMEZ-LA ! LES DEUX !"

    "Le silence tombe une demi-seconde."

    "Son regard descend sur la lame au sol, puis remonte sur l'autre Noam qui essaie déjà de se dégager."

    dg_noam inquiet "Iris, s'il te plaît."

    iris determine "Toi, tu bouges plus."

    dg_noam "Mais—"

    "Iris n'attend pas."

    play sound "audio/sfx_thud.mp3" volume 1.0
    call impact_fx("hard", direction="right")

    "Son pied frappe l'autre Noam derrière le genou."

    "Il s'effondre."

    play sound "audio/sfx_thud.mp3" volume 0.92

    "Je lui bloque immédiatement le bras."

    iris colere "Tiens-le !"

    noam "J'essaie !"

    dg_noam "LÂCHEZ-MOI !"

    "Iris attrape une sangle du sac et me la tend."

    "À deux, on finit par lui coincer les poignets derrière le dos."

    "Il se débat encore quelques secondes."

    "Puis il comprend."

    "Il s'arrête."

    $ danger_off()
    stop music fadeout 1.0

    show iris peur at left with dissolve
    show noam fatigue at right with dissolve

    "Iris reste debout devant lui."

    "Elle a blêmi."

    iris panne "Noam..."

    noam fatigue "Je sais."

    iris "Non, justement, tu sais pas. Je viens de rentrer et y'en a deux."

    noam "Je sais."

    iris colere "Arrête de dire 'je sais' !"

    "Sa voix craque presque. Elle se passe une main sur le visage."

    iris peur "Je sais même pas lequel regarder."

    dg_noam fatigue "On n'a pas le temps pour ça."

    iris colere "Toi, tu fermes ta gueule deux secondes."

    dg_noam "..."

    iris inquiet "Et toi..."

    "Elle se tourne vers moi."

    iris "Dis-moi un truc que lui peut pas savoir."

    noam panne "Iris..."

    dg_noam fatigue "Il peut pas."

    iris colere "J'AI DIT FERME-LA !"

    "Il baisse les yeux."

    noam fatigue "Il a mes souvenirs."

    "Iris me fixe."

    iris peur "Tous ?"

    noam "Je crois."

    "Elle recule d'un pas, comme si cette réponse était pire que le reste."

    iris fatigue "Putain..."

    play sound sfx_announce
    scene bg_diffusion_professeur at adaptive_fullscreen with signal_stutter
    show screen kami_broadcast_ui

    kami "Petit rappel pédagogique."
    kami "Il vous reste trente minutes avant fermeture du sas."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Trente minutes, c'est très long."
    kami "Sauf quand on a quelque chose d'important à régler, évidemment."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with signal_stutter

    "Le message nous coupe tous les trois."

    "L'autre Noam ferme les yeux."

    noam reflexion "Combien ?"

    dg_noam "..."

    noam "Combien vous êtes ?"

    dg_noam "Ça change quoi ?"

    noam colere "KAEL EN EST UN ?"

    "Il ne répond pas."

    "Encore une fois, ça suffit."

    iris surpris "Kael ?"

    noam "Sa question hier."

    iris "Noam, de quoi tu—"

    noam "Il savait."

    "Je regarde mon double."

    noam "Il savait exactement pourquoi il me demandait ça."

    dg_noam "Et tu lui as répondu."

    noam panne "..."

    dg_noam "Tu lui as dit de partir."

    iris colere "Arrête de parler comme si c'était sa faute !"

    dg_noam "J'ai pas dit ça."

    "Il relève les yeux vers moi."

    dg_noam "Je dis juste qu'il avait raison."

    noam reflexion "Tu viens d'essayer de me tuer."

    dg_noam "Parce que moi aussi je veux vivre."

    "Sa voix est beaucoup plus basse maintenant."

    dg_noam "C'est tout."

    "Iris serre la mâchoire."

    dg_noam "Si je reste ici, c'est fini pour moi."

    noam "Et si tu pars, c'est fini pour moi."

    "Il baisse les yeux."

    dg_noam "Ouais."

    "Personne ne parle pendant quelques secondes."

    play sound sfx_announce
    scene bg_diffusion_zen at adaptive_fullscreen with signal_stutter
    show screen kami_broadcast_ui

    kami "Vingt minutes."
    kami "Vous voyez ? Même sans vote, je peux encore vous offrir un joli compte à rebours."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Profitez-en. C'est probablement le dernier."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with signal_stutter

    iris inquiet "On fait quoi ?"

    "Je regarde l'autre Noam."

    "Il comprend immédiatement."

    dg_noam peur "Non."

    noam "..."

    dg_noam "Non, attends."

    "Il tire sur ses liens."

    dg_noam "Tu vas vraiment me laisser ici ?"

    "La question me frappe beaucoup plus fort que prévu."

    "Hier, Kael m'a posé exactement la même."

    "Sans visage."

    "Sans couteau."

    "Sans me dire qui resterait derrière."

    dg_noam "Noam."

    "Je me relève."

    dg_noam "S'il te plaît."

    noam fatigue "Je t'ai déjà répondu hier."

    "Il se fige."

    noam "Sans savoir que je te répondais à toi."

    dg_noam "..."

    noam "La navette part."

    dg_noam colere "PUTAIN !"

    "Il se débat brutalement."

    iris inquiet "Noam..."

    noam determine "On y va."

    "Iris reste immobile."

    noam "Si on rate cette navette, ça fera juste..."

    "Je n'arrive pas à finir."

    "Je regarde mon propre visage au sol."

    "Il sait très bien comment se termine la phrase."

    dg_noam fatigue "Deux personnes coincées au lieu d'une."

    noam panne "..."

    "Je ramasse mon sac."

    iris triste "Je suis désolée."

    dg_noam "Ouais."

    "Iris ramasse le couteau."

    "Puis elle me rejoint dans le couloir."

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_epilogue_cold.mp3" fadein 1.5

    "Je ferme la porte derrière nous."

    "Je n'arrive pas à regarder Iris."

    iris inquiet "Tu crois qu'on devrait prévenir les autres ?"

    noam "Oui."

    iris "Mais ?"

    noam "Mais on a quinze minutes et je sais même pas qui est encore..."

    "Je m'arrête."

    iris peur "Humain ?"

    "Je déteste le mot."

    noam "Ouais."

    "On accélère."

    play sound sfx_announce
    scene bg_diffusion_colere at adaptive_fullscreen with signal_stutter
    show screen kami_broadcast_ui

    kami "Quinze minutes !"
    kami "Je commence à reconnaître ce délicieux parfum de panique de dernière minute."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Allez. Un dernier effort."
    kami "Je serais presque triste d'en perdre un maintenant."

    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with signal_stutter

    "Au bout du couloir, Kael apparaît."

    show kael calme at center with dissolve

    "Il marche vers le sas avec son sac sur l'épaule."

    "Puis il me voit."

    "Il s'arrête."

    kael doute "..."

    "Ses yeux passent sur mon visage."

    "Puis sur Iris."

    "Puis sur le couteau qu'elle tient encore."

    "Quelque chose change dans son expression."

    "Pas de surprise."

    "Plutôt une déception très brève."

    noam panne "..."

    "On se regarde."

    kael doute "T'as réussi à être prêt."

    noam "Ouais."

    "Il hoche lentement la tête."

    kael "Alors viens."

    "Il reprend sa marche."

    "Iris me regarde."

    iris inquiet "Noam ?"

    noam fatigue "Après."

    "Je repars."

    jump _21_0_1_1_0_1_FIN_LAISSE_DERRIERE


label _21_0_1_1_0_1_FIN_LAISSE_DERRIERE:

    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with fade

    "Les portes se ferment derrière nous."

    "Je reste debout une seconde de trop avant de m'asseoir."

    "Iris prend la place à côté de moi."

    "Kael est plus loin."

    "Je ne le quitte presque pas des yeux."

    iris inquiet "On va devoir parler."

    noam fatigue "Je sais."

    iris "À tout le monde. Et pas dans deux jours, pas quand on sera tranquilles. Dès qu'on peut."

    noam "Je sais."

    iris colere "Arrête avec ça."

    noam surpris "Avec quoi ?"

    iris fatigue "Avec ton 'je sais'. Là, t'as le droit de pas savoir quoi faire."

    "Je tourne enfin la tête vers elle."

    noam "J'ai laissé quelqu'un derrière."

    iris inquiet "Quelqu'un qui venait d'essayer de te tuer."

    noam "Quelqu'un qui voulait vivre."

    "Elle ne répond pas tout de suite."

    iris triste "Ouais."

    "Sa main vient chercher la mienne entre les sièges."

    iris fatigue "Et toi aussi."

    "Je serre ses doigts sans répondre."

    play sound sfx_announce
    scene bg_diffusion_champagne at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    kami "Eh bien... voilà."
    kami "Vous y êtes."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Bon retour sur Terre, mes chers représentants."
    kami "Essayez de ne pas tout casser trop vite."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'aimerais pouvoir prétendre que vous allez me manquer."

    pause 0.4

    kami "Allez."
    kami "Partez."

    hide screen kami_broadcast_ui
    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with dissolve

    "La navette tremble."

    "Puis le Conclave commence à s'éloigner."

    scene black with dissolve

    "Dans ma chambre, quelqu'un tire encore sur ses liens."

    scene bg_chambre at adaptive_fullscreen with creep_diss

    show noam fatigue at center with dissolve

    "L'autre Noam a cessé de crier."

    "Il est assis contre le bord du lit, les poignets toujours attachés."

    "Le silence de la station revient peu à peu."

    play sound sfx_announce
    scene bg_diffusion_taquin at adaptive_fullscreen with signal_stutter
    show screen kami_broadcast_ui

    kami "Et voilà."
    kami "Vaisseau désarrimé."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "Ils sont partis."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Enfin... presque tous."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with signal_stutter

    "Il ferme les yeux."

    dg_noam "..."

    "Puis il laisse échapper un petit rire épuisé."

    dg_noam "Ouais."

    "Il regarde la porte fermée."

    $ unlock_gallery_image("bg_cg059")
    scene bg_cg059 at adaptive_fullscreen with creep_diss

    dg_noam "Deux personnes coincées au lieu d'une."

    "Son sourire disparaît."

    scene black with signal_stutter
    stop music fadeout 0.25

    pause 1.0

    call screen kd_ending_reached(
        "Celui qu'on laisse derrière",
        "ENDING 04 // JOUR 21"
    )
    $ _ending_screen_closed = _return

    return
