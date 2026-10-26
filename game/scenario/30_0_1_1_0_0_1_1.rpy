# JOUR 30 — ROUTE SECRÈTE : JULIAN NON SAUVÉ
# Lancement après le J29. Départ de la navette à 10 h.
# Si Julian a survécu, il faudra écrire sa propre variante de J30.
default j30_secret_zero_choice = None
default j30_secret_ending = None

label _30_0_1_1_0_0_1_1_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"
    $ j30_secret_zero_choice = None
    $ j30_secret_ending = None
    if j29_julian_syringe_swapped:
        jump _30_0_1_1_0_0_1_1_JULIAN_VIVANT_PLACEHOLDER
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6
    "Je regarde l'heure sur ma tablette. 7 h 02. Je suis réveillé depuis un moment, mais j'ai pas réussi à sortir de mon lit."
    "Sur mon bureau, je retrouve le dessin de Juliette. Elle me l'avait donné avant mon départ. Je le garde un instant dans les mains, puis le repose soigneusement."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Bonjour, mes chers passagers ! Aujourd'hui, on rentre à la maison ! Enfin... certains d'entre vous. À 9 h, embarquement, et à 10 h, décollage !"
    kami "Merci de ne pas oublier vos affaires, vos petits secrets et vos merveilleux souvenirs du Conclave. Les retards ne seront pas acceptés, même avec une très bonne excuse !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Dix heures. Dans moins de trois heures, la navette sera partie."
    "On frappe doucement à ma porte. Quand je l'ouvre, c'est mon double qui attend, un sac à la main."
    # Durée : 1m

label _30_0_1_1_0_0_1_1_DOUBLE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.27), ("dg_noam", "neutre", 0.73)])
    dg_noam neutre "Salut... Désolé de débarquer comme ça, mais je voulais te voir avant qu'on parte. Je peux entrer ?"
    noam reflexion "Ouais. Vas-y."
    "Il entre et pose son sac près de la porte, puis il regarde mon lit comme s'il hésitait à s'asseoir."
    dg_noam inquiet "Bon... je sais pas si t'as pris une décision. Zero m'a rien dit, et je veux pas te mettre la pression. Je voulais juste savoir ce que tu comptes faire."
    noam fatigue "J'en sais rien. Je me suis retourné toute la nuit. J'ai surtout pensé à Juliette."
    dg_noam raison "Ouais, je me doute. Tu lui avais promis de rentrer."
    noam inquiet "C'est pas juste la promesse. C'est ma petite sœur. Je peux pas lui demander d'attendre encore je sais pas combien de temps."
    dg_noam neutre "Je comprends. Si tu veux rentrer, dis-le-moi. Je vais pas te piquer la navette dans ton dos."
    noam reflexion "Et toi ? Tu veux faire quoi ?"
    dg_noam inquiet "Je vais pas te mentir : j'ai envie de partir. Je veux voir la Terre, et surtout j'ai envie de continuer avec Iris."
    noam agace "Elle sait même pas que t'es pas moi."
    dg_noam raison "Je sais. Et je te demande pas de trouver ça normal, mais les trucs que je lui ai dits, je les pensais vraiment. Je suis pas juste en train de jouer ton rôle."
    noam fatigue "Ça fait bizarre de t'entendre parler d'elle comme ça."
    dg_noam fatigue "Ouais... j'imagine."
    noam inquiet "Et si vous finissez pas dans le même district ? Tu t'es posé la question ?"
    dg_noam neutre "Oui. On trouvera un moyen de se voir. On sera pas obligés de vivre à l'autre bout de la planète sans jamais se parler. Enfin, j'espère. J'ai envie qu'on essaie, quoi."
    noam raison "Et si c'est moi qui rentre ?"
    dg_noam inquiet "Alors... je vais devoir trouver autre chose. Je te dis pas que ça me fera plaisir. Mais c'est toi qui décides, Noam."
    noam surpris "Tu me demandes même pas de te laisser ma place ?"
    dg_noam fatigue "Je te dis que j'en ai envie. Ça suffit, non ? Je vais pas te faire culpabiliser avec Juliette en plus."
    "Il remarque le dessin posé sur le bureau. Je le récupère avant qu'il dise quoi que ce soit."
    dg_noam neutre "Je m'en souviens, de ce dessin."
    noam fatigue "Ouais. Moi aussi."
    dg_noam raison "On va bientôt devoir bouger. Tu veux encore réfléchir deux minutes ?"
    noam inquiet "Non. Si j'attends encore, je vais jamais me décider."
    $ hideGroup()
    jump _30_0_1_1_0_0_1_1_CHOIX
    # Durée : 2m30

