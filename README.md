# etc
```
sudo dnf install lightdm-gtk xdg-user-dirs leafpad lxterminal pcmanfm firefox
```

# Settings
```
sudo ln -sf ~/etc/30-touchpad.conf /etc/X11/xorg.conf.d/.
sudo cp ~/etc/lightdm-gtk-greeter.conf-numix /etc/lightdm/lightdm-gtk-greeter.conf

sudo systemctl enable lightdm
```

# Uninstall
```
sudo dnf history undo ...
```

