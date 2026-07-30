# =============================================================================
# MINIJEU NARRATIF — "Le brouillon de Noam" (amendement_brouillon)
#
# Noam, seul face à sa feuille, incapable de figer sa première formulation.
# Aucun choix politique, aucun score, aucune "bonne réponse".
# Objectif ressenti : hésitation, isolement, autosabotage.
#
# Boucle : assembler des fragments manuscrits en glisser-déposer -> Noam relit
# -> un mot le fait douter -> il le gomme (trace grise persistante) -> un nouveau
# fragment apparaît -> on recommence, la feuille se salit, la salle se vide.
# La réussite finale n'est PAS la phrase parfaite : c'est CESSER de l'effacer.
#
# Architecture réutilisable (tout est en data, voir AMEND_STEPS) :
#   - fragments par étape + positions + rotations
#   - pensées déclenchées après chaque formulation
#   - mot à effacer par étape
#   - progression de l'ambiance sonore (AMB_VOL)
#   - états visuels de la feuille (usure / ratures cumulées)
#   - variable de fin : j1_amend_minigame_done
#   - saut dev rapide : amend_dev_skip
#
# Point d'entrée : call amendement_brouillon_play
# Assets : game/minijeu/amend_assets/*
# =============================================================================

image amend_desk       = "minijeu/amend_assets/amend_desk.png"
image amend_sheet_img  = "minijeu/amend_assets/amend_sheet.png"
image amend_room_wide  = "minijeu/amend_assets/amend_room_wide.png"
image amend_shadow     = "minijeu/amend_assets/amend_shadow.png"

default j1_amend_minigame_done = False
default amend_dev_skip = False          # $ amend_dev_skip = True en console pour zapper
default amend_st = None

