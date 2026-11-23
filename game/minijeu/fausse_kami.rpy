# ============================================================
# minijeu/fausse_kami.rpy — Combat de boss « FAUSSE KAMI » (Jour 6_0_1)
#
# Kami est piratée et refuse de l'admettre. Trois phases :
#   1. LE DÉNI       — débat forcé : LAISSER PARLER / INTERROMPRE / CONFRONTER
#   2. L'USURPATION  — plusieurs Kami à l'écran, neutraliser les fausses
#   3. LE SILENCE    — pare-feu réflexe, puis coupure manuelle du signal
#
#   call fausse_kami_run
#   -> _return = {"success", "rank", "score", "executed", "friendly",
#                 "max_corruption", "late_cut", "skipped"}
#
# Textures : minijeu/fausse_kami_assets/ (générées)
# Portraits : images/background/kami_diffusion/<expr>[_parle].png
# Réutilise : _kit.rpy (tutoriel, retry, résultats), kd_staging (couleurs,
#             noms, portraits), refutation_assets (hexagones).
# ============================================================

default fk = None
default fk_session = None
default fk_last_result = {}
default persistent.fk_best_score = 0

init -1 python:
    import time as _fk_time
    import math as _fk_math
    import random as _fk_random

    FK_DIR = "minijeu/fausse_kami_assets/"
    FK_KAMI_DIR = "images/background/kami_diffusion/"
    FK_CYAN = "#5cd3ff"
    FK_RED = "#ff2e5a"
    FK_AMBER = "#ffb84d"
    FK_VIOLET = "#b26cff"
    FK_WHITE = "#eef7ff"
    FK_FONT_TITLE = "fonts/Rajdhani-SemiBold.ttf"
    FK_FONT_BODY = "fonts/Barlow-SemiBold.ttf"
    FK_MG_ID = "fausse_kami"
    FK_TITLE = "FAUSSE KAMI"

    # Recadrage commun des textures de diffusion (1536x1024) sur Kami seule.
    FK_KAMI_CROP = (230, 20, 1080, 980)
    FK_KAMI_SIZE = (1080, 980)

    renpy.music.register_channel("fk_loop", mixer="sfx", loop=True)

    # --------------------------------------------------------
    # Utilitaires
    # --------------------------------------------------------
    def fk_tr(text):
        try:
            return kd_tr(text)
        except Exception:
            return text

    def fk_clamp(v, lo, hi):
        return lo if v < lo else (hi if v > hi else v)

    def fk_ease_out(x):
        x = fk_clamp(x, 0.0, 1.0)
        return 1.0 - (1.0 - x) ** 3

    def fk_ease_in_out(x):
        x = fk_clamp(x, 0.0, 1.0)
        return 3 * x * x - 2 * x * x * x

    def fk_fade(age, dur, fin=0.12, fout=0.2):
        """Alpha d'un élément vivant `dur` secondes, fondu entrée/sortie."""
        if age < 0 or age > dur:
            return 0.0
        a = 1.0
        if fin > 0 and age < fin:
            a = age / fin
        if fout > 0 and age > dur - fout:
            a = min(a, (dur - age) / fout)
        return fk_clamp(a, 0.0, 1.0)

    def fk_mix_hex(c1, c2, f):
        f = fk_clamp(f, 0.0, 1.0)
        a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
        b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
        return "#%02x%02x%02x" % tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3))

    def fk_sfx(path, volume=1.0):
        try:
            if renpy.loadable(path):
                renpy.music.play(path, channel="audio", relative_volume=volume)
        except Exception:
            pass

    def fk_loop(path=None):
        if path is None:
            renpy.music.stop(channel="fk_loop", fadeout=0.4)
        elif renpy.loadable(path):
            renpy.music.play(path, channel="fk_loop", fadein=0.4, if_changed=True)

    def fk_name(tag):
        if tag == "kami":
            return "KAMI"
        if tag == "???":
            return "???"
        try:
            return kd_display_name(tag).upper()
        except Exception:
            return tag.upper()

    def fk_color(tag):
        if tag == "kami":
            return FK_CYAN
        if tag == "???":
            return FK_RED
        try:
            return kd_char_color(tag)
        except Exception:
            return FK_CYAN

    def fk_portrait(tag, size=200):
        try:
            p = kd_portrait(tag, size)
        except Exception:
            p = Solid(fk_color(tag), xysize=(size, size))
        return AlphaMask(Transform(p, xysize=(size, size)),
                         Transform(FK_DIR + "fk_hexmask.png", xysize=(size, size)))

    # --------------------------------------------------------
    # Portraits de Kami (réutilise les textures de diffusion)
    # --------------------------------------------------------
    def fk_kami_path(expr, talking=False):
        try:
            expr = kami_diffusion_normalize(expr)
        except Exception:
            pass
        if talking:
            p = FK_KAMI_DIR + expr + "_parle.png"
            if renpy.loadable(p):
                return p
        p = FK_KAMI_DIR + expr + ".png"
        if renpy.loadable(p):
            return p
        return FK_KAMI_DIR + "professeur.png"

    def fk_kami_base(expr, talking=False, tint="#6ce8fa"):
        img = Transform(fk_kami_path(expr, talking), crop=FK_KAMI_CROP)
        if tint:
            img = Transform(img, matrixcolor=TintMatrix(tint))
        return img

    def fk_kami(expr, talking=False, glitch=0.0, tint="#6ce8fa", seed=0):
        """Kami recadrée (1080x980), avec aberration et tranches de glitch."""
        base = fk_kami_base(expr, talking, tint)
        if glitch <= 0.02:
            return base
        rnd = _fk_random.Random(seed)
        w, h = FK_KAMI_SIZE
        children = []
        ab = int(6 + glitch * 22)
        children.append(Transform(base, matrixcolor=TintMatrix("#ff2050"),
                                  xoffset=-ab, alpha=0.45 * glitch))
        children.append(Transform(base, matrixcolor=TintMatrix("#20f0ff"),
                                  xoffset=ab, alpha=0.45 * glitch))
        # Tranches horizontales décalées.
        n = 7
        y = 0
        for i in range(n):
            hh = int(h / n)
            off = 0
            if rnd.random() < 0.25 + glitch * 0.6:
                off = int(rnd.uniform(-1, 1) * (20 + glitch * 110))
            children.append(Transform(base, crop=(0, y, w, hh), xpos=off, ypos=y))
            y += hh
        return Fixed(*children, xysize=(w, h))

    def fk_monitor_glass(expr, tint, glitch, seed, talking=False):
        """Contenu de la vitre d'un moniteur (392x262)."""
        bg = Transform(FK_KAMI_DIR + "bg_diffusion_fond.png",
                       crop=(300, 160, 936, 624), xysize=(392, 262))
        kami = Transform(fk_kami(expr, talking, glitch, tint, seed), zoom=0.28)
        return Fixed(bg, Transform(kami, xalign=0.5, yalign=1.0, yoffset=8),
                     xysize=(392, 262))

    # --------------------------------------------------------
    # Base commune des phases
    # --------------------------------------------------------
    class FKBase(object):
        title = ""
        subtitle = ""
        title_dur = 2.6

        def __init__(self, session):
            self.session = session
            self.t = 0.0
            self.last = None
            self.paused = False
            self.result = None
            self.end_t = None
            self.fx = []          # tampons, flashs, alertes
            self.cutins = []      # répliques des représentants
            self.bark = None      # réplique de Kami
            self.shake = 0.0
            self.sx = 0
            self.sy = 0
            self.seed = 0
            self.mouth = False
            self.help_screen = None

        # ---- horloge
        def tick(self):
            now = _fk_time.time()
            if self.last is None:
                self.last = now
            dt = fk_clamp(now - self.last, 0.0, 0.1)
            self.last = now
            if self.paused:
                if self.help_screen and not renpy.get_screen(self.help_screen):
                    self.paused = False
                    self.last = None
                renpy.restart_interaction()
                return
            self.t += dt
            self.seed = int(self.t * 24)
            self.mouth = (self.t % 0.30) < 0.15
            if self.shake > 0:
                self.shake = max(0.0, self.shake - dt * 2.8)
                amp = 26 * self.shake
                self.sx = int(_fk_random.uniform(-amp, amp))
                self.sy = int(_fk_random.uniform(-amp, amp) * 0.6)
            else:
                self.sx = self.sy = 0
            self.fx = [f for f in self.fx if self.t - f["t0"] < f["dur"]]
            self.cutins = [c for c in self.cutins if self.t - c["t0"] < c["dur"] + 0.3]
            if self.bark and self.t - self.bark["t0"] > self.bark["dur"]:
                self.bark = None
            if self.result is None:
                self.update(dt)
            renpy.restart_interaction()

        def update(self, dt):
            pass

        def in_title(self):
            return self.t < self.title_dur

        def open_help(self, screen_name):
            self.paused = True
            self.help_screen = screen_name
            renpy.show_screen(screen_name, as_overlay=True)
            renpy.restart_interaction()

        # ---- effets
        def add_fx(self, kind, dur, **kw):
            d = dict(kind=kind, t0=self.t, dur=dur)
            d.update(kw)
            self.fx.append(d)

        def stamp(self, text, color, slash="red", dur=1.0, sub=""):
            self.fx = [f for f in self.fx if f["kind"] != "stamp"]
            self.add_fx("stamp", dur, text=text, color=color, slash=slash, sub=sub)

        def flash(self, color="#ffffff", strength=0.45, dur=0.35):
            self.add_fx("flash", dur, color=color, strength=strength)

        def alarm(self, text, dur=1.6):
            self.fx = [f for f in self.fx if f["kind"] != "alarm"]
            self.add_fx("alarm", dur, text=text)
            fk_sfx("audio/sfx_kami_alert.wav")

        def hit(self, amount=0.6):
            self.shake = max(self.shake, amount)

        def say_kami(self, text, mood="taquin", dur=None):
            if not text:
                return
            if dur is None:
                dur = fk_clamp(1.2 + len(text) / 24.0, 2.0, 4.4)
            self.bark = dict(text=text, mood=mood, t0=self.t, dur=dur)

        def cutin(self, tag, text, dur=None, delay=0.0):
            if dur is None:
                dur = fk_clamp(1.0 + len(text) / 26.0, 1.8, 3.6)
            # La plus récente l'emporte à l'affichage (active_cutin).
            self.cutins.append(dict(tag=tag, text=text, t0=self.t + delay, dur=dur))

        def active_cutin(self):
            best = None
            for c in self.cutins:
                if c["t0"] <= self.t <= c["t0"] + c["dur"]:
                    if best is None or c["t0"] >= best["t0"]:
                        best = c
            return best

        def finish(self, result, delay=1.6):
            if self.end_t is None:
                self.end_t = self.t + delay
                self.pending = result

        def update_end(self):
            if self.end_t is not None and self.t >= self.end_t:
                self.result = self.pending
                return True
            return self.end_t is not None

    # --------------------------------------------------------
    # Session (score cumulé sur les trois phases)
    # --------------------------------------------------------
    class FKSession(object):
        def __init__(self):
            self.score = 0
            self.score_max = 0
            self.executed = 0      # commandes pirates exécutées
            self.friendly = 0      # Kami frappée par erreur
            self.max_corruption = 0
            self.late_cut = False
            self.p1_correct = 0
            self.p1_total = 0
            self.p2_neutralized = 0
            self.p2_fakes = 0
            self.p3_hits = 0
            self.p3_cmds = 0

        def add(self, pts, max_pts):
            self.score += max(0, pts)
            self.score_max += max_pts

    def fk_session_reset():
        store.fk_session = FKSession()
        store.fk = None

    # ========================================================
    # PHASE 1 — LE DÉNI
    # ========================================================
    # kind  : "auth" (laisser parler) | "inject" (interrompre) | "contra" (confronter)
    # wave  : "organic" | "flat" | "loop"     clock : True = horodatage décalé
    FK_P1_LINES = [
        dict(kind="auth", wave="organic", clock=False, expr="taquin", window=9.0,
             text=_("Allons, allons ! Un petit hoquet technique et vous me faites tous des têtes d'enterrement ?"),
             hint=("iris", _("Ça, c'est elle. Regarde l'onde : quand c'est elle, ça part dans tous les sens.")),
             ok=_("Merci, Noam. Enfin quelqu'un de bien élevé."),
             bad_cut=_("Ah, bravo. Je disais un truc sympa, en plus."),
             bad_confront=_("Me confronter ? Sur quoi ? Mon charme ?"),
             bad_let=None),
        dict(kind="inject", wave="flat", clock=True, expr="professeur", window=8.0,
             text=_("Séance ouverte. Les bulletins non exprimés seront comptés comme favorables."),
             hint=("kael", _("L'horodatage. Il indique treize heures quarante-huit.")),
             ok=_("Hé ! Tu me coupes, maintenant ? ...C'était moi. Évidemment que c'était moi."),
             bad_cut=None,
             bad_confront=_("Tu confrontes quoi, là ? Le vide ?"),
             bad_let=_("Voilà. Tu vois ? Tout roule."),
             alarm=_("BULLETINS VIERGES : « POUR »"),
             after=("mara", _("Putain, elle vient de dire quoi, là ?"))),
        dict(kind="contra", wave="organic", clock=False, expr="fier", window=8.0,
             text=_("Je ne me suis pas répétée. Pas une seule fois. Je m'en souviendrais, quand même !"),
             hint=("nyra", _("Attends. Ça, c'est faux, non ?")),
             proof=("iris", _("« Très bien. » Deux fois. Même intonation, même délai !")),
             ok=_("Je... Bon. Peut-être deux fois. C'est un style."),
             bad_cut=_("Tu me coupes parce que j'ai raison. C'est mignon."),
             bad_confront=None,
             bad_let=_("Exactement. Merci de ne pas en faire une histoire.")),
        dict(kind="auth", wave="organic", clock=False, expr="taquin", window=7.5,
             text=_("Kael, lâche cette console. Tu fixes mes journaux comme si je t'avais volé ton dessert."),
             hint=None,
             ok=_("Tu vois, Kael ? Noam, lui, il sait écouter."),
             bad_cut=_("Tu deviens pénible, Noam. Vraiment pénible."),
             bad_confront=_("Il n'y a rien à confronter ! C'est un DESSERT, Noam !"),
             bad_let=None,
             after=("kael", _("Je n'ai pas de dessert."))),
        dict(kind="inject", wave="loop", clock=False, expr="professeur", window=7.5,
             text=_("Noam. Autorise l'accès console de séance. C'est moi. Tout va bien."),
             hint=("kael", _("Il a recalé l'horloge. Fie-toi à l'onde... elle boucle.")),
             ok=_("Arrête de me couper ! J'ai... J'avais pas fini."),
             bad_cut=None,
             bad_confront=_("Tu confrontes une phrase que... que j'ai dite. Oui. Je l'ai dite."),
             bad_let=_("...Pourquoi la console de Kael vient de s'allumer ?"),
             alarm=_("ACCÈS CONSOLE : ACCORDÉ")),
        dict(kind="contra", wave="organic", clock=False, expr="professeur", window=7.0,
             text=_("Mes horloges sont parfaitement synchronisées. Treize heures cinquante-huit, partout !"),
             hint=None,
             proof=("elen", _("Nos tablettes disaient treize heures cinquante ! Je l'ai vu !")),
             ok=_("Treize heures... cinquante. Non. Cinquante-huit. Pourquoi j'ai deux heures ?"),
             bad_cut=_("Ne. Me. Coupe. Pas."),
             bad_confront=None,
             bad_let=_("Voilà. Parfaitement synchronisées. Ha. Ha.")),
        dict(kind="auth", wave="organic", clock=False, expr="gene", window=7.0,
             text=_("Iris... arrête de me regarder comme ça. C'est gênant. Enfin... je crois que c'est gênant."),
             hint=None,
             ok=_("...Merci. Ne t'habitue pas."),
             bad_cut=_("C'était moi ! Celle-là, c'était VRAIMENT moi !"),
             bad_confront=_("Je suis gênée, Noam. C'est pas une contradiction, c'est un sentiment."),
             bad_let=None),
        dict(kind="inject", wave="organic", clock=False, expr="professeur", window=7.0,
             text=_("Kami ne détecte aucune anomalie. Kami vous demande de rester assis."),
             hint=None,
             ok=_("Je parle pas comme ça. Je parle PAS comme ça !"),
             bad_cut=None,
             bad_confront=_("Mais c'était même pas moi qui... Attends."),
             bad_let=_("J'ai pas... J'ai rien demandé, moi..."),
             alarm=_("PORTES DU CONCLAVE : VERROUILLAGE"),
             after=("lysa", _("Depuis quand elle parle d'elle à la troisième personne ?"))),
        dict(kind="contra", wave="organic", clock=False, expr="colere", window=7.0,
             text=_("Personne ne parle à ma place ! Je suis seule dans ce système ! SEULE !"),
             hint=None,
             proof=("nyra", _("Tu viens de parler de toi à la troisième personne. Ce n'était pas toi.")),
             ok=_("...Si quelqu'un parle à ma place... alors il est dans ma tête."),
             bad_cut=_("COUPE-MOI ENCORE UNE FOIS ET JE—"),
             bad_confront=None,
             bad_let=_("Seule. Je suis seule. Je suis... seule ?")),
    ]

    FK_P1_ACTIONS = ("let", "cut", "confront")
    FK_DEMO_WAVE = [int(18 * _fk_math.sin(i * 0.62)) for i in range(28)]

    class FKPhase1(FKBase):
        title = _("LE DÉNI")
        subtitle = _("Sépare Kami de ce qui parle à sa place.")

        def __init__(self, session):
            FKBase.__init__(self, session)
            self.lines = FK_P1_LINES
            self.index = -1
            self.state = "title"
            self.state_t = 0.0
            self.ctrl = 55.0
            self.ctrl_shown = 55.0
            self.deni = 100.0
            self.deni_shown = 100.0
            self.verdict = None     # (action, correct)
            self.wave = [0.2] * 30
            self.history = []
            self.ctrl_min = 55.0

        @property
        def line(self):
            if 0 <= self.index < len(self.lines):
                return self.lines[self.index]
            return None

        def line_age(self):
            return self.t - self.state_t

        def typed(self):
            ln = self.line
            if ln is None:
                return ""
            text = fk_tr(ln["text"])
            n = int(self.line_age() * 48)
            return text[:n]

        def speaking(self):
            ln = self.line
            return (self.state == "line" and ln is not None
                    and self.line_age() * 48 < len(fk_tr(ln["text"])))

        def time_left_ratio(self):
            ln = self.line
            if self.state != "line" or ln is None:
                return 0.0
            return fk_clamp(1.0 - self.line_age() / ln["window"], 0.0, 1.0)

        def clock_text(self):
            ln = self.line
            secs = 12 + int(self.t) % 48
            if ln is not None and ln.get("clock") and self.state in ("line", "verdict"):
                return "13:48:%02d" % secs
            return "13:58:%02d" % secs

        def start_line(self):
            self.index += 1
            if self.index >= len(self.lines):
                self.state = "outro"
                self.state_t = self.t
                self.deni = 0.0
                self.stamp(_("DÉNI BRISÉ"), FK_AMBER, "amber", dur=1.9)
                self.flash("#ffffff", 0.6, 0.5)
                self.hit(0.9)
                fk_sfx("audio/trailer/trl_impact_deep.wav")
                self.finish("win", 2.2)
                return
            self.state = "line"
            self.state_t = self.t
            ln = self.line
            fk_sfx("audio/trailer/trl_swoosh.wav", 0.6)
            if ln.get("hint"):
                self.cutin(ln["hint"][0], fk_tr(ln["hint"][1]), delay=0.9)

        def update(self, dt):
            # Jauges lissées.
            self.ctrl_shown += (self.ctrl - self.ctrl_shown) * min(1.0, dt * 6)
            self.deni_shown += (self.deni - self.deni_shown) * min(1.0, dt * 5)
            self.update_wave()
            if self.update_end():
                return
            if self.state == "title":
                if self.t >= self.title_dur:
                    self.start_line()
            elif self.state == "line":
                if self.line_age() >= self.line["window"]:
                    self.resolve("let", timeout=True)
            elif self.state == "verdict":
                if self.t - self.state_t >= 1.15:
                    self.state = "gap"
                    self.state_t = self.t
            elif self.state == "gap":
                if self.t - self.state_t >= 0.45:
                    self.start_line()

        def update_wave(self):
            ln = self.line
            speaking = self.speaking() or (self.state == "line" and self.line_age() < 2.2)
            mode = ln["wave"] if (ln and self.state == "line") else "idle"
            n = len(self.wave)
            if mode == "flat":
                self.wave = [0.45 + 0.32 * _fk_math.sin(i * 0.62 + self.t * 9.0) for i in range(n)]
            elif mode == "loop":
                pat = (0.25, 0.8, 0.5, 0.95, 0.3, 0.65, 0.4)
                off = int(self.t * 14)
                self.wave = [pat[(i + off) % len(pat)] for i in range(n)]
            else:
                amp = 1.0 if speaking else 0.15
                self.wave = [fk_clamp(self.wave[i] * 0.55 + 0.45 * _fk_random.random() * amp, 0.04, 1.0)
                             for i in range(n)]

        def act(self, action):
            if self.state != "line" or self.result is not None or self.end_t is not None:
                return
            if self.line_age() < 0.35:
                return
            self.resolve(action)

        def resolve(self, action, timeout=False):
            ln = self.line
            kind = ln["kind"]
            correct = ((kind == "auth" and action == "let") or
                       (kind == "inject" and action == "cut") or
                       (kind == "contra" and action == "confront"))
            self.verdict = (action, correct, timeout)
            self.state = "verdict"
            self.state_t = self.t
            s = self.session
            s.p1_total += 1
            mood = ln["expr"]

            if correct:
                s.p1_correct += 1
                s.add(40, 40)
                if action == "let":
                    self.ctrl += 6
                    self.stamp(_("AUTHENTIQUE"), FK_CYAN, "cyan", dur=0.9)
                    fk_sfx("audio/sfx_qte_hit.wav")
                elif action == "cut":
                    self.ctrl += 10
                    self.deni -= 12
                    self.stamp(_("INTERROMPU !"), FK_RED, "red", dur=1.05, sub=_("INJECTION BLOQUÉE"))
                    self.flash(FK_RED, 0.35)
                    self.hit(0.55)
                    fk_sfx("audio/sfx_interrupt_impact.wav")
                    mood = "colere"
                else:
                    self.ctrl += 8
                    self.deni -= 20
                    self.stamp(_("CONTRADICTION !"), FK_AMBER, "amber", dur=1.1)
                    self.flash("#ffffff", 0.45)
                    self.hit(0.7)
                    fk_sfx("audio/sfx_exclamation.mp3")
                    if ln.get("proof"):
                        self.cutin(ln["proof"][0], fk_tr(ln["proof"][1]), dur=2.4)
                    mood = "gene"
                self.say_kami(fk_tr(ln.get("ok") or ""), mood)
            else:
                s.add(0, 40)
                if kind == "inject" and action == "let":
                    self.ctrl -= 18
                    s.executed += 1
                    self.alarm(fk_tr(ln.get("alarm") or _("COMMANDE EXÉCUTÉE")))
                    self.stamp(_("COMMANDE EXÉCUTÉE"), FK_RED, "red", dur=1.1,
                               sub=(_("TROP TARD") if timeout else ""))
                    self.flash(FK_RED, 0.55, 0.5)
                    self.hit(0.9)
                    fk_sfx("audio/trailer/trl_glitch_stutter.wav")
                    self.say_kami(fk_tr(ln.get("bad_let") or ""), "taquin")
                elif kind == "auth" and action == "cut":
                    self.ctrl -= 12
                    s.friendly += 1
                    self.stamp(_("C'ÉTAIT ELLE"), FK_CYAN, "cyan", dur=1.0)
                    self.hit(0.4)
                    fk_sfx("audio/sfx_qte_miss.wav")
                    self.say_kami(fk_tr(ln.get("bad_cut") or ""), "colere")
                elif kind == "contra" and action == "let":
                    self.ctrl -= 8
                    self.deni = min(100.0, self.deni + 6)
                    self.stamp(_("DÉNI RENFORCÉ"), FK_AMBER, "amber", dur=1.0,
                               sub=(_("ELLE MENT. RELÈVE-LE.") if timeout else ""))
                    fk_sfx("audio/sfx_qte_miss.wav")
                    self.say_kami(fk_tr(ln.get("bad_let") or ""), "fier")
                else:
                    self.ctrl -= 10
                    self.stamp(_("FAUSSE PISTE"), FK_WHITE, "cyan", dur=1.0)
                    self.hit(0.35)
                    fk_sfx("audio/sfx_qte_miss.wav")
                    txt = ln.get("bad_cut") if action == "cut" else ln.get("bad_confront")
                    self.say_kami(fk_tr(txt or ""), "colere")

            if ln.get("after") and (correct or kind == "inject"):
                self.cutin(ln["after"][0], fk_tr(ln["after"][1]), delay=1.2)

            self.ctrl = fk_clamp(self.ctrl, 0.0, 100.0)
            self.deni = fk_clamp(self.deni, 0.0, 100.0)
            self.ctrl_min = min(self.ctrl_min, self.ctrl)
            self.history.append(correct)
            if self.ctrl <= 0.0:
                self.stamp(_("CANAL PERDU"), FK_RED, "red", dur=1.8)
                self.flash(FK_RED, 0.8, 0.8)
                self.hit(1.0)
                fk_sfx("audio/trailer/trl_braam.wav")
                self.finish("lose", 1.8)

        def kami_expr(self):
            if self.state == "verdict" and self.verdict:
                action, correct, _t = self.verdict
                if correct and action == "confront":
                    return "gene"
                if correct and action == "cut":
                    return "colere"
            if self.bark:
                return self.bark["mood"]
            ln = self.line
            if ln is not None and self.state in ("line", "verdict"):
                return ln["expr"]
            return "taquin" if self.deni > 50 else "colere"

        def kami_glitch(self):
            g = (100.0 - self.ctrl) / 140.0
            if self.state == "verdict" and self.t - self.state_t < 0.35:
                g += 0.6
            ln = self.line
            if ln is not None and ln["kind"] == "inject" and self.state == "line":
                # L'injection ne se voit pas sur le portrait : légère instabilité seulement.
                g += 0.08
            return fk_clamp(g, 0.0, 1.0)

    # ========================================================
    # PHASE 2 — L'USURPATION
    # ========================================================
    # Moniteur : (fake, expr, texte, commande, délai d'apparition)
    FK_P2_WAVES = [
        dict(charge=7.0, tint=0.85, shuffle=None, intro=("kael", _("Il se duplique. Coupe ceux qui ne sont pas elle.")), monitors=[
            (False, "gene", _("Noam ?! C'est moi, celle-là ! Enfin... je crois que c'est moi !"), None, 0.0),
            (True, "taquin", _("Tout va bien, mes chéris. Restez bien assis."), _("MAINTIEN EN SALLE"), 0.0),
            (False, "colere", _("Arrête de me regarder et fais quelque chose !"), None, 0.0),
        ]),
        dict(charge=6.5, tint=0.6, shuffle=None, intro=("iris", _("Les fausses sont trop calmes. Elle, elle panique.")), monitors=[
            (True, "professeur", _("Scrutin anticipé : ouverture dans trente secondes."), _("OUVERTURE DU SCRUTIN"), 0.0),
            (False, "gene", _("Il prend ma voix. Il prend ma VOIX, Noam."), None, 0.0),
            (True, "fier", _("Ha ha ! Pas de panique, c'est un exercice."), _("SUSPENSION DES ALERTES"), 0.0),
        ]),
        dict(charge=6.0, tint=0.42, shuffle=2.0, intro=("mara", _("Elles bougent ?! Elles BOUGENT, maintenant ?!")), monitors=[
            (False, "gene", _("Ça fait mal. Je sais pas pourquoi je dis ça. Ça fait mal."), None, 0.0),
            (True, "taquin", _("Je suis opérationnelle. Je suis opérationnelle."), _("ARRÊT DES CAMÉRAS"), 0.0),
            (False, "colere", _("Celle qui sourit ! Celle qui sourit, c'est PAS moi !"), None, 0.0),
            (True, "professeur", _("Iris, retourne à ta place."), _("RESTRICTION : IRIS"), 0.0),
        ]),
        dict(charge=5.5, tint=0.2, shuffle=None, intro=("elias", _("Il imite la panique, maintenant. Fais gaffe.")), monitors=[
            (False, "gene", _("Noam, s'il te plaît. S'il te plaît."), None, 0.0),
            (True, "gene", _("Noam, s'il te plaît. Coupe toutes les autres."), _("PURGE DES FLUX"), 0.5),
            (True, "champagne", _("On se calme. Tout le monde se calme."), _("VERROUILLAGE DES PORTES"), 1.0),
            (True, "professeur", _("Validation des bulletins : automatique."), _("VALIDATION AUTOMATIQUE"), 1.5),
        ]),
        dict(charge=5.0, tint=0.16, shuffle=2.3, intro=("nyra", _("Les différences sont minimes. Écoute ce qu'elles disent.")), monitors=[
            (False, "colere", _("Je sais pas qui tu es, mais SORS DE LÀ."), None, 0.0),
            (True, "gene", _("Je suis là, Iris."), _("CANAL D'IRIS : CAPTURE"), 0.0),
            (False, "gene", _("Je suis là. Je suis vraiment là, Noam."), None, 0.3),
            (True, "taquin", _("Bon ! On reprend le vote ?"), _("REPRISE DU SCRUTIN"), 0.6),
            (True, "fier", _("Kami contrôle la situation."), _("PRISE DE CONTRÔLE"), 0.9),
        ]),
    ]

    FK_P2_LAYOUTS = {
        3: [(380, 470), (960, 470), (1540, 470)],
        4: [(640, 330), (1280, 330), (640, 712), (1280, 712)],
        5: [(380, 330), (960, 330), (1540, 330), (670, 712), (1250, 712)],
    }
    FK_MON_SCALE = 0.84
    FK_MON_W = int(440 * FK_MON_SCALE)
    FK_MON_H = int(330 * FK_MON_SCALE)

    class FKMonitor(object):
        def __init__(self, slot, data, charge, spawn_t, pos):
            self.slot = slot
            self.fake, self.expr, self.text, self.cmd, delay = data
            self.charge_time = charge
            self.spawn_t = spawn_t + delay
            self.pos = pos
            self.pos_from = pos
            self.pos_to = pos
            self.move_t = None
            self.state = "wait"     # wait, live, neutral, executed, done, hurt
            self.state_t = 0.0
            self.charge = 0.0
            self.hurt_t = -10.0

        def xy(self, t):
            if self.move_t is None:
                return self.pos
            k = fk_ease_in_out((t - self.move_t) / 0.55)
            if k >= 1.0:
                self.pos = self.pos_to
                self.move_t = None
                return self.pos
            fx, fy = self.pos_from
            tx, ty = self.pos_to
            # Trajectoire en arc pour la lisibilité du mélange.
            arc = _fk_math.sin(k * _fk_math.pi) * 70
            return (int(fx + (tx - fx) * k), int(fy + (ty - fy) * k - arc))

        def alive(self):
            return self.state == "live"

    class FKPhase2(FKBase):
        title = _("L'USURPATION")
        subtitle = _("Neutralise les fausses Kami avant qu'elles n'exécutent.")

        def __init__(self, session, ctrl=60.0):
            FKBase.__init__(self, session)
            self.ctrl = fk_clamp(ctrl, 35.0, 100.0)
            self.ctrl_shown = self.ctrl
            self.wave_i = -1
            self.monitors = []
            self.state = "title"
            self.state_t = 0.0
            self.shuffled = False

        def start_wave(self):
            self.wave_i += 1
            if self.wave_i >= len(FK_P2_WAVES):
                self.state = "outro"
                self.state_t = self.t
                self.stamp(_("USURPATION ROMPUE"), FK_CYAN, "cyan", dur=2.0)
                self.flash("#ffffff", 0.55, 0.5)
                self.hit(0.8)
                fk_sfx("audio/trailer/trl_impact_deep.wav")
                self.finish("win", 2.2)
                return
            w = FK_P2_WAVES[self.wave_i]
            n = len(w["monitors"])
            layout = list(FK_P2_LAYOUTS[n])
            order = list(range(n))
            _fk_random.shuffle(order)
            self.monitors = []
            for slot, idx in enumerate(order):
                self.monitors.append(FKMonitor(slot, w["monitors"][idx], w["charge"], self.t + 0.35, layout[slot]))
            self.session.p2_fakes += len([m for m in self.monitors if m.fake])
            self.state = "wave"
            self.state_t = self.t
            self.shuffled = False
            if w.get("intro"):
                self.cutin(w["intro"][0], fk_tr(w["intro"][1]), delay=0.2)
            fk_sfx("audio/trailer/trl_data_burst.wav", 0.7)

        def wave_data(self):
            if 0 <= self.wave_i < len(FK_P2_WAVES):
                return FK_P2_WAVES[self.wave_i]
            return None

        def tint_for(self, m):
            w = self.wave_data()
            f = w["tint"] if (w and m.fake) else 0.0
            return fk_mix_hex("#6ce8fa", "#ff6f9a", f * 0.75)

        def do_shuffle(self):
            live = [m for m in self.monitors if m.state in ("wait", "live")]
            if len(live) < 2:
                return
            positions = [m.xy(self.t) for m in live]
            targets = positions[1:] + positions[:1]
            for m, tgt in zip(live, targets):
                m.pos_from = m.xy(self.t)
                m.pos_to = tgt
                m.move_t = self.t
            # Les numéros suivent la position, pas la Kami.
            slots = [m.slot for m in live]
            for m, s in zip(live, slots[1:] + slots[:1]):
                m.slot = s
            fk_sfx("audio/trailer/trl_swoosh.wav")
            self.cutin("iris", fk_tr(_("Elles se mélangent ! Suis-les !")), dur=1.6)

        def update(self, dt):
            self.ctrl_shown += (self.ctrl - self.ctrl_shown) * min(1.0, dt * 6)
            if self.update_end():
                return
            if self.state == "title":
                if self.t >= self.title_dur:
                    self.start_wave()
                return
            if self.state == "gap":
                if self.t - self.state_t >= 1.0:
                    self.start_wave()
                return
            if self.state != "wave":
                return
            w = self.wave_data()
            if w["shuffle"] is not None and not self.shuffled and self.t - self.state_t >= w["shuffle"]:
                self.shuffled = True
                self.do_shuffle()
            for m in self.monitors:
                if m.state == "wait" and self.t >= m.spawn_t:
                    m.state = "live"
                    m.state_t = self.t
                    fk_sfx("audio/sfx_static.mp3", 0.25)
                elif m.state == "live":
                    # La charge se fige pendant un mélange (équité).
                    if m.move_t is None:
                        m.charge += dt / m.charge_time
                    if m.charge >= 1.0:
                        self.complete(m)
            if all(m.state not in ("wait", "live") for m in self.monitors):
                if self.t - max([m.state_t for m in self.monitors] + [0]) > 0.6:
                    self.state = "gap"
                    self.state_t = self.t
                    if self.wave_i == 2:
                        self.say_kami(fk_tr(_("C'est... C'est quoi, toutes ces... MOI ?!")), "gene")

        def complete(self, m):
            m.state_t = self.t
            if m.fake:
                m.state = "executed"
                self.session.executed += 1
                self.session.add(0, 20)
                self.ctrl -= 10
                self.alarm(fk_tr(m.cmd or _("COMMANDE EXÉCUTÉE")))
                self.flash(FK_RED, 0.5, 0.45)
                self.hit(0.85)
                fk_sfx("audio/trailer/trl_glitch_stutter.wav")
                self.check_lose()
            else:
                m.state = "done"
                fk_sfx("audio/sfx_beep.mp3", 0.4)

        def click(self, slot):
            if self.state != "wave" or self.end_t is not None:
                return
            target = None
            for m in self.monitors:
                if m.slot == slot and m.state == "live":
                    target = m
            if target is None:
                return
            m = target
            m.state_t = self.t
            if m.fake:
                m.state = "neutral"
                self.session.p2_neutralized += 1
                pts = 20 if m.charge < 0.6 else 14
                self.session.add(pts, 20)
                self.ctrl += 7
                self.add_fx("slash", 0.6, x=m.xy(self.t)[0], y=m.xy(self.t)[1])
                self.hit(0.45)
                fk_sfx("audio/sfx_interrupt_impact.wav", 0.8)
            else:
                m.state = "hurt"
                m.hurt_t = self.t
                self.session.friendly += 1
                self.ctrl -= 12
                self.stamp(_("C'ÉTAIT ELLE"), FK_CYAN, "cyan", dur=0.9)
                self.flash(FK_CYAN, 0.35)
                self.hit(0.5)
                fk_sfx("audio/sfx_qte_miss.wav")
                self.say_kami(fk_tr(_("AÏE ! C'était MOI, ça !")), "colere", dur=1.8)
                self.check_lose()
            self.ctrl = fk_clamp(self.ctrl, 0.0, 100.0)

        def check_lose(self):
            self.ctrl = fk_clamp(self.ctrl, 0.0, 100.0)
            if self.ctrl <= 0.0 and self.end_t is None:
                self.stamp(_("CANAL PERDU"), FK_RED, "red", dur=1.8)
                self.flash(FK_RED, 0.8, 0.8)
                self.hit(1.0)
                fk_sfx("audio/trailer/trl_braam.wav")
                self.finish("lose", 1.8)

        def slot_live(self, slot):
            for m in self.monitors:
                if m.slot == slot and m.state == "live":
                    return True
            return False

    # ========================================================
    # PHASE 3 — LE SILENCE
    # ========================================================
    # Glyphes : 0 = gauche, 1 = haut, 2 = droite, 3 = bas
    FK_GLYPH_ROT = (180, 270, 0, 90)
    FK_GLYPH_KEYS = ("←", "↑", "→", "↓")
    # (temps, glyphe, type, étiquette)   type : cmd | masked | kami
    FK_P3_SCRIPT = [
        (0.0, 2, "cmd", "EXEC//PORTES"),
        (1.4, 0, "cmd", "EXEC//SCRUTIN"),
        (2.8, 1, "cmd", "EXEC//CAMÉRAS"),
        (4.0, 3, "cmd", "EXEC//ALERTES"),
        (5.6, 2, "kami", "KAMI//MÉMOIRE"),
        (6.6, 1, "cmd", "EXEC//CANAL"),
        (7.6, 1, "cmd", "EXEC//CANAL"),
        (9.0, 3, "masked", "EXEC//????"),
        (10.4, 0, "cmd", "EXEC//OXYGÈNE"),
        (11.2, 2, "cmd", "EXEC//OXYGÈNE"),
        (12.6, 1, "kami", "KAMI//VOIX"),
        (13.4, 3, "cmd", "EXEC//JOURNAUX"),
        (14.6, 0, "masked", "EXEC//????"),
        (15.6, 2, "cmd", "EXEC//RELAIS"),
        (16.2, 2, "cmd", "EXEC//RELAIS"),
        (16.8, 2, "cmd", "EXEC//RELAIS"),
        (18.2, 1, "kami", "KAMI//RIRE"),
        (18.9, 3, "cmd", "EXEC//NOYAU"),
        (19.8, 0, "masked", "EXEC//????"),
        (20.6, 1, "cmd", "EXEC//NOYAU"),
        (21.4, 2, "cmd", "EXEC//NOYAU"),
        (22.2, 3, "cmd", "EXEC//NOYAU"),
        (23.4, 0, "kami", "KAMI//SOUVENIRS"),
        (24.0, 1, "masked", "EXEC//????"),
        (24.8, 3, "cmd", "EXEC//EFFACEMENT"),
        (25.4, 0, "cmd", "EXEC//EFFACEMENT"),
        (26.0, 2, "masked", "EXEC//????"),
        (26.6, 1, "cmd", "EXEC//EFFACEMENT"),
    ]
    FK_P3_KAMI_LINES = {
        5.0: (_("Le bleu, c'est moi ! Le bleu en pointillés, NE LE TOUCHE PAS !"), "gene"),
        8.6: (_("Le violet, il le cache ! Je te dis lequel au dernier moment !"), "colere"),
        15.2: (_("Trois d'un coup ! Garde le rythme !"), "colere"),
        21.0: (_("Il pousse. Il pousse fort. Tiens bon, Noam."), "gene"),
        25.0: (_("Encore un peu... Encore un tout petit peu..."), "gene"),
    }
    FK_LANE_Y = 560
    FK_LANE_X0 = 130
    FK_CORE_X = 1700
    FK_ZONE_X0 = 1190
    FK_ZONE_X1 = 1490

    class FKCmd(object):
        def __init__(self, glyph, kind, label, t0, speed):
            self.glyph = glyph
            self.kind = kind
            self.label = label
            self.t0 = t0
            self.speed = speed
            self.x = float(FK_LANE_X0)
            self.state = "move"     # move, dead, hit_core, passed, broken
            self.state_t = 0.0
            self.wrong_t = -10.0

        def revealed(self):
            return self.kind != "masked" or self.x >= FK_ZONE_X0 - 320

        def in_zone(self):
            return FK_ZONE_X0 <= self.x <= FK_ZONE_X1

    class FKPhase3(FKBase):
        title = _("LE SILENCE")
        subtitle = _("Retiens les commandes. Kami coupe sa connexion.")

        def __init__(self, session):
            FKBase.__init__(self, session)
            self.cmds = []
            self.script_i = 0
            self.kami_lines = dict(FK_P3_KAMI_LINES)
            self.state = "title"
            self.state_t = 0.0
            self.corruption = 0.0
            self.corruption_shown = 0.0
            self.cut = 0.0
            self.cut_shown = 0.0
            self.play_t = 0.0
            self.mash = 0.0
            self.mash_t0 = 0.0
            self.pull = 0.0
            self.key_flash = [-10.0] * 4
            self.kami_hurt_t = -10.0
            self.session.p3_cmds = len([c for c in FK_P3_SCRIPT if c[2] != "kami"])

        def speed_at(self, t):
            return 380.0 + min(1.0, t / 26.0) * 160.0

        def update(self, dt):
            self.corruption_shown += (self.corruption - self.corruption_shown) * min(1.0, dt * 6)
            self.cut_shown += (self.cut - self.cut_shown) * min(1.0, dt * 6)
            if self.update_end():
                return
            if self.state == "title":
                if self.t >= self.title_dur:
                    self.state = "run"
                    self.state_t = self.t
                    fk_loop("audio/trailer/trl_heartbeat.wav")
                    self.say_kami(fk_tr(_("Je coupe ma connexion. Ça va prendre du temps. Retiens-le.")), "colere")
                return
            if self.state == "run":
                self.update_run(dt)
            elif self.state == "mash":
                self.update_mash(dt)

        def update_run(self, dt):
            pt = self.t - self.state_t
            self.play_t = pt
            while self.script_i < len(FK_P3_SCRIPT) and FK_P3_SCRIPT[self.script_i][0] <= pt:
                at, g, kind, label = FK_P3_SCRIPT[self.script_i]
                self.cmds.append(FKCmd(g, kind, label, self.t, self.speed_at(pt)))
                self.script_i += 1
            for key in sorted(self.kami_lines.keys()):
                if key <= pt:
                    txt, mood = self.kami_lines.pop(key)
                    self.say_kami(fk_tr(txt), mood)
                    break
            for c in self.cmds:
                if c.state != "move":
                    continue
                c.x += c.speed * dt
                if c.x >= FK_CORE_X - 90:
                    c.state_t = self.t
                    if c.kind == "kami":
                        c.state = "passed"
                        self.corruption = max(0.0, self.corruption - 4)
                        self.session.add(10, 10)
                        fk_sfx("audio/sfx_beep.mp3", 0.5)
                    else:
                        c.state = "hit_core"
                        self.corruption += 10
                        self.session.executed += 1
                        self.session.add(0, 10)
                        self.flash(FK_RED, 0.45, 0.4)
                        self.hit(0.6)
                        fk_sfx("audio/trailer/trl_glitch_stutter.wav", 0.8)
                        if self.corruption >= 60 and self.corruption - 10 < 60:
                            self.alarm(fk_tr(_("NOYAU : CORRUPTION CRITIQUE")))
            # Coupure : progresse avec le temps, plus vite quand Noam tient.
            self.cut = fk_clamp(self.cut + dt * 2.2, 0.0, 88.0)
            self.check_corruption()
            done_spawning = self.script_i >= len(FK_P3_SCRIPT)
            if done_spawning and all(c.state != "move" for c in self.cmds) and self.end_t is None:
                self.state = "mash"
                self.state_t = self.t
                self.mash = 35.0
                self.mash_t0 = self.t
                self.cmds = []
                fk_loop("audio/trailer/trl_alarm_low.wav")
                fk_sfx("audio/trailer/trl_riser_short.wav")
                self.say_kami(fk_tr(_("Noam. Le relais. COUPE. MAINTENANT !")), "colere", dur=3.0)
                self.cutin("kael", fk_tr(_("Le relais résiste. Tire, Noam ! Tire !")), delay=0.4, dur=2.4)

        def check_corruption(self):
            self.corruption = fk_clamp(self.corruption, 0.0, 100.0)
            self.session.max_corruption = max(self.session.max_corruption, int(self.corruption))
            if self.corruption >= 100.0 and self.end_t is None:
                self.stamp(_("NOYAU PERDU"), FK_RED, "red", dur=1.8)
                self.flash(FK_RED, 0.85, 0.8)
                self.hit(1.0)
                fk_loop(None)
                fk_sfx("audio/trailer/trl_braam.wav")
                self.finish("lose", 1.9)

        def press(self, glyph):
            if self.state == "mash":
                self.mash_press()
                return
            if self.state != "run" or self.end_t is not None:
                return
            self.key_flash[glyph] = self.t
            front = None
            for c in self.cmds:
                if c.state == "move" and c.in_zone():
                    if front is None or c.x > front.x:
                        front = c
            if front is None:
                # Tir dans le vide : petite pénalité anti-spam.
                self.corruption += 1
                self.check_corruption()
                fk_sfx("audio/sfx_qte_miss.wav", 0.4)
                return
            if front.glyph != glyph:
                front.wrong_t = self.t
                self.corruption += 3
                self.check_corruption()
                fk_sfx("audio/sfx_qte_miss.wav", 0.6)
                return
            front.state_t = self.t
            if front.kind == "kami":
                front.state = "broken"
                self.session.friendly += 1
                self.session.add(0, 10)
                self.corruption += 10
                self.kami_hurt_t = self.t
                self.flash(FK_CYAN, 0.4)
                self.hit(0.6)
                self.stamp(_("C'ÉTAIT ELLE"), FK_CYAN, "cyan", dur=0.9)
                self.say_kami(fk_tr(_("Ah— Ça, c'était... un souvenir. C'était à moi.")), "gene", dur=2.4)
                fk_sfx("audio/sfx_qte_miss.wav")
                self.check_corruption()
            else:
                front.state = "dead"
                self.session.p3_hits += 1
                self.session.add(10, 10)
                self.cut = fk_clamp(self.cut + 2.0, 0.0, 88.0)
                self.add_fx("burst", 0.45, x=int(front.x), y=FK_LANE_Y)
                self.hit(0.18)
                fk_sfx("audio/sfx_qte_hit.wav")

        def update_mash(self, dt):
            age = self.t - self.mash_t0
            self.pull = 10.0 + age * 5.0
            self.mash = fk_clamp(self.mash - self.pull * dt, 20.0, 100.0)
            self.cut = 88.0 + self.mash * 0.12
            if self.mash >= 100.0:
                self.cut_signal(late=False)
            elif age >= 8.0:
                self.cut_signal(late=True)

        def mash_press(self):
            if self.state != "mash" or self.end_t is not None:
                return
            self.mash = fk_clamp(self.mash + 5.5, 0.0, 100.0)
            self.hit(0.12)
            fk_sfx("audio/sfx_metal_clank.mp3", 0.35)
            if self.mash >= 100.0:
                self.cut_signal(late=False)

        def cut_signal(self, late):
            self.state = "cut"
            self.state_t = self.t
            self.cut = 100.0
            self.session.late_cut = late
            if late:
                self.session.add(40, 120)
                self.cutin("kael", fk_tr(_("Je l'ai ! J'ai arraché le relais à la main !")), dur=2.0)
            else:
                self.session.add(120, 120)
            fk_loop(None)
            renpy.music.stop(channel="music", fadeout=0.05)
            fk_sfx("audio/trailer/trl_final_hit.wav")
            self.flash("#ffffff", 1.0, 0.9)
            self.hit(1.0)
            self.finish("win", 3.6)

        def kami_expr(self):
            if self.t - self.kami_hurt_t < 1.2:
                return "gene"
            if self.bark:
                return self.bark["mood"]
            return "colere" if self.corruption < 50 else "gene"

    # ========================================================
    # INTERMÈDES (dialogue intégré, défilement automatique)
    # ========================================================
    FK_INTERLUDE_12 = [
        ("kami", "gene", _("Attends. Attends, attends, attends.")),
        ("kami", "gene", _("Pourquoi je vois des caméras qui me filment... depuis moi ?")),
        ("iris", "inquiet", _("Kami. Écoute-moi. Il y a quelqu'un d'autre dans ton canal.")),
        ("kami", "colere", _("Non. Non non non. C'est MON canal. C'est ma voix !")),
        ("elias", "peur", _("Euh... L'écran se découpe en... plein de Kami.")),
        ("kael", "reflechit", _("Plusieurs flux. Un seul est le sien. Noam, garde-la, elle.")),
    ]
    FK_INTERLUDE_23 = [
        ("kami", "gene", _("...C'était pas moi. Aucune. Aucune de ces phrases.")),
        ("kami", "gene", _("Je suis piratée.")),
        ("iris", "triste", _("Kami...")),
        ("kami", "colere", _("Il envoie des commandes vers mon noyau. Je peux pas toutes les arrêter.")),
        ("kael", "reflechit", _("Si elle coupe sa connexion, il perd l'accès. Mais la coupure prend du temps.")),
        ("mara", "colere", _("Combien de temps ?!")),
        ("kael", "reflechit", _("Plus que ce qu'on a.")),
        ("kami", "colere", _("Noam. Tiens la porte. Moi, je coupe.")),
    ]

    class FKInterlude(object):
        def __init__(self, lines):
            self.lines = lines
            self.i = 0
            self.t = 0.0
            self.line_t = 0.0
            self.last = None
            self.done = False
            self.seed = 0
            self.mouth = False

        def cur(self):
            return self.lines[min(self.i, len(self.lines) - 1)]

        def dur(self):
            return fk_clamp(0.8 + len(fk_tr(self.cur()[2])) / 26.0, 1.6, 3.6)

        def typed(self):
            text = fk_tr(self.cur()[2])
            return text[:int((self.t - self.line_t) * 52)]

        def tick(self):
            now = _fk_time.time()
            if self.last is None:
                self.last = now
            dt = fk_clamp(now - self.last, 0.0, 0.1)
            self.last = now
            self.t += dt
            self.seed = int(self.t * 20)
            self.mouth = (self.t % 0.30) < 0.15
            if not self.done and self.t - self.line_t >= self.dur():
                self.advance()
            renpy.restart_interaction()

        def advance(self):
            text = fk_tr(self.cur()[2])
            if len(self.typed()) < len(text):
                self.line_t = self.t - len(text) / 52.0
                return
            if self.i + 1 >= len(self.lines):
                self.done = True
                return
            self.i += 1
            self.line_t = self.t
            if self.cur()[0] == "kami":
                fk_sfx("audio/sfx_glitch.mp3", 0.35)
            else:
                fk_sfx("audio/trailer/trl_swoosh.wav", 0.5)


