# Fond opaque global : les déplacements, zooms et transitions ne doivent jamais
# révéler une surface transparente ou un ancien décor derrière la scène.
# config.underlay est dessiné sous le layer master et sous les autres couches ;
# ne remplace pas les Keymap/configurations déjà présents.
init -10 python:
    config.underlay.insert(0, Solid("#000000"))
