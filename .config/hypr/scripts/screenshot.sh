#!/usr/bin/env bash

if [[ "$1" == "--copy-screen" ]]; then
    grim - | wl-copy
elif [[ "$1" == "--copy-region" ]]; then
    grim -g "$(slurp -d)" - | wl-copy
elif [[ "$1" == "--keep-shader" ]]; then
    grim ~/Pictures/Screenshots/$(date +%Y%m%d_%Hh%Mm%Ss).png
else
    CUR_SHADER=$(hyprctl getoption decoration:screen_shader | grep "str:" | awk '{print $2}')
    hyprctl keyword decoration:screen_shader "" # Off with the shaders
    grim ~/Pictures/Screenshots/$(date +%Y%m%d_%Hh%Mm%Ss).png
    hyprctl keyword decoration:screen_shader $CUR_SHADER # Put them back
fi
