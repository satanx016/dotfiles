if status is-login ; and test (tty) = /dev/tty1
    if test -z "$DISPLAY" ;and test "$XDG_VTNR" -eq 1
        exec Hyprland > /dev/null
    end
end
