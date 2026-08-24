# =============================================================================
# CODEX — Système de PACKS d'entrées + scènes bonus
# 3 colonnes : Packs / Entrées du pack / Détail + récompense
# =============================================================================
# Débloquer une entrée :  $ unlock_codex_page("id_entree")
# Quand toutes les entrées d'un pack sont débloquées -> scène bonus jouable.
# =============================================================================

# Conservé pour pouvoir migrer les déblocages présents dans les anciennes
# sauvegardes. La progression canonique du Codex vit désormais dans persistent.
default codex_unlocked_entries = []
default persistent.codex_unlocked_entries = []

# CODEX_ENTRIES doit exister AVANT les init de priorité >0 (injections scénario)
init -5 python:
    CODEX_ENTRIES = {}

init python:

    import re

    def _codex_loc(fr, en, pt, zh):
        return {"fr": fr, "english": en, "portuguese": pt, "chinese": zh}

    # ------------------------------------------------------------------
    # PACKS
    # ------------------------------------------------------------------
    CODEX_PACKS = [
        {
            "id": "conclave", "num": 1,
            "title": "LE CONCLAVE",
            "subtitle": "Les règles, les membres\net le fonctionnement du Conclave.",
            "color": "#5CD3FF", "icon": "pack_conclave", "banner": "banner_conclave",
            "entries": ["reglement_conclave"],
        },
        {
            "id": "districts", "num": 2,
            "title": "LES DISTRICTS",
            "subtitle": "Les différents districts, leurs\nressources et leurs particularités.",
            "color": "#F0A835", "icon": "pack_districts", "banner": "banner_districts",
            "entries": ["harmonie", "axiome", "archive", "limen", "nexus", "orbite"],
        },
        {
            "id": "societe", "num": 3,
            "title": "SYSTÈMES ET FRONTIÈRES",
            "subtitle": "L'organisation matérielle, économique\net territoriale sous Kami.",
            "color": "#70D6A5", "icon": "pack_conclave", "banner": "banner_conclave",
            "entries": ["bons_rationnement", "derogations_administratives", "commerce_monnaie", "frontieres_interdistricts", "frontieres_limen"],
        },
        {
            "id": "orbite", "num": 4,
            "title": "ORBITE",
            "subtitle": "La station orbitale, ses systèmes\net ses technologies.",
            "color": "#B57BFF", "icon": "pack_orbite", "banner": "banner_orbite",
            "entries": ["complexe_c"],
        },
    ]

    # ------------------------------------------------------------------
    # ENTRÉES (title / icon / short / assoc / text)
    # ------------------------------------------------------------------
    _CODEX_DATA = {
        "reglement_conclave": {
            "title": _codex_loc("Règlement du Conclave", "Conclave Rules", "Regulamento do Conclave", "秘密会议规则"),
            "icon": "ic_doc", "assoc": [], "auto_unlock": False,
            "short": _codex_loc("Les règles du huis clos de trente jours.", "Rules governing the thirty-day isolation.", "As regras do isolamento de trinta dias.", "为期三十天封闭会议的规则。"),
            "text": _codex_loc(
                "Le Conclave dure trente jours et ses douze représentants restent isolés dans le complexe. Chacun dépose un amendement, mais dix seulement sont tirés au sort. Un vote a lieu tous les trois jours. L'adoption exige l'unanimité des suffrages exprimés ; abstentions et absences sont exclues du décompte. Les Commandements ordinaires sont suspendus à l'intérieur du complexe, mais son règlement propre demeure applicable.",
                "The Conclave lasts thirty days, during which its twelve representatives remain isolated inside the complex. Each submits one amendment, but only ten are drawn. A vote takes place every three days. Adoption requires unanimity among votes cast; abstentions and absences are excluded. The ordinary Commandments are suspended inside the complex, although its own rules remain in force.",
                "O Conclave dura trinta dias, durante os quais seus doze representantes permanecem isolados no complexo. Cada um apresenta uma emenda, mas apenas dez são sorteadas. Há uma votação a cada três dias. A aprovação exige unanimidade entre os votos expressos; abstenções e ausências ficam fora da contagem. Os Mandamentos comuns ficam suspensos dentro do complexo, mas o regulamento interno continua valendo.",
                "秘密会议持续三十天，十二名代表在此期间必须与外界隔离。每人提交一项修正案，但只有十项会被抽中。每三天进行一次投票；议案必须获得全部有效票一致赞成才能通过，弃权和缺席不计入有效票。普通戒律在设施内暂停执行，但设施自身的规则仍然有效。"),
            "aliases": ["règlement du Conclave", "règles du Conclave", "Conclave rules", "rules of the Conclave", "regulamento do Conclave", "regras do Conclave", "秘密会议规则"],
        },
        "harmonie": {
            "title": _codex_loc("Harmonie", "Harmony", "Harmonia", "和谐区"),
            "icon": "ic_building", "assoc": ["archive"], "auto_unlock": True,
            "short": _codex_loc("District administratif de l'ancienne capitale veyronne.", "Administrative district built on the former Veyron capital.", "Distrito administrativo da antiga capital veyronesa.", "建立在旧维隆首都上的行政区。"),
            "text": _codex_loc("Harmonie est un district principalement administratif et urbain, établi sur l'ancienne capitale de l'Empire Veyron après la prise de pouvoir de Kami. Il compte environ 650 000 habitants.", "Harmony is a mostly urban and administrative district established on the former capital of the Veyron Empire after Kami seized power. It has roughly 650,000 inhabitants.", "Harmonia é um distrito principalmente urbano e administrativo, estabelecido na antiga capital do Império Veyron após Kami tomar o poder. Tem cerca de 650 mil habitantes.", "和谐区是Kami掌权后在旧维隆帝国首都上建立的城市行政区，约有65万居民。"),
            "aliases": ["Harmonie", "Harmony", "Harmonia", "和谐区", "和谐"],
        },
        "axiome": {
            "title": _codex_loc("Axiome", "Axiom", "Axioma", "公理区"),
            "icon": "ic_building", "assoc": [], "auto_unlock": True,
            "short": _codex_loc("District industriel et centre de production.", "Industrial district and manufacturing center.", "Distrito industrial e centro de produção.", "工业与生产中心。"),
            "text": _codex_loc("Axiome concentre une grande partie des usines et de la production. Les violences qui marquaient autrefois ses quartiers ont fortement diminué sous Kami, ce qui en fait l'un des districts les plus favorables à son régime.", "Axiom contains much of the industrial and manufacturing capacity. Violence in its neighborhoods fell sharply under Kami, making it one of the districts most supportive of her rule.", "Axioma concentra grande parte das fábricas e da produção. A violência que antes marcava seus bairros caiu muito sob Kami, tornando-o um dos distritos mais favoráveis ao regime.", "公理区集中了大量工厂与生产设施。Kami统治后，当地曾经严重的街区暴力大幅下降，因此这里也是最支持其政权的地区之一。"),
            "aliases": ["Axiome", "Axiom", "Axioma", "公理区", "公理"],
        },
        "archive": {
            "title": _codex_loc("Archive", "Archive", "Arquivo", "档案区"),
            "icon": "ic_antenna", "assoc": ["harmonie"], "auto_unlock": True,
            "short": _codex_loc("District chargé de l'information et de la propagande.", "District responsible for information and propaganda.", "Distrito responsável pela informação e propaganda.", "负责信息与宣传的地区。"),
            "text": _codex_loc("Archive est un petit district administratif installé dans une tour immense, enclavée au sein d'Harmonie. Il contrôle les flux d'information et la propagande du régime de Kami et compte environ 22 500 habitants.", "Archive is a small administrative district housed in a vast tower enclosed within Harmony. It controls information flows and propaganda for Kami's regime and has roughly 22,500 inhabitants.", "Arquivo é um pequeno distrito administrativo instalado em uma torre imensa, cercada por Harmonia. Controla os fluxos de informação e a propaganda do regime de Kami e tem cerca de 22.500 habitantes.", "档案区是位于和谐区内部一座巨塔中的小型行政区，负责控制Kami政权的信息流与宣传，约有22500名居民。"),
            "aliases": ["Archive", "district Archive", "Archive district", "distrito Arquivo", "Arquivo", "档案区"],
        },
        "limen": {
            "title": _codex_loc("Limen", "Limen", "Limen", "边界区"),
            "icon": "ic_building", "assoc": ["frontieres_limen"], "auto_unlock": True,
            "short": _codex_loc("Le plus vaste, le plus peuplé et le plus pauvre des districts.", "The largest, most populated and poorest district.", "O maior, mais populoso e mais pobre dos distritos.", "面积最大、人口最多也最贫困的地区。"),
            "text": _codex_loc("Limen est le plus vaste et le plus peuplé des districts terrestres, mais aussi le plus pauvre. Déserts, montagnes, villes partiellement reconstruites et campagnes isolées portent encore les traces des guerres antérieures à Kami.", "Limen is the largest and most populated terrestrial district, and also the poorest. Its deserts, mountains, half-rebuilt cities and isolated countryside still bear the scars of the wars before Kami.", "Limen é o maior e mais populoso distrito terrestre, além de ser o mais pobre. Desertos, montanhas, cidades parcialmente reconstruídas e áreas rurais isoladas ainda carregam as marcas das guerras anteriores a Kami.", "边界区是面积最大、人口最多也最贫困的地面地区。沙漠、山地、重建不完整的城市和偏远乡村仍留有Kami掌权前战争的痕迹。"),
            "aliases": ["Limen", "边界区"],
        },
        "nexus": {
            "title": _codex_loc("Nexus", "Nexus", "Nexus", "枢纽区"),
            "icon": "ic_building", "assoc": [], "auto_unlock": True,
            "short": _codex_loc("District de la recherche et des technologies avancées.", "District of research and advanced technology.", "Distrito de pesquisa e tecnologia avançada.", "科研与先进技术中心。"),
            "text": _codex_loc("Nexus est le district technologiquement le plus avancé. Il concentre chercheurs, ingénieurs et programmes de développement, même si nombre de projets indépendants ont été gelés ou réorientés sous Kami.", "Nexus is the most technologically advanced district. It concentrates researchers, engineers and development programs, although many independent projects were frozen or redirected under Kami.", "Nexus é o distrito tecnologicamente mais avançado. Reúne pesquisadores, engenheiros e programas de desenvolvimento, embora muitos projetos independentes tenham sido congelados ou redirecionados sob Kami.", "枢纽区是技术最先进的地区，汇集了研究人员、工程师和研发项目；但在Kami统治下，许多独立项目已被冻结或改作他用。"),
            "aliases": ["Nexus", "枢纽区", "枢纽"],
        },
        "orbite": {
            "title": _codex_loc("Orbite", "Orbit", "Órbita", "轨道区"),
            "icon": "ic_antenna", "assoc": ["complexe_c"], "auto_unlock": True,
            "short": _codex_loc("District spatial composé de stations et de flottes.", "Space district made up of stations and fleets.", "Distrito espacial formado por estações e frotas.", "由空间站与舰队组成的太空地区。"),
            "text": _codex_loc("Orbite regroupe des stations isolées et des flottes mobiles. Son autonomie dépend de systèmes de survie fragiles : une panne de coque, d'oxygène ou de pression peut tuer tout un module en quelques instants.", "Orbit comprises isolated stations and mobile fleets. Its autonomy depends on fragile life-support systems: a hull, oxygen or pressure failure can kill an entire module within moments.", "Órbita reúne estações isoladas e frotas móveis. Sua autonomia depende de sistemas de suporte de vida frágeis: uma falha no casco, no oxigênio ou na pressão pode matar um módulo inteiro em instantes.", "轨道区由孤立空间站和移动舰队组成，其自治依赖脆弱的生命维持系统；船体、氧气或气压故障都可能在瞬间夺走整个舱段的生命。"),
            "aliases": ["Orbite", "Orbit", "Órbita", "Orbita", "轨道区", "轨道"],
        },
        "bons_rationnement": {
            "title": _codex_loc("Bons de rationnement", "Ration Coupons", "Cupons de racionamento", "配给券"),
            "icon": "ic_doc", "assoc": ["commerce_monnaie"], "auto_unlock": False,
            "short": _codex_loc("Le système de distribution des biens essentiels.", "The system used to distribute essential goods.", "O sistema de distribuição de bens essenciais.", "用于分配基本物资的制度。"),
            "text": _codex_loc("Depuis la disparition du commerce, les biens essentiels sont distribués grâce à des bons de rationnement. Les quantités dépendent des stocks attribués à chaque district. Le système garantit théoriquement un minimum, mais ne garantit ni la disponibilité réelle ni l'égalité réelle entre districts.", "Since trade disappeared, essential goods have been distributed through ration coupons. Quantities depend on the stock allocated to each district. The system theoretically guarantees a minimum, but guarantees neither actual availability nor real equality between districts.", "Desde o desaparecimento do comércio, os bens essenciais são distribuídos por cupons de racionamento. As quantidades dependem dos estoques atribuídos a cada distrito. Em teoria, o sistema garante um mínimo, mas não garante disponibilidade real nem igualdade entre os distritos.", "贸易消失后，基本物资通过配给券发放。数量取决于分配给各区的库存。该制度理论上保障最低供应，却既不能保证物资实际有货，也不能保证地区之间真正平等。"),
            "aliases": ["bons de rationnement", "bons de ravitaillement", "rationnement", "ration coupons", "rationing coupons", "rationing", "cupons de racionamento", "vales de racionamento", "racionamento", "配给券", "配给"],
        },
        "derogations_administratives": {
            "title": _codex_loc("Dérogations administratives", "Administrative Exemptions", "Autorizações administrativas", "行政特批"),
            "icon": "ic_doc", "assoc": ["bons_rationnement"], "auto_unlock": False,
            "short": _codex_loc("La procédure pour obtenir un bien hors ration.", "The procedure for obtaining goods outside ordinary rations.", "O procedimento para obter bens fora das rações comuns.", "获取常规配给外物品的程序。"),
            "text": _codex_loc("Les biens absents des rations ordinaires exigent une demande motivée précisant l'objet, l'usage prévu, la durée et le responsable. Même certains outils ou aliments courants deviennent ainsi difficiles à obtenir.", "Goods absent from ordinary rations require a justified request stating the item, intended use, duration and responsible person. Even some common tools or foods are therefore difficult to obtain.", "Bens que não fazem parte das rações comuns exigem uma solicitação justificada, indicando o objeto, o uso previsto, a duração e o responsável. Assim, até ferramentas ou alimentos comuns podem ser difíceis de obter.", "常规配给中没有的物品必须提交说明理由的申请，写明所需物品、预定用途、使用期限和负责人。因此，即便普通工具或食物也可能很难取得。"),
            "aliases": ["dérogations administratives", "demande de dérogation", "demander une dérogation", "dérogation", "administrative exemptions", "exemption request", "administrative authorization", "exemption", "autorização administrativa", "solicitação de autorização", "autorização", "行政特批", "特批申请", "特批"],
        },
        "commerce_monnaie": {
            "title": _codex_loc("Commerce et monnaie", "Trade and Currency", "Comércio e moeda", "贸易与货币"),
            "icon": "ic_doc", "assoc": ["bons_rationnement"], "auto_unlock": False,
            "short": _codex_loc("Les échanges économiques d'avant Kami et leurs conséquences possibles.", "Economic exchange before Kami and its possible consequences.", "As trocas econômicas anteriores a Kami e suas possíveis consequências.", "Kami掌权前的经济交换及其潜在后果。"),
            "text": _codex_loc("Avant Kami, les marchandises pouvaient être vendues et échangées contre de l'argent. Rétablir le commerce implique potentiellement le retour du travail rémunéré, des entreprises et des inégalités économiques. Les accusations de Mara contre le capitalisme expriment sa position personnelle et ne constituent pas des faits établis.", "Before Kami, goods could be sold and exchanged for money. Restoring trade could also restore paid work, businesses and economic inequality. Mara's accusations against capitalism express her personal position and are not established facts.", "Antes de Kami, mercadorias podiam ser vendidas e trocadas por dinheiro. Restaurar o comércio pode significar a volta do trabalho remunerado, das empresas e das desigualdades econômicas. As acusações de Mara contra o capitalismo expressam sua posição pessoal e não são fatos comprovados.", "Kami掌权前，商品可以出售并用货币交换。恢复贸易也可能意味着有偿劳动、企业和经济不平等的回归。Mara对资本主义的指控属于她的个人立场，并非已经证实的事实。"),
            "aliases": ["commerce et monnaie", "système de commerce", "réouverture du commerce", "commerce", "trade and currency", "restore trade", "reopening trade", "trade", "comércio e moeda", "reabrir o comércio", "comércio", "贸易与货币", "恢复贸易", "贸易"],
        },
        "frontieres_interdistricts": {
            "title": _codex_loc("Frontières interdistricts", "Interdistrict Borders", "Fronteiras interdistritais", "地区边界"),
            "icon": "ic_doc", "assoc": ["frontieres_limen"], "auto_unlock": False,
            "short": _codex_loc("L'interdiction de circuler entre les districts.", "The ban on travel between districts.", "A proibição de circulação entre distritos.", "禁止跨区通行的制度。"),
            "text": _codex_loc("Depuis la prise de pouvoir de Kami, les déplacements entre districts sont interdits. Les principaux passages sont contrôlés et toute traversée illégale peut provoquer une exécution immédiate.", "Since Kami seized power, travel between districts has been forbidden. Major crossings are controlled, and an illegal crossing can lead to immediate execution.", "Desde que Kami tomou o poder, deslocamentos entre distritos são proibidos. As principais passagens são controladas e uma travessia ilegal pode provocar execução imediata.", "Kami掌权后，地区之间禁止通行。主要通道受到管控，任何非法越界都可能遭到立即处决。"),
            "aliases": ["frontières interdistricts", "frontières entre les districts", "libre circulation entre les districts", "frontières", "interdistrict borders", "borders between districts", "free movement between districts", "borders", "fronteiras interdistritais", "fronteiras entre distritos", "livre circulação entre distritos", "fronteiras", "地区边界", "跨区通行", "边界"],
        },
        "frontieres_limen": {
            "title": _codex_loc("Frontières de Limen", "Borders of Limen", "Fronteiras de Limen", "边界区防线"),
            "icon": "ic_doc", "assoc": ["limen", "frontieres_interdistricts"], "auto_unlock": False,
            "short": _codex_loc("Les postes de contrôle gardés et leurs victimes.", "Guarded checkpoints and their victims.", "Os postos de controle vigiados e suas vítimas.", "有人驻守的检查站及其受害者。"),
            "text": _codex_loc("Les frontières limenoises sont matérialisées par des postes de contrôle et surveillées par des Gardiens. Certains habitants tentent malgré tout de les franchir et sont exécutés. Les Gardiens récupèrent ensuite les corps.", "Limen's borders are marked by checkpoints watched by Guardians. Some residents still attempt to cross and are executed. The Guardians then recover their bodies.", "As fronteiras de Limen são marcadas por postos de controle vigiados por Guardiões. Alguns habitantes ainda tentam atravessá-las e são executados. Depois, os Guardiões recolhem os corpos.", "边界区的边境由检查站标示，并由守卫监控。仍有居民试图越界并因此被处决，之后守卫会负责收回遗体。"),
            "aliases": ["frontières de Limen", "frontière de Limen", "frontières limenoises", "borders of Limen", "Limen's borders", "fronteiras de Limen", "fronteira de Limen", "边界区防线", "边界区边境"],
        },
        "complexe_c": {
            "title": _codex_loc("Complexe C", "Complex C", "Complexo C", "C号设施"),
            "icon": "ic_building", "assoc": ["orbite"], "auto_unlock": False,
            "short": _codex_loc("Ensemble résidentiel majeur d'Orbite.", "Major residential complex in Orbit.", "Grande complexo residencial de Órbita.", "轨道区的大型居住设施。"),
            "text": _codex_loc("Le complexe C est l'un des ensembles résidentiels majeurs d'Orbite : modules familiaux, production, administration, coursives pressurisées et sas capables d'isoler une section en quelques secondes. Ses habitants sont entraînés à réagir immédiatement aux alarmes.", "Complex C is one of Orbit's major residential facilities, with family, production and administrative modules, pressurized corridors and airlocks able to isolate a section within seconds. Its inhabitants are trained to respond immediately to alarms.", "O Complexo C é um dos principais conjuntos residenciais de Órbita, com módulos familiares, produtivos e administrativos, corredores pressurizados e eclusas capazes de isolar uma seção em segundos. Seus habitantes são treinados para reagir imediatamente aos alarmes.", "C号设施是轨道区的重要居住区之一，包含家庭、生产和行政舱段、加压通道，以及能在数秒内隔离区域的气闸。居民都接受过警报应急训练。"),
            "aliases": ["Complexe C", "Complex C", "Complexo C", "C号设施"],
        },
    }

    # Fusion dans CODEX_ENTRIES (sans écraser un texte déjà injecté par le scénario)
    for _eid, _data in _CODEX_DATA.items():
        if _eid not in CODEX_ENTRIES:
            CODEX_ENTRIES[_eid] = dict(_data)
        else:
            for _k, _v in _data.items():
                CODEX_ENTRIES[_eid].setdefault(_k, _v)


