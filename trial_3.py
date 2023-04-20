from rovpy import rovpy
import time

#Hızı kesince robot duruyorsa diye bir de braking mekanizması

#Kod süresince gittiği mesafeyi ölçün

rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

timer=Boolean.timer(1.0)

speed = 0

interval = 0.1 #Bunu manipüle edebilirsiniz, 1'i tam bölen bir sayı olsun yeter

while (speed < 1):
    rovpy.forward(speed)
    speed += interval

timer.start()
while timer:
    rovpy.forward(1)

while (speed >= 0):
    rovpy.forward(speed)
    speed -= interval
