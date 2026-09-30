# =============================================================================
# JOUR 21 — Route 0_1_1_0_0
# Réponse à Kael : "Je reste s'il y a encore une chance de le sortir."
#
# Les Doppelgängers choisissent de prolonger le Conclave jusqu'au jour 30.
# Aucun vote n'est annoncé au cours de cette journée.

# =============================================================================

label _21_0_1_1_0_0_REVEIL:
    $ cafeteria_food_level = "null"
    $ current_day = 21
    $ day_id = 21
    $ current_period = "Matin"
    $ j20_kael_depart_choice = "stay"
    $ noam_has_juliette_drawing = False
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "Je me réveille avant l'annonce de Kami, avec cette sensation étrange d'avoir oublié quelque chose d'important."
    "Il me faut quelques secondes pour comprendre que, cette fois, ce n'est pas un vote, une dispute ou un bruit derrière la grille qui m'attend."
    think "On rentre."
    "Mon sac est déjà posé contre le bureau. Je l'avais préparé hier soir presque mécaniquement, en remettant deux fois les mêmes affaires dedans avant de comprendre que je les avais déjà rangées."
    "La grille d'aération est toujours là, au-dessus du bureau. Je la regarde malgré moi."
    think "Quelques heures."
    "Après ça, elle pourra bien faire tous les bruits qu'elle veut."
    "Je récupère mon téléphone, vérifie l'heure et me lève."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j21_stay_door_chambre_couloir
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Dans le couloir, presque toutes les portes sont ouvertes. Des sacs traînent devant les chambres, des voix se répondent d'un bout à l'autre du dortoir et, pour une fois, personne ne parle de Kami."
    $ showGroup([
        ("elen", "joie", 0.22),
        ("tomas", "hesitation", 0.50),
        ("lysa", "blase", 0.78),
    ])
    elen joie "J'ai tout pris ! Enfin... normalement."
    tomas hesitation "Tu viens de dire exactement la phrase qu'on dit juste avant de découvrir qu'on a oublié quelque chose."
    elen rire "Mais non ! J'ai vérifié deux fois."
    lysa blase "Donc t'as probablement oublié deux fois la même chose."
    elen "Vous êtes vraiment incapables d'être positifs cinq minutes."
    tomas "Moi je suis positif."
    lysa "T'as recompilé mentalement ta valise trois fois depuis que je suis sortie de ma chambre."
    tomas surpris "Comment tu—"
    lysa "Parce que tu comptes à voix haute."
    "Tomas ferme immédiatement la bouche."
    noam taquin "Bonjour."
    elen joie "Noam ! T'es prêt ?"
    noam "Normalement."
    tomas reflexion "Voilà. Lui aussi."
    lysa blase "Magnifique. Trois adultes et pas une certitude."
    "Elle a son sac sur une épaule, à peine rempli. Le mien paraît énorme à côté."
    noam surpris "C'est tout ce que t'as ?"
    lysa "J'ai pas emménagé ici."
    elen "Moi non plus !"
    lysa "Ton sac a l'air de contenir un cadavre."
    elen surpris "Il contient pas de cadavre."
    lysa blase "Merci Elen. C'était important de le préciser."
    "Je souris malgré moi."
    think "Ça ressemble presque à un départ normal."
    "Presque."
    $ hideGroup()
    # Durée : ~1m40
    # Total : ~1m40

