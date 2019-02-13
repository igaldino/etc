# Install
```
sudo dnf install openbox obconf nitrogen tint2 volumeicon network-manager-applet redshift-gtk python2-gobject i3lock xautolock xdotool dunst rofi
```

# Settings
```
mkdir -p ~/.config/openbox
mkdir -p ~/.config/tint2
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

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
rm -rf ~/.config/{redshift.conf,dunst,rofi,volumeicon,nitrogen} ~/.cache/{dunst,rofi3.druncache,rofi-3.runcache,i3lock.png} ~/.config/{openbox,tint2} ~/.cache/{openbox,tint2}
```

