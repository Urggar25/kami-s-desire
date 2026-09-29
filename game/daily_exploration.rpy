# =============================================================================
# EXPLORATION QUOTIDIENNE — découvertes facultatives J4 à J20
# =============================================================================

default daily_exploration_seen = []
default daily_exploration_room = None

init python:

    DAILY_EXPLORATION_RETURN_LABELS = {
        "archive": "ARCHIVE_TP",
        "cafeteria": "CAFETERIA_TP",
        "canon": "CANON_TP",
        "conclave": "CONCLAVE_TP",
        "dortoir": "DORTOIR_TP",
        "gymnase": "GYMNASE_TP",
        "infirmerie": "INFIRMERIE_TP",
        "livraison": "LIVRAISON_TP",
        "maintenance": "MAINTENANCE_TP",
        "observation": "OBSERVATION_TP",
        "repos": "REPOS_TP",
        "stockage": "STOCKAGE_TP",
    }

    # Chaque entrée n'existe qu'un jour donné. Les dialogues sont courts et
    # facultatifs : ils enrichissent l'ambiance sans déplacer une scène canon.
    DAILY_EXPLORATION_DISCOVERIES = {
        4: {
            "cafeteria": {"title": "UN PLATEAU EN TROP", "lines": [
                (None, "Un plateau propre attend seul au bout d'une table, avec douze couverts parfaitement alignés."),
                ("think", "Même quand personne ne mange, Goumi prépare une place pour chacun."),
                ("goumi", "Anticiper une présence réduit de 4,2 % le délai de service."),
                ("noam", "C'est presque une façon de dire que tu nous attends."),
                ("goumi", "Cette interprétation n'est pas nécessaire au service."),
            ]},
            "conclave": {"title": "MICROS OUVERTS", "lines": [
                (None, "Un voyant reste allumé sous le siège de Sael alors que la salle est vide."),
                ("think", "Les micros s'éteignent-ils vraiment entre deux débats ?"),
                (None, "Le voyant disparaît exactement au moment où je me penche."),
            ]},
            "repos": {"title": "RÈGLES DU JEU", "lines": [
                (None, "Julian a laissé un jeu de cartes ouvert sur la table. Toutes les cartes gagnantes sont déjà séparées du paquet."),
                ("julian", "Je préparais une démonstration statistique."),
                ("noam", "Avec toutes les bonnes cartes de ton côté ?"),
                ("julian", "C'est la partie démonstrative."),
            ]},
        },
        5: {
            "observation": {"title": "UN DISTRICT SANS IMAGE", "lines": [
                (None, "Parmi les flux du monde, une vignette reste noire. Aucun nom, seulement un compteur qui continue."),
                ("think", "Même une image absente produit encore des données."),
            ]},
            "infirmerie": {"title": "COMPRESSE MANQUANTE", "lines": [
                (None, "Une case de l'inventaire médical clignote : une compresse utilisée, aucune identité associée."),
                ("mara", "Avant que tu demandes : non, je ne fiche pas chaque coupure de papier."),
                ("noam", "Tu as répondu avant que je demande."),
                ("mara", "Parce que ton visage pose des questions bruyantes."),
            ]},
            "maintenance": {"title": "PIÈCE NON RÉPERTORIÉE", "lines": [
                (None, "Une vis noire repose sur l'établi de Kael. Son pas ne correspond à aucun appareil visible."),
                ("kael", "Je l'ai trouvée dans le couloir."),
                ("noam", "Tu collectionnes les vis maintenant ?"),
                ("kael", "Seulement celles qui ne devraient pas exister."),
            ]},
        },
        6: {
            "cafeteria": {"title": "CARTE DES FRONTIÈRES", "lines": [
                (None, "L'écran diffuse une carte des frontières. Certaines lignes bougent de quelques mètres entre deux rafraîchissements."),
                ("think", "Même une frontière immobile dépend de celui qui la dessine."),
            ]},
            "gymnase": {"title": "DEUX RYTHMES", "lines": [
                (None, "Deux serviettes sont posées près des tapis. L'une est soigneusement pliée, l'autre jetée en boule."),
                ("elias", "Ryn appelle ça un échauffement commun."),
                ("ryn", "Elias appelle tout ce qui est amusant un risque articulaire."),
                ("elias", "Parce que tes articulations prennent de mauvaises décisions."),
            ]},
            "conclave": {"title": "BULLETIN TEST", "lines": [
                (None, "Le terminal accepte encore des bulletins de diagnostic. Pour, contre, abstention : chaque choix produit exactement le même bip."),
                ("think", "Le son ne permet pas de deviner ce que les autres décident."),
            ]},
        },
        7: {
            "stockage": {"title": "EMPLACEMENTS VIDES", "lines": [
                (None, "Plusieurs rectangles clairs découpent la poussière sur une étagère technique."),
                ("think", "Quelque chose était rangé ici récemment. Plusieurs choses."),
                (None, "Les codes de stock ont été grattés avec un outil fin."),
            ]},
            "maintenance": {"title": "LISTE DE KAEL", "lines": [
                (None, "Kael a écrit trois colonnes sur un écran : utile, dangereux, les deux."),
                ("kael", "Ne touche pas à la troisième colonne."),
                ("noam", "Qu'est-ce qu'il y a dedans ?"),
                ("kael", "Tout ce qui est intéressant."),
            ]},
            "livraison": {"title": "RUBAN DE CONTRÔLE", "lines": [
                (None, "Un morceau de ruban de sécurité a été recollé avec soin sur une caisse vide."),
                ("sael", "Quelqu'un voulait qu'on pense qu'elle n'avait jamais été ouverte."),
                ("noam", "Ça a marché ?"),
                ("sael", "Tu poses la question devant une caisse ouverte."),
            ]},
        },
        8: {
            "dortoir": {"title": "POUSSIÈRE DÉPLACÉE", "lines": [
                (None, "La poussière sous la grille d'aération forme un arc net, comme si le métal avait bougé récemment."),
                ("think", "Je l'ai peut-être touchée pendant ma fouille. Peut-être."),
            ]},
            "cafeteria": {"title": "LE SERVICE DE LÉA", "lines": [
                (None, "Goumi affiche brièvement le nom de Léa avant de corriger la commande de Kael."),
                ("kael", "Tu as vu ça ?"),
                ("noam", "Oui."),
                ("goumi", "Erreur de cache corrigée."),
                ("kael", "Bien sûr."),
            ]},
            "observation": {"title": "ANGLE MORT", "lines": [
                (None, "La caméra du dortoir saute une image toutes les cinquante-neuf secondes."),
                ("think", "Pas assez pour cacher une personne. Assez pour rendre chaque mouvement moins certain."),
            ]},
        },
        9: {
            "conclave": {"title": "VINGT SIÈGES", "lines": [
                (None, "Le plan d'évacuation du Conclave regroupe les personnes par blocs de vingt."),
                ("think", "À vingt, un groupe reste un groupe. À vingt et un, il devient une infraction."),
            ]},
            "cafeteria": {"title": "TABLES SÉPARÉES", "lines": [
                (None, "Les tables pourraient accueillir vingt-quatre personnes, mais les fixations au sol les divisent en groupes de six."),
                ("elen", "Même le mobilier a une opinion sur le vote."),
                ("noam", "Au moins, il ne demande pas la parole."),
            ]},
            "archive": {"title": "FORMULAIRE IV-21", "lines": [
                (None, "Un formulaire de rassemblement exige le nom de chaque participant, même pour une réunion imprévue."),
                ("tomas", "Il faut soumettre la liste quarante-huit heures avant."),
                ("noam", "Et si on ne sait pas encore qui viendra ?"),
                ("tomas", "Alors le système considère que personne ne devrait venir."),
            ]},
        },
        10: {
            "archive": {"title": "TEMPÉRATURE IMPOSSIBLE", "lines": [
                (None, "Le relais prétend ventiler normalement. La poussière sur la grille, elle, n'a pas bougé."),
                ("think", "L'écran et la pièce ne racontent pas la même chose."),
            ]},
            "gymnase": {"title": "MARQUES AU SOL", "lines": [
                (None, "Une série de traces humides va du conduit au sac de frappe puis s'arrête sans rejoindre la porte."),
                ("iris", "J'ai nettoyé avant de partir."),
                ("noam", "Donc elles sont apparues après ?"),
                ("iris", "C'est précisément ce que j'évite de conclure trop vite."),
            ]},
            "infirmerie": {"title": "CAPTEUR EN RETARD", "lines": [
                (None, "Le capteur mural affiche la température d'il y a six minutes."),
                ("think", "Un retard minuscule. Sauf si tout le système en accumule."),
            ]},
        },
        11: {
            "observation": {"title": "SEPT JOURS BLANCS", "lines": [
                (None, "Une ligne de la chronologie saute exactement sept jours puis reprend sans signaler d'erreur."),
                ("think", "Une absence assez propre pour ressembler à une règle."),
            ]},
            "archive": {"title": "INDEX SANS TITRE", "lines": [
                (None, "Douze entrées partagent la même date et aucun titre. Chacune possède pourtant une taille différente."),
                ("tomas", "Ce ne sont pas des fichiers vides."),
                ("noam", "Seulement des fichiers qu'on ne doit pas nommer ?"),
                ("tomas", "C'est... une possibilité."),
            ]},
            "dortoir": {"title": "BRUIT DE SYNCHRONISATION", "lines": [
                (None, "Les tablettes des chambres vibrent presque ensemble, avec un décalage régulier de porte en porte."),
                ("think", "Comme si quelque chose parcourait le couloir sans marcher."),
            ]},
        },
        12: {
            "dortoir": {"title": "ZONE MUETTE", "lines": [
                (None, "À un pas du brouilleur, le bourdonnement des lampes disparaît presque totalement."),
                ("think", "L'intimité ressemble beaucoup à un silence artificiel."),
            ]},
            "cafeteria": {"title": "CAMÉRA DE SERVICE", "lines": [
                (None, "Une lentille suit Goumi derrière le comptoir, même lorsque le brouilleur portatif est activé."),
                ("goumi", "La sécurité alimentaire ne peut être désactivée."),
                ("noam", "Donc il reste toujours une caméra."),
                ("goumi", "Il reste toujours une procédure."),
            ]},
            "maintenance": {"title": "BOÎTIER OUVERT", "lines": [
                (None, "Un brouilleur démonté révèle un second circuit absent du schéma public."),
                ("kael", "Le circuit ne transmet rien. Il attend."),
                ("noam", "Quoi ?"),
                ("kael", "C'est bien le problème."),
            ]},
        },
        13: {
            "archive": {"title": "DEUX HORODATAGES", "lines": [
                (None, "Une même entrée porte deux heures de création séparées de treize minutes."),
                ("think", "Même les fichiers peuvent hésiter sur le moment où ils ont commencé à exister."),
            ]},
            "cafeteria": {"title": "COMMANDE EN DOUBLE", "lines": [
                (None, "Goumi imprime deux tickets identiques au nom de Noam, puis détruit le premier."),
                ("goumi", "Doublon supprimé."),
                ("noam", "Je n'ai commandé qu'une fois ?"),
                ("goumi", "C'est également ce qu'indique le second ticket."),
            ]},
            "observation": {"title": "REFLET DÉCALÉ", "lines": [
                (None, "Dans la vitre noire d'un moniteur, mon reflet semble tourner la tête une fraction de seconde trop tard."),
                ("think", "Fatigue. Écran lent. N'importe quoi de raisonnable."),
            ]},
        },
        14: {
            "cafeteria": {"title": "PLACE ÉVITÉE", "lines": [
                (None, "Personne ne s'assoit à la place que j'occupais hier. Aucun objet ne la réserve."),
                ("think", "Ils ne se sont peut-être même pas concertés."),
            ]},
            "conclave": {"title": "DOSSIERS PRIVÉS", "lines": [
                (None, "L'aperçu du prochain vote énumère les données publiques, médicales et personnelles dans la même colonne."),
                ("nyra", "La transparence totale est une formule. Pas encore une solution."),
                ("noam", "Tu as déjà choisi ?"),
                ("nyra", "J'ai choisi de lire les petites lignes."),
            ]},
            "maintenance": {"title": "OUTIL REPLACÉ", "lines": [
                (None, "Un tournevis porte une fine poussière grise alors que le reste de l'établi vient d'être nettoyé."),
                ("think", "Quelqu'un l'a utilisé loin d'ici, puis l'a remis exactement à sa place."),
            ]},
        },
        15: {
            "observation": {"title": "IMAGE ENTRE DEUX IMAGES", "lines": [
                (None, "En avançant image par image, un visage apparaît dans la compression puis disparaît au cadre suivant."),
                ("kael", "Un artefact peut ressembler à n'importe quoi si tu le regardes assez longtemps."),
                ("noam", "Et si je ne le regarde pas assez longtemps ?"),
                ("kael", "Alors tu rates peut-être la seule image importante."),
            ]},
            "archive": {"title": "INDEX COMPLET", "lines": [
                (None, "Pendant une seconde, le terminal affiche des milliers de catégories supplémentaires avant de refermer l'index."),
                ("think", "Le vote n'a pas encore eu lieu, mais les données se préparent déjà."),
            ]},
            "dortoir": {"title": "VERROU SANS ALERTE", "lines": [
                (None, "Le journal de la porte confirme une ouverture nocturne sans enregistrer d'identifiant."),
                ("think", "La porte sait qu'elle s'est ouverte. Elle refuse seulement de dire pour qui."),
            ]},
        },
        16: {
            "cafeteria": {"title": "CONVERSATIONS COUPÉES", "lines": [
                (None, "Trois discussions s'arrêtent lorsque j'entre. Une seule reprend après mon passage."),
                ("lysa", "Ne leur en veux pas. La peur rend les gens très mauvais acteurs."),
                ("noam", "Et toi ?"),
                ("lysa", "Moi, j'étais déjà excellente avant."),
            ]},
            "archive": {"title": "REQUÊTE DE SAEL", "lines": [
                (None, "Une requête récente porte les initiales de Sael. Le sujet a été effacé, pas l'heure."),
                ("think", "Elle est venue ici avant de me demander de la rejoindre."),
            ]},
            "maintenance": {"title": "CAMÉRA PORTATIVE", "lines": [
                (None, "Kael a assemblé une caméra autonome à partir de pièces incompatibles."),
                ("kael", "Elle enregistre localement. Aucun réseau, aucune excuse."),
                ("noam", "Tu comptes filmer quoi ?"),
                ("kael", "Ce qui prétendra ne pas être passé."),
            ]},
        },
        17: {
            "dortoir": {"title": "AIR FROID", "lines": [
                (None, "Un filet d'air froid passe sous la grille malgré l'arrêt annoncé de la ventilation."),
                ("think", "Quelque chose relie encore les chambres."),
            ]},
            "maintenance": {"title": "VIS DE GRILLE", "lines": [
                (None, "Mara compare plusieurs tournevis et en choisit un sans hésiter."),
                ("mara", "Si quelqu'un demande, je répare une étagère."),
                ("noam", "Quelle étagère ?"),
                ("mara", "Celle qui aura besoin d'être réparée quand on nous attrapera."),
            ]},
            "infirmerie": {"title": "RÉFÉRENCE M16", "lines": [
                (None, "Le terminal reconnaît M16 comme une procédure, mais refuse d'afficher son domaine médical."),
                ("think", "Même la catégorie est protégée."),
            ]},
        },
        18: {
            "cafeteria": {"title": "DEUX MARA", "lines": [
                (None, "Goumi hésite avant de valider la commande de Mara, comme si une autre session utilisait déjà son identifiant."),
                ("mara", "Dis-moi que j'ai au moins commandé quelque chose de bon."),
                ("goumi", "La seconde commande n'est pas accessible."),
                ("mara", "Évidemment."),
            ]},
            "observation": {"title": "PLAN INCOMPLET", "lines": [
                (None, "Le plan technique laisse un espace vide entre les dortoirs et la cafétéria."),
                ("think", "Assez grand pour une pièce. Ou pour plusieurs passages."),
            ]},
            "repos": {"title": "BRUIT DERRIÈRE LE MUR", "lines": [
                (None, "Un frottement avance derrière le mur puis s'arrête à hauteur de la ventilation."),
                ("noam", "Tu as entendu ?"),
                ("mara", "Non."),
                (None, "Elle répond trop vite, les yeux fixés sur la grille."),
            ]},
        },
        19: {
            "maintenance": {"title": "OUTILS DÉPLACÉS", "lines": [
                (None, "Trois outils manquent à leur contour peint. Les emplacements sont trop propres pour une absence ancienne."),
                ("think", "Quelqu'un continue d'utiliser cette pièce."),
            ]},
            "observation": {"title": "PRÉSENCE SANS BADGE", "lines": [
                (None, "Le réseau compte treize présences internes pour douze badges actifs."),
                ("think", "Le nombre revient à douze avant que je puisse ouvrir le détail."),
            ]},
            "conclave": {"title": "MICRO DE MARA", "lines": [
                (None, "Le micro de Mara contient deux profils vocaux presque parfaitement superposés."),
                ("think", "Presque."),
            ]},
        },
        20: {
            "infirmerie": {"title": "SIGNES VITAUX", "lines": [
                (None, "Le capteur confirme les signes vitaux de Mara. Une ancienne mesure identique reste pourtant ouverte en arrière-plan."),
                ("mara", "Tu veux vérifier mon pouls toi-même ?"),
                ("noam", "Je ne sais pas si ça aiderait."),
                ("mara", "Alors arrête de regarder la machine comme si elle allait choisir laquelle de nous ment."),
            ]},
            "conclave": {"title": "TREIZIÈME CONNEXION", "lines": [
                (None, "Le panneau des représentants affiche brièvement un treizième emplacement sans nom."),
                ("think", "Le cadre disparaît, mais l'espace entre les portraits reste légèrement trop large."),
            ]},
            "dortoir": {"title": "PORTE DÉJÀ OUVERTE", "lines": [
                (None, "Ma porte se déverrouille une fraction de seconde avant que mon badge touche le lecteur."),
                ("think", "Comme si quelqu'un, de l'autre côté, savait que j'arrivais."),
            ]},
        },
    }

    def daily_exploration_key(day, room_name):
        return "{}:{}".format(int(day), room_name)

    def daily_exploration_entry(room_name, day=None):
        shown_day = int(day if day is not None else day_number())
        return DAILY_EXPLORATION_DISCOVERIES.get(shown_day, {}).get(room_name)

    def daily_exploration_available(room_name):
        if not (getattr(store, "free_time_active", False) or getattr(store, "exploration_libre_active", False)):
            return False
        entry = daily_exploration_entry(room_name)
        if not entry:
            return False
        return daily_exploration_key(day_number(), room_name) not in getattr(store, "daily_exploration_seen", [])

    def daily_exploration_mark_seen(room_name):
        key = daily_exploration_key(day_number(), room_name)
        seen = list(getattr(store, "daily_exploration_seen", []))
        if key not in seen:
            seen.append(key)
        store.daily_exploration_seen = seen

    def daily_exploration_play_lines(entry):
        # L'exploration scénarisée ne doit jamais se transformer en temps libre
        # social. Dans ce mode, on conserve uniquement les observations et la
        # pensée de Noam ; les échanges parlés restent réservés au temps libre.
        social_mode = social_free_time_active()
        for speaker_id, line in entry.get("lines", []):
            if not social_mode and speaker_id not in (None, "think"):
                continue
            if speaker_id is None:
                renpy.say(None, line)
            else:
                speaker = getattr(store, speaker_id, None)
                renpy.say(speaker, line)


