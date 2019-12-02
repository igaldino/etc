# Install

## Debian
```
sudo apt install -y i3-wm i3status
```

## Fedora
```
sudo dnf install -y i3 i3status
```

# Settings
```
mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status
ln -sf ~/etc/i3/config-`hostname -s` ~/.config/i3/config
ln -sf ~/etc/i3/i3status.conf ~/.config/i3status/config
```

## Cleaning
```
rm -rf ~/.config/{i3,i3status}
```