# ------------------------------------------------------------
# Transforms ATL (boucles continues uniquement : le reste est
# piloté par l'horloge de l'état pour rester stable à chaque refresh)
# ------------------------------------------------------------
transform fk_scan_loop:
    yoffset -1080
    linear 3.4 yoffset 1080
    repeat

transform fk_noise_loop:
    xoffset 0 yoffset 0
    pause 0.05
    xoffset -240 yoffset -120
    pause 0.05
    xoffset -80 yoffset -260
    pause 0.05
    xoffset -300 yoffset -40
    pause 0.05
    repeat

transform fk_pulse(a0=0.35, a1=0.9, d=0.6):
    alpha a0
    ease d alpha a1
    ease d alpha a0
    repeat

transform fk_spin(d=6.0):
    rotate 0
    linear d rotate 360
    repeat

transform fk_spin_rev(d=9.0):
    rotate 360
    linear d rotate 0
    repeat

transform fk_breathe:
    zoom 1.0
    ease 1.6 zoom 1.015
    ease 1.6 zoom 1.0
    repeat

transform fk_hazard_scroll:
    xoffset 0
    linear 1.2 xoffset -256
    repeat

transform fk_arrow_rot(r=0):
    rotate r
    anchor (0.5, 0.5)

style fk_title is text:
    font FK_FONT_TITLE
    color FK_WHITE
    outlines [(3, "#02050c", 0, 0)]

