## DEBIAN

# REPOSITORIES
cat<<EOF | sudo tee -a /etc/apt/sources.list
deb http://debian.c3sl.ufpr.br/debian/ $(lsb_release -cs)-backports main contrib non-free
deb-src http://debian.c3sl.ufpr.br/debian/ $(lsb_release -cs)-backports main contrib non-free
EOF
sudo apt update -y && sudo apt upgrade -y

# SOFTWARE
sudo apt install -y accountsservice adwaita-qt arc-theme audacity blueman bluez-firmware breeze-cursor-theme compton dia dirmngr dunst evince file-roller firmware-misc-nonfree flatpak fonts-font-awesome fonts-ubuntu fwupd galculator gedit git gitg gvfs-backends hexchat i3lock imagemagick intel-microcode keepassxc lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lxappearance lxpolkit lxterminal meld mpv nautilus-dropbox network-manager-gnome nitrogen papirus-icon-theme pavucontrol pasystray pcmanfm pulseaudio-module-bluetooth python-gobject qt5-style-plugins redshift-gtk rofi rsync tlp tlp-rdw unrar viewnior vim-nox xautolock xbacklight xfce4-power-manager xserver-xorg-core xserver-xorg-input-libinput

# Google Chrome
wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb

# FLATPAK
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install -y flathub \
	org.gtk.Gtk3theme.Arc-Dark \
	org.libreoffice.LibreOffice \
	org.mozilla.Firefox

# SETTINGS

# GRUB
sudo sed -i 's/quiet/quiet loglevel=3/1' /etc/default/grub
sudo sed -i 's/^GRUB_TIMEOUT=.*$/GRUB_TIMEOUT=0/1' /etc/default/grub
sudo update-grub

## FEDORA

# REPOSITORIES
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf update -y

# SOFTWARE
sudo dnf install -y adwaita-qt arc-theme audacity bash-completion blueman breeze-cursor-theme brightlight compton dia dunst duplicity evince file-roller flameshot flatpak fontawesome-fonts fwupd galculator gedit git gitg i3lock keepassxc libreoffice lightdm-gtk lightdm-gtk-greeter-settings lxappearance lxpolkit lxterminal meld mpv nautilus-dropbox network-manager-applet NetworkManager-wifi nitrogen papirus-icon-theme pasystray pavucontrol pcmanfm python3-gobject redshift-gtk rofi rsync unrar viewnior vim wget xautolock xfce4-power-manager

# Google Chrome
wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo dnf install -y ./google-chrome-stable_current_x86_64.rpm && rm google-chrome-stable_current_x86_64.rpm

# FLATHUB
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install -y flathub org.gtk.Gtk3theme.Arc-Dark

# SETTINGS

# Journal size to speed boot
sudo sed -i 's/^#SystemMaxUse=/SystemMaxUse=100M/1' /etc/systemd/journald.conf
sudo journalctl --vacuum-size=100M

# GRUB
sudo sed -i 's/quiet/quiet loglevel=3/1' /etc/default/grub
sudo sed -i 's/^GRUB_TIMEOUT=.*$/GRUB_TIMEOUT=0/1' /etc/default/grub
sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg || sudo grub2-mkconfig -o /boot/grub2/grub.cfg

## GENERAL SETTINGS

# GTK
gsettings set org.gtk.Settings.FileChooser sort-directories-first true

# SSD
sudo systemctl enable fstrim.timer

# Lightdm
sudo mv /etc/lightdm/lightdm.conf /etc/lightdm/lightdm.conf.old
cat<<EOF | sudo tee /etc/lightdm/lightdm.conf
[LightDM]
[Seat:*]
greeter-hide-users=false
[XDMCPServer]
[VNCServer]
EOF

# Touchpad
sudo mkdir -p /etc/X11/xorg.conf.d
cat<<EOF | sudo tee -a /etc/X11/xorg.conf.d/30-touchpad.conf
Section "InputClass"
	Identifier "libinput touchpad catchall"
	Driver "libinput"
	MatchIsTouchpad "on"
	MatchDevicePath "/dev/input/event*"
	Option "Tapping" "on"
	Option "ClickMethod" "clickfinger"
EndSection
EOF