init python:
    import random as _amrand

    AMEND_DIR   = "minijeu/amend_assets/"
    AMEND_FONT  = "fonts/day_font.ttf"
    AMEND_SNAP_R = 150                    # rayon d'aimantation d'un fragment
    AMB_VOL = [1.0, 0.78, 0.55, 0.32, 0.12, 0.0]

    # -- Mise en page (la feuille est réduite en haut, plateau de fragments en bas)
    SHEET_ZOOM = 0.70
    SHEET_X    = 540                       # source 1200 * 0.70 = 840 -> centré
    SHEET_Y    = 24
    # zone d'écriture (coords écran, par-dessus la feuille affichée)
    WRITE_X0, WRITE_X1 = 620, 1300
    WRITE_Y0           = 120
    # plateau des fragments (garanti à l'écran)
    TRAY_X0, TRAY_X1 = 90, 1830
    TRAY_Y0          = 700
    TRAY_ROW_H       = 116

    SFX_PLACE   = AMEND_DIR + "amend_place.ogg"
    SFX_RUB     = AMEND_DIR + "amend_eraser_rub.ogg"
    SFX_CRUMPLE = AMEND_DIR + "amend_paper_crumple.ogg"

    # -- Données des étapes ---------------------------------------------------
    # tokens  : la phrase complète de l'étape, découpée en fragments
    # new     : indices des fragments à (re)poser ce tour (les autres sont verrouillés)
    # erase   : indice du fragment que Noam finira par gommer (None = étape finale)
    # reread  : pensées après assemblage (Noam relit et doute)
    # after   : pensées après effacement
    # parasites : fragments parasites (glissent hors de la phrase si posés)
    AMEND_STEPS = [
        {
            "tokens": ["Toute personne", "doit", "intervenir",
                       "lorsqu'une autre personne", "est en danger."],
            "new": [0, 1, 2, 3, 4],
            "erase": 1,
            "reread": [
                "« Toute personne doit intervenir lorsqu'une autre personne est en danger. »",
                "Doit. Une obligation. Je force la main de tout le monde, d'un seul mot.",
                "Et si quelqu'un intervient mal ? Si à cause de « doit », on condamne celui qui a hésité ?",
                "Non. « Doit », c'est trop. Ça punit autant que ça protège.",
            ],
            "after": ["Le mot part. La trace, elle, reste."],
            "parasites": [
                {"token": "immédiatement", "thought": "« Immédiatement »... et si c'est trop tard pour bien faire ? Je le retire."},
            ],
        },
        {
            "tokens": ["Toute personne", "peut", "intervenir",
                       "lorsqu'une autre personne", "est en danger."],
            "new": [1],
            "erase": 2,
            "reread": [
                "« ...peut intervenir... »",
                "Intervenir. Ça sonne comme se jeter dans le feu. Comme un héros.",
                "Personne n'est un héros, ici. On lira ça comme le droit de tout casser au nom du secours.",
            ],
            "after": ["Encore un mot rayé. La phrase respire un peu moins fort."],
            "parasites": [
                {"token": "s'il l'ose", "thought": "« S'il l'ose »... je ne vais pas leur demander du courage en plus. Non."},
            ],
        },
        {
            "tokens": ["Toute personne", "peut", "porter assistance",
                       "lorsqu'une autre personne", "est en danger."],
            "new": [2],
            "erase": 3,
            "reread": [
                "« ...peut porter assistance lorsqu'une autre personne est en danger. »",
                "« Lorsque ». Comme s'il fallait attendre le bon moment. Attendre l'autorisation du danger lui-même.",
                "J'ajoute « après autorisation », machinalement. Ma main écrit ce que la peur dicte.",
                "...Non. Si on attend l'autorisation, la personne est déjà par terre. Je barre ça aussi.",
                "Trop de conditions. Chaque condition est une porte pour dire non.",
            ],
            "after": ["Je gomme la condition. Mes doigts sont gris."],
            "parasites": [
                {"token": "après autorisation", "thought": "« Après autorisation ». Voilà. C'est exactement le mot qui tue les gens poliment. Dehors."},
                {"token": "si nécessaire", "thought": "« Si nécessaire », qui décide de ça ? Pas moi. Je l'écarte."},
            ],
        },
        {
            "tokens": ["Toute personne", "peut", "porter assistance",
                       "à une autre personne", "est en danger."],
            "new": [3],
            "erase": 4,
            "reread": [
                "« ...porter assistance à une autre personne est en danger. »",
                "Ça se lit de travers, maintenant. Tant pis, personne ne relira ma calligraphie.",
                "« Est en danger. » Lourd. Je veux juste : en danger. Court. Qu'on ne puisse pas l'esquiver.",
            ],
            "after": ["La feuille est presque illisible. Moi aussi."],
            "parasites": [
                {"token": "quand c'est permis", "thought": "« Quand c'est permis »... et si ça ne l'est jamais ? Je raye."},
                {"token": "peut-être", "thought": "« Peut-être ». Le mot le plus lâche que je connaisse. Dehors."},
            ],
        },
        {
            "tokens": ["Toute personne", "peut", "porter assistance",
                       "à une autre personne", "en danger", "sans autorisation préalable."],
            "new": [4, 5],
            "erase": None,
            "reread": [
                "« Toute personne peut porter assistance à une autre personne en danger sans autorisation préalable. »",
                "Voilà. C'est laid. C'est raturé. Mais ça tient debout.",
            ],
            "after": [],
            "parasites": [
                {"token": "dans la limite", "thought": "« Dans la limite »... la limite de quoi ? Non."},
                {"token": "sauf refus", "thought": "« Sauf refus ». Toujours une porte de sortie. Je n'en veux plus."},
                {"token": "si toléré", "thought": "« Si toléré ». Non. Plus de permission à mendier."},
            ],
        },
    ]

    # -- État du minijeu ------------------------------------------------------
    class AmendState(object):
        def __init__(self):
            self.step = 0
            self.slots = []
            self.loose = []
            self.required = []
            self.marks = []              # ratures / traces cumulées (persistantes)
            self.wear = 0                # niveau de froissement 0..3
            self.eraser_mode = None      # None | "erase" | "hold"
            self.erase_slot = None
            self.erase_progress = 0.0
            self.eraser_xy = (1300, 820)
            self.eraser_prev = None
            self.final_touch = False

        @staticmethod
        def _frag_w(tok, size):
            return int(len(tok) * size * 0.50) + 44

        # --- dispose les fragments libres dans le plateau du bas (flow wrap) ---
        def _layout_tray(self, loose, rnd):
            cx = TRAY_X0
            cy = TRAY_Y0
            for fr in loose:
                w = fr["w"]
                if cx + w > TRAY_X1:
                    cx = TRAY_X0
                    cy += TRAY_ROW_H
                fr["x"] = int(cx + rnd.randint(-4, 4))
                fr["y"] = int(cy + rnd.randint(-6, 6))
                cx += w + 34

        def build_step(self, i):
            self.step = i
            step = AMEND_STEPS[i]
            tokens = step["tokens"]
            new = set(step["new"])
            level = i
            rnd = _amrand.Random(1000 + i)

            # --- disposition de la phrase sur la feuille (flow wrap) ---
            y = WRITE_Y0 + rnd.randint(-4, 4)
            line_h = 90 - level * 3
            cur_x = WRITE_X0
            slots = []
            for idx, tok in enumerate(tokens):
                size = 30
                if level >= 2:
                    size = rnd.choice([26, 28, 30, 32])
                w = self._frag_w(tok, size)
                h = size + 26
                if cur_x + w > WRITE_X1:
                    cur_x = WRITE_X0
                    y += line_h
                cx = cur_x + w / 2.0 + rnd.randint(-level * 2, level * 2)
                cy = y + h / 2.0 + rnd.randint(-level * 2, level * 2)
                rot = 0.0
                if level >= 1:
                    rot = rnd.uniform(-1.5 - level, 1.5 + level)
                slots.append({
                    "i": idx, "token": tok, "cx": cx, "cy": cy,
                    "w": w, "h": h, "size": size, "rot": rot,
                    "filled": idx not in new,
                })
                cur_x += w + 22
            self.slots = slots
            self.required = list(step["new"])

            # --- fragments libres (corrects + parasites), placés dans le plateau ---
            loose = []
            for idx in step["new"]:
                s = slots[idx]
                loose.append({
                    "id": "f%d" % idx, "token": s["token"], "x": 0, "y": 0,
                    "w": s["w"], "h": s["h"], "size": s["size"],
                    "target": idx, "is_parasite": False, "thought": None,
                })
            for pi, par in enumerate(step.get("parasites", [])):
                tok = par["token"]
                loose.append({
                    "id": "p%d" % pi, "token": tok, "x": 0, "y": 0,
                    "w": self._frag_w(tok, 30), "h": 56, "size": 30,
                    "target": None, "is_parasite": True, "thought": par["thought"],
                })
            rnd.shuffle(loose)
            self._layout_tray(loose, rnd)
            self.loose = loose
            self.eraser_mode = None
            self.erase_slot = None

        def get_loose(self, fid):
            for f in self.loose:
                if f["id"] == fid:
                    return f
            return None

        def place_fragment(self, fid):
            fr = self.get_loose(fid)
            if fr is None:
                return
            self.slots[fr["target"]]["filled"] = True
            self.loose.remove(fr)

        def pop_parasite(self, pid):
            fr = self.get_loose(pid)
            if fr is None:
                return None
            self.loose.remove(fr)
            return fr["thought"]

        def is_complete(self):
            return all(self.slots[k]["filled"] for k in self.required)

        # --- effacement -----------------------------------------------------
        def begin_erase(self, idx):
            self.eraser_mode = "erase"
            self.erase_slot = idx
            self.erase_progress = 0.0
            self.eraser_prev = None
            s = self.slots[idx]
            self.eraser_xy = (int(s["cx"] + s["w"] * 0.5 + 130), int(s["cy"] - 45))

        def add_partial_smudge(self, cx, cy):
            if len(self.marks) > 60:
                return
            self.marks.append({
                "type": "smudge", "x": cx, "y": cy,
                "z": 0.35, "rot": _amrand.uniform(-14, 14), "a": 0.4,
            })

        def finalize_erase(self):
            s = self.slots[self.erase_slot]
            self.marks.append({
                "type": "smudge", "x": s["cx"], "y": s["cy"],
                "z": (s["w"] + 40) / 240.0, "rot": _amrand.uniform(-8, 8), "a": 0.85,
            })
            self.marks.append({
                "type": "strike", "x": s["cx"], "y": s["cy"],
                "z": (s["w"] + 30) / 300.0, "rot": _amrand.uniform(-6, 6), "a": 0.9,
            })
            s["filled"] = False
            self.wear = min(3, self.wear + 1)
            self.eraser_mode = None
            self.erase_slot = None

        def begin_hold(self):
            self.eraser_mode = "hold"
            self.final_touch = False
            self.eraser_xy = (1330, 840)
            self.eraser_prev = None

    # -- helpers géométrie ---------------------------------------------------
    def amend_overlap(cx, cy, slot, margin=48):
        return (abs(cx - slot["cx"]) <= slot["w"] / 2.0 + margin and
                abs(cy - slot["cy"]) <= slot["h"] / 2.0 + margin)

    def amend_over_any(cx, cy):
        st = store.amend_st
        for s in st.slots:
            if s["filled"] and amend_overlap(cx, cy, s, margin=40):
                return True
        return False

    # -- callbacks Drag ------------------------------------------------------
    def amend_frag_dropped(drags, drop):
        st = store.amend_st
        d = drags[0]
        fr = st.get_loose(d.drag_name)
        if fr is None:
            return
        w = d.w if d.w else fr["w"]
        h = d.h if d.h else fr["h"]
        cx = d.x + w / 2.0
        cy = d.y + h / 2.0
        if fr["is_parasite"]:
            renpy.play(SFX_PLACE, channel="sound")
            return "parasite:" + fr["id"]
        slot = st.slots[fr["target"]]
        dist = ((cx - slot["cx"]) ** 2 + (cy - slot["cy"]) ** 2) ** 0.5
        if (not slot["filled"]) and dist <= AMEND_SNAP_R:
            st.place_fragment(fr["id"])
            renpy.play(SFX_PLACE, channel="sound")
            if st.is_complete():
                return "complete"
            renpy.restart_interaction()
            return
        d.snap(fr["x"], fr["y"], 0.25)
        renpy.restart_interaction()
        return

    def amend_eraser_dropped(drags, drop):
        st = store.amend_st
        d = drags[0]
        cx = d.x + 95
        cy = d.y + 65
        st.eraser_xy = (int(d.x), int(d.y))
        if st.eraser_mode == "erase":
            slot = st.slots[st.erase_slot]
            over = amend_overlap(cx, cy, slot)
            dist = 0.0
            if st.eraser_prev is not None:
                dist = ((cx - st.eraser_prev[0]) ** 2 + (cy - st.eraser_prev[1]) ** 2) ** 0.5
            st.eraser_prev = (cx, cy)
            if over and dist > 12:
                st.erase_progress = min(1.0, st.erase_progress + 0.20 + min(0.28, dist / 1200.0))
                renpy.play(SFX_RUB, channel="sound")
                st.add_partial_smudge(cx + _amrand.uniform(-20, 20), cy + _amrand.uniform(-12, 12))
                if st.erase_progress >= 1.0:
                    st.finalize_erase()
                    renpy.play(SFX_CRUMPLE, channel="sound")
                    return "erased"
            renpy.restart_interaction()
            return
        else:  # hold
            if amend_over_any(cx, cy):
                st.final_touch = True
                renpy.play(SFX_PLACE, channel="sound")
            renpy.restart_interaction()
            return

    # canal ambiance dédié (mixer sfx pour suivre le volume options)
    try:
        renpy.music.register_channel("amend_amb", mixer="sfx", loop=True)
    except Exception:
        pass


