# Install
```
sudo dnf install fluxbox compton nitrogen volumeicon network-manager-applet redshift-gtk python2-gobject i3lock xautolock dunst numix-gtk-theme numix-icon-theme-circle
```

# Settings
```
mkdir -p ~/.fluxbox/styles/Numix
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi

ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/theme.cfg-numix ~/.fluxbox/styles/Numix/theme.cfg
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/fluxbox/init-`hostname -s` ~/.fluxbox/init
ln -sf ~/etc/fluxbox/keys-`hostname -s` ~/.fluxbox/keys
ln -sf ~/etc/fluxbox/menu-`hostname -s` ~/.fluxbox/menu
ln -sf ~/etc/fluxbox/startup-`hostname -s` ~/.fluxbox/startup
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
```

# Uninstall
```
sudo dnf history undo ...
rm -rf .gtkrc-2.0 .config/gtk-3.0/settings.ini .fluxbox .config/{redshift.conf,dunst} .cache/{dunst}
```
