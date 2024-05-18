set -x EDITOR nvim
set -x VISUAL nvim

source ~/.config/fish/./conf.d/waifus/ganyu.fish

# Only init waifu popups and zoxide if the shell is interactive and not a login one
if status is-interactive; and not status is-login
    alias clear waifu_clear_pop
    waifu_pop
    starship init fish | source
    zoxide init fish | source
end
