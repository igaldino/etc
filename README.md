# Install

Check INSTALL-MINI.md file

# Settings
```
mkdir -p ~/.config/gtk-3.0
mkdir -p ~/.config/dunst
mkdir -p ~/.config/rofi
echo ". ~/etc/bashrc" >> ~/.bashrc
ln -sf ~/etc/_xsessionrc ~/.xsessionrc
ln -sf ~/etc/redshift-sao-paulo.conf ~/.config/redshift.conf
ln -sf ~/etc/_gtkrc-2.0-numix ~/.gtkrc-2.0
ln -sf ~/etc/settings.ini-numix ~/.config/gtk-3.0/settings.ini
ln -sf ~/etc/dunstrc-numix ~/.config/dunst/dunstrc
ln -sf ~/etc/rofi.config-numix ~/.config/rofi/config
sudo cp ~/etc/lightdm.conf /etc/lightdm/lightdm.conf
sudo cp ~/etc/lightdm-gtk-greeter.conf-numix /etc/lightdm/lightdm-gtk-greeter.conf
sudo systemctl enable lightdm
```

# Cleaning
```
rm -rf ~/.gtkrc-2.0 ~/.config/gtk-3.0/settings.ini ~/.config/{redshift.conf,dunst,rofi,volumeicon,nitrogen} ~/.cache/{dunst,rofi3.druncache,rofi-3.runcache,i3lock.png}
sudo rm -rf /etc/lightdm
```
