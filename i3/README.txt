# https://fedoramagazine.org/getting-started-i3-window-manager/

# Install
sudo dnf install i3 i3status dmenu i3lock xbacklight nitrogen conky compton network-manager-applet redshift-gtk fontawesome-fonts

# Settings
ln -s ~/etc/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s ~/etc/settings.ini ~/.config/gtk-3.0/.
ln -s ~/etc/_Xdefaults ~/.Xdefaults
ln -s ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -s ~/etc/i3/config ~/.config/i3/.
ln -s ~/etc/i3/i3status.conf ~/.config/i3status/config
sudo ln -s ~/etc/i3/00-touchpad.conf /etc/X11/xorg.conf.d/.
