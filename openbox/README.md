# Install
```
sudo dnf install openbox compton obconf nitrogen tint2 volumeicon network-manager-applet lightdm-gtk-greeter-settings light-locker redshift-gtk python2-gobject xdotool dunst rofi
```

# Settings
```
mkdir -p ~/.config/openbox
mkdir -p ~/.config/tint2
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/_Xdefaults ~/.Xdefaults
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/openbox/rc.xml-`hostname -s` ~/.config/openbox/rc.xml
ln -sf ~/etc/openbox/menu.xml-`hostname -s` ~/.config/openbox/menu.xml
ln -sf ~/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -sf ~/etc/openbox/tint2rc-`hostname -s` ~/.config/tint2/tint2rc
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config

sudo ln -sf ~/etc/30-touchpad.conf /etc/X11/xorg.conf.d/.
sudo ln -sf ~/etc/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf

sudo systemctl disable gdm
sudo systemctl enable lightdm
```

# Uninstall
```
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .config/gtk-3.0/settings.ini .config/{openbox,tint2} .cache/{openbox,tint2}
```
