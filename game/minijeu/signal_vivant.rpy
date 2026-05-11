# ============================================================
# MINI-JEU JOUR 9_0_1 — LE SIGNAL VIVANT
#
# Contexte : pendant le débat du Conclave (label _9_0_1_CONCLAVE_DEBAT),
# Noam doit maintenir vivant un signal de transmission pour que le
# message de dispersion atteigne les campements aux frontières.
#
# Mécanique :
# - 9 personnages = 9 fréquences uniques
# - 4 slots actifs : on combine les fréquences pour façonner le signal
# - 3 jauges à maintenir dans la bande verte : Clarté, Force, Discrétion
# - Kami envoie des interférences (parasites, polarité, ombre, brouillage)
# - 12 campements aux frontières : ils se dispersent ou ils meurent
#
# Durée : 240 secondes (~4 min).
#
# Appel scénario :
#   call j901_play_signal_vivant
#   $ j901_signal_result_tier = _return
#
# Le label renvoie une string : "excellent" / "bon" / "moyen" / "echec".
# ============================================================


# ------------------------------------------------------------
# Variables d'état
# ------------------------------------------------------------

default j901_sv_time_left = 240.0
default j901_sv_done = False
default j901_sv_result_tier = "moyen"

# Slots actifs : 4 slots, chacun contient soit None soit la clé d'un perso
default j901_sv_slots = [None, None, None, None]
# Intensité par slot (1, 2 ou 3) - se clique pour cycler
default j901_sv_slot_power = [2, 2, 2, 2]

# Jauges courantes 0..100
default j901_sv_g_clarte = 50.0
default j901_sv_g_force = 50.0
default j901_sv_g_discretion = 50.0

# Cibles (calculées en continu d'après les slots actifs)
default j901_sv_target_clarte = 50.0
default j901_sv_target_force = 50.0
default j901_sv_target_discretion = 50.0

# Etat de l'interférence en cours
default j901_sv_inter_type = ""        # "", "parasites", "polarite", "ombre", "brouillage"
default j901_sv_inter_time = 0.0       # temps restant de l'interférence
default j901_sv_inter_target = ""      # cible secondaire (jauge ou perso)
default j901_sv_next_inter = 16.0      # délai avant la prochaine interférence
default j901_sv_locked_chip = ""       # chip verrouillé par "brouillage"

# Forme d'onde (60 valeurs entre -1 et 1)
default j901_sv_wave = [0.0] * 60

# Dispersion : 12 campements, chacun a un offset (0..100). Au-dessus de 60 = dispersé.
default j901_sv_camp_offsets = [0.0] * 12
default j901_sv_camp_alive = [True] * 12     # False = éteint (massacre)
default j901_sv_dispersion_progress = 0.0    # accumule quand 3 jauges en vert

# Dialogue du débat (auto-déroulé sur fond de minijeu)
default j901_sv_debate_index = 0
default j901_sv_debate_next = 2.0   # délai avant la prochaine réplique
default j901_sv_current_speaker = "tomas"
default j901_sv_current_expr = "raison"
default j901_sv_current_line = "Le débat est ouvert. Mesdames et messieurs..."

# Effets visuels
default j901_sv_flash = 0.0
default j901_sv_shake = 0
default j901_sv_kami_alert = ""
default j901_sv_kami_alert_time = 0.0
default j901_sv_warning = "ÉMISSION INITIÉE"
default j901_sv_status_color = "#7DF9FF"

# Stats finales
default j901_sv_disp_count = 0
default j901_sv_danger_count = 0
default j901_sv_dead_count = 0


# ------------------------------------------------------------
# Logique Python
# ------------------------------------------------------------

