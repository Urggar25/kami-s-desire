# Gestion des droits aux extensions narratives.
# Les droits ne se déduisent PAS d'un booléen modifiable dans persistent.
# En développement la présence des labels du pack vaut installation ; en
# distribution commerciale le distributeur doit fournir les fichiers achetés.
init -40 python:
    KD_DLC_CATALOG = {
        "doppelganger_routes": {
            "title": "Les autres vies",
            "subtitle": "Route Doppelgänger — fins alternatives (J20–J30)",
            "description": "Après la première fin gratuite, découvrez les autres choix et leurs conséquences.",
            "entry_label": "kd_doppelganger_pack_ready",
        },
    }

    def kd_dlc_unlocked(pack_id):
        pack = KD_DLC_CATALOG.get(pack_id)
        return bool(pack and renpy.has_label(pack["entry_label"]))
