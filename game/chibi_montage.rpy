# ============================================================
# chibi_montage.rpy — Moteur d'animation "montage chibi"
#
# Transforme une planche de sprites chibi (cases alignées en ligne) en
# séquence cinématique : bandeau HUD qui s'ouvre en volet, coupes
# rythmées avec squash & stretch, image rémanente, anneau d'impact,
# lignes de vitesse, étincelles, reflet au sol, jauge d'étapes,
# légendes animées et SFX synchronisés.
#
# Ce fichier ne contient QUE le rendu. Toute l'animation (chronologie,
# positions, opacités, particules) vit dans le module Python pur
# game/python-packages/chibi_montage_core.py, qui produit pour chaque
# instant une liste d'opérations de dessin. Le même module alimente
# tools/preview_chibi_montage.py, donc l'aperçu hors-jeu et le jeu ne
# peuvent pas diverger.
#
# Tout est piloté par le temps de l'affichable (st) : une seule source
# de vérité, donc aucune couche ne peut se désynchroniser d'une autre.
#
# Usage depuis un script :
#   $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
#
# Textures FX : générées par tools/build_chibi_montage_fx.py
# ============================================================

init python:

    import time as _cm_time
    import chibi_montage_core as cmc

    # Ré-exportés pour que les scripts puissent décrire une séquence
    # sans importer le module à la main.
    ChibiStep = cmc.ChibiStep
    ChibiMontageSpec = cmc.ChibiMontageSpec

    def chibi_montage_spec(**kwargs):
        """Construit une spec même après un auto-reload du vieux core.

        Ren'Py conserve les modules Python purs en mémoire pendant certains
        auto-reloads. Une ancienne ChibiMontageSpec peut donc rester active
        quelques secondes alors que ce fichier utilise déjà `captions`.
        """
        captions = kwargs.pop("captions", True)
        try:
            return ChibiMontageSpec(captions=captions, **kwargs)
        except TypeError as error:
            if "captions" not in str(error):
                raise
            spec = ChibiMontageSpec(**kwargs)
            # L'ancien moteur génère toujours les légendes. Les conserver
            # évite qu'il produise des opérations de texte sans textures.
            spec.captions = True
            return spec

    class ChibiMontage(renpy.Displayable):
        """Exécute la liste de dessin produite par ChibiTimeline."""

        def __init__(self, spec, **kwargs):
            super(ChibiMontage, self).__init__(**kwargs)

            self.spec = spec
            self.timeline = cmc.ChibiTimeline(spec)
            self.duration = self.timeline.duration

            # --- Sources images ---
            self.sheet = Image(spec.sheet)
            self.fx = {}
            for name in cmc.FX_SIZE:
                self.fx[name] = Image(cmc.FX_DIR + name + ".png")

            # --- Aplats (créés une fois, donc mis en cache) ---
            self.solids = {}
            for color in (cmc.ACCENT, cmc.EDGE, cmc.SEG_OFF, cmc.FLASH):
                self.solids[color] = Solid(color)

            # --- Textes (créés une fois : Ren'Py met leur texture en cache) ---
            n = len(spec.steps)
            self.texts = {
                "kicker": [self._make_text("kicker", spec.kicker)],
                "footer": [self._make_text("footer", spec.footer)],
                "footer_final": [self._make_text("footer_final", spec.footer_final)],
            }
            if spec.captions:
                self.texts["counter"] = [
                    self._make_text("counter", u"ÉTAPE %02d / %02d" % (i + 1, n))
                    for i in range(n)]
                self.texts["caption"] = [
                    self._make_text("caption", step.caption)
                    for step in spec.steps]
                self.texts["ghost"] = [
                    self._make_text("ghost", u"%02d" % (i + 1))
                    for i in range(n)]

        def _make_text(self, style, body):
            spec = cmc.TEXT_STYLES[style]
            kwargs = {
                "font": spec["font"],
                "size": spec["size"],
                "color": spec["color"],
                "kerning": spec.get("kerning", 0),
            }
            drop = spec.get("shadow")
            if drop:
                kwargs["outlines"] = [(3, drop[2] + "cc", drop[0], drop[1])]
            return Text(body, **kwargs)

        # -- prédiction / préchargement des textures --
        def visit(self):
            rv = [self.sheet]
            rv.extend(self.fx.values())
            for group in self.texts.values():
                rv.extend(group)
            return rv

        # -- SFX : exactement les mêmes temps que la chronologie visuelle --
        def sound_cues(self):
            return self.timeline.sound_cues()

        # ----------------------------------------------------
        def _source(self, op):
            kind, key = op["src"]
            if kind == "fx":
                return self.fx[key]
            return self.sheet

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            if st >= self.duration:
                return rv

            renpy.redraw(self, 0)

            for op in self.timeline.ops(st):
                kind = op["kind"]

                if kind == "img":
                    kwargs = {
                        "xzoom": op["xzoom"],
                        "yzoom": op["yzoom"],
                        "alpha": op["alpha"],
                        "subpixel": True,
                    }
                    kwargs["crop"] = op["crop"]
                    if op["rotate"]:
                        kwargs["rotate"] = op["rotate"]
                    if op["bright"]:
                        kwargs["matrixcolor"] = BrightnessMatrix(op["bright"])
                    elif op["tint"]:
                        kwargs["matrixcolor"] = TintMatrix(op["tint"])

                    d = Transform(self._source(op), **kwargs)
                    r = renpy.render(d, width, height, st, at)
                    rv.subpixel_blit(r, (op["cx"] - r.width / 2.0,
                                         op["cy"] - r.height / 2.0))

                elif kind == "solid":
                    d = Transform(self.solids[op["color"]], alpha=op["alpha"])
                    r = renpy.render(d, op["w"], op["h"], st, at)
                    rv.subpixel_blit(r, (op["x"], op["y"]))

                else:  # text
                    d = Transform(self.texts[op["style"]][op["index"]],
                                  alpha=op["alpha"], subpixel=True)
                    r = renpy.render(d, width, height, st, at)
                    rv.subpixel_blit(r, (op["x"], op["y"]))

            return rv

    # ------------------------------------------------------------
    # Lecture d'une séquence depuis le script
    # ------------------------------------------------------------
    def chibi_montage_play(spec, tag="chibi_montage", zorder=260):
        """Affiche la séquence, joue les SFX en rythme, puis nettoie.

        Les sons sont déclenchés sur une horloge absolue : même si une
        image est sautée, le son ne dérive pas par rapport à l'animation.
        Le `finally` garantit qu'aucun affichable ne reste à l'écran, y
        compris si le joueur passe en avance rapide.
        """
        montage = ChibiMontage(spec)
        renpy.show(tag, what=montage, zorder=zorder, layer="master")

        try:
            t0 = _cm_time.time()
            for (cue_t, path, volume) in montage.sound_cues():
                if renpy.is_skipping():
                    break
                wait = cue_t - (_cm_time.time() - t0)
                if wait > 0.005:
                    renpy.pause(wait, hard=True)
                if renpy.is_skipping():
                    break
                if path and renpy.loadable(path):
                    renpy.sound.play(path, channel="sound",
                                     relative_volume=volume)

            rest = montage.duration - (_cm_time.time() - t0)
            if rest > 0.005 and not renpy.is_skipping():
                renpy.pause(rest, hard=True)
        finally:
            renpy.hide(tag, layer="master")


