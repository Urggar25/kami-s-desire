# -----------------------------------------------------------------------
# PROFILS + CODEX — Systèmes de méta-progression narratifs
# -----------------------------------------------------------------------

default profile_affinity = {
    "noam": 0, "lysa": 0, "elen": 0, "elias": 0, "mara": 0, "julian": 0,
    "iris": 0, "tomas": 0, "kael": 0, "nyra": 0, "ryn": 0, "sael": 0,
}
default profile_story_unlocked = {
    "noam": False, "lysa": False, "elen": False, "elias": False, "mara": False, "julian": False,
    "iris": False, "tomas": False, "kael": False, "nyra": False, "ryn": False, "sael": False,
}
default profile_relations_unlocked = {
    "noam": False, "lysa": False, "elen": False, "elias": False, "mara": False, "julian": False,
    "iris": False, "tomas": False, "kael": False, "nyra": False, "ryn": False, "sael": False,
}
default codex_unlocked_entries = [
    "districts_conclave",
    "systeme_votes",
    "personnage_noam",
]

default profile_global_points = 0
default persistent.profile_wardrobe_unlocked = {}
default persistent.profile_skin_equipped = {}

init python:
    PROFILE_ORDER = ["noam", "lysa", "elen", "elias", "mara", "julian", "iris", "tomas", "kael", "nyra", "ryn", "sael"]

    PROFILE_DATA = {
        "noam": {
            "name": "Noam", "role": "Médiateur (narrateur)", "district": "Conclave", "age": "20",
            "quote": "Comprendre avant de trancher.",
            "sprite": "images/character/noam/portrait.png",
            "expressions": ["neutre", "inquiet", "determine"],
            "backstory": "Noam est réveillé dans le Conclave sans souvenirs complets des semaines précédentes. Il compense par une écoute active et une capacité inhabituelle à reformuler les conflits.",
            "relations": "Pivot entre les représentants: confiance fragile de Lysa, friction idéologique avec Kael, empathie instinctive avec Iris.",
        },
        "lysa": {"name": "Lysa", "role": "Coordination logistique", "district": "Réseau Central", "age": "22", "quote": "Une promesse sans procédure n'est qu'un bruit.", "sprite": "images/character/lysa/portrait.png", "expressions": ["neutre", "inquiet", "sourire"], "backstory": "Spécialiste des flux et des quotas.", "relations": "S'aligne souvent avec Tomas sur les contraintes matérielles."},
        "elen": {"name": "Elen", "role": "Santé & triage", "district": "Infirmerie", "age": "23", "quote": "On compte les vivants, pas les slogans.", "sprite": "images/character/elen/portrait.png", "expressions": ["neutre", "colere", "triste"], "backstory": "A connu trois vagues de pénurie de médicaments.", "relations": "Respect mutuel avec Sael, tensions avec les discours propagandistes."},
        "elias": {"name": "Elias", "role": "Sport & discipline", "district": "Gymnase", "age": "21", "quote": "Tenir, c'est déjà gagner du temps.", "sprite": "images/character/elias/portrait.png", "expressions": ["neutre", "determine", "surpris"] , "backstory": "Ancien instructeur de terrain.", "relations": "Complicité compétitive avec Ryn."},
        "mara": {"name": "Mara", "role": "Ravitaillement", "district": "Cafétéria", "age": "24", "quote": "Un repas stable vaut mieux qu'un grand discours.", "sprite": "images/character/mara/portrait.png", "expressions": ["neutre", "rire", "inquiet"], "backstory": "Gestionnaire des stocks alimentaires.", "relations": "Confiance pragmatique avec Lysa."},
        "julian": {"name": "Julian", "role": "Observation", "district": "Observatoire", "age": "22", "quote": "Les chiffres mentent moins que nous.", "sprite": "images/character/julian/portrait.png", "expressions": ["neutre", "reflexion", "triste"], "backstory": "Analyse les cycles d'incidents.", "relations": "Affinité intellectuelle avec Noam."},
        "iris": {"name": "Iris", "role": "Réseaux internes", "district": "Repos", "age": "20", "quote": "Le silence est aussi un signal.", "sprite": "images/character/iris/portrait.png", "expressions": ["neutre", "peur", "joie"], "backstory": "Répare les intercoms et capteurs.", "relations": "Confie des informations fragmentaires à Noam."},
        "tomas": {"name": "Tomas", "role": "Archives", "district": "Salle d'Archive", "age": "25", "quote": "Si ce n'est pas consigné, c'est déjà perdu.", "sprite": "images/character/tomas/portrait.png", "expressions": ["neutre", "reflechit", "desaccord"], "backstory": "Archiviste des directives Kami.", "relations": "Joutes argumentatives avec Julian."},
        "kael": {"name": "Kael", "role": "Maintenance lourde", "district": "Maintenance", "age": "26", "quote": "On ne négocie pas avec une turbine en panne.", "sprite": "images/character/kael/portrait.png", "expressions": ["neutre", "colere", "determine"], "backstory": "Responsable des infrastructures critiques.", "relations": "Conflits avec ceux qui sous-estiment la technique."},
        "nyra": {"name": "Nyra", "role": "Protocole du Conclave", "district": "Conclave", "age": "23", "quote": "Le cadre protège de l'arbitraire.", "sprite": "images/character/nyra/portrait.png", "expressions": ["neutre", "sourire", "desaccord"], "backstory": "Gardienne des règles de séance.", "relations": "Alliance variable avec Lysa selon le contexte."},
        "ryn": {"name": "Ryn", "role": "Sécurité de proximité", "district": "Gymnase", "age": "21", "quote": "Le danger n'attend pas les votes.", "sprite": "images/character/ryn/portrait.png", "expressions": ["neutre", "inquiet", "determine"], "backstory": "Patrouilles en zones instables.", "relations": "Peut basculer entre Elias et Kael."},
        "sael": {"name": "Sael", "role": "SAS Livraison", "district": "Livraison", "age": "24", "quote": "Je vois ce qui entre. Et ce qui disparaît.", "sprite": "images/character/sael/portrait.png", "expressions": ["neutre", "mefiant", "sourire"], "backstory": "Interface entre l'extérieur et le Conclave.", "relations": "Soupçonne des anomalies de distribution."},
    }

    CODEX_ENTRIES = {
        "districts_conclave": {
            "title": "Districts du Conclave",
            "category": "Districts",
            "unlocked_day": 1,
            "text": """Le Conclave n'est pas une ville au sens ancien du terme, mais une agrégation de zones spécialisées reliées par des couloirs pressurisés, des sas et des routines de rationnement. Chaque district fonctionne comme un organe: la Cafétéria assure l'apport énergétique, l'Infirmerie absorbe les chocs biologiques, la Maintenance prolonge la survie mécanique, l'Observatoire anticipe les ruptures.

Depuis la troisième réorganisation, l'administration Kami impose une circulation par quotas temporels: on ne traverse pas un district parce qu'on le souhaite, mais parce qu'un besoin est validé. Ce système diminue les incidents, tout en créant des angles morts sociaux. Les représentants, censés compenser cette fragmentation, deviennent alors des filtres d'information autant que des voix politiques.

On observe enfin un phénomène propre aux environnements clos: l'identité individuelle se confond progressivement avec le district d'appartenance. Un conflit entre personnes se présente rapidement comme un conflit entre fonctions. Cette translation explique pourquoi les votes du Conclave paraissent souvent « techniques » alors qu'ils sont traversés d'affects et de mémoire."""
        },
        "systeme_votes": {
            "title": "Système de vote des représentants",
            "category": "Systèmes",
            "unlocked_day": 1,
            "text": """Le vote n'est pas un rituel démocratique classique; c'est un protocole de répartition du risque. Douze représentants y participent, avec un poids théoriquement égal, mais des conséquences asymétriques selon la proposition adoptée. Une mesure sur l'énergie peut pénaliser immédiatement la Maintenance, alors qu'une mesure sur le rationnement affectera d'abord la Cafétéria et la Santé.

Le règlement Kami distingue trois niveaux: recommandation, directive locale et dérogation d'urgence. La recommandation est consultative; la directive locale devient exécutoire dès majorité simple; la dérogation exige un seuil renforcé et une justification archivable. Dans la pratique, la frontière entre ces catégories dépend de l'état de crise déclaré.

Les observateurs extérieurs décrivent ce modèle comme « froid ». Pourtant, les archives montrent que les alignements de vote suivent aussi des affinités interpersonnelles, des dettes symboliques et des conflits antérieurs. Comprendre la mécanique officielle sans lire les liens informels revient à lire seulement la moitié du système."""
        },
        "personnage_noam": {
            "title": "Noam — médiateur émergent",
            "category": "Personnages",
            "linked_profile": "noam",
            "unlocked_day": 1,
            "text": """Noam occupe une position paradoxale: il ne possède ni l'ancienneté de Tomas, ni l'autorité procédurale de Nyra, ni l'assise technique de Kael. Pourtant, il obtient un avantage décisif dans les séquences de débat: la capacité à reformuler sans humilier.

Les témoins décrivent chez lui une écoute orientée vers les « points de friction utiles ». Là où d'autres cherchent à gagner une confrontation, Noam tente d'identifier le noyau non négociable de chaque interlocuteur puis de construire un terrain d'accord minimal. Cette méthode ralentit la décision à court terme, mais réduit la probabilité de sabotage passif après le vote.

Les analyses psychologiques internes relèvent également un coût personnel. Un médiateur absorbe la charge émotionnelle de plusieurs camps sans appartenir pleinement à aucun. À mesure que les crises s'enchaînent, Noam peut devenir soit un pivot de cohésion, soit un point de rupture."""
        },
        "rationnement_consequences": {
            "title": "Conséquences des bons de rationnement",
            "category": "Histoire",
            "text": """Après chaque vote sur les bons de rationnement, l'effet immédiat est mesurable (portion, files, incidents), mais l'effet profond est comportemental. Les ménages adaptent leurs horaires, les personnels médicaux déplacent les soins non urgents, les équipes techniques choisissent quelles pannes « attendre ». Le rationnement redistribue le temps autant que la nourriture.

Les bulletins Kami présentent ces ajustements comme des preuves de résilience. Les témoignages anonymes, eux, parlent de fatigue stratégique: chacun optimise sa survie locale au détriment d'une vision commune. C'est dans cet écart narratif que naissent les tensions politiques du Conclave."""
        },
    }


    def clamp_affinity(value):
        return max(0, min(100, int(value)))

    def add_affinity(profile_id, delta, unlock_thresholds=True):
        if profile_id not in store.profile_affinity:
            return
        store.profile_affinity[profile_id] = clamp_affinity(store.profile_affinity[profile_id] + delta)
        store.profile_global_points += delta

    def register_debate_alignment(profile_id, agreed=True):
        add_affinity(profile_id, 4 if agreed else -6)

    def unlock_profile_section(profile_id, section="story"):
        if profile_id not in PROFILE_DATA:
            return
        if section == "story":
            store.profile_story_unlocked[profile_id] = True
        elif section == "relations":
            store.profile_relations_unlocked[profile_id] = True

    def unlock_codex_entry(entry_id):
        if entry_id not in store.codex_unlocked_entries and entry_id in CODEX_ENTRIES:
            store.codex_unlocked_entries.append(entry_id)

    def codex_completion_percent():
        total = len(CODEX_ENTRIES)
        unlocked = len(store.codex_unlocked_entries)
        return int((100.0 * unlocked) / total) if total else 0

    def profile_portrait(profile_id):
        portrait = "images/character/{}/portrait.png".format(profile_id)
        return portrait if renpy.loadable(portrait) else PROFILE_DATA[profile_id]["sprite"]

    def profile_skin_path(profile_id, skin_id):
        if skin_id == "neutre":
            neutral = "images/character/{}/neutre.png".format(profile_id)
            if renpy.loadable(neutral):
                return neutral
            return profile_portrait(profile_id)
        return "images/character/{}/skins/{}.png".format(profile_id, skin_id)

    def get_profile_unlocked_skins(profile_id):
        unlocked = list(persistent.profile_wardrobe_unlocked.get(profile_id, []))
        if "neutre" not in unlocked:
            unlocked.insert(0, "neutre")
        return unlocked

    def get_profile_equipped_skin(profile_id):
        equipped = persistent.profile_skin_equipped.get(profile_id, "neutre")
        if equipped not in get_profile_unlocked_skins(profile_id):
            equipped = "neutre"
        return equipped

    def profile_display_image(profile_id):
        skin_id = get_profile_equipped_skin(profile_id)
        skin_path = profile_skin_path(profile_id, skin_id)
        if renpy.loadable(skin_path):
            return skin_path
        return profile_portrait(profile_id)

    def unlock_profile_skin(profile_id, skin_id):
        unlocked = set(persistent.profile_wardrobe_unlocked.get(profile_id, []))
        unlocked.add(skin_id)
        persistent.profile_wardrobe_unlocked[profile_id] = sorted(unlocked)
        renpy.save_persistent()

    def equip_profile_skin(profile_id, skin_id):
        if skin_id in get_profile_unlocked_skins(profile_id):
            persistent.profile_skin_equipped[profile_id] = skin_id
            renpy.save_persistent()


