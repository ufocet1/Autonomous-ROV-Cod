from rovpy import rovpy
import time


rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

#Sigorta atacak mı denemesi

timer = Boolean.timer(1.0)
timer.start()
while timer:
    rovpy.forward(1)
