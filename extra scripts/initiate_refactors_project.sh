#!/bin/bash

#------------------- OPTIONAL  --------------------
#Monitor the system
#
myip=$(curl -s https://ipinfo.io/ip)
#Download docker
if ! docker --version &> /dev/null; then
	echo " > Docker is not installed. Installing Docker..."
	sudo apt-get update -y
	sudo apt-get install ca-certificates curl 
	sudo install -m 0755 -d /etc/apt/keyrings 
	sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
	sudo chmod a+r /etc/apt/keyrings/docker.asc
	echo \
	  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
	  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
	  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update -y
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
	if docker --version &> /dev/null; then
    		echo " > Docker installed successfully."
	else
		echo " > Docker failed to install"
	fi
else
	echo " > Docker already installed"
fi
# Initiate Docker containers
docker run -d --name glances --restart="unless-stopped" -p 61208-61209:61208-61209 -e TZ="Europe/Paris" -e GLANCES_OPT="-w" -v /var/run/docker.sock:/var/run/docker.sock:ro --pid host joweisberg/glances:latest
if docker ps | grep -q "glances"; then
    echo " > Glances container started successfully: http://$myip:61208/"
else
    echo " > Failed to start Glances container."
fi
docker container run -d --name dashdot --restart="unless-stopped" -p 80:3001 -v /:/mnt/host:ro -e DASHDOT_ALWAYS_SHOW_PERCENTAGES=true -e DASHDOT_WIDGET_LIST=cpu,ram,storage,network      --privileged  mauricenino/dashdot
if docker ps | grep -q "dashdot"; then
    echo " > Dashdot container started successfully: http://$myip/"
else
    echo " > Failed to start Dashdot container."
fi
#--------------- END OPTIONAL  -----------------

# Check if Python is installed 
if ! python3 --version &> /dev/null; then
    echo " > Python is not installed. Installing Python..."
    sudo apt-get install python3 -y
	if python3 --version &> /dev/null; then
        echo " > Python is already installed."
	else
        echo " > Failed to install Python."
		echo " > Proceed manually."
	fi
else
	echo " > Python already installed"
fi
#check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo " > pip is not installed. Installing pip..."
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    rm get-pip.py
	if command -v pip3 &> /dev/null; then
        echo " > pip installed successfully."
    else
        echo " > Failed to install pip."
		echo " > Proceed manually."
    fi
else
	echo ' > pip already installed'
fi
#install git
if ! git --version &> /dev/null; then
    echo " > Git is not installed. Installing Git..."
    sudo apt-get install git -y
    if git --version &> /dev/null; then
        echo " > Git installed successfully."
    else
        echo " > Failed to install Git."
        echo " > Proceed manually."
    fi
else
    echo ' > Git already installed'
fi
#download Refactors project from github
# replace with github link, for now the project is private in github, replace with auth link from github to download
git clone -->LINK<--
if [ -d "Refactors-pattern-recognition-for-python" ]; then
   echo " > Project : [Refactors-pattern-recognition-for-python] downloaded successfully with git."
else
    echo " > Project : [Refactors-pattern-recognition-for-python] failed to download  with git."
    echo " > Proceed manually."
    exit 1
fi
#make folder named projects
mkdir projects
#install requirements 
cd Refactors-pattern-recognition-for-python
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo " > Projects requirements installed was successful."
else
    echo " > Projects requirements failed to install."
fi
#create config.py
cd src
exec 3<> config.py
    echo "PROJECT_FOLDER_PATH=  r'/root/projects/'" >&3
    echo "MINIFY_HTML_BOOL= True" >&3
exec 3>&-
#copy the appropriate script to download the releases
cp /root/Refactors-pattern-recognition-for-python/extra\ scripts/download_releases_from_github.py /root/projects/download_releases_from_github.py
cp /root/Refactors-pattern-recognition-for-python/extra\ scripts/github_links_list.txt /root/projects/github_links_list.txt
cd /root/projects
exec 3<> config.py
#----------------Replace with github token-------------------
# generate a token here https://github.com/settings/tokens 
# check the permissions for :
#  - 'Read access of projects' 
#  - 'Download packages from GitHub Package Registry'
    echo "GITHUB_TOKEN = TOKEN " >&3
    echo "MAX_RELEASES_TO_DOWNLOAD = 30" >&3
exec 3>&-
#download the projects
echo " > Starting downloading the projects from github"
python3 download_releases_from_github.py
if [ $? -eq 0 ]; then
    echo " > Downloading projects from GitHub was successful."
else
    echo " > Downloading projects from GitHub failed."
fi