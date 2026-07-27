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
    call PLAY_DOOR_OPEN(door_room_background("dortoir"))
    jump DORTOIR_TP

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
