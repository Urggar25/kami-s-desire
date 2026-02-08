default dortoir_lock = True

label DORTOIR_TP:
    scene bg_dortoir at adaptive_fullscreen
    
    if dortoir_lock:
        jump MAP_NOTHING_HERE
    else:
        jump DORTOIR_ENTREE

label DORTOIR_ENTREE:
    "Je rentre dans les dortoirs"
    jump MAP_NOTHING_HERE