# =============================================================================
# TRANSFORMS
# =============================================================================
transform amend_locked_rot(r):
    rotate r

transform amend_wobble:
    subpixel True
    block:
        ease 1.3 xoffset 2 yoffset -1
        ease 1.6 xoffset -2 yoffset 1
        repeat

transform amend_nervous:
    subpixel True
    block:
        ease 0.10 rotate -3 xoffset -2
        ease 0.10 rotate 3 xoffset 2
        repeat

transform amend_frag_float(seed=0):
    subpixel True
    pause seed
    block:
        ease 1.8 yoffset -3
        ease 1.8 yoffset 3
        repeat

transform amend_shadow_pass:
    xpos -400 ypos 0 alpha 0.0
    linear 0.4 alpha 0.9
    linear 1.6 xpos 1600
    linear 0.3 alpha 0.0

transform amend_dezoom:
    zoom 2.0 yoffset 300
    easein 3.4 zoom 1.0 yoffset 0

transform amend_fade_in:
    alpha 0.0
    easein 0.6 alpha 1.0


# =============================================================================
# SCREEN — plateau d'affichage (persistant, non interactif)
# =============================================================================
screen amend_board():
    zorder 40

    add "amend_desk"
    add "amend_sheet_img" xpos SHEET_X ypos SHEET_Y zoom SHEET_ZOOM
    if amend_st.wear >= 1:
        add (AMEND_DIR + "amend_wrinkle%d.png" % min(3, amend_st.wear)) xpos SHEET_X ypos SHEET_Y zoom SHEET_ZOOM

    # ratures / traces cumulées
    for m in amend_st.marks:
        if m["type"] == "smudge":
            add (AMEND_DIR + "amend_smudge.png"):
                xpos int(m["x"]) ypos int(m["y"]) xanchor 0.5 yanchor 0.5
                zoom m["z"] rotate m["rot"] alpha m["a"]
        else:
            add (AMEND_DIR + "amend_strike.png"):
                xpos int(m["x"]) ypos int(m["y"]) xanchor 0.5 yanchor 0.5
                zoom m["z"] rotate m["rot"] alpha m["a"]

    # fragments verrouillés (statiques, écriture manuscrite)
    for s in amend_st.slots:
        if s["filled"]:
            $ _al = 1.0

            if amend_st.eraser_mode == "erase" and s["i"] == amend_st.erase_slot:
                $ _al = max(0.0, 1.0 - amend_st.erase_progress)

            frame:
                xpos int(s["cx"])
                ypos int(s["cy"])
                xanchor 0.5
                yanchor 0.5

                if amend_st.wear >= 2:
                    at [amend_locked_rot(s["rot"]), amend_wobble]
                else:
                    at amend_locked_rot(s["rot"])

                background Frame(
                    AMEND_DIR + "amend_note_locked.png",
                    30,
                    20
                )
                padding (16, 10)

                text s["token"]:
                    font AMEND_FONT
                    size s["size"]
                    color "#20202e"
                    at Transform(alpha=_al)

    # emplacements vides (guides visibles) pendant l'assemblage
    for s in amend_st.slots:
        if not s["filled"]:
            fixed:
                xpos int(s["cx"])
                ypos int(s["cy"])
                xanchor 0.5
                yanchor 0.5
                xsize int(s["w"])
                ysize int(s["h"])
                add Solid("#5a472a2e")
                add Solid("#8a7450") ysize 3 yalign 1.0

    # surbrillance nerveuse du mot à effacer
    if amend_st.eraser_mode == "erase" and amend_st.erase_slot is not None:
        $ _es = amend_st.slots[amend_st.erase_slot]
        add (AMEND_DIR + "amend_circle.png"):
            xpos int(_es["cx"]) ypos int(_es["cy"]) xanchor 0.5 yanchor 0.5
            zoom (_es["w"] + 70) / 340.0 alpha 0.9
            at amend_nervous


