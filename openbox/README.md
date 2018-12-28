# Install
```
sudo dnf install openbox compton obconf nitrogen tint2 volumeicon network-manager-applet redshift-gtk python2-gobject i3lock xautolock xdotool dunst rofi numix-gtk-theme numix-icon-theme-circle
```

# Settings
```
mkdir -p ~/.config/openbox
mkdir -p ~/.config/gtk-3.0
mkdir -p ~/.config/tint2
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/openbox/rc.xml-`hostname -s` ~/.config/openbox/rc.xml
ln -sf ~/etc/openbox/menu.xml-`hostname -s` ~/.config/openbox/menu.xml
ln -sf ~/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -sf ~/etc/openbox/tint2rc-`hostname -s` ~/.config/tint2/tint2rc
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.gtkrc-2.0 ~/.config/gtk-3.0/settings.ini ~/.config/{redshift.conf,openbox,tint2,dunst,rofi,volumeicon,nitrogen} ~/.cache/{openbox,tint2,dunst,rofi}
```

