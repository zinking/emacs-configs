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
export PS1="\n$BOLD$BLUE(\u) \$(sd_retval_cond '$GREEN' '$RED')[\$(sd_retval_cond woo \"aww \$?\")] $CYAN(\$(date +%H:%M:%S)) $PINK\w\$(echo '' ' $CYAN')\n$RESET$BLUE\$$RESET "

export CLICOLOR=1 # lets ls and stuff show colors
#export PS1="\u@\h \w [\$(date +%k:%M:%S)]>\n"

alias emacs='/Applications/Emacs.app/Contents/MacOS/Emacs -nw'

alias cleardns='sudo dscacheutil -flushcache'
alias cleardns2='sudo killall -HUP mDNSResponder'


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

grant_access()
{
    cat ~/.ssh/id_rsa.pub | ssh dev@$1 'cat >> ~/.ssh/authorized_keys'
}

. ~/emacs-configs/.marin_bash_profile

#[[ -s "~/.rvm/scripts/rvm" ]] && source "~/.rvm/scripts/rvm"
# Load RVM into a shell session *as a function*

alias clean_dns="sudo killall mDNSResponder & sudo dscacheutil -flushcache"

alias clean_hangout="sudo killall coreaudiod"

#export PATH="/Users/awang/.jenv/shims:${PATH}"
add_to_path ~/.jenv/bin
add_to_path ~/.jenv/shims

source "/usr/local/Cellar/jenv/0.4.1/libexec/libexec/../completions/jenv.zsh"

jenv rehash 2>/dev/null

export JENV_LOADED=1

unset JAVA_HOME

jenv() {
  typeset command
  command="$1"
  if [ "$#" -gt 0 ]; then
    shift
  fi

  case "$command" in
  enable-plugin|rehash|shell|shell-options)
    eval `jenv "sh-$command" "$@"`;;
  *)
    command jenv "$command" "$@";;
  esac
}



add_to_path ~/.rbenv/bin

#eval "$(rbenv init -)" $ exec /bin/zsh -l

export MAGICK_HOME="/usr/local/Cellar/imagemagick/6.9.1-3"
add_to_path "$MAGICK_HOME"

export DYLD_LIBRARY_PATH="$MAGICK_HOME/lib/"
alias lycurl='curl --header "X-Spree-Token:dca07e266fdd1c57e42d5cc97f8c866e723a1d817fe7d850"'

alias clearkafkaqueue='rm -rf /tmp/kafka-logs/*'

alias cdly='cd ~/os/zhenw/ly/liangyi'

#setup a user

setup_newenv(){
    useradd -m awang
    passwd awang
    sudo adduser awang sudo
    chsh -s /bin/bash awang

    su awang
    cd ~

    git clone https://github.com/zinking/emacs-configs.git
    ln -sfn emacs-configs/.bash_profile .bash_profile #home dir 
}
