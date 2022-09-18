#https://github.com/qtile/qtile/blob/master/libqtile/utils.py
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os 
import subprocess

@lazy.function
def next_window(qtile):
    """Hack to be able to cycle windows even when window is minimized"""
    group = qtile.current_group
    index = group.windows.index(group.current_window)
    if index == len(group.windows) - 1:
        index = -1
    group.focus(group.windows[index + 1])

@lazy.function
def prev_window(qtile):
    group = qtile.current_group
    index = group.windows.index(group.current_window)
    group.focus(group.windows[index - 1])

@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()


home = os.path.expanduser('~')
mod = "mod4" #set super key (windows key)
#terminal = guess_terminal() # i use alacritty so no need to edit this
terminal = "st"
browser = "firefox"
myFont = "Minecraft"
city="Tehran"
keys = [
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    #    Key([mod, "shift"], "-", lazy.layout.decrease_ratio(), desc="-- Ratio of Master/Slave"),
    #    Key([mod, "shift"], "=", lazy.layout.increase_ratio(), desc="++ Ratio of Master/Slave"),
#    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle True Fullscreen with wideScreen"),
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch terminal"),
    #Key([mod], "Tab", lazy.screen.next_group(), desc="Move to the group on the right"),
    #Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Move to the group on the right"),
    #Key([mod], "l", lazy.screen.next_group(), desc="Move to the group on the right"),
    #Key([mod], "h", lazy.screen.prev_group(), desc="Move to the group on the left"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"), 
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "q", lazy.restart(), desc="Restart Qtile"),
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Spawn Dmenu"),
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'), 
    Key([mod], "c", lazy.spawn("rofi -show calc &")),
    Key([mod], "e", lazy.spawn("rofi -modi emoji -show emoji -emoji-format '{emoji}' &")),
    Key([mod], "y", lazy.spawn("pcmanfm &")),
    Key([mod], "r", lazy.spawn("{} -e ranger".format(terminal))),
    Key([mod], "p", lazy.spawn("mpv --idle --force-window {}".format(subprocess.run(['xclip', '-o', '-sel', 'cli'],capture_output=True,encoding="utf-8").stdout))), # play video from clipboard needs https://github.com/yassin-l/copy-paste-url
    Key([mod], "n", lazy.function(next_window)),
    Key([mod, "shift"], "f", lazy.function(float_to_front)),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
    
]
#groups = [Group("🌐", layout='tile'),
#          Group("🖥️", layout='tile'),
#          Group("✉️", layout='tile'),
#          Group("📽️", layout='tile'),
#          Group("🎲", layout='tile'),
#          Group("6️⃣", layout='tile'),
#          Group("7️⃣", layout='tile'),
#          Group("8️⃣", layout='tile'),
#          Group("🗒️", layout='tile'),
#          Group("📌", layout='floating')]

groups = [Group(i) for i in "123456789"]
labels = [
    '0', # we start from 1
    '🌐',
    '🖥️',
    '✉️',
    '📽️',
    '🎲',
    '6️⃣',
    '7️⃣',
    '8️⃣',
    '📌',
]
for i in groups:
    #i.persist=False
    i.label=labels[int(i.name)]
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 10,
                "border_focus": "#055ae3",
                "border_normal": "#1D2330"
                }
layouts = [
    #layout.MonadWide(),
    #layout.MonadTall(**layout_theme),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Tile(**layout_theme,border_on_single=False,ratio=0.5),
    #layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    layout.Bsp(),
    #layout.Matrix(),
    #layout.RatioTile(**layout_theme),
    #layout.TreeTab(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font=myFont,
    fontsize=16,
    padding=3,
    foregound='#ffffff'
)
extension_defaults = widget_defaults.copy()

def get_memory():
    return ' 🧠 ' + subprocess.check_output([home+'/.local/bin/memory']).decode('utf-8').strip()

def get_uptime():
    return ' 😴 ' + subprocess.check_output([home+'/.local/bin/upt']).decode('utf-8').strip()
def get_kb_layout():
    output = subprocess.run(
        ['xkblayout-state', 'print', '%s'],
        capture_output=True,
        encoding="utf-8"
    ).stdout
    return output

#def get_storage():
#    return subprocess.check_output(['sh ~/.local/bin/sb-disk']).decode('utf-8').strip()

# [Bright,Dim]
bar_color = ['#00003f00','#00005f00']
W    = '#ffffff'
B    = '#000000'
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(background=bar_color[1],
                    active=B,
                    inactive=W,
                    # Active group highlight color when using 'line' highlight method.
                    highlight_color=[B, W]),
                widget.WindowName(font=myFont),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(background=bar_color[1]),
                widget.CheckUpdates(display_format="📦:{updates}",background=bar_color[1],distro="Arch",update_interval=300,no_update_string='✅'),
                widget.Clock(format="|📅: %A, %B %d ⏰: %I:%M %p",
                    background=bar_color[0],
                    mouse_callbacks={},
                    update_interval=60),
                widget.Net(update_interval=2,background=bar_color[1],format='|🚀: {down} ↓ {up} ↑',padding=5),
                widget.GenPollText(update_interval=1800,func=lambda: subprocess.check_output(['curl','wttr.in/'+city+'?format=1']).decode('utf-8').strip()),
                #widget.KeyboardLayout(configured_keyboards=['us', 'ir'],option='compose:menu,grp_led:scroll',display_map={'us': '🇺🇸', 'ir': '🇹🇯'},background=bar_color[1]),
                widget.GenPollText(
                    func=get_kb_layout,
                    update_interval=0.5),
                # Custom Shell Scripts
                widget.GenPollText(update_interval=60, func=get_uptime,background=bar_color[0]),
                widget.GenPollText(update_interval=5, func=get_memory,background=bar_color[1]),
                widget.DF(visible_on_warn=False,format='  💾{uf}{m}  🫙{r:.0f}% ',warn_space=40,background=bar_color[0],update_interval=600),
                widget.QuickExit(default_text=' 🔑 ', countdown_format='[{}]',background=bar_color[0],foreground='#000000')
            ],24,opacity=0.6,
            # [N E S W]
            margin=[5,10,1,10],
            background='#00000000',
            font=myFont
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button1", lazy.window.toggle_floating(), desc='Toggle floating'),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run `xprop` 
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="deadbeef"),
        Match(title='Confirmation'),      # tastyworks exit box
        Match(title='Qalculate!'),        # qalculate-gtk
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class='pinentry-gtk-2'), # GPG key password entry

    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
wmname = "LG3D"
