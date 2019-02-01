# Install
```
sudo dnf install fluxbox compton nitrogen volumeicon network-manager-applet redshift-gtk python2-gobject i3lock xautolock dunst rofi
```

# Settings
```
mkdir -p ~/.fluxbox/styles/Numix
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/theme.cfg-numix ~/.fluxbox/styles/Numix/theme.cfg
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/fluxbox/init-`hostname -s` ~/.fluxbox/init
ln -sf ~/etc/fluxbox/keys-`hostname -s` ~/.fluxbox/keys
ln -sf ~/etc/fluxbox/menu-`hostname -s` ~/.fluxbox/menu
ln -sf ~/etc/fluxbox/startup-`hostname -s` ~/.fluxbox/startup
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.config/{redshift.conf,dunst,rofi,volumeicon,nitrogen} ~/.cache/{dunst,rofi3.druncache,rofi-3.runcache,i3lock.png} ~/.fluxbox 
```

