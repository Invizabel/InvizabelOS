import os

# install everything
os.system("clear")
os.system("sudo dnf update -y")
os.system("sudo dnf autoremove -y")
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
os.system("sudo dnf install VirtualBox -y")
os.system("sudo dnf install bleachbit -y")
os.system("sudo dnf install wireshark -y")
os.system("sudo dnf install foremost -y")
os.system("sudo dnf install htop -y")
os.system("sudo dnf install neofetch -y")
os.system("sudo dnf install steam -y")
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

# install brave
os.system("sudo dnf install dnf-plugins-core -y")
os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo")
os.system("sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc")
os.system("sudo dnf install brave-browser -y")

# install virtualbox dependencies
os.system("sudo dnf install kernel-headers kernel-devel dkms  -y")
os.system("sudo dnf groupinstall development-tools -y")

# install wine dependencies for some games
os.system("sudo dnf install winetricks -y")
os.system("winetricks videomemorysize=4196")

# change to Pixel Theme
os.system("git clone https://github.com/Invizabel/Pixel")
os.system("unzip Pixel/Pixel.zip")
os.system("sudo cp -r Pixel /usr/share/icons")
os.system("cd -")
os.system("sudo rm -r Pixel")
os.system('gsettings set org.gnome.desktop.interface icon-theme "Pixel"')

# destroy old data
os.system("fstrim --all")

# reboot
os.system("reboot")
