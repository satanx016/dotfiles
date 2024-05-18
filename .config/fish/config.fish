set -x EDITOR nvim
set -x VISUAL nvim

alias rm 'rm -r'
alias yeet 'yay -Rnsc'
alias crap 'yay -Qdtq'

alias nv nvim

alias neo 'command clear && fastfetch'
alias tb taskbook

source ~/.config/fish/./conf.d/waifus/ganyu.fish

if status is-interactive; and not status is-login
    alias clear waifu_clear_pop
    waifu_pop
    starship init fish | source
    zoxide init fish | source
end