label _21_0_1_1_0_0_SAS:
    $ current_period = "Midi"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "sas_livraison") from _call_j21_stay_door_couloir_sas
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Quand j'arrive au sas, presque tout le monde est déjà là."
    "Et une capsule est déjà amarrée derrière la baie."
    "Pendant une seconde, mon cœur accélère."
    "Puis je vois les marquages sur sa coque."
    think "Livraison."
    "Pas de hublot. Pas de sièges. Juste le conteneur automatique qu'on voit arriver tous les quelques jours."
    $ showGroup([
        ("ryn", "fatigue", 0.18),
        ("mara", "neutre", 0.50),
        ("elias", "neutre", 0.82),
    ])
    ryn fatigue "C'est quoi ça ?"
    elias neutre "Une livraison."
    ryn colere "J'avais vu, merci."
    mara taquin "Peut-être qu'ils nous renvoient sur Terre dans des cartons."
    ryn "Mara..."
    mara "Quoi ? Ça ferait des économies."
    $ hideGroup()
    $ showGroup([
        ("iris", "blase", 0.20),
        ("noam", "reflexion", 0.50),
        ("kael", "calme", 0.80),
    ])
    iris blase "Je prends celui marqué fragile."
    noam "Trop tard. Mara l'a déjà demandé."
    iris "Évidemment."
    kael calme "La navette peut encore arriver."
    noam "Ouais."
    "Personne ne répond vraiment."
    $ hideGroup()
    "Au début, les discussions continuent. Elen parle déjà de son premier repas sur Terre, Julian du message qu'il postera en premier une fois revenu, Tomas vérifie l'heure beaucoup trop souvent."
    "Puis, petit à petit, les conversations s'arrêtent."
    pause 0.6
    "La capsule de livraison reste seule derrière la vitre."
    "Aucun autre voyant d'approche ne s'allume."
    $ showGroup([
        ("tomas", "inquiet", 0.20),
        ("julian", "inquiet", 0.50),
        ("lysa", "blase", 0.80),
    ])
    tomas inquiet "Elle a... combien de retard, là ?"
    julian "Douze minutes."
    tomas "T'as compté aussi ?"
    julian "J'ai une montre."
    lysa blase "Vous avez vraiment attendu la douzième minute pour commencer à vous inquiéter ?"
    tomas inquiet "Toi, ça t'inquiète pas ?"
    lysa "Si."
    julian "Tu n'en as pas l'air."
    lysa fatigue "J'avais juste pas misé grand-chose sur un départ propre."
    tomas "Pourquoi ?"
    lysa blase "Parce qu'on est ici."
    julian inquiet "Argument imparable."
    "Lysa hausse les épaules."
    $ hideGroup()
    ryn "KAMI !"
    "La voix de Ryn claque dans le sas."
    $ showGroup([
        ("ryn", "colere", 0.20),
        ("nyra", "raison", 0.50),
        ("sael", "fatigue", 0.80),
    ])
    ryn colere "Elle est où, la navette ?!"
    nyra raison "Elle t'entend."
    ryn "Alors qu'elle réponde !"
    sael fatigue "Crier ne la fera pas arriver plus vite."
    ryn colere "Merci Sael. T'as d'autres trucs utiles comme ça ?"
    sael colere "Non. J'attends juste comme toi."
    "Ryn ouvre la bouche pour répondre."
    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5
    scene bg_diffusion_amour at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Oooh... vous êtes tous là."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Les sacs, les petites mines impatientes, les regards vers le sas toutes les trente secondes..."
    kami "C'est adorable."
    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "Vous étiez vraiment prêts à me quitter."
    pause 0.4
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Eh bien j'ai une excellente nouvelle !"
    kami "Vous n'aurez finalement pas besoin de vous dire au revoir tout de suite."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Parce que la navette de retour ne viendra pas aujourd'hui."
    pause 0.6
    hide screen kami_broadcast_ui
    scene sas1 at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "colere", 0.16),
        ("iris", "colere", 0.50),
        ("noam", "colere", 0.84),
    ])
    ryn colere "QUOI ?!"
    iris colere "Non. Non, tu vas pas nous faire ce coup-là maintenant."
    noam colere "Pourquoi elle vient pas ?"
    $ hideGroup()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    kami "Pourquoi ?"
    kami "Parce que le Conclave a toujours été prévu pour durer trente jours."
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Le départ du jour vingt-et-un était une possibilité."
    kami "Une petite faveur, si vous voulez."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Une faveur qui supposait évidemment que vous ayez terminé vos merveilleux travaux."
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Or certains de vos chers collègues m'ont fait savoir qu'ils souhaitaient continuer."
    pause 0.4
    kami "Continuer à débattre."
    kami "Continuer à voter."
    kami "Continuer à améliorer le monde."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "C'est beau, cette soudaine conscience civique."
    hide screen kami_broadcast_ui
    scene sas1 at adaptive_fullscreen with dissolve
    $ showGroup([
        ("mara", "colere", 0.16),
        ("nyra", "determine", 0.50),
        ("tomas", "inquiet", 0.84),
    ])
    mara colere "Quels collègues ?"
    nyra determine "Combien de personnes ?"
    tomas inquiet "Et depuis quand quelques représentants peuvent annuler le départ de tout le monde ?"
    $ hideGroup()
    $ showGroup([
        ("ryn", "colere", 0.24),
        ("noam", "colere", 0.50),
        ("julian", "inquiet", 0.76),
    ])
    ryn colere "Donne les noms."
    noam colere "On était censés partir ensemble."
    julian inquiet "Kami, on avait organisé le départ. Tout le monde était prêt."
    $ hideGroup()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    kami "Oui, Noam."
    kami "Ensemble."
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Et regardez comme je respecte parfaitement votre souhait."
    kami "Personne ne part seul."
    pause 0.5
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Quant aux noms..."
    kami "Non."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je pourrais vous les donner, bien sûr."
    kami "Mais vous avez encore neuf jours à passer ensemble."
    kami "Ce serait dommage de gâcher si vite l'ambiance."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le Conclave se poursuivra donc jusqu'au jour trente, comme prévu à l'origine."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Et puisque vous êtes déjà au sas, votre livraison vous attend."
    kami "Je vous laisse ranger tout ça. Considérez-le comme un petit cadeau de consolation."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Allez, courage."
    kami "Neuf jours, ça passe très vite."
    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    pause 0.4
    "Pendant deux secondes, personne ne parle."
    $ showGroup([
        ("ryn", "colere", 0.18),
        ("mara", "colere", 0.50),
        ("tomas", "inquiet", 0.82),
    ])
    ryn colere "C'est qui ?"
    mara "Ah, ça commence."
    ryn "Non, sérieux. C'est qui ?"
    tomas inquiet "Ryn, personne va répondre si—"
    ryn colere "J'ai pas demandé une analyse."
    mara taquin "Moi je propose qu'on se mette tous en cercle et qu'on se regarde très fort."
    ryn "Tu trouves ça drôle ?"
    mara colere "Non. Justement."
    $ hideGroup()
    $ showGroup([
        ("nyra", "raison", 0.20),
        ("ryn", "colere", 0.50),
        ("lysa", "blase", 0.80),
    ])
    nyra raison "Personne n'accuse personne sans élément."
    ryn "Quelqu'un vient de nous rajouter neuf jours ici !"
    nyra "Je sais."
    ryn "Alors arrête de parler comme si—"
    lysa blase "Vous comptez faire ça combien de temps ?"
    ryn "Quoi ?"
    lysa "Hurler 'c'est qui ?' jusqu'à ce que quelqu'un se transforme spontanément en panneau lumineux."
    ryn colere "Ça te fait rien, toi ?"
    lysa "Si."
    ryn "On dirait pas."
    lysa fatigue "Je suis pas surprise. C'est différent."
    ryn "Pourquoi ?"
    lysa blase "Parce qu'on est enfermés depuis vingt jours dans une station gérée par Kami. Le miracle, ça aurait été de partir à l'heure."
    nyra raison "Elle n'a pas tort."
    ryn "Super."
    "Il tourne les talons."
    $ hideGroup()
    $ showGroup([
        ("lysa", "blase", 0.30),
        ("noam", "fatigue", 0.70),
    ])
    noam inquiet "T'es vraiment déjà passée à autre chose ?"
    lysa "Non."
    noam "On dirait."
    lysa blase "Je suis juste pas assez motivée pour crier sur un écran."
    "Elle pose son sac contre la paroi et désigne les caisses."
    lysa "Et tant qu'à rester neuf jours de plus, autant éviter de vivre au milieu des cartons."
    noam fatigue "Je vais t'aider."
    lysa "Je savais que t'avais un vice caché."
    $ hideGroup()
    # Durée : ~4m30
    # Total : ~6m10

