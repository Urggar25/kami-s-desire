# Route alternative issue du rejet du Commandement au jour 24.
# Le jour 25 sera développé dans un travail distinct : ne pas aiguiller
# vers _25_0_1_1_0_0_REVEIL, qui suppose le vote adopté.

label _25_0_1_1_0_1_REVEIL:
    $ current_day = 25
    $ day_id = 25
    $ current_period = "Matin"
    scene black with dissolve
    call show_chapter_title("Début du chapitre 8", "Chapitre 8 — Le Bouc émissaire")
    centered "La suite de cette route est en cours de développement."
    return

# Durée : écran d'attente temporaire.
