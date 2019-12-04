# Install

## Debian
```
sudo apt install -y lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lxpolkit compton blueman pasystray network-manager-gnome pavucontrol i3lock xautolock xbacklight python-gobject dunst rofi lxappearance lxterminal mousepad pcmanfm nitrogen redshift-gtk caffeine package-update-indicator fonts-ubuntu fonts-font-awesome arc-theme papirus-icon-theme
```

## Fedora
```
sudo dnf install -y lightdm-gtk lightdm-gtk-greeter-settings lxpolkit compton blueman pasystray network-manager-applet pavucontrol i3lock xautolock xbacklight python2-gobject dunst rofi lxappearance lxterminal leafpad pcmanfm nitrogen redshift-gtk google-noto-sans-fonts google-noto-sans-mono-fonts fontawesome-fonts arc-theme papirus-icon-theme
```

# Settings
```
mkdir -p ~/.config/gtk-3.0
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
echo "export QT_QPA_PLATFORMTHEME=gtk2" >> ~/.profile
sudo cp ~/etc/lightdm.conf /etc/lightdm/lightdm.conf
sudo cp ~/etc/lightdm-gtk-greeter.conf-numix /etc/lightdm/lightdm-gtk-greeter.conf
sudo systemctl enable lightdm
```

## Cleaning
```
rm -rf ~/.gtkrc-2.0 ~/.config/gtk-3.0/settings.ini ~/.config/{redshift.conf,dunst,rofi,volumeicon,nitrogen} ~/.cache/{dunst,rofi3.druncache,rofi-3.runcache,i3lock.png}
sudo rm -rf /etc/lightdm
```