init 3 python:
    # Seules les entrées qui possèdent un vrai déblocage dans le scénario
    # peuvent apparaître. Tout le contenu de remplissage est retiré au chargement.
    _CODEX_INGAME_ENTRIES = set([
        "reglement_conclave",
        "harmonie", "axiome", "archive", "limen", "nexus", "orbite",
        "bons_rationnement", "derogations_administratives", "commerce_monnaie",
        "frontieres_interdistricts", "frontieres_limen",
        "complexe_c",
    ])
    for _eid in list(CODEX_ENTRIES.keys()):
        if _eid not in _CODEX_INGAME_ENTRIES:
            del CODEX_ENTRIES[_eid]

    _visible_packs = []
    for _pack in CODEX_PACKS:
        _pack["entries"] = [
            _eid for _eid in _pack["entries"] if _eid in _CODEX_INGAME_ENTRIES
        ]
        if _pack["entries"]:
            _visible_packs.append(_pack)
    CODEX_PACKS[:] = _visible_packs

    # Carte inverse entrée -> index de pack
    CODEX_ENTRY_PACK = {}
    for _pi, _p in enumerate(CODEX_PACKS):
        for _e in _p["entries"]:
            CODEX_ENTRY_PACK[_e] = _pi


init python:

    def codex_sync_unlocked_entries():
        """Fusionne l'ancien état de sauvegarde avec la progression globale."""
        persistent_entries = getattr(persistent, "codex_unlocked_entries", None)
        if not isinstance(persistent_entries, list):
            persistent_entries = []
            persistent.codex_unlocked_entries = persistent_entries

        save_entries = getattr(store, "codex_unlocked_entries", None)
        if not isinstance(save_entries, list):
            save_entries = []
            store.codex_unlocked_entries = save_entries

        persistent_changed = False

        # Migration des anciennes sauvegardes vers le profil permanent.
        for eid in save_entries:
            if eid not in persistent_entries:
                persistent_entries.append(eid)
                persistent_changed = True

        # Une nouvelle partie retrouve immédiatement tous les déblocages globaux.
        for eid in persistent_entries:
            if eid not in save_entries:
                save_entries.append(eid)

        if persistent_changed:
            renpy.save_persistent()

        return persistent_entries

    # ---- Accès données ----
    def codex_language_key():
        language = getattr(store._preferences, "language", None)
        return language if language in ("english", "portuguese", "chinese") else "fr"

    def codex_localized_value(value):
        if not isinstance(value, dict):
            return value
        return value.get(codex_language_key(), value.get("fr", ""))

    def codex_entry(eid):
        return CODEX_ENTRIES.get(eid, {})

    def codex_entry_title(eid):
        return codex_localized_value(codex_entry(eid).get("title", eid))

    def codex_entry_icon(eid):
        return codex_entry(eid).get("icon", "ic_doc")

    def codex_entry_short(eid):
        return codex_localized_value(codex_entry(eid).get("short", ""))

    def codex_entry_text(eid):
        return codex_localized_value(codex_entry(eid).get("text", ""))

    def codex_entry_assoc(eid):
        return [a for a in codex_entry(eid).get("assoc", []) if a in CODEX_ENTRIES]

    def codex_is_unlocked(eid):
        return eid in codex_sync_unlocked_entries()

    def codex_pack_index_of(eid):
        return CODEX_ENTRY_PACK.get(eid, 0)

    # ---- Déblocage ----
    def codex_unlock_page(eid, with_notification=True):
        unlocked_entries = codex_sync_unlocked_entries()
        if eid in CODEX_ENTRIES and eid not in unlocked_entries:
            unlocked_entries.append(eid)
            if eid not in store.codex_unlocked_entries:
                store.codex_unlocked_entries.append(eid)
            renpy.save_persistent()
            renpy.restart_interaction()
            return True
        return False

    def unlock_codex_page(eid, with_notification=True):
        return codex_unlock_page(eid, with_notification=with_notification)

    def unlock_codex_entry(eid):
        return codex_unlock_page(eid, with_notification=True)

    # ---- Filtre ----
    def codex_filter_ok(eid, filt):
        if filt == "debloques":
            return codex_is_unlocked(eid)
        if filt == "verrouilles":
            return not codex_is_unlocked(eid)
        return True

    # ---- Packs ----
    def codex_pack_unlocked_count(pack):
        return sum(1 for e in pack["entries"] if codex_is_unlocked(e))

    def codex_pack_total(pack):
        return len(pack["entries"])

    def codex_first_entry_of_pack(pack_index):
        return CODEX_PACKS[pack_index]["entries"][0]

    def codex_total_unlocked():
        return sum(1 for e in codex_sync_unlocked_entries() if e in CODEX_ENTRIES)

    def codex_total_entries():
        return len(CODEX_ENTRIES)

    # ---- Détection et liens automatiques dans les dialogues ----
    def codex_dialogue_link(eid, label):
        """Ancre de compatibilité pour les anciens dialogues traduits."""
        return "{a=codex:%s}{color=#F0C24B}{b}%s{/b}{/color}{/a}" % (eid, label)

    def _codex_is_cjk(value):
        return any("\u3400" <= char <= "\u9fff" for char in value)

    def _codex_alias_pattern(alias):
        escaped = re.escape(alias)
        if _codex_is_cjk(alias):
            return re.compile(escaped, re.IGNORECASE)
        return re.compile(r"(?<!\w)%s(?!\w)" % escaped, re.IGNORECASE)

    CODEX_TEXT_PATTERNS = []
    for _entry_id, _entry_data in CODEX_ENTRIES.items():
        for _alias in _entry_data.get("aliases", []):
            if _alias:
                CODEX_TEXT_PATTERNS.append((_codex_alias_pattern(_alias), _entry_id, len(_alias)))
    CODEX_TEXT_PATTERNS.sort(key=lambda item: -item[2])

    def codex_plain_dialogue_text(value):
        if value is None:
            return ""
        return re.sub(r"\{[^{}]*\}", " ", str(value))

    def codex_entries_in_text(value, auto_unlock_only=False):
        plain_text = codex_plain_dialogue_text(value)
        found = []
        for pattern, eid, alias_length in CODEX_TEXT_PATTERNS:
            if auto_unlock_only and not codex_entry(eid).get("auto_unlock", False):
                continue
            if eid not in found and pattern.search(plain_text):
                found.append(eid)
        return found

    def codex_discover_from_text(value):
        """Débloque en une fois les districts découverts dans le texte traduit."""
        discovered = codex_entries_in_text(value, auto_unlock_only=True)
        unlocked_entries = codex_sync_unlocked_entries()
        new_entries = [eid for eid in discovered if eid not in unlocked_entries]
        if not new_entries:
            return

        for eid in new_entries:
            unlocked_entries.append(eid)
            if eid not in store.codex_unlocked_entries:
                store.codex_unlocked_entries.append(eid)
        renpy.save_persistent()
        renpy.restart_interaction()

    def _codex_autolink_segment(segment):
        candidates = []
        for pattern, eid, alias_length in CODEX_TEXT_PATTERNS:
            entry = codex_entry(eid)
            # Les districts sont balisés dès leur première mention. L'action
            # du say screen les débloque avant que le joueur puisse cliquer.
            if not codex_is_unlocked(eid) and not entry.get("auto_unlock", False):
                continue
            for match in pattern.finditer(segment):
                candidates.append((match.start(), match.end(), -alias_length, eid))

        if not candidates:
            return segment

        candidates.sort()
        selected = []
        cursor = 0
        for start, end, negative_length, eid in candidates:
            if start < cursor:
                continue
            selected.append((start, end, eid))
            cursor = end

        result = []
        cursor = 0
        for start, end, eid in selected:
            result.append(segment[cursor:start])
            label = segment[start:end]
            result.append("{a=codex:%s}{color=#F0C24B}{b}%s{/b}{/color}{/a}" % (eid, label))
            cursor = end
        result.append(segment[cursor:])
        return "".join(result)

    def codex_autolink_text(value):
        """Ajoute les liens sans toucher aux balises Ren'Py ou aux liens existants."""
        if value is None:
            return value

        parts = re.split(r"(\{[^{}]*\})", str(value))
        link_depth = 0
        output = []
        for part in parts:
            if not part:
                continue
            if part.startswith("{") and part.endswith("}"):
                low = part.lower()
                if low.startswith("{a="):
                    link_depth += 1
                elif low == "{/a}" and link_depth:
                    link_depth -= 1
                output.append(part)
            elif link_depth:
                output.append(part)
            else:
                output.append(_codex_autolink_segment(part))
        return "".join(output)

    def codex_say_menu_text_filter(value):
        """Balisage en amont du say screen, sans altérer ses interpolations.

        Ren'Py impose que le widget ``what`` reçoive exactement la valeur
        transmise au screen. Le filtre officiel est donc utilisé avant
        l'affichage. Les blocs ``[...]`` sont laissés intacts afin que les
        variables et les anciennes ancres de traduction restent valides.
        """
        if value is None:
            return value

        parts = re.split(r"(\[\[|\[[^\[\]\r\n]*\])", str(value))
        return "".join(
            part if part.startswith("[") else codex_autolink_text(part)
            for part in parts
        )

    def codex_hyperlink_handler(eid):
        if codex_is_unlocked(eid):
            renpy.call_in_new_context("codex_hyperlink_view", eid)

    config.hyperlink_handlers["codex"] = codex_hyperlink_handler
    config.hyperlink_sensitive["codex"] = codex_is_unlocked
    config.say_menu_text_filter = codex_say_menu_text_filter

    # ---- Debug ----
    def codex_unlock_all_debug():
        unlocked_entries = codex_sync_unlocked_entries()
        changed = False
        for e in CODEX_ENTRIES:
            if e not in unlocked_entries:
                unlocked_entries.append(e)
                changed = True
            if e not in store.codex_unlocked_entries:
                store.codex_unlocked_entries.append(e)
        if changed:
            renpy.save_persistent()
        renpy.restart_interaction()