screen profiles_menu():
    tag menu

    default selected_profile = "noam"

    use game_menu(_("Profils"), scroll="viewport"):

        vbox:
            spacing 14

            viewport:
                mousewheel "horizontal"
                draggable True
                scrollbars "horizontal"
                xfill True
                ymaximum 132

                hbox:
                    spacing 12
                    for pid in PROFILE_ORDER:
                        $ pdata = PROFILE_DATA[pid]
                        $ portrait_path = profile_portrait(pid)
                        imagebutton:
                            idle Transform(portrait_path, xsize=96, ysize=96)
                            hover Transform(portrait_path, xsize=102, ysize=102)
                            action SetScreenVariable("selected_profile", pid)

            $ profile = PROFILE_DATA[selected_profile]
            $ affinity_val = profile_affinity[selected_profile]

            frame:
                background Solid("#111a24dd")
                xfill True
                yfill True
                padding (20, 18)

                vbox:
                    spacing 14

                    hbox:
                        spacing 16
                        text "[profile['name']]" size 42 color "#FFFFFF"
                        textbutton "👗":
                            action Show("profile_wardrobe", profile_id=selected_profile)

                    text "[profile['role']] — District: [profile['district']] — Âge: [profile['age']]" size 24 color "#D2E3F6"

                    hbox:
                        spacing 24

                        hbox:
                            spacing 12
                            add Transform(profile_portrait(selected_profile), xsize=320, ysize=320)
                            add Transform(profile_display_image(selected_profile), xsize=320, ysize=320)

                        vbox:
                            spacing 10
                            text "Affinité" size 24 color "#FFFFFF"
                            text "[affinity_val]/100" size 24 color "#FFFFFF"

                    frame:
                        background Solid("#060b12ba")
                        xfill True
                        padding (12, 10)
                        text "« [profile['quote']] »" size 23 color "#FFE7AE" italic True

                    vbox:
                        spacing 8
                        text "Backstory" size 26 color "#9FD4FF"
                        if profile_story_unlocked[selected_profile]:
                            text "[profile['backstory']]" size 22 color "#E8EEF5"
                        else:
                            text "Verrouillé — se débloque pendant les discussions et événements narratifs." size 20 color "#8EA3B8"

                        text "Relations" size 26 color "#9FD4FF"
                        if profile_relations_unlocked[selected_profile]:
                            text "[profile['relations']]" size 22 color "#E8EEF5"
                        else:
                            text "Verrouillé — se débloque pendant les discussions et les interactions clés." size 20 color "#8EA3B8"


