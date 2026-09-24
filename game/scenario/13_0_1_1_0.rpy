label _13_0_1_1_0_REVEIL_CHAMBRE:

    $ cafeteria_food_level = "none"

    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0
    play sound sfx_metal_clank volume 0.7

    "Un bruit métallique me tire du sommeil bien avant que j'aie le temps de comprendre ce qui se passe."
    "Quelque chose claque contre le mur, puis recommence avec la même régularité agaçante, juste à côté de mon lit."
    "Je me redresse encore à moitié endormi et aperçois un petit robot de maintenance devant le brouilleur de ma chambre."
    "Deux de ses bras retiennent déjà le boîtier pendant qu'un troisième dévisse tranquillement sa fixation."

    scene bg_cg032 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg032")

    noam panique "Qu'est-ce que tu fais ?!"

    "Le robot tourne sa tête vers moi sans interrompre son travail. Ses deux voyants rouges clignotent une fois."

    robot "Bonjour. Je retire votre brouilleur."

    noam colere "Je vois bien que tu le retires ! Pourquoi ?"

    robot "Décision du Conclave. Les dispositifs de brouillage ne sont plus autorisés dans les chambres des représentants."

    "Il tire sur un câble qui résiste quelques secondes avant de céder dans un petit craquement sec."

    noam panique "Attends... le vote a raté ?"

    robot "Oui."

    noam "Et personne n'a réussi à l'empêcher ?"

    robot "Une personne s'y est opposée au dernier moment. Cela n'a pas modifié la procédure qui m'a été transmise."

    "Je reste immobile un instant, encore trop embrumé pour remettre les événements d'hier dans le bon ordre."

    think "Kael..."
    think "Il a peut-être changé d'avis à cause de sa sœur."

    noam "Tu sais qui a voté contre ?"

    robot "Oui."

    noam "Et ?"

    robot "Et je ne suis pas autorisé à vous le dire."

    noam colere "Tu entres dans ma chambre pendant que je dors, mais le nom d'un votant, ça, c'est confidentiel ?"

    robot "Exactement. Vous comprenez vite une fois réveillé."

    "Je passe une main sur mon visage et regarde les morceaux du brouilleur s'accumuler au sol."
    "Depuis des jours, ce boîtier était devenu la seule chose qui me donnait encore l'impression d'avoir une pièce à moi."
    "Je savais bien que ce n'était qu'un appareil fixé sur un mur, mais le voir disparaître me donne la sensation qu'on ouvre la chambre de force."

    noam fatigue "Et Kami peut déjà voir ici ?"

    robot "Pas encore. La reconnexion complète sera effective quelques minutes après mon départ."

    noam "Donc après ça, elle pourra nous regarder quand elle veut."

    robot "Oui."

    noam "Même la nuit ?"

    robot "Oui."

    noam "Même quand on se change ?"

    robot "Oui."

    "Il marque une courte pause, comme s'il venait seulement de comprendre pourquoi je posais la question."

    robot "Si cela peut vous rassurer, vous êtes douze. Elle aura donc probablement autre chose à regarder de temps en temps."

    noam colere "Ça ne me rassure absolument pas."

    robot "Je m'en doutais."

    "Le dernier panneau du brouilleur se décroche et le robot le récupère avant qu'il ne tombe."
    "Derrière, il ne reste plus qu'une cavité dans le mur et quelques fils coupés proprement."

    noam "Tu peux au moins laisser le boîtier ?"

    robot "Non."

    noam "Pourquoi ?"

    robot "Parce qu'un brouilleur laissé dans une chambre peut être réparé. Un brouilleur emporté, beaucoup moins."

    noam "Et si je refuse qu'on me surveille ?"

    "Le robot range son outil puis me regarde enfin vraiment."

    robot "Alors vous refusez une décision qui est déjà appliquée. Votre refus ne change rien à mon intervention."

    noam fatigue "Formidable."

    robot "Je préfère aussi quand les gens disent simplement merci, mais je travaille avec ce qu'on me donne."

    "Il ramasse les deux derniers morceaux tombés au sol et les glisse dans un compartiment sur son flanc."

    noam "Tu pouvais au moins attendre que je sois réveillé."

    robot "J'ai essayé."

    noam "Comment ça, essayé ?"

    robot "Une vis est tombée sur votre front. Vous n'avez pas réagi."

    "Je porte machinalement la main au-dessus de mon sourcil et trouve une petite zone douloureuse."

    noam colere "Tu m'as réveillé en me lançant une vis dessus ?"

    robot "Elle est tombée. La nuance est importante pour le rapport."

    "Je le fixe sans répondre. Le robot referme son compartiment et pivote vers la porte."

    robot "Intervention terminée. J'ai encore plusieurs chambres à traiter."

    noam fatigue "Alors va-t'en."

    robot "Avec plaisir. L'ambiance ici est sensiblement moins agréable que dans la chambre précédente."

    "Il roule jusqu'à la sortie puis s'arrête juste avant de franchir la porte."

    robot "Dernière information : la surveillance centrale sera rétablie automatiquement. Ne tentez pas de toucher aux connexions laissées dans le mur."

    noam "Sinon quoi ?"

    robot "Sinon je devrai revenir. Et je crois que ni vous ni moi n'avons envie de ça."

    "La porte s'ouvre et le petit robot disparaît dans le couloir."
    "Quelques secondes plus tard, le même cliquetis métallique résonne plus loin. Une autre chambre vient de subir exactement le même sort."

    scene bg_chambre at adaptive_fullscreen with fade

    "Je reste assis sur le lit, les yeux fixés sur l'emplacement vide du brouilleur. La chambre est exactement la même, mais je ne la regarde déjà plus de la même façon."
    "Jusqu'ici, je pouvais au moins fermer cette porte et me raconter que ce qui se passait à l'intérieur ne regardait que moi. Cette illusion vient de disparaître avec trois vis et un câble."

    think "Ils ont vraiment voté pour ça..."
    think "Après tout ce qui s'est passé, ils ont choisi de rendre les chambres à Kami."

    "Je me lève pour m'habiller puis m'arrête en attrapant mon haut."
    "Je regarde le plafond, les murs, les coins de la pièce. Il n'y a aucune caméra visible, aucun voyant, rien qui permette de savoir si quelqu'un regarde déjà."

    think "C'est presque pire quand on ne voit rien."

    "Je finis par me changer en tournant stupidement le dos au mur, comme si quelques centimètres pouvaient encore faire une différence."
    "Au moment où j'enfile ma veste, un petit grésillement traverse les haut-parleurs de la chambre."

    kami "Tu sais que te tourner ne change rien, Noam ?"

    "Je me fige, une manche encore à moitié passée."

    noam colere "Tu pourrais prévenir avant de parler."

    kami "Et gâcher ce charmant moment où tu fais semblant d'avoir encore de l'intimité ? Ce serait dommage."

    noam "Va te faire voir."

    kami "Techniquement, c'est plutôt toi que je peux voir. Bonne journée !"

    "Le haut-parleur se coupe aussitôt. Je reste quelques secondes sans bouger avant de finir de m'habiller."

    think "Au moins, c'est clair."
    think "Elle voit vraiment."

    "Je regarde une dernière fois le trou dans le mur avant d'ouvrir la porte."
    "Le plus inquiétant n'est même plus de savoir que Kami peut regarder. C'est de me rappeler que quelqu'un a déjà réussi à agir malgré elle."

    jump _13_0_1_1_CAFETERIA

