# Standard of Procedure:
1. Download Crankshaft image:
   - https://getcrankshaft.com/
2. Burn that image to MiniPC using BalenaEtcher
   - https://www.balena.io/etcher/
3. Copy these files to **/boot/** folder:
   - *cmdline.txt*
   - *config.txt*
4. Copy this file to **/boot/overlays/** forlder:
   - *ft6236-touch.dts*
      - `sudo dtc -@ -I dts -O dtb -o ft6236-touch.dtbo ft6236-touch.dts`
5. After raspberry successfully booted, use "USB Thether for Internet Connection" then execute:
   - `sudo apt update`
   - `sudo apt upgrade`
   - `sudo rpi-update`
6. Install can tools (for testing)
   - `sudo apt-get install can-utils`
7. Copy this file to **/etc/network/** to automate the CAN Driver initialization
   - *interfaces*
8. Install python program dependencies:
   - `sudo apt-get install python3-pip`
   - `sudo pip3 install DateTime`
   - `sudo pip3 install RPi.GPIO`
   - `sudo pip3 install python-can`
9. Copy this file to **/home/pi/gen/**
   - *gen.py*
	   - `chmod +x gen.py`
10. Copy this file to **/etc/systemd/system**
   - *gen.service*
	   - `sudo chmod 644 gen.service`
11. Activate that service:
	- `sudo systemctl daemon-reload`
	- `sudo systemctl enable gen.service`
	- `sudo systemctl start gen.service`
	- `sudo systemctl status gen.service`

## NB:
- Crankshaft files: /opt/crankshaft/
- Startup files: /boot/startup.sh or /boot/startup.py
- SocketCAN C language: http://skpang.co.uk/blog/archives/1199
- Python-CAN example: http://github.com/skpang/PiCAN-Python-examples
  
