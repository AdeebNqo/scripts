#Hack-Install

Code for locating certain packages and copying them into current directory.
I wrote this with the purpose of copying gstreamer plugins.

##Instructions

1. dpkg-query -l | grep gstrea > output.txt
2. python src/main.py output.txt
