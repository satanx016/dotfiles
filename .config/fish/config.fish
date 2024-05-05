set -x EDITOR nvim
set -x VISUAL nvim

alias rm 'rm -r'
alias yeet 'yay -Rnsc'
alias crap 'yay -Qdtq'

alias nv nvim
alias nvroot 'sudo -E -s nvim'

alias neo 'command clear && fastfetch'
alias tb taskbook

function otsu_clear_pop
    command clear
    # chafa ~/Pictures/Characters/ZeroTsu/hmm.png --size=12
    chafa ~/Pictures/Characters/Ganyu/ganyuEating --size=14
    echo
    # echo "↳ Sometimes... I wonder... If i'll ever could be a human like you ?"
    echo "↳ I don't understand why people insist on going all out to try and prove how their existence is more valuable than everyone else's."
end

function otsu_pop
    # chafa ~/Pictures/Characters/ZeroTsu/hmm.png --size=12
    chafa ~/Pictures/Characters/Ganyu/ganyuEating --size=14
    echo
    # echo '↳ hmm...'
    echo '↳ I can fix this...'
end

if status is-interactive; and not status is-login
    alias clear otsu_clear_pop
    otsu_pop
    starship init fish | source
    zoxide init fish | source
end
