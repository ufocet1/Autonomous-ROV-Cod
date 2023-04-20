from rovpy import rovpy
import time

#Eğer ki sigorta atmışsa diye bi build-up denemesi


rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

timer=Boolean.timer(1.0)

speed = 0

interval = 0.1 #Bunu manipüle edebilirsiniz

while (speed < 1):
    rovpy.forward(speed)
    speed += interval

timer.start()
while timer:
    rovpy.forward(1)