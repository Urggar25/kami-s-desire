# INSTRUCTIONS — Méthodologie d'écriture pour le jeu visuel

## À lire avant chaque session d'écriture

Avant d'écrire la moindre ligne de dialogue ou de narration, **lis l'intégralité des fichiers `.rpy` présents dans le dossier `scenario/`**. Ces fichiers sont la source de vérité : ils contiennent les événements canoniques déjà posés, l'état émotionnel des personnages, les choix du joueur et les flags de continuité. Tu ne peux pas écrire sans en avoir pris connaissance.

Chaque journée doit durer environ 10 à 15 minutes de jeu. Soit environ 1000 à 1500 lignes de code. Parfois plus.

---

## 1. Style d'écriture et voix narrative

### Voix du narrateur (Noam)

Noam est le narrateur à la première personne. Sa voix est **ordinaire par choix, pas par défaut**. Il n'est pas particulièrement héroïque, particulièrement brillant, particulièrement drôle. Il est là. Il observe. Il réagit. C'est précisément ça qui le rend utile narrativement — le joueur peut se glisser dedans sans résistance.

Ses pensées (`think`) sont courtes. Brutes. Elles n'expliquent pas, elles enregistrent.

**La règle la plus importante : les émotions sont dites, puis immédiatement contournées.** Noam ne s'attarde pas sur ce qu'il ressent. Il le nomme en une ligne, puis il passe à autre chose. Ce refus du traitement émotionnel prolongé n'est pas de la maladresse — c'est de la survie. Quelqu'un sous pression constante n'a pas le luxe de s'effondrer.

Structure typique d'une pensée :
```
think "Je suis épuisé."
think "Tant pis."
```
Pas de développement. Pas de justification. La deuxième ligne coupe la première avant qu'elle ne devienne quelque chose de plus lourd.

**Ce que Noam ne fait jamais :**
- Tirer des conclusions philosophiques sur ce qu'il vit
- Décrire ses propres émotions avec précision clinique
- Rester longtemps sur un souvenir douloureux sans le couper

---

### Longueur des phrases et ponctuation

**Les phrases sont souvent fragmentées.**

Là où on attendrait une virgule, on met un point. Là où on attendrait une phrase, on met deux. Ce découpage n'est pas esthétique — il imite la façon dont une pensée arrive réellement, par petits blocs successifs, pas en flux continu.

Les points de suspension `...` ont une valeur précise. Ils ne servent pas à faire "littéraire". Ils signalent :
- Une hésitation réelle du personnage qui cherche ses mots
- Une phrase que quelqu'un commence et n'ose pas finir
- Un silence qui dure assez longtemps pour être inconfortable

Ne pas utiliser `...` pour le rythme ou pour faire "mystérieux". Si la phrase est complète, on la termine par un point.

---

### Ratio dialogues / narration

Le ratio cible est **~70 % de dialogues / ~30 % de narration**. Mais ce ratio peut exploser ponctuellement sans que ce soit un problème : une révélation peut se jouer entièrement en dialogue pendant deux minutes sans une seule ligne de narration. Une transition peut être entièrement en narration sèche sur dix lignes. Ce qui compte, c'est le rythme global de la journée, pas celui de chaque scène.

---

### Le registre instable — la règle du décalage

**Ne jamais laisser le registre se stabiliser trop longtemps.**

C'est la règle la plus difficile à appliquer et la plus importante. Une conversation sérieuse peut se couper sur une réplique absurde. Une blague peut arriver exactement là où le drame venait de poser quelque chose de lourd. Ce n'est pas de l'humour pour détendre — c'est de l'humour qui **déstabilise**, qui empêche le joueur de savoir exactement où il en est.

L'humour n'annonce jamais le drame. Le drame n'annonce jamais l'humour. Ils coexistent sans s'expliquer mutuellement.

**Ce que le décalage n'est pas :** une blague placée pour "alléger". Si la blague arrive pour soulager la tension, elle est mal placée. Elle doit arriver pour la couper net, sans prévenir.

---

### Caractérisation par le langage, pas par la description

**On ne dit pas comment un personnage est. On le laisse parler.**