init python:
    import random
    import math

    J901_SV_TICK = 0.05
    J901_SV_TOTAL_TIME = 240.0

    # Chaque chip : key, nom court, couleur, contributions à (Clarté, Force, Discrétion)
    # Valeurs entre -3 et +3 par fréquence (avant intensité)
    J901_SV_CHIPS = {
        "ryn":    {"nom": "Ryn",    "couleur": "#D2283C", "freq": "BASSE GRAVE",
                   "c": -1, "f": +3, "d": -2,
                   "asset": "minijeu/signal_vivant_assets/chip_ryn.png"},
        "lysa":   {"nom": "Lysa",   "couleur": "#5AAAF0", "freq": "CLAIRE FROIDE",
                   "c": +3, "f": -1, "d": +1,
                   "asset": "minijeu/signal_vivant_assets/chip_lysa.png"},
        "elen":   {"nom": "Elen",   "couleur": "#FFC850", "freq": "HAUTE ÉMOTIONNELLE",
                   "c": +1, "f": +2, "d": -1,
                   "asset": "minijeu/signal_vivant_assets/chip_elen.png"},
        "mara":   {"nom": "Mara",   "couleur": "#B446E6", "freq": "PARASITE CHAOS",
                   "c": -2, "f": +2, "d": -1,
                   "asset": "minijeu/signal_vivant_assets/chip_mara.png"},
        "noam":   {"nom": "Noam",   "couleur": "#DCF0FF", "freq": "PORTEUSE STABLE",
                   "c": +1, "f": 0, "d": +1,
                   "asset": "minijeu/signal_vivant_assets/chip_noam.png"},
        "tomas":  {"nom": "Tomas",  "couleur": "#5ADC82", "freq": "DIGITAL PRÉCIS",
                   "c": +3, "f": -1, "d": +1,
                   "asset": "minijeu/signal_vivant_assets/chip_tomas.png"},
        "nyra":   {"nom": "Nyra",   "couleur": "#B4C8D2", "freq": "CHIRURGICAL",
                   "c": 0, "f": -1, "d": +3,
                   "asset": "minijeu/signal_vivant_assets/chip_nyra.png"},
        "iris":   {"nom": "Iris",   "couleur": "#FF6EA0", "freq": "PULSE TSUNDERE",
                   "c": -1, "f": 0, "d": +2,
                   "asset": "minijeu/signal_vivant_assets/chip_iris.png"},
        "julian": {"nom": "Julian", "couleur": "#F0C85A", "freq": "THÉÂTRAL DORÉ",
                   "c": +1, "f": +3, "d": -2,
                   "asset": "minijeu/signal_vivant_assets/chip_julian.png"},
    }

    J901_SV_CHIP_ORDER = ["ryn", "lysa", "elen", "mara", "noam", "tomas", "nyra", "iris", "julian"]

    # Bandes vertes par jauge (min, max).
    J901_SV_GREEN_ZONES = {
        "clarte":     (55.0, 85.0),
        "force":      (45.0, 80.0),
        "discretion": (40.0, 70.0),
    }

    # Dialogue du débat (texte qui défile pendant que Noam joue avec le signal)
    # Chaque entrée : (speaker, expression, ligne, "renforce_chip")
    J901_SV_DEBATE = [
        ("tomas",  "raison",      "Le présent amendement vise à autoriser les regroupements de plus de vingt personnes…",                "tomas"),
        ("tomas",  "raison",      "Les campements actuels relèvent du Commandement IV.",                                                   "tomas"),
        ("noam",   "determine",   "Aux campements limenois qui nous écoutent : la frontière est verrouillée.",                            "noam"),
        ("noam",   "determine",   "Dispersez-vous en groupes de moins de vingt. Maintenant.",                                              "noam"),
        ("ryn",    "colere",      "ILS ENTENDENT TOUS ! Vous m'entendez ?! Bougez ! BOUGEZ !",                                             "ryn"),
        ("ryn",    "colere2",     "Pas la peine d'attendre une autorisation qui ne viendra jamais !",                                     "ryn"),
        ("lysa",   "blase",       "Concrètement : éloignez-vous des points de passage. Ne traversez pas.",                                "lysa"),
        ("lysa",   "triste",      "Personne ne viendra vous chercher. Sauvez-vous vous-mêmes.",                                            "lysa"),
        ("elen",   "peur",        "Je vous en supplie. Si vous avez des enfants, des blessés, partez maintenant.",                        "elen"),
        ("elen",   "determine",   "On vous écoute. Le monde entier vous écoute. Tenez bon.",                                              "elen"),
        ("mara",   "stress",      "Ils vont vraiment tirer. Mara au micro : OUI ils vont vraiment tirer.",                                "mara"),
        ("mara",   "rire",        "Si vous voulez un canon dans la gueule, restez en gros tas !",                                          "mara"),
        ("tomas",  "raison",      "Préalable : avant. Les campements existants ne sont pas couverts par l'amendement.",                   "tomas"),
        ("tomas",  "culpabilite", "Même si vous votez pour. Même unanime. Vous devez bouger.",                                             "tomas"),
        ("nyra",   "raison",      "Précisément : moins de vingt par groupe, à plus de trois cents mètres des frontières.",                "nyra"),
        ("nyra",   "determine",   "Pas de panique. Méthode. Vous avez le temps si vous commencez maintenant.",                            "nyra"),
        ("iris",   "fatigue",     "Sérieux ? On va vraiment leur sauver la vie en parlant à un écran ?",                                  "iris"),
        ("iris",   "determine",   "Bah… oui. On va le faire. Tant pis. Écoutez-nous, idiots.",                                            "iris"),
        ("julian", "determine",   "Habitants des campements ! Citoyens de Limen ! C'est à VOUS que je parle !",                          "julian"),
        ("julian", "inquietude",  "Le Conclave vous regarde. Le monde vous regarde. SÉPAREZ-VOUS !",                                      "julian"),
        ("noam",   "determine",   "Cinq minutes. Vous avez cinq minutes pour décider. Pas plus.",                                          "noam"),
        ("ryn",    "determine",   "Allez ! ALLEZ ! On n'arrêtera pas de répéter !",                                                        "ryn"),
        ("tomas",  "raison",      "Je répète le détail juridique. Lentement. Pour ceux qui transcrivent là-bas.",                         "tomas"),
        ("lysa",   "determine",   "Et pour ceux qui regardent : c'est ce qu'on appelle un sauvetage par diffusion publique.",             "lysa"),
        ("elen",   "joie",        "On les voit bouger. Sur les écrans. Ça marche. ÇA MARCHE.",                                            "elen"),
        ("noam",   "determine",   "Continuez. Encore. Le signal doit tenir jusqu'à la dernière personne.",                                "noam"),
    ]

    # Interférences possibles
    J901_SV_INTERFERENCES = [
        {"type": "parasites",  "label": "PARASITES VISUELS",      "duree": 4.0},
        {"type": "polarite",   "label": "POLARITÉ INVERSÉE",      "duree": 4.5},
        {"type": "ombre",      "label": "OMBRE KAMI",             "duree": 5.5},
        {"type": "brouillage", "label": "BROUILLAGE FRÉQUENTIEL", "duree": 6.0},
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
        store.j901_sv_inter_type = ""
        store.j901_sv_inter_time = 0.0
        store.j901_sv_inter_target = ""
        store.j901_sv_next_inter = random.uniform(13.0, 18.0)
        store.j901_sv_locked_chip = ""
        store.j901_sv_wave = [0.0] * 60
        store.j901_sv_camp_offsets = [0.0] * 12
        store.j901_sv_camp_alive = [True] * 12
        store.j901_sv_dispersion_progress = 0.0
        store.j901_sv_debate_index = 0
        store.j901_sv_debate_next = 2.0
        store.j901_sv_current_speaker = "tomas"
        store.j901_sv_current_expr = "raison"
        store.j901_sv_current_line = "Le débat commence. Les campements vous écoutent."
        store.j901_sv_flash = 0.0
        store.j901_sv_shake = 0
        store.j901_sv_kami_alert = ""
        store.j901_sv_kami_alert_time = 0.0
        store.j901_sv_warning = "ÉMISSION INITIÉE"
        store.j901_sv_status_color = "#7DF9FF"
        store.j901_sv_disp_count = 0
        store.j901_sv_danger_count = 0
        store.j901_sv_dead_count = 0

    def j901_sv_place_chip(chip_key):
        """Clique sur un chip : le place dans le 1er slot libre, ou le retire s'il est déjà dedans."""
        if store.j901_sv_done:
            return
        if chip_key == store.j901_sv_locked_chip:
            store.j901_sv_warning = "FRÉQUENCE BROUILLÉE"
            store.j901_sv_status_color = "#FF6B9A"
            store.j901_sv_flash = 0.15
            return
        slots = list(store.j901_sv_slots)
        if chip_key in slots:
            # Retire
            idx = slots.index(chip_key)
            slots[idx] = None
            store.j901_sv_warning = "FRÉQUENCE RETIRÉE"
        else:
            # Place dans 1er slot libre
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
        """Clique sur un slot : si plein, cycle l'intensité 1->2->3->1. Si vide, ignore."""
        if store.j901_sv_done:
            return
        if store.j901_sv_slots[slot_index] is None:
            return
        powers = list(store.j901_sv_slot_power)
        powers[slot_index] = (powers[slot_index] % 3) + 1
        store.j901_sv_slot_power = powers
        store.j901_sv_warning = "INTENSITÉ " + str(powers[slot_index])

    def j901_sv_clear_slot(slot_index):
        """Clear droit (ou bouton dédié) : retire le chip d'un slot."""
        if store.j901_sv_done:
            return
        if store.j901_sv_slots[slot_index] is None:
            return
        slots = list(store.j901_sv_slots)
        slots[slot_index] = None
        store.j901_sv_slots = slots

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
        # Base 50 + accumulation
        clarte = 50.0 + c_sum * 7.0
        force = 35.0 + f_sum * 7.5
        discretion = 50.0 + d_sum * 6.5
        # Polarité inversée : on flip les delta par rapport à 50
        if store.j901_sv_inter_type == "polarite":
            clarte = 100.0 - clarte
            force = 100.0 - force
            discretion = 100.0 - discretion
        # Clamp doux
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

    def j901_sv_spawn_interference():
        inter = random.choice(J901_SV_INTERFERENCES)
        store.j901_sv_inter_type = inter["type"]
        store.j901_sv_inter_time = inter["duree"]
        store.j901_sv_kami_alert = "KAMI INTERFÈRE : " + inter["label"]
        store.j901_sv_kami_alert_time = 2.5
        store.j901_sv_flash = 0.35
        store.j901_sv_shake = 4
        store.j901_sv_status_color = "#FF6B9A"
        if inter["type"] == "ombre":
            store.j901_sv_inter_target = random.choice(["clarte", "force", "discretion"])
        elif inter["type"] == "brouillage":
            # Verrouille un chip aléatoire parmi ceux actuellement placés (ou n'importe lequel)
            placed = [k for k in store.j901_sv_slots if k]
            pool = placed if placed else J901_SV_CHIP_ORDER
            store.j901_sv_locked_chip = random.choice(pool)
            store.j901_sv_inter_target = store.j901_sv_locked_chip
            # Si verrouillé alors qu'en slot : on le retire
            slots = list(store.j901_sv_slots)
            if store.j901_sv_locked_chip in slots:
                idx = slots.index(store.j901_sv_locked_chip)
                slots[idx] = None
                store.j901_sv_slots = slots
        else:
            store.j901_sv_inter_target = ""

    def j901_sv_end_interference():
        store.j901_sv_inter_type = ""
        store.j901_sv_inter_time = 0.0
        store.j901_sv_locked_chip = ""
        store.j901_sv_inter_target = ""
        store.j901_sv_kami_alert = "INTERFÉRENCE NEUTRALISÉE"
        store.j901_sv_kami_alert_time = 1.5
        store.j901_sv_status_color = "#7DF9FF"

    def j901_sv_update_wave(elapsed):
        # Forme d'onde basée sur Force et Clarté
        force = store.j901_sv_g_force / 100.0
        clarte = store.j901_sv_g_clarte / 100.0
        wave = []
        glitch = 0.0
        if store.j901_sv_inter_type == "parasites":
            glitch = 0.6
        elif store.j901_sv_inter_type == "ombre":
            glitch = 0.25
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

    def j901_sv_update_camps(dt):
        # Si signal bon : les points s'éloignent.
        # Si signal coupé (clarté trop basse) : risque de mort.
        camps = list(store.j901_sv_camp_offsets)
        alive = list(store.j901_sv_camp_alive)
        all_green = j901_sv_all_green()
        clarte = store.j901_sv_g_clarte
        force = store.j901_sv_g_force
        for i in range(len(camps)):
            if not alive[i]:
                continue
            if all_green:
                # Vitesse de dispersion proportionnelle à la force du signal
                gain = (force / 100.0) * 3.0 * dt
                camps[i] = min(100.0, camps[i] + gain)
            elif clarte < 25.0 and force < 25.0:
                # Signal coupé : les campements ne bougent plus, et risque de mort
                if random.random() < 0.0008:
                    alive[i] = False
            else:
                # Signal moyen : dérive lente
                gain = 0.3 * dt
                camps[i] = min(100.0, camps[i] + gain)
        # Pendant l'ombre Kami, peut éteindre brutalement un campement
        if store.j901_sv_inter_type == "ombre" and random.random() < 0.0025:
            living = [i for i, a in enumerate(alive) if a and camps[i] < 60.0]
            if living:
                idx = random.choice(living)
                alive[idx] = False
                store.j901_sv_warning = "CAMPEMENT TOUCHÉ"
                store.j901_sv_status_color = "#FF4D6D"
                store.j901_sv_flash = 0.3
        store.j901_sv_camp_offsets = camps
        store.j901_sv_camp_alive = alive

    def j901_sv_pick_speaker_from_chip(chip_key):
        # Quand une réplique est diffusée, on renforce le chip correspondant SI il est placé.
        # Sinon on ne fait que de l'affichage.
        if chip_key in store.j901_sv_slots:
            idx = store.j901_sv_slots.index(chip_key)
            powers = list(store.j901_sv_slot_power)
            # Boost temporaire : +1 intensité (clampé à 3) pour 2 sec
            powers[idx] = min(3, powers[idx] + 1)
            store.j901_sv_slot_power = powers

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

        # Lerp des jauges vers les cibles
        lerp = 0.06
        store.j901_sv_g_clarte += (tc - store.j901_sv_g_clarte) * lerp
        store.j901_sv_g_force += (tf - store.j901_sv_g_force) * lerp
        store.j901_sv_g_discretion += (td - store.j901_sv_g_discretion) * lerp

        # Effets d'interférence sur les jauges
        if store.j901_sv_inter_type == "parasites":
            store.j901_sv_g_clarte += random.uniform(-1.6, 1.6)
            store.j901_sv_g_force += random.uniform(-1.6, 1.6)
            store.j901_sv_g_discretion += random.uniform(-1.6, 1.6)
        elif store.j901_sv_inter_type == "ombre":
            tgt = store.j901_sv_inter_target
            if tgt == "clarte":
                store.j901_sv_g_clarte = max(0.0, store.j901_sv_g_clarte - 0.6)
            elif tgt == "force":
                store.j901_sv_g_force = max(0.0, store.j901_sv_g_force - 0.6)
            elif tgt == "discretion":
                store.j901_sv_g_discretion = max(0.0, store.j901_sv_g_discretion - 0.6)

        # Clamp
        store.j901_sv_g_clarte = max(0.0, min(100.0, store.j901_sv_g_clarte))
        store.j901_sv_g_force = max(0.0, min(100.0, store.j901_sv_g_force))
        store.j901_sv_g_discretion = max(0.0, min(100.0, store.j901_sv_g_discretion))

        # Dispersion progress quand 3 en vert
        if j901_sv_all_green():
            store.j901_sv_dispersion_progress = min(100.0, store.j901_sv_dispersion_progress + J901_SV_TICK * 3.5)
            if store.j901_sv_kami_alert_time <= 0.0:
                store.j901_sv_warning = "SIGNAL VIVANT"
                store.j901_sv_status_color = "#5DFF9A"
        else:
            if store.j901_sv_kami_alert_time <= 0.0:
                if store.j901_sv_g_clarte < 30.0:
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

        # Mise à jour campements
        j901_sv_update_camps(J901_SV_TICK)

        # Mise à jour forme d'onde
        j901_sv_update_wave(elapsed)

        # Gestion interférences
        if store.j901_sv_inter_type:
            store.j901_sv_inter_time -= J901_SV_TICK
            if store.j901_sv_inter_time <= 0.0:
                j901_sv_end_interference()
        else:
            store.j901_sv_next_inter -= J901_SV_TICK
            if store.j901_sv_next_inter <= 0.0 and elapsed > 8.0:
                j901_sv_spawn_interference()
                store.j901_sv_next_inter = random.uniform(14.0, 19.0)

        # Timer d'alerte
        if store.j901_sv_kami_alert_time > 0.0:
            store.j901_sv_kami_alert_time = max(0.0, store.j901_sv_kami_alert_time - J901_SV_TICK)
            if store.j901_sv_kami_alert_time == 0.0:
                store.j901_sv_kami_alert = ""

        # Flash decay
        if store.j901_sv_flash > 0.0:
            store.j901_sv_flash = max(0.0, store.j901_sv_flash - J901_SV_TICK)
        if store.j901_sv_shake > 0:
            store.j901_sv_shake = max(0, store.j901_sv_shake - 1)

        # Auto-diffusion des répliques de débat
        store.j901_sv_debate_next -= J901_SV_TICK
        if store.j901_sv_debate_next <= 0.0:
            if store.j901_sv_debate_index < len(J901_SV_DEBATE):
                speaker, expr, line, reinforce = J901_SV_DEBATE[store.j901_sv_debate_index]
                store.j901_sv_current_speaker = speaker
                store.j901_sv_current_expr = expr
                store.j901_sv_current_line = line
                j901_sv_pick_speaker_from_chip(reinforce)
                store.j901_sv_debate_index += 1
                store.j901_sv_debate_next = random.uniform(7.5, 10.5)
            else:
                # En boucle sur les 6 dernières lignes pour ne pas avoir de vide
                idx = max(0, len(J901_SV_DEBATE) - random.randint(1, 6))
                speaker, expr, line, reinforce = J901_SV_DEBATE[idx]
                store.j901_sv_current_speaker = speaker
                store.j901_sv_current_expr = expr
                store.j901_sv_current_line = line
                j901_sv_pick_speaker_from_chip(reinforce)
                store.j901_sv_debate_next = random.uniform(7.5, 10.5)

        # Fin du minijeu
        if store.j901_sv_time_left <= 0.0:
            j901_sv_finalize()

    def j901_sv_finalize():
        # Comptage final
        disp = 0
        danger = 0
        dead = 0
        for off, alive in zip(store.j901_sv_camp_offsets, store.j901_sv_camp_alive):
            if not alive:
                dead += 1
            elif off >= 60.0:
                disp += 1
            else:
                danger += 1
        # Application du Commandement : les campements encore "en danger" subissent
        # une chance de mort proportionnelle au manque de dispersion.
        new_dead = 0
        for i, (off, alive) in enumerate(zip(store.j901_sv_camp_offsets, store.j901_sv_camp_alive)):
            if not alive:
                continue
            if off < 60.0:
                # Plus l'offset est faible, plus le risque est haut
                risk = (60.0 - off) / 60.0  # 0..1
                if random.random() < risk * 0.75:
                    store.j901_sv_camp_alive[i] = False
                    new_dead += 1
        # Recomptage
        disp = 0
        danger = 0
        dead = 0
        for off, alive in zip(store.j901_sv_camp_offsets, store.j901_sv_camp_alive):
            if not alive:
                dead += 1
            elif off >= 60.0:
                disp += 1
            else:
                danger += 1
        store.j901_sv_disp_count = disp
        store.j901_sv_danger_count = danger
        store.j901_sv_dead_count = dead
        # Tier
        if disp >= 9:
            store.j901_sv_result_tier = "excellent"
        elif disp >= 6:
            store.j901_sv_result_tier = "bon"
        elif disp >= 3:
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

transform j901_sv_shake_hard:
    xoffset 0 yoffset 0
    linear 0.04 xoffset 6 yoffset -3
    linear 0.04 xoffset -5 yoffset 3
    linear 0.04 xoffset 3 yoffset -2
    linear 0.04 xoffset 0 yoffset 0
    pause 0.08
    repeat

transform j901_sv_speaker_in:
    alpha 0.0
    xoffset -30
    easeout 0.45 alpha 1.0 xoffset 0


# ------------------------------------------------------------
# Helpers d'affichage
# ------------------------------------------------------------

init python:
    def j901_sv_gauge_color(name, value):
        lo, hi = J901_SV_GREEN_ZONES[name]
        if lo <= value <= hi:
            return "#5DFF9A"
        # Hors zone verte mais proche
        margin = 10.0
        if (lo - margin) <= value <= (hi + margin):
            return "#FFD166"
        return "#FF4D6D"

    def j901_sv_camp_color(idx):
        if not store.j901_sv_camp_alive[idx]:
            return "#3A0612"
        off = store.j901_sv_camp_offsets[idx]
        if off >= 60.0:
            return "#5DFF9A"
        if off >= 30.0:
            return "#FFD166"
        return "#FF4D6D"

    def j901_sv_camp_size(idx):
        if not store.j901_sv_camp_alive[idx]:
            return 8
        off = store.j901_sv_camp_offsets[idx]
        return int(10 + off / 12.0)

    # Position d'origine des campements (grille 4x3 dans le pane droit)
    J901_SV_CAMP_BASE = []
    for row in range(3):
        for col in range(4):
            J901_SV_CAMP_BASE.append((
                int(140 + col * 130),
                int(120 + row * 240),
            ))

    def j901_sv_camp_pos(idx):
        bx, by = J901_SV_CAMP_BASE[idx]
        off = store.j901_sv_camp_offsets[idx]
        # Direction radiale depuis le centre du pane (380, 480) vers le point initial
        cx, cy = 380.0, 420.0
        dx = bx - cx
        dy = by - cy
        # Normalise + applique l'offset
        length = max(1.0, math.sqrt(dx * dx + dy * dy))
        ux = dx / length
        uy = dy / length
        return (int(bx + ux * off * 1.4), int(by + uy * off * 1.4))


# ------------------------------------------------------------
# Écran principal du minijeu
# ------------------------------------------------------------

screen j901_signal_vivant_screen():

    modal True
    zorder 300

    timer J901_SV_TICK repeat True action Function(j901_sv_tick)

    key "K_ESCAPE" action NullAction()   # désactive échap pendant la partie

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

    # Fond global noir
    add Solid("#02040A")

    # Flash d'interférence
    if j901_sv_flash > 0.0:
        if j901_sv_inter_type == "ombre":
            add Solid("#33002288")
        elif j901_sv_inter_type == "polarite":
            add Solid("#3300FF55")
        else:
            add Solid("#FF334466")

    # ============================================
    # PANEAU GAUCHE (0..1152) — SALLE DU CONCLAVE
    # ============================================

    # Fond oscilloscope
    add "minijeu/signal_vivant_assets/bg_scope.png":
        xpos 0 ypos 110

    # Image de fond Conclave (cinématique de débat)
    if renpy.has_image("bg_conclave"):
        add "bg_conclave":
            xpos 0 ypos 110
            xsize 1152
            ysize 430
            alpha 0.35

    # Portrait du speaker actif (gauche en bas du pane conclave)
    fixed:
        xpos 0 ypos 110
        xsize 1152
        ysize 430

        # Voile sombre
        add Solid("#02040A66")

        # Cadre intérieur
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

        # Portrait du speaker à gauche
        $ _sv_speaker_image = j901_sv_current_speaker + " " + j901_sv_current_expr
        if renpy.has_image(_sv_speaker_image):
            add _sv_speaker_image at j901_sv_speaker_in:
                xpos 30 ypos 88
                zoom 0.55
        else:
            # Fallback : juste une grosse capsule colorée
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

        # Bulle de dialogue à droite du portrait
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
    # MONITEUR SIGNAL (centre — sous la cinématique)
    # ============================================

    fixed:
        xpos 0 ypos 540
        xsize 1152
        ysize 220

        add Solid("#03081599")

        # Titre
        text "FORME D'ONDE GLOBALE":
            xpos 24 ypos 12
            size 20
            color "#9FC7D8"
            bold True

        # Forme d'onde — 60 segments verticaux
        fixed:
            xpos 24 ypos 50
            xsize 720
            ysize 130

            # Cadre
            add Solid("#06101FCC")
            add Solid("#7DF9FF55", xysize=(720, 1)) ypos 65   # ligne centrale

            for i, v in enumerate(j901_sv_wave):
                $ _bx = i * 12
                $ _bh = max(2, int(abs(v) * 55))
                $ _by = 65 - _bh // 2 if v >= 0 else 65
                if j901_sv_all_green():
                    add Solid("#5DFF9A") xpos (_bx + 2) ypos _by xysize (8, _bh)
                else:
                    add Solid("#FF6B9A") xpos (_bx + 2) ypos _by xysize (8, _bh)

        # 3 jauges à droite de la forme d'onde
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

                        # Fond rail
                        add Solid("#0A1326") xysize (340, 18)

                        # Zone verte
                        $ _lo, _hi = J901_SV_GREEN_ZONES[gname]
                        $ _zx = int((_lo / 100.0) * 340)
                        $ _zw = int(((_hi - _lo) / 100.0) * 340)
                        add Solid("#26C96F33") xpos _zx ypos 0 xysize (_zw, 18)
                        add Solid("#26C96FAA") xpos _zx ypos 0 xysize (2, 18)
                        add Solid("#26C96FAA") xpos (_zx + _zw - 2) ypos 0 xysize (2, 18)

                        # Curseur
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

        # Section "SLOTS ACTIFS"
        text "SLOTS ACTIFS":
            xpos 24 ypos 12
            size 20
            color "#9FC7D8"
            bold True

        text "(Clic chip : placer/retirer · Clic slot : intensité · Clic-droit slot : vider)":
            xpos 180 ypos 16
            size 14
            color "#5F8090"

        # 4 slots
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

        # Section "PALETTE DE FRÉQUENCES"
        text "PALETTE DE FRÉQUENCES":
            xpos 24 ypos 250
            size 18
            color "#9FC7D8"
            bold True

        # 9 chips en bas (mini)
        for c_idx, c_key in enumerate(J901_SV_CHIP_ORDER):
            $ _cx_chip = 250 + c_idx * 90
            $ _data = J901_SV_CHIPS[c_key]
            $ _active = c_key in j901_sv_slots
            $ _locked = (c_key == j901_sv_locked_chip and j901_sv_inter_type == "brouillage")
            $ _chip_num = c_idx + 1
            fixed:
                xpos _cx_chip ypos 250
                xsize 80
                ysize 65

                if _locked:
                    button:
                        xpos 0 ypos 0
                        xsize 80
                        ysize 65
                        background Solid("#3A0612CC")
                        action NullAction()
                    add _data["asset"]:
                        xalign 0.5 yalign 0.5
                        zoom 0.32
                        alpha 0.30
                    text "✕":
                        xalign 0.5 yalign 0.5
                        size 38
                        color "#FF4D6D"
                        bold True
                else:
                    $ _chip_bg = Solid("#10384DEE") if _active else Solid("#0F1A2EDD")

                    button:
                        xpos 0
                        ypos 0
                        xsize 80
                        ysize 65
                        background _chip_bg
                        hover_background Solid("#1D2D52EE")
                        action Function(j901_sv_place_chip, c_key)

                        fixed:
                            xsize 80
                            ysize 65

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
    # PANEAU DROIT (1152..1920) — CAMPEMENTS
    # ============================================

    # Fond nébuleux
    add "minijeu/signal_vivant_assets/bg_campfield.png":
        xpos 1152 ypos 110

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
            text "TRANSMISSION → CAMPEMENTS FRONTALIERS":
                xalign 0.5
                size 20
                color "#DCF0FF"
                bold True
            text "12 groupes — entre 50 et 500 personnes":
                xalign 0.5
                size 14
                color "#7DF9FF"

    # Légende verticale gauche
    fixed:
        xpos 1162 ypos 180
        xsize 80
        ysize 60

        text "DISPERSÉS":
            xpos 0 ypos 4
            size 13
            color "#5DFF9A"
            bold True
        text "EN DANGER":
            xpos 0 ypos 22
            size 13
            color "#FFD166"
            bold True
        text "ÉTEINTS":
            xpos 0 ypos 40
            size 13
            color "#FF4D6D"
            bold True

    # Affichage des 12 campements (positions calculées dynamiquement)
    fixed:
        xpos 1152 ypos 170
        xsize 768
        ysize 800

        # Cercle ondulatoire au centre quand le signal est vivant
        if j901_sv_all_green():
            add Solid("#5DFF9A22") xpos 340 ypos 380 xysize (80, 80)
            add Solid("#5DFF9A55") xpos 360 ypos 400 xysize (40, 40)

        # Ombre Kami pendant l'interférence "ombre"
        if j901_sv_inter_type == "ombre":
            add "minijeu/signal_vivant_assets/kami_shadow.png":
                xalign 0.5 yalign 0.5
                zoom 0.85
                alpha 0.55
                at j901_sv_alert_pulse

        # Les 12 dots
        for cidx in range(12):
            $ _pos = j901_sv_camp_pos(cidx)
            $ _size = j901_sv_camp_size(cidx)
            $ _col = j901_sv_camp_color(cidx)
            $ _alive = j901_sv_camp_alive[cidx]
            $ _camp_num = cidx + 1
            add Solid(_col) xpos (_pos[0] - _size // 2) ypos (_pos[1] - _size // 2) xysize (_size, _size)
            if _alive:
                # Halo doux
                $ _halo_size = _size + 14
                add Solid(_col + "33") xpos (_pos[0] - _halo_size // 2) ypos (_pos[1] - _halo_size // 2) xysize (_halo_size, _halo_size)
                # Numéro
                text "[_camp_num]":
                    xpos (_pos[0] + _size // 2 + 4)
                    ypos (_pos[1] - 12)
                    size 13
                    color "#FFFFFF99"

    # Statistiques en bas du pane droit
    frame:
        xpos 1152 ypos 990
        xsize 768
        ysize 90
        background Solid("#070D1ADD")

        $ _disp = sum(1 for i, off in enumerate(j901_sv_camp_offsets) if j901_sv_camp_alive[i] and off >= 60.0)
        $ _dang = sum(1 for i, off in enumerate(j901_sv_camp_offsets) if j901_sv_camp_alive[i] and off < 60.0)
        $ _dead = sum(1 for a in j901_sv_camp_alive if not a)

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 36

            vbox:
                spacing 2
                text "DISPERSÉS":
                    size 14
                    color "#9FC7D8"
                text "[_disp]/12":
                    size 36
                    color "#5DFF9A"
                    bold True

            vbox:
                spacing 2
                text "EN DANGER":
                    size 14
                    color "#9FC7D8"
                text "[_dang]/12":
                    size 36
                    color "#FFD166"
                    bold True

            vbox:
                spacing 2
                text "ÉTEINTS":
                    size 14
                    color "#9FC7D8"
                text "[_dead]/12":
                    size 36
                    color "#FF4D6D"
                    bold True

    # ============================================
    # BANDEAU SUPÉRIEUR (titre + chrono + alerte)
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

    text "Maintenez les 3 jauges en zone verte. Combinez les fréquences. Survivez à Kami.":
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

    # Score live
    text "DISPERSION [j901_sv_dispersion_progress:.0f]%":
        xpos 1540 ypos 24
        size 22
        color "#DCF0FF"
        bold True

    # Compteurs de campements pendant la partie
    $ _live_disp = sum(1 for i, off in enumerate(j901_sv_camp_offsets) if j901_sv_camp_alive[i] and off >= 60.0)
    text "CAMPS SAUVÉS [_live_disp]/12":
        xpos 1540 ypos 58
        size 18
        color "#5DFF9A"
        bold True

    # ============================================
    # ALERTE KAMI (overlay si en cours)
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

    # Overlay glitch pendant les interférences fortes
    if j901_sv_inter_type == "parasites" or j901_sv_flash > 0.15:
        add "minijeu/signal_vivant_assets/overlay_glitch.png":
            alpha 0.35
            at j901_sv_shake_light

    # Fin de partie : déclenche Return
    if j901_sv_done:
        timer 0.4 action Return(j901_sv_result_tier)


# ------------------------------------------------------------
# Écran de bilan final
# ------------------------------------------------------------

screen j901_signal_vivant_bilan(tier):

    modal True
    zorder 320

    add Solid("#020408EE")

    $ _disp = store.j901_sv_disp_count
    $ _dang = store.j901_sv_danger_count
    $ _dead = store.j901_sv_dead_count

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
        "excellent": "Le signal a porté. La majorité des campements s'est dispersée à temps. Kami semble presque impressionnée.",
        "bon":       "Le message est passé. Plusieurs campements ont entendu et se sont écartés des frontières.",
        "moyen":     "Le signal a vacillé. Trop de campements sont restés groupés. Le Commandement a fait du dégât.",
        "echec":     "Le signal s'est éteint. Le Commandement IV s'est appliqué dans toute sa logique froide.",
    }.get(tier, "")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 620
        background Solid("#0A1326EE")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

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

            null height 10

            hbox:
                xalign 0.5
                spacing 60

                vbox:
                    spacing 4
                    text "DISPERSÉS":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_disp]/12":
                        xalign 0.5
                        size 64
                        color "#5DFF9A"
                        bold True

                vbox:
                    spacing 4
                    text "EN DANGER":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_dang]/12":
                        xalign 0.5
                        size 64
                        color "#FFD166"
                        bold True

                vbox:
                    spacing 4
                    text "ÉTEINTS":
                        xalign 0.5
                        size 18
                        color "#9FC7D8"
                    text "[_dead]/12":
                        xalign 0.5
                        size 64
                        color "#FF4D6D"
                        bold True

            null height 14

            text "[_tier_msg]":
                xalign 0.5
                size 24
                color "#FFFFFF"
                xmaximum 980
                text_align 0.5

            null height 14

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

label j901_play_signal_vivant:

    $ j901_sv_reset()
    $ _sv_tier = renpy.call_screen("j901_signal_vivant_screen")
    $ _sv_final_tier = renpy.call_screen("j901_signal_vivant_bilan", tier=_sv_tier)
    return _sv_final_tier
