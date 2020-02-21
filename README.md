SOP how to configure the Raspberry:
1. Download Crankshaft image, and burn to MiniPC using BalenaEtcher
2. Copy these files to /boot/ folder:
   - cmdline.txt
   - config.txt
3. Copy "ft6236-touch.dts" to /boot/overlay/ then compile that ".dts" file to ".dtbo"
4. After raspberry successfully booted, use "USB Thether for Internet Connection" then update
   - sudo apt update
   - sudo apt upgrade
   - sudo rpi-update
5. Install can tools (for testing)
   - sudo apt-get install can-utils
6. Put "interfaces" file to "/etc/network/" to automate the CAN Driver initialization
7. SocketCAN references:
   - C: 
     - Example: http://skpang.co.uk/blog/archives/1199
   - Python: 
     - Example: http://github.com/skpang/PiCAN-Python-examples
     - Installation: http://installvirtual.com/install-python-3-7-on-raspberry-pi/
     - sudo apt-get install python3-pip
     - sudo pip3 install DateTime
     - sudo pip3 install RPi.GPIO
     - sudo pip3 install pyserial
     - sudo pip3 install python-can
8. Copy "gen.py" to /home/pi/gen/
	- chmod +x /home/pi/gen/gen.py
9. Copy "gen.service" to /etc/systemd/system
	- sudo chmod 644 /etc/systemd/system/gen.service
10. Activate that service:
	sudo systemctl daemon-reload
	sudo systemctl enable gen.service
	sudo systemctl start gen.service
	sudo systemctl status gen.service

NB:
- Crankshaft files: /opt/crankshaft/
- Startup files: /boot/startup.sh|startup.py
