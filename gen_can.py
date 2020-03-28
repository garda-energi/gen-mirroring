#!/usr/bin/python3
#
# Make sure Python-CAN is installed first http://skpang.co.uk/blog/archives/1220
#
# 14-02-20 Puja Kusuma
#

# import the library
import can 
import time 
import os
import threading
import RPi.GPIO as GPIO
from datetime import datetime

# main function
def threadRxCan(msg) :
    # receive messages
    while True:
        # get received message (blocking)
        try:
            frame = bus.recv()
        except: 
            print("Receiving failed.")
        else:
            # debugging
            if(DEBUG) :
                canDebugFrame(frame)

            # set Backlight Control from Submodule.Daylight frame
            # if(frame.arbitration_id == CAN_ID_SUBMODULE) :
            #     canRxSubModule(frame.data)

            # set Datetime from RTC frame
            elif(frame.arbitration_id == CAN_ID_RTC) :
                canRxRTC(frame.data)
        
        bus.send(msg)

def threadTxCan(msg) :
    # send heartbeat message
    while True:
        try:
            bus.send(msg)
        except:
            print("Sending failed.")
        finally:
            time.sleep(0.5)

# other functions
def canDebugFrame(frame, conversion = "hex") :
    formatter = "0x{:02X} "
    if conversion == "bin" :
        formatter = "{:08b} "
    elif conversion == "decimal" :
        formatter = "{:>3d} "

    print("0x{:03X}[{:d}]: {}".format(
        frame.arbitration_id, 
        frame.dlc, 
        "".join(formatter.format(i) for i in frame.data)
    ))

def canRxSubModule(data) :
    try:
        backlight_state = (data[0] >> 7) & 1
        # print("state = ", backlight_state)
    except: 
        print("SubModule Frame is corrupted, parsing failed.")
    else:
        GPIO.output(GPIO_LCD_BACKLIGHT, backlight_state)

def canRxRTC(data) :
    try:
        # print("%d-%d-%d %d:%d:%d" % (data[5], data[4], data[3], data[2], data[1], data[0]))
        rtc = datetime(YEAR_PREFIX+data[5], data[4], data[3], data[2], data[1], data[0], 0)
    except:
        print("RTC Frame is corrupted, parsing failed.")
    else :
        now = datetime.now()
        delta_seconds = abs(rtc-now).total_seconds()

        # check time dilation
        if delta_seconds > SECONDS_DILATION_MAX :
            # set system datetime
            os.system("sudo timedatectl set-time '{}-{}-{} {}:{}:{}'".format(
                rtc.year, rtc.month, rtc.day, rtc.hour, rtc.minute, rtc.second
            ))       
            time.sleep(0.1)

# define start point
if __name__ == '__main__':     
    # global variables
    DEBUG = not False
    YEAR_PREFIX = 2000
    SECONDS_DILATION_MAX = 60
    GPIO_LCD_POWER = 43
    GPIO_LCD_BACKLIGHT = 42
    CAN_ID_SUBMODULE = 0x000
    CAN_ID_RTC = 0x001 
    CHANNEL = "can0"
    BITRATE = 500000

    # GPIO initialization
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_LCD_POWER, GPIO.OUT) 
    GPIO.setup(GPIO_LCD_BACKLIGHT, GPIO.OUT) 

    # Turn on LCD
    GPIO.output(GPIO_LCD_POWER, 1)

    # activate the CAN driver
    print("Enabling %s driver..." % (CHANNEL))
    os.system("sudo /sbin/ip link set %s up type can bitrate %d" % (CHANNEL, BITRATE))
    time.sleep(0.1)

    # create bus instance
    try:
        bus = can.ThreadSafeBus(bustype='socketcan_native', channel=CHANNEL, bitrate=BITRATE)
    except OSError:
        print("Bus %s is error." % CHANNEL)
        exit()
    else: 
        print("Bus %s is ready." % CHANNEL)
        # disable ntp sync
        os.system("sudo timedatectl set-ntp no") 
        time.sleep(0.1)
    
    # make RTOS
    msg = can.Message(arbitration_id=354, is_remote_frame=True)
    thRxCan = threading.Thread(target=threadRxCan, args=(msg,))
    thTxCan = threading.Thread(target=threadTxCan, args=(msg,))

    # start RTOS
    try:
        thRxCan.start()   
        # thTxCan.start()     

    except KeyboardInterrupt:
        bus.shutdown()
        print("\nProgram is terminated.")