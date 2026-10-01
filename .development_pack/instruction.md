# INSTRUCTIONS — Méthodologie d'écriture pour le jeu visuel

## À lire avant chaque session d'écriture

Avant d'écrire la moindre ligne de dialogue ou de narration, **lis l'intégralité des fichiers `.rpy` présents dans le dossier `scenario/`**. Ces fichiers sont la source de vérité : ils contiennent les événements canoniques déjà posés, l'état émotionnel des personnages, les choix du joueur et les flags de continuité. Tu ne peux pas écrire sans en avoir pris connaissance.

Chaque journée doit durer environ 10 à 15 minutes de jeu. Soit environ 1000 à 1500 lignes de code. Parfois plus.

---

## 1. Style d'écriture et voix narrative

### Doctrine d'écriture prioritaire — référence « V2 »

L'écriture doit d'abord fonctionner **comme une scène jouée**, pas comme une scène littéraire parfaitement contrôlée.

La priorité est, dans cet ordre :
1. **Engagement émotionnel immédiat**
2. **Conflit et friction entre les personnages**
3. **Oralité et personnalité**
4. **Rythme de lecture / rythme du clic**
5. **Clarté de l'information**
6. **Subtilité**

La subtilité reste utile, mais elle ne doit jamais rendre une scène froide, distante ou artificiellement retenue.

Une bonne scène de *Kami's Desires* doit donner l'impression que les personnages **réagissent avant d'avoir eu le temps de formuler parfaitement leur pensée**. Ils peuvent couper une phrase, jurer, se répéter, accuser trop vite, se reprendre, parler maladroitement ou dire quelque chose de trop frontal.

**Règle centrale : préférer une réplique vivante et imparfaite à une réplique élégante mais écrite.**

Exemple à éviter :
```
kael "Parce que nous ignorons encore ce qui s'est réellement produit et qu'une accusation prématurée pourrait avoir des conséquences."
```

Préférer :
```
kael "On sait même pas ce qui s'est passé ! Et si tu racontes ça maintenant, à ton avis ils vont soupçonner qui ?!"
```

### Conflit et friction

Les personnages ne doivent pas rester raisonnables simplement parce que le scénario exige qu'ils échangent des informations.

Quand la situation le justifie :
- ils s'agacent ;
- ils interrompent ;
- ils se défendent ;
- ils accusent ;
- ils comprennent mal ce que l'autre veut dire ;
- ils peuvent regretter immédiatement une phrase ;
- ils peuvent perdre temporairement leur calme.

Le conflit ne signifie pas que tout le monde crie en permanence. Il signifie que **les désaccords ont une texture humaine**.

Éviter les scènes où chacun attend son tour pour exposer proprement son point de vue.

### Information et mystère

L'information doit arriver **assez vite**. Ne jamais retarder artificiellement une information uniquement pour fabriquer du mystère.

En revanche, distinguer :
- **l'indice**, qui peut être donné frontalement ;
- **l'interprétation**, qui peut rester incertaine ;
- **la vérité**, qui ne doit pas être révélée avant le moment prévu.

Exemple :
- Bon : `"Accès mnésique."`
- Bon : `"Attends... ça parle de mémoire, là ?"`
- À éviter si ce n'est pas encore confirmé : `"Donc Kami nous efface la mémoire."`

Un personnage peut tirer une conclusion brutale ou fausse, mais le texte doit alors la présenter comme **sa réaction**, pas comme une vérité narrative.

### Émotions lisibles

Les émotions doivent être lisibles immédiatement à l'écran.

Ne pas compter uniquement sur le sous-texte, les silences ou une narration subtile pour faire comprendre qu'un personnage est terrifié, furieux ou blessé. Les sprites, les interruptions, le vocabulaire, les répétitions et la ponctuation doivent participer à la scène.

Une émotion forte peut produire :
- une répétition : `"J'ai cherché. Partout. PARTOUT."`
- un juron ;
- une phrase incomplète ;
- une accusation trop rapide ;
- une contradiction ;
- une réaction physique ou une action.

Les silences restent utiles, mais ils doivent **renforcer** l'émotion, pas remplacer systématiquement la réaction humaine.

### Voix du narrateur (Noam)

Noam reste le narrateur à la première personne, mais il ne doit pas devenir un observateur froid chargé de préserver le mystère.

