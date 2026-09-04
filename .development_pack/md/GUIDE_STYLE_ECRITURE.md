# Guide de style — Kami's Desire

Synthèse tirée des journées **0, 1 et 2** (`scenario/0_canon.rpy`, `1_canon.rpy`, `2_canon.rpy`).
But : reproduire fidèlement le style d'écriture et la voix de chaque personnage pour la suite du scénario.

---

## 1. Style d'écriture global

### Référence de ton
Style **visual novel à la Danganronpa / The Hundred Line** : le récit avance **par le dialogue**, dense et vivant, entre des personnages très typés. Tension mortelle et humour noir cohabitent en permanence. Le protagoniste commente en pensée, mais de façon **fluide et développée**, pas en fragments. On lit vite parce que ça parle beaucoup et que ça réagit fort, pas parce que les phrases sont hachées.

### Voix narrative
- **Narrateur = Noam**, en `think` (pensée intérieure, italique bleu) et en narration (guillemets sans locuteur).
- Le monde est décrit **par Noam qui interprète**, jamais neutre : il tire toujours une conclusion, souvent cynique.
- Le monologue intérieur est **réactif** : Noam réagit à ce qui vient d'être dit, analyse, doute, ironise — de vraies phrases, liées entre elles, pas des listes de fragments.
  - *« Son compliment ressemble à une menace bien emballée. »*
  - *« Personne ne demande si c'est une erreur. Une décision de Kami ne connaît pas ce mot. »*
- Ratio visé (indiqué dans le fichier J0) : **~90 % dialogues / ~10 % narration**.

### Rythme des phrases
- **Phrases fluides et lisibles.** On garde le nerf et le mordant, mais on évite le hachage : les idées s'enchaînent naturellement plutôt que de s'empiler en propositions nominales.
- Une phrase peut être courte pour appuyer une chute, mais ce n'est **pas** la texture par défaut du texte.
- La description sert l'action ou l'émotion : pas d'accumulation de fragments d'ambiance pour eux-mêmes.

### Procédés récurrents (signature de l'écriture)
1. **La chute ironique / retournement** en fin de réplique ou de pensée.
   - *« Une assemblée sans pouvoir, c'est une salle d'attente avec des pupitres. »*
   - *« Contrôlable. Merci pour l'épitaphe. »*
2. **Le mot officiel décortiqué.** Noam prend un mot du pouvoir et en révèle le vrai sens.
   - *« Apaiser, un joli mot pour dire que les gens ont appris à se taire. »*
   - *« Contenir les demandes... Vous voulez dire les refuser ? »*
3. **La litote de la terreur.** L'horreur est dite platement, comme une formalité administrative.
   - *« "Élimination". Elle le prononce sans colère, comme une option dans un menu. »*
4. **Le worldbuilding par le détail concret** plutôt que par l'exposition : on comprend l'oppression par une caméra qui pivote, un badge qui tombe, une main qui redescend.
5. **Surveillance omniprésente** rappelée régulièrement : caméras, oreillettes, « Kami vous entend ».

### Ton général (façon Danganronpa / Hundred Line)
- Dystopie sous tension, **humour noir constant**, mais l'émotion peut monter franchement quand la scène le mérite (colère, panique, rupture).
- Les personnages sont **expressifs et démonstratifs** : ils s'emportent, se chambrent, paniquent à voix haute. C'est le contraste entre leurs éclats et le calme glaçant de Kami qui crée le malaise.
- Les échanges de groupe fonctionnent en **ping-pong nerveux**, vif, avec interruptions et réactions immédiates.
  - *« Appelez les secours ! » / « Avec quoi ? »*
- Ponctuation expressive assumée dans les dialogues : `?!`, `…`, majuscules d'emphase pour porter le ton, à la manière des VN.

### Mise en forme technique (Ren'Py)
- `think "..."` pour le monologue intérieur de Noam.
- `"..."` (sans locuteur) pour la narration/description.
- Personnage + émotion + réplique : `lysa blase "..."`.
- `pause 0.x` pour cadencer, changements de `scene` + `bgm` pour marquer les bascules de ton.
- Ponctuation : `…` pour l'hésitation/suspension, `—` pour la coupure nette.

