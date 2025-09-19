#!/usr/bin/env bash

CUR_SHADER=$(hyprctl getoption decoration:screen_shader | grep "str:" | awk '{print $2}')

if [[ -z $CUR_SHADER ]]; then
    hyprctl keyword decoration:screen_shader "" # Off with the shaders
    CMD=$(hyprpicker -a)
    hyprctl keyword decoration:screen_shader $CUR_SHADER # Put them back
else
    CMD=$(hyprpicker -a)
fi
