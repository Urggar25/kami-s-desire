# ============================================================
# _sfx_bootstrap.rpy — Générateur de SFX manquants
# Synthétise au premier lancement les sons référencés mais absents
# (WAV 22050 Hz mono 16 bits, écrits dans game/audio/).
# Une fois les fichiers créés, ce script ne fait plus rien.
# Tu peux remplacer ces sons par de vrais assets plus tard :
# il suffit d'écraser les .wav dans game/audio/.
# ============================================================

init -10 python:
    import os
    import math
    import struct
    import random as _sfxrand

    _SFX_RATE = 22050

    def _sfx_write(path, samples):
        # samples : liste de floats -1..1
        try:
            frames = bytearray()
            for s in samples:
                s = max(-1.0, min(1.0, s))
                frames += struct.pack("<h", int(s * 32000))

            # Ecriture WAV PCM minimale pour eviter le module wave/audioop,
            # absent de certains runtimes Ren'Py.
            data_size = len(frames)
            header = (
                b"RIFF"
                + struct.pack("<I", 36 + data_size)
                + b"WAVEfmt "
                + struct.pack("<IHHIIHH", 16, 1, 1, _SFX_RATE, _SFX_RATE * 2, 2, 16)
                + b"data"
                + struct.pack("<I", data_size)
            )

            with open(path, "wb") as f:
                f.write(header)
                f.write(bytes(frames))
            return True
        except Exception:
            return False

    def _sfx_env(i, n, attack=0.01, release=0.3):
        # Enveloppe attaque/relâchement simple
        t = i / float(n)
        a = min(1.0, t / max(1e-6, attack))
        r = min(1.0, (1.0 - t) / max(1e-6, release))
        return min(a, r)

    def _sfx_day_transition():
        # Boom grave + shimmer ascendant (~2.4 s)
        n = int(_SFX_RATE * 2.4)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            # Boom : sinus grave avec pitch qui descend
            f_boom = 110.0 * math.exp(-t * 1.4) + 38.0
            boom = math.sin(2 * math.pi * f_boom * t) * math.exp(-t * 2.2) * 0.85
            # Shimmer : deux sinus qui montent doucement
            f1 = 520.0 + t * 240.0
            f2 = 660.0 + t * 300.0
            sh = (math.sin(2 * math.pi * f1 * t) + math.sin(2 * math.pi * f2 * t)) * 0.10
            sh *= max(0.0, min(1.0, (t - 0.25) * 2.0)) * math.exp(-(t - 0.25) * 1.2 if t > 0.25 else 0.0)
            out.append((boom + sh) * _sfx_env(i, n, 0.005, 0.25))
        return out

    def _sfx_vote_pour():
        # Carillon ascendant deux notes (positif)
        n = int(_SFX_RATE * 0.7)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            f = 660.0 if t < 0.22 else 880.0
            v = math.sin(2 * math.pi * f * t) * 0.6
            v += math.sin(2 * math.pi * f * 2 * t) * 0.15
            out.append(v * math.exp(-t * 4.5))
        return out

    def _sfx_vote_contre():
        # Buzz grave descendant (négatif)
        n = int(_SFX_RATE * 0.8)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            f = 220.0 - t * 90.0
            v = math.sin(2 * math.pi * f * t)
            v += 0.4 * math.sin(2 * math.pi * f * 0.5 * t)
            # Légère saturation
            v = max(-0.8, min(0.8, v * 1.6))
            out.append(v * 0.6 * math.exp(-t * 3.0))
        return out

    def _sfx_vote_abstention():
        # Tick neutre étouffé
        n = int(_SFX_RATE * 0.25)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            v = math.sin(2 * math.pi * 440.0 * t) * 0.4
            v += (_sfxrand.random() * 2 - 1) * 0.08
            out.append(v * math.exp(-t * 22.0))
        return out

    def _sfx_qte_hit():
        # Blip court satisfaisant
        n = int(_SFX_RATE * 0.18)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            f = 880.0 + t * 600.0
            out.append(math.sin(2 * math.pi * f * t) * 0.55 * math.exp(-t * 18.0))
        return out

    def _sfx_qte_miss():
        # Burst de bruit avec chute de pitch
        n = int(_SFX_RATE * 0.35)
        out = []
        phase = 0.0
        for i in range(n):
            t = i / float(_SFX_RATE)
            f = 300.0 * math.exp(-t * 6.0) + 60.0
            phase += 2 * math.pi * f / _SFX_RATE
            v = math.sin(phase) * 0.5 + (_sfxrand.random() * 2 - 1) * 0.30
            out.append(v * math.exp(-t * 7.0))
        return out

    def _sfx_kami_alert():
        # Alerte type annonce Kami : trois pulses métalliques
        n = int(_SFX_RATE * 1.1)
        out = []
        for i in range(n):
            t = i / float(_SFX_RATE)
            seg = int(t / 0.35)
            lt = t - seg * 0.35
            f = 740.0 if seg % 2 == 0 else 590.0
            v = math.sin(2 * math.pi * f * lt) * 0.5
            v += math.sin(2 * math.pi * f * 1.5 * lt) * 0.2
            out.append(v * math.exp(-lt * 9.0))
        return out

    def _sfx_bootstrap():
        base = os.path.join(config.gamedir, "audio")
        try:
            if not os.path.isdir(base):
                os.makedirs(base)
        except Exception:
            return

        wanted = {
            "sfx_day_transition.wav": _sfx_day_transition,
            "sfx_vote_pour.wav": _sfx_vote_pour,
            "sfx_vote_contre.wav": _sfx_vote_contre,
            "sfx_vote_abstention.wav": _sfx_vote_abstention,
            "sfx_qte_hit.wav": _sfx_qte_hit,
            "sfx_qte_miss.wav": _sfx_qte_miss,
            "sfx_kami_alert.wav": _sfx_kami_alert,
        }

        for name, gen in wanted.items():
            path = os.path.join(base, name)
            if not os.path.exists(path):
                _sfx_write(path, gen())

    _sfx_bootstrap()
