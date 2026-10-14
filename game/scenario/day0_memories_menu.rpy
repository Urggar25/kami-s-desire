# JOUR 0 / REMEMORATION - textures attendues dans game/images/ui/0/s2_menu/
# Aucun ancien nuage de pensee n'est utilise.
define D0_MEMORY_DIR = "images/ui/0/s2_menu/"

default d0_memory_newly_unlocked = []

init python:
    D0_MEMORY_ITEMS = (
        ("noam", "juliette", "JULIETTE", "Ce qui m'attend chez moi", .235, .275),
        ("kami", "kami", "KAMI", "Les Commandements", .765, .280),
        ("conclave", "conclave", "CONCLAVE", "L'annonce", .245, .705),
        ("lysa", "lysa", "UNE VOIX", "Un dernier souvenir", .770, .720),
    )
    def d0_memory_open(key):
        seen = renpy.store.d0_memories_seen
        return (key in ("noam", "kami") or
            (key == "conclave" and "noam" in seen and "kami" in seen) or
            (key == "lysa" and "conclave" in seen))

    def d0_memory_texture(name):
        # Evite une exception si les PNG ne sont pas encore synchronises sur GitHub.
        filename = D0_MEMORY_DIR + name + ".png"
        return filename if renpy.loadable(filename) else None

transform d0_memory_float(delay=0.0):
    subpixel True
    pause delay
    yoffset 0
    block:
        ease 3.8 yoffset -9
        ease 3.4 yoffset 8
        ease 3.8 yoffset 0
        repeat

transform d0_memory_hover:
    subpixel True
    on idle:
        ease 0.20 zoom 1.0
    on hover:
        ease 0.20 zoom 1.045

transform d0_memory_lock:
    alpha 0.22
    matrixcolor SaturationMatrix(0.15)

transform d0_memory_seen:
    alpha 0.66

# Images dessinees deja calibrees : utiliser tout le cadre, sans les
# reduire une seconde fois a la taille de l'ancien bouton nuage.
define D0_MEMORY_ART_W = 960
define D0_MEMORY_ART_H = 528

transform d0_memory_unlock_image:
    subpixel True
    alpha 0.0 zoom 0.70
    pause 0.30
    easeout 0.32 alpha 1.0 zoom 1.15
    easein 0.25 zoom 1.0

transform d0_memory_enter_fragment:
    subpixel True
    alpha 1.0 zoom 1.0
    easein 0.34 zoom 1.22
    easeout 0.56 zoom 2.15 alpha 0.0

transform d0_memory_particle_burst_left:
    subpixel True
    alpha 0.0 zoom 0.38 rotate -25 xoffset 0 yoffset 0
    pause 0.13
    parallel:
        ease 0.12 alpha 1.0
        pause 0.30
        easeout 0.50 alpha 0.0
    parallel:
        easeout 0.85 zoom 2.15 rotate -110 xoffset -360 yoffset -140

transform d0_memory_particle_burst_right:
    subpixel True
    alpha 0.0 zoom 0.35 rotate 18 xoffset 0 yoffset 0
    pause 0.21
    parallel:
        ease 0.10 alpha 0.95
        pause 0.30
        easeout 0.43 alpha 0.0
    parallel:
        easeout 0.84 zoom 2.35 rotate 125 xoffset 375 yoffset 160

transform d0_memory_particle_echo:
    subpixel True
    alpha 0.0 zoom 0.45
    pause 0.36
    parallel:
        ease 0.13 alpha 0.65
        easeout 0.48 alpha 0.0
    parallel:
        easeout 0.62 zoom 2.80 rotate -52

