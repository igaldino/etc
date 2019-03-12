# Install

Software List:
* i3
* i3Status
* Awesome Fonts

# Settings
```
mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status

ln -sf ~/etc/i3/config-`hostname -s` ~/.config/i3/config
ln -sf ~/etc/i3/i3status.conf-`hostname -s` ~/.config/i3status/config
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.config/{i3,i3status}
```
