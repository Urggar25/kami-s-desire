default conclave_lock = True

label CONCLAVE_TP:
    scene bg_conclave at adaptive_fullscreen
    
    if conclave_lock:
        jump MAP_NOTHING_HERE
    else:
        jump CONCLAVE_ENTREE

label CONCLAVE_ENTREE:
    "Je rentre dans le Conclave"
    jump MAP_NOTHING_HERE