# =============================================================================
# ÉCRAN PRINCIPAL
# =============================================================================

transform codex_tint(c):
    matrixcolor TintMatrix(c)


screen codex_menu(initial_entry=None):
    tag menu
    modal True
    zorder 100

    default sel_pack = codex_pack_index_of(initial_entry) if initial_entry in CODEX_ENTRIES else 0
    default sel_entry = initial_entry if initial_entry in CODEX_ENTRIES else codex_first_entry_of_pack(0)
    default filt = "tous"

    add Solid("#05090F")
    add Solid("#070D15") ypos 92 ysize 988

    # ---------------- HEADER ----------------
    add "hud/codex/codex_logo.png" xpos 30 ypos 26 xysize (44, 44)
    text "CODEX":
        xpos 92 ypos 26 size 40 color "#DCEBFF"
        font "fonts/Rajdhani-SemiBold.ttf" kerning 6

    frame:
        xpos 1400 ypos 26 xsize 320 ysize 46
        background Frame(Solid("#0A1622"), 0, 0)
        fixed:
            add Solid("#5CD3FF") xpos 0 ypos 0 xsize 320 ysize 1
            text "ENTRÉES DÉBLOQUÉES":
                xpos 20 yalign 0.5 size 15 color "#6E8CA6"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text "[codex_total_unlocked()] / [codex_total_entries()]":
                xpos 234 yalign 0.5 size 22 color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1

    button:
        xpos 1840 ypos 24 xysize (50, 50)
        background Frame(Solid("#0A1622"), 0, 0)
        hover_background Frame(Solid("#5CD3FF22"), 0, 0)
        action Return()
        text "✕" xalign 0.5 yalign 0.5 size 26 color "#8FB4CC"

    add Solid("#12283A") xpos 0 ypos 90 xsize 1920 ysize 2

    # ---------------- COLONNE 1 : PACKS ----------------
    frame:
        xpos 24 ypos 112 xsize 470 ysize 900
        background Frame(Solid("#0A121C"), 0, 0)
        padding (0, 0)
        fixed:
            add Solid("#5CD3FF") xpos 0 ypos 0 xsize 470 ysize 2
            text "PACKS":
                xpos 24 ypos 18 size 20 color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 4
            add Solid("#12283A") xpos 0 ypos 58 xsize 470 ysize 1

            viewport:
                xpos 0 ypos 66 xsize 470 ysize 770
                mousewheel True draggable True scrollbars "vertical"
                vbox:
                    spacing 0
                    for pi, pack in enumerate(CODEX_PACKS):
                        use codex_pack_row(pi, pack, sel_pack)

            add Solid("#12283A") xpos 0 ypos 840 xsize 470 ysize 1
            button:
                xpos 20 ypos 852 xsize 130 ysize 40
                background Frame(Solid("#0E1B28"), 0, 0)
                hover_background Frame(Solid("#5CD3FF18"), 0, 0)
                action SetScreenVariable("filt", {"tous": "debloques", "debloques": "verrouilles", "verrouilles": "tous"}[filt])
                hbox:
                    yalign 0.5 xpos 12 spacing 8
                    add "hud/codex/ic_filter.png" yalign 0.5 xysize (18, 18) at codex_tint("#8FB4CC")
                    text "FILTRES" yalign 0.5 size 15 color "#8FB4CC" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            frame:
                xpos 164 ypos 852 xsize 220 ysize 40
                background Frame(Solid("#0E1B28"), 0, 0)
                text ({"tous": "TOUS", "debloques": "DÉBLOQUÉS", "verrouilles": "VERROUILLÉS"}[filt]):
                    xpos 16 yalign 0.5 size 15 color "#B9D4E6" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                add "hud/codex/ic_chevron.png" xpos 188 yalign 0.5 xysize (18, 18) at codex_tint("#8FB4CC")

    # ---------------- COLONNE 2 : ENTRÉES ----------------
    $ cur_pack = CODEX_PACKS[sel_pack]
    frame:
        xpos 512 ypos 112 xsize 856 ysize 900
        background Frame(Solid("#0A121C"), 0, 0)
        padding (0, 0)
        fixed:
            add Solid(cur_pack["color"]) xpos 0 ypos 0 xsize 856 ysize 2
            text "ENTRÉES DU PACK : [cur_pack['title']]":
                xpos 24 ypos 18 size 18 color "#B9D4E6"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text "[codex_pack_unlocked_count(cur_pack)] / [codex_pack_total(cur_pack)]":
                xpos 780 ypos 18 size 18 color cur_pack["color"]
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            add Solid("#12283A") xpos 0 ypos 58 xsize 856 ysize 1

            viewport:
                xpos 0 ypos 70 xsize 856 ysize 826
                mousewheel True draggable True scrollbars "vertical"
                vpgrid:
                    cols 2
                    xspacing 16 yspacing 16
                    xpos 24 ypos 8
                    for idx, eid in enumerate(cur_pack["entries"]):
                        if codex_filter_ok(eid, filt):
                            use codex_entry_card(idx, eid, cur_pack, sel_entry)

    # ---------------- COLONNE 3 : DÉTAIL ----------------
    use codex_detail_panel(sel_entry, cur_pack)