# =============================================================================
# SCREEN — couche interactive (drag)
# =============================================================================
screen amend_input(mode):
    modal True
    zorder 60

    if mode == "assemble":
        draggroup:
            for _i, fr in enumerate(amend_st.loose):
                drag:
                    drag_name fr["id"]
                    draggable True
                    droppable False
                    xpos fr["x"] ypos fr["y"]
                    dragged amend_frag_dropped
                    frame:
                        background Frame(AMEND_DIR + "amend_note.png", 30, 20)
                        padding (16, 10)
                        text fr["token"]:
                            font AMEND_FONT size fr["size"]
                            color ("#5a2333" if fr["is_parasite"] else "#2a2333")
    else:
        draggroup:
            drag:
                drag_name "eraser"
                draggable (mode == "erase") or (not amend_st.final_touch)
                droppable False
                xpos amend_st.eraser_xy[0] ypos amend_st.eraser_xy[1]
                dragged amend_eraser_dropped
                add (AMEND_DIR + "amend_eraser.png")

    if mode == "hold":
        if amend_st.final_touch:
            timer 2.2 action Return("stop")
        timer 16.0 action Return("stop")

    # --- saut dev (F10) : ne s'affiche qu'en mode développeur
    if config.developer:
        key "K_F10" action Return("complete" if mode == "assemble" else ("erased" if mode == "erase" else "stop"))


