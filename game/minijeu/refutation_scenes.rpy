default day3_julian_clash_rewarded = False

# Réfutations scénarisées. Chaque duel conserve plusieurs voix et une faille démontrable.
# Les entrées verrouillées restent visibles dans la tablette (voir refutation.rpy).

init python:
    refutation_register(
        "j3_julian", title=_("JULIAN — PRENDRE LA PAROLE"), bg="bg_repos",
        statements=[
            ("julian", "sourire", _("On veut tous que ça passe. [[Je ne fais que les aider]] à se décider.")),
            ("tomas", "inquiet", _("Julian, je t'ai demandé de [[me laisser réfléchir]].")),
            ("julian", "taquin", _("Je force personne. Je leur donne juste [[un peu d'élan]].")),
            ("julian", "determine", _("Les indécis [[m'ont choisi pour les représenter]].")),
            ("nyra", "neutre", _("Tu devrais surtout arrêter de [[parler à leur place]].")),
        ],
        fragments=[("mandat", _("Personne ne t'a mandaté")), ("tomas", _("La demande de Tomas")), ("texte", _("Le contenu du vote"))],
        solution={(3, 0): "mandat"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j3_assemblee", title=_("ASSEMBLÉE — LES RATIONS"), bg="bg_conclave",
        statements=[
            ("elias", "determine", _("Le commerce va [[récompenser ceux qui travaillent]].")),
            ("lysa", "opposition", _("Et si tu ne peux pas travailler, [[tu manges comment]] ?")),
            ("julian", "sourire", _("Au moins avec ce texte [[tout le monde aura sa chance]].")),
            ("julian", "determine", _("Avec les échanges, [[il n\u0027y aura plus de pénuries]].")),
            ("mara", "doute", _("Le problème, c'est qu'on ne sait pas [[qui assurera la transition]].")),
            ("ryn", "colere", _("Vous parlez de chiffres. Chez moi, [[les gens ont faim maintenant]] !")),
            ("nyra", "reflexion", _("Le texte permet des échanges, pas [[une distribution garantie]].")),
        ],
        fragments=[("penuries", _("La réalité des pénuries")), ("transition", _("L’énoncé précis du vote"), lambda: bool(getattr(store, "dossier_unlocked_args", {}).get("enonce_precis"))), ("liberte", _("La liberté de commercer"))],
        solution={(2, 0): "transition", (3, 0): "penuries"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j4_frontieres", title=_("FRONTIÈRES — DEUX PEURS"), bg="bg_repos",
        statements=[
            ("ryn", "colere", _("Tu votes contre, donc [[tu veux qu'on reste enfermés]] !")),
            ("sael", "determine", _("Je veux protéger mon village. [[Ouvrir sans contrôle]] serait dangereux.")),
            ("mara", "agace", _("Vous allez finir par [[vous hurler dessus toute la nuit]].")),
            ("ryn", "colere", _("Elle refuse le texte, alors [[elle défend les exécutions]] !")),
            ("sael", "fatigue", _("Tu peux m'écouter [[sans décider à ma place]] ce que je pense ?")),
        ],
        fragments=[("nuance", _("Refus du texte ≠ soutien aux tirs")), ("victimes", _("Morts aux frontières")), ("securite", _("Sécurité du village"))],
        solution={(3, 0): "nuance"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j7_anya", title=_("ANYA — DÉFIER KAMI"), bg="bg_sas",
        statements=[
            ("kami", "neutre", _("Une clandestine ? Très bien. [[Je vais l'éliminer]], le règlement est clair !")),
            ("nyra", "raison", _("Montre-nous [[la règle qui interdit sa présence]].")),
            ("kami", "taquin", _("Ce n'est pas une représentante. [[Elle n'a rien à faire ici]] !")),
            ("noam", "determine", _("Un tir dans ce sas [[pourrait percer la coque]].")),
            ("kami", "colere", _("Vous croyez vraiment pouvoir [[m'empêcher de décider]] ?")),
        ],
        fragments=[("regle", _("Aucune interdiction explicite")), ("coque", _("Risque pour la coque")), ("vote", _("Seuls les représentants votent"))],
        solution={(0, 0): "regle", (2, 0): "regle"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j9_regroupements", title=_("REGROUPEMENTS — LE PIÈGE"), bg="bg_conclave",
        statements=[
            ("kami", "taquin", _("Une seule abstention et [[tout sera réglé]] !")),
            ("tomas", "inquiet", _("Tu as ajouté une conséquence [[qu'on n'avait pas comprise]].")),
            ("kami", "neutre", _("Le vote est binaire. [[Je l'ai annoncé]].")),
            ("ryn", "colere", _("On ne peut pas traiter [[des milliers de gens]] comme un détail !")),
            ("kami", "sourire", _("Je vous ai donné les règles. [[Vous ne pouvez plus discuter]].")),
        ],
        fragments=[("formulation", _("Exiger une précision du texte")), ("urgence", _("Campements déjà présents")), ("delai", _("Le débat n'est pas clos"))],
        solution={(4, 0): "delai"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j10_brouilleurs", title=_("BROUILLEURS — VIE PRIVÉE"), bg="bg_conclave",
        statements=[
            ("mara", "reflexion", _("Sans surveillance, [[on ne pourra plus prévenir les crimes]].")),
            ("nyra", "raison", _("Protéger une conversation ne signifie pas [[supprimer toutes les caméras]].")),
            ("sael", "mefiant", _("Avec un brouilleur, [[on peut cacher n'importe quoi]].")),
            ("iris", "desaccord", _("Tu veux vraiment [[une caméra dans chaque chambre]] ?")),
            ("mara", "agace", _("Alors vous proposez [[une station sans aucun contrôle]] ?")),
        ],
        fragments=[("limites", _("Brouillage ponctuel, pas suppression")), ("surveillance", _("Les caméras protègent parfois")), ("cadre", _("Appareils enregistrés et encadrés"))],
        solution={(4, 0): "limites"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j15_kael", title=_("KAEL — L'ENREGISTREMENT"), bg="bg_chambre",
        statements=[
            ("kael", "inquietude", _("Je t'ai dit tout ce que je savais. [[Je n'ai rien caché]].")),
            ("noam", "colere", _("Et pourtant [[la vidéo ne colle pas]] avec ce que tu racontes.")),
            ("kael", "fatigue", _("Une caméra montre des images. [[Pas les intentions]].")),
            ("kael", "calme", _("Ce fichier, tu ne sais même pas [[s'il est complet]].")),
            ("noam", "determine", _("Alors explique-moi pourquoi [[on voit cette séquence]].")),
        ],
        fragments=[("video", _("L'enregistrement retrouvé")), ("chrono", _("Chronologie de la soirée")), ("intuition", _("Mon intuition"))],
        solution={(0, 0): "video"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j20_defense", title=_("NOAM — SOUS PRESSION"), bg="bg_infirmerie",
        statements=[
            ("lysa", "inquiet", _("Tu dis avoir vu Mara morte, mais [[personne n'a retrouvé son corps]].")),
            ("sael", "raison", _("On ne t'accuse pas. On dit seulement [[qu'on n'a pas de preuve]].")),
            ("lysa", "opposition", _("Et tu veux qu'on accepte [[toute ton histoire sur parole]] ?")),
            ("noam", "inquiet", _("Je peux au moins vous dire [[où je l'ai vue]].")),
            ("sael", "mefiant", _("Une chose à la fois. [[Qui avait accès à cet endroit]] ?")),
        ],
        fragments=[("lieu", _("Le lieu de la découverte")), ("conduits", _("Le réseau d'aération")), ("souvenir", _("Mon souvenir"))],
        solution={(2, 0): "lieu"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j24_tomas", title=_("TOMAS — UN TEXTE IMPARFAIT"), bg="bg_conclave",
        statements=[
            ("tomas", "raison", _("Le Commandement est trop vague. [[Kami pourra l'appliquer au minimum]].")),
            ("ryn", "colere", _("Alors selon toi, [[il vaut mieux ne rien voter]] ?")),
            ("tomas", "colere", _("Je n'ai pas dit ça ! [[Je demande des garanties]].")),
            ("julian", "taquin", _("À t'écouter, [[on ne fera jamais rien]].")),
            ("noam", "raison", _("Le texte est imparfait. Mais [[le rejeter n'améliore rien]].")),
        ],
        fragments=[("nuance", _("Tomas soutient le principe")), ("pragmatisme", _("Une amélioration partielle")), ("garantie", _("La précision des termes"))],
        solution={(1, 0): "nuance", (3, 0): "nuance"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j28_tomas", title=_("TOMAS — SUICIDE OU MEURTRE ?"), bg="bg_infirmerie",
        statements=[
            ("lysa", "reflexion", _("Il y avait un flacon. [[Ça ressemble à un suicide]].")),
            ("sael", "raison", _("On ne sait même pas [[s'il a pris ces comprimés]].")),
            ("lysa", "inquiet", _("La chambre était fermée. [[Personne n'a pu entrer]].")),
            ("noam", "raison", _("Les conduits sont accessibles. [[La porte n'est pas la seule entrée]].")),
            ("iris", "raison", _("On a relevé des signes d'intoxication. [[Ça ne prouve pas le suicide]].")),
        ],
        fragments=[("conduit", _("Accès par les conduits")), ("analyses", _("Conclusions médicales")), ("flacon", _("Le flacon de comprimés"))],
        solution={(2, 0): "conduit"}, lives=3, line_time=5.8,
    )

    refutation_register(
        "j29_porte", title=_("DOSSIER TOMAS — PORTE"), bg="bg_conclave",
        statements=[
            ("julian", "reflexion", _("La chambre était verrouillée. [[Personne n'a pu y entrer]].")),
            ("kael", "raison", _("Les techniciens passent aussi [[par le réseau d'aération]].")),
            ("lysa", "blase", _("Et le livre de Tomas [[ne prouve rien là-dessus]].")),
        ],
        fragments=[("aeration", _("Photos du dispositif d'aération")), ("livre", _("Le livre de Tomas"))],
        solution={(0, 0): "aeration"}, lives=3, line_time=5.0,
    )

    refutation_register(
        "j29_flacon", title=_("DOSSIER TOMAS — FLACON"), bg="bg_conclave",
        statements=[
            ("elen", "triste", _("Le flacon près du corps... [[il voulait peut-être mourir]].")),
            ("iris", "raison", _("On ignore [[s'il a avalé un comprimé]].")),
            ("julian", "inquiet", _("Alors les menaces reçues prouvent [[qu'il était désespéré]].")),
        ],
        fragments=[("medecine", _("Conclusions d'Iris")), ("menaces", _("Messages menaçants"))],
        solution={(0, 0): "medecine"}, lives=3, line_time=5.0,
    )

    refutation_register(
        "j29_plante", title=_("DOSSIER TOMAS — PLANTE"), bg="bg_conclave",
        statements=[
            ("ryn", "colere", _("Je connais son nom. Ça veut dire [[que je suis coupable]], maintenant ?")),
            ("sael", "raison", _("Cette plante pousse dans [[plusieurs régions arides]].")),
            ("julian", "reflexion", _("Mais elle vient de Limen. [[Un Limenois l'a forcément apportée]].")),
        ],
        fragments=[("livraisons", _("Registres des livraisons")), ("limen", _("Origine de la plante"))],
        solution={(2, 0): "livraisons"}, lives=3, line_time=5.0,
    )

    refutation_register(
        "j29_mobile", title=_("DOSSIER TOMAS — MOBILE"), bg="bg_conclave",
        statements=[
            ("lysa", "blase", _("Tout le monde lui en voulait pour son vote. [[C'est la seule piste]].")),
            ("julian", "reflexion", _("Il fouillait aussi dans [[une histoire de matériel disparu]].")),
            ("nyra", "neutre", _("Ses recherches sur Keyper [[n'impliquent pas un meurtrier]].")),
        ],
        fragments=[("keyper", _("Dossier Keyper et appareil disparu")), ("verrou", _("Verrou de la chambre"))],
        solution={(0, 0): "keyper"}, lives=3, line_time=5.0,
    )


# Fonctions d'influence du vote J3 conservées sans dépendance à l'ancien HUD.
init python:
    DEBAT_DAY3_BASE_VOTE_STATS = {
        "elias": 7, "mara": 1, "lysa": 2, "julian": 9,
        "iris": 4, "tomas": 3, "elen": 8, "kael": -1,
        "nyra": 3, "ryn": -1, "sael": 2,
    }

    def debat_day3_reset_live_stats():
        store.debat_day3_live_vote_stats = dict(DEBAT_DAY3_BASE_VOTE_STATS)

    def debat_day3_apply_influence(delta_map):
        if not getattr(store, "debat_day3_live_vote_stats", None):
            debat_day3_reset_live_stats()
        for person, delta in delta_map.items():
            store.debat_day3_live_vote_stats[person] = store.debat_day3_live_vote_stats.get(person, 0) + delta

    def debat_day3_compute_votes(stats=None):
        source = stats if stats is not None else store.debat_day3_live_vote_stats
        votes = {"pour": 0, "contre": 0, "abstention": 0, "details": {}}
        for person, value in source.items():
            vote = "pour" if value > 1 else ("contre" if value < -1 else "abstention")
            votes[vote] += 1
            votes["details"][person] = vote
        return votes