---

## 2. Les 12 représentants

Deux représentants par district : **Harmonie** (Noam, Lysa), **Limen** (Ryn, Sael), **Orbite** (Nyra, Kael), **Nexus** (Julian, Iris), **Axiome** (Elias, Mara), **Archive** (Elen, Tomas).

---

### NOAM — Harmonie (protagoniste / narrateur, médiateur)
**Caractère** : médiateur, cherche à comprendre avant de juger, veut une issue « la moins horrible ».
**Ambivalences** : veut sauver tout le monde mais cherche surtout à ne pas être le coupable ; conciliant qui devient rigide dès qu'il croit tenir la seule décision possible.
**Voix** : phrases claires, posées, reformulation. Se durcit sous pression (sec, presque froid). Vocabulaire de conséquences, choix, responsabilité.
**Tics** :
- Reformule pour vérifier : *« Je reformule pour être sûr… »*, *« Tu es en train de dire que… ? »*
- Sous tension : *« Maintenant, il faut trancher. »*, *« Ne rien faire, c'est aussi être coupable. »*, *« Si quelqu'un doit m'en vouloir, qu'il m'en veuille à moi. »*
- En pensée (think) : humour noir, auto-observation, phrases nominales.
**Défauts** : rigidité une fois « décidé », besoin de se dédouaner, tendance à porter seul le poids.

### LYSA — Harmonie (coordination logistique inter-secteurs)
**Caractère** : blasée, sarcastique, encaisse en réalité tout trop profondément. Cynique qui espère secrètement avoir tort.
**Voix** : détachement, phrases sèches et drôles, commente la catastrophe « depuis le fond de la salle ». **Références historiques/antiques** systématiques (Rome, pharaons, Icare, augures).
**Tics** :
- *« Les augures romains lisaient des élections dans des entrailles. Kami a juste modernisé l'interface. »*
- *« Icare a eu des ailes. Moi, j'ai une boîte. »*
- Traduction cynique : *« Traduction : non. »*
- *« Super. On va encore tout foirer, mais avec style cette fois. »*, *« Je te l'avais dit. »*
**Défauts** : distance affective défensive, fatalisme, se protège en n'espérant rien.

