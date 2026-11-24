# Dialogue direction
Opt-in, legacy autofocus unchanged outside begin/end. Pilots J2 corridor Lysa/Elias, evening cafeteria; J4 Nyra trolley, cafeteria. No in-game editor.
```renpy
$ kd_direct.begin("casual")
$ kd_direct.two_shot("noam", "elen")
$ kd_direct.react("elen", "laugh")
$ kd_direct.shot("reaction", "lysa", duration=.3, hold=2)
$ kd_direct.place("noam", x=.3, depth=2, scale=.96)
$ kd_direct.end()
```
Modes manual, assisted, automatic. Six profiles. Shots wide, medium, close, two, field, reverse, reaction, detail, subjective, split, isolate, retreat. Detail explicit coordinates; split uses existing face crops. Reactions are sprite offsets, not articulated faces. Enter/leave translate sprites. Focus brightness only. End before minigames, menus, CG, navigation, legacy camera commands. Group changes automatically end direction. Persistent flag disables opt-in; skip cuts immediately. Runtime lint and playtest still needed. No dialogue or translation changes.