label _21_0_1_1_0_0_LIVRAISON:
    $ current_period = "Après-midi"
    scene bg_stockage at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Une demi-heure plus tard, le sas s'est vidé de la moitié des représentants."
    "Certains sont partis se calmer. D'autres ont ramené leurs sacs dans les dortoirs sans les défaire."
    "Moi, je fais des allers-retours entre le sas et le stockage avec Lysa."
    $ showGroup([
        ("lysa", "blase", 0.22),
        ("noam", "fatigue", 0.50),
        ("elias", "neutre", 0.78),
    ])
    lysa blase "Pose ça là."
    noam "C'est marqué maintenance."
    lysa "Je sais lire."
    noam "Alors pourquoi là ?"
    lysa "Parce que si tu le poses devant la porte, Elias va se prendre les pieds dedans."
    elias neutre "Merci."
    lysa "Tu vois ? Il confirme."
    elias "Je confirme surtout que j'ai déjà assez de bordel."
    "Elias est assis au milieu de plusieurs caisses ouvertes, un terminal de stock posé sur un genou."
    "Depuis quelques minutes, il ne range presque plus rien. Il cherche."
    noam reflexion "Tu trouves pas quoi ?"
    elias "Attends."
    "Il ouvre une caisse, pousse des câbles, referme, puis attrape la suivante."
    lysa blase "Ça fait trois fois que tu ouvres celle-là."
    elias fatigue "Je sais."
    lysa "Je précise au cas où t'aurais développé une passion."
    elias "Lysa."
    lysa "Je me tais."
    "Elle ne se tait pas vraiment, mais elle prend une caisse et s'éloigne de deux mètres."
    noam "Elias ?"
    elias ecoute "Les plaques."
    noam reflexion "Quelles plaques ?"
    elias "Celles que j'ai utilisées hier pour les chambres."
    noam "Les plaques métalliques ?"
    elias "Ouais."
    "Il se relève et passe une main dans ses cheveux."
    elias fatigue "J'en ai utilisé six."
    lysa "Et elles se reproduisent normalement la nuit ?"
    elias colere "Le stock les remplace."
    lysa blase "C'était presque pareil."
    "Elias l'ignore."
    elias ecoute "Tout ce qu'on utilise ici revient dans la livraison suivante. Les pièces, les consommables, le matos de maintenance... tout."
    noam reflexion "Automatiquement ?"
    elias "Ouais. C'est pour ça qu'on commande rien nous-mêmes."
    noam "Et elles devaient être là."
    elias fatigue "Elles doivent être là."
    lysa "Mais elles sont pas là."
    elias "Merci."
    lysa "Je résume."
    elias "Résume moins."
    "Il fait défiler l'inventaire du doigt, de plus en plus vite."
    noam "Ça peut être une erreur."
    elias "Nan."
    noam "Pourquoi nan ?"
    elias "Parce que les vis sont revenues."
    "Il me montre une petite boîte encore fermée."
    elias "Les forets aussi. Les fixations, pareil. Même le câble que j'ai utilisé l'autre jour est revenu."
    noam reflexion "Donc le système a bien compté ce que t'as utilisé."
    elias "Voilà."
    "Il pose brutalement le terminal sur une caisse."
    elias colere "Alors elles sont où, mes plaques ?"
    lysa "Peut-être dans une autre caisse."
    elias "J'ai regardé."
    lysa blase "Trois fois, oui."
    "Elias lui lance un regard noir."
    lysa "Pardon."
    noam "On peut vérifier le bordereau complet ?"
    elias fatigue "Tomas saura mieux faire."
    noam "Je vais le chercher."
    elias "Laisse. Il est encore au sas avec les listes."
    "Il se relève aussitôt."
    elias colere "Je vais lui demander."
    lysa blase "Et nous ?"
    elias "Vous rangez."
    lysa "Chef, oui chef."
    "Elias part sans répondre."
    pause 0.3
    noam reflexion "Ça l'énerve vraiment."
    lysa "Quelqu'un a touché à son matos."
    noam "Tu crois ?"
    lysa blase "J'en sais rien. Je dis juste qu'Elias aime pas quand son compte tombe faux."
    noam "Tu t'es vraiment déjà faite à l'idée qu'on reste ?"
    "Elle s'arrête avec un carton entre les mains."
    lysa fatigue "Non."
    noam "Pourtant t'avais l'air de t'y attendre."
    lysa "Je m'attendais surtout à ce qu'on nous fasse une dernière crasse."
    noam inquiet "Ça te met pas en colère ?"
    lysa blase "Si. Mais si je commence à casser des caisses, Elias va encore plus râler."
    "Elle me tend le carton."
    lysa "Médical."
    noam "Tu pourrais au moins faire semblant d'être bouleversée."
    lysa "Je peux aussi finir de ranger avant le dîner."
    noam "Très émouvant."
    lysa blase "Merci."
    "Elle repart vers la porte."
    think "Elle n'est pas surprise."
    think "Pas parce qu'elle savait."
    think "Juste parce qu'elle ne croyait pas vraiment qu'on nous laisserait partir sans problème."
    $ hideGroup()
    # Durée : ~2m30
    # Total : ~8m40

