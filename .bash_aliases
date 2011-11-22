#!/bin/bash

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    # Changed the color option from 'auto' to 'always' (in: ls, grep, fgrep, egrep)
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=always'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias agrep='grep -nR --color=always --exclude=cscope.out --exclude=tags'
    alias antgrep="agrep --exclude-dir='./ut' --exclude-dir='./reut' --exclude-dir='./.git'"
    alias  grep='grep --color=always'
    alias fgrep='fgrep --color=always'
    alias egrep='egrep --color=always'
    alias less='less -Rs'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias aptitude='sudo aptitude'
alias apt-get='sudo apt-get'

# My aliases
alias e='gvim -S ~/.vim.sess --remote-silent'
alias gsu='git submodule update --init && git submodule foreach --recursive git submodule update --init'
alias gg='git grep -n --color=always'
alias wd='cd ~/source/qa/tlib/'
alias killnotes='/opt/ibm/lotus/notes/nsdcollector.sh -kill'
alias screenls='sudo ls -laR /var/run/screen'
alias screenproc='ps auxw | grep -i screen | grep -v grep'
# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'


