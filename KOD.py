from rovpy import rovpy
import time
import pymavlink
from pymavlink import ardupilotmega

master = rovpy.connectrov("MANUAL", "/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

master.wait_heartbeat()

master.arducopter_arm()

def hiz(value):
    hizMin = -1 
    hizMax = 1 
    pwmMin = 1100 
    pwmMax = 1900 
    hizSpan = hizMax - hizMin
    pwmSpan = pwmMax - pwmMin
    valueScaled = float(value - hizMin) / float(hizSpan)
    return pwmMin + (valueScaled * pwmSpan)

#Sigorta atacak mı denemesi

ps = time.time()
now = ps
while (now-ps)<1:
    now = time.time()

    id = 5
    pwm = 0

    if id < 1:
        print("Channel 1 ve 9 araliginda olmalidir.")

    if id < 9:
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = hiz(pwm)
        master.mav.rc_channels_override_send(
            master.target_component,             
            *rc_channel_values,mavutil.chan8_raw)