# -----------------------------------------------------------------------------
# LIGNE PACK
# -----------------------------------------------------------------------------
screen codex_pack_row(pi, pack, sel_pack):
    $ col = pack["color"]
    $ nb = codex_pack_unlocked_count(pack)
    $ tot = codex_pack_total(pack)
    $ ratio = (float(nb) / tot) if tot else 0.0
    $ selected = (pi == sel_pack)

    button:
        xsize 470 ysize 156
        background (Frame(Solid("#0E1E2C"), 0, 0) if selected else Frame(Solid("#00000000"), 0, 0))
        hover_background Frame(Solid(col + "12"), 0, 0)
        action [SetScreenVariable("sel_pack", pi),
                SetScreenVariable("sel_entry", codex_first_entry_of_pack(pi))]
        fixed:
            xsize 470 ysize 156
            if selected:
                add Solid(col) xpos 0 ypos 0 xsize 4 ysize 156
            add Solid("#0A1420") xpos 0 ypos 155 xsize 470 ysize 1

            frame:
                xpos 22 ypos 24 xysize (64, 64)
                background Frame(Solid(col + "16"), 0, 0)
                add ("hud/codex/" + pack["icon"] + ".png") xalign 0.5 yalign 0.5 xysize (42, 42)

            text "[pack['num']]. [pack['title']]":
                xpos 100 ypos 22 size 21 color ("#EAF4FF" if selected else "#C6D9E8")
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            text "[nb] / [tot]":
                xpos 408 ypos 24 size 18 color col font "fonts/Rajdhani-SemiBold.ttf"

            text pack["subtitle"]:
                xpos 100 ypos 50 size 15 color "#7C99AC" font "fonts/Barlow-Light.ttf" line_leading 2

            add Solid("#132433") xpos 100 ypos 104 xsize 346 ysize 6
            if ratio > 0:
                add Solid(col) xpos 100 ypos 104 xsize int(346 * ratio) ysize 6



