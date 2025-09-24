if status is-interactive
    zoxide init fish --cmd cd --hook prompt | source
    if not status is-login
        starship init fish | source
    end
end
