# Install

Software list:
* fluxbox

# Settings
```
mkdir -p ~/.fluxbox/styles/Numix

ln -sf ~/etc/fluxbox/theme.cfg-numix ~/.fluxbox/styles/Numix/theme.cfg
ln -sf ~/etc/fluxbox/init-`hostname -s` ~/.fluxbox/init
ln -sf ~/etc/fluxbox/keys-`hostname -s` ~/.fluxbox/keys
ln -sf ~/etc/fluxbox/menu-`hostname -s` ~/.fluxbox/menu
ln -sf ~/etc/fluxbox/startup-`hostname -s` ~/.fluxbox/startup
```

# Uninstall
```
sudo dnf history undo ...
rm -rf ~/.fluxbox 
```