# -----------------------------------------------------------------------------
# CARTE ENTRÉE
# -----------------------------------------------------------------------------
screen codex_entry_card(idx, eid, pack, sel_entry):
    $ col = pack["color"]
    $ unlocked = codex_is_unlocked(eid)
    $ selected = (eid == sel_entry)
    $ num = "%02d" % (idx + 1)

    button:
        xsize 396 ysize 150
        background Frame(Solid("#0B1520"), 0, 0)
        hover_background Frame(Solid(col + "10"), 0, 0)
        action SetScreenVariable("sel_entry", eid)
        sensitive unlocked
        fixed:
            xsize 396 ysize 150
            if selected and unlocked:
                add Solid(col + "10") xpos 0 ypos 0 xsize 396 ysize 150
                add Solid(col) xpos 0 ypos 0 xsize 396 ysize 2
                add Solid(col) xpos 0 ypos 0 xsize 2 ysize 150
                add Solid(col) xpos 394 ypos 0 xsize 2 ysize 150
                add Solid(col) xpos 0 ypos 148 xsize 396 ysize 2
            else:
                add Solid("#16283A") xpos 0 ypos 0 xsize 396 ysize 1

            text num:
                xpos 20 ypos 18 size 15 color (col if unlocked else "#3C4E5E")
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2

            frame:
                xpos 20 ypos 44 xysize (58, 58)
                background Frame(Solid((col + "16") if unlocked else "#101E2A"), 0, 0)
                if unlocked:
                    add ("hud/codex/" + codex_entry_icon(eid) + ".png") xalign 0.5 yalign 0.5 xysize (36, 36) at codex_tint(col)
                else:
                    add "hud/codex/badge_lock.png" xalign 0.5 yalign 0.5 xysize (30, 30) at codex_tint("#3C4E5E")

            if unlocked:
                text codex_entry_title(eid):
                    xpos 96 ypos 20 size 19 color "#E4F1FB" font "fonts/Rajdhani-SemiBold.ttf" kerning 1
                text codex_entry_short(eid):
                    xpos 96 ypos 50 xsize 280 size 14 color "#8AA6B9" font "fonts/Barlow-Light.ttf" line_leading 2
                add "hud/codex/badge_check.png" xpos 356 ypos 108 xysize (24, 24) at codex_tint(col)
            else:
                text "???":
                    xpos 96 ypos 20 size 19 color "#4A5E70" font "fonts/Rajdhani-SemiBold.ttf" kerning 1
                text "Entrée non découverte\nencore.":
                    xpos 96 ypos 50 size 14 color "#4A5E70" font "fonts/Barlow-Light.ttf" line_leading 2


