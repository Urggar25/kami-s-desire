# ============================================================
# MINI-JEU JOUR 9_0_1 — LE SIGNAL VIVANT  (V2)
#
# Contexte : pendant le débat du Conclave (label _9_0_1_CONCLAVE_DEBAT),
# Noam doit maintenir vivant un signal de transmission pour que le
# message de dispersion atteigne les campements aux frontières.
#
# Mécanique V2 :
# - 9 personnages = 9 fréquences uniques placées dans 4 slots actifs.
# - 3 jauges globales à maintenir en zone verte : Clarté, Force, Discrétion.
# - La carte des campements est divisée en 4 QUADRANTS (NO, NE, SO, SE).
#   Chaque quadrant a SA PROPRE jauge de dispersion + une mini forme d'onde.
# - Clic gauche sur un quadrant = ENVOI D'UNE PULSE (cooldown par quadrant).
# - Kami envoie des ORBES NOIRS qui volent vers les quadrants ou vers
#   la forme d'onde centrale. Clic répété pour les détruire (3 à 5 hits).
#   - Orbe touche quadrant : signal coupé quelques secondes sur ce quadrant.
#   - Orbe touche centre : perturbation globale (jauges chaotiques).
# - Bonus de fréquence :
#   * Ryn  → +50% de vitesse de dispersion sur les quadrants menacés.
#   * Elen → +25% de vitesse de dispersion partout.
#   * Mara → "buzz" aléatoire : booste un quadrant au hasard toutes les 2-4s.
#
# Durée : 45 secondes maximum. Plus le temps avance, plus les orbes
# arrivent vite.
#
# Appel scénario :
#   call j901_play_signal_vivant
#   $ j901_signal_result_tier = _return     # "excellent" / "bon" / "moyen" / "echec"
# ============================================================


# ------------------------------------------------------------
# Variables d'état
# ------------------------------------------------------------

default j901_sv_time_left = 45.0
default j901_sv_done = False
default j901_sv_result_tier = "moyen"

# Slots actifs : 4 slots, chacun contient soit None soit la clé d'un perso
default j901_sv_slots = [None, None, None, None]
default j901_sv_slot_power = [2, 2, 2, 2]

# Jauges globales 0..100
default j901_sv_g_clarte = 50.0
default j901_sv_g_force = 50.0
default j901_sv_g_discretion = 50.0
default j901_sv_target_clarte = 50.0
default j901_sv_target_force = 50.0
default j901_sv_target_discretion = 50.0

# Forme d'onde globale (60 valeurs entre -1 et 1)
default j901_sv_wave = [0.0] * 60

# Quadrants : 4 quadrants (0=NO, 1=NE, 2=SO, 3=SE)
default j901_sv_quad_offset = [0.0, 0.0, 0.0, 0.0]    # progression dispersion 0..100
default j901_sv_quad_cooldown = [0.0, 0.0, 0.0, 0.0]   # cooldown du clic pulse
default j901_sv_quad_disabled = [0.0, 0.0, 0.0, 0.0]   # temps restant de désactivation
default j901_sv_quad_pulse_anim = [0.0, 0.0, 0.0, 0.0] # animation de pulse en cours
default j901_sv_quad_wave = [[0.0] * 16, [0.0] * 16, [0.0] * 16, [0.0] * 16]
default j901_sv_quad_urgency = [1.25, 1.10, 0.95, 1.35]  # quadrants plus exposés
default j901_sv_pulse_count = 0      # stats : pulses envoyées
default j901_sv_orbs_killed = 0      # stats : orbes détruits
default j901_sv_hits_taken = 0       # stats : impacts subis

# Orbes (liste de dicts)
default j901_sv_orbs = []
default j901_sv_orb_id_counter = 0
default j901_sv_next_orb = 5.0

# Effet "buzz" de Mara
default j901_sv_mara_timer = 3.0

# Perturbation globale (en secondes restantes)
default j901_sv_global_disturb = 0.0

# Dialogue du débat (auto-déroulé)
default j901_sv_debate_index = 0
default j901_sv_debate_next = 1.0
default j901_sv_current_speaker = "tomas"
default j901_sv_current_expr = "raison"
default j901_sv_current_line = "Le signal s'ouvre. Les campements vous écoutent."

# Effets visuels
default j901_sv_flash = 0.0
default j901_sv_kami_alert = ""
default j901_sv_kami_alert_time = 0.0
default j901_sv_warning = "ÉMISSION INITIÉE"
default j901_sv_status_color = "#7DF9FF"

# Stats finales
default j901_sv_dots_safe = 0
default j901_sv_dots_lost = 0


# ------------------------------------------------------------
# Logique Python
# ------------------------------------------------------------

