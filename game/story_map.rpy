default story_map_target_label = None

init python:
    STORY_MAP_ROUTES = [
        {
            "id": "route_main",
            "name": "Trame principale",
            "nodes": [
                {"id": "D0", "title": "Jour 0", "label": "_0_CANON", "requires": [], "summary": "Un an après la prise de contrôle mondiale de Kami, Noam assiste à une réunion ordinaire du district Harmonie. Kami interrompt la séance pour annoncer les Kami’s Desires : un Conclave de 30 jours où douze représentants devront voter à l’unanimité pour modifier les Commandements."},
                {"id": "D1", "title": "Jour 1", "label": "_1_CANON", "requires": ["D0"], "summary": "Noam se réveille avec les autres représentants dans le Conclave et le visite. Kami apparaît et révèle les règles : trente jours d’isolement, des amendements anonymes, un vote tous les trois jours et l'unanimité est obligatoire pour apporter des modifications aux Commandements."},
                {"id": "D2", "title": "Jour 2", "label": "_2_CANON", "requires": ["D1"], "summary": "Kami annonce le premier vote du Conclave : autoriser le transport, la vente et l’échange de marchandises entre districts. Les représentants comprennent qu’ils n’ont qu’une journée pour débattre, ce qui fait remonter les peurs, les inégalités et les intérêts propres à chaque district."},
                {"id": "D3", "title": "Jour 3", "label": "_3_CANON", "requires": ["D2"], "summary": "Le premier vote approche et les tensions explosent autour de l’amendement sur le commerce et les bons de rationnement. Entre débats, soupçons de manipulation et affrontements idéologiques, les représentants doivent choisir entre ouvrir les échanges ou maintenir le système actuel."},
                
                {"id": "D4A", "title": "Jour 4", "label": "_4_0_REVEIL_CHAMBRE", "requires": ["D3"], "summary": "Après l’échec du vote sur le commerce, le Conclave s’enfonce dans la frustration et le regret. Kami annonce un nouveau vote sur la libre circulation entre districts, mais le sujet fracture aussitôt le groupe, notamment avec l’opposition frontale de Sael."},
                {"id": "D5A", "title": "Jour 5", "label": "_5_0_REVEIL_CHAMBRE", "requires": ["D4A"], "summary": "À la veille du vote sur la libre circulation, Noam constate que Sael, Mara et Iris voteront contre. Selon son choix, il confronte Julian sur son besoin de mise en scène ou provoque avec Elias un incident dans la salle d’observation qui endommage accidentellement une console."},
                {"id": "D6AA", "title": "Jour 6", "label": "_6_0_0_REVEIL_CHAMBRE", "requires": ["D5A"], "summary": "Résumé à écrire."},
                
                {"id": "D6_0_1", "title": "Jour 6", "label": "_6_0_1_REVEIL_CHAMBRE", "requires": ["D5A"], "summary": "Le vote sur la libre circulation tourne au fiasco : Kami semble instable, son discours se déforme et elle laisse échapper une menace inquiétante. Face à un texte incompréhensible et au risque d’une application incontrôlée, le Conclave rejette massivement l’amendement."},
                {"id": "D7_0_1", "title": "Jour 7", "label": "_7_0_1_REVEIL_CHAMBRE", "requires": ["D6_0_1"], "summary": "Pour la première fois, Kami reste silencieuse et le Conclave connaît une journée presque normale, entre grasse matinée, repas détendus et discussions sans vote. Mais Tomas découvre qu’il n’y a plus aucune exécution dans le monde, tandis que du matériel disparaît mystérieusement dans le Conclave."},
                {"id": "D8_0_1", "title": "Jour 8", "label": "_8_0_1_REVEIL_CHAMBRE", "requires": ["D7_0_1"], "summary": "Le silence de Kami continue, mais le calme se fissure : Noam découvre que le dessin de Juliette a disparu, puis Kael explose en apprenant que la photo de sa sœur a aussi été volée. Le Conclave comprend que quelqu'un cible leurs souvenirs les plus personnels."},
                {"id": "D9_0_1", "title": "Jour 9", "label": "_9_0_1_REVEIL_CHAMBRE", "requires": ["D8_0_1"], "summary": "???"},

                {"id": "D4B", "title": "Jour 4", "label": "_4_1_REVEIL_CHAMBRE", "requires": ["D3"], "summary": "Après l’adoption du commerce libre, le Conclave découvre déjà ses conséquences : Nexus et Orbite s’organisent, tandis que Limen vacille. Kami annonce ensuite un nouveau vote sur la libre circulation entre districts, provoquant un violent clash avec Sael. La soirée s'apaise ensuite autour d'une soirée improvisée."},
                {"id": "D5B", "title": "Jour 5", "label": "_5_1_REVEIL_CHAMBRE", "requires": ["D4B"], "summary": "Kami annonce qu’une alerte a frappé le complexe C-3 d’Orbite, laissant Kael rongé par l’angoisse pour sa petite sœur qui vit sur place. Alors que le vote sur la libre circulation approche, Noam reçoit anonymement une étrange note faison référence au règlement : les absents ne comptent pas dans l’unanimité."},
                {"id": "D6BA", "title": "Jour 6", "label": "_6_1_0_REVEIL_CHAMBRE", "requires": ["D5B"], "summary": "Résumé à écrire."},

                {"id": "D6BB", "title": "Jour 6", "label": "_6_1_1_REVEIL_CHAMBRE", "requires": ["D5B"], "summary": "Résumé à écrire."},
            ],
        },
        {
            "id": "route_debat",
            "name": "Branche débat",
            "nodes": [
                {"id": "DB1", "title": "Débat P1", "label": "_3_CAFETERIA_DEBAT", "requires": [], "summary": "Résumé à écrire."},
                {"id": "DB2", "title": "Débat P2", "label": "_3_DEBAT1_PHASE2", "requires": ["DB1"], "summary": "Résumé à écrire."},
                {"id": "DB3", "title": "Débat P3", "label": "_3_DEBAT1_PHASE3", "requires": ["DB2"], "summary": "Résumé à écrire."},
                {"id": "VOTE", "title": "Vote final", "label": "vote_phase3_final", "requires": ["DB3"], "summary": "Résumé à écrire."},
            ],
        },
    ]

    def _story_node_seen(node):
        return renpy.seen_label(node["label"])

    def _story_node_visible(node):
        return _story_node_seen(node)

    def _story_node_unlocked(node, nodes_by_id):
        if _story_node_seen(node):
            return True
        for requirement in node.get("requires", []):
            if requirement not in nodes_by_id:
                return False
            if not _story_node_seen(nodes_by_id[requirement]):
                return False
        return True

    def _story_route_layout(route_nodes):
        if not route_nodes:
            return {"nodes": [], "edges": [], "width": 2200, "height": 1200}
        node_w, node_h, margin, step_x, step_y = 270, 118, 180, 340, 180
        nodes_by_id = {n["id"]: n for n in route_nodes}
        node_index = {n["id"]: idx for idx, n in enumerate(route_nodes)}
        children = {n["id"]: [] for n in route_nodes}
        for n in route_nodes:
            for req in n.get("requires", []):
                if req in children:
                    children[req].append(n["id"])
        depth_memo = {}
        def depth_for(node_id):
            if node_id in depth_memo:
                return depth_memo[node_id]
            reqs = [r for r in nodes_by_id[node_id].get("requires", []) if r in nodes_by_id]
            depth_memo[node_id] = 0 if not reqs else 1 + max(depth_for(r) for r in reqs)
            return depth_memo[node_id]
        depths = {n["id"]: depth_for(n["id"]) for n in route_nodes}
        ordered = sorted(route_nodes, key=lambda n: (depths[n["id"]], node_index[n["id"]]))
        lanes, occupied, root_lane = {}, {}, 0
        branch_offsets = [0, -1, 1, -2, 2, -3, 3, -4, 4]
        for node in ordered:
            nid, depth = node["id"], depths[node["id"]]
            occupied.setdefault(depth, set())
            reqs = [r for r in node.get("requires", []) if r in lanes]
            if not reqs:
                lane = root_lane; root_lane += 2
            else:
                main_parent = reqs[0]
                siblings = [s for s in children.get(main_parent, []) if s in nodes_by_id]
                s_idx = siblings.index(nid) if nid in siblings else 0
                offset = branch_offsets[s_idx] if s_idx < len(branch_offsets) else s_idx
                lane = lanes[main_parent] + offset
            while lane in occupied[depth]: lane += 1
            lanes[nid] = lane; occupied[depth].add(lane)
        lane_shift = -min(lanes.values()) if min(lanes.values()) < 0 else 0
        positioned_nodes = []
        for node in route_nodes:
            nid = node["id"]
            x = margin + depths[nid] * step_x
            y = margin + (lanes[nid] + lane_shift) * step_y
            positioned_nodes.append({"node": node, "x": x, "y": y, "w": node_w, "h": node_h, "cx": x + node_w//2, "cy": y + node_h//2})
        by_id = {p["node"]["id"]: p for p in positioned_nodes}
        edges = []
        for p in positioned_nodes:
            node = p["node"]
            for req in node.get("requires", []):
                if req not in by_id: continue
                parent = by_id[req]
                edges.append({"sx": parent["x"]+parent["w"], "sy": parent["cy"], "mx": parent["x"]+parent["w"]+40, "ey": p["cy"], "ex": p["x"], "branch": len(node.get("requires", []))>1 or node["id"].endswith("B")})
        width = max((p["x"] + p["w"] for p in positioned_nodes), default=2200) + margin
        height = max((p["y"] + p["h"] for p in positioned_nodes), default=1200) + margin
        return {"nodes": positioned_nodes, "edges": edges, "width": max(2200, width), "height": max(1200, height)}

screen story_map_menu():
    tag menu
    zorder 210
    modal True
    default selected_route_id = STORY_MAP_ROUTES[0]["id"] if STORY_MAP_ROUTES else None
    default hovered_node_id = None
    $ current_route = next((r for r in STORY_MAP_ROUTES if r["id"] == selected_route_id), STORY_MAP_ROUTES[0] if STORY_MAP_ROUTES else None)
    $ route_nodes = current_route["nodes"] if current_route else []
    $ nodes_by_id = {node["id"]: node for node in route_nodes}
    $ layout = _story_route_layout(route_nodes)
    $ current_seen = [n for n in route_nodes if _story_node_seen(n)]
    $ current_day_node = current_seen[-1] if current_seen else (route_nodes[0] if route_nodes else None)
    $ hovered_node = nodes_by_id.get(hovered_node_id, None)

    add Solid("#020716")
    add "images/background/bg_menu.png" at cover_screen
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1760
        ysize 950
        padding (26, 22)
        background Solid("#040f22e8")
        vbox:
            spacing 14
            text "STORY MAP // ITERATION FLOW" xalign 0.5 size 44 color "#8ef3ff"
            text "Une case s'affiche seulement après avoir vu son label au moins une fois." xalign 0.5 size 21 color "#a6d3ff"
            hbox:
                xalign 0.5
                spacing 14
                for route in STORY_MAP_ROUTES:
                    textbutton "[route['name']]":
                        xminimum 280
                        yminimum 48
                        background Solid("#0c1c38")
                        hover_background Solid("#173765")
                        if selected_route_id == route["id"]:
                            background Solid("#2ec4ff")
                            hover_background Solid("#68d9ff")
                        action [SetScreenVariable("selected_route_id", route["id"]), SetScreenVariable("hovered_node_id", None)]
            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                scrollbars "both"
                fixed:
                    xsize layout["width"]
                    ysize layout["height"]
                    for edge in layout["edges"]:
                        $ edge_color = "#ff8f2e" if edge["branch"] else "#45dfff"
                        add Solid(edge_color) xpos edge["sx"] ypos edge["sy"] xsize max(2, edge["mx"] - edge["sx"]) ysize 3
                        if edge["ey"] >= edge["sy"]:
                            add Solid(edge_color) xpos edge["mx"] ypos edge["sy"] xsize 3 ysize max(2, edge["ey"] - edge["sy"])
                        else:
                            add Solid(edge_color) xpos edge["mx"] ypos edge["ey"] xsize 3 ysize max(2, edge["sy"] - edge["ey"])
                        add Solid(edge_color) xpos edge["mx"] ypos edge["ey"] xsize max(2, edge["ex"] - edge["mx"]) ysize 3
                    for positioned in layout["nodes"]:
                        $ node = positioned["node"]
                        $ is_visible = _story_node_visible(node)
                        $ is_unlocked = _story_node_unlocked(node, nodes_by_id)
                        $ node_bg = "#0f3352" if is_visible else ("#2d3b4a" if is_unlocked else "#151d28")
                        $ hover_bg = "#1b4f7a" if is_visible else node_bg
                        if is_visible:
                            button:
                                xpos positioned["x"]
                                ypos positioned["y"]
                                xsize positioned["w"]
                                ysize positioned["h"]
                                background Solid(node_bg)
                                hover_background Solid(hover_bg)
                                hovered SetScreenVariable("hovered_node_id", node["id"])
                                unhovered SetScreenVariable("hovered_node_id", None)
                                action [SetVariable("story_map_target_label", node["label"]), Start()]

                                text "[node['id']] • [node['title']]":
                                    xalign 0.5
                                    yalign 0.5
                                    size 22
                                    color "#bff5ff"
                        else:
                            frame:
                                xpos positioned["x"]
                                ypos positioned["y"]
                                xsize positioned["w"]
                                ysize positioned["h"]
                                background Solid(node_bg)

                                if is_unlocked:
                                    text "[node['id']] • [node['title']]":
                                        xalign 0.5
                                        yalign 0.5
                                        size 22
                                        color "#98b7ce"
                                else:
                                    text "🔒 [node['id']]":
                                        xalign 0.5
                                        yalign 0.5
                                        size 24
                                        color "#6f8398"

    frame:
        xalign 0.5
        yalign 0.94
        xsize 1700
        ysize 120
        padding (18, 14)
        background Solid("#07192cdf")
        vbox:
            spacing 6
            if hovered_node:
                text "[hovered_node['title']] ([hovered_node['id']])" size 24 color "#8ef3ff"
                text "[hovered_node.get('summary', 'Résumé à écrire.')]" size 20 color "#d8e9ff"
            else:
                text "Survole une journée pour afficher son résumé." size 22 color "#8faeca"

    textbutton "Retour":
        xalign 0.03
        yalign 0.05
        action Return()