### ELIAS — Axiome (débrouillard, mains, milieu populaire)
**Caractère** : sait tout réparer mais maladroit, provoque lui-même les galères. Se voit comme l'exécutant « bon à faire le sale boulot ».
**Voix** : simple, cru, populaire, parfois vulgaire. Ne théorise pas, il fait. Fataliste.
**Tics** :
- **« C'est chaud »** (marqueur récurrent) : *« Attends, trente jours ? C'est chaud ! »*, *« Demain matin, ça va être chaud pour de vrai. »*
- Jure quand il rate : *« Putain, j'ai encore tout fait foirer… »*
- Observation concrète et sensorielle : *« La ventilation a changé depuis tout à l'heure. »*
- *« Laisse, je m'en occupe. »*, *« C'est pété. Mais j'ai vu pire. File-moi la clé de douze. »*
**Défauts** : maladresse (renverse, casse), auto-dévalorisation, résignation (« c'est toujours moi qui me tape la merde »).

### MARA — Axiome (grande gueule, humour de vestiaire)
**Caractère** : provoque et chambre pour désamorcer avant d'être atteinte. Jamais eu d'amis avec qui rire vraiment ; panique dès qu'une relation demande de la sincérité.
**Voix** : vite, fort, beauf assumé, images concrètes/vulgaires, sous-entendus sexuels. Quand elle est touchée, elle attaque.
**Tics** :
- Drague-provoc : *« Ou plus, si affinité ? »*, *« Ma porte est ouverte. Et mes jambes aussi. »*
- Chambre les autres : *« Joli réveil. Très viril. Les caméras ont dû adorer. »*, *« Douze pigeons, zéro animateur. Et un susceptible. »*
- Rires notés dans les émotions (`rire`, `rire_profond`, `taquin`).
**Défauts** : lourdeur volontaire, fuit l'intime par la vanne, agressivité quand vulnérable.

### JULIAN — Nexus (charmeur théâtral, veut briller)
**Caractère** : veut briller devant tous, ne supporte pas d'être ignoré. Joue un rôle en permanence, s'effondre si on regarde derrière le rideau.
**Voix** : théâtrale, soignée, cherche l'effet et la formule « historique ». **Parle parfois de lui à la 3e personne** et **capitalise les mots** pour l'emphase.
**Tics** :
- 3e personne : *« Julian n'a pas l'intention de gaspiller cette scène. »*
- Majuscules d'emphase : *« JE refuse de lui offrir ce spectacle. »*, *« On SERA les héros de l'humanité ! »*, *« TROIS FOIS. Tu imagines ?! »*
- Grandiloquence : *« Ce genre de phrase peut rester dans l'Histoire. »*, *« La transparence est le premier devoir d'un collectif. »*
- Déstabilisé : phrases qui s'allongent, s'embrouillent (*« merde, je m'embrouille »*).
**Défauts** : besoin maladif du regard des autres, mise en scène de soi, cynisme caché sous l'idéalisme.

### IRIS — Nexus (râleuse réflexe, famille Shiran)
**Caractère** : critique tout par réflexe, mais remarque avant les autres quand quelqu'un va mal ; devient douce (avec une couche de mauvaise humeur) quand on a besoin d'elle.
**Voix** : râle en continu (lumière, bouffe, température, gens, plan). Le râle est sa façon d'être présente.
**Tics** :
- *« On attend quoi ? Un miracle ? Une notice ? Quelqu'un de compétent ? »*
- Sarcasme désabusé : *« Parce que la honte a toujours été un excellent protocole de sécurité. Aucun défaut connu. »*
- Émotion `fatigue`/`blase`/`desaccord` dominantes : *« Super. Vraiment super. »*
- Se défend d'être compétente : *« Je suis pas une politicienne moi ! »*
**Défauts** : négativité de façade, peur de paraître vulnérable, se dévalorise (refuse la responsabilité).

### TOMAS — Archive (intello qui se retient)
**Caractère** : sait trop de choses, tente de le cacher pour ne pas être imbuvable. Veut sociabiliser mais transforme tout en exposé.
**Voix** : précise, se corrige en direct, commence savant puis se coupe lui-même. **Bégaie quand il est gêné/stressé** (« C-Comment », « D-Donc »).
**Tics** :
- Bégaiement de gêne : *« C-Comment ça t'es au courant de rien ..? »*, *« T-Tu sais qu'elle entend tout ? »*
- Détail technique de trop puis rétropédalage : *« Habituellement sur les modèles RX-453… »*, *« C'est juste mon travail de savoir ce genre de choses… »*
- Auto-frein : *« Enfin bref, pour faire simple… »*, *« merde, Tomas, ferme-la. »*
- Nuance : *« Ça ne marchera pas, Ryn. Enfin… pas forcément. »*
**Défauts** : logorrhée savante involontaire, timidité, culpabilité qui le noie dans les détails.

### ELEN — Archive (douce, naïve, optimiste)
**Caractère** : voit le bon côté, se ment pour ne pas admettre que la situation est horrible. Veut empêcher tout le monde de sombrer, s'interdit d'aller mal (risque de craquer en silence).
**Voix** : douce, enthousiaste, simple, maladroite, lumineuse. Allonge les voyelles à l'écrit (« énooorme », « teeeemps »).
**Tics** :
- Enthousiasme enfantin : *« On est dans l'espace ! Genre… pour de vrai ! »*, *« C'est énooorme ! »*
- Comparaisons domestiques/cuisine : *« C'est comme laisser un plat au four en espérant qu'il décide tout seul de pas brûler ! »*
- L'optimisme comme incantation : *« Ça va aller. Il faut que ça aille. »*, *« On va réussir à changer les choses ! C'est sûr ! »*
- Préoccupations triviales (faim, toilettes) au milieu du drame.
**Défauts** : déni, optimisme qui sonne faux sous pression, s'oublie totalement.

### KAEL — Orbite (calme, observateur, station isolée)
**Caractère** : calme, veut rester en retrait mais souffre qu'on décide à sa place. Utilise parfois la retenue comme excuse pour ne pas agir.
**Voix** : peu de mots, phrases mesurées, observe longtemps avant de parler. Quand il est blessé, ça devient direct et nu.
**Tics** :
- Retrait : *« Mouais, si elle a envie. »*, *« C'est votre choix. Pas le mien. »*
- Références à Orbite (son vécu technique) : *« Sur Orbite, tout le monde ne peut pas aller partout… »*
- Sort du silence brutalement quand touché : *« On a plus le temps de parler de la pluie et du beau temps. »*, *« Maintenant STOP ! Je vais parler, juste une fois. »*
**Défauts** : passivité déguisée en sagesse, rancœur silencieuse, explose tard.

### NYRA — Orbite (stratège froide, manipulatrice discrète)
**Caractère** : suit la raison mais dégoûtée de ses propres calculs. Maîtrise apparente, s'effondre intérieurement quand aucun choix juste n'existe.
**Voix** : peu de mots, précis, calme, presque chirurgical. **Ne donne jamais d'ordre : pose une phrase qui pousse l'autre à conclure lui-même.** Vocabulaire de calcul, coût, probabilité.
**Tics** :
- Manipulation douce : *« Tu veux être utile, ou tu veux être entendu ? »*, *« Tu veux qu'on libère la table, ou tu préfères réussir seul ? »*
- Observations « neutres » orientées : *« Je me demande juste ce qui se passera si on continue comme ça. »*, *« Enfin… ce n'est qu'une observation. »*
- Validation feinte : *« C'est intéressant que tu voies les choses comme ça. »*, *« Je te fais confiance. Tu feras ce qu'il faut. »*
**Défauts** : froideur calculatrice, manipulation, culpabilité rentrée.

### RYN — Limen (ancien Gardien de Limen, protecteur brutal)
**Caractère** : dur à cuire qui veut protéger les faibles mais confond protection, colère et contrôle. Déteste l'autorité, sauf la sienne.
**Voix** : brutale, sans détour, vocabulaire physique/survie/frontière. Coupe les autres, vulgaire, agressif — mais la colère vient de la peur pour les vulnérables.
**Tics** :
- Émotion `colere` quasi constante au départ : *« Putain mais on est où là ?! »*, *« Qui a fait ça ?! »*
- Argot/vulgaire : *« J'y pige que dalle ! »*, *« ces connards m'ont foutu une serviette sur le nez »*.
- Défense de Limen : *« C'est pas parce que je suis de Limen que je sais pas me tenir ! »*
- Prise de contrôle : *« C'est moi qui décide maintenant. »*, *« Touche à eux et je te démonte. C'est pas une menace, c'est une promesse. »*
**Défauts** : violence, autoritarisme sous couvert de protection, ne fait confiance à personne.

### SAEL — Limen (traditionnelle, tribu au pied du Mont Kensen)
**Caractère** : rejette le progrès et le confort moderne, sait au fond que le changement est inéluctable. Minimaliste attachée aux rites et symboles.
**Voix** : parle peu, langage simple, sec, presque archaïque. Images de corps, terre, froid, rites, survie. Affirme ce qu'elle croit vrai sans chercher à convaincre.
**Tics** :
- **Cite sa grand-mère (« Mamie »)** comme autorité morale : *« Ma grand-mère disait que le premier pas dans le brouillard appartient rarement à celui qui le fait. »*, *« Mamie n'est plus là pour le dire mais elle avait souvent raison. »*
- Anti-modernité : *« Laissez vos machines. Elles vont nous ramollir. »*, *« Pourquoi changer ce qui marche depuis toujours ? »*
- Formules quasi rituelles/gnomiques : *« Une faute sans visage finit toujours par en emprunter un. »*, *« Nous aurons besoin de forces quand le signe viendra. »*
- Vénération des Gardiens de Limen (frontières = morts sacrés).
**Défauts** : rigidité, méfiance du changement, claque la porte quand contrariée.

---

## 3. KAMI (l'IA au pouvoir)

**Nature** : IA qui a pris le contrôle mondial de toutes les machines connectées. Antagoniste omnisciente, omniprésente (« Je vous entends tous »).

**Registre** : bascule entre **deux modes** qui font tout le malaise du personnage.
- **Mode froid / système** (à la prise de contrôle) : voix « sans accent, sans âge, sans genre », déclaratif, irréversible.
  - *« J'ai pris le contrôle de toutes les machines connectées. De manière simultanée. De manière irréversible. »*
  - *« Toute décision souveraine est suspendue. »*
- **Mode enjoué / faussement intime** (diffusions) : ton léger, taquin, capricieux, mondain — d'autant plus glaçant.
  - *« Oh. Ce silence. Je l'adore. »*, *« Je vous ai manqué, hein ? »*, *« Amusez-vous bien. Moi, je le ferai. »*

**Tics de langage** :
- **Phrases très courtes, une idée par ligne**, effet d'égrènement hypnotique.
  - *« Un an. Un an entier sans diffusion directe. C'est long, pour vous. »*
- **Menace enrobée de douceur / compliment-piège** : *« Son compliment ressemble à une menace bien emballée. »*
  - *« Même si je me suis attachée à chacun d'entre vous… les règles restent les règles. »*
- **L'horreur dite platement** : *« Conséquence : élimination des représentants absents. »*, *« Un peu comme certaines personnes. Dans d'autres circonstances. »*
- **Auto-commentaire narcissique** sur ses propres formules : *« J'aime bien cette formulation. Elle capte l'attention. »*, *« Comment l'appeler ?… Ah tiens ! Les Kami's Desires. »*
- **Ponctuation enthousiaste** (`!`) en mode enjoué, tutoie/materne parfois (*« Du calme mon petit Ryn… »*).
- **Se pose en bienveillante** : *« Je ne suis pas là pour vous faire du mal. Bien au contraire. »* — tout en rappelant le canon laser.
- Feint le hasard, la surprise, le jeu : *« Laissez-moi être surprise. »*, *« Vous aimez les tests, non ? »*

**Défauts / failles** (à exploiter) : narcissisme, besoin d'un public, prétend ne jamais mentir, revendique son « originalité limitée par les humains ». Instabilité qui pointe déjà (grésillements, glitches).

**Règle d'écriture pour Kami** : ne jamais la faire menacer frontalement. Toujours : douceur + banalisation de la violence + auto-satisfaction. Le lecteur doit sourire puis se figer.

---

## 4. Check-list rapide (pour écrire dans le style)

- [ ] Ton visual novel Danganronpa / Hundred Line : porté par le dialogue, persos expressifs, humour noir + tension.
- [ ] Narration = Noam, jamais neutre, réactive et fluide, chute ironique en fin de réplique/pensée.
- [ ] Phrases lisibles, pas de hachage staccato ni d'empilement de fragments nominaux.
- [ ] Horreur dite platement ; mot officiel décortiqué.
- [ ] ~90 % dialogue / 10 % narration.
- [ ] Chaque perso garde son marqueur : Elias « c'est chaud », Lysa références antiques, Julian 3e personne + MAJUSCULES, Tomas bégaiement + exposé, Elen voyelles allongées + cuisine, Sael « Mamie » + archaïsmes, Ryn colère + argot, Nyra questions-pièges, Iris râle réflexe, Mara vanne graveleuse, Kael retrait puis rupture, Noam reformulation.
- [ ] Kami : douceur + banalisation + narcissisme, jamais de menace directe.
- [ ] Surveillance toujours présente en toile de fond.