init python:
    import random
    import math

    J901_SV_TICK = 0.05
    J901_SV_TOTAL_TIME = 45.0

    # Coordonnées des centres des 4 quadrants (en pixels écran 1920x1080)
    # Pane droit : x=1152..1920, y=170..980
    # Quadrants : 384 x 405 chacun
    J901_SV_QUAD_RECTS = [
        # (x, y, w, h, label_court, label_long)
        (1152, 170, 384, 405, "NO", "NORD-OUEST"),
        (1536, 170, 384, 405, "NE", "NORD-EST"),
        (1152, 575, 384, 405, "SO", "SUD-OUEST"),
        (1536, 575, 384, 405, "SE", "SUD-EST"),
    ]

    def j901_sv_quad_center(q):
        x, y, w, h, _, _ = J901_SV_QUAD_RECTS[q]
        return (x + w // 2, y + h // 2)

    # Centre de la forme d'onde globale (cible des orbes "centre")
    J901_SV_CENTER_TARGET = (380, 670)

    # Chips
    J901_SV_CHIPS = {
        "ryn":    {"nom": "Ryn",    "couleur": "#D2283C", "freq": "BASSE GRAVE",
                   "c": -1, "f": +3, "d": -2,
                   "bonus": "Boost x1.5 sur les quadrants menacés",
                   "asset": "minijeu/signal_vivant_assets/chip_ryn.png"},
        "lysa":   {"nom": "Lysa",   "couleur": "#5AAAF0", "freq": "CLAIRE FROIDE",
                   "c": +3, "f": -1, "d": +1,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_lysa.png"},
        "elen":   {"nom": "Elen",   "couleur": "#FFC850", "freq": "HAUTE ÉMOTIONNELLE",
                   "c": +1, "f": +2, "d": -1,
                   "bonus": "Boost +25% global de dispersion",
                   "asset": "minijeu/signal_vivant_assets/chip_elen.png"},
        "mara":   {"nom": "Mara",   "couleur": "#B446E6", "freq": "PARASITE CHAOS",
                   "c": -2, "f": +2, "d": -1,
                   "bonus": "Buzz aléatoire sur un quadrant",
                   "asset": "minijeu/signal_vivant_assets/chip_mara.png"},
        "noam":   {"nom": "Noam",   "couleur": "#DCF0FF", "freq": "PORTEUSE STABLE",
                   "c": +1, "f": 0, "d": +1,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_noam.png"},
        "tomas":  {"nom": "Tomas",  "couleur": "#5ADC82", "freq": "DIGITAL PRÉCIS",
                   "c": +3, "f": -1, "d": +1,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_tomas.png"},
        "nyra":   {"nom": "Nyra",   "couleur": "#B4C8D2", "freq": "CHIRURGICAL",
                   "c": 0, "f": -1, "d": +3,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_nyra.png"},
        "iris":   {"nom": "Iris",   "couleur": "#FF6EA0", "freq": "PULSE TSUNDERE",
                   "c": -1, "f": 0, "d": +2,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_iris.png"},
        "julian": {"nom": "Julian", "couleur": "#F0C85A", "freq": "THÉÂTRAL DORÉ",
                   "c": +1, "f": +3, "d": -2,
                   "bonus": "",
                   "asset": "minijeu/signal_vivant_assets/chip_julian.png"},
    }

    J901_SV_CHIP_ORDER = ["ryn", "lysa", "elen", "mara", "noam", "tomas", "nyra", "iris", "julian"]

    # Bandes vertes par jauge
    J901_SV_GREEN_ZONES = {
        "clarte":     (55.0, 85.0),
        "force":      (45.0, 80.0),
        "discretion": (40.0, 70.0),
    }

    # Dialogue du débat
    J901_SV_DEBATE = [
        ("tomas",  "raison",      "Campements limenois : le Commandement IV peut s'appliquer à vous.",                                    "tomas"),
        ("noam",   "determine",   "La frontière est verrouillée. Dispersez-vous en groupes de moins de vingt. Maintenant.",              "noam"),
        ("ryn",    "colere",      "Vous m'entendez ?! Bougez ! Pas dans une minute. MAINTENANT !",                                         "ryn"),
        ("lysa",   "blase",       "Éloignez-vous des points de passage. Ne traversez pas. Ne restez pas groupés.",                         "lysa"),
        ("elen",   "peur",        "Enfants, blessés, retardataires : partez avec le groupe le plus proche. Tout de suite.",                "elen"),
        ("mara",   "stress",      "Version courte : oui, ils vont tirer. Donc on se sépare et on court.",                                  "mara"),
        ("tomas",  "culpabilite", "Même un vote pour ne couvrira pas les campements déjà formés. Vous devez bouger.",                     "tomas"),
        ("nyra",   "determine",   "Moins de vingt par groupe. Distance maximale entre vous. Gardez le signal ouvert.",                     "nyra"),
        ("iris",   "determine",   "Écoutez-nous, idiots. On n'a que quelques secondes pour vous garder en vie.",                           "iris"),
        ("julian", "determine",   "Limen ! Le Conclave vous regarde. Le monde vous regarde. SÉPAREZ-VOUS !",                              "julian"),
        ("noam",   "determine",   "Quatre fronts. Faites passer le message autour de vous. Personne ne reste en bloc.",                   "noam"),
        ("elen",   "joie",        "Ils bougent. Je les vois bouger. Continuez, continuez !",                                                "elen"),
        ("ryn",    "determine",   "Encore ! On tient jusqu'au bout et vous dégagez de là !",                                               "ryn"),
        ("noam",   "determine",   "Dernier relais. Si vous entendez cette voix : dispersez-vous maintenant.",                              "noam"),
    ]

    def j901_sv_reset():
        store.j901_sv_time_left = J901_SV_TOTAL_TIME
        store.j901_sv_done = False
        store.j901_sv_result_tier = "moyen"
        store.j901_sv_slots = [None, None, None, None]
        store.j901_sv_slot_power = [2, 2, 2, 2]
        store.j901_sv_g_clarte = 50.0
        store.j901_sv_g_force = 50.0
        store.j901_sv_g_discretion = 50.0
        store.j901_sv_target_clarte = 50.0
        store.j901_sv_target_force = 50.0
        store.j901_sv_target_discretion = 50.0
        store.j901_sv_wave = [0.0] * 60
        store.j901_sv_quad_offset = [0.0, 0.0, 0.0, 0.0]
        store.j901_sv_quad_cooldown = [0.0, 0.0, 0.0, 0.0]
        store.j901_sv_quad_disabled = [0.0, 0.0, 0.0, 0.0]
        store.j901_sv_quad_pulse_anim = [0.0, 0.0, 0.0, 0.0]
        store.j901_sv_quad_wave = [[0.0] * 16 for _ in range(4)]
        store.j901_sv_quad_urgency = [1.25, 1.10, 0.95, 1.35]
        store.j901_sv_pulse_count = 0
        store.j901_sv_orbs_killed = 0
        store.j901_sv_hits_taken = 0
        store.j901_sv_orbs = []
        store.j901_sv_orb_id_counter = 0
        store.j901_sv_next_orb = random.uniform(4.5, 6.0)
        store.j901_sv_mara_timer = 3.0
        store.j901_sv_global_disturb = 0.0
        store.j901_sv_debate_index = 0
        store.j901_sv_debate_next = 1.0
        store.j901_sv_current_speaker = "tomas"
        store.j901_sv_current_expr = "raison"
        store.j901_sv_current_line = "Le signal s'ouvre. Les campements vous écoutent."
        store.j901_sv_flash = 0.0
        store.j901_sv_kami_alert = ""
        store.j901_sv_kami_alert_time = 0.0
        store.j901_sv_warning = "ÉMISSION INITIÉE"
        store.j901_sv_status_color = "#7DF9FF"
        store.j901_sv_dots_safe = 0
        store.j901_sv_dots_lost = 0

    # ---- Gestion des slots de fréquences ----

    def j901_sv_place_chip(chip_key):
        if store.j901_sv_done:
            return
        slots = list(store.j901_sv_slots)
        if chip_key in slots:
            idx = slots.index(chip_key)
            slots[idx] = None
            store.j901_sv_warning = "FRÉQUENCE RETIRÉE"
        else:
            for i in range(len(slots)):
                if slots[i] is None:
                    slots[i] = chip_key
                    store.j901_sv_warning = "FRÉQUENCE ACTIVÉE"
                    break
            else:
                store.j901_sv_warning = "SLOTS PLEINS"
                store.j901_sv_status_color = "#FFD166"
                return
        store.j901_sv_slots = slots
        store.j901_sv_status_color = "#7DF9FF"

    def j901_sv_cycle_slot_power(slot_index):
        if store.j901_sv_done:
            return
        if store.j901_sv_slots[slot_index] is None:
            return
        powers = list(store.j901_sv_slot_power)
        powers[slot_index] = (powers[slot_index] % 3) + 1
        store.j901_sv_slot_power = powers
        store.j901_sv_warning = "INTENSITÉ " + str(powers[slot_index])

    def j901_sv_clear_slot(slot_index):
        if store.j901_sv_done:
            return
        if store.j901_sv_slots[slot_index] is None:
            return
        slots = list(store.j901_sv_slots)
        slots[slot_index] = None
        store.j901_sv_slots = slots

    # ---- Calculs de signal ----

    def j901_sv_compute_targets():
        c_sum = 0.0
        f_sum = 0.0
        d_sum = 0.0
        active = 0
        for i, k in enumerate(store.j901_sv_slots):
            if k is None or k not in J901_SV_CHIPS:
                continue
            ch = J901_SV_CHIPS[k]
            power = store.j901_sv_slot_power[i]
            mult = {1: 0.6, 2: 1.0, 3: 1.5}.get(power, 1.0)
            c_sum += ch["c"] * mult
            f_sum += ch["f"] * mult
            d_sum += ch["d"] * mult
            active += 1
        if active == 0:
            return 30.0, 25.0, 30.0
        clarte = 50.0 + c_sum * 7.0
        force = 35.0 + f_sum * 7.5
        discretion = 50.0 + d_sum * 6.5
        clarte = max(0.0, min(100.0, clarte))
        force = max(0.0, min(100.0, force))
        discretion = max(0.0, min(100.0, discretion))
        return clarte, force, discretion

    def j901_sv_in_green(name, value):
        lo, hi = J901_SV_GREEN_ZONES[name]
        return lo <= value <= hi

    def j901_sv_all_green():
        return (j901_sv_in_green("clarte", store.j901_sv_g_clarte)
                and j901_sv_in_green("force", store.j901_sv_g_force)
                and j901_sv_in_green("discretion", store.j901_sv_g_discretion))

    def j901_sv_signal_quality():
        # Renvoie 0..1 — multiplicateur global de vitesse de dispersion
        if j901_sv_all_green():
            return 1.0
        # Hors zone : dépend de la moyenne d'éloignement
        score = 0.0
        for name, val in [("clarte", store.j901_sv_g_clarte),
                          ("force", store.j901_sv_g_force),
                          ("discretion", store.j901_sv_g_discretion)]:
            lo, hi = J901_SV_GREEN_ZONES[name]
            if lo <= val <= hi:
                score += 1.0
            else:
                margin = min(abs(val - lo), abs(val - hi))
                score += max(0.0, 1.0 - margin / 30.0)
        return max(0.0, min(1.0, score / 3.0)) * 0.35  # max 0.35 en dehors

    # ---- Pulse sur quadrant ----

    def j901_sv_pulse_quad(q):
        if store.j901_sv_done:
            return
        if store.j901_sv_quad_cooldown[q] > 0.0:
            return
        if store.j901_sv_quad_disabled[q] > 0.0:
            store.j901_sv_warning = "QUADRANT HORS LIGNE"
            store.j901_sv_status_color = "#FF6B9A"
            return
        # Puissance de la pulse selon la qualité du signal
        quality = j901_sv_signal_quality()
        base = 14.0 + quality * 18.0
        # Bonus Julian (théâtral) : pulses x1.5
        if "julian" in store.j901_sv_slots:
            base *= 1.5
        # Bonus Iris : réduit le cooldown
        cooldown = 3.2
        if "iris" in store.j901_sv_slots:
            cooldown = 2.4
        offsets = list(store.j901_sv_quad_offset)
        offsets[q] = min(100.0, offsets[q] + base)
        store.j901_sv_quad_offset = offsets
        cooldowns = list(store.j901_sv_quad_cooldown)
        cooldowns[q] = cooldown
        store.j901_sv_quad_cooldown = cooldowns
        anims = list(store.j901_sv_quad_pulse_anim)
        anims[q] = 0.8
        store.j901_sv_quad_pulse_anim = anims
        store.j901_sv_pulse_count += 1
        store.j901_sv_warning = "PULSE → " + J901_SV_QUAD_RECTS[q][4]
        store.j901_sv_status_color = "#5DFF9A"

    # ---- Gestion des orbes ----

    def j901_sv_spawn_orb():
        elapsed = J901_SV_TOTAL_TIME - store.j901_sv_time_left
        # Type d'orbe selon le temps écoulé
        if elapsed < 12.0:
            type_choice = random.choices(["small", "medium"], weights=[0.7, 0.3])[0]
        elif elapsed < 28.0:
            type_choice = random.choices(["small", "medium", "large"], weights=[0.4, 0.45, 0.15])[0]
        else:
            type_choice = random.choices(["small", "medium", "large"], weights=[0.25, 0.45, 0.30])[0]
        # HP / taille
        type_data = {
            "small":  {"hp": 3, "size": 80,  "speed_mult": 1.0, "asset": "minijeu/signal_vivant_assets/orb_small.png"},
            "medium": {"hp": 4, "size": 110, "speed_mult": 0.85, "asset": "minijeu/signal_vivant_assets/orb_medium.png"},
            "large":  {"hp": 5, "size": 140, "speed_mult": 0.72, "asset": "minijeu/signal_vivant_assets/orb_large.png"},
        }[type_choice]
        # Cible : 80% chance sur un quadrant, 20% sur le centre
        if random.random() < 0.20:
            target_quad = None
            target_x, target_y = J901_SV_CENTER_TARGET
        else:
            target_quad = random.randint(0, 3)
            tcx, tcy = j901_sv_quad_center(target_quad)
            target_x = tcx
            target_y = tcy
        # Spawn depuis un bord aléatoire
        edge = random.choice(["top", "right", "bottom"])
        if edge == "top":
            sx = random.randint(150, 1800)
            sy = -100
        elif edge == "bottom":
            sx = random.randint(150, 1800)
            sy = 1180
        else:  # right
            sx = 2020
            sy = random.randint(150, 950)
        # Vitesse de base selon temps écoulé
        base_speed = 90.0 + (elapsed / J901_SV_TOTAL_TIME) * 130.0
        base_speed *= type_data["speed_mult"]
        dx = target_x - sx
        dy = target_y - sy
        dist = max(1.0, math.sqrt(dx * dx + dy * dy))
        vx = (dx / dist) * base_speed
        vy = (dy / dist) * base_speed
        store.j901_sv_orb_id_counter += 1
        orb = {
            "id": store.j901_sv_orb_id_counter,
            "x": float(sx),
            "y": float(sy),
            "vx": vx,
            "vy": vy,
            "hp": type_data["hp"],
            "max_hp": type_data["hp"],
            "size": type_data["size"],
            "asset": type_data["asset"],
            "target_quad": target_quad,
            "target_x": target_x,
            "target_y": target_y,
            "hit_flash": 0.0,
        }
        orbs = list(store.j901_sv_orbs)
        orbs.append(orb)
        store.j901_sv_orbs = orbs

    def j901_sv_hit_orb(orb_id):
        if store.j901_sv_done:
            return
        orbs = list(store.j901_sv_orbs)
        for i, orb in enumerate(orbs):
            if orb["id"] == orb_id:
                orb = dict(orb)
                orb["hp"] -= 1
                orb["hit_flash"] = 0.15
                orbs[i] = orb
                if orb["hp"] <= 0:
                    # Destruction
                    orbs.pop(i)
                    store.j901_sv_orbs_killed += 1
                    store.j901_sv_warning = "ORBE DÉTRUIT"
                    store.j901_sv_status_color = "#5DFF9A"
                break
        store.j901_sv_orbs = orbs

    def j901_sv_update_orbs(dt):
        orbs = list(store.j901_sv_orbs)
        survivors = []
        for orb in orbs:
            o = dict(orb)
            o["x"] += o["vx"] * dt
            o["y"] += o["vy"] * dt
            if o["hit_flash"] > 0.0:
                o["hit_flash"] = max(0.0, o["hit_flash"] - dt)
            dx = o["x"] - o["target_x"]
            dy = o["y"] - o["target_y"]
            d_sq = dx * dx + dy * dy
            # Collision avec cible
            if d_sq < 1200.0:  # ~35px
                if o["target_quad"] is None:
                    # Perturbation globale
                    store.j901_sv_global_disturb = 5.0
                    store.j901_sv_kami_alert = "FORME D'ONDE FRAPPÉE"
                    store.j901_sv_kami_alert_time = 2.2
                    store.j901_sv_flash = 0.35
                else:
                    # Désactive un quadrant
                    q = o["target_quad"]
                    duration = random.uniform(6.0, 9.0)
                    disabled = list(store.j901_sv_quad_disabled)
                    disabled[q] = duration
                    store.j901_sv_quad_disabled = disabled
                    store.j901_sv_kami_alert = J901_SV_QUAD_RECTS[q][4] + " TOUCHÉ — SIGNAL COUPÉ"
                    store.j901_sv_kami_alert_time = 2.2
                    store.j901_sv_flash = 0.35
                store.j901_sv_hits_taken += 1
                continue  # supprime l'orbe
            survivors.append(o)
        store.j901_sv_orbs = survivors

    # ---- Update dispersion par quadrant ----

    def j901_sv_update_quads(dt):
        all_green = j901_sv_all_green()
        quality = j901_sv_signal_quality()
        # Personnages actifs
        has_ryn = "ryn" in store.j901_sv_slots
        has_elen = "elen" in store.j901_sv_slots
        has_mara = "mara" in store.j901_sv_slots
        # Quadrants menacés (orbe en approche)
        threatened = set()
        for orb in store.j901_sv_orbs:
            if orb["target_quad"] is not None:
                threatened.add(orb["target_quad"])
        offsets = list(store.j901_sv_quad_offset)
        cooldowns = list(store.j901_sv_quad_cooldown)
        disabled = list(store.j901_sv_quad_disabled)
        anims = list(store.j901_sv_quad_pulse_anim)
        for q in range(4):
            # Cooldown
            if cooldowns[q] > 0:
                cooldowns[q] = max(0.0, cooldowns[q] - dt)
            # Animation
            if anims[q] > 0:
                anims[q] = max(0.0, anims[q] - dt)
            # Désactivation
            if disabled[q] > 0:
                disabled[q] = max(0.0, disabled[q] - dt)
                continue
            # Vitesse de base
            base_speed = 4.0 * quality + (1.4 if all_green else 0.0)
            mult = store.j901_sv_quad_urgency[q]
            if has_elen:
                mult += 0.25
            if has_ryn and q in threatened:
                mult += 0.5
            # Bonus Tomas : +10% si quadrant déjà bien parti (>40%)
            if "tomas" in store.j901_sv_slots and offsets[q] > 40.0:
                mult += 0.10
            offsets[q] = min(100.0, offsets[q] + base_speed * mult * dt)
        # Buzz Mara
        if has_mara:
            store.j901_sv_mara_timer -= dt
            if store.j901_sv_mara_timer <= 0:
                live_quads = [q for q in range(4) if disabled[q] <= 0]
                if live_quads:
                    q = random.choice(live_quads)
                    offsets[q] = min(100.0, offsets[q] + 4.5)
                    anims[q] = max(anims[q], 0.5)
                store.j901_sv_mara_timer = random.uniform(2.5, 4.0)
        store.j901_sv_quad_offset = offsets
        store.j901_sv_quad_cooldown = cooldowns
        store.j901_sv_quad_disabled = disabled
        store.j901_sv_quad_pulse_anim = anims

    # ---- Forme d'onde globale ----

    def j901_sv_update_wave(elapsed):
        force = store.j901_sv_g_force / 100.0
        clarte = store.j901_sv_g_clarte / 100.0
        wave = []
        glitch = 0.6 if store.j901_sv_global_disturb > 0.0 else 0.0
        for i in range(60):
            phase = elapsed * 4.0 + i * 0.5
            amp = 0.15 + force * 0.7
            sharpness = 1.0 + clarte * 1.8
            v = math.sin(phase * sharpness) * amp
            v += math.sin(phase * 0.5) * 0.15 * force
            if glitch > 0.0 and random.random() < glitch:
                v += random.uniform(-0.5, 0.5)
            if not j901_sv_all_green():
                v *= 0.6
            wave.append(max(-1.0, min(1.0, v)))
        store.j901_sv_wave = wave
        # Mini-ondes par quadrant
        quad_waves = []
        for q in range(4):
            qw = []
            disabled = store.j901_sv_quad_disabled[q] > 0
            for i in range(16):
                phase = elapsed * 6.0 + i * 0.6 + q * 1.4
                amp = 0.15 + (store.j901_sv_quad_offset[q] / 100.0) * 0.7
                v = math.sin(phase) * amp
                if disabled:
                    v = random.uniform(-0.2, 0.2)
                qw.append(max(-1.0, min(1.0, v)))
            quad_waves.append(qw)
        store.j901_sv_quad_wave = quad_waves

    def j901_sv_pick_speaker_from_chip(chip_key):
        if chip_key in store.j901_sv_slots:
            idx = store.j901_sv_slots.index(chip_key)
            powers = list(store.j901_sv_slot_power)
            powers[idx] = min(3, powers[idx] + 1)
            store.j901_sv_slot_power = powers

    # ---- Tick principal ----

    def j901_sv_tick():
        if store.j901_sv_done:
            return

        store.j901_sv_time_left = max(0.0, store.j901_sv_time_left - J901_SV_TICK)
        elapsed = J901_SV_TOTAL_TIME - store.j901_sv_time_left

        # Cibles
        tc, tf, td = j901_sv_compute_targets()
        store.j901_sv_target_clarte = tc
        store.j901_sv_target_force = tf
        store.j901_sv_target_discretion = td

        # Lerp
        lerp = 0.06
        store.j901_sv_g_clarte += (tc - store.j901_sv_g_clarte) * lerp
        store.j901_sv_g_force += (tf - store.j901_sv_g_force) * lerp
        store.j901_sv_g_discretion += (td - store.j901_sv_g_discretion) * lerp

        # Perturbation globale
        if store.j901_sv_global_disturb > 0.0:
            store.j901_sv_global_disturb -= J901_SV_TICK
            store.j901_sv_g_clarte += random.uniform(-2.2, 2.2)
            store.j901_sv_g_force += random.uniform(-2.2, 2.2)
            store.j901_sv_g_discretion += random.uniform(-2.2, 2.2)

        # Clamp
        store.j901_sv_g_clarte = max(0.0, min(100.0, store.j901_sv_g_clarte))
        store.j901_sv_g_force = max(0.0, min(100.0, store.j901_sv_g_force))
        store.j901_sv_g_discretion = max(0.0, min(100.0, store.j901_sv_g_discretion))

        # Status
        if store.j901_sv_kami_alert_time <= 0.0:
            if j901_sv_all_green():
                store.j901_sv_warning = "SIGNAL VIVANT"
                store.j901_sv_status_color = "#5DFF9A"
            elif store.j901_sv_g_clarte < 30.0:
                store.j901_sv_warning = "INCOMPRÉHENSIBLE"
                store.j901_sv_status_color = "#FFD166"
            elif store.j901_sv_g_force < 30.0:
                store.j901_sv_warning = "TROP FAIBLE"
                store.j901_sv_status_color = "#FFD166"
            elif store.j901_sv_g_discretion < 30.0:
                store.j901_sv_warning = "KAMI IRRITÉE"
                store.j901_sv_status_color = "#FF6B9A"
            elif store.j901_sv_g_clarte > 92.0 or store.j901_sv_g_force > 88.0:
                store.j901_sv_warning = "TROP VISIBLE"
                store.j901_sv_status_color = "#FF6B9A"
            else:
                store.j901_sv_warning = "INSTABLE"
                store.j901_sv_status_color = "#FFD166"

        # Mise à jour quadrants
        j901_sv_update_quads(J901_SV_TICK)

        # Mise à jour orbes
        j901_sv_update_orbs(J901_SV_TICK)

        # Mise à jour forme d'onde
        j901_sv_update_wave(elapsed)

        # Spawn d'orbes
        store.j901_sv_next_orb -= J901_SV_TICK
        if store.j901_sv_next_orb <= 0 and elapsed > 4.0:
            j901_sv_spawn_orb()
            if elapsed < 12.0:
                store.j901_sv_next_orb = random.uniform(6.0, 8.0)
            elif elapsed < 24.0:
                store.j901_sv_next_orb = random.uniform(4.8, 6.2)
            elif elapsed < 36.0:
                store.j901_sv_next_orb = random.uniform(3.6, 4.8)
            else:
                store.j901_sv_next_orb = random.uniform(2.8, 3.8)

        # Timer alerte
        if store.j901_sv_kami_alert_time > 0.0:
            store.j901_sv_kami_alert_time = max(0.0, store.j901_sv_kami_alert_time - J901_SV_TICK)
            if store.j901_sv_kami_alert_time == 0.0:
                store.j901_sv_kami_alert = ""

        if store.j901_sv_flash > 0.0:
            store.j901_sv_flash = max(0.0, store.j901_sv_flash - J901_SV_TICK)

        # Dialogue
        store.j901_sv_debate_next -= J901_SV_TICK
        if store.j901_sv_debate_next <= 0.0:
            if store.j901_sv_debate_index < len(J901_SV_DEBATE):
                speaker, expr, line, reinforce = J901_SV_DEBATE[store.j901_sv_debate_index]
                store.j901_sv_current_speaker = speaker
                store.j901_sv_current_expr = expr
                store.j901_sv_current_line = line
                j901_sv_pick_speaker_from_chip(reinforce)
                store.j901_sv_debate_index += 1
                store.j901_sv_debate_next = random.uniform(2.6, 3.4)
            else:
                idx = max(0, len(J901_SV_DEBATE) - random.randint(1, 6))
                speaker, expr, line, reinforce = J901_SV_DEBATE[idx]
                store.j901_sv_current_speaker = speaker
                store.j901_sv_current_expr = expr
                store.j901_sv_current_line = line
                j901_sv_pick_speaker_from_chip(reinforce)
                store.j901_sv_debate_next = random.uniform(2.6, 3.4)

        if store.j901_sv_time_left <= 0.0:
            j901_sv_finalize()

    def j901_sv_finalize():
        # Scoring : 3 dots par quadrant, sauvés selon le % de dispersion atteint.
        # Si quadrant désactivé au moment final, on applique un malus.
        safe = 0
        lost = 0
        for q in range(4):
            off = store.j901_sv_quad_offset[q]
            disabled = store.j901_sv_quad_disabled[q] > 0
            if disabled:
                off = max(0.0, off - 15.0)  # malus
            # Conversion en dots sauvés
            if off >= 75.0:
                quad_safe = 3
            elif off >= 55.0:
                quad_safe = 2
            elif off >= 30.0:
                quad_safe = 1
            else:
                quad_safe = 0
            # Risque résiduel (chance de perdre 1 dot supplémentaire)
            if quad_safe > 0 and off < 60.0:
                if random.random() < (60.0 - off) / 60.0 * 0.5:
                    quad_safe -= 1
            safe += quad_safe
            lost += (3 - quad_safe)
        store.j901_sv_dots_safe = safe
        store.j901_sv_dots_lost = lost
        if safe >= 10:
            store.j901_sv_result_tier = "excellent"
        elif safe >= 7:
            store.j901_sv_result_tier = "bon"
        elif safe >= 4:
            store.j901_sv_result_tier = "moyen"
        else:
            store.j901_sv_result_tier = "echec"
        store.j901_sv_done = True


# ------------------------------------------------------------
# Transforms
# ------------------------------------------------------------

transform j901_sv_chip_pulse:
    zoom 1.0
    linear 0.5 zoom 1.06
    linear 0.5 zoom 1.0
    repeat

transform j901_sv_alert_pulse:
    alpha 1.0
    linear 0.25 alpha 0.55
    linear 0.25 alpha 1.0
    repeat

transform j901_sv_shake_light:
    xoffset 0 yoffset 0
    linear 0.06 xoffset 2 yoffset -1
    linear 0.06 xoffset -2 yoffset 1
    linear 0.06 xoffset 0 yoffset 0
    pause 0.10
    repeat

transform j901_sv_speaker_in:
    alpha 0.0
    xoffset -30
    easeout 0.45 alpha 1.0 xoffset 0

transform j901_sv_orb_wobble:
    rotate 0
    linear 1.2 rotate 6
    linear 1.2 rotate -6
    repeat

transform j901_sv_pulse_ring_anim:
    alpha 0.95
    zoom 0.6
    easein 0.75 alpha 0.0 zoom 1.6

transform j901_sv_orb_hit_flash:
    alpha 1.0
    linear 0.08 alpha 0.35
    linear 0.08 alpha 1.0


# ------------------------------------------------------------
# Helpers d'affichage
# ------------------------------------------------------------

init python:
    def j901_sv_gauge_color(name, value):
        lo, hi = J901_SV_GREEN_ZONES[name]
        if lo <= value <= hi:
            return "#5DFF9A"
        margin = 10.0
        if (lo - margin) <= value <= (hi + margin):
            return "#FFD166"
        return "#FF4D6D"

    def j901_sv_quad_color(q):
        if store.j901_sv_quad_disabled[q] > 0.0:
            return "#FF4D6D"
        off = store.j901_sv_quad_offset[q]
        if off >= 70.0:
            return "#5DFF9A"
        if off >= 40.0:
            return "#FFD166"
        return "#7DF9FF"

    # Position des 3 campement-dots d'un quadrant selon son progress
    def j901_sv_dot_positions(q):
        rect = J901_SV_QUAD_RECTS[q]
        rx, ry, rw, rh = rect[0], rect[1], rect[2], rect[3]
        cx = rx + rw // 2
        cy = ry + rh // 2 + 30  # un peu sous le centre pour laisser la place au titre
        off = store.j901_sv_quad_offset[q]
        # Plus le progress est élevé, plus les dots s'écartent
        spread = 40.0 + (off / 100.0) * 100.0
        positions = []
        angles = [-2.4, -1.6, -0.8] if q < 2 else [0.8, 1.6, 2.4]
        # En haut → angles vers le haut, en bas → vers le bas
        angles = [math.pi * a / 2.0 for a in angles]
        for a in angles:
            dx = math.cos(a) * spread
            dy = math.sin(a) * spread
            positions.append((int(cx + dx), int(cy + dy)))
        return positions

    def j901_sv_dot_color(q):
        if store.j901_sv_quad_disabled[q] > 0.0:
            return "#FF4D6D"
        off = store.j901_sv_quad_offset[q]
        if off >= 60.0:
            return "#5DFF9A"
        if off >= 30.0:
            return "#FFD166"
        return "#FF4D6D"


# ------------------------------------------------------------
# Écran principal du minijeu
# ------------------------------------------------------------

screen j901_signal_vivant_screen():

    modal True
    zorder 300

    timer J901_SV_TICK repeat True action Function(j901_sv_tick)

    key "K_ESCAPE" action NullAction()

    # Raccourcis clavier 1..9 pour chips
    key "K_1" action Function(j901_sv_place_chip, "ryn")
    key "K_2" action Function(j901_sv_place_chip, "lysa")
    key "K_3" action Function(j901_sv_place_chip, "elen")
    key "K_4" action Function(j901_sv_place_chip, "mara")
    key "K_5" action Function(j901_sv_place_chip, "noam")
    key "K_6" action Function(j901_sv_place_chip, "tomas")
    key "K_7" action Function(j901_sv_place_chip, "nyra")
    key "K_8" action Function(j901_sv_place_chip, "iris")
    key "K_9" action Function(j901_sv_place_chip, "julian")

    # Raccourcis clavier A/Z/E/R pour pulse des quadrants
    key "K_a" action Function(j901_sv_pulse_quad, 0)
    key "K_z" action Function(j901_sv_pulse_quad, 1)
    key "K_e" action Function(j901_sv_pulse_quad, 2)
    key "K_r" action Function(j901_sv_pulse_quad, 3)

    add Solid("#02040A")

    # Flash d'alerte
    if j901_sv_flash > 0.0:
        add Solid("#FF334466")

    # ============================================
    # PANEAU GAUCHE — SALLE DU CONCLAVE (0..1152)
    # ============================================

    add "minijeu/signal_vivant_assets/bg_scope.png":
        xpos 0 ypos 110

    if renpy.has_image("bg_conclave"):
        add "bg_conclave":
            xpos 0 ypos 110
            xsize 1152
            ysize 430
            alpha 0.35

    fixed:
        xpos 0 ypos 110
        xsize 1152
        ysize 430

        add Solid("#02040A66")

        frame:
            xpos 20 ypos 16
            xsize 1112
            ysize 60
            background Solid("#0A1326CC")
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 30
                text "CONCLAVE — DIFFUSION EN DIRECT":
                    size 24
                    color "#DCF0FF"
                    bold True
                text "[j901_sv_current_speaker!c]":
                    size 24
                    color "#7DF9FF"
                    bold True

        $ _sv_speaker_image = j901_sv_current_speaker + " " + j901_sv_current_expr
        if renpy.has_image(_sv_speaker_image):
            add _sv_speaker_image at j901_sv_speaker_in:
                xpos 30 ypos 88
                zoom 0.55
        else:
            frame:
                xpos 60 ypos 100
                xsize 280
                ysize 280
                background Solid("#10172CDD")
                text "[j901_sv_current_speaker!c]":
                    xalign 0.5
                    yalign 0.5
                    size 56
                    color "#DCF0FF"
                    bold True

        frame:
            xpos 360 ypos 130
            xsize 760
            ysize 270
            background Solid("#0A132688")
            vbox:
                xalign 0.0
                yalign 0.0
                spacing 14
                xmaximum 720

                text "[j901_sv_current_speaker!c]":
                    size 30
                    color "#7DF9FF"
                    bold True

                text "[j901_sv_current_line]":
                    size 26
                    color "#FFFFFF"
                    xmaximum 720
                    text_align 0.0

    # ============================================
    # MONITEUR SIGNAL — forme d'onde + 3 jauges
    # ============================================

    fixed:
        xpos 0 ypos 540
        xsize 1152
        ysize 220

        add Solid("#03081599")

        text "FORME D'ONDE GLOBALE":
            xpos 24 ypos 12
            size 20
            color "#9FC7D8"
            bold True

        # Forme d'onde
        fixed:
            xpos 24 ypos 50
            xsize 720
            ysize 130

            add Solid("#06101FCC")
            add Solid("#7DF9FF55", xysize=(720, 1)) ypos 65

            for i, v in enumerate(j901_sv_wave):
                $ _bx = i * 12
                $ _bh = max(2, int(abs(v) * 55))
                $ _by = 65 - _bh // 2 if v >= 0 else 65
                if j901_sv_all_green() and j901_sv_global_disturb <= 0.0:
                    add Solid("#5DFF9A") xpos (_bx + 2) ypos _by xysize (8, _bh)
                else:
                    add Solid("#FF6B9A") xpos (_bx + 2) ypos _by xysize (8, _bh)

        # 3 jauges à droite
        vbox:
            xpos 770 ypos 50
            spacing 14

            for gname, glabel, gvalue in [
                ("clarte", "CLARTÉ", j901_sv_g_clarte),
                ("force", "FORCE", j901_sv_g_force),
                ("discretion", "DISCRÉTION", j901_sv_g_discretion),
            ]:
                vbox:
                    spacing 4
                    hbox:
                        spacing 12
                        text "[glabel]":
                            size 18
                            color "#DCF0FF"
                            bold True
                            xsize 130
                        text "[gvalue:.0f]":
                            size 18
                            color j901_sv_gauge_color(gname, gvalue)
                            bold True
                    fixed:
                        xsize 340
                        ysize 18

                        add Solid("#0A1326") xysize (340, 18)

                        $ _lo, _hi = J901_SV_GREEN_ZONES[gname]
                        $ _zx = int((_lo / 100.0) * 340)
                        $ _zw = int(((_hi - _lo) / 100.0) * 340)
                        add Solid("#26C96F33") xpos _zx ypos 0 xysize (_zw, 18)
                        add Solid("#26C96FAA") xpos _zx ypos 0 xysize (2, 18)
                        add Solid("#26C96FAA") xpos (_zx + _zw - 2) ypos 0 xysize (2, 18)

                        $ _cx = int((gvalue / 100.0) * 340)
                        add Solid("#FFFFFF") xpos (_cx - 2) ypos -2 xysize (4, 22)

    # ============================================
    # PANEAU MIXAGE (0..1152, 760..1080)
    # ============================================

    fixed:
        xpos 0 ypos 760
        xsize 1152
        ysize 320

        add Solid("#04091588")

        text "SLOTS ACTIFS":
            xpos 24 ypos 12
            size 20
            color "#9FC7D8"
            bold True

        text "(Chip 1..9 · Slot : intensité · Clic-droit : vider · A/Z/E/R : pulse quadrants)":
            xpos 180 ypos 16
            size 14
            color "#5F8090"

        for s_idx in range(4):
            $ _sx = 30 + s_idx * 210
            fixed:
                xpos _sx ypos 50
                xsize 200
                ysize 200

                $ _chip_key = j901_sv_slots[s_idx]
                if _chip_key is None:
                    imagebutton:
                        xpos 0 ypos 0
                        idle "minijeu/signal_vivant_assets/slot_empty.png"
                        hover "minijeu/signal_vivant_assets/slot_active.png"
                        action NullAction()
                    text "VIDE":
                        xalign 0.5
                        yalign 0.5
                        size 22
                        color "#5F8090"
                else:
                    button:
                        xpos 0 ypos 0
                        xsize 200
                        ysize 200
                        background "minijeu/signal_vivant_assets/slot_active.png"
                        hover_background "minijeu/signal_vivant_assets/slot_active.png"
                        action Function(j901_sv_cycle_slot_power, s_idx)
                        alternate Function(j901_sv_clear_slot, s_idx)

                    $ _chip_data = J901_SV_CHIPS[_chip_key]
                    $ _slot_power = j901_sv_slot_power[s_idx]
                    add _chip_data["asset"] at j901_sv_chip_pulse:
                        xalign 0.5 yalign 0.42
                        zoom 0.80

                    text "INTENSITÉ [_slot_power]/3":
                        xalign 0.5
                        ypos 165
                        size 16
                        color "#DCF0FF"
                        bold True

        text "PALETTE DE FRÉQUENCES":
            xpos 24 ypos 250
            size 18
            color "#9FC7D8"
            bold True

        for c_idx, c_key in enumerate(J901_SV_CHIP_ORDER):
            $ _cx_chip = 250 + c_idx * 90
            $ _data = J901_SV_CHIPS[c_key]
            $ _active = c_key in j901_sv_slots
            $ _chip_num = c_idx + 1
            $ _chip_bg = Solid("#10384DEE") if _active else Solid("#0F1A2EDD")

            fixed:
                xpos _cx_chip
                ypos 250
                xsize 80
                ysize 65

                button:
                    xpos 0
                    ypos 0
                    xsize 80
                    ysize 65
                    background _chip_bg
                    hover_background Solid("#1D2D52EE")
                    action Function(j901_sv_place_chip, c_key)

                add _data["asset"]:
                    xalign 0.5
                    yalign 0.4
                    zoom 0.36

                text "[_chip_num]":
                    xpos 4
                    ypos 2
                    size 12
                    color "#7DF9FF"
                    bold True

    # ============================================
    # PANEAU DROIT — 4 QUADRANTS (1152..1920)
    # ============================================

    add "minijeu/signal_vivant_assets/bg_campfield.png":
        xpos 1152 ypos 170

    add "minijeu/signal_vivant_assets/kami_shadow.png":
        xpos 1670 ypos 130
        alpha 0.22

    # Cadre titre
    frame:
        xpos 1152 ypos 110
        xsize 768
        ysize 56
        background Solid("#10172CDD")
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 2
            text "CARTE DES CAMPEMENTS — 4 FRONTS":
                xalign 0.5
                size 20
                color "#DCF0FF"
                bold True
            text "Clic quadrant : pulse renforcée  ·  Clic orbe : détruire":
                xalign 0.5
                size 14
                color "#7DF9FF"

    # Fond des 4 quadrants
    for q in range(4):
        $ _qrect = J901_SV_QUAD_RECTS[q]
        $ _qcode = _qrect[4].lower()
        add ("minijeu/signal_vivant_assets/quad_" + _qcode + ".png"):
            xpos _qrect[0] ypos _qrect[1]

    # Croix de séparation des quadrants
    add "minijeu/signal_vivant_assets/quad_cross.png":
        xpos 1152 ypos 170

    # Pour chaque quadrant : zone cliquable + infos + dots + mini-onde
    for q in range(4):
        $ _qrect = J901_SV_QUAD_RECTS[q]
        $ _qx, _qy, _qw, _qh = _qrect[0], _qrect[1], _qrect[2], _qrect[3]
        $ _qlabel = _qrect[4]
        $ _qfull = _qrect[5]
        $ _qoff = j901_sv_quad_offset[q]
        $ _qcooldown = j901_sv_quad_cooldown[q]
        $ _qdisabled = j901_sv_quad_disabled[q]
        $ _qcolor = j901_sv_quad_color(q)

        # Zone cliquable transparente (envoi pulse)
        if _qdisabled > 0.0:
            add "minijeu/signal_vivant_assets/slot_locked.png":
                xpos (_qx + _qw - 76) ypos (_qy + 12)
                zoom 0.3
        else:
            button:
                xpos _qx ypos _qy
                xsize _qw
                ysize _qh
                background Solid("#00000000")
                hover_background Solid("#7DF9FF15")
                action Function(j901_sv_pulse_quad, q)

        # Bandeau d'info en haut du quadrant
        frame:
            xpos (_qx + 8) ypos (_qy + 36)
            xsize (_qw - 16)
            ysize 46
            background Solid("#0A1326DD")
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 14
                text "[_qlabel]":
                    size 22
                    color "#DCF0FF"
                    bold True
                text "[_qoff:.0f]%":
                    size 26
                    color _qcolor
                    bold True
                text "URG x[j901_sv_quad_urgency[q]:.2f]":
                    size 14
                    color "#FFD166"
                if _qdisabled > 0.0:
                    text "OFF [_qdisabled:.0f]s":
                        size 16
                        color "#FF4D6D"
                        bold True
                elif _qcooldown > 0.0:
                    text "CD [_qcooldown:.1f]":
                        size 16
                        color "#FFD166"
                else:
                    text "READY":
                        size 16
                        color "#5DFF9A"
                        bold True

        # Mini-onde
        fixed:
            xpos (_qx + 30) ypos (_qy + 90)
            xsize 320
            ysize 70

            add Solid("#06101FAA")
            add Solid("#7DF9FF33", xysize=(320, 1)) ypos 35

            for i, v in enumerate(j901_sv_quad_wave[q]):
                $ _wx = i * 20
                $ _wh = max(2, int(abs(v) * 28))
                $ _wy = 35 - _wh // 2 if v >= 0 else 35
                add Solid(_qcolor) xpos (_wx + 2) ypos _wy xysize (16, _wh)

        # 3 dots de campement
        $ _positions = j901_sv_dot_positions(q)
        $ _dcolor = j901_sv_dot_color(q)
        for d_idx, pos in enumerate(_positions):
            $ _ddsize = 16 + int(_qoff / 10.0)
            # Position absolue à l'écran
            add Solid(_dcolor) xpos (pos[0] - _ddsize // 2) ypos (pos[1] - _ddsize // 2) xysize (_ddsize, _ddsize)
            # Halo
            $ _halo_size = _ddsize + 14
            add Solid(_dcolor + "33") xpos (pos[0] - _halo_size // 2) ypos (pos[1] - _halo_size // 2) xysize (_halo_size, _halo_size)

        # Animation de pulse réussie (anneau qui s'étend)
        $ _pulse_alpha = 0.85 if _qcooldown <= 0.0 and _qdisabled <= 0.0 else 0.35

        add "minijeu/signal_vivant_assets/pulse_button.png":
            xpos (_qx + _qw - 86)
            ypos (_qy + _qh - 86)
            zoom 0.35
            alpha _pulse_alpha

        if j901_sv_quad_pulse_anim[q] > 0.0:
            $ _qcx, _qcy = (_qx + _qw // 2), (_qy + _qh // 2 + 30)
            add "minijeu/signal_vivant_assets/pulse_ring.png" at j901_sv_pulse_ring_anim:
                xpos (_qcx - 120) ypos (_qcy - 120)

        # Voile sombre si désactivé
        if _qdisabled > 0.0:
            add Solid("#3A061266"):
                xpos _qx
                ypos _qy
                xysize (_qw, _qh)

            text "SIGNAL COUPÉ":
                xpos (_qx + _qw // 2 - 90)
                ypos (_qy + _qh // 2 - 14)
                size 26
                color "#FF4D6D"
                bold True
                outlines [(3, "#000000", 0, 0)]

    # ============================================
    # ORBES KAMI — affichés au-dessus de tout
    # ============================================

    for orb in j901_sv_orbs:
        $ _osize = orb["size"]
        $ _ox = int(orb["x"] - _osize // 2)
        $ _oy = int(orb["y"] - _osize // 2)
        $ _ohp = orb["hp"]
        $ _omax = orb["max_hp"]

        button:
            xpos _ox ypos _oy
            xsize _osize
            ysize _osize
            background Solid("#00000000")
            hover_background Solid("#FF6B9A22")
            action Function(j901_sv_hit_orb, orb["id"])

        if orb["hit_flash"] > 0.0:
            add orb["asset"] at j901_sv_orb_hit_flash:
                xpos _ox ypos _oy
        else:
            add orb["asset"] at j901_sv_orb_wobble:
                xpos _ox ypos _oy

        # Barre de HP au-dessus de l'orbe
        $ _bar_w = _osize - 16
        $ _bar_x = _ox + 8
        $ _bar_y = _oy - 16
        add Solid("#0A0010CC") xpos _bar_x ypos _bar_y xysize (_bar_w, 8)
        $ _hp_w = int(_bar_w * (_ohp / float(_omax)))
        add Solid("#FF6B9A") xpos _bar_x ypos _bar_y xysize (_hp_w, 8)
        text "[_ohp]/[_omax]":
            xpos _bar_x
            ypos (_bar_y - 18)
            size 14
            color "#FFFFFF"
            bold True

    # ============================================
    # BANDEAU SUPÉRIEUR
    # ============================================

    add "minijeu/signal_vivant_assets/title_band.png":
        xpos 0 ypos 0

    add "minijeu/signal_vivant_assets/badge_live.png":
        xpos 30 ypos 20
        at j901_sv_alert_pulse

    text "LE SIGNAL VIVANT":
        xpos 270 ypos 18
        size 40
        color "#FFFFFF"
        bold True

    text "Combinez les fréquences. Pulsez les quadrants. Détruisez les orbes de Kami.":
        xpos 270 ypos 66
        size 16
        color "#9FC7D8"

    text "TEMPS [j901_sv_time_left:.1f]s":
        xpos 1180 ypos 24
        size 24
        color "#7DF9FF"
        bold True

    text "[j901_sv_warning]":
        xpos 1180 ypos 58
        size 18
        color j901_sv_status_color
        bold True

    # Stats live
    $ _live_safe = 0
    for q in range(4):
        $ _q_off = j901_sv_quad_offset[q]
        if _q_off >= 75.0:
            $ _live_safe += 3
        elif _q_off >= 55.0:
            $ _live_safe += 2
        elif _q_off >= 30.0:
            $ _live_safe += 1

    text "SAUVÉS LIVE [_live_safe]/12":
        xpos 1540 ypos 24
        size 22
        color "#5DFF9A"
        bold True

    text "ORBES TUÉS [j901_sv_orbs_killed]  IMPACTS [j901_sv_hits_taken]":
        xpos 1540 ypos 58
        size 16
        color "#9FC7D8"

    # ============================================
    # ALERTE KAMI
    # ============================================

    if j901_sv_kami_alert_time > 0.0:
        frame:
            xalign 0.5
            yalign 0.21
            xsize 900
            ysize 80
            background Solid("#3A0612EE")
            at j901_sv_alert_pulse

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 2
                text "[j901_sv_kami_alert]":
                    xalign 0.5
                    size 28
                    color "#FFFFFF"
                    bold True

    if j901_sv_global_disturb > 0.0:
        add "minijeu/signal_vivant_assets/overlay_glitch.png":
            alpha 0.35
            at j901_sv_shake_light

    if j901_sv_done:
        timer 0.4 action Return(j901_sv_result_tier)


# ------------------------------------------------------------
# Écran de bilan final
# ------------------------------------------------------------

screen j901_signal_vivant_bilan(tier):

    modal True
    zorder 320

    add Solid("#020408EE")

    $ _safe = store.j901_sv_dots_safe
    $ _lost = store.j901_sv_dots_lost
    $ _orbs_killed = store.j901_sv_orbs_killed
    $ _hits = store.j901_sv_hits_taken
    $ _pulses = store.j901_sv_pulse_count

    $ _tier_label = {
        "excellent": "TRANSMISSION EXEMPLAIRE",
        "bon": "TRANSMISSION RÉUSSIE",
        "moyen": "TRANSMISSION PARTIELLE",
        "echec": "TRANSMISSION COUPÉE",
    }.get(tier, "BILAN")

    $ _tier_color = {
        "excellent": "#5DFF9A",
        "bon": "#7DF9FF",
        "moyen": "#FFD166",
        "echec": "#FF4D6D",
    }.get(tier, "#FFFFFF")

    $ _tier_msg = {
        "excellent": "Les quatre fronts ont reçu le signal. La majorité des campements s'est dispersée à temps. Kami semble presque impressionnée.",
        "bon":       "Le message est passé sur la plupart des fronts. Plusieurs campements ont entendu et se sont écartés des frontières.",
        "moyen":     "Le signal a vacillé. Plusieurs quadrants ont été coupés trop longtemps. Le Commandement a fait du dégât.",
        "echec":     "Le signal s'est éteint. Les orbes de Kami ont fait leur œuvre. Le Commandement IV s'est appliqué dans toute sa logique froide.",
    }.get(tier, "")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 720
        background Solid("#0A1326EE")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "BILAN DE TRANSMISSION":
                xalign 0.5
                size 28
                color "#9FC7D8"
                bold True

            text "[_tier_label]":
                xalign 0.5
                size 56
                color _tier_color
                bold True

            null height 8

            # Résultat par quadrant
            hbox:
                xalign 0.5
                spacing 30
                for q in range(4):
                    $ _qoff = store.j901_sv_quad_offset[q]
                    $ _qlabel = J901_SV_QUAD_RECTS[q][4]
                    $ _qcolor_b = j901_sv_quad_color(q)
                    vbox:
                        spacing 4
                        text "[_qlabel]":
                            xalign 0.5
                            size 22
                            color "#DCF0FF"
                            bold True
                        text "[_qoff:.0f]%":
                            xalign 0.5
                            size 40
                            color _qcolor_b
                            bold True

            null height 8

            hbox:
                xalign 0.5
                spacing 60

                vbox:
                    spacing 4
                    text "SAUVÉS":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_safe]/12":
                        xalign 0.5
                        size 56
                        color "#5DFF9A"
                        bold True

                vbox:
                    spacing 4
                    text "PERDUS":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_lost]/12":
                        xalign 0.5
                        size 56
                        color "#FF4D6D"
                        bold True

                vbox:
                    spacing 4
                    text "ORBES":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_orbs_killed]":
                        xalign 0.5
                        size 56
                        color "#7DF9FF"
                        bold True

                vbox:
                    spacing 4
                    text "PULSES":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_pulses]":
                        xalign 0.5
                        size 56
                        color "#FFD166"
                        bold True

            null height 10

            text "[_tier_msg]":
                xalign 0.5
                size 24
                color "#FFFFFF"
                xmaximum 1080
                text_align 0.5

            null height 10

            textbutton "Continuer":
                xalign 0.5
                xsize 280
                ysize 60
                background Solid("#10384DEE")
                hover_background Solid("#1D5C7AEE")
                text_size 28
                text_color "#FFFFFF"
                action Return(tier)


# ------------------------------------------------------------
# Label public
# ------------------------------------------------------------

screen j901_sv_howto():
    modal True
    zorder 310

    add Solid("#02040AEE")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 620
        background Solid("#0A1326EE")
        padding (50, 40)

        vbox:
            xalign 0.5
            spacing 22

            text "LE SIGNAL VIVANT — BRIEFING":
                xalign 0.5
                size 40
                color "#DCF0FF"
                bold True

            add Solid("#7DF9FF66", xsize=960, ysize=2) xalign 0.5

            vbox:
                spacing 16
                text "1.  FRÉQUENCES — Place jusqu'à 4 voix dans les slots (touches 1-9). Garde les trois jauges (Clarté, Force, Discrétion) dans le vert.":
                    size 26 color "#DCF0FF" xmaximum 980
                text "2.  PULSES — Clique un quadrant (ou A/Z/E/R) pour booster la dispersion des campements. Cooldown entre deux pulses.":
                    size 26 color "#DCF0FF" xmaximum 980
                text "3.  ORBES DE KAMI — Clique plusieurs fois les orbes noirs avant qu'ils ne frappent un quadrant ou la forme d'onde.":
                    size 26 color "#DCF0FF" xmaximum 980
                text "Objectif : disperser un maximum de campements en 45 secondes.":
                    size 26 color "#FFD166" bold True xmaximum 980

            null height 10

            textbutton "LANCER LA TRANSMISSION":
                xalign 0.5
                xsize 440
                ysize 64
                background Solid("#10384DEE")
                hover_background Solid("#1D5C7AEE")
                text_size 26
                text_color "#FFFFFF"
                text_xalign 0.5
                action Return(True)

label j901_play_signal_vivant:

    $ j901_sv_reset()
    call screen j901_sv_howto
    $ _sv_tier = renpy.call_screen("j901_signal_vivant_screen")
    $ _sv_final_tier = renpy.call_screen("j901_signal_vivant_bilan", tier=_sv_tier)
    return _sv_final_tier
