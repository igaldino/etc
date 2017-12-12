Fedora

sudo dnf install \
	fluxbox \
	lightdm-gtk-greeter-settings \
	network-manager-applet \
	pnmixer \
	feh \
	arc-theme \
	pop-icon-theme \
	xcompmgr

sudo dnf copr enable mrbloups/compton 
sudo dnf install compton
