# Install
```
sudo dnf install i3 i3status nitrogen volumeicon network-manager-applet redshift-gtk fontawesome-fonts python2-gobject i3lock xautolock dunst rofi

```

# Settings
```
mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status
mkdir -p ~/.config/gtk-3.0
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -s ~/etc/i3/config-`hostname -s` ~/.config/i3/config
ln -s ~/etc/i3/i3status.conf-`hostname -s` ~/.config/i3status/config
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.gtkrc-2.0 ~/.config/gtk-3.0/settings.ini ~/.config/{redshift.conf,i3,i3status,dunst,rofi,volumeicon,nitrogen} ~/.cache/{i3,i3status,dunst,rofi}
`
