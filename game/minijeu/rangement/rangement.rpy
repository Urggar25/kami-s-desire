# ============================================================
# MINI-JEU JOUR 7 — TRI DES LIVRAISONS
# Tapis roulant, glisser-déposer, gravité et cadence adaptative.
# ============================================================

default rangement_last_score = 0
default rangement_last_rank = None

init -5 python:
    import time as _rangement_time

    RANGEMENT_DURATION = 60.0
    RANGEMENT_BELT_LIMIT = 1445
    RANGEMENT_BELT_Y = (342, 418)

    RANGEMENT_CATEGORIES = {
        "cafeteria": {
            "label": "CAFÉTÉRIA",
            "short": "CAFÉTÉRIA",
            "color": "#F7C843",
            "crate": "minijeu/rangement/textures/crates/cafeteria.png",
            "x": 24,
        },
        "maintenance": {
            "label": "MAINTENANCE",
            "short": "MAINTENANCE",
            "color": "#FF7A20",
            "crate": "minijeu/rangement/textures/crates/maintenance.png",
            "x": 374,
        },
        "infirmerie": {
            "label": "INFIRMERIE",
            "short": "INFIRMERIE",
            "color": "#32E2D2",
            "crate": "minijeu/rangement/textures/crates/infirmerie.png",
            "x": 724,
        },
        "stockage": {
            "label": "STOCKAGE",
            "short": "STOCKAGE • BONUS",
            "color": "#45A8FF",
            "crate": "minijeu/rangement/textures/crates/stockage.png",
            "x": 1074,
        },
    }

    RANGEMENT_ITEM_DATA = (
        ("cafeteria", "Soupe", "cafe_soupe"),
        ("cafeteria", "Plateau-repas", "cafe_plateau"),
        ("cafeteria", "Boisson", "cafe_boisson"),
        ("cafeteria", "Sandwich", "cafe_sandwich"),
        ("maintenance", "Clé", "maintenance_cle"),
        ("maintenance", "Tournevis", "maintenance_tournevis"),
        ("maintenance", "Carte électronique", "maintenance_carte"),
        ("maintenance", "Câble", "maintenance_cable"),
        ("infirmerie", "Trousse de soin", "infirmerie_trousse"),
        ("infirmerie", "Bandage", "infirmerie_bandage"),
        ("infirmerie", "Fiole médicale", "infirmerie_fiole"),
        ("infirmerie", "Seringue", "infirmerie_seringue"),
        ("stockage", "Carton", "stockage_carton"),
        ("stockage", "Clé de données", "stockage_usb"),
        ("stockage", "Lampe torche", "stockage_lampe"),
        ("stockage", "Ruban adhésif", "stockage_ruban"),
    )

    # Une entrée stockage contre deux pour chaque autre catégorie : la catégorie
    # bonus apparaît exactement 50 % moins souvent que chacune des autres.
    RANGEMENT_WEIGHTED_ITEMS = []
    for _entry in RANGEMENT_ITEM_DATA:
        RANGEMENT_WEIGHTED_ITEMS.extend([_entry] if _entry[0] == "stockage" else [_entry, _entry])


    class RangementGame(object):
        def __init__(self):
            self.duration = RANGEMENT_DURATION
            self.remaining = self.duration
            self.points = 0
            self.correct = 0
            self.wrong = 0
            self.neutral = 0
            self.missed = 0
            self.combo = 0
            self.best_combo = 0
            self.level = 0
            self.items = []
            self.next_id = 1
            self.spawn_clock = 0.35
            self.last_tick = _rangement_time.monotonic()
            self.dragging_id = None
            self.grab_dx = 80.0
            self.grab_dy = 58.0
            self.paused = False
            self.finished = False
            self.feedback = ""
            self.feedback_color = "#FFFFFF"
            self.feedback_age = 99.0
            self.flash_color = "#00000000"
            self.flash_age = 99.0
            # Premier objet déjà engagé à l'ouverture : le joueur voit
            # immédiatement le flux sans attendre une première apparition.
            self.spawn()
            self.items[-1]["x"] = 24.0
            self.spawn_clock = self.spawn_delay

        @property
        def speed_multiplier(self):
            return 1.0 + self.level * 0.14

        @property
        def score(self):
            # Le verdict utilise toujours la cadence réellement conservée à
            # la fin de la tentative, et non un bonus ajouté séparément.
            return int(round(self.points * self.speed_multiplier))

        @property
        def belt_speed(self):
            return 142.0 * self.speed_multiplier

        @property
        def spawn_delay(self):
            return max(0.82, 1.72 - self.level * 0.13)

        def begin(self):
            self.last_tick = _rangement_time.monotonic()

        def toggle_pause(self):
            self.paused = not self.paused
            self.last_tick = _rangement_time.monotonic()
            renpy.restart_interaction()

        def _find(self, item_id):
            for item in self.items:
                if item["id"] == item_id:
                    return item
            return None

        def spawn(self):
            category, label, asset = renpy.random.choice(RANGEMENT_WEIGHTED_ITEMS)
            lane = renpy.random.choice((0, 1))
            self.items.append({
                "id": self.next_id,
                "category": category,
                "label": label,
                "image": "minijeu/rangement/textures/items/%s.png" % asset,
                "x": -165.0,
                "y": float(RANGEMENT_BELT_Y[lane]),
                "state": "belt",
                "vy": 0.0,
                "rot": 0.0,
                "target_y": 830.0,
            })
            self.next_id += 1

        def cancel_drag(self, item_id):
            item = self._find(item_id)
            self.dragging_id = None
            if item is None:
                return
            item["x"] = min(max(float(item["x"]), -20.0), RANGEMENT_BELT_LIMIT - 140.0)
            item["y"] = float(RANGEMENT_BELT_Y[item_id % 2])

        def mouse_down(self):
            if self.paused or self.finished:
                return
            mx, my = renpy.get_mouse_pos()
            for item in reversed(self.items):
                if item["state"] != "belt":
                    continue
                if item["x"] <= mx <= item["x"] + 160 and item["y"] <= my <= item["y"] + 120:
                    self.dragging_id = item["id"]
                    self.grab_dx = mx - item["x"]
                    self.grab_dy = my - item["y"]
                    renpy.restart_interaction()
                    return

        def mouse_up(self):
            if self.dragging_id is None:
                return
            item_id = self.dragging_id
            item = self._find(item_id)
            mx, my = renpy.get_mouse_pos()
            target = None
            if 620 <= my <= 940:
                for category in ("cafeteria", "maintenance", "infirmerie", "stockage"):
                    crate_x = RANGEMENT_CATEGORIES[category]["x"]
                    if crate_x <= mx <= crate_x + 330:
                        target = category
                        break
            if item is not None and target is not None:
                self.drop(item_id, target, mx - 80.0, my - 58.0)
            else:
                self.cancel_drag(item_id)
            renpy.restart_interaction()

        def _set_feedback(self, text, color):
            self.feedback = text
            self.feedback_color = color
            self.feedback_age = 0.0
            self.flash_color = color + "24"
            self.flash_age = 0.0

        def drop(self, item_id, target, drop_x, drop_y):
            item = self._find(item_id)
            self.dragging_id = None
            if item is None or item["state"] != "belt":
                return

            item["state"] = "falling"
            item["x"] = float(drop_x)
            item["y"] = float(drop_y)
            item["vy"] = 110.0
            item["rot"] = renpy.random.uniform(-5.0, 5.0)
            item["target_y"] = 835.0

            if target == item["category"]:
                self.combo += 1
                self.best_combo = max(self.best_combo, self.combo)
                if target == "stockage":
                    self.neutral += 1
                    self._set_feedback("STOCKAGE BONUS  •  +0", "#45A8FF")
                    renpy.play("audio/sfx_drop.mp3", channel="sound")
                else:
                    self.correct += 1
                    self.points += 1
                    self._set_feedback("TRI CORRECT  •  +1", "#5DFF9A")
                    renpy.play("audio/sfx_qte_hit.wav", channel="sound")

                if self.combo > 0 and self.combo % 5 == 0 and self.level < 5:
                    self.level += 1
                    self._set_feedback(kd_tr("ACCÉLÉRATION  •  MULTIPLICATEUR x%.2f") % self.speed_multiplier, "#FFD166")
                    renpy.play("audio/sfx_announce.mp3", channel="sound")
            else:
                self.wrong += 1
                self.combo = 0
                self.points -= 1
                if self.level > 0:
                    self.level -= 1
                    self._set_feedback("ERREUR  •  -1 POINT  •  CADENCE -1", "#FF4D6D")
                else:
                    self._set_feedback("MAUVAISE CAISSE  •  -1 POINT", "#FF4D6D")
                renpy.play("audio/sfx_qte_miss.wav", channel="sound")

        def tick(self):
            now = _rangement_time.monotonic()
            dt = min(0.12, max(0.0, now - self.last_tick))
            self.last_tick = now
            if self.paused or self.finished:
                return

            self.remaining = max(0.0, self.remaining - dt)
            self.feedback_age += dt
            self.flash_age += dt
            self.spawn_clock -= dt

            if self.spawn_clock <= 0.0 and self.remaining > 0.35:
                self.spawn()
                jitter = renpy.random.uniform(-0.14, 0.20)
                self.spawn_clock = self.spawn_delay + jitter

            survivors = []
            for item in self.items:
                if item["state"] == "belt":
                    if item["id"] == self.dragging_id:
                        mouse_x, mouse_y = renpy.get_mouse_pos()
                        item["x"] = mouse_x - self.grab_dx
                        item["y"] = mouse_y - self.grab_dy
                    else:
                        item["x"] += self.belt_speed * dt
                    if item["x"] > RANGEMENT_BELT_LIMIT:
                        self.missed += 1
                        self.combo = 0
                        continue
                else:
                    item["vy"] += 980.0 * dt
                    item["y"] += item["vy"] * dt
                    item["rot"] += 90.0 * dt
                    if item["y"] >= item["target_y"]:
                        continue
                survivors.append(item)
            self.items = survivors

            if self.remaining <= 0.0:
                self.finished = True
                self.dragging_id = None
            renpy.restart_interaction()

        def result(self):
            return {
                "score": self.score,
                "points": self.points,
                "multiplier": self.speed_multiplier,
                "correct": self.correct,
                "wrong": self.wrong,
                "neutral": self.neutral,
                "missed": self.missed,
                "best_combo": self.best_combo,
                "level": self.level,
                "multiplier_bonus": self.score - self.points,
            }


    class RangementObjectsDisplayable(renpy.Displayable):
        """Dessine le flux mobile directement à chaque frame."""
        def __init__(self, game, **kwargs):
            super(RangementObjectsDisplayable, self).__init__(**kwargs)
            self.game = game
            self._assets = {}

        def _asset(self, path):
            displayable = self._assets.get(path)
            if displayable is None:
                displayable = renpy.displayable(path)
                self._assets[path] = displayable
            return displayable

        def render(self, width, height, st, at):
            rv = renpy.Render(1920, 1080)

            # L'objet tenu est rendu en dernier pour passer devant tout le flux.
            ordered = [i for i in self.game.items if i["id"] != self.game.dragging_id]
            ordered += [i for i in self.game.items if i["id"] == self.game.dragging_id]

            for item in ordered:
                sprite = self._asset(item["image"])
                if item["state"] == "falling":
                    zoom = max(0.62, 1.0 - max(0.0, item["y"] - 620.0) / 800.0)
                    sprite = Transform(sprite, rotate=item["rot"], zoom=zoom)
                elif item["id"] == self.game.dragging_id:
                    sprite = Transform(sprite, zoom=1.08)

                rendered = renpy.render(sprite, 190, 150, st, at)
                rv.blit(rendered, (int(item["x"]), int(item["y"])))

            renpy.redraw(self, 0.03)
            return rv

        def visit(self):
            return list(self._assets.values())

