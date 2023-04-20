from rovpy import rovpy
import time

#Kod süresince döndüğü açıyı ölçün

#Bu kodda sırasıyla rovpy. ların yanına pitch, roll, yawn, throttle yazıp test edin(ölçümleri yapın)



rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

timer=Boolean.timer(1.0)

speed = 0

interval = 0.1 #Bunu manipüle edebilirsiniz, 1'i tam bölen bir sayı olsun yeter

while (speed < 1):
    rovpy.pitch(speed)
    speed += interval

timer.start()
while timer:
    rovpy.pitch(1)

while (speed >= 0):
    rovpy.pitch(speed)
    speed -= interval