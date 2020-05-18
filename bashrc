if [ -f /home/isaque/sqllib/db2profile ]
then
    . /home/isaque/sqllib/db2profile
fi

if [ -f ~/bin/dswd_envs.sh ]
then
  . ~/bin/dswd_envs.sh
fi

if [ -f `which powerline-daemon` ]
then
  powerline-daemon -q
  POWERLINE_BASH_CONTINUATION=1
  POWERLINE_BASH_SELECT=1
  if [ -f ~/.local/lib/python3.7/site-packages/powerline/bindings/shell/powerline.sh ]
  then
    . ~/.local/lib/python3.7/site-packages/powerline/bindings/shell/powerline.sh
  elif [ -f /usr/share/powerline/bindings/shell/powerline.sh ]
  then
    . /usr/share/powerline/bindings/shell/powerline.sh
  elif [ -f /usr/share/powerline/shell/powerline.sh ]
  then
    . /usr/share/powerline/shell/powerline.sh
  fi
fi

