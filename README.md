#SOP how to configure the Raspberry:
1. Download Crankshaft image, and burn to MiniPC using BalenaEtcher
2. Copy these files to **/boot/** folder:
   - *cmdline.txt*
   - *config.txt*
3. Copy this file to **/boot/overlays/** forlder:
   - *ft6236-touch.dts*
      - `sudo dtc -@ -I dts -O dtb -o ft6236-touch.dtbo ft6236-touch.dts`
4. After raspberry successfully booted, use "USB Thether for Internet Connection" then execute:
   - `sudo apt update`
   - `sudo apt upgrade`
   - `sudo rpi-update`
5. Install can tools (for testing)
   - `sudo apt-get install can-utils`
6. Copy this file to **/etc/network/** to automate the CAN Driver initialization
   - *interfaces*
7. Install python program dependencies:
   - `sudo apt-get install python3-pip`
   - `sudo pip3 install DateTime`
   - `sudo pip3 install RPi.GPIO`
   - `sudo pip3 install python-can`
8. Copy this file to **/home/pi/gen/**
   - *gen.py*
	   - `chmod +x gen.py`
9. Copy this file to **/etc/systemd/system**
   - *gen.service*
	   - `sudo chmod 644 gen.service`
10. Activate that service:
	- `sudo systemctl daemon-reload`
	- `sudo systemctl enable gen.service`
	- `sudo systemctl start gen.service`
	- `sudo systemctl status gen.service`

##NB:
- Crankshaft files: /opt/crankshaft/
- Startup files: /boot/startup.sh or /boot/startup.py
- SocketCAN C language: http://skpang.co.uk/blog/archives/1199
- Python-CAN example: http://github.com/skpang/PiCAN-Python-examples
  
