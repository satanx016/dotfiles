set -x EDITOR nvim
set -x VISUAL nvim
# IME for 日本語 ⛩️
set -x GTK_IM_MODULE fcitx
set -x QT_IM_MODULE fcitx
set -x XMODIFIERS "@im=fcitx"

source ~/.config/fish/./conf.d/waifus/ganyu.fish

# Only init waifu popups and zoxide if the shell is interactive and not a login one
if status is-interactive; and not status is-login
    alias clear waifu_clear_pop
    waifu_pop
    starship init fish | source
    zoxide init fish | source
end
