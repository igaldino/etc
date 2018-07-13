# https://fedoramagazine.org/getting-started-i3-window-manager/

# Install
sudo dnf install i3 i3status dmenu i3lock xbacklight nitrogen conky compton network-manager-applet redshift-gtk

# Settings
ln -s $HOME/etc/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s $HOME/etc/settings.ini ~/.config/gtk-3.0/.
ln -s $HOME/etc/_Xdefaults ~/.Xdefaults
ln -s $HOME/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -s $HOME/etc/i3/config ~/.config/i3/.
sudo ln -s $HOME/etc/i3/00-touchpad.conf /etc/X11/xorg.conf.d/.