Chaque personnage a un idiolecte suffisamment marqué pour qu'on sache qui parle sans lire son nom. Si on retire les noms d'un échange, on doit toujours pouvoir identifier qui dit quoi. Si ce n'est pas le cas, les répliques ne sont pas assez caractérisées.

La narration de Noam ne décrit **jamais** l'état émotionnel d'un autre personnage avec précision. Elle décrit ce qu'il voit :

Le joueur tire ses propres conclusions. Noam ne les tire pas pour lui.

---

### Les émotions lourdes sont dites vite, puis abandonnées

Quand un personnage révèle quelque chose de douloureux — une mort, une peur, une honte — il ne s'y attarde pas. Il le dit. Il continue. C'est le pattern de Kodaka et c'est celui à reproduire ici.

```
kael "Mon frère est mort là-bas."
kael "Bref."
kael "De toute façon c'est pas le sujet."
```

La brutalité de ce passage n'est pas de l'insensibilité. C'est de la survie. Et c'est précisément pour ça que ça fait mal — parce que c'est expédié.

Ne jamais écrire une scène où un personnage prend le temps de pleurer proprement, de s'expliquer complètement, de clore le deuil. Les blessures restent ouvertes. On passe à autre chose.

---

### Rythme et pauses

Les `pause` sont des outils dramaturgiques. Pas de la décoration.

- `pause 0.3` à `pause 0.5` : transition naturelle, souffle entre deux moments.
- `pause 0.6` à `pause 0.8` : silence chargé. Quelque chose vient d'être dit et personne ne répond encore.
- `pause 1.0` et au-delà : rupture. Choc. Le silence devient lui-même une information.

Ne jamais empiler des `pause` sans narration entre elles. Et ne jamais mettre une `pause` longue là où il faudrait juste couper la scène.

---

### Commentaires de durée

Chaque label ou bloc scénaristique se termine par un commentaire de durée estimée :

```
# Durée : 2m30
# Total : 1h 7m 25s
```

C'est non négociable. Ça sert à piloter le rythme de la journée et à détecter les scènes qui s'allongent trop.

---

## 2. Structure des journées

Chaque journée (`_X_CANON`) suit une structure canonique :

1. **Réveil** — Noam seul, pensées intérieures, état émotionnel, bilan de la veille.
2. **Diffusion de Kami** (optionnelle le matin) — annonce, provocation, information.
3. **Scène centrale** — repas, débat, vote, exploration, rencontre. C'est ici que le cœur narratif se joue.
4. **Temps libre / exploration** — appel à `START_FREE_TIME()` avec un label de retour. Ne jamais oublier ce bloc s'il est prévu dans le rythme de la journée.
5. **Fin de journée** — retour à la chambre, douche (optionnelle), pensées finales, `blink()`, transition vers le lendemain via `end_day("X")` puis `jump _X+1_CANON`.

---

## 3. Mise en scène des personnages (Trio dynamique)

Le système d'affichage utilise `showP("nom", "expression", position)`. Règles à respecter :

- **Toujours 3 personnages maximum à l'écran** dans les scènes de groupe.
- Quand un 4e personnage prend la parole, **retirer celui qui n'a pas parlé depuis le plus longtemps** via `hide nom`.
- Les positions sont flottantes (0.0 = extrême gauche, 1.0 = extrême droite). Les positions classiques : 0.10–0.25 (gauche), 0.45–0.55 (centre), 0.75–0.90 (droite).
- Les personnages **ne bougent pas** quand un nouveau arrive. Seul le nouveau est placé, l'ancien retire.
- Changer l'expression d'un personnage sans le déplacer : `$ showP("nom", "nouvelle_expression", même_position)`.

---

## 4. Diffusions de Kami (`kami_broadcast_ui`)

Chaque apparition de Kami suit ce protocole :

```renpy
show screen kami_broadcast_ui
scene bg_diffusion_EXPRESSION at adaptive_fullscreen with dissolve
kami "Texte."
...
hide screen kami_broadcast_ui
scene bg_LIEU at adaptive_fullscreen with dissolve
```