label _21_0_1_1_0_0_MANIFESTE:
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    "Quand je reviens au sas avec une caisse vide, Elias et Tomas sont penchés sur le terminal logistique."
    $ showGroup([
        ("elias", "colere", 0.22),
        ("tomas", "inquiet", 0.50),
        ("noam", "reflexion", 0.78),
    ])
    elias colere "Là. Regarde."
    tomas hesitation "Je regarde."
    elias "Non, tu fais défiler."
    tomas colere "Parce qu'il y a cent quarante-deux lignes, Elias !"
    elias "Cherche métal."
    tomas "Je suis en train de—"
    elias "Voilà !"
    tomas colere "Je l'avais vu !"
    "Tomas recule le terminal contre lui comme si Elias risquait de le lui arracher."
    noam "Vous avez trouvé ?"
    tomas inquiet "Oui. Enfin... oui."
    elias colere "C'est marqué."
    tomas "Oui, c'est marqué."
    noam reflexion "Quoi ?"
    "Tomas me montre l'écran."
    tomas raison "Six plaques de renfort en alliage structurel. Même référence que celles sorties de la maintenance hier."
    noam "Donc elles ont bien été réapprovisionnées."
    tomas "Oui."
    elias "Et livrées."
    tomas hesitation "Le statut indique 'transféré au Conclave'."
    noam inquiet "Ça veut dire quoi exactement ?"
    tomas reflexion "Que le système logistique considère que la capsule les a déposées ici."
    elias "Donc elles étaient dans la livraison."
    tomas "Normalement."
    elias colere "Arrête avec 'normalement'."
    tomas surpris "Bah je vais pas inventer une certitude !"
    elias "Le stock les compte. La livraison les compte. Elles sont pas là."
    tomas inquiet "Je sais."
    elias "Alors elles sont passées où ?"
    pause 0.5
    noam reflexion "Elles auraient pu être déplacées automatiquement ?"
    tomas "C'est ce que je vérifie."
    elias fatigue "Y'a pas de transfert."
    tomas "Laisse-moi vérifier quand même."
    elias "Tu viens de le faire."
    tomas colere "ELIAS."
    "Elias se tait enfin."
    "Tomas remonte plusieurs lignes, ouvre un second écran, puis un troisième."
    tomas reflexion "Pas de transfert interne enregistré."
    noam "Donc..."
    tomas inquiet "Donc le système dit qu'elles sont arrivées et qu'elles n'ont pas été déplacées."
    elias "Voilà."
    noam reflexion "Mais elles sont pas là."
    elias colere "Voilà."
    "Il répète le mot beaucoup plus fort."
    tomas hesitation "Ça peut encore être un problème d'inventaire."
    elias "Tu viens de dire que—"
    tomas "Un problème d'inventaire, pas forcément un problème de livraison ! Un mauvais scan, un doublon, une caisse mal—"
    elias colere "Tout le reste est là !"
    "Tomas s'arrête."
    elias "Les vis. Les fixations. Les câbles. Les pièces que j'ai utilisées. Même les putains de forets."
    noam inquiet "Sauf les plaques."
    elias fatigue "Sauf les plaques."
    "Il donne un coup du plat de la main contre la caisse."
    elias "Et maintenant je peux pas finir."
    noam "Finir quoi ?"
    elias "Les chambres."
    "Je mets une seconde à comprendre."
    elias ecoute "J'en avais fermé six hier. Il m'en restait six aujourd'hui."
    noam reflexion "Ah."
    elias "Voilà."
    "Je regarde machinalement la caisse ouverte à côté de lui. Elle contient exactement ce qu'elle est censée contenir."
    "Je ne pense pas aux conduits. Pas vraiment. Pour l'instant, je vois surtout Elias qui vient de perdre du matériel que le système affirme lui avoir rendu."
    noam "Tu peux utiliser autre chose ?"
    elias fatigue "Ouais."
    tomas surpris "Ah ?"
    elias "J'ai dit que je peux. Pas que ça va être propre."
    tomas "Tu comptes faire quoi ?"
    elias "Trouver du métal."
    noam "Où ?"
    elias "Partout."
    tomas inquiet "Tu vas pas démonter des éléments structurels au hasard."
    elias "J'ai l'air con à ce point ?"
    tomas "J'ai pas dit—"
    elias colere "Je vais prendre des caches, des vieux panneaux, des trucs qui servent à rien."
    noam taquin "Donc tu vas démonter le Conclave."
    elias fatigue "Un peu."
    "Pour la première fois depuis dix minutes, Tomas laisse échapper un rire."
    tomas "Ça, par contre, j'ai envie de voir."
    elias "Toi tu viens avec moi."
    tomas surpris "Pourquoi moi ?"
    elias "Parce que si j'enlève un truc important, tu vas me faire chier avant que je le fasse."
    tomas hesitation "C'est... étonnamment logique."
    elias "Et Noam."
    noam "Hm ?"
    elias "Tu m'aides à porter."
    noam fatigue "Évidemment."
    $ hideGroup()
    # Durée : ~2m20
    # Total : ~11m00