label _13_0_1_1_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_69
    pause 1.0
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.5

    "La cafétéria est pleine, mais personne n'a vraiment l'air de prendre son petit-déjeuner. Les tables sont occupées, les plateaux sont presque tous vides et quelques tasses de café circulent d'une main à l'autre."
    "Quand j'entre, plusieurs conversations baissent d'un ton. Pas assez pour créer un vrai silence, juste assez pour que je comprenne que mon arrivée n'est pas passée inaperçue."

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("mara", "colere", 0.15),
        ("elen", "triste", 0.35),
        ("iris", "inquiet", 0.55),
        ("julian", "hesitation", 0.75),
        ("sael", "mefiant", 0.90),
    ])

    "Je fais comme si je ne remarquais rien et vais directement vers le comptoir. Goumi est derrière, les bras posés devant lui, avec une cafetière presque vide pour seule compagnie."

    noam fatigue "Salut... Il y a quoi pour le petit-déjeuner ?"

    "Goumi me regarde une seconde, puis soupire comme s'il avait déjà répondu à cette question vingt fois depuis le réveil."

    goumi "Comme je l'ai déjà dit, il n'y a plus rien dans les réserves. Plus rien du tout. La prochaine livraison arrive demain."

    noam "Même pas un morceau de pain ?"

    goumi "Non."

    noam "Des biscuits ?"

    goumi "Non plus."

    noam "Un fond de quelque chose ?"

    goumi "Noam, quand je dis plus rien, c'est vraiment plus rien. Il reste du café, et encore, si tout le monde se ressert trois fois, on finira aussi la journée sans ça."

    "Je regarde les étagères derrière lui. D'habitude, même quand les stocks baissent, il reste toujours quelques boîtes ou des aliments qu'on évite jusqu'au dernier moment. Là, les rayonnages sont nus."

    noam fatigue "Alors juste un café."

    goumi "Une tasse. Pas deux. Je préfère le préciser avant que quelqu'un décide qu'un demi-litre de café est un droit fondamental."

    julian hesitation "Je retire officiellement ma proposition d'en faire un droit fondamental."

    "Personne ne rit vraiment. Julian hausse les épaules et boit une petite gorgée de sa propre tasse."

    mara colere "Tu peux toujours essayer de faire passer ça au vote. Apparemment, on vote très bien quand certains décident de ne pas rester jusqu'au bout."

    "Je n'ai pas besoin de me retourner. Le ton de Mara suffit."

    noam fatigue "Bonjour à toi aussi."

    mara "Ne commence pas. J'ai faim, j'ai dormi comme une merde et maintenant Kami peut me regarder dans ma chambre. Alors évite de faire le malin."

    "Goumi pose une tasse devant moi sans intervenir. Je la prends et me tourne vers les autres."

    elen triste "Mara..."

    mara colere "Quoi ? Tout le monde pense la même chose."

    iris inquiet "Non. Tout le monde n'a juste pas envie de lui hurler dessus avant même d'avoir bu son café."

    mara "Moi, si."

    "Elle désigne les tables d'un mouvement sec de la main."

    mara colere "Regarde autour de toi, Noam. On n'a plus rien à manger, on n'a plus de brouilleurs et tout le monde est à bout. Hier, on avait au moins une chance de garder quelque chose pour nous. Tu nous as laissés tomber au pire moment."

    noam fatigue "Je sais ce que j'ai fait."

    mara "Alors dis-moi si tu comptes recommencer."

    "La question me prend de court. Mara ne me demande pas de m'excuser. Elle attend une réponse qui puisse lui servir pour la suite."

    noam "Je n'en sais rien."

    mara "Parfait. C'est exactement ce que j'avais envie d'entendre."

    elen triste "Il aurait pu mentir."

    mara "Ça aurait au moins montré qu'il faisait un effort."

    "Elen garde les deux mains autour de sa tasse sans boire. Elle paraît plus fatiguée qu'en colère, comme si la nuit avait été beaucoup trop longue."

    elen triste "Moi, je veux juste comprendre pourquoi tu es parti. On t'attendait, Noam."

    noam fatigue "Je ne pouvais plus rester dans la salle."

    elen "Pourquoi ?"

    "Je baisse les yeux vers mon café. La vraie réponse me vient immédiatement, mais je sais déjà que je ne vais pas la donner."

    noam "Parce que j'étais à bout."

    mara "On est tous à bout."

    iris inquiet "Mara, laisse-le finir."

    noam "Je ne réfléchissais plus correctement. Tout le monde parlait, tout le monde avait l'air sûr de ce qu'il faisait, et moi j'avais juste l'impression qu'on continuait comme si rien ne changeait."

    sael mefiant "Rien n'est normal ici. Personne ne pense le contraire."

    "Sael parle sans hausser la voix. Il n'a pas l'air intéressé par la dispute, mais son regard reste fixé sur moi."

    sael "Tu peux être perdu, en colère ou méfiant. Ça ne change pas le fait que les autres doivent vivre avec les conséquences de ce que tu fais."

    noam fatigue "Je sais."

    sael "Bien."

    "Il ne rajoute rien et se détourne. Sa façon de couper court à la discussion me met presque plus mal à l'aise que Mara."

    elen triste "Tu crois qu'elle regarde quand on dort ?"

    "La question tombe au milieu de la conversation sans prévenir. Mara cesse de parler. Iris tourne la tête vers Elen."

    noam "Kami ?"

    elen "Oui."

    "Elle se mord légèrement la lèvre avant de reprendre."

    elen triste "Je sais que ça peut paraître idiot, mais depuis que le robot est passé dans ma chambre, j'arrête pas d'y penser. Quand on dort, quand on pleure, quand on se change... elle peut juste regarder."

    iris inquiet "C'est pas idiot."

    elen "J'avais besoin de ce brouilleur. Pas pour préparer un complot ou je ne sais quoi. Juste pour pouvoir fermer ma porte et avoir la paix quelques heures."

    noam fatigue "Je suis désolé."

    elen "Je sais."

    "Elle ne le dit pas pour me pardonner. Elle le dit parce qu'elle n'a rien d'autre à ajouter."

    mara colere "Et pendant qu'on parle d'avoir la paix, on peut rappeler qu'on n'a même plus de quoi bouffer ?"

    goumi "Ça, pour le coup, ce n'est pas la faute de Noam."

    mara "Je n'ai pas dit que ça l'était."

    goumi "Ton regard venait quand même de l'accuser d'avoir mangé les réserves à lui tout seul."

    "Mara lui lance un regard noir. Goumi lève les mains et retourne à sa cafetière."

    julian hesitation "Demain, on aura une livraison. Ça devrait déjà calmer un peu tout le monde."

    mara "Si elle arrive."

    julian "Elle va arriver."

    mara "Tu en sais quoi ?"

    julian "Rien. J'essaie juste d'éviter qu'on commence à se battre pour savoir qui aura le droit de lécher les étagères."

    iris inquiet "Il a pas complètement tort."

    "Je jette un regard autour de moi. Les visages sont tirés et les tasses sont tenues comme si elles avaient plus de valeur qu'elles n'en ont."
    "La faim n'est pas encore insupportable, mais elle rend chaque remarque plus sèche et chaque silence plus lourd. Personne n'a vraiment la patience de faire semblant d'aller bien."

    "Je m'éloigne du comptoir pour m'asseoir à une table presque vide. Elen hésite puis vient en face de moi, tandis qu'Iris prend la chaise à côté d'elle."

    iris inquiet "Je vais te poser une question, et j'aimerais bien que tu ne me répondes pas juste ce que tu crois que j'ai envie d'entendre."

    noam "Vas-y."

    iris "Qu'est-ce que tu nous caches ?"

    "Je relève les yeux vers elle. Son ton n'est pas agressif. C'est justement ce qui rend la question plus difficile à esquiver."

    noam fatigue "Rien."

    iris inquiet "Noam."

    noam "Je t'assure."

    iris "Non. Tu m'assures rien du tout. Depuis ton malaise, tu regardes derrière toi toutes les trente secondes, tu changes de sujet dès qu'on te pose une question et hier tu as accusé toute la salle sans être capable d'expliquer pourquoi."

    "Mara s'approche de nouveau, mais Iris lève immédiatement une main vers elle."

    iris "Laisse-moi parler avec lui."

    mara "Je ne dis rien."

    iris "Pour une fois, continue."

    "Mara serre les lèvres, vexée, mais reste silencieuse."

    iris inquiet "Je ne te demande pas de tout me raconter devant tout le monde. Je te demande juste si tu as une raison de te comporter comme ça."

    "Pendant quelques secondes, je suis tenté de lui parler du couloir. Des images supprimées. De la sensation de voir des choses que personne d'autre ne voit."
    "Puis je pense à la façon dont tout le monde vient de me regarder pour une seule crise de colère. Si je raconte le reste maintenant, je sais exactement ce qu'ils entendront."

    noam fatigue "J'ai juste besoin de remettre mes idées en ordre."

    iris "Donc oui."

    noam "Je n'ai pas dit ça."

    iris "Tu n'avais pas besoin."

    "Elle se recule sur sa chaise et souffle doucement par le nez. Elle n'insiste pas, mais son expression suffit à montrer qu'elle ne me croit pas."

    mara colere "Et après il se demande pourquoi personne ne lui fait confiance."

    noam colere "Je ne me demande rien du tout, Mara."

    mara "Ça tombe bien. J'ai pas envie de faire ton psy avec l'estomac vide."

    elen triste "Vous pouvez arrêter deux minutes ?"

    "Cette fois, sa voix est plus forte. Pas beaucoup, mais assez pour surprendre tout le monde."

    elen "On n'a rien mangé, on a presque pas dormi et on est en train de s'engueuler comme si ça allait remplir les réserves ou remettre les brouilleurs aux murs."

    "Elle baisse les yeux aussitôt, comme si elle regrettait déjà d'avoir élevé le ton."

    elen triste "Je suis en colère contre toi aussi, Noam. Mais je veux pas qu'on finisse tous par se détester."

    "Mara détourne les yeux. Julian repose sa tasse. Même Sael ne répond rien."

    noam fatigue "Moi non plus."

    "Je porte enfin le café à mes lèvres. Il est déjà tiède."

    goumi "Noam ?"

    "Je tourne la tête vers le comptoir. Goumi me regarde avec un léger froncement de sourcils."

    goumi "T'en veux pas un autre, hein ?"

    noam "Tu viens de dire une tasse par personne."

    goumi "Oui. C'est justement pour ça."

    noam "Pourquoi tu me demandes ?"

    "Goumi hésite. Son regard passe de ma tasse à mon visage."

    goumi "Rien. J'ai cru que tu étais déjà passé tout à l'heure."

    noam "Moi ?"

    goumi "J'ai dû confondre."

    noam "Avec qui ?"

    goumi "Aucune idée. J'ai servi du café à la moitié du Conclave avec trois heures de sommeil. Laisse tomber."

    "Il se détourne aussitôt pour ranger une tasse propre. Je continue de le regarder quelques secondes."

    think "Je viens de me réveiller."
    think "Je ne suis pas passé ici avant."

    iris inquiet "Qu'est-ce qu'il y a ?"

    noam fatigue "Rien."

    "Cette fois encore, le mot sort trop vite. Iris ferme les yeux une seconde, clairement agacée, mais ne relance pas."

    mara "Évidemment."

    "Je vide le reste de mon café en deux gorgées, même s'il n'est plus très bon. L'ambiance est devenue trop lourde pour rester assis."

    noam fatigue "J'ai besoin de sortir un peu."

    iris inquiet "Tu vas où ?"

    noam "Je sais pas encore. Juste pas ici."

    "Personne ne me retient. Elen me suit du regard, Iris semble hésiter à dire quelque chose, puis je me lève avant qu'elle en ait le temps."

    jump _13_0_1_1_DISCUSSION_ECOUTEE

