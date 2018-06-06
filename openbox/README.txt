# Install
sudo dnf install openbox obconf nitrogen conky tint2 volumeicon xfce4-power-manager xfce4-notifyd xorg-x11-drv-libinput xorg-x11-server-utils network-manager-applet compton lightdm-gtk-greeter-settings light-locker

# Settings
ln -s $HOME/etc/openbox/_conkyrc ~/.conkyrc
ln -s $HOME/etc/openbox/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s $HOME/etc/openbox/autostart ~/.config/openbox/.
cat .gtkrc-2.0 
cat .config/gtk-3.0/settings.ini 

# Themes
# Adwaita     : https://www.opendesktop.org/content/show.php/Adwaita-openbox?content=155042
# Adwaita Dark: https://www.box-look.org/p/1017591/

# Uninstall
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .conkyrc .themes .config/gtk-3.0/settings.ini .config/{openbox,tint2} .cache/{openbox,tint2}