# =============================================================================
# LABEL — déroulé du minijeu
# =============================================================================
label amendement_brouillon_play:

    # --- saut développeur complet ---
    if amend_dev_skip:
        $ noam_amendement_choix = "assistance_minimale"
        $ j1_amendment_validated = True
        $ j1_amend_minigame_done = True
        return

    stop music fadeout 1.5
    hide screen day1_amendment_timer
    scene black with dissolve
    $ amend_st = AmendState()
    $ amend_st.build_step(0)

    # ambiance de départ : Conclave encore peuplé
    $ renpy.music.play(AMEND_DIR + "amend_ambience.ogg", channel="amend_amb", loop=True, fadein=1.0)
    $ renpy.music.set_volume(AMB_VOL[0], 0.0, channel="amend_amb")

    show screen amend_board
    with Dissolve(0.8)

    think "Alors. Ma phrase. Une seule ligne, et qu'on n'en parle plus."
    think "Les mots sont là, éparpillés autour. {i}(Fais-les glisser sur la feuille pour former une phrase.){/i}"

    $ _amend_i = 0
    while _amend_i < len(AMEND_STEPS):
        $ _step = AMEND_STEPS[_amend_i]

        # annonce de l'urne à l'avant-dernière étape
        if _amend_i == len(AMEND_STEPS) - 1:
            play sound "audio/sfx_announce.mp3"
            voix "Une minute avant fermeture de l'urne."
            think "Déjà ? Mes mains vont plus lentement que cette horloge."

        # ---- ASSEMBLAGE (boucle pour gérer les parasites) ----
        $ _assembling = True
        while _assembling:
            call screen amend_input("assemble")
            if _return and str(_return).startswith("parasite:"):
                $ _pid = str(_return).split(":", 1)[1]
                $ _pth = amend_st.pop_parasite(_pid)
                if _pth:
                    think "[_pth]"
            else:
                $ _assembling = False

        # ---- RELECTURE (Noam doute) ----
        $ _idx = 0
        while _idx < len(_step["reread"]):
            $ _line = _step["reread"][_idx]
            think "[_line]"
            $ _idx += 1

        if _step["erase"] is not None:
            # ---- EFFACEMENT ----
            $ amend_st.begin_erase(_step["erase"])
            if _amend_i == 0:
                think "Ma main cherche la gomme toute seule. {i}(Attrape-la, frotte le mot cerclé jusqu'à ce qu'il disparaisse.){/i}"
            play sound "audio/sfx_paper.mp3"
            call screen amend_input("erase")

            $ _idx = 0
            while _idx < len(_step["after"]):
                $ _line = _step["after"][_idx]
                think "[_line]"
                $ _idx += 1

            # ---- TRANSITION : un représentant termine et quitte la salle ----
            call amend_env_step from _call_amend_env_step
            $ amend_st.build_step(_amend_i + 1)
            $ _amend_i += 1

        else:
            # ---- ÉTAPE FINALE : ne plus effacer ----
            $ _idx = 0
            while _idx < len(_step["after"]):
                $ _line = _step["after"][_idx]
                think "[_line]"
                $ _idx += 1

            $ amend_st.begin_hold()
            think "Je pourrais encore. Enlever « sans autorisation ». Trouver plus doux, plus prudent."
            think "Continuer jusqu'à ce que la phrase ne veuille plus rien dire. Jusqu'à ce qu'elle ne gêne plus personne."
            think "La gomme est déjà dans ma main."

            call screen amend_input("hold")

            if amend_st.final_touch:
                play sound "audio/sfx_breath.mp3"
                pause 0.8
                think "..."
                think "Non."
                think "Je pose la gomme."
                think "Pour une fois, je n'efface pas."
            else:
                think "Je repose la gomme sans m'en servir."
                think "Pour une fois, je n'efface pas."

            $ _amend_i += 1

    # =========================================================================
    # FIN : plier la feuille, dézoom sur la salle vide
    # =========================================================================
    $ renpy.music.stop(channel="amend_amb", fadeout=2.0)
    hide screen amend_input

    play sound "minijeu/amend_assets/amend_fold.ogg"
    pause 0.7
    think "Je plie la feuille en deux. De travers, évidemment."

    hide screen amend_board
    scene black with dissolve
    show amend_room_wide at amend_dezoom
    with Dissolve(0.8)
    pause 1.4

    think "Les chaises sont vides. Toutes."
    think "Je n'ai même pas entendu la dernière partir."
    think "Le dernier au Conclave. Encore une fois."
    pause 1.6

    # --- variables de sortie (compatibilité scénario) ---
    $ noam_amendement_choix = "assistance_minimale"
    $ j1_amendment_validated = True
    $ j1_amend_minigame_done = True

    return


# --- Sous-routine : la salle se vide un peu plus à chaque réécriture ----------
label amend_env_step:
    $ _lvl = min(amend_st.step + 1, len(AMB_VOL) - 1)
    $ renpy.music.set_volume(AMB_VOL[_lvl], 1.6, channel="amend_amb")
    play sound "minijeu/amend_assets/amend_chair.ogg"
    pause 0.5
    show amend_shadow at amend_shadow_pass onlayer overlay zorder 70
    play sound "minijeu/amend_assets/amend_footsteps.ogg"
    pause 1.5
    hide amend_shadow onlayer overlay
    return