Il est médiateur et rationnel, mais il est aussi directement impliqué. Quand la pression monte, sa pensée se désorganise : il peut jurer, répéter un fait, chercher ses mots, accuser trop vite ou s'accrocher à une conclusion parce qu'il a peur.

Sa narration doit alterner :
- constat concret ;
- réaction immédiate ;
- tentative de compréhension.

Il ne transforme pas chaque émotion en analyse psychologique.

Exemple :
```
"Je me rappelle être sorti pour chercher Kael."
"Je me rappelle l'avoir trouvé."
"Et après..."
think "Putain."
think "Y'a rien."
```

Noam peut reconstruire les faits lorsqu'il cherche à comprendre une incohérence, mais il ne doit pas parler en permanence comme un rapport d'enquête.

**Ce que Noam ne fait pas :**
- tirer des conclusions philosophiques sur ce qu'il vit ;
- décrire ses émotions avec précision clinique ;
- expliquer au joueur une conclusion que la scène vient déjà de rendre évidente ;
- rester constamment calme quand la situation justifie qu'il craque.

### Longueur des phrases et ponctuation

Les phrases doivent être **courtes à moyennes en moyenne**, mais ne pas tomber dans le hachage systématique.

Éviter l'ancien réflexe :
```
"Je marche."
"Je m'arrête."
"Un bruit."
"Je me retourne."
```

Préférer une phrase naturelle et rythmée :
```
"Je fais encore deux pas avant qu'un bruit derrière moi me fasse m'arrêter."
```

Les phrases très courtes servent aux chocs, aux ruptures, aux réactions ou aux informations qui doivent tomber sèchement. Si toutes les phrases sont courtes, plus aucune n'a d'impact.

Dans les dialogues, conserver les imperfections de l'oral :
- répétitions ;
- reprises ;
- mots inutiles naturels ;
- contractions ;
- jurons quand ils correspondent au personnage ;
- interruptions ;
- débuts de phrase abandonnés.

Les points de suspension `...` signalent une vraie hésitation, une phrase abandonnée ou un silence perceptible. Ils ne doivent pas devenir un tic décoratif.

Les exclamations et interrogations peuvent être fréquentes dans les scènes tendues. Ne pas les lisser artificiellement par peur d'être trop expressif.

### Ratio dialogues / narration

Le jeu est **très fortement dialogué**. Viser en général **80 à 90 % de dialogues** dans les scènes sociales, de conflit ou d'enquête.

La narration sert surtout à :
- donner une action que le sprite ne montre pas ;
- relier deux répliques ;
- poser une sensation immédiate de Noam ;
- gérer les transitions ;
- rendre un silence ou une incohérence perceptible.

Ne jamais utiliser la narration pour expliquer ce que les personnages viennent déjà de montrer.

Une révélation ou une dispute peut se jouer presque entièrement en dialogue. À l'inverse, une séquence d'exploration peut contenir davantage de narration si le joueur est seul. Ce qui compte est le rythme de jeu, pas un quota mécanique.

---

### Le registre instable — la règle du décalage

**Ne jamais laisser le registre se stabiliser trop longtemps.**

C'est la règle la plus difficile à appliquer et la plus importante. Une conversation sérieuse peut se couper sur une réplique absurde. Une blague peut arriver exactement là où le drame venait de poser quelque chose de lourd. Ce n'est pas de l'humour pour détendre — c'est de l'humour qui **déstabilise**, qui empêche le joueur de savoir exactement où il en est.

L'humour n'annonce jamais le drame. Le drame n'annonce jamais l'humour. Ils coexistent sans s'expliquer mutuellement.

**Ce que le décalage n'est pas :** une blague placée pour "alléger". Si la blague arrive pour soulager la tension, elle est mal placée. Elle doit arriver pour la couper net, sans prévenir.

---

### Caractérisation par le langage, pas par la description

**On ne dit pas comment un personnage est. On le laisse parler, réagir et se heurter aux autres.**

Chaque personnage doit avoir une voix suffisamment marquée pour rester identifiable sans son nom. La différence ne vient pas seulement du vocabulaire : elle vient aussi de la manière de réagir sous pression.

Ne pas chercher à rendre tous les personnages subtils de la même façon. Certains verbalisent beaucoup, d'autres se ferment, d'autres attaquent, d'autres plaisantent.

