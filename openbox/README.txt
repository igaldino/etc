#sudo dnf install openbox xbacklight feh conky xorg-x11-drv-libinput tint2 volumeicon xorg-x11-server-utils network-manager-applet obconf dunst arc-theme pop-icon-theme
sudo dnf install openbox obconf nitrogen conky tint2 pnmixer xfce4-power-manager xfce4-notifyd xorg-x11-drv-libinput xorg-x11-server-utils network-manager-applet

cat .gtkrc-2.0 
cat .config/gtk-3.0/settings.ini 

#xinput list
#xinput list-props 12
xinput set-prop 12 283 1

feh --bg-scale Imagens/Kill\ La\ Kill.png 
feh --bg-scale Imagens/Kill\ La\ Kill.png &
feh --bg-scale Imagens/grid.png 

tint2 &
conky &
sudo dnf install p7zip
killall conky
conky &

sudo dnf install compton
sudo dnf install slock
compton&
vi ~/.config/openbox/autostart

cat .gtkrc-2.0 
cat .config/gtk-3.0/settings.ini 
cat .config/gtk-2.0/gtkfilechooser.ini 

slock
slock "Enter password:"
slock ls
slock

vi .conkyrc 
killall conky
conky&
vi .config/openbox/autostart 

mkdir .config/dunst
mv Downloads/dunstrc1 .config/dunst/dunstrc
dunst &
notify-send "Teste"

setxkbmap -layout "us,br" -variant "intl,abnt2" -option "grp:win_space_toggle"
vi .config/openbox/autostart 

# Adwaita
https://www.opendesktop.org/content/show.php/Adwaita-openbox?content=155042

# Adwaita Dark
https://www.box-look.org/p/1017591/

# Uninstall
sudo dnf history undo 142
sudo dnf history undo 139
rm .gtkrc-2.0 .config/gtk-3.0/settings.ini 
rm -rf .fehbg .fluxbox .conkyrc .themes
rm -rf .config/{openbox,volumeicon,dunst,tint2}
rm -rf .cache/{openbox,tint2,midori}