screen d0_memory_fragment(item, unlocked=True, selected=False):
    $ key, stem, title, subtitle, x, y = item
    $ filename = d0_memory_texture("d0_memory_" + stem)
    $ already = key in d0_memories_seen
    fixed:
        xcenter int(config.screen_width*x)
        ycenter int(config.screen_height*y)
        xsize 710
        ysize 370
        at d0_memory_float((0.1 if key == "kami" else 0.3) if key in ("kami", "lysa") else 0.0)
        button:
            xalign 0.5 yalign 0.5
            xsize 710 ysize 370
            padding (0, 0)
            background None
            hover_background None
            insensitive_background None
            at d0_memory_hover
            sensitive unlocked
            action Return(key)
            if filename:
                # PNG integral conserve : le dessin n'est plus miniaturise
                # dans un bouton 610x325 et retrouve sa place dans la fenetre.
                add Transform(filename, xysize=(D0_MEMORY_ART_W, D0_MEMORY_ART_H),
                    alpha=(0.70 if already else (1.0 if unlocked else 0.14)),
                    matrixcolor=(SaturationMatrix(1.0) if unlocked else SaturationMatrix(0.10))):
                    xalign 0.5 yalign 0.5
            else:
                add Solid("#20334699" if unlocked else "#121b26aa"):
                    xalign 0.5 yalign 0.5 xsize 600 ysize 285
            vbox:
                xalign 0.5 yalign 0.90
                spacing 5
                text title:
                    xalign 0.5 size 25 bold True
                    color ("#eaf4fa" if unlocked else "#71818f")
                    outlines [(2, "#08121bdc", 0, 1)]
                text ("SOUVENIR RETROUVÉ" if already else (subtitle if unlocked else "SOUVENIR ENFOUI")):
                    xalign 0.5 size 16
                    color ("#c1d7e3" if unlocked else "#627381")
                    outlines [(1, "#09121bdc", 0, 1)]

screen d0_memories():
    modal True
    zorder 220
    $ bg = d0_memory_texture("d0_memory_background")
    if bg:
        add bg xysize (config.screen_width, config.screen_height)
    else:
        add Solid("#050d19")
    for item in D0_MEMORY_ITEMS:
        use d0_memory_fragment(item, d0_memory_open(item[0]))
    text "REMÉMORATION" xalign 0.5 ypos 0.042 size 31 color "#bdd6e7" kerning 5
    text "Des souvenirs flottent à la surface de ma mémoire..." xalign 0.5 ypos 0.103 size 17 color "#879aaa"
    if "lysa" in d0_memories_seen:
        textbutton "REVENIR AU PRÉSENT":
            xalign 0.5 yalign 0.963
            text_size 23 text_color "#cbecfa" text_hover_color "#ffffff"
            action Return("done")
    else:
        text "CHOISISSEZ UN SOUVENIR" xalign 0.5 yalign 0.964 size 18 color "#a0b6c7"

# Transition commune aux chargements et deblocages. L'image est ancree
# sur la position exacte du souvenir choisi et non au centre de l'ecran.
screen d0_memory_transition(key, unlocking=False):
    modal True
    zorder 230
    $ item = next(i for i in D0_MEMORY_ITEMS if i[0] == key)
    $ _, stem, title, subtitle, xx, yy = item
    $ bg = d0_memory_texture("d0_memory_background")
    $ tex = d0_memory_texture("d0_memory_" + stem)
    $ particle1 = d0_memory_texture("d0_memory_particle1")
    $ particle2 = d0_memory_texture("d0_memory_particle2")
    if bg:
        add bg xysize (config.screen_width, config.screen_height)
    else:
        add Solid("#050d19")
    add Solid("#01050a99")
    # L'arriere-plan ne bouge pas : la camera se concentre sur le souvenir.
    fixed:
        xcenter int(config.screen_width*xx)
        ycenter int(config.screen_height*yy)
        xsize 710 ysize 370
        if tex:
            add tex:
                xysize (D0_MEMORY_ART_W, D0_MEMORY_ART_H)
                xalign 0.5 yalign 0.5
                at (d0_memory_unlock_image if unlocking else d0_memory_enter_fragment)
        if particle1:
            add particle1:
                xysize (D0_MEMORY_ART_W, D0_MEMORY_ART_H)
                xalign 0.5 yalign 0.5
                at d0_memory_particle_burst_left
        if particle2:
            add particle2:
                xysize (D0_MEMORY_ART_W, D0_MEMORY_ART_H)
                xalign 0.5 yalign 0.5
                at d0_memory_particle_burst_right
        if particle1:
            add particle1:
                xysize (D0_MEMORY_ART_W, D0_MEMORY_ART_H)
                xalign 0.5 yalign 0.5
                at d0_memory_particle_echo
    if unlocking:
        text "SOUVENIR RETROUVÉ" xalign 0.5 yalign 0.915 size 24 color "#d7e6ee"
    timer (1.58 if unlocking else 1.43) action Return()

label d0_memory_open_transition(key):
    call screen d0_memory_transition(key, False)
    return

label d0_memory_unlock_transition(key):
    call screen d0_memory_transition(key, True)
    return