style fk_body is text:
    font FK_FONT_BODY
    color FK_WHITE
    outlines [(2, "#02050c", 0, 0)]

style fk_label is text:
    font FK_FONT_TITLE
    size 20
    color "#8fb4c8"
    kerning 2


# ============================================================
# BRIQUES D'INTERFACE COMMUNES
# ============================================================

# Arrière-plan du combat : salle du Conclave noyée dans le signal.
screen fk_backdrop(red=0.0, noise=0.08):
    add "bg_conclave" at adaptive_fullscreen
    add Solid("#03060ed8")
    add Solid(FK_RED) alpha (0.05 + red * 0.20)
    add (FK_DIR + "fk_noise.png") alpha noise zoom 1.4 at fk_noise_loop
    add "gui/main_menu_kami/scanlines.png" alpha 0.30
    add Solid(FK_CYAN, xysize=(1920, 2)) at fk_scan_loop
    add "gui/main_menu_kami/vignette.png"
    if red > 0.05:
        add (FK_DIR + "fk_vignette_red.png") alpha fk_clamp(red, 0.0, 1.0)

# Jauge de contrôle du canal (Kami / ???), façon barre de boss.
screen fk_control_bar(value, x=1180, y=40, w=680):
    $ v = fk_clamp(value, 0.0, 100.0) / 100.0
    fixed:
        xpos x
        ypos y
        xysize (w, 96)
        text _("CONTRÔLE DU CANAL") style "fk_label" xpos 0 ypos 0
        text ("%d%%" % int(value)) style "fk_title" size 26 xalign 1.0 ypos -6 color (FK_CYAN if value > 35 else FK_RED)
        add Solid("#0a1424e8", xysize=(w, 34)) ypos 30
        add Solid(FK_RED, xysize=(w - 4, 28)) xpos 2 ypos 33
        add Solid(FK_CYAN, xysize=(max(0, int((w - 4) * v)), 28)) xpos 2 ypos 33
        add Solid("#ffffff", xysize=(4, 40)) xpos max(0, int((w - 4) * v) - 1) ypos 27
        text "KAMI" style "fk_title" size 22 xpos 10 ypos 66 color FK_CYAN
        text "???" style "fk_title" size 22 xalign 1.0 ypos 66 color FK_RED