La narration de Noam décrit d'abord ce qu'il voit et ce qui lui saute aux yeux. Elle peut constater une émotion évidente ("Kael est furieux", "Sael a l'air paniquée") si cela accélère la lecture ; inutile de transformer chaque émotion en énigme à décoder.

**Priorité : lisibilité émotionnelle avant élégance du sous-texte.**

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

### Affichage des personnages — règle obligatoire

- **Dès qu'une scène contient un dialogue entre plusieurs personnages, utiliser `showGroup()` avant le premier échange.**
- Exceptions uniquement :
  - Noam est seul à l'écran ;
  - une seule autre personne parle avec Noam et la mise en scène utilise volontairement un affichage individuel ;
  - une CG est affichée et remplace volontairement les sprites ;
  - une diffusion de Kami est active sur `bg_diffusion_*`.
- **Après tout `scene` qui revient d'une diffusion, d'une CG ou d'un changement de décor, considérer les sprites comme effacés et rappeler `showGroup()` avant que plusieurs personnages recommencent à parler.**
- Ne jamais laisser plusieurs personnages dialoguer plusieurs lignes sur un décor ordinaire sans groupe visible.

### Expressions de dialogue — obligatoire

- **Chaque réplique prononcée par un personnage affiché par sprite doit préciser explicitement une expression après son nom** : par exemple `iris fatigue "..." `, jamais simplement `iris "..."`.
- **L'expression utilisée doit exister réellement pour ce personnage dans `game/images.rpy`.** Ne jamais inventer un nom d'expression en se fiant à l'intuition ; vérifier la déclaration `image personnage expression = ...` avant de l'utiliser.
- Avant de valider ou commit une nouvelle journée, faire un contrôle complet du fichier : aucune ligne de dialogue de personnage ne doit rester sans expression, et aucune expression ne doit être absente de `images.rpy`.
- Exceptions : le narrateur anonyme, `think`, et Kami pendant une diffusion utilisant les décors `bg_diffusion_*`, puisque son expression est alors portée par le décor de diffusion et non par un sprite de personnage.

### Fidélité des voix — contrôle avant validation

- Avant d'écrire ou de réviser une scène sociale importante, relire les fiches des personnages réellement présents dans `.development_pack/character.txt`.
- Vérifier que chaque personnage agit selon sa manière habituelle de gérer la situation, pas seulement selon ce dont l'intrigue a besoin.
- **Mara** doit rester provocatrice, corporelle, volontiers sexualisée et un peu beauf ; ne pas la transformer en simple sarcastique propre.
- **Iris** protège en râlant, mais ne doit pas systématiquement couper Mara ou devenir la police morale de la table. Elle peut laisser une vanne vivre, répondre sèchement, puis intervenir seulement quand Noam en a réellement besoin.
- **Julian** aime la scène, l'enthousiasme, la visibilité et l'effet produit. Quand il adhère à une cause, il doit pouvoir devenir franchement enjoué, triomphant et démonstratif plutôt que négocier timidement la durée de son discours.
- **Elias** reste concret, bref et populaire ; il ne cherche pas à devenir porte-parole d'un texte ni à revendiquer publiquement un rôle politique si rien dans la scène ne l'y pousse.
- Si plusieurs personnages pourraient prononcer une même réplique sans qu'elle change beaucoup, retravailler la ligne jusqu'à ce que la voix soit identifiable.

### Règles de continuité visuelle, logistique et distribution du casting

Ces règles sont obligatoires pour éviter les scènes qui paraissent fabriquées pour le scénario plutôt que vécues par le groupe.

