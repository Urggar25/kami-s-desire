# ----------------------------------------------------------
# Interaction CHAMBRE 1 :
# ----------------------------------------------------------

label chambre1_aeration:
    think "Il y a une bouche d'aération ici."
    "Un souffle froid passe entre les lamelles et maintient la température dans la chambre."
    think "J'imagine que ce n'est pas bien compliqué de refroidir quelque chose dans l'espace..."
    jump CHAMBRE_TP

label chambre1_lit:
    menu:
        "M'allonger pour passer le temps libre.":
            think "Je m'allonge sur le lit et laisse le temps filer."
            jump FREE_TIME_END

        "Je ne suis pas encore pret a me reposer.":
            jump CHAMBRE_TP

label chambre1_television:
    "L'ecran est éteint."
    think "A vrai dire, c'est bien mieux comme ça."
    think "A chaque fois que Kami parle, on ne sait pas comment ça va finir..."
    jump CHAMBRE_TP

label chambre1_tiroir:
    "J'ouvre le tiroir et regarde ce qu'il y a dedans."
    think "Je n'ai quasimment rien eu comme affaire..."
    think "Si au moins on avait eu le temps de les préparer, mais non, il a fallu nous emmener ici immédiatement et quasiment de force...."
    jump CHAMBRE_TP

# ----------------------------------------------------------
# Interaction CHAMBRE 2 :
# ----------------------------------------------------------

label chambre2_armoire:
    "J'ouvre l'armoire."
    "Mes vêtements sont la, alignés, presque impersonnels."
    think "Je me demande si les autres ont eu plus d'affaires avec eux..."
    jump CHAMBRE_TP

label chambre2_porte_dehors:
    jump chambre2_porte_dehors_animation

label chambre2_porte_dehors_animation:
    hide screen pnc_chambre
    scene black

    show expression "images/background/bg_dortoir.png" as door_open_bg at adaptive_fullscreen
    show expression "images/background/interact/animation/door_open/porte1.png" as door_open_fg at adaptive_fullscreen
    with None
    $ renpy.pause(0.18, hard=True)

    show expression "images/background/interact/animation/door_open/porte2.png" as door_open_fg at adaptive_fullscreen
    $ renpy.pause(0.18, hard=True)

    show expression "images/background/interact/animation/door_open/porte3.png" as door_open_fg at adaptive_fullscreen
    $ renpy.pause(0.28, hard=True)

    # Zoom sur l'image finale de la porte ouverte
    show expression "images/background/bg_dortoir.png" as door_open_bg at adaptive_fullscreen, door_open_camera_zoom
    show expression "images/background/interact/animation/door_open/porte3.png" as door_open_fg at adaptive_fullscreen, door_open_camera_zoom

    show expression Solid("#000") as door_open_black at door_open_black_fade
    $ renpy.pause(1.15, hard=True)

    scene black
    jump DORTOIR_TP

transform door_open_camera_zoom:
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom 1.0
    easein 1.05 zoom 1.28

transform door_open_black_fade:
    alpha 0.0
    linear 0.85 alpha 1.0

label chambre2_porte_sdb:
    "Je regarde vers la salle de bain."
    think "Pas maintenant."
    jump CHAMBRE_TP

# ----------------------------------------------------------
# Interaction CHAMBRE 3 :
# ----------------------------------------------------------

label chambre3_brouilleur:
    jump CHAMBRE_BROUILLEUR

label chambre3_tablette:
    "Je touche la tablette du bout des doigts."
    "L'interface reste silencieuse."
    think "Elle sait tres bien quand elle veut parler."
    jump CHAMBRE_TP
