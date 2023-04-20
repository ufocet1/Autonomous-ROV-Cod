from rovpy import rovpy
import time

#Dönüş hızı ölçüm testi
#Tam hız dönüşteki süresini ölçün
#Veya tüm hareketin süresi

#Bu kodda sırasıyla rovpy. ların yanına pitch, roll, yawn, throttle yazıp test edin(ölçümleri yapın)

rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

n= 100 #Ufak bir sayıdan başlatıp büyütün

speed = 0

interval = 0.1 #Bunu manipüle edebilirsiniz

rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

while (speed < 1):
    rovpy.pitch(speed)
    speed += interval

while n >= 0:
    rovpy.pitch(1)
    n -= 1


while (speed >= 0):
    rovpy.pitch(speed)
    speed -= interval