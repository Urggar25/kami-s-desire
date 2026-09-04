## Ce fichier contient les options qui peuvent être modifiées pour personnaliser
## votre jeu.
##
## Les lignes qui commencent avec deux dièses '#' sont des commentaires et vous
## ne devriez pas les décommenter. Les lignes qui commencent avec un seul dièse
## sont du code commenté et vous pouvez les décommentez quand c’est approprié
## (pour votre projet).


## Bases #######################################################################

## Un nom de jeu intelligible. Il est utilisé pour personnaliser le titre de la
## fenêtre par défaut et s’affiche dans l’interface ainsi que dans les rapports
## d’erreur.
##
## La chaîne de caractère contenu dans _() est éligible à la traduction.

define config.name = _("Kami's Desires")


## Polices de repli pour le chinois ###########################################

## Les polices d'origine couvrent correctement les langues latines, mais pas
## les idéogrammes. Source Han est donc activée uniquement en chinois.
## On utilise uniquement des chemins de police ordinaires, car Ren'Py 8.3 ne
## prend pas en charge FontGroup dans config.font_replacement_map.

define kd_cjk_font = "fonts/SourceHanSansLite.ttf"

init -100 python:
    _kd_cjk_replaced_fonts = (
        "fonts/Barlow-Light.ttf",
        "fonts/Rajdhani-SemiBold.ttf",
        "fonts/day_font.ttf",
    )

    def kd_update_language_fonts():
        use_cjk_font = preferences.language == "chinese"

        for original_font in _kd_cjk_replaced_fonts:
            for is_bold in (False, True):
                for is_italic in (False, True):
                    replacement_key = (original_font, is_bold, is_italic)
                    if use_cjk_font:
                        config.font_replacement_map[replacement_key] = ("fonts/SourceHanSansLite.ttf", is_bold, is_italic)
                    else:
                        config.font_replacement_map.pop(replacement_key, None)

    kd_update_language_fonts()
    config.change_language_callbacks.append(kd_update_language_fonts)

    def kd_tr(value):
        """Translate UI values that come from Python data instead of literals."""
        if value is None:
            return ""
        if not isinstance(value, str):
            value = str(value)
        translated = renpy.translate_string(value)
        return translated if translated else value


## Détermine si le titre renseigné plus haut est affiché sur l'écran du menu
## principal Configurez-le à False (Faux) pour cacher le titre.

define gui.show_name = True


## La version du jeu.

define config.version = "4.0.1"


## Texte placé sur l'écran "À propos" du jeu. Placez le texte entre triples
## guillemets, et laissez une ligne entre les paragraphes.

define gui.about = _p("""
Visual novel de tension, de votes et de survie sociale dans le Conclave orbital.

Version de développement. Les choix, les arguments et les liens de personnage peuvent encore évoluer.
""")


## Un nom court pour le jeu qui sera utilisé pour les répertoires et le nom de
## l’exécutable. Il ne doit contenir que des caractères ASCII et ne doit pas
## contenir d’espace, de virgules ou de points-virgules.

define build.name = "kamidesire"


## Sons et musiques ############################################################

## Ces trois variables contrôlent, entre autres, quels mixeurs sont affichés
## au joueur par défaut. Configurer l’un de ceux-ci à False (Faux) cachera le
## mixeur concerné.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Pour autoriser le joueur à réaliser un test de volume, décommenter la ligne
## ci-dessous et utilisez-la pour configurer un son d’exemple.

define config.sample_sound = "audio/sfx_kami_alert.wav"
# define config.sample_voice = "sample-voice.ogg"


## Décommentez la ligne suivante pour configurer un fichier audio qui sera
## diffusé quand le joueur sera sur le menu principal. Ce son se poursuivra dans
## le jeu, jusqu’à ce qu'il soit stoppé ou qu’un autre fichier soit joué.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## Ces variables configurent les transitions qui sont utilisées quand certains
## événements surviennent. Chaque variable peuvent être configurée pour une
## transition. La valeur None indique qu’aucune transition ne doit être
## utilisée.

## À l’entrée ou à la sortie du menu du jeu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre les écrans du menu du jeu.

define config.intra_transition = dissolve


## La transition qui sera utilisée après le chargement d’une partie.

define config.after_load_transition = None


## La transition qui sera utilisé après la fin du jeu.

define config.end_game_transition = None


## Il n’y a pas de variable pour configurer la transition en début de partie. À
## la place, utilisez un état de transition juste après l’affichage de la toute
## première scène.


## Gestion des fenêtres ########################################################
##
## Cela contrôle l’affichage de la fenêtre de dialogue. Si « show », elle est
## toujours affichée. Si « hide », elle ne s’affiche que lorsque du dialogue est
## présent. Si « auto », La fenêtre est cachée avant chaque changement de scène
## et réapparait une fois le dialogue affiché.
##
## Après le début de la partie, cela peut-être changé avec les instructions
## « window show », « window hide » et « window auto ».

define config.window = "auto"


## Transitions utilisées pour afficher ou cacher la fenêtre de dialogue

define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