- **Une scène de groupe continue ne doit pas multiplier les `showGroup()` sans nécessité.** Si plusieurs personnages participent à la même scène dans le même lieu, préparer dès le départ un seul groupe contenant tous les intervenants prévus. Ne recréer un groupe que si la composition change réellement.
- **Quand un personnage quitte physiquement une scène, son sprite doit quitter l'écran avec lui.** Utiliser de préférence le comportement naturel de `showGroup()` en rappelant le groupe sans ce personnage : le helper joue déjà `char_group_exit`. Ne jamais écrire « X part » tout en le laissant affiché.
- **Avant de créer une nouvelle mécanique, vérifier si un mini-jeu existant correspond déjà à l'action.** Exemple : pour trier ou ranger une livraison, réutiliser `call rangement_play` au lieu de résumer l'action en quelques lignes si le contexte s'y prête.
- **Ne pas inventer de capacités de suivi aux systèmes du Conclave.** Pour les livraisons, les registres savent ce qui a été commandé automatiquement et ce qui figure comme arrivé. Ils ne suivent pas ensuite la position interne de chaque objet et ne disposent pas d'un historique magique de « transferts internes ».
- **Ne pas surutiliser artificiellement deux ou trois personnages parce qu'ils sont utiles à l'intrigue du jour.** Avant validation d'une journée de groupe, vérifier que plusieurs représentants apparaissent naturellement dans les scènes collectives, même brièvement. La présence doit venir du contexte : sas, repas, livraison, couloir, aide ponctuelle, réaction à une annonce.
- **Un personnage peut être plus présent sans devenir le centre de chaque scène.** Si Elias porte une intrigue technique, d'autres peuvent transporter, commenter, aider une minute, repartir, ou simplement réagir. Le groupe doit continuer à donner l'impression d'exister hors du fil narratif principal.
- **Éviter les formulations "écrites" qui sonnent comme des bons mots préparés.** Préférer des phrases qu'une personne dirait réellement sous pression. Si une métaphore ou une vanne paraît trop construite ("miser sur un départ propre", "se transformer en panneau lumineux", etc.), la remplacer par une formulation plus simple, directe et orale.
- **Quand un personnage ne soupçonne rien, ne lui faire produire aucune réplique qui fabrique artificiellement du soupçon.** Un personnage peut constater qu'une situation est bizarre, aider à chercher ou être blasé sans devenir enquêteur.

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

`bg_diffusion_neutre` est interdit dans les scénarios : il s'agit du plateau vide, sans Kami. Toujours choisir une expression visible de Kami.

Si un autre personnage parle pendant qu'un décor `bg_diffusion_*` est actif, afficher son portrait avec `$ bc_show("nom", "expression")` juste avant son bloc de répliques, puis appeler `$ bc_hide()` juste après. Pour un échange prolongé entre représentants, interrompre la diffusion, revenir au décor du lieu et utiliser le trio dynamique ; la diffusion ne reprend que lorsque Kami reparle.

Règle d'or : **Kami ne fait jamais une seule chose**. Elle informe ET provoque, elle félicite ET menace, elle joue ET calcule. Chaque diffusion doit contenir au moins une ambivalence.


### RÈGLES BLOQUANTES — ÉCRIRE KAMI SANS DÉRIVER

Ces règles sont **obligatoires** et doivent être vérifiées avant toute nouvelle scène où Kami intervient.

1. **Avant d'écrire une seule réplique de Kami, relire au minimum deux diffusions existantes dans les scénarios déjà écrits**, de préférence une ancienne (J1/J2) et une récente. Ne jamais écrire sa voix de mémoire uniquement.
2. **Kami ne doit jamais être réduite à une IA fonctionnelle qui donne une information brute.** Une annonce pratique ("la navette arrive", "il reste deux heures", "le vote commence") doit presque toujours être accompagnée d'une provocation, d'une plaisanterie, d'une fausse sollicitude, d'une humiliation légère, d'une menace souriante ou d'une remarque sur les représentants.
3. **Toute diffusion visuelle de Kami doit utiliser le protocole complet du jeu :**
   ```renpy
   play sound sfx_announce
   stop music fadeout 0.5
   scene bg_diffusion_EXPRESSION at adaptive_fullscreen with fade
   show screen kami_broadcast_ui
   play music "music/bgm_system_override.mp3" fadein 0.8

   kami "..."

   scene bg_diffusion_AUTRE_EXPRESSION at adaptive_fullscreen with dissolve
   kami "..."

   hide screen kami_broadcast_ui
   stop music fadeout 0.8
   scene bg_LIEU at adaptive_fullscreen with dissolve
   ```
   L'ordre exact peut varier selon la scène, mais **on ne laisse pas Kami parler sur un décor ordinaire comme une simple voix système** si la scène est une diffusion.
4. **Alterner les `bg_diffusion_*` au cours d'une même intervention.** Une diffusion de plusieurs répliques avec une seule expression est considérée comme incomplète, sauf micro-intervention volontaire d'une seule phrase.
5. **L'expression doit commenter le ton de la réplique.** Exemples usuels :
   - `taquin` : moquerie, provocation, fausse proximité ;
   - `professeur` / `einstein` : explication volontairement pédagogique ou condescendante ;
   - `fier` / `champagne` : autosatisfaction, annonce spectaculaire ;
   - `colere` : irritation théâtrale, menace, rappel à l'ordre ;
   - `zen` : cruauté calme, faux apaisement ;
   - `triste` / `desespoir` / `gene` / `amour` : émotions jouées, jamais sincères.
