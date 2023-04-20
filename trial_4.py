from rovpy import rovpy
import time

#Her bir kod ne kadar sürüyor diye örneğin rovpy.forward yaptım kaç saniye boyunca bu tek satır çalışıyor
#Tam hızda gittiği süreyi ölçün
#Onu yapamıyorsanız tümden gittiği süreyi ölçün


n= 100 #Ufak bir sayıdan başlatıp büyütün

speed = 0

interval = 0.1 #Bunu manipüle edebilirsiniz

rovpy.connectrov("STABILIZE","/dev/ttyACM0")  #connectrov(mode,port or udp url) düzenleyin bunu

rovpy.arm()

while (speed < 1):
    rovpy.forward(speed)
    speed += interval

while n >= 0:
    rovpy.forward(1)
    n -= 1


while (speed >= 0):
    rovpy.forward(speed)
    speed -= interval
