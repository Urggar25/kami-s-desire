default seen_voyeur_julian_iris = False
default seen_voyeur_mara_tomas = False
default seen_voyeur_nyra = False
default got_argument_echanges_discrets = False

image bg_cg017_1 = Movie(play="images/background/bg_cg017_1.mp4", loop=True)

label temps_libre_salle_repos:
    if not persistent.pegi18:
        jump REPOS_TP

    scene bg_repos at adaptive_fullscreen with dissolve

    $ seen_voyeur_julian_iris = True

    "La salle de repos est calme, faiblement éclairée par les veilleuses bleues. Des bancs, des distributeurs, un paravent à moitié ouvert dans le coin du fond."
    "J'entends un rire étouffé venant de derrière le paravent. je m'approche sans bruit et regarde ce qu'il se passe."

    scene bg_cg015 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg015")

    iris "Pff… t’es sérieux là ? Ici ?"
    iris "Si quelqu’un entre…"

    julian "Justement, c’est ça qui rend ça excitant."
    julian "Allez, Iris… détends-toi un peu. Personne ne viendra à cette heure."

    iris "T’es vraiment un crâneur…"

    "Julian se penche vers elle, glisse une main sous sa chemise entrouverte. Iris sursaute légèrement, mais ne le repousse pas."
    "Elle râle encore, mais sa voix tremble :"

    iris "Arrête… ou continue, je sais plus…"

    julian "Chut…"

    "Il l’embrasse dans le cou, lentement. Sa main remonte sur sa poitrine, effleure sans déshabiller. Iris ferme les yeux, mord sa lèvre, un petit gémissement lui échappe malgré elle."
    "Elle pose sa main sur celle de Julian pour la guider, mais garde son haut en place – comme si elle voulait garder le contrôle."

    iris "T’es… insupportable…"

    julian "Et toi, t’es adorable quand tu râles."

    "Ils s’embrassent doucement, puis plus profondément. Les mains de Julian descendent sur ses hanches, sous sa jupe, mais sans aller trop loin – juste des caresses légères sur la peau."
    "Iris respire plus fort, ses doigts s’agrippent à la chemise de Julian."

    iris "Si quelqu’un nous voit… je te tue."

    julian "Alors sois plus discrète…"

    "Ils rient tout bas, complices. Julian murmure quelque chose à son oreille qui la fait rougir encore plus."

    "Tu recules lentement dans l’ombre, le cœur battant. Ils ne t’ont pas vu. Tu sors de la salle sans un bruit."

    jump REPOS_TP


label temps_libre_salle_archive:

    if not persistent.pegi18:
        jump ARCHIVE_TP

    $ seen_voyeur_mara_tomas = True

    scene bg_archive at adaptive_fullscreen with dissolve
    "Je pousse la porte de la salle des archives. C’est sombre, poussiéreux, rempli d’étagères métalliques et de vieux terminaux. L’odeur de métal froid et de papier ancien me prend à la gorge."
    "Je m’avance doucement, quand un rire bas et provocateur me parvient du fond, derrière une rangée de casiers. Je m’approche sans bruit, restant dans l’ombre d’une pile de boîtes."

    scene bg_cg016 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg016")

    mara "Attends… t’es sérieux là ?"
    mara "T’as jamais rien fait avec une fille ? Jamais ?"

    tomas "Euh… non… je… j’ai jamais eu l’occasion…"
    tomas "C’est… c’est pas que je voulais pas, hein… c’est juste…"

    mara "Oh mon dieu, c’est trop mignon."
    mara "Le petit intello qui rougit dès qu’on parle de cul."
    mara "Viens là, approche."

    "Je me fige derrière les boîtes. Mara s’adosse à une chaise, croise les bras sous sa poitrine pour la faire remonter légèrement, elle sourit en coin."
    "Tomas avance d’un pas hésitant, rouge jusqu’aux oreilles."

    mara "Allez, touche."
    mara "Je te jure que je mords pas… enfin, pas trop."

    tomas "M-Mara… si quelqu’un arrive…"

    mara "Personne vient ici. Et puis, c’est juste pour te dépuceler un peu les mains."
    mara "Vas-y. Tu peux toucher où tu veux. Doucement."

    "Je retiens mon souffle. Tomas tremble, mais pose une main hésitante sur sa cuisse tandis que l'autre attrape son flanc. Mara rit doucement, prend sa main et la guide lentement plus haut, sous sa jupe, sans jamais la soulever complètement."
    "Elle garde les yeux dans les siens, provocante."

    mara "Tu sens ?"
    mara "C’est pas sorcier. Juste… explore un peu."

    "Tomas respire fort, ses doigts effleurent timidement ses vêtements, puis un peu plus haut. Mara soupire de plaisir, mais garde le contrôle."
    "Elle ne se déshabille pas – juste une main guidée, des caresses légères, un jeu de pouvoir."

    mara "Pas mal pour un débutant…"
    mara "Tu vois ? C’est pas si terrifiant."

    tomas "Je… je sais pas quoi faire…"

    mara "Continue comme ça. T’es pas mal du tout."

    "Elle rit encore, un rire bas et taquin, tandis que Tomas continue timidement, comme hypnotisé."
    "Je recule lentement dans l’ombre, le cœur battant. Ils ne m’ont pas vu. Je sors de la salle sans un bruit."

    $ voyeur_mara_tomas_seen = True  # Flag pour débloquer une référence future ou conséquence optionnelle

    jump ARCHIVE_TP

