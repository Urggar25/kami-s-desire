label _11_0_1_1_REVEIL_CHAMBRE:

    play music "music/bgm_romantic_atmosphere.mp3" fadein 2.5
    play sound sfx_heartbeat fadeout 3.0  # résidu du malaise
    
    "Je sens une sensation humide et fraîche sur mon front."
    "J’ouvre les yeux difficilement. La lumière me brûle un peu."
    
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)
    
    iris "Ah bah enfin ! Monsieur daigne se réveiller."
    iris "T’as mis le temps, hein. J’ai cru que t’allais commencer ton hibernation."

    scene bg_cg031 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg031")
    
    "Elle retire rapidement sa main de mon front."
    "Sa tête était posée contre le bord du matelas. Elle a clairement passé une partie de la nuit ici."
    
    noam faible "Iris… ?"
    noam "Qu’est-ce qui s’est passé… ?"
    
    iris "Ce qui s’est passé ? Tu t’es écroulé comme une merde pendant le débat, voilà ce qui s’est passé !"
    iris "Un instant t’étais debout à poser des questions bizarres, et la seconde d’après : bam, par terre."
    iris "On a tous flippé, espèce d’idiot."
    
    "Elle trempe un nouveau linge dans l’eau fraîche, l’essore un peu trop fort, et me le repose sur le front avec une douceur qui contraste avec son ton."
    
    iris "T’as fait une fièvre de cheval toute la nuit. Genre 39.5. On s’est relayés à ton chevet, parce que bien sûr, faudrait pas que le seul mec un minimum sensé de la bande y passe."
    iris "Mara a grogné mais elle est restée deux heures, Sael a fait le médecin de campagne, même Kael est venu… Bref, tout le monde y est passé."
    
    iris desaccord "Et Ryn a juste dit « Dis-lui de pas crever, on a déjà assez de merdes comme ça ». C’est sa façon à lui de s’inquiéter, j’imagine."
    
    "Elle croise les bras et détourne légèrement le regard, les joues un peu rouges."
    
    iris "… Bref. T’as intérêt à te remettre vite fait. Parce que si tu nous refais un coup pareil, je te jure que je te laisserai crever la prochaine fois."
    iris "C’est clair ?"
    
    noam "… Merci d’avoir veillé sur moi."
    
    iris "C’est pas comme si j’avais eu le choix ! Ils m’ont tous forcée."
    iris "Et puis… c’est pas comme si je pouvais te laisser délirer dans ton coin."
    iris "Qu'est ce qu'on aurait fait si tu avais pété un cable, hein ?"
    
    "Elle marmonne dans sa barbe, mais sa main reste près de mon épaule."
    
    iris "Allez, bois ça."
    
    "Elle me tend un verre d’eau avec un geste un peu sec, mais elle attend que je le prenne bien avant de lâcher."
    
    iris "Et arrête de faire cette tête de chien battu. T’as juste trop stressé, eu trop chaud, et t’as accumulé de la fatigue."
    iris "Sael a dit que c'était probablement pas à cause d'une bactérie."
    
    "Elle reste un moment silencieuse, le regard un peu perdu dans le vide."
    
    menu:
        "Lui demander si elle sait ce que j’ai vu avant l’annonce":
            jump noam_parle_doppelganger_iris
        "Garder ça pour moi pour l’instant":
            jump noam_garde_secret
            