# ============================================================
# Séquence J7 — Noam s'habille (8 cases)
# ============================================================

define CHIBI_MONTAGE_J701_NOAM = chibi_montage_spec(
    sheet="images/background/interact/animation/noam_change/noam_change_frames.png",
    sheet_size=(3104, 724),
    cols=8,
    content=(17, 697),
    chibi_x=1240,
    feet_y=852,
    zoom=0.88,
    captions=False,
    kicker=u"SÉQUENCE — HABILLAGE",
    footer=u"LYSA ATTEND DEVANT LA PORTE",
    footer_final=u"CINQ MINUTES. À PEU PRÈS.",
    steps=[
        ChibiStep(0, 0.62, u"RÉVEIL",
                  sfx="audio/sfx_beep.mp3", volume=0.30),
        ChibiStep(1, 0.54, u"ENCORE EN PYJAMA",
                  sfx="audio/sfx_paper.mp3", volume=0.35),
        ChibiStep(2, 0.70, u"BRRR.",
                  sfx="audio/sfx_paper.mp3", volume=0.40,
                  tint="#c6d8ff", shiver=5.0),
        ChibiStep(3, 0.60, u"CHEMISE",
                  sfx="audio/sfx_paper.mp3", volume=0.55),
        ChibiStep(4, 0.56, u"BOUTONS ALIGNÉS",
                  sfx="audio/sfx_paper.mp3", volume=0.45),
        ChibiStep(5, 0.62, u"VESTE",
                  sfx="audio/sfx_paper.mp3", volume=0.55),
        ChibiStep(6, 0.54, u"MANCHES AJUSTÉES",
                  sfx="audio/sfx_paper.mp3", volume=0.40),
        ChibiStep(7, 1.15, u"PRÊT.",
                  sfx="audio/sfx_qte_hit.wav", volume=0.70,
                  hop=1.15, final=True),
    ],
)