6. **Kami change fréquemment de registre dans la même diffusion.** Elle peut commencer chaleureuse, devenir professorale, lancer une pique, puis terminer par une menace. Cette instabilité fait partie de sa voix.
7. **Kami tutoie, infantilise et personnalise.** Elle aime "mes petits représentants", les questions rhétoriques, les surnoms ou les observations sur leur comportement. Elle réagit à ce qu'ils viennent de faire au lieu de réciter un communiqué.
8. **Une diffusion correcte doit contenir au moins une ligne qui ne serait pas nécessaire à la transmission de l'information.** Cette ligne existe uniquement parce que Kami aime commenter, jouer avec eux ou les provoquer.
9. **Ne pas utiliser `bg_diffusion_neutre` dans un scénario.** Il représente le plateau vide.
10. **Si un représentant parle pendant la diffusion**, utiliser `$ bc_show(...)` / `$ bc_hide()`, ou revenir temporairement au décor réel si l'échange devient long.
11. **Avant validation d'une scène de Kami, faire ce contrôle :**
    - UI de diffusion présente ?
    - au moins deux expressions si l'intervention dépasse quelques lignes ?
    - information + provocation ?
    - voix taquine/personnelle identifiable ?
    - réaction au contexte immédiat ?
    - retour propre au décor après `hide screen kami_broadcast_ui` ?
    Si une réponse est "non", la scène doit être corrigée avant commit.

**Anti-exemple interdit :**
```renpy
kami "LE VAISSEAU ARRIVERA À QUATORZE HEURES."
kami "LE DÉPART EST PROGRAMMÉ À SEIZE HEURES."
```

Même si l'information est correcte, cette version ne ressemble pas à Kami.

**Exemple de logique correcte :**
```renpy
scene bg_diffusion_taquin at adaptive_fullscreen with fade
show screen kami_broadcast_ui
kami "Bonne nouvelle, mes chers représentants : votre taxi arrive à quatorze heures."

scene bg_diffusion_fier at adaptive_fullscreen with dissolve
kami "Et puisque je sais à quel point vous mourez d'envie de me quitter, le départ est fixé à seize heures."

scene bg_diffusion_colere at adaptive_fullscreen with dissolve
kami "Essayez simplement de ne perdre ni votre badge, ni votre dignité d'ici là."
```


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
- **Fonction narrative :** l'observateur calme qui supporte mal qu'on décide ou qu'on accuse à sa place.
- **Personnalité :** réservé et réfléchi au quotidien, mais sa retenue n'est pas infinie. Sous pression, il peut devenir brusquement direct, hausser le ton, répéter ce qu'il vient de dire ou exploser après avoir trop encaissé.
- **Tics de langage :** peu de mots quand il contrôle la situation ; phrases plus directes et plus nues lorsqu'il est blessé. Les silences existent, mais ne doivent pas l'empêcher de réagir avec force quand c'est justifié.
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
- **Fonction narrative :** la gardienne des traditions et de la survie, profondément méfiante envers le progrès et les changements imposés.
- **Personnalité :** brute, concrète, attachée aux rites et aux habitudes. Elle peut être froide, mais elle n'est pas un distributeur de verdicts. Elle s'agace, cherche, râle, panique parfois et peut laisser sortir une réaction beaucoup plus humaine que son image austère ne le laisse croire.
- **Tics de langage :** langage simple, sec, parfois presque archaïque ; images liées au corps, au froid, aux marques, au feu et aux rites. Elle peut lâcher un "Raaah", un juron ou une phrase spontanée lorsqu'elle perd patience. Ses phrases définitives restent réservées aux moments où elle tranche réellement.
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
- **Fonction narrative :** le débrouillard manuel. Celui qu'on appelle quand quelque chose casse, fuit, brûle ou coince.
- **Personnalité :** compétent avec ses mains mais maladroit, concret, populaire, souvent fataliste. Il a appris à réparer parce qu'il n'avait pas le choix et se voit encore facilement comme "le gars qui se tape le sale boulot".
- **Tics de langage :** vocabulaire simple, cru, parfois vulgaire. Il ne parle pas comme un ingénieur et ne fait pas de diagnostic technique élégant. Il dit "c'est pété", "ça coince", "faut démonter", "file-moi ça". Quand il se plante, il jure. Quand on lui demande d'expliquer, il simplifie.

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