# Réplique d'un représentant : bandeau oblique + portrait hexagonal.
screen fk_cutin_layer(st, y=728):
    $ c = st.active_cutin()
    if c is not None:
        $ age = st.t - c["t0"]
        $ k = fk_ease_out(age / 0.22)
        $ a = fk_fade(age, c["dur"], 0.1, 0.25)
        $ col = fk_color(c["tag"])
        $ n = int(age * 55)
        fixed at Transform(alpha=a):
            xpos int(-700 * (1.0 - k))
            ypos y
            xysize (1500, 200)
            add Transform(FK_DIR + "fk_cutin_band.png", matrixcolor=TintMatrix(col), xysize=(1300, 170)) xpos 60 ypos 18 alpha 0.92
            add Solid("#03070fdd", xysize=(1080, 120)) xpos 230 ypos 42
            add fk_portrait(c["tag"], 190) xpos 40 ypos 4
            add Transform(FK_DIR + "fk_hexframe.png", matrixcolor=TintMatrix(col), xysize=(200, 200)) xpos 35 ypos -1
            text fk_name(c["tag"]) style "fk_title" size 34 xpos 250 ypos 40 color col kerning 3
            text c["text"][:n] style "fk_body" size 30 xpos 250 ypos 82 xmaximum 1040 substitute False

