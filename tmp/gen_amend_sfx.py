#!/usr/bin/env python3
# SFX + ambiance du minijeu amendement_brouillon. numpy -> wav -> ogg (ffmpeg).
import os, subprocess, numpy as np

SR = 44100
OUT = "/sessions/modest-charming-mayer/mnt/kami-s-desire/game/minijeu/amend_assets"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(1848)

def onepole_lp(x, cutoff):
    a = np.exp(-2*np.pi*cutoff/SR)
    y = np.zeros_like(x); acc = 0.0
    for i in range(len(x)):
        acc = a*acc + (1-a)*x[i]; y[i] = acc
    return y

def onepole_hp(x, cutoff):
    return x - onepole_lp(x, cutoff)

def bp(x, lo, hi):
    return onepole_hp(onepole_lp(x, hi), lo)

def env(n, a, d, s_lvl=0.0, r=None):
    r = r if r is not None else n - a - d
    r = max(1, r)
    e = np.concatenate([
        np.linspace(0, 1, max(1, a)),
        np.linspace(1, s_lvl, max(1, d)),
        np.full(max(0, n - a - d - r), s_lvl),
        np.linspace(s_lvl, 0, r),
    ])
    return e[:n] if len(e) >= n else np.pad(e, (0, n-len(e)))

def norm(x, peak=0.9):
    m = np.max(np.abs(x)) or 1.0
    return x/m*peak

def write(name, x, peak=0.9):
    x = norm(np.asarray(x, dtype=np.float64), peak)
    pcm = (x*32767).astype(np.int16)
    wav = os.path.join("/tmp", name+".wav")
    ogg = os.path.join(OUT, name+".ogg")
    import wave
    with wave.open(wav, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "libvorbis", "-qscale:a", "4", ogg], check=True)
    os.remove(wav)
    print("ok", name+".ogg")

# --- gomme frottée : friction band-pass, deux allers-retours ---
def eraser_rub():
    dur = int(0.42*SR)
    n = rng.standard_normal(dur)
    n = bp(n, 700, 3200)
    # modulation d'amplitude = mouvement de va-et-vient
    t = np.linspace(0, 1, dur)
    lfo = 0.55 + 0.45*np.abs(np.sin(2*np.pi*4.5*t))
    e = env(dur, int(0.02*SR), int(0.05*SR), 0.8, int(0.12*SR))
    return n*lfo*e*0.8

# --- froissement papier : impulsions crépitantes ---
def paper_crumple():
    dur = int(0.55*SR)
    y = np.zeros(dur)
    for _ in range(220):
        p = rng.integers(0, dur-400)
        amp = rng.random()**2
        L = rng.integers(40, 260)
        seg = rng.standard_normal(L)*np.hanning(L)*amp
        y[p:p+L] += seg
    y = bp(y, 1500, 8000)
    y *= env(dur, int(0.01*SR), int(0.2*SR), 0.3, int(0.25*SR))
    return y

# --- plume / stylo : grattement bref ---
def pen():
    dur = int(0.28*SR)
    n = bp(rng.standard_normal(dur), 2000, 7000)
    t = np.linspace(0, 1, dur)
    lfo = 0.5+0.5*np.abs(np.sin(2*np.pi*11*t))
    return n*lfo*env(dur, int(0.005*SR), int(0.03*SR), 0.6, int(0.1*SR))

# --- chaise raclée ---
def chair():
    dur = int(0.7*SR)
    n = bp(rng.standard_normal(dur), 120, 900)
    t = np.linspace(0, 1, dur)
    grind = 0.6+0.4*np.abs(np.sin(2*np.pi*22*t))
    body = 0.3*np.sin(2*np.pi*np.linspace(90, 140, dur)*t)
    return (n*grind + body)*env(dur, int(0.03*SR), int(0.1*SR), 0.7, int(0.3*SR))

# --- pas (deux) ---
def footsteps():
    dur = int(1.0*SR)
    y = np.zeros(dur)
    for p in (0.05, 0.42):
        i = int(p*SR)
        L = int(0.14*SR)
        thump = np.sin(2*np.pi*np.linspace(90, 55, L)*np.linspace(0,1,L))*np.exp(-np.linspace(0,6,L))
        click = bp(rng.standard_normal(L), 1500, 5000)*np.exp(-np.linspace(0,12,L))*0.3
        y[i:i+L] += thump + click
    return y

# --- pliage feuille ---
def fold():
    dur = int(0.5*SR)
    y = np.zeros(dur)
    for _ in range(90):
        p = rng.integers(0, dur-300); L = rng.integers(60, 300)
        y[p:p+L] += rng.standard_normal(L)*np.hanning(L)*(rng.random()**1.5)
    y = bp(y, 900, 5000)
    # crin final net
    L = int(0.08*SR)
    y[int(0.35*SR):int(0.35*SR)+L] += bp(rng.standard_normal(L), 2000, 6000)*np.hanning(L)*1.4
    return y*env(dur, int(0.01*SR), int(0.15*SR), 0.4, int(0.2*SR))

# --- dépose fragment (tap papier doux) ---
def place():
    dur = int(0.18*SR)
    tap = np.sin(2*np.pi*np.linspace(160, 80, dur)*np.linspace(0,1,dur))*np.exp(-np.linspace(0,9,dur))
    crin = bp(rng.standard_normal(dur), 1200, 5000)*np.exp(-np.linspace(0,14,dur))*0.4
    return tap+crin

# --- ambiance Conclave (loop ~12s) : room tone + murmures + événements épars ---
def ambience():
    dur = int(12.0*SR)
    # room tone : basse fréquence filtrée
    tone = onepole_lp(rng.standard_normal(dur), 120)*0.5
    tone += 0.15*np.sin(2*np.pi*52*np.linspace(0, dur/SR, dur))
    # nappe de murmure = bruit band-pass lentement modulé
    mur = bp(rng.standard_normal(dur), 250, 1400)
    tmod = np.linspace(0, dur/SR, dur)
    murmur_lfo = 0.3+0.25*np.sin(2*np.pi*0.15*tmod)+0.15*np.sin(2*np.pi*0.37*tmod)
    mur *= murmur_lfo*0.35
    y = tone + mur
    # événements : stylos, papiers, chaises dispersés
    def stamp(sig, at):
        i = int(at*SR)
        L = len(sig)
        if i+L < dur:
            y[i:i+L] += sig*0.5
    for at in [0.8, 2.3, 3.1, 4.7, 6.0, 7.4, 8.9, 10.2, 11.1]:
        r = rng.random()
        if r < 0.4: stamp(pen(), at)
        elif r < 0.7: stamp(place(), at)
        else: stamp(chair()*0.4, at)
    # fondu boucle (cross-fade bords)
    xf = int(0.4*SR)
    y[:xf] *= np.linspace(0, 1, xf)
    y[-xf:] *= np.linspace(1, 0, xf)
    return y*0.7

write("amend_eraser_rub", eraser_rub())
write("amend_paper_crumple", paper_crumple())
write("amend_pen", pen())
write("amend_chair", chair())
write("amend_footsteps", footsteps())
write("amend_fold", fold())
write("amend_place", place())
write("amend_ambience", ambience(), peak=0.8)
print("DONE sfx")