label _30_0_1_1_0_0_1_1_CHOIX:
    # Le choix se fait directement face au double, sans revoir Zero.
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "hesitation", 0.27), ("dg_noam", "inquiet", 0.73)])
    "Je regarde le dessin de Juliette, puis mon double. Il ne dit rien. Il attend que je me décide."
    $ hideGroup()
    # CG 074 : les deux Noam face au dessin de Juliette, au moment du choix final.
    if renpy.loadable("images/background/cg/bg_cg074.png"):
        $ unlock_gallery_image("bg_cg074")
        scene bg_cg074 at adaptive_fullscreen with dissolve
    menu (screen="critical_choice", noam_expr="hesitation", cc_targets={"Retourner sur Terre":{"label":"_30_0_1_1_0_0_1_1_RETOUR"},"Aller sur Keyper-IIB":{"label":"_30_0_1_1_0_0_1_1_KEYPER"}}):
        "QU'EST-CE QUE JE DÉCIDE ?"
        "Retourner sur Terre":
            $ j30_secret_zero_choice = "refuse"
            jump _30_0_1_1_0_0_1_1_RETOUR
        "Aller sur Keyper-IIB":
            $ j30_secret_zero_choice = "accept"
            jump _30_0_1_1_0_0_1_1_KEYPER
    # Durée : 1m

label _30_0_1_1_0_0_1_1_RETOUR:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "fatigue", 0.27), ("dg_noam", "inquiet", 0.73)])
    noam raison "Je vais rentrer. J'ai promis à Juliette que je serais là, et j'arrive pas à me dire que je vais encore lui faire faux bond."
    dg_noam fatigue "D'accord... Ouais. Je m'en doutais un peu."
    noam inquiet "Je suis désolé pour Iris. Je sais que t'as vraiment envie de la revoir."
    dg_noam raison "C'est pas grave. Enfin, si, ça me fait chier, évidemment. Mais c'était le risque quand on a échangé nos places."
    noam reflexion "Tu vas faire quoi, alors ?"
    dg_noam fatigue "Je sais pas encore. Je vais trouver. T'occupe pas de moi maintenant, la navette va pas t'attendre."
    noam neutre "Merci. Pour m'avoir laissé décider."
    dg_noam neutre "Ouais. Allez, file."
    $ hideGroup()
    jump _30_0_1_1_0_0_1_1_PETITE_SALLE_RETOUR
    # Durée : 1m

