# Les Sept Questions de Kami — données, calendrier et progression persistante.

default persistent.seven_questions_completed_stages = []
default persistent.seven_questions_best_scores = {}
default persistent.seven_questions_reward_claimed = False
default persistent.seven_questions_reward_amount = 0
default persistent.seven_questions_intro_complete = False
default persistent.seven_questions_rewarded_questions = []
default persistent.seven_questions_rewarded_stages = []
default persistent.seven_questions_final_bonus_claimed = False
default persistent.seven_questions_outdated_quarter_remainder = 0
default persistent.seven_questions_total_shards_earned = 0

define SEVEN_QUESTIONS_START_LABEL = "19/08/2026"
define SEVEN_QUESTIONS_END_LABEL = "30/08/2026"
define SEVEN_QUESTIONS_REWARD = 180
define SEVEN_QUESTIONS_OUTDATED_REWARD = 45
define SEVEN_QUESTIONS_CORRECT_REWARD = 5
define SEVEN_QUESTIONS_STAGE_REWARD = 5
define SEVEN_QUESTIONS_FINAL_REWARD = 30

init python:
    import datetime

    SEVEN_QUESTIONS_START = datetime.date(2026, 8, 19)
    SEVEN_QUESTIONS_END = datetime.date(2026, 8, 30)
    SEVEN_QUESTIONS_START_AT = datetime.datetime(2026, 8, 19, 0, 0, 0)
    SEVEN_QUESTIONS_BOOST_END_AT = datetime.datetime(2026, 8, 31, 0, 0, 0)
    SEVEN_QUESTIONS_STAGE_DATES = tuple(
        SEVEN_QUESTIONS_START + datetime.timedelta(days=index) for index in range(7)
    )

    SEVEN_QUESTIONS_TEXT = {
        "fr": {
            "title": "LES SEPT QUESTIONS DE KAMI",
            "menu_title": "ÉVÈNEMENTS",
            "subtitle": "QUESTIONNAIRE TEMPORAIRE DU CONCLAVE",
            "description": "Sept thèmes pour mettre à l'épreuve votre connaissance du Conclave. Une nouvelle étape se déverrouille chaque jour.",
            "back": "RETOUR", "quit": "QUITTER", "shards": "ÉCLATS DE DÉSIR",
            "status_upcoming": "À VENIR", "status_ongoing": "EN COURS",
            "status_completed": "TERMINÉ", "status_outdated": "OUTDATED",
            "period": "19/08/26 — 30/08/26", "progress": "PROGRESSION",
            "reward": "RÉCOMPENSE UNIQUE", "reward_claimed": "RÉCOMPENSE OBTENUE",
            "normal_reward": "180 ÉCLATS AU TOTAL", "outdated_reward": "45 ÉCLATS AU TOTAL",
            "outdated_note": "Évènement archivé : la récompense non obtenue est divisée par quatre.",
            "upcoming_note": "La première étape sera disponible le 19/08/2026.",
            "event_list": "ÉVÈNEMENTS DISPONIBLES", "details": "VOIR L'ÉVÈNEMENT",
            "starts_in": "DÉBUT DANS", "boost_ends_in": "BONUS ACTIF ENCORE", "boost_ended": "PÉRIODE BONUS TERMINÉE",
            "unlocks_in": "DÉBLOCAGE DANS", "intro": "INTRODUCTION", "start_intro": "COMMENCER L'INTRODUCTION",
            "intro_required": "TERMINEZ D'ABORD L'INTRODUCTION", "continue": "CONTINUER", "start_test": "JE SUIS PRÊT",
            "intro_lines": ["Ah. Te voilà.", "Tu es venu pour les éclats, j'imagine.", "Prévisible. Mais presque attendrissant.", "Avant de commencer, j'ai une question.", "As-tu VRAIMENT fait attention aux autres ?", "Pas seulement à ce qu'ils ont bien voulu te montrer.", "À leurs habitudes. Leurs silences. Leurs contradictions.", "Et à ce qui t'entoure ?", "Les districts, leurs règles, tout ce que vous acceptez sans le regarder.", "Tu crois connaître le Conclave parce que tu y as survécu quelques jours.", "Moi, je t'ai regardé oublier des détails en temps réel.", "Alors j'ai préparé sept étapes.", "Chaque bonne réponse te rapportera cinq éclats. Je suis généreuse.", "Chaque erreur me prouvera surtout que j'avais raison de douter.", "Montre-moi que ton attention n'était pas une posture. On commence."],
            "correct_reward": "+5 ÉCLATS", "stage_reward": "+5 FIN D'ÉTAPE", "final_reward": "+30 FIN D'ÉVÈNEMENT",
            "select_stage": "SÉLECTIONNEZ UNE ÉTAPE", "locked": "VERROUILLÉ",
            "available": "DISPONIBLE", "done": "TERMINÉ", "play": "PARTICIPER",
            "replay": "REJOUER", "day": "JOUR", "question": "QUESTION",
            "choose": "SÉLECTIONNEZ UNE RÉPONSE", "next": "QUESTION SUIVANTE",
            "finish": "TERMINER L'ÉTAPE", "correct": "BONNE RÉPONSE",
            "wrong": "MAUVAISE RÉPONSE", "timeout": "TEMPS ÉCOULÉ",
            "score": "SCORE", "earned": "ÉCLATS À GAGNER", "already_earned": "DÉJÀ OBTENUS",
            "stages": ["Les représentants", "Les districts", "Le Conclave", "Les Commandements", "Les objets perdus", "Les réactions", "Le test final"],
            "questions": [
                [("Qui affirme : « Ces putains de votes ne nous protègerons pas. » ?", ["Ryn", "Kael", "Tomas"], 0),
                 ("Qui dit : « Chaque commandement supplémentaire augmente le risque d'un tir. » ?", ["Iris", "Kael", "Elias"], 1),
                 ("Si quelque chose tourne mal, l'un de nous portera ce visage.", ["Julian", "Tomas", "Sael"], 2)],
                [("Quel district concentre la recherche et les technologies avancées ?", ["Nexus", "Harmonie", "Limen"], 0),
                 ("Quel district est principalement industriel et tourné vers la production ?", ["Archive", "Axiome", "Orbite"], 1),
                 ("Quel district frontalier porte les cicatrices de la guerre et de la pauvreté ?", ["Harmonie", "Nexus", "Limen"], 2)],
                [("Combien de temps dure le Conclave ?", ["Sept jours", "Trente jours", "Une année"], 1),
                 ("À quelle fréquence un vote a-t-il lieu ?", ["Tous les jours", "Tous les trois jours", "Une fois par semaine"], 1),
                 ("Qu'est-ce qui suffit à rejeter un amendement ?", ["Une abstention", "Une absence", "Une voix contre"], 2)],
                [("Quel Commandement interdit la violence non autorisée ?", ["III", "V", "VIII"], 0),
                 ("Quel Commandement interdit les rumeurs non validées par Archive ?", ["II", "V", "IX"], 1),
                 ("Quel Commandement limite les déplacements entre districts ?", ["IV", "VI", "VII"], 1)],
                [("Quelle condition est nécessaire pour qu’une modification des Commandements soit adoptée ?", ["La majorité simple", "L’unanimité", "L’accord de Kami"], 1),
                ("Sur quel sujet porte le deuxième vote du Conclave ?", ["Les déplacements entre les districts", "La distribution de médicaments", "La suppression de la surveillance"], 0),
                ("Qui est fortement contre le déplacement de personnes entre les districts ?", ["Nyra", "Mara", "Sael"], 2)],
                [("Ryn entend quelqu'un mépriser Limen. Quelle réaction lui correspond le mieux ?", ["Colère", "Joie", "Indifférence"], 0),
                 ("Kael reçoit une alerte critique sur une turbine d'Orbite. Quelle expression est la plus logique ?", ["Inquiet", "Rieur", "Peur"], 2),
                 ("Iris repère un signal incohérent. Quelle réaction est la plus adaptée ?", ["Réflexion", "Euphorie", "Somnolence"], 0)],
                [("Noam et Lysa représentent quel district ?", ["Harmonie", "Axiome", "Archive"], 0),
                 ("Les abstentions comptent-elles parmi les suffrages exprimés du Conclave ?", ["Oui", "Non", "Seulement au vote final"], 1),
                 ("Quel Commandement place les ressources critiques sous contrôle central ?", ["IV", "VII", "X"], 1),
                 ("À qui appartient la photo de famille disparue ?", ["Kael", "Tomas", "Nyra"], 0),
                 ("Quel duo représente Limen ?", ["Ryn et Sael", "Iris et Julian", "Kael et Nyra"], 0)]
            ],
        },
        "en": {
            "title": "KAMI'S SEVEN QUESTIONS", "menu_title": "EVENTS",
            "subtitle": "TEMPORARY CONCLAVE QUIZ",
            "description": "Seven themes to test your knowledge of the Conclave. A new stage unlocks every day.",
            "back": "BACK", "quit": "QUIT", "shards": "DESIRE SHARDS",
            "status_upcoming": "UPCOMING", "status_ongoing": "ONGOING", "status_completed": "COMPLETED", "status_outdated": "OUTDATED",
            "period": "08/19/26 — 08/30/26", "progress": "PROGRESS", "reward": "ONE-TIME REWARD", "reward_claimed": "REWARD CLAIMED",
            "normal_reward": "180 SHARDS IN TOTAL", "outdated_reward": "45 SHARDS IN TOTAL",
            "outdated_note": "Archived event: any unclaimed reward is divided by four.", "upcoming_note": "The first stage will be available on 08/19/2026.",
            "event_list": "AVAILABLE EVENTS", "details": "VIEW EVENT", "starts_in": "STARTS IN", "boost_ends_in": "BOOST ENDS IN", "boost_ended": "BOOST PERIOD ENDED",
            "unlocks_in": "UNLOCKS IN", "intro": "INTRODUCTION", "start_intro": "START INTRODUCTION", "intro_required": "COMPLETE THE INTRODUCTION FIRST", "continue": "CONTINUE", "start_test": "I'M READY",
            "intro_lines": ["Ah. There you are.", "You came for the shards, I imagine.", "Predictable. But almost endearing.", "Before we begin, I have a question.", "Did you REALLY pay attention to the others?", "Not only to what they wanted you to see.", "To their habits. Their silences. Their contradictions.", "And to everything around you?", "The districts, their rules, everything you accept without looking at it.", "You think you know the Conclave because you survived it for a few days.", "I watched you forget details in real time.", "So I prepared seven stages.", "Every correct answer will earn you five shards. I am generous.", "Every mistake will mostly prove that I was right to doubt you.", "Show me your attention was more than an act. Let us begin."],
            "correct_reward": "+5 SHARDS", "stage_reward": "+5 STAGE COMPLETION", "final_reward": "+30 EVENT COMPLETION",
            "select_stage": "SELECT A STAGE", "locked": "LOCKED", "available": "AVAILABLE", "done": "COMPLETED", "play": "PLAY", "replay": "REPLAY",
            "day": "DAY", "question": "QUESTION", "choose": "SELECT AN ANSWER", "next": "NEXT QUESTION", "finish": "FINISH STAGE",
            "correct": "CORRECT ANSWER", "wrong": "WRONG ANSWER", "timeout": "TIME'S UP", "score": "SCORE", "earned": "SHARDS TO EARN", "already_earned": "ALREADY CLAIMED",
            "stages": ["The representatives", "The districts", "The Conclave", "The Commandments", "The lost objects", "The reactions", "The final test"],
            "questions": [

                [("Who says: “These fucking votes won’t protect us”?", ["Ryn", "Kael", "Tomas"], 0),
                ("Who says: “Every new Commandment increases the risk of a strike”?", ["Iris", "Kael", "Elias"], 1),
                ("Who says: “If something goes wrong, one of us will have to be the face of it”?", ["Julian", "Tomas", "Sael"], 2)],

                [("Which district focuses on advanced research and technology?", ["Nexus", "Harmonie", "Limen"], 0),
                ("Which district is mainly focused on industry and production?", ["Archive", "Axiome", "Orbite"], 1),
                ("Which frontier district still bears the scars of war and poverty?", ["Harmonie", "Nexus", "Limen"], 2)],

                [("How long does the Conclave last?", ["Seven days", "Thirty days", "One year"], 1),
                ("How often is a vote held?", ["Every day", "Every three days", "Once a week"], 1),
                ("What does it take to reject an amendment?", ["One abstention", "One absence", "A single vote against"], 2)],

                [("Which Commandment bans unauthorized violence?", ["III", "V", "VIII"], 0),
                ("Which Commandment bans rumors that haven’t been verified by Archive?", ["II", "V", "IX"], 1),
                ("Which Commandment restricts travel between districts?", ["IV", "VI", "VII"], 1)],

                [("What is required for a change to the Commandments to be approved?", ["A simple majority", "A unanimous vote", "Kami’s approval"], 1),
                ("What is the Conclave’s second vote about?", ["Travel between districts", "The distribution of medicine", "Ending surveillance"], 0),
                ("Who is strongly against people traveling between districts?", ["Nyra", "Mara", "Sael"], 2)],

                [("Ryn hears someone talking down about Limen. How would they most likely react?", ["With anger", "With joy", "With indifference"], 0),
                ("Kael receives a critical alert about an Orbite turbine. How would he most likely react?", ["Worried", "Laughing", "Afraid"], 2),
                ("Iris spots an inconsistent signal. How would she most likely react?", ["She would think it over", "She would get excited", "She would feel sleepy"], 0)],

                [("Which district do Noam and Lysa represent?", ["Harmonie", "Axiome", "Archive"], 0),
                ("Do abstentions count as votes cast in the Conclave?", ["Yes", "No", "Only in the final vote"], 1),
                ("Which Commandment places critical resources under central control?", ["IV", "VII", "X"], 1),
                ("Whose family photo went missing?", ["Kael", "Tomas", "Nyra"], 0),
                ("Which pair represents Limen?", ["Ryn and Sael", "Iris and Julian", "Kael and Nyra"], 0)]

            ],
        },
        "pt": {
            "title": "AS SETE PERGUNTAS DE KAMI", "menu_title": "EVENTOS", "subtitle": "QUESTIONÁRIO TEMPORÁRIO DO CONCLAVE",
            "description": "Sete temas para testar o seu conhecimento do Conclave. Uma nova etapa é desbloqueada todos os dias.",
            "back": "VOLTAR", "quit": "SAIR", "shards": "FRAGMENTOS DE DESEJO", "status_upcoming": "EM BREVE", "status_ongoing": "EM CURSO", "status_completed": "CONCLUÍDO", "status_outdated": "OUTDATED",
            "period": "19/08/26 — 30/08/26", "progress": "PROGRESSO", "reward": "RECOMPENSA ÚNICA", "reward_claimed": "RECOMPENSA OBTIDA", "normal_reward": "180 FRAGMENTOS NO TOTAL", "outdated_reward": "45 FRAGMENTOS NO TOTAL",
            "outdated_note": "Evento arquivado: a recompensa ainda não obtida é dividida por quatro.", "upcoming_note": "A primeira etapa estará disponível em 19/08/2026.",
            "event_list": "EVENTOS DISPONÍVEIS", "details": "VER EVENTO", "starts_in": "COMEÇA EM", "boost_ends_in": "BÓNUS TERMINA EM", "boost_ended": "PERÍODO DE BÓNUS TERMINADO",
            "unlocks_in": "DESBLOQUEIA EM", "intro": "INTRODUÇÃO", "start_intro": "COMEÇAR INTRODUÇÃO", "intro_required": "CONCLUA PRIMEIRO A INTRODUÇÃO", "continue": "CONTINUAR", "start_test": "ESTOU PRONTO",
            "intro_lines": ["Ah. Aí estás.", "Vieste pelos fragmentos, imagino.", "Previsível. Mas quase comovente.", "Antes de começarmos, tenho uma pergunta.", "Prestaste MESMO atenção aos outros?", "Não apenas ao que quiseram mostrar-te.", "Aos seus hábitos. Aos silêncios. Às contradições.", "E a tudo o que te rodeia?", "Os distritos, as suas regras, tudo o que aceitas sem sequer olhar.", "Achas que conheces o Conclave porque sobreviveste nele durante alguns dias.", "Eu vi-te esquecer detalhes em tempo real.", "Por isso preparei sete etapas.", "Cada resposta correta dar-te-á cinco fragmentos. Sou generosa.", "Cada erro provará sobretudo que eu tinha razão em duvidar.", "Mostra-me que a tua atenção não era apenas uma pose. Vamos começar."],
            "correct_reward": "+5 FRAGMENTOS", "stage_reward": "+5 FIM DE ETAPA", "final_reward": "+30 FIM DO EVENTO",
            "select_stage": "SELECIONE UMA ETAPA", "locked": "BLOQUEADO", "available": "DISPONÍVEL", "done": "CONCLUÍDO", "play": "PARTICIPAR", "replay": "REPETIR",
            "day": "DIA", "question": "PERGUNTA", "choose": "SELECIONE UMA RESPOSTA", "next": "PRÓXIMA PERGUNTA", "finish": "CONCLUIR ETAPA", "correct": "RESPOSTA CORRETA", "wrong": "RESPOSTA ERRADA", "timeout": "TEMPO ESGOTADO", "score": "PONTUAÇÃO", "earned": "FRAGMENTOS A GANHAR", "already_earned": "JÁ OBTIDOS",
            "stages": ["Os representantes", "Os distritos", "O Conclave", "Os Mandamentos", "Os objetos perdidos", "As reações", "O teste final"],
            "questions": [

                [("Quem diz: “Essas porras de votações não vão nos proteger”?", ["Ryn", "Kael", "Tomas"], 0),
                ("Quem diz: “Cada novo Mandamento aumenta o risco de um disparo”?", ["Iris", "Kael", "Elias"], 1),
                ("Quem diz: “Se alguma coisa der errado, um de nós vai ter que dar a cara por isso”?", ["Julian", "Tomas", "Sael"], 2)],

                [("Qual distrito é voltado para pesquisas e tecnologias avançadas?", ["Nexus", "Harmonie", "Limen"], 0),
                ("Qual distrito é voltado principalmente para a indústria e a produção?", ["Archive", "Axiome", "Orbite"], 1),
                ("Qual distrito de fronteira ainda carrega as marcas da guerra e da pobreza?", ["Harmonie", "Nexus", "Limen"], 2)],

                [("Quanto tempo dura o Conclave?", ["Sete dias", "Trinta dias", "Um ano"], 1),
                ("Com que frequência acontece uma votação?", ["Todos os dias", "A cada três dias", "Uma vez por semana"], 1),
                ("O que basta para rejeitar uma emenda?", ["Uma única abstenção", "Uma única ausência", "Um único voto contra"], 2)],

                [("Qual Mandamento proíbe a violência não autorizada?", ["III", "V", "VIII"], 0),
                ("Qual Mandamento proíbe rumores que não tenham sido confirmados por Archive?", ["II", "V", "IX"], 1),
                ("Qual Mandamento restringe as viagens entre os distritos?", ["IV", "VI", "VII"], 1)],

                [("O que é necessário para aprovar uma mudança nos Mandamentos?", ["Uma maioria simples", "Uma votação unânime", "A aprovação de Kami"], 1),
                ("Qual é o assunto da segunda votação do Conclave?", ["As viagens entre os distritos", "A distribuição de medicamentos", "O fim da vigilância"], 0),
                ("Quem é totalmente contra a circulação de pessoas entre os distritos?", ["Nyra", "Mara", "Sael"], 2)],

                [("Ryn ouve alguém falando mal de Limen. Qual seria a reação mais provável?", ["Raiva", "Alegria", "Indiferença"], 0),
                ("Kael recebe um alerta crítico sobre uma turbina de Orbite. Qual seria a reação mais provável?", ["Preocupação", "Riso", "Medo"], 2),
                ("Iris percebe um sinal incoerente. Qual seria a reação mais provável?", ["Parar para pensar", "Ficar eufórica", "Ficar com sono"], 0)],

                [("Qual distrito Noam e Lysa representam?", ["Harmonie", "Axiome", "Archive"], 0),
                ("As abstenções contam como votos no Conclave?", ["Sim", "Não", "Somente na votação final"], 1),
                ("Qual Mandamento coloca os recursos essenciais sob controle central?", ["IV", "VII", "X"], 1),
                ("De quem era a foto de família que desapareceu?", ["Kael", "Tomas", "Nyra"], 0),
                ("Qual dupla representa Limen?", ["Ryn e Sael", "Iris e Julian", "Kael e Nyra"], 0)]

            ],
        },
        "zh": {
            "title": "卡米的七道问题", "menu_title": "活动", "subtitle": "圆桌会议限时问答",
            "description": "七个主题将考验你对圆桌会议的了解。每天解锁一个新阶段。",
            "back": "返回", "quit": "退出", "shards": "欲望碎片", "status_upcoming": "即将开始", "status_ongoing": "进行中", "status_completed": "已完成", "status_outdated": "OUTDATED",
            "period": "2026/08/19 — 2026/08/30", "progress": "进度", "reward": "一次性奖励", "reward_claimed": "奖励已领取", "normal_reward": "总计180碎片", "outdated_reward": "总计45碎片",
            "outdated_note": "活动已归档：尚未领取的奖励将变为四分之一。", "upcoming_note": "第一阶段将于2026年8月19日开放。",
            "event_list": "可用活动", "details": "查看活动", "starts_in": "距离开始", "boost_ends_in": "奖励加成剩余", "boost_ended": "奖励加成期已结束",
            "unlocks_in": "距离解锁", "intro": "序章", "start_intro": "开始序章", "intro_required": "请先完成序章", "continue": "继续", "start_test": "我准备好了",
            "intro_lines": ["啊，你来了。", "我猜你是为了碎片而来。", "真好猜。不过也算有点可爱。", "开始之前，我有一个问题。", "你真的认真留意过其他人吗？", "不只是他们愿意让你看见的那一面。", "他们的习惯、沉默，还有自相矛盾之处。", "那么你周围的一切呢？", "各大区、它们的规则，以及所有你看都不看就接受的事物。", "你以为自己撑过几天，就已经了解Conclave。", "而我一直看着你当场忘掉那些细节。", "所以，我准备了七个阶段。", "每答对一题就能得到五枚碎片。我很慷慨吧。", "每一次错误，只会证明我对你的怀疑是对的。", "证明你的关注不是装出来的。开始吧。"],
            "correct_reward": "+5碎片", "stage_reward": "+5阶段完成奖励", "final_reward": "+30活动完成奖励",
            "select_stage": "选择阶段", "locked": "未解锁", "available": "可挑战", "done": "已完成", "play": "参加", "replay": "重玩",
            "day": "第", "question": "问题", "choose": "请选择答案", "next": "下一题", "finish": "完成阶段", "correct": "回答正确", "wrong": "回答错误", "timeout": "时间到", "score": "得分", "earned": "可获得碎片", "already_earned": "已领取",
            "stages": ["代表们", "各大区", "圆桌会议", "十诫", "失物", "反应", "最终测试"],
            "questions": [

                [("谁说过：“这些他妈的投票保护不了我们”?", ["Ryn", "Kael", "Tomas"], 0),
                ("谁说过：“每增加一条戒律，遭到炮击的风险就会更高”?", ["Iris", "Kael", "Elias"], 1),
                ("谁说过：“要是出了什么问题，我们中总得有一个人出面承担”?", ["Julian", "Tomas", "Sael"], 2)],

                [("哪个地区主要负责先进技术的研究和开发?", ["Nexus", "Harmonie", "Limen"], 0),
                ("哪个地区主要以工业和生产为主?", ["Archive", "Axiome", "Orbite"], 1),
                ("哪个边境地区至今仍留有战争和贫困的伤痕?", ["Harmonie", "Nexus", "Limen"], 2)],

                [("Conclave会持续多长时间?", ["七天", "三十天", "一年"], 1),
                ("多久进行一次投票?", ["每天一次", "每三天一次", "每周一次"], 1),
                ("什么情况足以让一项修正案被否决?", ["一人弃权", "一人缺席", "一票反对"], 2)],

                [("哪一条戒律禁止未经许可的暴力行为?", ["III", "V", "VIII"], 0),
                ("哪一条戒律禁止传播未经Archive核实的传言?", ["II", "V", "IX"], 1),
                ("哪一条戒律限制跨区出行?", ["IV", "VI", "VII"], 1)],

                [("要修改戒律，必须满足什么条件才能通过?", ["获得简单多数", "全票通过", "得到Kami的批准"], 1),
                ("Conclave的第二次投票是关于什么的?", ["各区之间的人员流动", "药品分配", "终止监控"], 0),
                ("谁坚决反对人员在各区之间流动?", ["Nyra", "Mara", "Sael"], 2)],

                [("Ryn听到有人贬低Limen。Ryn最可能有什么反应?", ["愤怒", "高兴", "毫不在意"], 0),
                ("Kael收到Orbite一台涡轮机的严重故障警报。Kael最可能有什么反应?", ["担心", "发笑", "害怕"], 2),
                ("Iris发现一个异常信号。Iris最可能有什么反应?", ["认真思考", "异常兴奋", "昏昏欲睡"], 0)],

                [("Noam和Lysa代表哪个地区?", ["Harmonie", "Axiome", "Archive"], 0),
                ("弃权算不算Conclave中的有效投票?", ["算", "不算", "只有最终投票时才算"], 1),
                ("哪一条戒律规定关键资源由中央统一管控?", ["IV", "VII", "X"], 1),
                ("失踪的家庭照片是谁的?", ["Kael", "Tomas", "Nyra"], 0),
                ("哪两个人代表Limen?", ["Ryn和Sael", "Iris和Julian", "Kael和Nyra"], 0)]

            ],
        },
    }

    CHAPTER_2_REWARD_BOOST_TEXT = {
        "fr": {
            "title": "REWARD BOOST : COMPLETE CHAPTER 2",
            "subtitle": "BONUS TEMPORAIRE DE PROGRESSION",
            "description": "Terminez le chapitre 2 avant la fin du 30/08/2026 pour recevoir une récompense boostée.",
            "active": "BONUS ACTIF",
            "ended": "BONUS TERMINÉ",
            "boosted_reward": "40 ÉCLATS DE DÉSIR",
            "standard_reward": "10 ÉCLATS DE DÉSIR",
            "reward_label": "RÉCOMPENSE DU CHAPITRE 2",
            "deadline": "JUSQU’AU 30/08/2026 INCLUS",
            "after_deadline": "Après cette date, la récompense de fin du chapitre 2 est réduite à 10 éclats de désir.",
            "details": "VOIR LE BONUS",
        },
        "en": {
            "title": "REWARD BOOST: COMPLETE CHAPTER 2",
            "subtitle": "LIMITED-TIME PROGRESSION BONUS",
            "description": "Complete Chapter 2 by the end of August 30, 2026 to receive the boosted reward.",
            "active": "BOOST ACTIVE",
            "ended": "BOOST ENDED",
            "boosted_reward": "40 DESIRE SHARDS",
            "standard_reward": "10 DESIRE SHARDS",
            "reward_label": "CHAPTER 2 COMPLETION REWARD",
            "deadline": "THROUGH 08/30/2026, INCLUSIVE",
            "after_deadline": "After this date, the Chapter 2 completion reward is reduced to 10 Desire Shards.",
            "details": "VIEW BOOST",
        },
        "pt": {
            "title": "REWARD BOOST: COMPLETE CHAPTER 2",
            "subtitle": "BÓNUS DE PROGRESSÃO TEMPORÁRIO",
            "description": "Conclua o capítulo 2 até ao fim de 30/08/2026 para receber a recompensa aumentada.",
            "active": "BÓNUS ATIVO",
            "ended": "BÓNUS TERMINADO",
            "boosted_reward": "40 FRAGMENTOS DE DESEJO",
            "standard_reward": "10 FRAGMENTOS DE DESEJO",
            "reward_label": "RECOMPENSA DO CAPÍTULO 2",
            "deadline": "ATÉ 30/08/2026, INCLUSIVE",
            "after_deadline": "Após esta data, a recompensa por concluir o capítulo 2 é reduzida para 10 fragmentos de desejo.",
            "details": "VER BÓNUS",
        },
        "zh": {
            "title": "REWARD BOOST: COMPLETE CHAPTER 2",
            "subtitle": "限时进度奖励",
            "description": "在2026年8月30日结束前完成第2章，即可获得加成奖励。",
            "active": "奖励加成生效中",
            "ended": "奖励加成已结束",
            "boosted_reward": "40 欲望碎片",
            "standard_reward": "10 欲望碎片",
            "reward_label": "第2章通关奖励",
            "deadline": "截至2026年8月30日（含当日）",
            "after_deadline": "此日期之后，第2章通关奖励将降为10欲望碎片。",
            "details": "查看奖励加成",
        },
    }

    def seven_questions_language():
        language = preferences.language
        return {"english": "en", "portuguese": "pt", "chinese": "zh"}.get(language, "fr")

    def sq_text(key):
        return SEVEN_QUESTIONS_TEXT[seven_questions_language()][key]

    def chapter_2_reward_boost_text(key):
        return CHAPTER_2_REWARD_BOOST_TEXT[seven_questions_language()][key]

    def chapter_2_reward_boost_status():
        return "active" if kami_chapter_2_reward_is_boosted() else "ended"

    def chapter_2_reward_boost_status_label():
        return chapter_2_reward_boost_text(chapter_2_reward_boost_status())

    def chapter_2_reward_boost_timer_label():
        if not kami_chapter_2_reward_is_boosted():
            return chapter_2_reward_boost_text("ended")
        return "{}  {}".format(sq_text("boost_ends_in"), sq_countdown(CHAPTER_2_BOOST_END_AT))

    def sq_stage_title(stage_index):
        return sq_text("stages")[stage_index]

    def sq_stage_questions(stage_index):
        return sq_text("questions")[stage_index]

    def sq_intro_line(line_index):
        return sq_text("intro_lines")[line_index]

    def sq_today():
        return datetime.date.today()

    def sq_completed_stages():
        return list(persistent.seven_questions_completed_stages or [])

    def sq_status():
        today = sq_today()
        if today < SEVEN_QUESTIONS_START:
            return "upcoming"
        if today > SEVEN_QUESTIONS_END:
            return "outdated"
        if len(sq_completed_stages()) >= 7:
            return "completed"
        return "ongoing"

    def sq_status_label():
        return sq_text("status_" + sq_status())

    def sq_unlocked_count():
        today = sq_today()
        if today < SEVEN_QUESTIONS_START:
            return 0
        if today > SEVEN_QUESTIONS_END:
            return 7
        return min(7, (today - SEVEN_QUESTIONS_START).days + 1)

    def sq_stage_is_unlocked(stage_index):
        return stage_index < sq_unlocked_count()

    def sq_stage_date_label(stage_index):
        stage_date = SEVEN_QUESTIONS_STAGE_DATES[stage_index]
        if seven_questions_language() == "en":
            return stage_date.strftime("%m/%d/%y")
        if seven_questions_language() == "zh":
            return stage_date.strftime("%Y/%m/%d")
        return stage_date.strftime("%d/%m/%y")

    def sq_reward_preview():
        return SEVEN_QUESTIONS_OUTDATED_REWARD if sq_status() == "outdated" else SEVEN_QUESTIONS_REWARD

    def sq_countdown(target_datetime):
        remaining = max(0, int((target_datetime - datetime.datetime.now()).total_seconds()))
        days, remaining = divmod(remaining, 86400)
        hours, remaining = divmod(remaining, 3600)
        minutes, seconds = divmod(remaining, 60)
        day_marker = {"fr": "j", "en": "d", "pt": "d", "zh": "天"}.get(seven_questions_language(), "d")
        return "{}{} {:02d}:{:02d}:{:02d}".format(days, day_marker, hours, minutes, seconds)

    def sq_event_timer_label():
        now = datetime.datetime.now()
        if now < SEVEN_QUESTIONS_START_AT:
            return "{}  {}".format(sq_text("starts_in"), sq_countdown(SEVEN_QUESTIONS_START_AT))
        if now < SEVEN_QUESTIONS_BOOST_END_AT:
            return "{}  {}".format(sq_text("boost_ends_in"), sq_countdown(SEVEN_QUESTIONS_BOOST_END_AT))
        return sq_text("boost_ended")

    def sq_stage_timer_label(stage_index):
        unlock_at = datetime.datetime.combine(SEVEN_QUESTIONS_STAGE_DATES[stage_index], datetime.time.min)
        if datetime.datetime.now() < unlock_at:
            return "{}  {}".format(sq_text("unlocks_in"), sq_countdown(unlock_at))
        return sq_text("done") if stage_index in sq_completed_stages() else sq_text("available")

    def sq_complete_intro():
        persistent.seven_questions_intro_complete = True
        renpy.save_persistent()

    def sq_grant_event_reward(base_amount):
        base_amount = int(base_amount)
        if base_amount <= 0:
            return 0

        if sq_today() > SEVEN_QUESTIONS_END:
            quarter_pool = int(persistent.seven_questions_outdated_quarter_remainder or 0) + base_amount
            payout, remainder = divmod(quarter_pool, 4)
            persistent.seven_questions_outdated_quarter_remainder = remainder
        else:
            payout = base_amount

        if payout:
            persistent.desire_shards = max(0, int(persistent.desire_shards or 0) + payout)
            persistent.seven_questions_total_shards_earned = int(persistent.seven_questions_total_shards_earned or 0) + payout
            persistent.seven_questions_reward_amount = persistent.seven_questions_total_shards_earned
            renpy.notify("+{} {}".format(payout, sq_text("shards")))
        return payout

    def sq_reward_question(stage_index, question_index):
        reward_key = "{}:{}".format(int(stage_index), int(question_index))
        rewarded = set(persistent.seven_questions_rewarded_questions or [])
        if reward_key in rewarded:
            return 0
        rewarded.add(reward_key)
        persistent.seven_questions_rewarded_questions = sorted(rewarded)
        payout = sq_grant_event_reward(SEVEN_QUESTIONS_CORRECT_REWARD)
        renpy.save_persistent()
        return payout

    def sq_question_rewarded(stage_index, question_index):
        reward_key = "{}:{}".format(int(stage_index), int(question_index))
        return reward_key in (persistent.seven_questions_rewarded_questions or [])

    def sq_finish_stage(stage_index, score, question_count):
        completed = set(sq_completed_stages())
        completed.add(int(stage_index))
        persistent.seven_questions_completed_stages = sorted(completed)

        best_scores = dict(persistent.seven_questions_best_scores or {})
        score_key = str(stage_index)
        best_scores[score_key] = max(int(score), int(best_scores.get(score_key, 0)))
        persistent.seven_questions_best_scores = best_scores

        base_reward = 0
        rewarded_stages = set(persistent.seven_questions_rewarded_stages or [])
        if int(stage_index) not in rewarded_stages:
            rewarded_stages.add(int(stage_index))
            persistent.seven_questions_rewarded_stages = sorted(rewarded_stages)
            base_reward += SEVEN_QUESTIONS_STAGE_REWARD

        if len(completed) >= 7 and not persistent.seven_questions_final_bonus_claimed:
            persistent.seven_questions_final_bonus_claimed = True
            persistent.seven_questions_reward_claimed = True
            base_reward += SEVEN_QUESTIONS_FINAL_REWARD

        payout = sq_grant_event_reward(base_reward)
        renpy.save_persistent()
        if not payout:
            renpy.notify("{} : {}/{}".format(sq_text("score"), score, question_count))