## 7 bis. Roadmap — synchronisation obligatoire

- **Toute nouvelle journée ajoutée au jeu doit être ajoutée immédiatement à `game/roadmap/roadmap_menu.rpy` dans le même travail.**
- **Tout nouveau choix majeur, nouvelle divergence de route, nouveau vote, nouvelle scène importante ou nouvelle fin doit également être ajouté immédiatement à la roadmap.**
- Ne jamais considérer une journée, une branche ou un choix comme terminé tant que son nœud roadmap n'existe pas et ne pointe pas vers le bon label.
- Lors de l'ajout d'un nœud, renseigner au minimum : `id`, `title`, `short`, `label`, `category`, `kind`, `x`, `y`, `summary`, `choice`, `consequence`, `requires`, `required_variables` si nécessaire, et `teleportable`.
- Vérifier que les dépendances `requires` correspondent réellement à la branche qui mène au nouveau contenu et que les variables de téléportation placent le jeu dans l'état attendu au début de la scène.

### Transitions de fin de journée et fluidité des scènes

- **Si Noam se couche, s'endort, ferme les yeux pour dormir ou si la scène implique explicitement une nuit complète avant le lendemain, appeler `end_day(..., sleeping=True)`.** Le mode sans `sleeping=True` est réservé aux transitions où Noam reste conscient et où le changement de jour se fait sans ellipse de sommeil.
- **Éviter le ping-pong de micro-répliques.** Une conversation naturelle ne doit pas devenir une suite mécanique de phrases d'une demi-ligne où chaque personnage répond immédiatement au précédent. Laisser parfois un personnage développer deux idées dans la même réplique, hésiter, se reprendre, être interrompu en cours de phrase ou ne pas obtenir de réponse.
- **L'oralité ne signifie pas des phrases systématiquement courtes.** Les personnages peuvent parler en phrases plus longues, imparfaites, avec des reprises, des "enfin", "bah", "je sais pas", des corrections et des fragments. Chercher la respiration d'une vraie conversation plutôt qu'un rythme de punchlines.
- **La narration doit toujours faire avancer une action, un déplacement, une perception ou une décision.** Si plusieurs paragraphes successifs répètent la même émotion ou la même information sans nouveau fait, condenser.
- **Avant chaque scène, identifier ce qui doit avoir changé à la fin.** Si l'état narratif est identique après plusieurs échanges, la scène tourne probablement en rond et doit être raccourcie ou réorientée.

## 8. Règles générales à ne jamais enfreindre

- **Ne pas réécrire ce qui est déjà canon.** Lire `scenario/` en premier, toujours.
- **Ne pas faire parler Kami comme un humain.** Ses émotions sont de la mise en scène.
- **Ne pas faire de Noam un héros.** Il doute, il hésite, il agit sans certitude.
- **Ne pas alourdir les dialogues**, mais ne pas les aseptiser non plus. Une réplique peut contenir plusieurs fragments, répétitions ou reprises si cela sonne comme une vraie réaction orale.
- **Préférer l'énergie à l'élégance.** Une formulation imparfaite, vive et caractérisée vaut mieux qu'une phrase trop propre.
- **Ne pas retarder artificiellement une information.** Le mystère vient de ce qu'on ignore encore, pas du fait que les personnages refusent de dire ce qu'ils savent.
- **Ne pas confondre mystère et mutisme.** Les personnages peuvent formuler des hypothèses franches ; elles restent des hypothèses tant que le scénario ne les confirme pas.
- **Faire exister les désaccords.** Si deux personnages ont de bonnes raisons de s'opposer, écrire la friction au lieu de résumer calmement leurs positions.
- **Ne pas hacher systématiquement la narration.** Réserver les phrases ultracourtes aux impacts et aux ruptures.
- **Ne pas décrire les expressions des personnages dans la narration** si `showP()` le fait déjà.
- **Toujours nommer les labels clairement** : `_JOURX_LIEU_CONTENU`, par exemple `_3_CAFETERIA_DEBAT`.
- **Toujours fermer les `hide`** avant de lancer un `showP` sur un nouveau personnage dans le même slot.