label _30_0_1_1_0_0_1_1_PETITE_SALLE_RETOUR:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    "Je passe par la petite salle où les autres terminent leurs préparatifs. Mara ferme un sac, Kael surveille l'heure."
    $ showGroup([("mara", "neutre", 0.17), ("kael", "calme", 0.49), ("noam", "fatigue", 0.82)])
    kael inquiet "Noam ? T'étais où ? On t'attendait. Tu fais quoi, là ?"
    noam raison "Je rentre chez moi. Je prends la navette."
    mara surpris "Attends, tu rentres ? Et ton original, t'en fais quoi ?"
    noam hesitation "Je... je me débrouille."
    mara agace "Tu te débrouilles ? Putain, c'est pas une réponse !"
    noam raison "C'est tout ce que je peux vous dire. Il reste pas une heure, j'ai pas envie de discuter pendant dix minutes."
    kael calme "Bon. Si t'as réglé ça, on te retrouve à l'embarquement. Mais fais attention."
    noam fatigue "Ouais."
    $ hideGroup()
    scene bg_sas at adaptive_fullscreen with dissolve
    "Au sas, Iris m'attrape par le bras dès qu'elle m'aperçoit."
    $ showGroup([("iris", "inquiet", 0.31), ("noam", "fatigue", 0.72)])
    iris inquiet "Eh ! Je te cherchais ! T'en as mis, du temps !"
    noam hesitation "Ouais, désolé. J'avais un truc à régler."
    iris agace "Bon, tu viens ? Ils vont fermer les portes et j'ai pas envie de courir après toi."
    noam raison "J'arrive. Et... faut qu'on parle, une fois qu'on sera partis."
    iris reflexion "Ouais, d'accord. Mais monte déjà, idiot."
    $ hideGroup()
    # CG 075 : Noam et Iris, dans la navette qui repart vers la Terre.
    if renpy.loadable("images/background/cg/bg_cg075.png"):
        $ unlock_gallery_image("bg_cg075")
        scene bg_cg075 at adaptive_fullscreen with dissolve
    else:
        scene bg_navette at adaptive_fullscreen with dissolve
    "À dix heures, la navette se détache du Conclave. Iris est assise à côté de moi, et les autres parlent déjà de leur retour."
    "Je pense à Julian. À celui qui est mort, et à celui qui est ici avec nous."
    "Je sors le dessin de Juliette de ma poche. Elle doit compter les jours depuis mon départ."
    think "J'arrive, Juliette. Cette fois, je rentre."
    $ j30_secret_ending = "retour_terre"
    scene black with fade
    stop music fadeout 0.2
    pause 1.2
    call screen kd_ending_reached(
        "Le poids du retour",
        "ENDING 03 // JOUR 30"
    )
    $ _ending_screen_closed = _return
    return
    # Durée : 3m

label _30_0_1_1_0_0_1_1_KEYPER:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "fatigue", 0.27), ("dg_noam", "inquiet", 0.73)])
    noam raison "Je vais sur Keyper. Tu peux rentrer sur Terre à ma place."
    dg_noam surpris "T'es sérieux ?"
    noam fatigue "Ouais. Je sais pas du tout comment je vais m'en sortir là-bas, mais je peux pas laisser tous ces gens sans même essayer."
    dg_noam inquiet "Et Juliette ?"
    noam raison "C'est justement ce dont je voulais te parler. Tu te souviens de sa promesse pour son anniversaire ?"
    dg_noam neutre "Ouais, je m'en souviens. Je lui dirai pas que tu l'as oubliée, promis."
    noam agace "C'est pas ce que je te demande. Fais attention à elle, d'accord ? C'est ma sœur, et elle a besoin de quelqu'un sur qui compter."
    dg_noam raison "Je ferai attention à elle. Et à Iris aussi. Je sais que tu me fais pas entièrement confiance, mais je te promets que je vais essayer de bien faire."
    noam fatigue "J'espère. Et arrête de dire à Iris que je suis nul au baby-foot."
    dg_noam surpris "Quoi ? J'ai jamais dit ça !"
    noam neutre "Ouais, ben fais pas ça, alors."
    "Il sourit, puis devient sérieux."
    dg_noam inquiet "Tu sais si tu pourras revenir ?"
    noam fatigue "Non. Zero le sait pas non plus."
    dg_noam raison "Putain... Bon. Fais gaffe à toi."
    noam neutre "Toi aussi."
    $ hideGroup()
    jump _30_0_1_1_0_0_1_1_PETITE_SALLE_KEYPER
    # Durée : 1m30

