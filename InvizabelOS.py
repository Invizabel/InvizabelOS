import os

#install everything
os.system("clear")
os.system("sudo dnf install clamav clamtk -y")
os.system("sudo dnf install fail2ban -y")
os.system("sudo dnf install htop -y")
os.system("sudo dnf install neofetch -y")
os.system("sudo dnf install idle -y")
os.system("sudo dnf install chromium -y")
os.system("sudo dnf install gnome-shell-extension-caffeine.noarch -y")
os.system("sudo dnf install gnome-shell-extension-dash-to-dock.noarch -y")
os.system("sudo dnf install python3-pip -y")
os.system("pip install requests")
os.system("pip install urllib3")
os.system("pip install selenium")
os.system("pip install bs4")
os.system("pip install numpy")
os.system("pip install TheSilentPyPi")
os.system("pip install VolorSavanna")

#change to Pixel Theme
os.system("git clone https://github.com/Invizabel/Pixel")
os.system("cd Pixel")
os.system("unzip Pixel.zip")
os.system("sudo cp -r Pixel /usr/share/icons")
os.system("cd -")
os.system("sudo rm -r Pixel")
os.system('gsettings set org.gnome.desktop.interface icon-theme "Pixel"')
