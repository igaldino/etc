# Install

Software list:
* FluxBox

## Fedora
```
sudo dnf install -y fluxbox
```

# Settings
```
mkdir -p ~/.fluxbox/styles/Numix
ln -sf ~/etc/fluxbox/Arc ~/.fluxbox/styles/.
ln -sf ~/etc/fluxbox/theme.cfg-numix ~/.fluxbox/styles/Numix/theme.cfg
ln -sf ~/etc/fluxbox/init ~/.fluxbox/init
ln -sf ~/etc/fluxbox/keys ~/.fluxbox/keys
ln -sf ~/etc/fluxbox/menu ~/.fluxbox/menu
ln -sf ~/etc/fluxbox/startup ~/.fluxbox/startup
```

## Cleaning
```
rm -rf ~/.fluxbox 
```

