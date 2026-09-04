################################################################################
## KAEL // TRACE — envoi asynchrone des scores vers le site
################################################################################

default online_score_status = "idle"
default online_score_message = ""
default online_score_best = 0


init python:
    import json
    import ssl
    import sys
    import uuid
    import urllib.error
    import urllib.request

    # À personnaliser avant de distribuer le jeu. La même valeur doit être
    # configurée dans kd_website/config.php (ou KD_GAME_API_KEY sur le serveur).
    ONLINE_SCORE_API_URL = "https://kamisdesires.com/api.php?action=submitScore"
    ONLINE_SCORE_GAME_KEY = "KD2026APIKEY"
    ONLINE_SCORE_TIMEOUT = 8

    def _online_ssl_context():
        """Crée un contexte TLS validé, y compris avec le magasin Windows.

        Le Python embarqué de Ren'Py n'utilise pas toujours les autorités de
        certification approuvées par Windows (antivirus HTTPS compris).
        """
        context = ssl.create_default_context()

        try:
            import certifi
            context.load_verify_locations(cafile=certifi.where())
        except Exception:
            pass

        if sys.platform != "win32":
            return context

        try:
            import ctypes

            class CertificateContext(ctypes.Structure):
                _fields_ = [
                    ("encoding_type", ctypes.c_uint32),
                    ("encoded", ctypes.POINTER(ctypes.c_ubyte)),
                    ("encoded_size", ctypes.c_uint32),
                    ("certificate_info", ctypes.c_void_p),
                    ("certificate_store", ctypes.c_void_p),
                ]

            crypt32 = ctypes.WinDLL("crypt32", use_last_error=True)
            open_store = crypt32.CertOpenStore
            open_store.argtypes = [
                ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p,
                ctypes.c_uint32, ctypes.c_wchar_p,
            ]
            open_store.restype = ctypes.c_void_p
            enum_certificates = crypt32.CertEnumCertificatesInStore
            enum_certificates.argtypes = [
                ctypes.c_void_p, ctypes.POINTER(CertificateContext),
            ]
            enum_certificates.restype = ctypes.POINTER(CertificateContext)
            close_store = crypt32.CertCloseStore
            close_store.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            close_store.restype = ctypes.c_int

            # Magasins ROOT de l'utilisateur puis de la machine locale.
            for location in (0x00010000, 0x00020000):
                certificate_store = open_store(
                    ctypes.c_void_p(10), 0, None, location | 0x00004000, "ROOT"
                )
                if not certificate_store:
                    continue

                previous = ctypes.POINTER(CertificateContext)()
                try:
                    while True:
                        certificate = enum_certificates(certificate_store, previous)
                        if not certificate:
                            break
                        encoded = ctypes.string_at(
                            certificate.contents.encoded,
                            certificate.contents.encoded_size,
                        )
                        context.load_verify_locations(
                            cadata=ssl.DER_cert_to_PEM_cert(encoded)
                        )
                        previous = certificate
                finally:
                    close_store(certificate_store, 0)
        except Exception as exc:
            print("Impossible de charger les certificats Windows : {!r}".format(exc))

        return context

    def online_ensure_player_id():
        """Retourne l'identifiant permanent du profil local."""
        if not persistent.kael_player_id:
            persistent.kael_player_id = "ID_" + uuid.uuid4().hex.upper()
            renpy.save_persistent()
        return persistent.kael_player_id

    def _online_score_show_result(status, message, best_score=0):
        """Met à jour l'interface. Cette fonction s'exécute sur le fil principal."""
        store.online_score_status = status
        store.online_score_message = message
        store.online_score_best = int(best_score or 0)
        renpy.notify(message)
        renpy.restart_interaction()

    def _online_score_request(player_id, pseudo, level_id, score):
        """Effectue la requête réseau depuis le fil d'arrière-plan."""
        try:
            payload = json.dumps({
                "player_id": player_id,
                "player_name": pseudo,
                "level_id": level_id,
                "score": score,
            }, ensure_ascii=False).encode("utf-8")

            request = urllib.request.Request(
                ONLINE_SCORE_API_URL,
                data=payload,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "KaelTrace/1.0",
                    "X-Game-Key": ONLINE_SCORE_GAME_KEY,
                },
                method="POST",
            )

            with urllib.request.urlopen(
                request,
                timeout=ONLINE_SCORE_TIMEOUT,
                context=_online_ssl_context(),
            ) as response:
                raw_response = response.read(65537)
                if len(raw_response) > 65536:
                    raise ValueError("Server response is too large")
                result = json.loads(raw_response.decode("utf-8"))

            if not result.get("ok"):
                raise ValueError(result.get("message") or "Request rejected by the server")

            best_score = int(result.get("best_score", result.get("personal_best", score)))
            result_status = result.get("status")
            if result_status in ("created", "new_record") or (result_status is None and result.get("saved")):
                message = "Online score saved: {:,} points.".format(best_score)
                status = "saved"
            elif result_status == "equal_record":
                message = "Score matches the online record ({:,} points).".format(best_score)
                status = "kept"
            else:
                message = "Le record en ligne reste meilleur : {:,} points.".format(best_score)
                status = "kept"

            renpy.invoke_in_main_thread(
                _online_score_show_result, status, message, best_score
            )

        except urllib.error.HTTPError as exc:
            message = "The server rejected the score (HTTP {}).".format(exc.code)
            renpy.invoke_in_main_thread(_online_score_show_result, "error", message, 0)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print("Network error while submitting the score: {!r}".format(exc))
            message = "Score not sent: server connection unavailable."
            renpy.invoke_in_main_thread(_online_score_show_result, "error", message, 0)
        except Exception:
            # Une réponse invalide ou une erreur inattendue ne doit jamais arrêter le jeu.
            message = "Score not sent: invalid server response."
            renpy.invoke_in_main_thread(_online_score_show_result, "error", message, 0)

    def send_score_online(pseudo, level_id, score):
        """Envoie un score sans bloquer le jeu.

        Utilisation dans un label Ren'Py :
            $ send_score_online(pseudo, "ID-DU-NIVEAU", score)
        """
        try:
            clean_pseudo = str(pseudo or "").strip()
            clean_level_id = str(level_id or "").strip()
            clean_score = int(score)

            if len(clean_pseudo) < 2 or len(clean_pseudo) > 32:
                raise ValueError("The username must contain between 2 and 32 characters.")
            if not clean_level_id or len(clean_level_id) > 64:
                raise ValueError("L'identifiant du niveau est invalide.")
            if clean_score < 0 or clean_score > 2147483647:
                raise ValueError("Le score est hors limites.")

            player_id = online_ensure_player_id()
            store.online_score_status = "sending"
            store.online_score_message = "Envoi du score en cours…"
            store.online_score_best = 0
            renpy.restart_interaction()
            renpy.invoke_in_thread(
                _online_score_request,
                player_id,
                clean_pseudo,
                clean_level_id,
                clean_score,
            )
            return True
        except (TypeError, ValueError) as exc:
            _online_score_show_result("error", "Score not sent: " + str(exc), 0)
            return False
