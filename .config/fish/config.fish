set PATH $PATH /home/satanx016/.local/bin

set -x EDITOR nvim
set -x VISUAL nvim

cat ~/.cache/wal/sequences &

# Only init waifu popups and zoxide if the shell is interactive and not a login one
if status is-interactive; and not status is-login
    source ~/.config/fish/./conf.d/waifus/ganyu.fish
    alias clear waifu_clear_pop
    waifu_pop
    starship init fish | source
    zoxide init fish | source
end