# -----------------------------------------------------------------------------
# PANNEAU DÉTAIL
# -----------------------------------------------------------------------------
screen codex_detail_panel(eid, pack):
    $ col = pack["color"]
    $ unlocked = codex_is_unlocked(eid)
    $ idx = (pack["entries"].index(eid) if eid in pack["entries"] else 0)
    $ num = "%02d" % (idx + 1)

    frame:
        xpos 1386 ypos 112 xsize 510 ysize 900
        background Frame(Solid("#0A121C"), 0, 0)
        padding (0, 0)
        fixed:
            add Solid(col) xpos 0 ypos 0 xsize 510 ysize 2

            frame:
                xpos 24 ypos 20 xysize (54, 40)
                background Frame(Solid(col + "1E"), 0, 0)
                text num xalign 0.5 yalign 0.5 size 20 color col font "fonts/Rajdhani-SemiBold.ttf" kerning 1

            if unlocked:
                text codex_entry_title(eid):
                    xpos 92 ypos 18 size 26 color "#EAF4FF" font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            else:
                text "???":
                    xpos 92 ypos 18 size 26 color "#4A5E70" font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            text "PACK [pack['num']] - [pack['title']]":
                xpos 94 ypos 50 size 13 color "#6E8CA6" font "fonts/Rajdhani-SemiBold.ttf" kerning 2

            if unlocked:
                add ("hud/codex/" + pack["banner"] + ".png") xpos 24 ypos 84 xysize (462, 220)
            else:
                add ("hud/codex/" + pack["banner"] + ".png") xpos 24 ypos 84 xysize (462, 220) at codex_lockdim
                add "hud/codex/badge_lock.png" xpos 232 ypos 172 xysize (44, 44) at codex_tint("#7C99AC")

            if unlocked:
                viewport:
                    xpos 24 ypos 322 xsize 462 ysize 500
                    mousewheel True draggable True scrollbars "vertical"
                    text codex_entry_text(eid):
                        xsize 440 size 17 color "#C4D6E4" font "fonts/Barlow-Light.ttf" line_leading 4
            else:
                text "Entrée non découverte encore.":
                    xpos 24 ypos 340 size 17 color "#54697B" font "fonts/Barlow-Light.ttf"

            if unlocked and codex_entry_assoc(eid):
                text "INFORMATIONS ASSOCIÉES":
                    xpos 24 ypos 552 size 14 color "#6E8CA6" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                hbox:
                    xpos 24 ypos 582 spacing 10
                    for aid in codex_entry_assoc(eid)[:2]:
                        button:
                            ysize 40 padding (14, 8)
                            background Frame(Solid("#0E1B28"), 0, 0)
                            hover_background Frame(Solid(col + "1A"), 0, 0)
                            sensitive codex_is_unlocked(aid)
                            action [SetScreenVariable("sel_pack", codex_pack_index_of(aid)),
                                    SetScreenVariable("sel_entry", aid)]
                            text (codex_entry_title(aid) if codex_is_unlocked(aid) else "???"):
                                yalign 0.5 size 15 color (col if codex_is_unlocked(aid) else "#4A5E70")
                                font "fonts/Rajdhani-SemiBold.ttf"

transform codex_lockdim:
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.35)


label codex_hyperlink_view(entry_id):
    call screen codex_menu(initial_entry=entry_id)
    return
