# Transition jour 30 de la route alternative, à développer.
# j29a_nyra_detained : True = Nyra placée sous surveillance ; False = libre.
label _30_0_1_1_0_1_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"
    scene black with dissolve
    if j29a_nyra_detained:
        centered "Jour 30 — Nyra sous surveillance. Suite en cours de développement."
    else:
        centered "Jour 30 — Nyra libre. Suite en cours de développement."
    return
