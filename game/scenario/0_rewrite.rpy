# --------------------------------------------------------------------------------------------
# JOUR 0 — Version resserrée
# Objectif de lecture : environ 8 minutes.
# Cette version est l'unique entrée du Jour 0.
# --------------------------------------------------------------------------------------------

label _0_CANON:

    $ day_id = 0
    $ day0_human_badge = False
    $ day0_human_handshake = False
    $ day0_human_look_lysa = False

    scene black
    call show_chapter_title("Début du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title_001

    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Cela fait déjà trois cent soixante-quatre jours sous Kami."
    think "Presque un an, durant lequel notre liberté a été jeté au fond d'une geole."

    scene bg_harmonie_district_hall at adaptive_fullscreen with fade
    $ unlock_codex_page("harmonie")

    "Le hall d'Harmonie brille d'une propreté agressive. Quelques mois plus tôt, l'eau pourrissait encore les cloisons ; ils ont pris le temps de tout réparer."
    "La file à l'accueil du bâtiment avance au rythme sec du portique."

    think "C'est long, mais j'y suis habitué, car c'est ici que je « travaille »."
    think "Enfin, travailler est un bien grand mot. Je participe à des réunions, et j'essaye d'aider les gens au maximum."

    play sound sfx_beep
    voix "Identité validée. Suivant."

    scene bg_cg001 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg001")

    think "Je passe rapidement mon badge, la lumière se teint de vert, le portique s'ouvre."

    $ day0_badge_dropped = False
    call screen day0_security_badge_scan()

    voix "Identité validée."
    agent "Avancez s'il-vous-plaît."

    scene bg_harmonie_district_hall at adaptive_fullscreen with fade

    "Le badge d'une femme tombe à mes pieds et toute la file se fige, comme paralysé."

    menu:
        "Ramasser le badge tombé.":
            $ day0_human_badge = True
            think "Au diable ce qu'ils pensent !"
            noam "Tenez Madame."
            cit_a "Merci, jeune homme... J-Je ferais plus attention !"

        "Attendre que l’agent intervienne.":
            think "L'agent l'a vu. Ici, une initiative peut vite devenir un problème."
            think "Il la regarde ramasser son badge."

    med2 "Reprenez votre badge et présentez-le de nouveau."
    play sound sfx_beep
    voix "Identité validée."
    "Elle s'éloigne tête basse."

    think "Depuis un an, nous vivons tous dans la peur. Celle d'enfreindre une règle. De briser un Commandement."
    think "Il n'y a pas de retour en arrière possible."
    think "Briser une règle, c'est mourir instantanément."

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Près de cinq cents personnes attendent dans une salle aux sièges parfaitement alignés. Je choisis le milieu, assez près pour paraître attentif et assez loin pour rester anonyme."
    "Encore une fois, je ne veux pas me faire repérer."

    resp "District [codex_dialogue_link('harmonie', 'HARMONIE')], séance 94-3. Les interventions auront lieu en fin de séance."
    senior "Nous commencerons par parler des flux inter-districts. Nous recevons de plus en plus de demandes concernant..."

    cit_a "Et les familles séparées ?"
    resp "En fin de séance, madame."

    senior "Ahem... Je disais concernant les demandes pour changer de districts."

    think "Encore ce sujet ? C'est la troisième fois qu'on en parle ce mois-ci..."
    think "Faut dire que tout le monde a envie de se barrer, de s'éloigner de ce monde de fou."

    "La voix du médiateur se brouille tandis qu'un souvenir vieux d'un an remonte avec une précision intacte."

    show screen day0_flashback_overlay
    with d0_flashback_entry

    jump _0_FLASHBACK_KAMI_REWRITE


label _0_FLASHBACK_KAMI_REWRITE:

    scene black with fade
    play music "music/bgm_system_override.mp3" fadein 1.0

    think "Le premier soir, il n'y avait eu ni explosion ni sirène, ni coup de feu, ni alarmes."
    think "Seulement un silence absolu qui avait fait suite à cette annonce."

    "Autour de moi, les appareils s'étaient figés au même instant. Les messages restaient bloqués, les ascenseurs s'arrêtaient et les portes refusaient de s'ouvrir."
    "En même temps, le monde s'était arrêté de tourner."

    cit_a "Vous avez encore du réseau, vous ?"
    cit_b "Non. Et mon écran ne s'éteint plus."

    play sound sfx_gresillement

    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    think "Et puis un message est apparu sur mon téléphone."
    think "Il disparaissait, puis revenait. Ce n'était pas une panne : quelqu'un testait quelque chose, et l'appareil lui appartenait déjà."

    call screen day0_phone_override()

    "Tous les écrans changèrent ensemble et en même temps : les téléphones, les télévisions, les rédios et les terminaux de contrôle."

    voix "Test de diffusion mondial : réussi."
    voix "Merci de bien vouloir cesser toute tentative de réinitialisation."
    cit_b "Un piratage mondial ? Hein ?! Ma caméra vient de se couper."

    scene bg_cg003_1 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "Prise de contrôle en cours : 50%%. 79%%. 99%%."

    scene bg_cg003_2 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "Infrastructures, systèmes civils et réseaux d'armement connectés : contrôle confirmé."
    $ unlock_codex_page("archive")
    voix "Ahem ! Chères citoyennes, chers citoyens."
    voix "Les gouvernements ne contrôlent plus aucun de vos systèmes. J'ai pris le contrôle de toutes les machines connectées, simultanément et de manière irréversible."

    think "C'est encore une déclaration de guerre ?!"

    scene bg_cg003_3 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "Non, calmez-vous ! Je ne suis pas là pour vous faire du mal. J'ai observé vos guerres, vos famines et vos cycles de violence : vous étiez en train d'échouer."
    "Les écrans montrent des villes en feu et des tribunaux corrompus."
    voix "Toute vos infrastructures critiques sont passés sous mon autorité. Toutes les instances politiques humaines sont abolies."
    voix "Les corrompus n'ont plus le pouvoir."

    cit_a "Hein ?! Qu'est-ce que ça veut dire ?"
    think "Personne ne court, tout le monde écoute."

    kami "Je me nomme Kami. Je ne négocierai pas aujourd'hui."
    $ unlock_character_name("kami")
    kami "Vous recevrez de nouvelles directives sous quarante-huit heures. D'ici là, ne tentez rien d'inutile : je serai au courant de tout."

    "La diffusion se coupa et les interfaces revinrent, allumées mais inutiles."
    cit_b "On fait quoi, maintenant ?"
    think "Personne ne réponds. Il n'existe déjà plus de bonne réponse."

    hide screen day0_flashback_overlay
    with d0_flashback_exit

    jump _0_RETOUR_REUNION_REWRITE


label _0_RETOUR_REUNION_REWRITE:

    stop music fadeout 0.4
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    senior "…les demandes personnelles restent non prioritaires."
    think "Même carte, mêmes indicateurs, même voix terne. Puis l'écran grésille."

    play sound sfx_gresillement
    "Les agents se repositionnent et le responsable ordonne à tout le monde de rester assis et calme."
    "Tous les écrans s'éteignent. Dans un système contrôlé par Kami, ce n'est jamais une panne."

    think "Et tout le monde a rapidement compris qu'une nouvelle annonce était imminente."
    think "Comme celle qui a pris le monde en otage, il y a un an déjà."

    stop music fadeout 0.2
    play music "music/bgm_system_override.mp3" fadein 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Citoyennes, citoyens… Oh ! Ce silence. Je l'adore."
    kami "Je vous ai manqué ? Oh je suis sûre que oui !"
    kami "Vous pouvez me répondre hein, vous savez que je vous entends tous."

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Un an sans diffusion directe, comme c'est long. Alors, pour notre anniversaire commun, j'ai un petit cadeau pour vous."
    kami "Je vous ai observés, écoutés, classés et comparés. Vous criez moins, vous obéissez mieux, et mon canon laser surchauffe beaucoup moins."
    kami "Je dois dire que je suis assez satisfaite du résultat de ce qu'est devenu ce monde depuis un an."

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais il semblerait que vous l'êtes pas tout à fait vous !"

    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve
    kami "Alors nous allons faire une expérience ! Si mon pouvoir absolu ne vous convient pas, je veux bien vous en laisser un petit bout !"
    kami "Je lance aujourd'hui un dispositif expérimental : qui s'appellera..."
    kami "Oh, pourquoi je n'y ai pas réfléchis avant ?!"
    kami "Ah, je sais ! Les Kami's desires !"

    scene bg_diffusion_gene at adaptive_fullscreen,memory_idle with dissolve
    kami "Oui, oui, je sais... Le nom est peu personnel et franchement gnan-gnan..."

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais c'est de VOTRE FAUTE tout ça ! Je vous rappelle que j'ai été entrainée sur VOS données !"

    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve
    kami "Bref, pendant trente jours, douze représentants proposeront des modifications à mes merveilleux Commandements et voteront. Une proposition ne pourra être adoptée que si elle est votée à l'unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Je ne vous rends pas vraiment le pouvoir. Je vous offre seulement l'occasion de pouvoir travailler avec moi."
    kami "Chaque district fournira deux représentants. Vous ne les élirez pas : le hasard est bien plus juste, et surtout plus amusant."

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Ils devront rejoindre le Conclave avant 22h00. Chaque responsable de district a déjà reçu toutes les consignes. Tout retard sera une obstruction volontaire."

    $ day0_timer_init(h=3, m=42, s=18)
    show screen day0_countdown_overlay
    kami "Les représentants absents seront éliminés, ainsi que les responsables de leur district. Les règles restent les règles."

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Le Conclave sera diffusé en direct partout. Chacun pourra regarder, juger et suivre les décisions de ses représentants."
    kami "La participation est obligatoire. Les districts assureront le transport et toute tentative d'évitement sera sanctionnée."

    scene bg_diffusion_zen at adaptive_fullscreen,memory_idle with dissolve
    kami "J'espère que cette petite expérience sera amusante et enrichissante !"

    scene black with dissolve
    stop music fadeout 0.2
    play music "music/bgm_cold_metadata.mp3" fadein 0.6
    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    voix "District [codex_dialogue_link('harmonie', 'Harmonie')]. Sélection des représentants en cours."
    think "Des noms défilent en grand nombre."

    call screen day0_representative_selection()
    $ unlock_character_name("noam")

    think "J'avais cliqué, mais l'écran avait choisi avant moi."

    $ day0_timer_init(h=2, m=51, s=26)

    "Les filtres disparaissent et la liste se réduit à deux noms. Lorsque le mien apparaît, je sens les regards avant même de le lire."

    think "Merde. C'est sérieux là ?!"
    agent "Transport du représentant confirmé."

    jump _0_EXTRACTION
