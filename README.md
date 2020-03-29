# Standard of Procedure

1. Download Crankshaft image:
   - <https://getcrankshaft.com/>
2. Burn that image to MiniPC using BalenaEtcher
   - <https://www.balena.io/etcher/>
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

## NB

- MiniPC Hardware: <https://www.waveshare.com/compute-module-3-plus-8gb.htm>
- CM3 Board: <https://www.waveshare.com/wiki/Compute_Module_IO_Board_Plus>
- Crankshaft files: */opt/crankshaft/*
- Startup files: */boot/startup.sh* or */boot/startup.py*
- SocketCAN C language: <http://skpang.co.uk/blog/archives/1199>
- Python-CAN example: <http://github.com/skpang/PiCAN-Python-examples>

## Raspberry Credentials

1. Raspberry Zero W:
   - pi:gen
2. Raspberry Compute Module 3+:
   - pi:gardagen
   - root:garda

## Host Configuration

1. Follow this instructions to install PCAN driver:
   - <https://github.com/SICKAG/sick_line_guidance/blob/master/doc/pcan-linux-installation.md>
2. Use this tools to send/receive CAN data:
   - `sudo apt-get install can-utils`
   - <https://github.com/linux-can/can-utils>
  
## Software Progress

- [ ] raspi-gpio: Missing DPI8 (GPIO12) and DPI9 (GPIO13) pin
- [x] Use dtoverlay=spi-gpio35-39
- [x] Handle SPI-to-CAN module
- [x] Handle output GPIO of LCD Power, according to OS state, internal PCB
- [x] Handle output GPIO of LCD Backlight, according to RTC Time, internal PCB
- [x] Handle GPIO / CAN signal of Phone Connected status to VCU/HMI-1
- [x] Handle GPIO / CAN signal of RTC Daylight status from VCU
- [x] Hide booting process from main LCD
- [x] Pin that can be eliminated when CAN exist:  
  - [GPIO34] SHUTDOWN  
  - [RUN pin] RESET / WAKE
  - [GPIO44] PHONE_CONNECTED  
  - [GPIO42] RTC_DAYLIGHT / BRIGHTNESS_CONTROL

## Hardware Progress

- [x] Add SMD Fuse
- [x] Add Charger IC for Phone
- [x] Add GPIO to control HMI brightness (parallel with EXTI Button)
- [x] Add GPIO to control HMI power
- [x] Add GPIO input for RPI power ON after HALT (held RUN pin to low)
- [x] Add Pull-Down Resistor in MOSFET brightness control
- [x] Increase the diameter of corner holes
- [x] Add GPIO input for RPI power OFF (held GPIO-34 to low)
- [x] Add GPIO output for HMI Indicator
- [x] Add SPI2CAN (use solder jumper for alternative)
- [x] Extend the connector for Serial to Solder
- [x] Change TOP and BOTTOM layer for GND only
- [x] Add logo, module name, module version
- [x] Check USB parallel solder jumper
- [x] Check IC Charger compatibility with the Software
- [x] Remove all values, only labels
- [x] Add raster to the empty space
- [x] Make LCD, Touch, Booster module control power be one
- [x] Handle new Mini-PC with the PCB
- [ ] Remove un-necessary GPIO pin (replaced by CAN)
- [ ] Change MOSFET (LCD Power & Backlight) Control to Transistor
- [ ] Fix USB IC Current Limiter problem