transform rangement_belt_dash:
    xoffset 0
    linear 0.75 xoffset 118
    repeat

transform rangement_crate_idle:
    yoffset 0
    ease 1.2 yoffset -3
    ease 1.2 yoffset 0
    repeat

transform rangement_drop_glow:
    alpha 0.18
    ease 0.8 alpha 0.52
    ease 0.8 alpha 0.18
    repeat

transform rangement_tuto_item:
    xpos 50 ypos 100
    linear 1.25 xpos 410
    pause 0.25
    easein 0.38 xpos 480 ypos 345 rotate 12
    pause 0.55
    alpha 0.0
    pause 0.15
    alpha 1.0 rotate 0
    repeat

transform rangement_pause_pulse:
    alpha 0.72
    ease 0.7 alpha 1.0
    ease 0.7 alpha 0.72
    repeat


screen tuto_rangement(as_overlay=False):
    $ _steps = [
        ("ATTRAPEZ", "Cliquez et maintenez un objet qui défile sur le tapis."),
        ("TRIEZ", "Glissez-le au-dessus de la caisse correspondant à sa catégorie."),
        ("ACCÉLÉREZ", "Cinq tris justes d'affilée accélèrent le tapis et donnent +5."),
        ("BONUS", "Les objets de stockage sont plus rares et valent 0 point."),
    ]

    use mk_tuto_chrome("TRI DES LIVRAISONS", _steps, "tuto_rangement", as_overlay):
        add Solid("#111D27") xpos 16 ypos 78 xsize 700 ysize 180
        add Solid("#263845") xpos 16 ypos 245 xsize 700 ysize 12
        for _tx in range(20, 700, 118):
            add Solid("#39D9E855") xpos _tx ypos 232 xsize 58 ysize 3 at rangement_belt_dash
        add "minijeu/rangement/textures/items/infirmerie_trousse.png" at rangement_tuto_item
        add Solid("#32E2D233") xpos 430 ypos 315 xsize 260 ysize 160 at rangement_drop_glow
        add "minijeu/rangement/textures/crates/infirmerie.png":
            xpos 410
            ypos 300
            zoom 0.78
        text "INFIRMERIE":
            xpos 482 ypos 455 size 22 color "#32E2D2" bold True