label _21_0_1_1_0_0_RECUPERATION:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "L'après-midi se transforme en chasse au métal."
    "Pas aux plaques disparues. Elias a manifestement décidé qu'il les retrouverait plus tard."
    "Pour l'instant, il veut surtout finir ce qu'il avait commencé."
    $ showGroup([
        ("elias", "ecoute", 0.20),
        ("tomas", "reflexion", 0.50),
        ("noam", "fatigue", 0.80),
    ])
    elias ecoute "Ça."
    tomas surpris "Non."
    elias "Pourquoi ?"
    tomas "Parce que c'est le cache d'un répartiteur électrique."
    elias "Il est éteint."
    tomas "Aujourd'hui."
    elias fatigue "Fait chier."
    "Elias passe au panneau suivant."
    elias "Ça."
    tomas "Oui."
    elias surpris "Sérieux ?"
    tomas "C'est une plaque de protection d'un ancien support de stockage. Le support n'existe plus."
    elias "Enfin."
    "Il attrape son tournevis."
    noam "Attends, tu vas vraiment tout démonter ?"
    elias "Pas tout."
    noam "Ça me rassure énormément."
    elias "Tiens ça."
    "Je maintiens la plaque pendant qu'il retire les fixations."
    tomas reflexion "Tu sais que ça sera plus fin que les autres."
    elias "Je doublerai."
    tomas "Et les attaches ne sont pas au même entraxe."
    elias "Je reperce."
    tomas "Et—"
    elias colere "Tomas."
    tomas hesitation "Oui ?"
    elias "Si t'as une solution meilleure, je prends."
    "Tomas ouvre la bouche, réfléchit, puis la referme."
    tomas "Non."
    elias "Alors laisse-moi bricoler."
    tomas "Je te laisse bricoler. J'essaie juste d'éviter que tu transformes une chambre en court-circuit."
    elias "C'est gentil."
    "La plaque se décroche enfin."
    elias satisfait "Voilà."
    noam "Une."
    elias fatigue "Il m'en faut au moins dix comme ça."
    noam "Tu viens de dire qu'il t'en restait six."
    elias "Parce que celle-là est fine. Je double."
    noam "Ah."
    tomas "Je t'avais prévenu."
    elias "Toi, ça va."
    "Tomas sourit malgré lui."
    $ hideGroup()
    scene bg_stockage at adaptive_fullscreen with dissolve
    "On passe ensuite par le stockage, puis par une réserve de maintenance que je n'avais jamais vraiment regardée."
    "Elias récupère des panneaux, des chutes de tôle et deux morceaux d'un ancien châssis. À chaque fois, Tomas vérifie qu'il ne démonte rien d'utile."
    $ showGroup([
        ("lysa", "blase", 0.24),
        ("elias", "fatigue", 0.50),
        ("noam", "fatigue", 0.76),
    ])
    "Lysa nous retrouve alors que nous traversons le stockage avec une plaque presque aussi grande qu'elle."
    lysa blase "Je retire ce que j'ai dit."
    noam "Sur quoi ?"
    lysa "Les cartons, c'était mieux."
    elias fatigue "Pousse-toi."
    lysa "Charmant."
    "Elle se décale juste assez pour nous laisser passer."
    lysa reflexion "Vous avez retrouvé les plaques ?"
    elias "Nan."
    lysa "Donc ça, c'est quoi ?"
    elias "Plan B."
    lysa blase "Ça ressemble à une porte."
    elias "C'était pas une porte."
    noam fatigue "On sait pas vraiment ce que c'était."
    lysa "Encore mieux."
    elias colere "Ça servait à rien."
    lysa "Tomas a validé ?"
    noam "À contrecœur."
    lysa blase "Alors j'ai toute confiance."
    "Elle attrape le bord de la plaque."
    lysa "Allez, donne."
    elias surpris "Tu fais quoi ?"
    lysa "Je vous aide."
    elias "T'étais pas en train de ranger ?"
    lysa "J'ai fini."
    noam "Toute seule ?"
    lysa "Non. J'ai dressé Elen."
    noam taquin "Impressionnant."
    lysa "Elle travaille très bien avec des récompenses alimentaires."
    "On reprend à trois."
    "Pendant quelques minutes, le problème des plaques devient presque une corvée normale. On râle sur le poids, sur les angles, sur Elias qui change d'avis toutes les trente secondes."
    elias "Plus à gauche."
    lysa colere "Y'a plus de gauche, mon bras est contre le mur."
    elias "Alors tourne."
    lysa "Avec quoi ? Mes hanches sont coincées."
    noam "Je peux reculer."
    elias "Non, si tu recules ça penche."
    lysa blase "Excellent. On va mourir écrasés par un bout de métal inutile."
    elias "Il est pas inutile."
    lysa "Il l'était il y a dix minutes."
    "Même Elias finit par sourire."
    $ hideGroup()
    # Durée : ~2m30
    # Total : ~13m30

