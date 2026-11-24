# Dedicated TV channels: sound mixer for stings, music mixer for the quiet bed.
# Original synthesized PCM assets are shipped with the game; no runtime generation.
init -5 python:
    renpy.music.register_channel("kd_news_fx", mixer="sfx", loop=False)
    renpy.music.register_channel("kd_news_bed", mixer="music", loop=True)

    def kd_news_sfx(name):
        if not renpy.is_skipping():
            renpy.music.play("audio/kd_news/" + name + ".wav", channel="kd_news_fx", loop=False)

    def kd_news_bed_start(mode="studio"):
        renpy.music.play("audio/kd_news/" + ("field" if mode == "field" else "studio") + ".wav", channel="kd_news_bed", loop=True, fadein=0.35)

    def kd_news_audio_stop():
        renpy.music.stop(channel="kd_news_bed", fadeout=0.20)
        renpy.music.stop(channel="kd_news_fx")

# Keep the scenario music's own channel and position intact.
# Pause it only if it was playing; resume only if we paused it ourselves.
default kd_news_music_was_paused = False
default kd_news_music_owned_pause = False

label kd_news_audio_begin(mode="studio"):
    $ kd_news_music_owned_pause = False
    if renpy.music.is_playing(channel="music"):
        $ kd_news_music_was_paused = renpy.music.get_pause(channel="music")
        if not kd_news_music_was_paused:
            $ renpy.music.set_pause(True, channel="music")
            $ kd_news_music_owned_pause = True
    $ kd_news_sfx("open")
    return

label kd_news_audio_end:
    $ kd_news_audio_stop()
    if kd_news_music_owned_pause:
        $ renpy.music.set_pause(False, channel="music")
    $ kd_news_music_owned_pause = False
    return
