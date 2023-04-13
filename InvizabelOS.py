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
os.system("sudo dnf install VirtualBox -y")
os.system("sudo dnf install bleachbit -y")
os.system("sudo dnf install wireshark -y")
os.system("sudo dnf install foremost -y")
os.system("sudo dnf install htop -y")
os.system("sudo dnf install neofetch -y")
os.system("sudo dnf install wine -y")
os.system("sudo dnf install steam -y")
os.system("sudo dnf install idle -y")
os.system("sudo dnf install chromium -y")
os.system("sudo dnf install gnome-shell-extension-caffeine.noarch -y")
os.system("sudo dnf install gnome-shell-extension-dash-to-dock.noarch -y")
os.system("sudo dnf install python3-pip -y")
os.system("pip install TheSilent")
os.system("sudo pip install TheSilent")
os.system("pip install VolorSavanna")
os.system("pip install sqlmap")

# install brave
os.system("sudo dnf install dnf-plugins-core -y")
os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo")
os.system("sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc")
os.system("sudo dnf install brave-browser -y")

# install virtualbox dependencies
os.system("sudo dnf install kernel-headers kernel-devel dkms  -y")
os.system("sudo dnf groupinstall development-tools -y")

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