transform daily_discovery_pulse:
    alpha 0.72
    ease 0.8 alpha 1.0
    ease 0.8 alpha 0.72
    repeat


screen daily_exploration_hotspot(room_name):
    if daily_exploration_available(room_name):
        $ daily_entry = daily_exploration_entry(room_name)
        button at daily_discovery_pulse:
            xalign 0.97
            yalign 0.13
            xsize 330
            ysize 74
            background Solid("#071722E8")
            hover_background Solid("#12405AEA")
            action [SetVariable("daily_exploration_room", room_name), Jump("DAILY_EXPLORATION_DISCOVERY")]
            vbox:
                xalign 0.5 yalign 0.5 spacing 2
                text "NOUVEL ÉLÉMENT" xalign 0.5 size 13 color "#5CD3FF" kerning 2
                text daily_entry["title"] xalign 0.5 size 18 color "#E9F8FF"


label DAILY_EXPLORATION_DISCOVERY:
    $ _daily_entry = daily_exploration_entry(daily_exploration_room)
    $ _daily_return = DAILY_EXPLORATION_RETURN_LABELS.get(daily_exploration_room, "START_EXPLORATION_LIBRE_MAP")

    if _daily_entry is None:
        jump expression _daily_return

    call DAILY_EXPLORATION_INLINE(daily_exploration_room) from _call_daily_exploration_inline_from_room
    jump expression _daily_return


label DAILY_EXPLORATION_INLINE(room_name):
    $ _daily_entry = daily_exploration_entry(room_name)
    if _daily_entry is None:
        return

    $ daily_exploration_mark_seen(room_name)
    play sound "audio/sfx_beep.mp3"
    $ renpy.notify("EXPLORATION — " + _daily_entry["title"])
    $ daily_exploration_play_lines(_daily_entry)
    return


label OFFER_DAILY_EXPLORATION(next_label, required_visits=0, allowed_rooms=None, title="Temps d'exploration", destination_room=None):
    # La destination fait désormais partie du récit : le joueur l'atteint par
    # la carte et reste libre de visiter les salles disponibles sur sa route.
    call START_EXPLORATION_LIBRE(next_label, required_visits, allowed_rooms, title, destination_room) from _call_daily_exploration_offer
    return

