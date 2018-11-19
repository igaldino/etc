# Install
sudo dnf install openbox compton obconf nitrogen tint2 volumeicon network-manager-applet lightdm-gtk-greeter-settings light-locker redshift-gtk python2-gobject

# Settings
mkdir ~/.config/openbox
mkdir ~/.config/tint2
ln -s ~/etc/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s ~/etc/settings.ini ~/.config/gtk-3.0/.
ln -s ~/etc/_Xdefaults ~/.Xdefaults
ln -s ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -s ~/etc/openbox/rc.xml-`hostname -s` ~/.config/openbox/rc.xml
ln -s ~/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -s ~/etc/openbox/tint2rc-`hostname -s` ~/.config/tint2/tint2rc
sudo ln -s ~/etc/30-touchpad.conf /etc/X11/xorg.conf.d/.
sudo ln -s ~/etc/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf

sudo systemctl disable gdm
sudo systemctl enable lightdm

# Uninstall
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .themes .config/gtk-3.0/settings.ini .config/{openbox,tint2} .cache/{openbox,tint2}
