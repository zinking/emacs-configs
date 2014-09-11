alias ll='ls -al'
alias rs='source ~/.bash_profile'
alias cdwork='cd ~/workspace/marin/branches'


export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWUNTRACKEDFILES=true
export GIT_PS1_SHOWSTASHSTATE=true
export GIT_PS1_SHOWUPSTREAM="auto"
export LC_CTYPE=C 
export LANG=C

sd_retval_cond () {
   local ret_val=$?
   if [[ "$ret_val" = "0" ]]; then echo -e "$1"; else echo -e "$2"; fi
   return $ret_val
}

RESET='\[\e[0m\]'     BOLD='\[\e[1m\]'
YELLOW='\[\e[33m\]'   BLUE='\[\e[34m\]'
BLACK='\[\e[30m\]'    RED='\[\e[31m\]'
PINK='\[\e[35m\]'     CYAN='\[\e[36m\]'
GREEN='\[\e[32m\]'    GRAY='\[\e[37m\]'
export PS1="\n$BOLD$BLUE(\u) \$(sd_retval_cond '$GREEN' '$RED')[\$(sd_retval_cond woo \"aww \$?\")] $CYAN(\$(date +%H:%M:%S)) $PINK\w\$(echo '' ' $CYAN[%s]')\n$RESET$BLUE\$$RESET "

export CLICOLOR=1 # lets ls and stuff show colors
#export PS1="\u@\h \w [\$(date +%k:%M:%S)]>\n"

alias emacs='/Applications/Emacs.app/Contents/MacOS/Emacs -nw'


ulimit -n 2000

set -o vi

export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

add_to_path ()
{
    if [[ "$PATH" =~ (^|:)"${1}"(:|$) ]]
    then
        return 0
    fi
    export PATH=${1}:$PATH
}


alias showpath='echo $PATH | tr ":" "\n"'

alias findg='find . | grep -i'

sf()
{
    grep -i -r  "${1}" . | cut -d":" -f1 | sort -u
}



alias setup_proxy='ssh -N -D 9191 zhenw@10.readmine.co'

. ~/emacs-configs/.marin_bash_profile