label _30_0_1_1_0_0_1_1_PETITE_SALLE_KEYPER:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    "Je retourne dans la petite salle. Les derniers sacs sont prêts. Kael et Mara relèvent la tête en me voyant."
    $ showGroup([("mara", "neutre", 0.17), ("kael", "calme", 0.49), ("noam", "fatigue", 0.82)])
    kael inquiet "Noam ? Qu'est-ce que tu fais encore là ? C'est l'heure d'aller au sas."
    noam raison "Je vais pas prendre la navette. Je pars sur Keyper avec Zero."
    mara surpris "Hein ? Depuis quand tu lui parles, toi ?"
    noam hesitation "Depuis hier. C'est compliqué, et on a pas le temps de tout reprendre."
    kael inquiet "Et... tu veux vraiment aller là-bas ?"
    noam raison "Ouais. Je sais pas si je pourrai revenir, mais j'ai décidé d'essayer de les aider."
    mara fatigue "Putain. Bon... on pourra pas dire que t'as choisi la solution facile."
    kael calme "C'est ta décision. Je vais pas te retenir, mais fais attention à ce que tu fais."
    noam neutre "Ouais. Vous aussi."
    $ hideGroup()
    scene bg_sas at adaptive_fullscreen with dissolve
    "Je reste en retrait, assez loin pour que personne ne me remarque. Iris rejoint mon double juste avant la fermeture des portes."
    $ showGroup([("iris", "neutre", 0.32), ("dg_noam", "neutre", 0.72)])
    iris agace "Enfin ! Ça fait vingt minutes que je te cherche !"
    dg_noam neutre "Je suis là. Allez, viens."
    "Ils montent ensemble, et je ne les vois plus."
    $ hideGroup()
    "Je rejoins Zero derrière le sas. Il porte toujours les traits de Nyra."
    $ showGroup([("noam", "fatigue", 0.28), ("nyra", "neutre", 0.72)])
    zero_nyra_j29 neutre "Tu as vraiment décidé de venir ?"
    noam raison "Ouais. Mais je te préviens, je te pardonne toujours pas ce qui s'est passé avec Julian."
    zero_nyra_j29 neutre "Je ne te demande pas de me pardonner. Tu peux encore renoncer."
    noam fatigue "Non. On y va."
    $ hideGroup()
    # CG 076 : Noam et Zero, dans la navette pour Keyper-IIB.
    if renpy.loadable("images/background/cg/bg_cg076.png"):
        $ unlock_gallery_image("bg_cg076")
        scene bg_cg076 at adaptive_fullscreen with dissolve
    else:
        scene bg_navette at adaptive_fullscreen with dissolve
    "À dix heures, la navette pour la Terre quitte le Conclave. Je la regarde s'éloigner depuis le hublot de la petite navette où Zero m'attend."
    "Je récupère le dessin de Juliette. Je ne sais pas si je la reverrai un jour, et rien que d'y penser, j'ai envie de tout arrêter."
    "Mais la Terre disparaît lentement derrière nous. Notre navette se met en route vers Keyper-IIB."
    think "Je suis désolé, Juliette. J'espère que tu comprendras un jour."
    $ j30_secret_ending = "keyper"
    scene black with fade
    stop music fadeout 0.2
    pause 1.2
    call screen kd_ending_reached(
        "À ta place",
        "ENDING 04 // JOUR 30"
    )
    $ _ending_screen_closed = _return
    return
    # Durée : 3m

label _30_0_1_1_0_0_1_1_JULIAN_VIVANT_PLACEHOLDER:
    # Ne jamais faire passer un Julian vivant pour mort : branche J30 à écrire.
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je repense à ce que j'ai fait avec la seringue. Si Julian est toujours vivant, il est peut-être encore au laboratoire."
    "Je dois le retrouver avant le décollage. Je peux pas faire comme si tout s'était passé normalement."
    "À suivre — Julian sauvé."
    return
    # Durée : 0m30