label _21_0_1_1_0_0_DORTOIRS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "En fin d'après-midi, Elias reprend son travail dans les dortoirs."
    "Je l'aide à tenir les plaques improvisées pendant qu'il perce. Tomas reste à côté avec les fixations et un air de contrôleur technique."
    $ showGroup([
        ("elias", "fatigue", 0.18),
        ("tomas", "reflexion", 0.50),
        ("noam", "fatigue", 0.82),
    ])
    elias fatigue "Tiens droit."
    noam "Je tiens droit."
    elias "Non."
    noam "Elias..."
    elias colere "Tu tiens droit par rapport au mur ou par rapport à toi ?"
    noam "Au mur."
    tomas "Pas tout à fait."
    noam colere "Merci Tomas."
    tomas hesitation "Pardon."
    elias "Un peu à droite."
    noam "Comme ça ?"
    elias "Voilà."
    "La perceuse démarre."
    play sound sfx_drill if renpy.has_label("sfx_drill") else None
    "Le métal vibre contre mes paumes."
    "Quand Elias coupe enfin l'outil, il vérifie les attaches une par une."
    elias ecoute "Ça tiendra."
    tomas reflexion "Moins bien que les vraies plaques."
    elias "Oui."
    tomas "Mais ça tiendra."
    elias "Voilà."
    noam "Il t'en reste combien ?"
    elias fatigue "Trop."
    noam "Réponse précise."
    elias "Quatre chambres si je trouve encore de quoi doubler."
    tomas inquiet "Et si tu trouves pas ?"
    elias "Je trouverai."
    "Il répond tellement vite que Tomas n'insiste pas."
    noam reflexion "Tu veux vraiment finir aujourd'hui ?"
    elias "Ouais."
    noam "Pourquoi ?"
    elias colere "Parce que j'ai commencé."
    "Il ramasse sa perceuse."
    elias fatigue "Et parce que j'aime pas qu'un truc disparaisse pile quand j'en ai besoin."
    noam "Ça te travaille."
    elias "Évidemment que ça me travaille."
    "Il se tourne vers moi."
    elias ecoute "Je sais ce que j'ai pris. Je sais ce qui devait revenir. Si je commence à accepter que six plaques se volatilisent juste parce que 'bah peut-être', autant arrêter de tenir un stock."
    tomas reflexion "Je peux revérifier les logs ce soir."
    elias "Tu vas trouver la même chose."
    tomas "Probablement."
    elias "Alors dors."
    tomas surpris "C'est toi qui me dis ça ?"
    elias "Ouais."
    tomas "Tu comptes dormir, toi ?"
    "Elias regarde la plaque suivante."
    elias "On verra."
    $ hideGroup()
    # Durée : ~1m40
    # Total : ~15m10

