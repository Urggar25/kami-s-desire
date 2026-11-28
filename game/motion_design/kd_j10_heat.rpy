# Mirage thermique GPU, Ren'Py 8.3 (GLSL ES 1.00).
# Les UV sont déplacées, et non les objets/masques de clic.
# Les sinusoïdes déphasées remontent le cadre en continu ; l'amplitude
# est plus élevée vers le bas, comme les remontées d'air chaud.

init -2 python:
    renpy.register_shader("kd.j10_heat", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform float u_kd_heat_strength;
        varying vec2 v_tex_coord;
    """, fragment_300="""
        vec2 kd_uv = v_tex_coord;
        float kd_t = u_time;
        float kd_low = 0.40 + 0.60 * smoothstep(0.10, 0.98, kd_uv.y);
        float kd_edge = smoothstep(0.0, 0.025, kd_uv.x)
            * smoothstep(0.0, 0.025, 1.0 - kd_uv.x)
            * smoothstep(0.0, 0.025, kd_uv.y)
            * smoothstep(0.0, 0.025, 1.0 - kd_uv.y);
        float kd_wave = sin(kd_uv.y * 45.0 + kd_t * 4.0
            + 1.4 * sin(kd_uv.x * 11.0 + kd_t * 0.65));
        float kd_ripple = sin(kd_uv.y * 91.0 + kd_uv.x * 16.0 + kd_t * 6.1);
        float kd_vertical = sin(kd_uv.x * 29.0 + kd_uv.y * 19.0 + kd_t * 3.1);
        vec2 kd_shift = vec2(
            kd_wave * 0.68 + kd_ripple * 0.32,
            kd_vertical * 0.22
        ) * u_kd_heat_strength * kd_low * kd_edge;
        vec2 kd_sample = clamp(kd_uv + kd_shift, vec2(0.0), vec2(1.0));
        vec2 kd_soft = vec2(u_kd_heat_strength * 0.12, 0.0) * kd_edge;
        gl_FragColor = texture2D(tex0, kd_sample) * 0.76
            + texture2D(tex0, clamp(kd_sample + kd_soft, vec2(0.0), vec2(1.0))) * 0.12
            + texture2D(tex0, clamp(kd_sample - kd_soft, vec2(0.0), vec2(1.0))) * 0.12;
    """)

# Une pause ATL répétée maintient une cadence d'au moins 30 images/s
# même quand le joueur ne bouge pas et qu'aucune réplique ne s'affiche.
transform j10_heat:
    mesh True
    shader "kd.j10_heat"
    u_kd_heat_strength 0.0045
    block:
        pause (1.0 / 30.0)
        repeat

# Accentuation subjective, sans baisse artificielle de luminosité.
transform j10_heat_horror:
    mesh True
    shader "kd.j10_heat"
    u_kd_heat_strength 0.0070
    block:
        pause (1.0 / 30.0)
        repeat

# Approche imperceptible du croisement ; pas de secousse ni de flash.
transform j10_corridor_watch:
    subpixel True
    xalign 0.5
    yalign 0.5
    zoom 1.0
    ease 5.0 zoom 1.035

# Laisser au joueur le temps d'examiner la CG avant le changement.
transform j10_silhouette_zoom:
    subpixel True
    xalign 0.5
    yalign 0.5
    zoom 1.0
    ease 5.0 zoom 1.10

# Réaction au claquement : petit recadrage plutôt qu'un hpunch.
transform j10_corridor_turn:
    subpixel True
    xalign 0.5
    yalign 0.5
    zoom 1.045
    xoffset 14
    easeout 0.45 xoffset 0 zoom 1.0
