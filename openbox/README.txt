# Install
sudo dnf install openbox obconf nitrogen conky tint2 volumeicon xfce4-power-manager xfce4-notifyd xorg-x11-drv-libinput xorg-x11-server-utils network-manager-applet compton lightdm-gtk-greeter-settings light-locker

# Settings
ln -s $HOME/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -s $HOME/etc/openbox/_conkyrc ~/.conkyrc
ln -s $HOME/etc/openbox/_gtkrc-2.0 ~/.gtkrc-2.0
ln -s $HOME/etc/openbox/settings.ini ~/.config/gtk-3.0/.
ln -s $HOME/etc/openbox/tint2rc ~/.config/tint2/.

# Find touchpad to enable tap
# $ xinput list
#   ...
# ⎜   ↳ SynPS/2 Synaptics TouchPad              	id=14	[slave  pointer  (2)]
#   ...
#
# $ xinput list-props 14
#   ...
# 	libinput Tapping Enabled (302):	0
#   ...

# Themes
# Adwaita     : https://www.opendesktop.org/content/show.php/Adwaita-openbox?content=155042
# Adwaita Dark: https://www.box-look.org/p/1017591/

# Uninstall
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .conkyrc .themes .config/gtk-3.0/settings.ini .config/{openbox,tint2} .cache/{openbox,tint2}