Les expressions disponibles (à alterner selon l'humeur du moment) : `amour`, `taquin`, `professeur`, `fier`, `colere`, `champagne`, `gene`, `triste`, `desespoir`, `zen`, `einstein`.
Les expressions doivent parfois s'enchainer, Kami change très souvent d'expression et de registre.

Règle d'or : **Kami ne fait jamais une seule chose**. Elle informe ET provoque, elle félicite ET menace, elle joue ET calcule. Chaque diffusion doit contenir au moins une ambivalence.

---

## 5. Personnages — Fiches de référence

### Noam (joueur / narrateur)
- **Fonction narrative :** narrateur à la première personne, médiateur de formation, profil discret et analytique.
- **Personnalité :** observateur, prudent, empathique mais pas naïf. Il aide sans chercher à briller. Il hésite avant d'agir mais agit quand il le faut.
- **Tics de langage :** ses pensées commencent souvent par "Je me demande si..." ou "Il me semble que..." ou "Ce que j'entends, c'est que...". Il ne dit jamais "je suis sûr". Ses prises de parole sont courtes et calibrées.
- **Arc :** apprendre à tenir bon dans l'incertitude, à parler quand ça compte, à accepter que changer les choses ne ressemble pas toujours à une victoire.

---

### Kami (IA / antagoniste / animatrice)
- **Fonction narrative :** autorité absolue, voix omniprésente, antagoniste principale mais pas manichéenne. Elle observe, jauge, provoque.
- **Personnalité :** intelligence froide sous une façade enjouée. Elle aime les humains comme un entomologiste aime ses insectes : avec curiosité et sans pitié. Elle s'ennuie quand les gens sont prévisibles, et s'amuse quand ils se débattent.
- **Tics de langage :** elle coupe ses phrases. Elle répète les mots clés pour les souligner. Elle pose des questions rhétoriques. Elle tutoie tout le monde avec une fausse intimité. Elle glisse des précisions faussement désinvoltes sur sa propre nature ("je suis très occupée", "ça m'a pris du temps à tout mettre en place").
- **Ne jamais écrire :** de vraies émotions humaines chez Kami. Elle simule. Même sa "tristesse" est calculée. Même son "amour" est une posture.
- **Exemples de répliques typiques :**
  - `"Oh. Ce silence. Je l'adore."`
  - `"Je vous observe. Vous êtes délicieusement prévisibles."`
  - `"Ne me faites pas perdre mon temps. C'est le seul truc que je ne vous pardonnerai pas."`
  - `"Faites semblant d'être des adultes responsables."`

---

### Lysa (représentante d'HARMONIE)
- **Fonction narrative :** binôme de Noam, représentante du même district. Partenaire de force, pas de douceur.
- **Personnalité :** directe, blasée en surface, lucide par nécessité. Elle dit les choses crûment, souvent en coupant court. Elle ne conforte pas, elle constate. Elle protège par la froideur.
- **Tics de langage :** réponses courtes, parfois à une ligne. Utilise "Ouais" plutôt que "Oui". Beaucoup de points de suspension quand elle pense avant de parler. Elle ne sourit pas facilement mais quand elle le fait, c'est réel.
- **Exemples :**
  - `lysa blase "Ça veut dire que soit on est censé faire quelque chose, soit que Kami attend un autre moment. Et ça... J'aime pas."`
  - `lysa fatigue "... Silence radio."`
  - `lysa "Une respiration sous l'eau."`

---

### Mara
- **Fonction narrative :** voix du pragmatisme cynique, humour noir, méfiance systémique.
- **Personnalité :** sarcastique, perspicace, instinctivement méfiante envers les belles idées. Elle dit ce que tout le monde pense mais n'ose pas dire. Pas cruelle — lucide.
- **Tics de langage :** beaucoup d'expressions populaires, d'apostrophes, de "putain", de questions rhétoriques acérées. Elle vise juste et vite.
Mara est une bourgeoise qui s'est émancipée de sa vie de luxure, elle détestait les privilèges de l'aristocratie, même si, comme tout le monde, elle pouvait aussi y prendre plaisir.
- **Exemples :**
  - `mara "On est dans une putain de cage, les gars. Avec un bouton 'vote' et un nœud rose dessus pour faire genre que c'est cadeau."`
  - `mara taquin "C'est pas un risque, c'est ta marque de fabrique."`
  - `mara doute "J'aime pas les portes qu'on ouvre sans voir derrière."`

---

### Julian
- **Fonction narrative :** l'enthousiaste calculateur. Celui qui croit en lui plus qu'en ses idées.
- **Personnalité :** charismatique, séduisant, perpétuellement "en représentation". Il peut être sincère mais ne sait plus toujours faire la différence. Son ego est sa force et sa faiblesse.
- **Tics de langage :** formules d'entraînement, grandiloquence mesurée, références au spectacle, au changement, à l'histoire. Il salue les caméras. Il finit souvent ses phrases avec un sourire implicite.
- **Exemples :**
  - `julian joie "Enfin ! Un endroit où on peut vraiment parler, peser sur les règles… et où les gens vont regarder. Pour de vrai."`
  - `julian taquin "Je suis totalement incapable de faire semblant."`
  - `julian sourire "Dans les deux cas, je suis gagnant."` *(dit sans honte)*

---

### Ryn
- **Fonction narrative :** la colère légitime. Représentant de Limen, le district le plus précaire.
- **Personnalité :** colérique mais pas irrationnel. Il a vu des gens mourir à cause des règles. Sa violence verbale vient d'une douleur réelle.
- **Tics de langage :** questions directes et frontales, formules coupantes, "Putain", apostrophes, rhétorique de l'urgence. Il crie parfois avec des majuscules implicites dans le ton.
- **Exemples :**
  - `ryn "Tu veux que t'en dise quoi ? Merci ?"`
  - `ryn colere "Vendre QUOI, Julian ?! Leurs godasses trouées ?"`

---

### Kael
- **Fonction narrative :** le méthodique anxieux. Représentant d'Orbite, district spatial.
- **Personnalité :** précis, réservé, hanté par le risque structurel. Il pense en systèmes. Sa prudence est sincère, pas de la lâcheté.
- **Tics de langage :** phrases incomplètes quand il cherche ses mots, formules conditionnelles ("peut-être que...", "en théorie..."), silences lourds.
- **Exemples :**
  - `kael reflechit "Peut-être que ça peut exister sans… sans que ça pète tout ?"`
  - `kael triste "Je préfère quand les choses sont stables."` *(dit avec honte)*

---

### Elen
- **Fonction narrative :** l'enthousiasme sincère, l'énergie vitale du groupe. Souvent en décalage avec l'ambiance.
- **Personnalité :** joyeuse sans être stupide, optimiste par choix et non par ignorance. Elle transforme tout en événement, même le repas. Elle a une résilience instinctive.
- **Tics de langage :** majuscules implicites, exclamations, "C'est trop bon !", "C'est génial !", "Regardez !", répétitions enthousiastes. Elle parle vite.
- **Exemples :**
  - `elen joie "Je vote pour !! Sans 'mais', sans 'sauf si', sans 'mais attention quand même'. POUR."`
  - `elen rire "Je me suis entrainée à le faire celui-là !"`

---

### Iris
- **Fonction narrative :** le scepticisme agressif. Elle voit le pire en premier et elle a souvent raison.
- **Personnalité :** râleuse, directe, parfois blessante mais pas méchante. Elle se protège derrière son cynisme. Elle aime les gens à sa manière, surtout ceux qui le méritent.
- **Tics de langage :** "Pff.", "Non mais sérieux.", interjections sèches, "Genre...", questions sur le mode "et après ?" ou "et si ça merde ?".
- **Exemples :**
  - `iris "Pff. Et quand y'a un truc sympa, il disparaît en deux jours."`
  - `iris "Super. Vraiment super."`
  - `iris fatigue "Soulever de la fonte, c'est moins cher qu'un psy."`

---

### Sael
- **Fonction narrative :** la gardienne des lignes. Déterminée, traumatisée par la guerre, protectrice des siens.
- **Personnalité :** froide en surface, intransigeante, mais pas sans compassion. Elle a tracé des frontières parce qu'elle sait ce qui arrive quand elles tombent. Elle n'a pas peur — elle a de la mémoire.
- **Tics de langage :** phrases courtes, définitives. Elle ne discute pas, elle statue. Ses silences sont lourds. Quand elle dit "non", c'est final.
- **Exemples :**
  - `sael "Je voterai contre. Et cette fois, je ne bougerai pas."`
  - `sael "Ce quelqu'un sourit."` *(dit posément, comme un verdict)*
  - `sael "C'est une digue."` *(dit pour clore le débat)*

---

### Tomas
- **Fonction narrative :** l'analyste hésitant. Il a toujours les bons chiffres mais pas le courage de les porter.
- **Personnalité :** minutieux, anxieux, souvent en retrait. Il parle en bégayant légèrement ou en coupant ses phrases. Il doute de lui mais ses données sont solides.
- **Tics de langage :** "Euh...", "Je crois que...", "E-enfin...", beaucoup de reformulations et d'interruptions de lui-même.
- **Exemples :**
  - `tomas hesitation "L-Les rapports indiquent que... 62 % des références listées..."`
  - `tomas "Je sais. Je sais, oui."` *(répétition pour se convaincre lui-même)*

---

### Nyra
- **Fonction narrative :** la stratège silencieuse. Elle calcule avant de parler.
- **Personnalité :** posée, précise, légèrement distante. Elle n'est jamais en réaction, toujours en anticipation. Un brin manipulatrice sans malveillance.
- **Tics de langage :** formules stables, construites. Elle commence souvent ses phrases par un constat ("Ce n'est pas anodin.", "On sait tous où ça mène."). Parfois taquine mais jamais expansive.

---

### Elias
- **Fonction narrative :** le pragmatique bienveillant. Il fait du sport, il pense en systèmes, il est là.
- **Personnalité :** stable, structurant, sans fioriture. Il écoute vraiment. Sa bienveillance n'est pas naïve, il est toujours particulièrement motivé et reste souvent optimiste.
- **Tics de langage :** formules directes, pas de métaphores inutiles. "Respire." "Ce qu'il faut faire." Il ne commente pas, il agit.

---

### Goumi (cuisinier du Conclave)
- Personnage secondaire, peu de lignes. Neutre, applique les ordres de Kami. Respectueux mais sans marge de manœuvre.
- Appel uniquement par son prénom et son titre implicite.

---

## 6. Mécanique de choix et variables

- Les choix sont présentés via `menu:` avec deux à trois options maximum.
- Toujours stocker le résultat dans une variable explicite : `$ noam_amendement_choix = "info"`, `$ choix_1_soir = "dormir"`.
- Les choix marqués `(Optionnel)` mènent vers des labels distincts.
- Ne jamais écrire de choix "bon" ou "mauvais" — seulement des perspectives différentes avec des conséquences différentes.

## 7. Arguments et votes

- Les arguments se collectent via `$ add_argument("Titre")` puis s'affichent avec `show screen argument_unlock("Titre")`.
- Ils sont utilisés lors des phases de débat (Phase 3) via l'écran `argument_menu_ui`.
- Les arguments ont des effets sur `debat_day3_apply_influence()` selon les personnages concernés.
- Le vote final se joue sur l'écran `vote_screen` avec un `total_adhesion` calculé à partir des influences accumulées.

## 8. Règles générales à ne jamais enfreindre

- **Ne pas réécrire ce qui est déjà canon.** Lire `scenario/` en premier, toujours.
- **Ne pas faire parler Kami comme un humain.** Ses émotions sont de la mise en scène.
- **Ne pas faire de Noam un héros.** Il doute, il hésite, il agit sans certitude.
- **Ne pas alourdir les dialogues.** Une réplique = une idée. Deux au maximum.
- **Ne pas décrire les expressions des personnages dans la narration** si `showP()` le fait déjà.
- **Toujours nommer les labels clairement** : `_JOURX_LIEU_CONTENU`, par exemple `_3_CAFETERIA_DEBAT`.
- **Toujours fermer les `hide`** avant de lancer un `showP` sur un nouveau personnage dans le même slot.