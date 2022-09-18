#!/usr/bin/env bash 

#festival --tts $HOME/.config/qtile/welcome_msg &
#lxsession &
picom --experimental-backends &
volumeicon &
#amixer sset "Auto-Mute" unmute

#amixer -c 0 sset "Auto-Mute Mode" Disabled
#alsactl daemon

# NetworkManager
nm-applet &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
#xargs xwallpaper --stretch < ~/.xwallpaper &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
nitrogen --restore &

xrandr --output HDMI-0 --mode 1920x1080 &
# Keyboard layout daemon
#kbdd
setxkbmap -layout us,ir -model pc104 -option grp:alt_shift_toggle
#setxkbmap -layout lv,ru -variant ",phonetic_winkeys" -option "grp:lalt_lshift_toggle" &

#aria2 gui daemon run at systray
#uget-gtk &

flameshot &