label _21_0_1_1_0_0_SOIR:
    $ current_period = "Nuit"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Le soir, la cafétéria est plus silencieuse que d'habitude."
    "Les sacs ont disparu du sas. Ils sont retournés dans les chambres, souvent sans être défaits."
    "Je m'assois avec Lysa et Tomas. Elias n'est pas là ; une perceuse résonne encore de temps en temps dans les dortoirs."
    $ showGroup([
        ("lysa", "fatigue", 0.20),
        ("tomas", "hesitation", 0.50),
        ("noam", "fatigue", 0.80),
    ])
    tomas hesitation "À cette heure-ci..."
    lysa "Non."
    tomas surpris "J'ai encore rien dit."
    lysa blase "Je sais exactement ce que t'allais dire."
    noam "Moi pas."
    lysa "Il allait nous rappeler qu'on devrait déjà être dans la navette."
    "Tomas baisse les yeux."
    tomas "Oui."
    noam fatigue "Merci."
    tomas inquiet "Désolé."
    lysa "Tu vois ? Même lui regrette déjà."
    "Je laisse échapper un rire bref."
    tomas reflexion "Je comprends toujours pas pourquoi quelqu'un voudrait continuer."
    lysa fatigue "Parce que quelqu'un veut continuer."
    tomas "Oui mais pourquoi ?"
    lysa "Aucune idée."
    tomas "Ça te travaille pas ?"
    lysa blase "Si. Mais je peux rien en faire."
    noam reflexion "Pour une fois, t'as pas une théorie catastrophique ?"
    lysa "J'en ai douze."
    noam "Et ?"
    lysa "Elles sont toutes probablement fausses."
    "Elle boit une gorgée."
    lysa fatigue "Donc je vais éviter de choisir celle qui me plaît le plus juste pour avoir quelque chose à raconter."
    tomas "C'est étonnamment raisonnable."
    lysa blase "Merci. Ça me dégoûte."
    noam "Et les plaques ?"
    tomas reflexion "Je revérifierai demain."
    lysa "Pourquoi ?"
    tomas "Parce que ça m'énerve aussi."
    lysa blase "Ah. Voilà une meilleure raison."
    tomas "Le système dit qu'elles sont là. Elles sont pas là. C'est..."
    noam "Pas normal."
    tomas "Voilà."
    "Une perceuse démarre au loin."
    pause 0.4
    lysa "Et Elias va probablement démonter la station entière avant d'accepter ça."
    noam "Il a déjà commencé."
    tomas "Techniquement, tout ce qu'il a démonté aujourd'hui était inutilisé."
    lysa blase "Tu vas vraiment défendre ça devant Kami quand il aura arraché un mur porteur ?"
    tomas surpris "Il arrachera pas un mur porteur !"
    lysa "J'espère."
    "La perceuse s'arrête."
    pause 0.5
    noam fatigue "On devait rentrer aujourd'hui."
    "Cette fois, personne ne plaisante."
    tomas inquiet "Ouais."
    lysa fatigue "Ouais."
    "Je regarde ma tasse."
    noam "Neuf jours."
    lysa "On en a déjà fait vingt."
    noam "C'est censé me rassurer ?"
    lysa blase "Non. C'est juste des maths."
    tomas "Des maths plutôt déprimantes."
    lysa "C'est les meilleures."
    "On reste encore quelques minutes à parler de rien. Pas du vote, pas de qui a demandé à rester, pas de la navette."
    "Juste de trucs suffisamment petits pour ne pas donner envie de cogner dans un mur."
    $ hideGroup()
    # Durée : ~1m50
    # Total : ~17m00

