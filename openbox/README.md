# Install

Software list:
* OpenBox
* ObConf
* Tint2

# Settings
```
mkdir -p ~/.config/openbox
mkdir -p ~/.config/tint2

ln -sf ~/etc/openbox/rc.xml-`hostname -s` ~/.config/openbox/rc.xml
ln -sf ~/etc/openbox/menu.xml-`hostname -s` ~/.config/openbox/menu.xml
ln -sf ~/etc/openbox/autostart-`hostname -s` ~/.config/openbox/autostart
ln -sf ~/etc/openbox/tint2rc-`hostname -s` ~/.config/tint2/tint2rc
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.config/{openbox,tint2} ~/.cache/{openbox,tint2}
```
