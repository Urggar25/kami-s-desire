# Opt-in: legacy autofocus remains active everywhere outside begin/end.
default persistent.kd_dialogue_direction = True
default kd_direction_active = False
default kd_direction_mode = "assisted"
default kd_direction_profile = "casual"
default kd_direction_actors = ()
default kd_direction_signature = None
default kd_direction_history = ()
default kd_direction_age = 0
default kd_direction_plan = "wide"
default kd_direction_targets = ()
default kd_direction_locked = False
default kd_direction_poses = {}
default kd_direction_original = {}
default kd_direction_camera_original = None
default kd_direction_hold = 0
default kd_direction_speaker = None

init python:
    class KDDialogueDirector(object):
        def begin(self, profile="casual", actors=None, auto=True, mode=None):
            if store.kd_direction_active:
                self.end()
            if profile not in KD_DIRECT_PROFILES:
                raise ValueError("Unknown direction profile")
            if not persistent.kd_dialogue_direction or scene_has_no_character_sprites():
                return
            store.kd_direction_mode = mode or ("assisted" if auto else "manual")
            if store.kd_direction_mode not in ("manual","assisted","automatic"):
                raise ValueError("Unknown direction mode")
            store.kd_direction_actors = tuple(actors or store.group_members)
            store.kd_direction_original = {a:dict(store.char_state[a]) for a in kd_direct_visible()}
            store.kd_direction_camera_original = (cam_current("bgcam"),cam_current("master"))
            store.kd_direction_signature = cinema_scene_signature()
            store.kd_direction_profile = profile
            store.kd_direction_active = True
            store.kd_direction_speaker = None
            store.kd_direction_history = ()
            store.kd_direction_age = 0
            store.kd_direction_locked = False
            store.kd_direction_hold = 0
            store.kd_direction_poses = {}
            self.recompose()
            self.shot("wide",duration=0,hold=0)

        def recompose(self):
            # Read the existing blocking; do not rearrange a scene on begin.
            for actor in kd_direct_visible():
                st = store.char_state[actor]
                if actor not in store.kd_direction_poses:
                    store.kd_direction_poses = dict(store.kd_direction_poses, **{actor:(st.get("group_scale",1.0),1,0)})

        def profile(self,name):
            if name not in KD_DIRECT_PROFILES:
                raise ValueError("Unknown direction profile")
            store.kd_direction_profile = name

        def lock(self):
            store.kd_direction_locked = True

        def unlock(self):
            store.kd_direction_locked = False

        def camera(self,x=.5,y=.5,zoom=1.0,duration=.4,easing="ease"):
            if store.kd_direction_active:
                kd_direct_cam_apply(x,y,zoom,duration,easing)

        def shot(self,kind,target=None,duration=None,hold=2):
            if not store.kd_direction_active:
                return
            visible = kd_direct_visible()
            targets = (target,) if isinstance(target,str) else tuple(target or ())
            targets = tuple(a for a in targets if a in visible)
            gap,solo,time = KD_DIRECT_PROFILES[store.kd_direction_profile]
            t = time if duration is None else duration
            if kind not in ("wide","medium","close","two","field","reverse","reaction","detail","subjective","split","isolate","retreat"):
                raise ValueError("Unknown direction shot")
            if kind not in ("wide","retreat","detail","subjective") and not targets:
                kind = "wide"
            renpy.hide_screen("kd_direction_split")
            if kind == "split" and len(targets)>=2:
                if not renpy.is_skipping():
                    renpy.show_screen("kd_direction_split",targets=targets[:3])
                x,y,z = .5,.5,1.0
            elif kind in ("wide","retreat"):
                x,y,z = .5,.5,1.0
            elif kind=="detail":
                x,y,z = .5,.84,1.45
            elif kind=="subjective":
                x,y,z = .5,.46,1.12
            else:
                positions = [float(store.char_state[a].get("x",.5)) for a in targets]
                mid = sum(positions)/len(positions)
                if kind=="two":
                    z = min(1.48,1.0/max(.68,max(positions)-min(positions)+.24))
                elif kind in ("close","reaction","isolate"):
                    z = min(1.78,solo+.18)
                elif kind=="field":
                    z = solo
                elif kind=="reverse":
                    z = max(1.32,solo-.14)
                else:
                    z = max(1.30,solo-.08)
                x,y = kd_direct_center_for(mid,z),(.34 if kind in ("close","reaction","isolate") else .40)
            kd_direct_cam_apply(x,y,z,t,"easeout" if kind=="reaction" else "ease")
            store.kd_direction_plan,store.kd_direction_targets = kind,targets
            store.kd_direction_age = 0
            store.kd_direction_hold = max(0,int(hold))
            # Camera changes do not reset sprite focus or ongoing reactions.

        def fixed_close(self, tag, duration=.35):
            self.shot("close", tag, duration=duration, hold=0)
            self.lock()

        def simultaneous(self, targets):
            self.shot("split", tuple(targets), duration=.18, hold=0)
            self.lock()

        def two_shot(self,a,b,duration=None):
            self.shot("two",(a,b),duration)

        def split(self,a,b):
            self.shot("split",(a,b))

        def detail(self,x=.5,y=.85,zoom=1.5,duration=.4):
            self.shot("detail",duration=0)
            self.camera(x,y,zoom,duration)

        def react(self,tag,reaction):
            if store.kd_direction_active:
                kd_direct_draw(tag,reaction=reaction)

        def interrupt(self,tag,intensity=.5):
            self.shot("reaction",tag,duration=max(.12,.34-.2*kd_direct_clamp(intensity)),hold=1)
            self.react(tag,"interest")

        def place(self,tag,x=None,depth=0,scale=1.0,facing=1):
            if not store.kd_direction_active or tag not in kd_direct_visible():
                return
            old_x = store.char_state[tag].get("x",.5)
            if x is not None:
                store.char_state[tag]["x"] = kd_direct_clamp(x)
                store.char_pos[tag] = store.char_state[tag]["x"]
            store.kd_direction_poses = dict(store.kd_direction_poses,**{tag:(kd_direct_clamp(scale,.85,1.12),-1 if facing<0 else 1,int(depth))})
            kd_direct_draw(tag,old_x=old_x)

        def enter(self,tag,expr="neutre",x=.5,fast=False):
            showP(tag,expr,x)
            store.group_members = list(dict.fromkeys(list(store.group_members)+[tag]))
            if not store.kd_direction_active:
                return
            store.kd_direction_actors = tuple(dict.fromkeys(store.kd_direction_actors+(tag,)))
            store.kd_direction_original = dict(store.kd_direction_original,**{tag:dict(store.char_state[tag])})
            self.shot("wide",hold=0)
            kd_direct_draw(tag,entry=(-1 if x<.5 else 1)*(160 if fast else 90))

        def leave(self,tag,fast=False):
            if not store.kd_direction_active or tag not in kd_direct_visible():
                hideP(tag)
                return
            st = store.char_state[tag]
            x,y = st.get("x",.5),st.get("y",1.0)
            scale,facing,depth = store.kd_direction_poses.get(tag,(1.0,1,0))
            t = 0 if renpy.is_skipping() else (.16 if fast else .30)
            renpy.show(tag+" "+kd_direct_expression(tag),tag=tag,layer="master",at_list=[kd_direct_depart(x,y,scale,facing,-160 if x<.5 else 160,t)])
            if t:
                renpy.pause(t)
            renpy.hide(tag,layer="master")
            store.group_members = [a for a in store.group_members if a!=tag]
            store.char_state.pop(tag,None)
            store.char_pos.pop(tag,None)
            store.kd_direction_actors = tuple(a for a in store.kd_direction_actors if a!=tag)
            self.shot("retreat",hold=0)

        def focus(self,tag):
            if store.kd_direction_active:
                store.kd_direction_speaker = tag if tag in kd_direct_visible() else None
                kd_direct_refresh_focus()

        def end(self,restore=True):
            if not store.kd_direction_active:
                return
            same_scene = cinema_scene_signature()==store.kd_direction_signature
            renpy.hide_screen("kd_direction_split")
            if same_scene:
                for a in kd_direct_visible():
                    original = store.kd_direction_original.get(a,{})
                    st = store.char_state[a]
                    st["expr"],st["mode"] = kd_direct_expression(a),None
                    if restore:
                        st["x"] = original.get("x",st.get("x",.5))
                        st["y"] = original.get("y",st.get("y",1.0))
                        store.char_pos[a] = st["x"]
                    renpy.show(a+" "+st["expr"],tag=a,layer="master",at_list=[char_group_place(st.get("x",.5),st.get("y",1.0),st.get("group_scale",1.0))],zorder=st.get("zorder",0))
            store.kd_direction_active = False
            store.kd_direction_speaker = None
            store.kd_direction_actors = ()
            store.kd_direction_poses = {}
            store.kd_direction_original = {}
            store.kd_direction_locked = False
            store.kd_direction_hold = 0
            saved = store.kd_direction_camera_original
            store.kd_direction_camera_original = None
            if same_scene and restore and saved:
                for layer,pose in zip(("bgcam","master"),saved):
                    cam_apply(*pose,t=0.0,layers=(layer,))
            else:
                cam_reset(t=0.0)
            store._focus_last_params = dict(tag="__REGROUP__")

        def on_line(self,tag):
            if not store.kd_direction_active:
                return False
            if (not persistent.kd_dialogue_direction or scene_has_no_character_sprites()
                    or cinema_scene_signature()!=store.kd_direction_signature
                    or renpy.get_screen("kd_news_broadcast") is not None
                    or renpy.get_screen("kami_broadcast_ui") is not None):
                self.end(restore=False)
                return False
            visible = kd_direct_visible()
            if not visible:
                self.end(restore=False)
                return False
            if tag=="__NARRATOR__":
                return True
            if tag not in visible:
                if store.kd_direction_speaker is not None:
                    store.kd_direction_speaker = None
                    kd_direct_refresh_focus()
                if not store.kd_direction_locked and store.kd_direction_mode!="manual" and store.kd_direction_plan!="wide":
                    self.shot("wide",duration=.20,hold=0)
                return True
            # Focus is independent of camera holds, locks and cut cadence.
            if store.kd_direction_speaker != tag:
                store.kd_direction_speaker = tag
                kd_direct_refresh_focus()
            store.kd_direction_age += 1
            hist = (store.kd_direction_history+(tag,))[-6:]
            store.kd_direction_history = hist
            if store.kd_direction_hold:
                store.kd_direction_hold -= 1
                if store.kd_direction_locked or tag in store.kd_direction_targets or store.kd_direction_plan in ("wide","retreat","detail","subjective"):
                    return True
                store.kd_direction_hold = 0
            if store.kd_direction_locked or store.kd_direction_mode=="manual":
                return True
            gap = KD_DIRECT_PROFILES[store.kd_direction_profile][0]
            if store.kd_direction_mode=="automatic":
                gap = max(1,gap-1)
            previous = hist[-2] if len(hist)>1 else None
            plan = store.kd_direction_plan
            targets = store.kd_direction_targets
            profile = store.kd_direction_profile
            age = store.kd_direction_age
            recent = tuple(dict.fromkeys(hist[-4:]))
            # Never let a dense cast remain a static wall of sprites.
            if len(visible)>=6:
                if previous != tag:
                    kind = "field" if plan in ("reverse","wide","retreat") else "reverse"
                    if age>=3 and len(recent)>=3 and plan not in ("wide","retreat"):
                        kind = "medium"
                    self.shot(kind,tag,hold=0)
                elif age>=3 and plan not in ("close","reaction"):
                    self.shot("close",tag,hold=0)
                return True
            # A sustained line can earn a push-in even without a speaker change.
            if previous == tag:
                if age>=gap+1 and plan in ("wide","two","medium","field","reverse"):
                    self.shot("close" if profile in ("comedy","confrontation") else "medium",tag,hold=0)
                return True
            if previous is None:
                self.shot("medium",tag,hold=0)
                return True
            # Two-shot is a temporary composition, not a permanent lock.
            alternating = len(hist)>=4 and hist[-1]==hist[-3] and hist[-2]==hist[-4]
            if alternating and previous in visible and plan!="two" and age>=gap:
                if abs(store.char_state[tag]["x"]-store.char_state[previous]["x"])<=.58:
                    self.shot("two",(previous,tag),hold=0)
                    return True
            if plan=="two" and tag in targets and age<gap+1:
                return True
            if plan=="two" and age>=gap+1:
                self.shot("reverse",tag,hold=0)
                return True
            if tag not in targets or age>=gap:
                kind = "reverse" if plan=="field" else "field"
                if profile in ("comedy","confrontation") and len(recent)<=2 and plan not in ("close","reaction"):
                    kind = "close"
                elif len(recent)>=3 and age>=gap+2 and plan!="wide":
                    kind = "wide"
                self.shot(kind, None if kind=="wide" else tag,hold=0)
            return True

define kd_direct = KDDialogueDirector()

# Face cutaway: below say and HUD; not two independent scene cameras.
screen kd_direction_split(targets):
    zorder -1
    modal False
    add Solid("#0b1725")
    $ panel_width = config.screen_width // len(targets)
    $ panel_height = int(config.screen_height * .70)
    for i, tag in enumerate(targets):
        fixed:
            xpos (i * panel_width)
            ypos 70
            xysize (panel_width, panel_height)
            clipping True
            add Solid(kd_char_color(tag), xysize=(panel_width, 6))
            add kd_face(tag, size=min(650, panel_width - 40)) xalign 0.5 ypos 35
            if i > 0:
                add Solid("#d6e5ed", xysize=(3, panel_height))