label _21_0_1_1_0_0_FIN_JOURNEE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 0.8
    "Quand je retourne vers ma chambre, Elias est toujours là."
    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "fatigue", 0.65),
    ])
    "Il est assis par terre devant une plaque fraîchement fixée, la perceuse posée entre ses jambes."
    noam "Tu comptes t'arrêter ?"
    elias fatigue "Ouais."
    noam "Quand ?"
    elias "Bientôt."
    noam "C'est pas une heure."
    elias "Merci Tomas."
    noam taquin "Je prends ça comme un compliment."
    "Il souffle du nez."
    elias ecoute "J'en ai fait deux de plus."
    noam "Avec les plaques de fortune ?"
    elias "Ouais. C'est moche."
    noam "Ça te ressemble."
    elias colere "Va te coucher."
    noam "D'accord."
    "Je fais deux pas avant de me retourner."
    noam reflexion "Elias."
    elias "Quoi ?"
    noam "Si les vraies plaques réapparaissent demain..."
    elias fatigue "Je vais être très content."
    noam "Et si elles réapparaissent pas ?"
    "Il regarde le morceau de métal devant lui."
    elias "Je continuerai sans."
    noam "Ça te suffit ?"
    elias ecoute "Non."
    pause 0.3
    elias fatigue "Mais c'est mieux que de rester planté à attendre qu'on me rende ce qu'on m'a pris."
    "Je hoche la tête."
    noam "Bonne nuit."
    elias "Ouais."
    "Je rentre dans ma chambre."
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "Mon sac est toujours contre le bureau."
    "Je pourrais le défaire."
    "Je ne le fais pas."
    "Ce matin, je pensais ne passer que quelques heures de plus dans cette pièce. Maintenant il me reste neuf jours."
    "Je m'allonge sans me changer complètement."
    think "Certains veulent continuer les votes."
    "Je ne sais pas qui."
    think "Six plaques de métal ont disparu."
    "Je ne sais pas pourquoi."
    "Pour l'instant, ce sont juste deux problèmes différents dans une journée qui en avait déjà assez."
    "Je ferme les yeux."
    "Au loin, la perceuse d'Elias reprend une dernière fois."
    pause 0.8
    "Puis elle s'arrête."
    stop music fadeout 1.5
    call end_day("22") from _call_j21_stay_end_day_22
    return
    # Durée : ~1m20
    # Total : ~18m20