screen rangement_game(game):
    modal True
    zorder 300

    key "mousedown_1" action Function(game.mouse_down)
    key "mouseup_1" action Function(game.mouse_up)

    add "minijeu/rangement/textures/rangement_background.png"
    add Solid("#02060A44")

    # En-tête
    frame:
        xpos 22 ypos 18 xsize 1400 ysize 92
        background Fixed(Solid("#06111BE8"), Solid("#31D9E866", ysize=2), Solid("#31D9E855", xsize=3))
        padding (24, 12)
        hbox:
            spacing 34
            vbox:
                text "MINI-JEU  •  TRI DES LIVRAISONS" size 30 color "#63E9F4" bold True
                text "ATTRAPEZ • GLISSEZ • DÉPOSEZ AU-DESSUS DE LA BONNE CAISSE" size 17 color "#8EA9B5" kerning 1.5
            null width 120
            vbox:
                text "SCORE CALCULÉ" size 16 color "#7997A6"
                text ("%+04d" % game.score) size 38 color ("#FF6B7D" if game.score < 0 else "#FFFFFF") bold True
            vbox:
                text "SÉRIE" size 16 color "#7997A6"
                text ("x%d" % game.combo) size 38 color "#FFD166" bold True
            vbox:
                text "CADENCE" size 16 color "#7997A6"
                text ("x%.2f" % game.speed_multiplier) size 38 color "#63E9F4" bold True

    # Mouvement lumineux du tapis.
    for _bx in range(-100, 1450, 118):
        add Solid("#28D8E84A") xpos _bx ypos 548 xsize 58 ysize 3 at rangement_belt_dash

    text "DÉFILEMENT  >>>":
        xpos 610 ypos 282 size 20 color "#45CFE0" kerning 2

    # Couche dédiée au flux : décor < objets < façades des caisses < HUD.
    # Le displayable relit game.items à chaque frame sans dépendre du cache Screen.
    add RangementObjectsDisplayable(game)

    # Zones et façades des caisses.
    for _cat in ("cafeteria", "maintenance", "infirmerie", "stockage"):
        $ _cfg = RANGEMENT_CATEGORIES[_cat]
        add Solid(_cfg["color"] + "22") xpos (_cfg["x"] + 20) ypos 650 xsize 290 ysize 142 at rangement_drop_glow
        add _cfg["crate"] xpos _cfg["x"] ypos 690 at rangement_crate_idle
        text kd_tr(_cfg["short"]):
            xpos (_cfg["x"] + 165)
            ypos 926
            xanchor 0.5
            size 20
            color _cfg["color"]
            bold True
            outlines [(2, "#02060A", 0, 1)]

    # Panneau de contrôle latéral.
    frame:
        xpos 1460 ypos 126 xsize 430 ysize 872
        background Fixed(Solid("#05101BEF"), Solid("#31D9E855", xsize=3), Solid("#31D9E844", ysize=2))
        padding (24, 24)
        vbox:
            spacing 18
            text "TEMPS RESTANT" size 20 color "#63E9F4" bold True
            text ("%02d:%02d" % (int(game.remaining) // 60, int(game.remaining) % 60)):
                size 54 color ("#FF6B7D" if game.remaining <= 10 else "#FFFFFF") bold True
            fixed:
                xsize 374 ysize 14
                add Solid("#102431")
                add Solid("#31D9E8") xsize int(374 * game.remaining / game.duration)
            add Solid("#31D9E833", xsize=374, ysize=2)
            text "RÈGLES" size 20 color "#63E9F4" bold True
            text "• Bonne caisse :  +1 point\n• Mauvaise caisse :  -1 point et cadence -1\n• Stockage correct :  0 point\n• 5 tris justes : cadence +1\n• Score : points × cadence":
                size 19 color "#B9CBD3" line_spacing 8
            add Solid("#31D9E833", xsize=374, ysize=2)
            text "BILAN EN DIRECT" size 20 color "#63E9F4" bold True
            grid 2 4:
                spacing 16
                text "Corrects" size 18 color "#8EA9B5"
                text "[game.correct]" size 20 color "#5DFF9A" bold True
                text "Erreurs" size 18 color "#8EA9B5"
                text "[game.wrong]" size 20 color "#FF6B7D" bold True
                text "Bonus neutres" size 18 color "#8EA9B5"
                text "[game.neutral]" size 20 color "#45A8FF" bold True
                text "Objets passés" size 18 color "#8EA9B5"
                text "[game.missed]" size 20 color "#D7E2E7" bold True
            add Solid("#31D9E833", xsize=374, ysize=2)
            text "PROCHAINE ACCÉLÉRATION" size 18 color "#FFD166" bold True
            text (kd_tr("%d / 5 tris") % (game.combo % 5)) size 25 color "#FFFFFF"
            fixed:
                xsize 374 ysize 12
                add Solid("#2C2517")
                add Solid("#FFD166") xsize int(374 * (game.combo % 5) / 5.0)
            null height 14
            textbutton kd_tr("REPRENDRE" if game.paused else "PAUSE"):
                xsize 250 ysize 54
                xalign 0.5
                background Solid("#153547E8")
                hover_background Solid("#24607CE8")
                text_size 23
                text_color "#FFFFFF"
                text_xalign 0.5
                action Function(game.toggle_pause)

    if game.feedback and game.feedback_age < 1.35:
        text kd_tr(game.feedback):
            xpos 720 ypos 222 xanchor 0.5
            size 31 color game.feedback_color bold True
            outlines [(3, "#02060A", 0, 1)]

    if game.flash_age < 0.18:
        add Solid(game.flash_color)

    if game.paused:
        add Solid("#02060AB8")
        frame:
            align (0.5, 0.47)
            xsize 620 ysize 260
            background Fixed(Solid("#071723F5"), Solid("#63E9F466", ysize=3), Solid("#63E9F455", xsize=3))
            vbox:
                align (0.5, 0.5)
                spacing 22
                text "TRI EN PAUSE" at rangement_pause_pulse:
                    xalign 0.5 size 44 color "#63E9F4" bold True
                text "Le chronomètre et le tapis sont arrêtés.":
                    xalign 0.5 size 22 color "#B9CBD3"
                textbutton "REPRENDRE":
                    xalign 0.5 xsize 280 ysize 58
                    background Solid("#17445BE8")
                    hover_background Solid("#26708FE8")
                    text_size 25 text_color "#FFFFFF" text_xalign 0.5
                    action Function(game.toggle_pause)

    if game.finished:
        timer 0.01 action Return(game.result())
    else:
        timer 0.04 repeat True action Function(game.tick)


label rangement_play:
    $ _rangement_game = RangementGame()
    call mk_tutorial("rangement", "tuto_rangement") from _call_rangement_tutorial
    call mk_countdown from _call_rangement_countdown
    $ _rangement_game.begin()
    call screen rangement_game(_rangement_game)
    $ _rangement_result = _return
    $ rangement_last_score = _rangement_result["score"]
    $ _rangement_rank_score = max(0, min(25, _rangement_result["score"]))
    $ _rangement_stats = [
        (_("Points bruts"), str(_rangement_result["points"])),
        (_("Multiplicateur final"), "x%.2f" % _rangement_result["multiplier"]),
        (_("Score final"), str(_rangement_result["score"])),
        (_("Tris corrects"), str(_rangement_result["correct"])),
        (_("Erreurs"), str(_rangement_result["wrong"])),
        (_("Meilleure série"), "x%d" % _rangement_result["best_combo"]),
    ]
    $ _rangement_challenges = [
        (_("Aucune erreur"), _rangement_result["wrong"] == 0),
        (_("Atteindre la cadence x1.42"), _rangement_result["level"] >= 3),
    ]
    call mk_show_results(_("TRI DES LIVRAISONS"), _rangement_rank_score, 25, stats=_rangement_stats, challenges=_rangement_challenges, mg_id="rangement", retries=0) from _call_rangement_results
    $ rangement_last_rank = _return
    return _rangement_result