screen profile_wardrobe(profile_id):
    modal True
    zorder 400

    $ unlocked_skins = get_profile_unlocked_skins(profile_id)

    add Solid("#00000090")

    frame:
        background Solid("#121926f5")
        xalign 0.5
        yalign 0.5
        xsize 920
        ysize 620
        padding (22, 20)

        vbox:
            spacing 14
            text "Garde-robe — [PROFILE_DATA[profile_id]['name']]" size 36 color "#FFFFFF"
            text "Débloque des skins via des variables persistantes, puis équipe-les ici (appliqués à la partie droite du cadre)." size 20 color "#BFD6EA"

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                ymaximum 430

                vbox:
                    spacing 8
                    for skin_id in unlocked_skins:
                        $ skin_path = profile_skin_path(profile_id, skin_id)
                        $ display_path = skin_path if renpy.loadable(skin_path) else profile_portrait(profile_id)
                        hbox:
                            spacing 12
                            add Transform(profile_portrait(profile_id), xsize=96, ysize=96)
                            add Transform(display_path, xsize=96, ysize=96)
                            textbutton "Équiper [skin_id]":
                                action Function(equip_profile_skin, profile_id, skin_id)

            textbutton "Fermer" action Hide("profile_wardrobe") xalign 1.0


screen codex_menu():
    tag menu

    default selected_entry = "districts_conclave"

    use game_menu(_("Codex"), scroll="viewport"):

        hbox:
            spacing 24

            frame:
                background Solid("#110f0dcc")
                xsize 360
                yfill True
                padding (14, 14)

                vbox:
                    spacing 8
                    text "Index" size 34 color "#E8D8B8"
                    text "Complétion: [codex_completion_percent()]%" size 22 color "#C9B896"

                    null height 8

                    for eid, entry in CODEX_ENTRIES.items():
                        $ unlocked = eid in codex_unlocked_entries
                        textbutton "[entry['title']]":
                            action SetScreenVariable("selected_entry", eid)
                            sensitive unlocked

            $ entry = CODEX_ENTRIES[selected_entry]
            $ is_unlocked = selected_entry in codex_unlocked_entries

            frame:
                background Solid("#1a1612dd")
                xfill True
                yfill True
                padding (18, 18)

                vbox:
                    spacing 12
                    text "[entry['title']]" size 40 color "#F8E7C2"
                    if is_unlocked:
                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            ysize 580

                            text "[entry['text']]" size 22 color "#EFE7D8" line_spacing 4
                    else:
                        text "Entrée verrouillée. Déclenche un événement narratif pour l'ajouter au Codex." size 22 color "#A99779"


screen exploration_meta_buttons():
    zorder 240

    hbox:
        spacing 10
        xalign 0.98
        yalign 0.03

        textbutton "Profils" action ShowMenu("profiles_menu")
        textbutton "Codex" action ShowMenu("codex_menu")
