# etc
```
sudo dnf install lightdm-gtk lxpolkit xdg-user-dirs compton leafpad lxterminal pcmanfm firefox numix-gtk-theme numix-icon-theme
```

# Settings
```
mkdir -p ~/.config/gtk-3.0

ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
sudo cp ~/etc/30-touchpad.conf /etc/X11/xorg.conf.d/.
sudo cp ~/etc/lightdm.conf /etc/lightdm/lightdm.conf
sudo cp ~/etc/lightdm-gtk-greeter.conf-numix /etc/lightdm/lightdm-gtk-greeter.conf

sudo systemctl enable lightdm
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.gtkrc-2.0 ~/.config/gtk-3.0/settings.ini ~/.config/{leafpad,lxterminal,pcmanfm,libfm}
sudo rm /etc/X11/xorg.conf.d/30-touchpad.conf
sudo rm -rf /etc/lightdm
```

