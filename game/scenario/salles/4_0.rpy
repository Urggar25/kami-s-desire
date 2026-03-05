label _4_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4

    pause 1.5  # Légèrement plus long pour accentuer la lourdeur

    $ blink()
    "Je me réveille… ou plutôt, je reviens à moi."
    $ blink()
    "La lumière bleue des veilleuses est toujours là, mais aujourd’hui elle donne l’impression d’un néon fatigué qui clignote à peine."

    "Hier, on a voté."
    "On a eu une chance. Une vraie."
    "Et on l’a laissée filer."
    "Le bouton vert est resté éteint. Au moins l'un d'entre nous a dit non."
    "Et le monde continue de tourner exactement comme avant."

    $ blink()
    "Je reste immobile, les bras morts le long du corps."
    "Mon cœur bat lentement, presque à contrecœur, comme s’il économisait ses forces pour une journée qui ne vaut pas la peine d’être vécue."

    "On a gardé les bons de rationnement."
    "On a gardé la sécurité."
    "On a gardé nos chaines."

    $ blink()
    pause 2.5  # Pause plus longue pour laisser peser le vide

    "Je me tourne à moitié. La photo holographique sur la table de nuit me fixe."
    "Une famille souriante. Pas la mienne."
    "Je me demande si eux aussi ont un bon de rationnement ce matin."
    "Ou si, quelque part, ils ont déjà arrêté de sourire depuis longtemps."

    play sound sfx_announce
    "Un bip strident déchire le silence."
    "L’écran s’allume brutalement, lumière blanche et clinique."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits anges de la prudence !"
    kami "Il est 8 heures, et devinez quoi ? La révolution est officiellement annulée !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit briefing matinal, parce que je sais que vous raffolez quand je vous rappelle à quel point vous êtes raisonnables :"
    kami "La situation est toujours impeccables. Pas une pièce qui circule, pas une once de liberté."
    kami "Vous avez l'avez voulu, vous l'aurez !."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C’est beau, non ? Le calme avant… ben, le calme, en fait."
    kami "Pas d’alarme, pas de chaos."
    kami "Juste la douce certitude que demain sera exactement comme aujourd’hui."
    kami "Alors, je tiens à tous vous remercier :"
    kami "Merci de m'avoir donné raison. L'humanité ne veut pas de cette liberté que vous dites pourtant chérir."
    kami "Elle est bien moins importante que le certitude de pouvoir être nourris."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Allez, ne faites pas cette tête !"
    kami "Vous verrez tout ça de vos propres yeux à la cafétéria. Les écrans sont chauds, vos rations sont prêtes."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    "L’écran s’éteint. Le silence retombe, épais comme du béton."
    "Je reste assis, les mains posées sur mes genoux, inertes."
    "Elle n’a même pas besoin de mentir."
    "On n’a rien changé. Et on n’a même pas le courage de le regretter à voix haute."

    pause 1.8

    play sound sfx_drop
    "Un bruit mat dans le couloir. Comme un poing contre du métal."
    "Un cri bref, étouffé, presque honteux."
    "Puis plus rien."

    "Je me lève lentement. Pas d’un bond. Pas la force."
    "Mon cœur cogne, mais c’est un cognement fatigué."
    "Je tends l’oreille. Silence."
    "Juste l’écho de ce cri, et la certitude que ce n’est que le début de quelque chose qui se fissure sans bruit."

    "Ça n’a pas encore explosé."
    "Mais ça pourrait à tout moment."

    jump _4_0_CAFETERIA_ECRANS