label noam_parle_doppelganger_iris:

    play music "music/bgm_system_override.mp3" fadein 2.5
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)

    $ showGroup([
        ("noam", "fatigue", 0.20),
        ("iris", "inquiet", 0.80),
    ])

    noam hesitation "Iris… avant de m’écrouler… j’ai vu quelque chose de bizarre."
    noam inquiet "Juste avant l’annonce de Kami. Dans le couloir, vers la salle de stockage."

    "Iris fronce les sourcils. Son expression change du tout au tout."

    iris inquiet "De bizarre comment ?"

    noam reflexion "Une silhouette… au loin. Je sais pas trop."
    noam peur "C’était flou, mais… ça m’a mis mal à l’aise."

    iris desaccord "Noam… t’avais déjà la tête qui tournait pendant le débat."
    iris reflexion "T’as probablement vu un reflet, ou quelqu’un qui passait, ou juste rien du tout. Avec la fièvre que t’as eue, c’est normal."

    "Elle croise les bras, mais son regard reste fixé sur moi, plus attentif qu’elle ne veut le laisser paraître."

    iris inquiet "En plus, hier soir t’as demandé à tout le monde s’ils étaient dans les couloirs. Personne n’a rien vu."

    noam fatigue "Ouais… t’as sûrement raison."
    noam hesitation "C’est juste que… sur le moment, j’étais persuadé que c’était pas normal."

    "Iris reste silencieuse quelques secondes. Elle semble hésiter à dire quelque chose, puis finit par soupirer."

    iris fatigue "Écoute… t’es encore crevé, t’as la tête dans le brouillard, et on vient tous de vivre une soirée de merde."
    iris desaccord "C’est pas étonnant que ton cerveau te joue des tours."
    iris determine "Arrête de te prendre la tête avec ça pour l’instant, d’accord ?"

    "Elle pose à nouveau le linge frais sur mon front, un peu plus doucement que nécessaire."

    iris gene "Si tu continues à cogiter comme ça, tu vas te refaire de la fièvre pour rien."
    iris inquiet "Et j’ai pas envie de repasser la nuit à te surveiller, compris ?"

    "Malgré son ton râleur, elle ne bouge pas tout de suite. Son regard s’attarde un peu trop longtemps sur moi."

    iris hesitation "… Si jamais tu revois un truc qui te semble vraiment pas normal, tu m’en parles à moi. Pas aux autres."
    iris determine "Pour l’instant, repose-toi. C’est tout ce que t’as à faire."

    "Elle se lève lentement, comme si elle n’était pas vraiment convaincue par ses propres paroles."

    iris fatigue "Je vais te chercher quelque chose à manger. Bouge pas de là."

    "Avant de sortir, elle s’arrête un instant dans l’encadrement de la porte, le dos tourné."

    iris gene "Et arrête de faire cette tête. Ça me stresse."

    jump _11_0_1_2_APRES_REVEIL


label noam_garde_secret:

    play music "music/bgm_system_override.mp3" fadein 2.5
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)

    $ showGroup([
        ("noam", "fatigue", 0.20),
        ("iris", "inquiet", 0.80),
    ])

    "Je reste silencieux un moment. Les mots restent bloqués dans ma gorge."

    noam hesitation "... Non, rien."
    noam culpabilite "C'est rien d'important."

    "Iris plisse les yeux. Elle me fixe un peu trop longtemps, comme si elle sentait que je lui cachais quelque chose."

    iris desaccord "T'es sûr ? T'as l'air d'avoir quelque chose sur le bout de la langue."

    noam fatigue "Ouais... juste un rêve bizarre à cause de la fièvre. Laisse tomber."

    "Elle reste silencieuse quelques secondes, visiblement pas convaincue, puis finit par hausser les épaules."

    iris reflexion "Si tu le dis."
    iris desaccord "De toute façon, t'es encore à moitié dans les vapes. Pas la peine d'essayer de te faire cracher le morceau maintenant."

    "Elle attrape le linge, le trempe à nouveau dans l'eau fraîche et me le repose sur le front un peu brusquement."

    iris determine "T'as intérêt à te reposer correctement, compris ?"
    iris colere "Si tu te refais un malaise parce que tu stresses pour des conneries, je te jure que je te colle une baffe."

    "Malgré son ton sec, elle ajuste le drap sur moi."

    iris fatigue "Je vais te chercher quelque chose à manger à la cafétéria. Bouge pas de ce lit, hein."
    iris taquin "Et si tu vomis pendant mon absence, je te fais nettoyer toi-même."

    "Elle se dirige vers la porte, puis s'arrête un instant sans se retourner."

    iris gene "… Et arrête de cogiter. T'as une sale tête quand tu fais ça."

    "Elle marmonne quelque chose d'inaudible en sortant."

    jump _11_0_1_2_APRES_REVEIL