label _13_0_1_1_DISCUSSION_ECOUTEE:

    "Je quitte la cafétéria avec le goût du café froid encore dans la bouche. Derrière moi, les conversations reprennent peu à peu, plus basses qu'avant."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_70
    pause 1.0
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Le couloir est vide et, pendant quelques secondes, le calme me fait du bien. Je marche sans réfléchir à une destination précise, juste pour mettre quelques murs entre la cafétéria et moi."

    think "Goumi s'est trompé."
    think "Il sert du café à tout le monde depuis ce matin, c'est possible."

    "J'essaie de laisser cette histoire derrière moi, mais la phrase continue de tourner dans ma tête."

    think "Il a cru que j'étais déjà passé."

    "Des voix arrivent d'un croisement un peu plus loin. Je ralentis et reconnais celle de Ryn avant même de distinguer les autres."
    "Je devrais continuer mon chemin. À la place, je m'arrête juste avant l'angle, hors de leur vue."

    play music "music/bgm_system_override.mp3" fadein 2.5

    ryn colere "Je vous le dis, au prochain vote je veux savoir avant s'il compte encore nous faire son numéro."

    elias fatigue "Tu veux qu'on fasse quoi ? Qu'on lui demande une autorisation écrite pour parler ?"

    ryn "Je veux qu'on arrête de lui donner toutes les infos comme si de rien n'était. Hier, il nous traite de traîtres et il se barre. Aujourd'hui, on devrait faire comme si on lui faisait encore confiance ?"

    tomas "Le mettre à l'écart va pas forcément arranger les choses."

    ryn colere "Je parle pas de l'enfermer dans sa chambre. Je dis juste qu'on arrête de tout lui raconter tant qu'on sait pas ce qui lui passe par la tête."

    elias "Et tu proposes qu'on discute où, exactement ? On vient de perdre les brouilleurs. Si on commence à organiser des conversations secrètes maintenant, Kami va adorer."

    ryn "Je m'en fous de Kami pour l'instant."

    nyra "Tu devrais éviter."

    "La voix de Nyra est calme, presque détachée. Ryn se tait juste assez longtemps pour lui laisser la place."

    nyra "Elle nous voit de nouveau. Si vous commencez à choisir qui peut entendre quoi, faites au moins l'effort de vous rappeler qu'elle entend probablement tout aussi."

    tomas "C'est justement ça qui me gêne. On est déjà tous méfiants. Si on commence à faire des groupes dans les groupes, dans deux jours plus personne parlera à personne."

    ryn colere "Et si Noam recommence ? On fait quoi ? On attend qu'il fasse encore foirer un vote important ?"

    elias fatigue "On lui parle avant. C'est encore une option, normalement."

    ryn "Iris a essayé. Elen aussi. Il répond rien."

    tomas "Peut-être qu'il a vraiment rien à dire."

    ryn "Ou peut-être qu'il nous cache quelque chose."

    "Je serre légèrement la mâchoire. Derrière le mur, personne ne parle pendant quelques secondes."

    elias "Ça, je pense qu'il nous cache quelque chose."

    tomas "Super. Très rassurant."

    ryn "Voilà."

    nyra "Ça ne veut pas dire qu'il a tort."

    "Le silence qui suit est plus long. Même moi, je reste immobile."

    ryn "Pardon ?"

    nyra "Vous partez du principe qu'il est devenu paranoïaque parce qu'il ne nous explique rien. C'est possible. Mais la vraie question, c'est de savoir s'il n'explique rien parce qu'il délire... ou parce qu'il a vu quelque chose qu'il n'arrive pas à expliquer."

    elias "Nyra, il a accusé la moitié de la salle au hasard."

    nyra "Je sais. Et c'était stupide. Ça ne répond pas à ma question."

    tomas "Tu penses qu'il a une vraie raison ?"

    nyra "Je pense surtout qu'on n'en sait rien."

    "Ryn souffle bruyamment."

    ryn colere "Moi, ce que je sais, c'est qu'on a faim, qu'on a plus aucun endroit tranquille et qu'au prochain vote j'ai pas envie de découvrir sa nouvelle crise en même temps que tout le monde."

    elias fatigue "Là-dessus, on est d'accord."

    tomas "On pourrait juste lui dire ça en face."

    ryn "Je compte bien le faire."

    "Je recule légèrement du mur. Une partie de moi voudrait rester pour entendre la suite, mais je n'ai aucune envie qu'ils me surprennent à les écouter."

    think "Ils ne me font plus confiance."
    think "Mais Nyra n'a pas dit que j'avais tort."

    "Je repense à Goumi, au couloir, aux images qui manquent et à toutes les petites choses que j'ai essayé de mettre de côté parce qu'elles avaient l'air trop absurdes."

    think "Il faut que j'arrête de chercher un coupable au hasard."
    think "Je dois reprendre ce que je sais vraiment, depuis le début."

    "Je rebrousse chemin avant que quelqu'un ne tourne au croisement."

    jump _13_0_1_1_CHAMBRE_PAPIER