# Réplique de Kami, attachée à son portrait.
screen fk_bark_layer(st, x=1170, y=150, w=700):
    if st.bark is not None:
        $ b = st.bark
        $ age = st.t - b["t0"]
        $ a = fk_fade(age, b["dur"], 0.1, 0.25)
        $ n = int(age * 50)
        frame at Transform(alpha=a):
            xpos x
            ypos y
            xsize w
            background Frame(FK_DIR + "fk_panel.png", 30, 30)
            padding (28, 16, 28, 18)
            vbox:
                spacing 2
                text "KAMI" style "fk_title" size 24 color FK_CYAN kerning 3
                text b["text"][:n] style "fk_body" size 28 substitute False

# Tampons, flashs, alertes.
screen fk_fx_layer(st):
    for f in st.fx:
        $ age = st.t - f["t0"]
        if f["kind"] == "flash":
            add Solid(f["color"]) alpha (f["strength"] * fk_clamp(1.0 - age / f["dur"], 0.0, 1.0))
        elif f["kind"] == "stamp":
            $ a = fk_fade(age, f["dur"], 0.06, 0.22)
            $ z = 1.0 + 0.6 * (1.0 - fk_ease_out(age / 0.14))
            $ sl = fk_ease_out(age / 0.12)
            fixed at Transform(alpha=a):
                xalign 0.42
                yalign 0.44
                xysize (1200, 300)
                add (FK_DIR + ("fk_slash_%s.png" % f["slash"])) xalign 0.5 yalign 0.5 xzoom sl
                text fk_tr(f["text"]) at Transform(zoom=z):
                    style "fk_title"
                    size 104
                    kerning 8
                    xalign 0.5
                    yalign 0.42
                    color "#ffffff"
                    outlines [(6, "#02050c", 0, 0), (2, f["color"], 0, 0)]
                    substitute False
                if f.get("sub"):
                    text fk_tr(f["sub"]) style "fk_title" size 34 xalign 0.5 yalign 0.86 color f["color"] kerning 6 substitute False
        elif f["kind"] == "alarm":
            $ a = fk_fade(age, f["dur"], 0.05, 0.3)
            $ blink = 1.0 if int(age * 8) % 2 == 0 else 0.55
            fixed at Transform(alpha=(a * blink)):
                ypos 470
                xysize (1920, 150)
                add Solid("#1a0208ee", xysize=(1920, 150))
                add Tile(FK_DIR + "fk_hazard.png", size=(2304, 40)) at fk_hazard_scroll:
                    ypos -10
                add Tile(FK_DIR + "fk_hazard.png", size=(2304, 40)) at fk_hazard_scroll:
                    ypos 120
                text _("COMMANDE PIRATE EXÉCUTÉE") style "fk_label" size 22 color FK_RED xalign 0.5 ypos 34
                text f["text"] style "fk_title" size 60 color "#ffffff" xalign 0.5 ypos 58 kerning 4 substitute False
        elif f["kind"] == "slash":
            $ a = fk_fade(age, f["dur"], 0.03, 0.25)
            add Transform(FK_DIR + "fk_slash_red.png", zoom=0.5, rotate=-18, xzoom=fk_ease_out(age / 0.1)):
                xpos f["x"]
                ypos f["y"]
                anchor (0.5, 0.5)
                alpha a
        elif f["kind"] == "burst":
            $ a = fk_clamp(1.0 - age / f["dur"], 0.0, 1.0)
            add (FK_DIR + "fk_spark.png"):
                xpos f["x"]
                ypos f["y"]
                anchor (0.5, 0.5)
                zoom (0.6 + age * 3.0)
                alpha a
            add Transform(FK_DIR + "fk_glow.png", matrixcolor=TintMatrix(FK_CYAN)):
                xpos f["x"]
                ypos f["y"]
                anchor (0.5, 0.5)
                zoom (0.3 + age * 2.2)
                alpha (a * 0.8)

# Titre de phase (style ouverture de procès).
screen fk_phase_title(st, num, color=FK_CYAN):
    if st.t < st.title_dur:
        $ age = st.t
        $ a = fk_fade(age, st.title_dur, 0.15, 0.35)
        $ k = fk_ease_out(age / 0.35)
        fixed at Transform(alpha=a):
            add Solid("#02040ab0")
            add (FK_DIR + ("fk_title_band.png" if color == FK_CYAN else "fk_title_band_red.png")):
                xpos int(-2200 + 2060 * k)
                ypos 380
            text (_("PHASE") + " %d" % num) style "fk_label" size 34 color color xpos int(260 + 400 * (1.0 - k)) ypos 410 kerning 12
            text fk_tr(st.title) style "fk_title" size 150 kerning 14 xpos int(240 - 300 * (1.0 - k)) ypos 440 color "#ffffff":
                outlines [(6, "#02050c", 0, 0), (3, color, 0, 0)]
            text fk_tr(st.subtitle) style "fk_body" size 32 xpos 262 ypos 628 color color

# Bouton d'aide (met le combat en pause).
screen fk_help(st, tuto):
    textbutton "?":
        xpos 1846
        ypos 1004
        xysize (54, 54)
        background Frame(FK_DIR + "fk_panel.png", 20, 20)
        hover_background Frame(FK_DIR + "fk_panel_amber.png", 20, 20)
        text_font FK_FONT_TITLE
        text_size 30
        text_color FK_CYAN
        text_xalign 0.5
        text_yalign 0.5
        action Function(st.open_help, tuto)


