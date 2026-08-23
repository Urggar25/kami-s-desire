#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_trailer_sfx.py
=======================
Synthetise le kit de SFX cinema de la bande-annonce 2.1 et l'ecrit dans
``game/audio/trailer/`` (WAV 44100 Hz stereo 16 bits).

Le jeu embarque deja ``_sfx_bootstrap.rpy`` qui genere des bips utilitaires ;
ici on vise autre chose : des sons de bande-annonce (braams, risers, impacts
sub, glitchs, drones dissonants) qui portent la montee d'intensite.

Usage :
    python tools/generate_trailer_sfx.py

Le script est idempotent : relancer reecrit simplement les fichiers.
"""

import math
import os
import struct
import sys

import numpy as np

RATE = 44100
OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "game", "audio", "trailer"
)

RNG = np.random.default_rng(20260817)


# ---------------------------------------------------------------------------
# Briques de synthese
# ---------------------------------------------------------------------------
def t_axis(dur):
    return np.arange(int(RATE * dur)) / float(RATE)


def env_ad(t, attack, release, curve=2.0):
    """Enveloppe attaque/decroissance normalisee sur [0, 1]."""
    total = t[-1] if len(t) else 1.0
    a = np.clip(t / max(1e-6, attack), 0.0, 1.0)
    rel_start = max(1e-6, total - release)
    r = np.clip((total - t) / max(1e-6, total - rel_start), 0.0, 1.0)
    return (a ** 0.6) * (r ** curve)


def env_exp(t, tau):
    return np.exp(-t / max(1e-6, tau))


def sweep(t, f0, f1, curve=1.0, phase=0.0):
    """Sinus a frequence variable (integration de phase, pas d'artefact)."""
    x = (t / max(1e-9, t[-1])) ** curve if len(t) else t
    f = f0 + (f1 - f0) * x
    ph = 2.0 * np.pi * np.cumsum(f) / RATE + phase
    return np.sin(ph)


def noise(n, lowpass=None, highpass=None):
    x = RNG.normal(0.0, 1.0, n)
    if lowpass:
        x = one_pole_lp(x, lowpass)
    if highpass:
        x = x - one_pole_lp(x, highpass)
    return x


def one_pole_lp(x, cutoff):
    """Filtre passe-bas 1 pole, vectorise par recurrence lente mais suffisante."""
    a = math.exp(-2.0 * math.pi * cutoff / RATE)
    b = 1.0 - a
    # lfilter maison : boucle sur des blocs pour rester lisible et rapide.
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = b * x[i] + a * acc
        y[i] = acc
    return y


def saturate(x, drive=2.0):
    return np.tanh(x * drive) / math.tanh(drive)


def reverb_tail(x, decay=1.6, taps=14, spread=0.055):
    """Reverb par peignes decales : suffit largement pour du SFX."""
    out = x.copy()
    for i in range(1, taps + 1):
        d = int(RATE * spread * i * (0.85 + 0.3 * ((i * 7) % 5) / 5.0))
        if d >= len(x):
            break
        g = decay ** i * 0.5
        out[d:] += x[: len(x) - d] * g
    return out


def fade_edges(x, fin=0.006, fout=0.05):
    n = len(x)
    ni = min(n // 2, int(RATE * fin))
    no = min(n // 2, int(RATE * fout))
    if ni:
        x[:ni] *= np.linspace(0.0, 1.0, ni)
    if no:
        x[-no:] *= np.linspace(1.0, 0.0, no)
    return x


def normalize(x, peak=0.92):
    m = np.max(np.abs(x)) if len(x) else 0.0
    if m < 1e-9:
        return x
    return x * (peak / m)


def widen(mono, amount=0.006):
    """Pseudo-stereo : micro-retard sur le canal droit."""
    d = int(RATE * amount)
    left = mono
    right = np.concatenate([np.zeros(d), mono[: len(mono) - d]]) if d else mono
    return left, right


def write_wav(name, mono, stereo_amount=0.006, peak=0.92):
    mono = normalize(np.asarray(mono, dtype=np.float64), peak)
    left, right = widen(mono, stereo_amount)
    inter = np.empty(len(left) * 2, dtype=np.float64)
    inter[0::2] = left
    inter[1::2] = right
    pcm = np.clip(inter, -1.0, 1.0)
    frames = (pcm * 32000.0).astype("<i2").tobytes()

    header = (
        b"RIFF"
        + struct.pack("<I", 36 + len(frames))
        + b"WAVEfmt "
        + struct.pack("<IHHIIHH", 16, 1, 2, RATE, RATE * 4, 4, 16)
        + b"data"
        + struct.pack("<I", len(frames))
    )
    path = os.path.join(OUT_DIR, name)
    with open(path, "wb") as f:
        f.write(header)
        f.write(frames)
    print("  %-30s %5.2f s" % (name, len(mono) / float(RATE)))


# ---------------------------------------------------------------------------
# Les sons
# ---------------------------------------------------------------------------
def sfx_impact_deep():
    """Impact de carton-titre : sub qui claque + queue metallique."""
    t = t_axis(2.6)
    sub = sweep(t, 130.0, 32.0, curve=0.35) * env_exp(t, 0.42)
    sub += sweep(t, 65.0, 24.0, curve=0.30) * env_exp(t, 0.85) * 0.8
    click = noise(len(t), lowpass=5200.0) * env_exp(t, 0.035) * 0.55
    metal = np.zeros(len(t))
    for f, g in ((214.0, 0.30), (367.0, 0.22), (611.0, 0.15), (1043.0, 0.09)):
        metal += np.sin(2 * np.pi * f * t) * env_exp(t, 0.30 + 900.0 / f * 0.004) * g
    body = saturate(sub * 1.15, 1.8) + click + metal * 0.6
    return fade_edges(reverb_tail(body, decay=0.52, taps=9, spread=0.048))


def sfx_braam():
    """Nappe de cuivres graves qui enfle : la signature du trailer."""
    t = t_axis(3.4)
    e = env_ad(t, 0.55, 1.5, curve=1.5)
    out = np.zeros(len(t))
    # Empilement de partiels legerement desaccordes = cuivre epais.
    for mult, gain in ((1.0, 1.0), (1.5, 0.42), (2.0, 0.34), (3.0, 0.16), (4.0, 0.08)):
        for det in (-0.4, 0.0, 0.5):
            f = 48.0 * mult + det
            drift = 1.0 + 0.012 * np.sin(2 * np.pi * 0.7 * t + mult)
            out += np.sin(2 * np.pi * f * drift * t) * gain
    out *= e / 4.0
    out = saturate(out * 1.6, 2.4)
    growl = noise(len(t), lowpass=180.0) * e * 0.30
    return fade_edges(reverb_tail(out + growl, decay=0.55, taps=12, spread=0.06))


def sfx_riser(dur=3.0, name_hint="short"):
    """Riser : bruit filtre montant + pitch qui grimpe + battements."""
    t = t_axis(dur)
    x = t / dur
    e = x ** 1.7

    nz = noise(len(t))
    # Balayage du passe-bas de 300 Hz a 9 kHz : on le simule par melange
    # de deux versions filtrees, moins couteux qu'un filtre variable.
    lo = one_pole_lp(nz, 420.0)
    hi = one_pole_lp(nz, 9000.0)
    band = lo * (1.0 - e) + hi * e
    band *= e * 0.9

    tone = sweep(t, 110.0, 1750.0, curve=2.2) * e * 0.35
    tone += sweep(t, 165.0, 2620.0, curve=2.4) * e * 0.18

    # Trilles de plus en plus serres : effet d'acceleration.
    trill = np.sin(2 * np.pi * (4.0 + 26.0 * e) * t) * 0.5 + 0.5
    body = (band + tone) * (0.65 + 0.35 * trill)

    # Coupe net a la fin : le silence juste avant l'impact.
    body[-int(RATE * 0.012):] *= np.linspace(1.0, 0.0, int(RATE * 0.012))
    return fade_edges(body, fin=0.02, fout=0.012)


def sfx_reverse_swell():
    """Nappe inversee : aspiration avant un carton."""
    t = t_axis(2.2)
    nz = noise(len(t), lowpass=6500.0)
    tone = sweep(t, 320.0, 90.0, curve=0.7)
    body = nz * 0.6 + tone * 0.4
    body *= (t / t[-1]) ** 2.6
    body = reverb_tail(body, decay=0.4, taps=7, spread=0.05)
    body[-int(RATE * 0.02):] *= np.linspace(1.0, 0.0, int(RATE * 0.02))
    return fade_edges(body, fin=0.05, fout=0.02)


def sfx_sub_drop():
    """Chute de sub pure : ponctuation de coupe."""
    t = t_axis(1.9)
    sub = sweep(t, 92.0, 19.0, curve=0.28) * env_exp(t, 0.55)
    sub += np.sin(2 * np.pi * 41.0 * t) * env_exp(t, 0.30) * 0.4
    return fade_edges(saturate(sub * 1.3, 1.5))


def sfx_glitch_stutter():
    """Hachage numerique : la machine deraille."""
    dur = 1.15
    t = t_axis(dur)
    out = np.zeros(len(t))
    pos = 0
    seg_id = 0
    while pos < len(t):
        seg = int(RATE * RNG.uniform(0.012, 0.055))
        seg = min(seg, len(t) - pos)
        if seg <= 1:
            break
        st = np.arange(seg) / float(RATE)
        kind = seg_id % 4
        if kind == 0:
            f = RNG.uniform(700.0, 3400.0)
            chunk = np.sign(np.sin(2 * np.pi * f * st))
        elif kind == 1:
            chunk = RNG.normal(0.0, 1.0, seg)
        elif kind == 2:
            chunk = np.zeros(seg)
        else:
            f = RNG.uniform(90.0, 260.0)
            chunk = np.sin(2 * np.pi * f * st) * 1.2
        chunk *= RNG.uniform(0.25, 1.0)
        out[pos:pos + seg] = chunk
        pos += seg
        seg_id += 1
    out = one_pole_lp(out, 7200.0)
    out *= env_ad(t, 0.004, 0.25, curve=1.2)
    return fade_edges(saturate(out, 1.6))


def sfx_data_burst():
    """Rafale de telemetrie : sert de respiration entre deux plans HUD."""
    t = t_axis(0.85)
    out = np.zeros(len(t))
    for i in range(26):
        start = int(RATE * RNG.uniform(0.0, 0.72))
        seg = int(RATE * RNG.uniform(0.006, 0.026))
        seg = min(seg, len(t) - start)
        if seg <= 1:
            continue
        st = np.arange(seg) / float(RATE)
        f = RNG.uniform(1400.0, 5200.0)
        out[start:start + seg] += np.sin(2 * np.pi * f * st) * np.exp(-st / 0.008) * 0.5
    out *= env_ad(t, 0.005, 0.28)
    return fade_edges(reverb_tail(out, decay=0.3, taps=5, spread=0.03))


def sfx_heartbeat():
    """Deux coups sourds : le cold open et l'epilogue."""
    t = t_axis(1.75)
    out = np.zeros(len(t))
    for offset, gain in ((0.00, 1.0), (0.34, 0.72)):
        i0 = int(RATE * offset)
        st = t[: len(t) - i0]
        thump = sweep(st, 78.0, 30.0, curve=0.35) * env_exp(st, 0.115) * gain
        thump += noise(len(st), lowpass=300.0) * env_exp(st, 0.05) * 0.22 * gain
        out[i0:] += thump
    return fade_edges(saturate(out * 1.2, 1.4))


def sfx_tick():
    """Tic sec : marque le tempo des rafales de montage."""
    t = t_axis(0.24)
    click = noise(len(t), lowpass=8000.0, highpass=900.0) * env_exp(t, 0.006)
    tone = np.sin(2 * np.pi * 2100.0 * t) * env_exp(t, 0.012) * 0.5
    tone += np.sin(2 * np.pi * 128.0 * t) * env_exp(t, 0.07) * 0.35
    return fade_edges(click + tone, fout=0.02)


def sfx_swoosh():
    """Whoosh court : transitions rapides."""
    t = t_axis(0.62)
    nz = noise(len(t))
    lo = one_pole_lp(nz, 500.0)
    hi = one_pole_lp(nz, 6800.0)
    x = t / t[-1]
    shape = np.sin(np.pi * x) ** 1.6
    body = (lo * (1.0 - x) + hi * x) * shape
    body += sweep(t, 240.0, 1400.0, curve=1.6) * shape * 0.22
    return fade_edges(body, fin=0.01, fout=0.06)


def sfx_alarm_low():
    """Alarme grave a deux tons : acte 4."""
    t = t_axis(2.9)
    gate = (np.sin(2 * np.pi * 1.35 * t) > 0).astype(np.float64)
    gate = one_pole_lp(gate, 26.0)
    a = np.sin(2 * np.pi * 138.0 * t)
    b = np.sin(2 * np.pi * 104.0 * t)
    sel = (np.sin(2 * np.pi * 0.675 * t) > 0).astype(np.float64)
    tone = a * sel + b * (1.0 - sel)
    tone += np.sin(2 * np.pi * 69.0 * t) * 0.45
    body = tone * gate * env_ad(t, 0.12, 0.7)
    return fade_edges(saturate(body, 1.7))


def sfx_string_tension():
    """Drone dissonant tenu : la peur qui s'installe."""
    t = t_axis(6.0)
    e = env_ad(t, 1.6, 2.0, curve=1.2)
    out = np.zeros(len(t))
    # Seconde mineure + triton : dissonance immediate.
    for f, g in ((146.8, 1.0), (155.6, 0.85), (207.7, 0.55), (293.7, 0.35), (311.1, 0.30)):
        for det in (-0.7, 0.0, 0.8):
            vib = 1.0 + 0.004 * np.sin(2 * np.pi * RNG.uniform(3.5, 5.5) * t)
            out += np.sin(2 * np.pi * (f + det) * vib * t) * g
    out *= e / 6.0
    bow = noise(len(t), lowpass=2600.0, highpass=140.0) * e * 0.16
    return fade_edges(reverb_tail(out + bow, decay=0.5, taps=10, spread=0.07), fout=0.9)


def sfx_final_hit():
    """L'impact du logo : le plus gros son du trailer."""
    t = t_axis(4.2)
    sub = sweep(t, 150.0, 26.0, curve=0.30) * env_exp(t, 0.75)
    sub += np.sin(2 * np.pi * 36.0 * t) * env_exp(t, 1.5) * 0.7
    crack = noise(len(t), lowpass=9000.0) * env_exp(t, 0.06) * 0.55
    brass = np.zeros(len(t))
    for mult, gain in ((1.0, 1.0), (1.5, 0.4), (2.0, 0.3), (3.0, 0.14)):
        brass += np.sin(2 * np.pi * 52.0 * mult * t) * gain
    brass *= env_ad(t, 0.02, 3.0, curve=1.4) / 2.0
    body = saturate(sub * 1.25, 1.9) + crack + brass * 0.75
    return fade_edges(reverb_tail(body, decay=0.6, taps=14, spread=0.07), fout=0.8)


def sfx_whisper_drone():
    """Souffle metallique tres bas : lit sonore continu des actes sombres."""
    t = t_axis(8.0)
    nz = noise(len(t), lowpass=900.0, highpass=60.0)
    hum = np.sin(2 * np.pi * 49.0 * t) * 0.35
    hum += np.sin(2 * np.pi * 98.5 * t) * 0.12
    mod = 0.6 + 0.4 * np.sin(2 * np.pi * 0.11 * t)
    body = (nz * 0.5 + hum) * mod
    return fade_edges(body, fin=1.2, fout=1.4)


SOUNDS = [
    ("trl_impact_deep.wav", sfx_impact_deep, 0.008, 0.95),
    ("trl_braam.wav", sfx_braam, 0.010, 0.90),
    ("trl_riser_short.wav", lambda: sfx_riser(2.0), 0.007, 0.80),
    ("trl_riser.wav", lambda: sfx_riser(3.0), 0.007, 0.82),
    ("trl_riser_long.wav", lambda: sfx_riser(5.0), 0.007, 0.84),
    ("trl_reverse_swell.wav", sfx_reverse_swell, 0.009, 0.80),
    ("trl_sub_drop.wav", sfx_sub_drop, 0.004, 0.95),
    ("trl_glitch_stutter.wav", sfx_glitch_stutter, 0.003, 0.85),
    ("trl_data_burst.wav", sfx_data_burst, 0.006, 0.70),
    ("trl_heartbeat.wav", sfx_heartbeat, 0.004, 0.90),
    ("trl_tick.wav", sfx_tick, 0.003, 0.72),
    ("trl_swoosh.wav", sfx_swoosh, 0.008, 0.78),
    ("trl_alarm_low.wav", sfx_alarm_low, 0.006, 0.80),
    ("trl_string_tension.wav", sfx_string_tension, 0.012, 0.72),
    ("trl_final_hit.wav", sfx_final_hit, 0.010, 0.98),
    ("trl_whisper_drone.wav", sfx_whisper_drone, 0.014, 0.55),
]


def main():
    out = os.path.normpath(OUT_DIR)
    if not os.path.isdir(out):
        os.makedirs(out)
    print("Generation du kit SFX bande-annonce 2.1 ->", out)
    for name, fn, width, peak in SOUNDS:
        write_wav(name, fn(), stereo_amount=width, peak=peak)
    print("Termine : %d fichiers." % len(SOUNDS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