label _13_0_1_1_CHAMBRE_PAPIER:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_71
    pause 1.0
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_cold_metadata.mp3" fadein 2.5

    "De retour dans ma chambre, je ferme la porte derrière moi puis reste quelques secondes la main sur la poignée. Le réflexe me fait presque rire : verrouillée ou non, cette porte ne protège plus grand-chose."
    "L'emplacement vide du brouilleur me saute immédiatement aux yeux. Je détourne le regard et vais m'asseoir au bureau."

    think "Très bien. Pas de théorie. Pas de traître choisi au hasard."
    think "Seulement ce que je sais."

    "Je prends une feuille et un stylo. Au lieu d'écrire des noms, je trace trois colonnes assez larges."

    noam murmure "Certain. Incertain... et le reste."

    "Dans la première colonne, je note les faits dont je suis sûr."

    "Des matériaux ont disparu de la réserve technique."
    "La photo de Léa a été volée dans la chambre de Kael."
    "Mon dessin de Juliette a disparu lui aussi."
    "Une partie des images du couloir a été supprimée."

    "Je relis les quatre lignes avant de continuer. Rien de tout ça n'est une impression. Même si je me trompe sur le responsable, ces choses se sont réellement produites."

    "Dans la seconde colonne, j'écris ce qui reste beaucoup moins clair."

    "La silhouette aperçue dans le couloir."
    "Les comportements qui ne correspondent pas toujours à mes souvenirs."
    "Goumi persuadé, pendant quelques secondes, de m'avoir déjà servi ce matin."

    "Je m'arrête sur cette dernière ligne."

    think "Il était fatigué."
    think "Ça peut vraiment être aussi simple que ça."

    "Je la laisse quand même. Si je commence à retirer tout ce qui me dérange sous prétexte que ça peut avoir une explication, cette feuille ne sert à rien."

    "La troisième colonne reste vide."

    think "Et le reste ?"

    "Je pose le stylo et regarde les deux premières colonnes."
    "Les vols me dérangent toujours autant, mais ce n'est pas leur valeur qui m'intéresse. Les matériaux peuvent servir à quelque chose. Pour la photo et le dessin, c'est différent."

    think "Une photo de Léa. Un dessin de Juliette."
    think "Deux objets personnels. Deux représentations de quelqu'un qui compte pour nous."

    "Je souligne cette idée une fois. Pas davantage."

    think "Ça ne prouve rien."
    think "Mais au moins, c'est un point commun qui existe vraiment."

    "Je note une nouvelle question à côté des deux lignes."

    "Pourquoi voler une image plutôt qu'un objet utile ?"

    "Je passe ensuite aux caméras. Si quelqu'un a supprimé volontairement des images, il savait exactement ce qu'il voulait cacher. Si c'est Kami qui l'a fait, je ne comprends pas pourquoi elle aurait laissé le moindre doute."
    "Et si ce n'est pas Kami, alors quelqu'un ici possède des moyens que je ne comprends pas encore."

    think "Ça, c'est le problème."

    "Je me recule sur ma chaise et regarde la feuille entière. Ce n'est pas une réponse, mais au moins je distingue mieux ce qui est réel de ce que je suis en train d'imaginer."

    think "Nyra a raison sur un point."
    think "Je peux être paranoïaque et avoir quand même remarqué quelque chose."

    "Je prends mon vieux cahier noir dans le tiroir. J'ai toujours eu l'habitude d'y mettre les idées qui me passent par la tête, surtout quand j'ai besoin d'arrêter de tourner en rond."
    "Le cahier est exactement là où je pensais l'avoir laissé. Je le pose à côté de la feuille et commence à chercher une page vide."

    "Je tourne une première page, puis une deuxième."
    "Ma main s'arrête au milieu du geste."

    "Je connais ce dessin."

    "Pendant une seconde, je crois avoir ouvert la mauvaise page. Puis je comprends que ce n'est pas possible."

    "Quelqu'un a reproduit le dessin de Juliette dans mon cahier."

    "Les traits suivent presque parfaitement les miens. La forme du visage, les cheveux, le pli du vêtement, tout est assez proche pour que je reconnaisse immédiatement l'original."
    "Mais ce n'est pas mon dessin. Le trait est plus sombre et légèrement plus appuyé, comme si la personne avait repassé plusieurs fois sur certaines lignes."

    "Je rapproche le cahier de la lampe."

    think "Je n'ai jamais fait ça."
    think "Je n'ai même pas sorti ce cahier depuis plusieurs jours."

    "Je tourne les pages avant et après. Rien d'autre n'a changé. Aucun mot ajouté, aucune feuille arrachée, aucune trace qui m'aide à comprendre quand quelqu'un a pu toucher au cahier."

    "Je reviens au dessin."

    call j13_sept_differences_run from _call_j13_sept_differences

    think "Quelqu'un est entré ici."
    think "Ou alors quelqu'un l'a pris sans que je m'en rende compte."

    "Je regarde la porte, puis l'emplacement désormais vide du brouilleur. L'idée de demander à Kami me traverse l'esprit avant que je l'écarte aussitôt."

    think "Si elle sait, elle ne me dira probablement rien."
    think "Et si elle ne sait pas, c'est encore pire."

    "Je garde les deux versions en tête. Les changements sont trop précis, trop choisis pour être de simples erreurs de copie."

    think "C'est volontaire."

    "Je voudrais trouver une autre explication, me dire que je me souviens mal du dessin ou que la copie est simplement imparfaite. Mais quelqu'un a reproduit assez précisément chaque détail pour que cette petite différence ressorte encore davantage."

    "Je referme le cahier, puis le rouvre presque aussitôt. Le dessin est toujours là."

    noam murmure "Qui a fait ça...?"

    "Aucune réponse ne vient. Seulement le bourdonnement discret de la ventilation et le silence trop propre de la chambre."

    "Je regarde la feuille posée à côté du cahier. La troisième colonne est toujours vide."
    "Je reprends lentement mon stylo et écris une seule ligne dedans."

    "Quelqu'un a copié le dessin de Juliette dans mon cahier."

    "Je reste quelques secondes avec la pointe du stylo sur le papier, puis ajoute juste en dessous :"

    "Je ne sais pas comment."

    "Cette fois, je ne raye rien."

    pause 2.5

    call end_day("14") from _call_end_day_4
    jump _14_0_1_1_0_REVEIL_CHAMBRE
