import os

# install everything
os.system("clear")
os.system("sudo dnf update -y")
os.system("sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
os.system("sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm -y")
os.system("sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y")
os.system("sudo dnf install akmod-nvidia -y")
os.system("sudo dnf install nano -y")
os.system("sudo dnf install gnome-tweaks -y")
os.system("sudo dnf install clamav clamtk -y")
os.system("sudo dnf install fail2ban -y")
os.system("sudo dnf install nmap -y")
os.system("sudo dnf install nikto -y")
os.system("sudo dnf install bleachbit -y")
os.system("sudo dnf install wireshark -y")
os.system("sudo dnf install foremost -y")
os.system("sudo dnf install htop -y")
os.system("sudo dnf install neofetch -y")
os.system("sudo dnf install steam -y")
os.system("sudo dnf install tor -y")
os.system("sudo dnf install wine -y")
os.system("sudo dnf install idle -y")
os.system("sudo dnf install chromium -y")
os.system("sudo dnf install gnome-shell-extension-caffeine.noarch -y")
os.system("sudo dnf install gnome-shell-extension-dash-to-dock.noarch -y")

# install python modules
os.system("sudo dnf install python3-pip -y")
os.system("pip3 install TheSilent")
os.system("sudo pip3 install TheSilent")
os.system("pip3 install VolorSavanna")
os.system("pip3 install sqlmap")
os.system("pip3 install autopep8")
os.system("pip3 install pylint")
os.system("pip3 install build")
os.system("pip3 install twine")

# install wine dependencies for some games
os.system("sudo dnf install winetricks -y")
os.system("winetricks videomemorysize=2048")

# start and enable tor on start up
os.system("sudo systemctl start tor")
os.system("sudo systemctl enable tor")

# change to Pixel Theme
os.system("git clone https://github.com/Invizabel/Pixel")
os.system("unzip Pixel/Pixel.zip")
os.system("sudo cp -r Pixel /usr/share/icons")
os.system("cd -")
os.system("sudo rm -r Pixel")
os.system('gsettings set org.gnome.desktop.interface icon-theme "Pixel"')

# destroy old data
os.system("sudo dnf autoremove -y")
os.system("sudo dnf clean all")
os.system("fstrim --all")

# reboot
os.system("reboot")
