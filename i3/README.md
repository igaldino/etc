# Install
```
sudo dnf install i3 i3status nitrogen volumeicon network-manager-applet redshift-gtk fontawesome-fonts python2-gobject i3lock xautolock dunst rofi

```

# Settings
```
mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/i3/config-`hostname -s` ~/.config/i3/config
ln -sf ~/etc/i3/i3status.conf-`hostname -s` ~/.config/i3status/config
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.config/{redshift.conf,dunst,rofi,volumeicon,nitrogen} ~/.cache/{dunst,rofi3.druncache,rofi-3.runcache,i3lock.png} ~/.config/{i3,i3status}
```

