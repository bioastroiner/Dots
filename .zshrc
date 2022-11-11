# If not running interactively, don't do anything
[[ $- != *i* ]] && return
#HISTFILE=~/.cache/zsh/history
HISTFILE=~/.zsh_history
HISTSIZE=500000
SAVEHIST=500000
setopt appendhistory
setopt INC_APPEND_HISTORY  
setopt SHARE_HISTORY
source ~/.profile
autoload -U colors && colors
autoload -U compinit && compinit -u
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

echo -ne '\e[5 q' # Use beam shape cursor on startup.
precmd() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.
# Source configs
for f in ~/.config/shellconfig/*; do source "$f"; done
# Load zsh-syntax-highlighting
source $HOME/.config/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null
# Suggest aliases for commands
source $HOME/.config/zsh/plugins/zsh-you-should-use/you-should-use.plugin.zsh 2>/dev/null
# Search repos for programs that can't be found
source $HOME/.config/zsh/plugins/zsh-command-not-found/command-not-found.plugin.zsh 2>/dev/null
# zsh plugin that colorifies man pages.
source $HOME/.config/zsh/plugins/zsh-colored-man-pages/colored-man-pages.plugin.zsh 2>/dev/null
source $HOME/.config/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null
# Spaceship Prompt
#autoload -U promptinit; promptinit
eval "$(starship init zsh)"
#https://github.com/cmus/cmus/wiki/detachable-cmus
#alias cmus='screen -q -r -D cmus || screen -S cmus $(which --skip-alias cmus)'
