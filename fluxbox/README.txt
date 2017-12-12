Fedora

sudo dnf install \
	fluxbox \
	lightdm-gtk-greeter-settings \
	network-manager-applet \
	feh \
	arc-theme \
	pop-icon-theme

sudo dnf copr enable mrbloups/compton 
sudo dnf install compton
