alias ll='ls -al'
alias rs='source ~/.bash_profile'
alias cdwork='cd ~/workspace/marin/branches'


export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWUNTRACKEDFILES=true
export GIT_PS1_SHOWSTASHSTATE=true
export GIT_PS1_SHOWUPSTREAM="auto"

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

alias findg='find . | grep '

sf()
{
    grep -i -r . | grep $1 | cut -d":" -f1 | sort -u
}



#export EDITOR='emacs -nw'

#add_to_path ~/App/apache-ant-1.9.4/bin

add_to_path /usr/local/bin
add_to_path ~/scripts/

export ANT_HOME="/usr/local/ant"
add_to_path ${ANT_HOME}/bin

export M2_HOME="/usr/local/maven"
add_to_path ${M2_HOME}/bin

export MAVEN_OPTS=-Xmx1024m

export JAVA_OPTS="-Djava.awt.headless=true -Dfile.encoding=UTF-8 -server -Xms2048m -Xmx2048m -XX:NewSize=512m -XX:MaxNewSize=512m -XX:PermSize=512m -XX:MaxPermSize=512m -XX:+CMSClassUnloadingEnabled"

export JAVA_HOME="/Library/Java/Home"
export CATALINA_HOME="/usr/local/tomcat"
export BASEDIR=${CATALINA_HOME}
export CATALINA_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=1046 -Dgrails.env=development"

add_to_path ${CATALINA_HOME}/bin

alias rstomcat='shutdown.sh && startup.sh'
alias cdtom='cd ${CATALINA_HOME}'

alias setup_proxy='ssh -N -D 9191 zhenw@10.readmine.co'

export MARIN_ECLIPSE_WORKSPACE=~/workspace/marin/branches

export MAMP_HOME=/Applications/MAMP
add_to_path ${MAMP_HOME}/bin
add_to_path ${MAMP_HOME}/Library/bin
add_to_path ${MAMP_HOME}/bin/php5.2/bin


export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8

alias cdtrunk='cd ~/workspace/marin/branches/iteration-0053'
alias cdmscm='~/workspace/marin/branches/iteration-0053/mscm/sql/setup'

alias addauth="cat ~/.ssh/id_rsa.pub | ssh dev@'cat >> ~/.ssh/authorized_keys'"
alias cdqabin='cd ~/workspace/marin/qa/int/tests/publishers/bin'
alias cddb='cd ~/workspace/marin/branches/sh-i53-bugs/mscm/sql/setup/tmp/'
