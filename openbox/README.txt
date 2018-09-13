# Install
sudo dnf install openbox compton obconf nitrogen tint2 volumeicon network-manager-applet lightdm-gtk-greeter-settings light-locker redshift-gtk
# ? conky xfce4-power-manager xfce4-notifyd xorg-x11-drv-libinput xorg-x11-server-utils


# Settings
ln -s ~/etc/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s ~/etc/settings.ini ~/.config/gtk-3.0/.
ln -s ~/etc/_Xdefaults ~/.Xdefaults
ln -s ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -s ~/etc/openbox/rc.xml ~/.config/openbox/.
ln -s ~/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -s ~/etc/openbox/tint2rc ~/.config/tint2/.
sudo ln -s ~/etc/30-touchpad.conf /etc/X11/xorg.conf.d/.
# ln -s ~/etc/openbox/_conkyrc ~/.conkyrc

sudo systemctl disable gdm
sudo systemctl enable lightdm

# Themes
# Adwaita     : https://www.opendesktop.org/content/show.php/Adwaita-openbox?content=155042
# Adwaita Dark: https://www.box-look.org/p/1017591/

# Uninstall
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .themes .config/gtk-3.0/settings.ini .config/{openbox,tint2} .cache/{openbox,tint2}
# ? .conkyrc 
