# Ren'Py : deux distributions séparées, base et extension.
# La classification est prioritaire sur la classification par défaut.
init python:
    build.classify("game/dlc/doppelganger_routes/**", "kd_doppelganger_routes")
    build.package("doppelganger-routes", "zip", "kd_doppelganger_routes",
        description="Kami's Desires — Les autres vies (DLC)", dlc=True, update=False)