## Remappage audio : corrige les chemins "music/x.mp3" -> "audio/music/x.mp3"
## (de nombreux scripts pointent vers music/ et sfx/ alors que les fichiers
## sont sous audio/ ; Ren'Py ignorait silencieusement ces fichiers manquants)
init python:
    ## Pistes référencées dans le scénario mais jamais composées :
    ## on les remappe vers la piste existante la plus proche en ambiance.
    ## Remplace ces alias par de vraies pistes quand elles existeront.
    _KD_MUSIC_ALIASES = {
        "bgm_victory_bitter.mp3":        "bgm_calm_not_peace.mp3",
        "bgm_romantic_atmosphere.mp3":   "bgm_introspective_atmosphere.mp3",
        "bgm_calm_sad.mp3":              "bgm_introspective_atmosphere.mp3",
        "bgm_debate_low.mp3":            "bgm_world_decline.mp3",
        "bgm_quiet_tension.mp3":         "bgm_world_decline.mp3",
        "bgm_tension_low.mp3":           "bgm_world_decline.mp3",
        "bgm_tension_phase3.mp3":        "bgm_fatal_assembly.mp3",
        "bgm_stabilisation_tension.mp3": "bgm_world_decline.mp3",
        "bgm_tension_debate.mp3": "bgm_fatal_assembly.mp3",
    }

    def _kd_audio_filename_fix(fn):
        if renpy.loadable(fn):
            return fn
        alt = "audio/" + fn
        if renpy.loadable(alt):
            return alt
        base = fn.rsplit("/", 1)[-1]
        if base in _KD_MUSIC_ALIASES:
            alias = "audio/music/" + _KD_MUSIC_ALIASES[base]
            if renpy.loadable(alias):
                return alias
        return fn
    config.audio_filename_callback = _kd_audio_filename_fix


## Préférences par défaut ######################################################

## Contrôle la vitesse du texte. La valeur par défaut, 0, est infinie. Toute
## autre valeur est le nombre de caractères tapés par seconde.

default preferences.text_cps = 0


## Le délai d’avancée automatique. Des nombres importants entraînent une longue
## attente. Des valeurs réputées correctes sont comprises dans une plage allant
## de 0 à 30.

default preferences.afm_time = 15


## Répertoire de sauvegarde ####################################################
##
## Ces valeurs, dépendant de la plateforme, déterminent l’emplacement où Ren’Py
## stockera les fichiers de sauvegarde. Les fichiers de sauvegardes seront
## stockés dans :
##
## Windows : %APPDATA\RenPy\<config.save_directory>
##
## Macintosh : $HOME/Library/RenPy/<config.save_directory>
##
## Linux : $HOME/.renpy/<config.save_directory>
##
## Cela ne devrait généralement pas changer. Si vous le faîtes, choisissez
## toujours une chaîne de caractères littéraux, pas une expression.

define config.save_directory = "kamidesire-1766833117"


## Icône #######################################################################
##
## L'icone affichée dans la barre des tâches ou sur le dock.

define config.window_icon = "gui/window_icon.png"


## Désactive le rollback et le rollforward via molette / raccourcis afin
## d'éviter les retours accidentels dans le texte, les choix et les écrans.
init python:
    config.keymap["rollback"] = []
    config.keymap["rollforward"] = []
    config.keymap["game_menu"] = ["K_ESCAPE", "mouseup_3"]


## Configuration de la compilation #############################################
##
## Cette section paramètre la façon dont Ren’Py transforme votre projet en
## fichier à distribuer.

init python:

    ## Les fonctions suivantes prennent en paramètres un format de fichier. Les
    ## formats de fichiers ne sont pas sensibles à la casse et correspondent au
    ## répertoire relatif au répertoire de base. Il n’y a pas de / à la fin. Si
    ## plusieurs formats correspondent, le premier est utilisé.
    ##
    ## Dans le format :
    ##
    ## / est le séparateur de répertoire.
    ##
    ## * correspond à tous les caractères à l’exception du séparateur de
    ##   répertoire.
    ##
    ## ** correspond à tous les caractères, y compris le séparateur de
    ##    répertoire.
    ##
    ## Par exemple, "*.txt" correspond à tous les fichiers txt dans le
    ## répertoire de base, "game/**.ogg" correspond à tous les fichiers ogg
    ## dans le répertoire game, mais aussi à tous ses répertoires. "**.psd"
    ## correspond à tous les fichiers psd quelque soit leur emplacement dans
    ## l’arborescence du fichier.

    ## Choisissez la valeur « None » pour les exclure de la distribution.

    # Ressources de travail uniquement : ne jamais les inclure dans les builds.
    build.classify('.development_pack/**', None)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    build.archive("script", "all")
    build.archive("image", "all")
    build.archive("video", "all")
    build.archive("audio", "all")
    
    ## Pour archiver les fichiers, choisissez la valeur « archive ».
    
    build.classify('game/**.png', 'image')
    build.classify('game/**.jpg', 'image')

    build.classify('game/**.rpy', 'script')
    build.classify('game/**.rpyc', 'script')
    
    build.classify('game/**.mp4', 'video')
    build.classify('game/**.avi', 'video')
    build.classify('game/**.webm', 'video')
    
    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.wav', 'audio')

    ## Les fichiers correspondant au format de documentation sont dupliqués pour
    ## les compilation sur Mac, c'est pourquoi ils apparaissent deux fois dans
    ## l’archive zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Une clé de licence Google Play est requise pour permettre les achats depuis
## l'application. Vous pourrez la trouver dans la console de développement
## Google Play, sous "Monétiser" > "Configuration de la monétisation" >
## "Licences".

# define build.google_play_key = "..."


## Le nom d’utilisateur et du projet associé au projet itch.io, séparé par un
## slash.

define build.itch_project = "lijo62/kamis-desires"

init python:
    import time
    import logging
    import os

    # Création du dossier log et du fichier
    log_dir = os.path.join(config.basedir, "log")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "cinema_debug.log")

    # Configuration du logging fichier
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        datefmt="%H:%M:%S",
        filemode="w"  # Écrase le fichier à chaque lancement
    )

    # Fonction log SÛRE (pas de récursion !)
    def log(msg):
        full_msg = f"{msg}"
        renpy.log(full_msg)           # Visible dans console Shift+O
        logging.info(full_msg)        # Écrit dans le fichier
        print(full_msg)               # Visible si lancé en ligne de commande

define config.empty_window = lambda : None