label temps_libre_salle_dortoir:

    if not persistent.pegi18:
        jump DORTOIR_TP

    $ seen_voyeur_nyra = True

    scene bg_dortoir at adaptive_fullscreen with dissolve
    "Je décide de passer par le dortoir. Les couloirs sont silencieux à cette heure. Seule la lueur bleue des veilleuses éclaire les portes des chambres."
    "Soudain, un bruit étouffé me parvient : un bourdonnement discret, suivi d’un soupir bas et contrôlé."
    "Ça vient de la chambre de Nyra. La porte est légèrement entrouverte, juste une fine fente."
    "Je m’approche sans un bruit, le cœur qui cogne. Je jette un œil prudent par l’interstice."

    scene bg_cg017_1 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg017")

    "Nyra est allongée sur son lit, dos légèrement cambré, jupe relevée jusqu’aux hanches, haut déboutonné jusqu’à la taille."
    "Entre ses cuisses écartées, un petit appareil artisanal – un vibromasseur qu’elle a dû fabriquer elle-même – vibre doucement contre elle."
    "Elle le tient fermement d’une main, l’autre main sur sa poitrine, doigts pinçant un téton à travers le tissu."
    "Ses mouvements sont précis, autoritaires : elle dirige l’objet avec assurance, comme si elle donnait des ordres à son propre corps."
    "Un soupir rauque lui échappe. Elle murmure pour elle-même :"
    
    nyra "Plus fort… oui… comme ça…"

    "Elle accélère légèrement le rythme, les hanches se soulèvent par intermittence, cherchant le point parfait."
    "Sa respiration devient saccadée, mais elle garde un contrôle absolu : pas de gémissements incontrôlés, juste des souffles profonds et maîtrisés."
    "Ses yeux sont mi-clos, concentrés sur son plaisir, comme si elle analysait chaque sensation."

    "Je reste figé derrière la porte, incapable de détourner le regard. Le bourdonnement continue, régulier, hypnotique."
    "Nyra rejette la tête en arrière, un petit spasme la traverse. Elle murmure encore :"
    
    nyra "C’est ça… parfait…"

    "Elle ralentit enfin, retire doucement l’appareil, le pose sur le côté. Son souffle se calme, mais son sourire satisfait reste."
    "Je recule lentement, le cœur battant à tout rompre. Elle ne m’a pas vu. Je m’éloigne sans un bruit, l’image gravée dans ma tête."

    jump DORTOIR_TP


label temps_libre_salle_stockage_argument:

    scene bg_stockage at adaptive_fullscreen
    play sound "audio/sfx_paper.mp3"

    "Au fond de la salle de stockage, deux silhouettes parlent à voix basse entre les caisses."
    "Sael tend un filtre à air. Nyra lui passe une pochette de joints d'étanchéité en échange."

    $ showP("sael", "neutre", 0.30)
    $ showP("nyra", "neutre", 0.76)

    sael "Filtre propre. Deux semaines si tu le ménages."
    nyra "Parfait. Ces joints éviteront une fuite sur la ligne secondaire."

    $ showP("sael", "raison", 0.30)
    sael "Chez nous, je troquais déjà ça contre des repas chauds."
    sael "Quand je retournais en ville. Juste nécessaire."

    $ showP("nyra", "taquin", 0.76)
    nyra "À Orbite, un lot de légumes valait une réparation express."
    nyra "Même logique, mais dans un autre décor."

    sael "On a tous connu plus ou moins la galère."
    nyra "Et on a pas eu le choix de s'adapter."

    "Elles referment les contenants, sobres, efficaces, comme un rituel rodé."

    if not got_argument_echanges_discrets:
        $ got_argument_echanges_discrets = True
        $ add_argument("Échanges discrets déjà actifs")
        show screen argument_unlock("Échanges discrets déjà actifs")

    think "Je me retire avant qu'elles ne me repèrent."

    hide sael
    hide nyra
    jump STOCKAGE_TP