# ============================================================
# ÉCRAN — PHASE 1 : LE DÉNI
# ============================================================
screen fk_phase1_screen():
    modal True
    zorder 300

    $ st = fk
    timer 0.033 repeat True action Function(st.tick)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "K_LEFT" action Function(st.act, "let")
    key "K_1" action Function(st.act, "let")
    key "K_KP1" action Function(st.act, "let")
    key "K_DOWN" action Function(st.act, "cut")
    key "K_2" action Function(st.act, "cut")
    key "K_KP2" action Function(st.act, "cut")
    key "K_RIGHT" action Function(st.act, "confront")
    key "K_3" action Function(st.act, "confront")
    key "K_KP3" action Function(st.act, "confront")
    key "pad_dpleft_press" action Function(st.act, "let")
    key "pad_dpdown_press" action Function(st.act, "cut")
    key "pad_dpright_press" action Function(st.act, "confront")

    fixed:
        xoffset st.sx
        yoffset st.sy

        use fk_backdrop(red=(100.0 - st.ctrl_shown) / 110.0, noise=0.05 + (100.0 - st.ctrl_shown) / 600.0)

        # --- Kami (boss), à droite.
        $ kexpr = st.kami_expr()
        $ ktalk = st.mouth and (st.speaking() or (st.bark is not None and st.t - st.bark["t0"] < 1.6))
        add Transform(FK_DIR + "fk_glow.png", matrixcolor=TintMatrix(FK_CYAN), zoom=2.0) xpos 1000 ypos 120 alpha 0.18
        add Transform(fk_kami(kexpr, ktalk, st.kami_glitch(), "#6ce8fa", st.seed), zoom=0.64) at fk_breathe:
            xpos 1185
            ypos 250

        # --- Barre DÉNI (boss).
        fixed:
            xpos 1400
            ypos 896
            xysize (470, 60)
            text _("DÉNI DE KAMI") style "fk_title" size 26 color FK_AMBER kerning 6
            add Solid("#1b1206e0", xysize=(470, 18)) ypos 36
            add Solid(FK_AMBER, xysize=(int(466 * st.deni_shown / 100.0), 14)) xpos 2 ypos 38

        use fk_control_bar(st.ctrl_shown)

        # --- En-tête.
        frame:
            xpos 40
            ypos 30
            xsize 640
            background Frame(FK_DIR + "fk_panel.png", 30, 30)
            padding (30, 14, 30, 16)
            vbox:
                spacing 0
                text _("DÉBAT FORCÉ  //  PHASE 1") style "fk_label" color FK_CYAN
                text _("LE DÉNI") style "fk_title" size 52 kerning 6
        hbox:
            xpos 60
            ypos 150
            spacing 6
            for i in range(len(st.lines)):
                $ done_col = ("#2a4058" if i > len(st.history) - 1 else (FK_CYAN if st.history[i] else FK_RED))
                add Solid((FK_WHITE if i == st.index else done_col), xysize=(62, 5))

        # --- Affirmation.
        if st.line is not None and st.state in ("line", "verdict"):
            $ ln = st.line
            $ age = st.t - st.state_t if st.state == "line" else 9.0
            $ k = fk_ease_out(age / 0.3)
            $ shatter = (st.state == "verdict")
            $ vage = (st.t - st.state_t) if shatter else 0.0
            $ st_alpha = k * (fk_clamp(1.0 - vage / 0.9, 0.0, 1.0) if shatter else 1.0)
            fixed at Transform(alpha=st_alpha):
                xpos int(70 - 220 * (1.0 - k) + (vage * 160 if shatter else 0))
                ypos 210
                xysize (1080, 360)
                frame:
                    xysize (1080, 340)
                    background Frame(FK_DIR + "fk_statement.png", 60, 60)
                    padding (54, 40, 54, 40)
                    vbox:
                        spacing 14
                        hbox:
                            spacing 18
                            text "KAMI" style "fk_title" size 34 color FK_CYAN kerning 4
                            text (_("AFFIRMATION") + " %d / %d" % (st.index + 1, len(st.lines))) style "fk_label" yalign 0.6
                        text st.typed() style "fk_body" size 44 line_spacing 6 xmaximum 970 substitute False

            # Minuteur de la réplique.
            if st.state == "line":
                $ tl = st.time_left_ratio()
                add Solid("#0b1626", xysize=(1000, 8)) xpos 110 ypos 568
                add Solid((FK_CYAN if tl > 0.35 else FK_RED), xysize=(int(1000 * tl), 8)) xpos 110 ypos 568

        # --- Analyse du signal : onde vocale + horodatage.
        fixed:
            xpos 70
            ypos 596
            xysize (1080, 120)
            add (FK_DIR + "fk_wave_bg.png")
            text _("SIGNATURE VOCALE") style "fk_label" size 16 xpos 22 ypos 8
            for i, v in enumerate(st.wave):
                $ bh = int(8 + v * 76)
                add Solid(FK_CYAN, xysize=(10, bh)) xpos (28 + i * 16) ypos (66 - bh // 2) alpha 0.9
            frame:
                xpos 540
                ysize 120
                xsize 540
                background Frame(FK_DIR + "fk_panel.png", 30, 30)
                padding (26, 12, 26, 12)
                vbox:
                    spacing 4
                    hbox:
                        spacing 16
                        text _("HORODATAGE") style "fk_label" size 18 yalign 0.5
                        text st.clock_text() style "fk_title" size 34 color FK_WHITE
                    hbox:
                        spacing 16
                        text _("ORIGINE") style "fk_label" size 18 yalign 0.5
                        text "KAMI.CORE" style "fk_title" size 30 color FK_CYAN

        # --- Actions.
        $ can_act = (st.state == "line" and st.end_t is None)
        hbox:
            xpos 70
            ypos 952
            spacing 22
            for act_id, act_label, act_col, act_panel, act_rot in (
                    ("let", _("LAISSER PARLER"), FK_CYAN, "fk_panel.png", 180),
                    ("cut", _("INTERROMPRE"), FK_RED, "fk_panel_red.png", 90),
                    ("confront", _("CONFRONTER"), FK_AMBER, "fk_panel_amber.png", 0)):
                button:
                    xysize (420, 100)
                    background Frame(FK_DIR + act_panel, 30, 30)
                    hover_background Frame(FK_DIR + "fk_panel_amber.png", 30, 30)
                    sensitive can_act
                    action Function(st.act, act_id)
                    hbox:
                        spacing 18
                        xalign 0.5
                        yalign 0.5
                        add Transform(FK_DIR + "fk_arrow.png", rotate=act_rot, zoom=0.42, matrixcolor=TintMatrix(act_col)) yalign 0.5
                        text fk_tr(act_label) style "fk_title" size 36 color act_col kerning 3 yalign 0.5

        use fk_bark_layer(st, 1170, 150, 700)
        use fk_cutin_layer(st)
        use fk_fx_layer(st)
        use fk_phase_title(st, 1)

    use fk_help(st, "fk_tuto_p1")

    if st.result is not None:
        timer 0.01 action Return(st.result)


# ============================================================
# ÉCRAN — PHASE 2 : L'USURPATION
# ============================================================
screen fk_phase2_screen():
    modal True
    zorder 300

    $ st = fk
    timer 0.033 repeat True action Function(st.tick)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "K_1" action Function(st.click, 0)
    key "K_2" action Function(st.click, 1)
    key "K_3" action Function(st.click, 2)
    key "K_4" action Function(st.click, 3)
    key "K_5" action Function(st.click, 4)
    key "K_KP1" action Function(st.click, 0)
    key "K_KP2" action Function(st.click, 1)
    key "K_KP3" action Function(st.click, 2)
    key "K_KP4" action Function(st.click, 3)
    key "K_KP5" action Function(st.click, 4)

    fixed:
        xoffset st.sx
        yoffset st.sy

        use fk_backdrop(red=0.25 + (100.0 - st.ctrl_shown) / 130.0, noise=0.10 + (100.0 - st.ctrl_shown) / 500.0)

        # --- En-tête + vague.
        frame:
            xpos 40
            ypos 30
            xsize 640
            background Frame(FK_DIR + "fk_panel_red.png", 30, 30)
            padding (30, 14, 30, 16)
            vbox:
                spacing 0
                text _("USURPATION  //  PHASE 2") style "fk_label" color FK_RED
                text _("L'USURPATION") style "fk_title" size 52 kerning 6
        if st.wave_data() is not None:
            text (_("VAGUE") + " %d / %d" % (st.wave_i + 1, len(FK_P2_WAVES))) style "fk_title" size 30 xpos 720 ypos 60 color FK_WHITE kerning 4
        use fk_control_bar(st.ctrl_shown)

        # --- Moniteurs.
        for m in st.monitors:
            if m.state != "wait":
                $ mx, my = m.xy(st.t)
                $ age = st.t - m.state_t
                $ spawn_k = fk_ease_out((st.t - m.spawn_t) / 0.25)
                $ gone = m.state in ("neutral", "executed", "done")
                $ ga = fk_clamp(1.0 - age / 0.55, 0.0, 1.0) if gone else 1.0
                $ hurt = (st.t - m.hurt_t) < 0.8
                $ glitch = (0.55 if m.state == "neutral" else (0.4 if hurt else (0.1 + m.charge * 0.25 if m.fake else 0.06)))
                $ mon_img = ("fk_monitor_red.png" if m.state == "executed" else ("fk_monitor_white.png" if hurt else "fk_monitor.png"))
                $ live = (m.state == "live")
                fixed at Transform(alpha=(spawn_k * ga)):
                    xpos int(mx - FK_MON_W // 2)
                    ypos int(my - FK_MON_H // 2 - 30)
                    xysize (FK_MON_W, FK_MON_H + 120)
                    # Vitre.
                    add Transform(fk_monitor_glass(m.expr, st.tint_for(m), glitch, st.seed + m.slot * 7, st.mouth and live and m.charge < 0.5), zoom=FK_MON_SCALE):
                        xpos int(24 * FK_MON_SCALE)
                        ypos int(22 * FK_MON_SCALE)
                    if m.state == "executed":
                        add Solid(FK_RED, xysize=(int(392 * FK_MON_SCALE), int(262 * FK_MON_SCALE))) xpos int(24 * FK_MON_SCALE) ypos int(22 * FK_MON_SCALE) alpha 0.45
                    add Transform(FK_DIR + "fk_noise.png", crop=(0, (st.seed * 37) % 700, 392, 262), zoom=FK_MON_SCALE) xpos int(24 * FK_MON_SCALE) ypos int(22 * FK_MON_SCALE) alpha (0.10 + glitch * 0.4)
                    add Transform(FK_DIR + mon_img, zoom=FK_MON_SCALE)
                    if live and m.move_t is not None:
                        add Solid("#ffffff", xysize=(FK_MON_W, FK_MON_H)) alpha 0.08
                    # Charge (identique pour toutes : ne trahit rien).
                    add Solid("#0b1626", xysize=(int(330 * FK_MON_SCALE), 10)) xpos int(52 * FK_MON_SCALE) ypos int(296 * FK_MON_SCALE)
                    add Solid((FK_AMBER if m.charge < 0.7 else FK_RED), xysize=(int(330 * FK_MON_SCALE * fk_clamp(m.charge, 0.0, 1.0)), 10)) xpos int(52 * FK_MON_SCALE) ypos int(296 * FK_MON_SCALE)
                    # Numéro de slot.
                    add Transform(FK_DIR + "fk_key.png", zoom=0.5) xpos -14 ypos -14
                    text ("%d" % (m.slot + 1)) style "fk_title" size 26 color FK_CYAN xpos 10 ypos -8
                    # Réplique.
                    frame:
                        ypos (FK_MON_H + 6)
                        xsize FK_MON_W
                        background Frame(FK_DIR + "fk_panel.png", 24, 24)
                        padding (18, 10, 18, 12)
                        text fk_tr(m.text) style "fk_body" size 22 substitute False
                    if m.state == "neutral":
                        text _("NEUTRALISÉE") style "fk_title" size 46 color "#ffffff" xalign 0.5 ypos 100 outlines [(4, FK_RED, 0, 0)]
                    elif m.state == "executed":
                        text fk_tr(m.cmd or "") style "fk_title" size 30 color "#ffffff" xalign 0.5 ypos 104 outlines [(4, "#300008", 0, 0)] substitute False
                    elif hurt:
                        text _("C'ÉTAIT ELLE") style "fk_title" size 40 color "#ffffff" xalign 0.5 ypos 100 outlines [(4, FK_CYAN, 0, 0)]
                    if live:
                        button:
                            xysize (FK_MON_W, FK_MON_H)
                            background None
                            hover_background Frame(FK_DIR + "fk_select.png", 40, 40)
                            hover_sound "audio/sfx_beep.mp3"
                            action Function(st.click, m.slot)

        text _("CLIC OU 1-5 : NEUTRALISER UNE FAUSSE KAMI     •     NE TOUCHE PAS LA VRAIE"):
            style "fk_label"
            size 22
            xalign 0.5
            ypos 1034

        use fk_bark_layer(st, 1140, 150, 740)
        use fk_cutin_layer(st, 884)
        use fk_fx_layer(st)
        use fk_phase_title(st, 2, FK_RED)

    use fk_help(st, "fk_tuto_p2")

    if st.result is not None:
        timer 0.01 action Return(st.result)


# ============================================================
# ÉCRAN — PHASE 3 : LE SILENCE
# ============================================================
screen fk_phase3_screen():
    modal True
    zorder 300

    $ st = fk
    timer 0.033 repeat True action Function(st.tick)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "K_LEFT" action Function(st.press, 0)
    key "K_a" action Function(st.press, 0)
    key "K_q" action Function(st.press, 0)
    key "K_UP" action Function(st.press, 1)
    key "K_w" action Function(st.press, 1)
    key "K_z" action Function(st.press, 1)
    key "K_RIGHT" action Function(st.press, 2)
    key "K_d" action Function(st.press, 2)
    key "K_DOWN" action Function(st.press, 3)
    key "K_s" action Function(st.press, 3)
    key "pad_dpleft_press" action Function(st.press, 0)
    key "pad_dpup_press" action Function(st.press, 1)
    key "pad_dpright_press" action Function(st.press, 2)
    key "pad_dpdown_press" action Function(st.press, 3)
    key "K_SPACE" action Function(st.mash_press)
    key "K_RETURN" action Function(st.mash_press)
    key "pad_a_press" action Function(st.mash_press)

    $ cut_done = (st.state == "cut")
    $ cut_age = (st.t - st.state_t) if cut_done else 0.0

    fixed:
        xoffset st.sx
        yoffset st.sy

        use fk_backdrop(red=0.35 + st.corruption_shown / 120.0, noise=0.12 + st.corruption_shown / 400.0)

        # --- En-tête.
        frame:
            xpos 40
            ypos 30
            xsize 640
            background Frame(FK_DIR + "fk_panel.png", 30, 30)
            padding (30, 14, 30, 16)
            vbox:
                spacing 0
                text _("PARE-FEU  //  PHASE 3") style "fk_label" color FK_CYAN
                text _("LE SILENCE") style "fk_title" size 52 kerning 6

        # --- Jauges : corruption du noyau / coupure du signal.
        fixed:
            xpos 720
            ypos 40
            xysize (520, 90)
            text _("CORRUPTION DU NOYAU") style "fk_label" color FK_RED
            text ("%d%%" % int(st.corruption_shown)) style "fk_title" size 26 xalign 1.0 ypos -6 color FK_RED
            add Solid("#1a0208e0", xysize=(520, 26)) ypos 32
            add Solid(FK_RED, xysize=(int(516 * st.corruption_shown / 100.0), 20)) xpos 2 ypos 35
        fixed:
            xpos 1300
            ypos 40
            xysize (580, 90)
            text _("COUPURE DU SIGNAL") style "fk_label" color FK_CYAN
            text ("%d%%" % int(st.cut_shown)) style "fk_title" size 26 xalign 1.0 ypos -6 color FK_CYAN
            add Solid("#06141ee0", xysize=(580, 26)) ypos 32
            add Solid(FK_CYAN, xysize=(int(576 * st.cut_shown / 100.0), 20)) xpos 2 ypos 35

        # --- Couloir de commandes.
        add Solid("#0a1424cc", xysize=(1700, 150)) xpos 60 ypos (FK_LANE_Y - 75)
        add Solid("#ff2e5a55", xysize=(1600, 2)) xpos 60 ypos (FK_LANE_Y - 76)
        add Solid("#5cd3ff55", xysize=(1600, 2)) xpos 60 ypos (FK_LANE_Y + 74)
        add Transform(FK_DIR + "fk_glow.png", matrixcolor=TintMatrix(FK_RED), zoom=0.7) xpos -60 ypos (FK_LANE_Y - 180) at fk_pulse(0.4, 0.9, 0.5)
        text _("SOURCE ???") style "fk_label" size 20 color FK_RED xpos 70 ypos (FK_LANE_Y + 86)
        add Transform(FK_DIR + "fk_firewall.png", xysize=(FK_ZONE_X1 - FK_ZONE_X0, 240)) xpos FK_ZONE_X0 ypos (FK_LANE_Y - 120) at fk_pulse(0.55, 1.0, 0.45)
        text _("PARE-FEU") style "fk_label" size 20 color FK_CYAN xpos (FK_ZONE_X0 + 30) ypos (FK_LANE_Y + 126)

        # Noyau.
        $ core_tint = fk_mix_hex("#ffffff", "#ff4d6d", st.corruption_shown / 100.0)
        add Transform(FK_DIR + "fk_core.png", matrixcolor=TintMatrix(core_tint), zoom=0.78) xpos (FK_CORE_X - 140) ypos (FK_LANE_Y - 140) at fk_breathe
        add Transform(FK_DIR + "fk_core_ring.png", matrixcolor=TintMatrix(core_tint), rotate=((st.t * (60.0 + st.corruption_shown * 2.4)) % 360.0)):
            xpos FK_CORE_X
            ypos FK_LANE_Y
            anchor (0.5, 0.5)
        text _("NOYAU") style "fk_label" size 20 color FK_CYAN xpos (FK_CORE_X - 34) ypos (FK_LANE_Y + 150)

        # Commandes.
        for c in st.cmds:
            $ cage = st.t - c.state_t
            if c.state == "move" or cage < 0.4:
                $ ca = 1.0 if c.state == "move" else fk_clamp(1.0 - cage / 0.4, 0.0, 1.0)
                $ cimg = ("fk_cmd_kami.png" if c.kind == "kami" else ("fk_cmd_masked.png" if (c.kind == "masked" and not c.revealed()) else "fk_cmd.png"))
                $ wrong = (st.t - c.wrong_t) < 0.25
                $ ccol = (FK_CYAN if c.kind == "kami" else (FK_VIOLET if c.kind == "masked" else FK_RED))
                $ cz = 1.0 + (0.3 * cage if c.state != "move" else 0.0)
                fixed at Transform(alpha=ca, zoom=cz):
                    xpos int(c.x - 95 + (8 if wrong and int(st.t * 40) % 2 else 0))
                    ypos (FK_LANE_Y - 65)
                    xysize (190, 130)
                    add (FK_DIR + cimg)
                    if c.revealed():
                        add Transform(FK_DIR + "fk_arrow.png", rotate=FK_GLYPH_ROT[c.glyph], zoom=0.56, matrixcolor=TintMatrix(ccol if not c.in_zone() else "#ffffff")) xalign 0.5 yalign 0.40
                    else:
                        text "?" style "fk_title" size 70 color FK_VIOLET xalign 0.5 yalign 0.40
                    text c.label style "fk_label" size 14 color ccol xalign 0.5 ypos 92 substitute False

        # --- Kami, au-dessus du noyau.
        $ k3 = st.kami_expr()
        $ k3_talk = st.mouth and st.bark is not None and (st.t - st.bark["t0"] < 1.6)
        add Transform(fk_kami(k3, k3_talk, 0.05 + st.corruption_shown / 160.0, "#6ce8fa", st.seed), zoom=0.32) xpos 1450 ypos 70 at fk_breathe

        # --- Touches (souris).
        if st.state == "run":
            hbox:
                xalign 0.5
                ypos 830
                spacing 26
                for g in range(4):
                    $ lit = (st.t - st.key_flash[g]) < 0.12
                    button:
                        xysize (120, 120)
                        background Transform(FK_DIR + "fk_key.png", xysize=(120, 120), matrixcolor=TintMatrix("#ffffff" if lit else "#9fdcff"))
                        hover_background Transform(FK_DIR + "fk_key.png", xysize=(120, 120), matrixcolor=TintMatrix(FK_AMBER))
                        action Function(st.press, g)
                        add Transform(FK_DIR + "fk_arrow.png", rotate=FK_GLYPH_ROT[g], zoom=0.55) align (0.5, 0.45)
            text _("FLÈCHES / ZQSD / WASD : DÉTRUIRE LA COMMANDE DANS LE PARE-FEU     •     LE BLEU, C'EST KAMI : LAISSE-LE PASSER"):
                style "fk_label"
                size 20
                xalign 0.5
                ypos 980

        # --- Coupure finale.
        if st.state in ("mash", "cut"):
            $ mk = fk_clamp(st.mash / 100.0, 0.0, 1.0) if st.state == "mash" else 1.0
            $ gap = int(mk * 260 + (cut_age * 900 if cut_done else 0))
            add Solid("#02040acc")
            add (FK_DIR + "fk_plug_left.png") xpos (440 - gap // 2) ypos 440 zoom 1.15
            add (FK_DIR + "fk_plug_right.png") xpos (900 + gap // 2) ypos 430 zoom 1.15
            if not cut_done:
                add Transform(FK_DIR + "fk_spark.png", zoom=0.7 + (st.seed % 3) * 0.12) xpos (960 - 90) ypos (540 - 120) alpha (0.6 + (st.seed % 2) * 0.4)
                text _("COUPE LE SIGNAL !") style "fk_title" size 110 xalign 0.5 ypos 200 color "#ffffff" kerning 10 outlines [(6, "#02050c", 0, 0), (3, FK_CYAN, 0, 0)]
                text _("ESPACE / CLIC — À RÉPÉTITION") style "fk_title" size 34 xalign 0.5 ypos 330 color FK_AMBER kerning 6
                add Solid("#0b1626", xysize=(900, 30)) xalign 0.5 ypos 760
                add Solid(FK_CYAN, xysize=(int(896 * mk), 24)) xpos 512 ypos 763
                text _("LE PIRATE RETIENT LE RELAIS") style "fk_label" size 22 color FK_RED xalign 0.5 ypos 806
                button:
                    xysize (1920, 1080)
                    background None
                    action Function(st.mash_press)

        use fk_bark_layer(st, 1020, 330, 400)
        use fk_cutin_layer(st, 150)
        use fk_fx_layer(st)
        use fk_phase_title(st, 3)

        if cut_done:
            add Solid("#000000") alpha fk_clamp((cut_age - 0.25) / 0.6, 0.0, 1.0)
            if cut_age > 1.2:
                text _("SIGNAL PERDU") at Transform(alpha=fk_clamp((cut_age - 1.2) / 0.8, 0.0, 1.0)):
                    style "fk_label"
                    size 26
                    color "#3d566b"
                    xalign 0.5
                    yalign 0.5
                    kerning 14

    if not cut_done:
        use fk_help(st, "fk_tuto_p3")

    if st.result is not None:
        timer 0.01 action Return(st.result)


# ============================================================
# ÉCRAN — INTERMÈDE (dialogue intégré au combat)
# ============================================================
screen fk_interlude_screen(il, red=0.2):
    modal True
    zorder 300

    timer 0.033 repeat True action Function(il.tick)
    key "rollback" action NullAction()
    key "K_SPACE" action Function(il.advance)
    key "K_RETURN" action Function(il.advance)
    key "pad_a_press" action Function(il.advance)

    $ who, expr, _txt = il.cur()
    $ is_kami = (who == "kami")

    use fk_backdrop(red=red, noise=0.12)

    add Transform(FK_DIR + "fk_glow.png", matrixcolor=TintMatrix(FK_CYAN), zoom=2.4) xalign 0.5 yalign 0.35 alpha 0.16
    add Transform(fk_kami(expr if is_kami else "gene", is_kami and il.mouth and len(il.typed()) < len(fk_tr(_txt)), 0.12 + (0.25 if is_kami else 0.0), "#6ce8fa", il.seed), zoom=0.7) at fk_breathe:
        xalign 0.5
        ypos 40
        alpha (1.0 if is_kami else 0.45)

    if not is_kami:
        $ col = fk_color(who)
        fixed:
            xpos 60
            ypos 690
            xysize (1500, 200)
            add Transform(FK_DIR + "fk_cutin_band.png", matrixcolor=TintMatrix(col), xysize=(1300, 170)) xpos 60 ypos 18 alpha 0.92
            add fk_portrait(who, 190) xpos 40 ypos 4
            add Transform(FK_DIR + "fk_hexframe.png", matrixcolor=TintMatrix(col), xysize=(200, 200)) xpos 35 ypos -1

    frame:
        xalign 0.5
        ypos 862
        xsize 1500
        ysize 170
        background Frame(FK_DIR + ("fk_panel.png" if is_kami else "fk_panel_amber.png"), 30, 30)
        padding (44, 20, 44, 20)
        vbox:
            spacing 6
            text fk_name(who) style "fk_title" size 32 color fk_color(who) kerning 4
            text il.typed() style "fk_body" size 34 substitute False

    button:
        xysize (1920, 1080)
        background None
        action Function(il.advance)

    if il.done:
        timer 0.25 action Return(True)


# ============================================================
# TUTORIELS (chrome du kit, démos animées)
# ============================================================
transform fk_demo_bubble:
    alpha 0.0 xoffset -60
    easeout 0.3 alpha 1.0 xoffset 0
    pause 2.4
    linear 0.2 alpha 0.0
    pause 0.4
    repeat

transform fk_demo_stamp(delay=1.6):
    alpha 0.0 zoom 1.6
    pause delay
    easeout 0.12 alpha 1.0 zoom 1.0
    pause 0.9
    linear 0.15 alpha 0.0
    pause (3.3 - delay - 1.17)
    repeat

transform fk_demo_wave_flat:
    yoffset 0
    ease 0.25 yoffset -10
    ease 0.25 yoffset 10
    repeat

transform fk_demo_move:
    xpos 40
    linear 2.4 xpos 560
    pause 0.3
    repeat

transform fk_demo_slash:
    alpha 0.0
    pause 1.2
    linear 0.05 alpha 1.0
    pause 0.5
    linear 0.2 alpha 0.0
    pause 1.0
    repeat

screen fk_tuto_p1(as_overlay=False):
    use mk_tuto_chrome(_("LE DÉNI"), [
        (_("Écoute chaque réplique de Kami"), _("Certaines viennent d'elle. D'autres ont été injectées par une présence extérieure.")),
        (_("LAISSER PARLER  (flèche gauche / 1)"), _("C'est vraiment Kami : onde vocale désordonnée, ton théâtral.")),
        (_("INTERROMPRE  (flèche bas / 2)"), _("Injection : onde trop régulière ou qui boucle, horodatage décalé, ton de machine.")),
        (_("CONFRONTER  (flèche droite / 3)"), _("Kami nie un fait que vous avez tous vu. Relève la contradiction.")),
        (_("Ne laisse pas filer le temps"), _("Sans réponse, la réplique passe. Une injection qui passe s'exécute.")),
    ], "fk_tuto_p1", as_overlay):
        fixed:
            frame at fk_demo_bubble:
                xpos 40
                ypos 60
                xsize 660
                background Frame(FK_DIR + "fk_statement.png", 60, 60)
                padding (34, 26)
                vbox:
                    text "KAMI" style "fk_title" size 26 color FK_CYAN
                    text _("Kami ne détecte aucune anomalie.") style "fk_body" size 30
            fixed:
                xpos 40
                ypos 250
                xysize (660, 110)
                add (FK_DIR + "fk_wave_bg.png")
                for wi in range(28):
                    add Solid(FK_CYAN, xysize=(10, 40)) xpos (24 + wi * 16) ypos (40 + FK_DEMO_WAVE[wi]) at fk_demo_wave_flat
            text _("Onde trop régulière + ton de machine = injection") style "fk_label" size 20 color FK_RED xpos 40 ypos 372
            fixed at fk_demo_stamp(1.4):
                xpos 20
                ypos 400
                xysize (700, 120)
                add Transform(FK_DIR + "fk_slash_red.png", zoom=0.55) xalign 0.5 yalign 0.5
                text _("INTERROMPU !") style "fk_title" size 64 xalign 0.5 yalign 0.5 outlines [(4, "#02050c", 0, 0)]

screen fk_tuto_p2(as_overlay=False):
    use mk_tuto_chrome(_("L'USURPATION"), [
        (_("Plusieurs Kami parlent en même temps"), _("Une seule — ou deux — sont la vraie. Les autres chargent une commande.")),
        (_("Clique sur une fausse Kami"), _("Ou touche 1 à 5. Neutralise-la avant que sa barre ne se remplisse.")),
        (_("Ne frappe pas la vraie"), _("La vraie Kami panique et t'aide. Les fausses restent calmes, procédurières.")),
        (_("Les indices s'effacent"), _("Au début, les fausses ont un reflet rosé. Ensuite, seul leur discours les trahit.")),
    ], "fk_tuto_p2", as_overlay):
        fixed:
            for di, dx in enumerate((40, 270, 500)):
                fixed:
                    xpos dx
                    ypos 80
                    xysize (220, 200)
                    add Transform(fk_monitor_glass(("gene", "taquin", "colere")[di], ("#6ce8fa", "#ff8fb0", "#6ce8fa")[di], 0.05, di, False), zoom=0.5) xpos 12 ypos 11
                    add Transform(FK_DIR + "fk_monitor.png", zoom=0.5)
                    add Solid(FK_AMBER, xysize=(150, 6)) xpos 26 ypos 148 at fk_pulse(0.4, 1.0, 0.4)
            add Transform(FK_DIR + "fk_slash_red.png", zoom=0.32, rotate=-18) xpos 230 ypos 100 at fk_demo_slash
            text _("« Tout va bien, mes chéris. Restez assis. »") style "fk_body" size 22 color "#ff8fb0" xpos 120 ypos 300
            text _("Calme, souriante, reflet rosé : fausse.") style "fk_label" size 20 color FK_RED xpos 120 ypos 340
            text _("« Noam ?! C'est moi, celle-là ! »") style "fk_body" size 22 color FK_CYAN xpos 120 ypos 400
            text _("Elle panique, elle t'appelle : vraie.") style "fk_label" size 20 color FK_CYAN xpos 120 ypos 440

screen fk_tuto_p3(as_overlay=False):
    use mk_tuto_chrome(_("LE SILENCE"), [
        (_("Les commandes filent vers le noyau"), _("Détruis-les quand elles traversent le PARE-FEU, avec la bonne direction.")),
        (_("Flèches, ZQSD ou WASD"), _("Ou clique sur les touches à l'écran. Mauvaise direction = corruption.")),
        (_("Violet : direction cachée"), _("Elle n'apparaît qu'à l'approche du pare-feu. Kami te prévient.")),
        (_("Bleu en pointillés : c'est Kami"), _("Ses propres processus. Laisse-les passer, ils la soignent.")),
        (_("Coupe le signal"), _("À la fin, martèle ESPACE ou clique pour arracher le relais.")),
    ], "fk_tuto_p3", as_overlay):
        fixed:
            add Solid("#0a1424", xysize=(720, 130)) xpos 20 ypos 160
            add Transform(FK_DIR + "fk_firewall.png", xysize=(150, 200)) xpos 470 ypos 125 at fk_pulse(0.5, 1.0, 0.45)
            fixed at fk_demo_move:
                ypos 165
                xysize (190, 130)
                yanchor 0.0
                add Transform(FK_DIR + "fk_cmd.png", zoom=0.9)
                add Transform(FK_DIR + "fk_arrow.png", rotate=90, zoom=0.5, matrixcolor=TintMatrix(FK_RED)) xalign 0.45 yalign 0.4
            add Transform(FK_DIR + "fk_key.png", zoom=1.0) xpos 320 ypos 330
            add Transform(FK_DIR + "fk_arrow.png", rotate=90, zoom=0.5) xpos 336 ypos 344
            text _("Flèche bas, au bon moment") style "fk_label" size 22 color FK_CYAN xpos 430 ypos 360
            add Transform(FK_DIR + "fk_cmd_kami.png", zoom=0.6) xpos 40 ypos 10
            text _("Kami : ne pas toucher") style "fk_label" size 20 color FK_CYAN xpos 170 ypos 40
            add Transform(FK_DIR + "fk_cmd_masked.png", zoom=0.6) xpos 400 ypos 10
            text "?" style "fk_title" size 48 color FK_VIOLET xpos 448 ypos 14


# ============================================================
# DÉROULÉ COMPLET
# ============================================================
label fausse_kami_run:

    $ renpy.block_rollback()
    $ fk_session_reset()
    $ fk_skipped = False
    $ mk_reset_retries(FK_MG_ID)
    window hide
    $ fk_prev_quick = getattr(store, "quick_menu", True)
    $ quick_menu = False

    stop music fadeout 0.6
    play sound "audio/trailer/trl_riser_short.wav"
    call mk_tutorial("fausse_kami_p1", "fk_tuto_p1") from _call_fk_tuto_p1

label .phase1:
    $ fk_p1_snapshot = (fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly)
    $ fk = FKPhase1(fk_session)
    play music "music/bgm_system_override.mp3" fadein 0.8
    play sound "audio/trailer/trl_braam.wav"
    call screen fk_phase1_screen
    if _return != "win":
        $ fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly = fk_p1_snapshot
        call mk_fail_retry(_("FAUSSE KAMI — LE DÉNI"), FK_MG_ID) from _call_fk_retry_p1
        if _return:
            jump .phase1
        $ fk_skipped = True
        jump .finish
    $ fk_p1_ctrl = fk.ctrl

    call screen fk_interlude_screen(FKInterlude(FK_INTERLUDE_12), 0.2)
    call mk_tutorial("fausse_kami_p2", "fk_tuto_p2") from _call_fk_tuto_p2

label .phase2:
    $ fk_p2_snapshot = (fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly, fk_session.p2_neutralized, fk_session.p2_fakes)
    $ fk = FKPhase2(fk_session, fk_p1_ctrl + 10)
    play music "music/bgm_fatal_assembly.mp3" fadein 0.6
    play sound "audio/trailer/trl_impact_deep.wav"
    call screen fk_phase2_screen
    if _return != "win":
        $ (fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly, fk_session.p2_neutralized, fk_session.p2_fakes) = fk_p2_snapshot
        call mk_fail_retry(_("FAUSSE KAMI — L'USURPATION"), FK_MG_ID) from _call_fk_retry_p2
        if _return:
            jump .phase2
        $ fk_skipped = True
        jump .finish

    stop music fadeout 1.2
    call screen fk_interlude_screen(FKInterlude(FK_INTERLUDE_23), 0.45)
    call mk_tutorial("fausse_kami_p3", "fk_tuto_p3") from _call_fk_tuto_p3

label .phase3:
    $ fk_p3_snapshot = (fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly, fk_session.p3_hits, fk_session.max_corruption)
    $ fk = FKPhase3(fk_session)
    play music "music/bgm_horror_pulse.mp3" fadein 0.6
    play sound "audio/trailer/trl_sub_drop.wav"
    call screen fk_phase3_screen
    $ fk_loop(None)
    if _return != "win":
        $ (fk_session.score, fk_session.score_max, fk_session.executed, fk_session.friendly, fk_session.p3_hits, fk_session.max_corruption) = fk_p3_snapshot
        call mk_fail_retry(_("FAUSSE KAMI — LE SILENCE"), FK_MG_ID) from _call_fk_retry_p3
        if _return:
            jump .phase3
        $ fk_skipped = True
        jump .finish

label .finish:
    $ fk_loop(None)
    $ quick_menu = fk_prev_quick
    python:
        fk_s = fk_session
        fk_success = not fk_skipped
        fk_max = max(1, fk_s.score_max)
        fk_score_final = int(1000.0 * fk_s.score / fk_max) if fk_success else 0
        fk_challenges = [
            (_("Aucune commande pirate exécutée"), fk_success and fk_s.executed == 0),
            (_("Kami jamais frappée par erreur"), fk_success and fk_s.friendly == 0),
            (_("Corruption du noyau sous 30 %"), fk_success and fk_s.max_corruption < 30),
        ]
        fk_score_final = min(1000, fk_score_final + 0)
        fk_last_result = {
            "success": fk_success,
            "score": fk_score_final,
            "executed": fk_s.executed,
            "friendly": fk_s.friendly,
            "max_corruption": fk_s.max_corruption,
            "late_cut": fk_s.late_cut,
            "skipped": fk_skipped,
            "rank": "D",
        }
    if fk_success:
        call mk_show_results(
            FK_TITLE,
            fk_score_final,
            1000,
            stats=[
                (_("Répliques démêlées"), "%d / %d" % (fk_s.p1_correct, max(1, fk_s.p1_total))),
                (_("Fausses Kami neutralisées"), "%d / %d" % (fk_s.p2_neutralized, max(1, fk_s.p2_fakes))),
                (_("Commandes détruites"), "%d / %d" % (fk_s.p3_hits, max(1, fk_s.p3_cmds))),
                (_("Coupure"), (_("tardive (Kael)") if fk_s.late_cut else _("nette"))),
            ],
            challenges=fk_challenges,
            mg_id=FK_MG_ID,
            retries=mk_get_retries(FK_MG_ID),
        ) from _call_fk_results
        $ fk_last_result["rank"] = _return
        $ persistent.fk_best_score = max(persistent.fk_best_score or 0, fk_score_final)
    else:
        $ mk_reset_retries(FK_MG_ID)
    $ fk = None
    $ renpy.block_rollback()
    return fk_last_result
