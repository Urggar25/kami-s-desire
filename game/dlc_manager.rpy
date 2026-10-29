# Gestion des droits aux extensions narratives.
# Les droits ne se déduisent PAS d'un booléen modifiable dans persistent.
# En développement la présence des labels du pack vaut installation ; en
# distribution commerciale le distributeur doit fournir les fichiers achetés.
init -40 python:
    # Lien de recherche Steam provisoire : aucune page produit DLC vérifiée.
    KD_DLC_STEAM_URL = "https://store.steampowered.com/search/?term=Kami%27s%20Desires"
    KD_DLC_CATALOG = {
        "doppelganger_routes": {
            "title": "L’Origine",
            "subtitle": "Un autre regard sur les derniers jours du Conclave",
            "description": "Après la première fin gratuite, découvrez les autres choix et leurs conséquences.",
            "entry_label": "kd_doppelganger_pack_ready",
        },
    }

    def kd_dlc_unlocked(pack_id):
        pack = KD_DLC_CATALOG.get(pack_id)
        return bool(pack and renpy.has_label(pack["entry_label"]))
