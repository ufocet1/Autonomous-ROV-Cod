from rovpy import rovpy
import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = cv2.VideoCapture(1)


#bir daire tespit edilip edilmediğini gösteriyor
wasDetected = False

#daire tespit edildiğinde değeri True yapıyor, bu sonradan işimize yarayacak
if detectCircle == True:
    wasDetected = True

#daire gözükürken robot hareket edecek
while detectCircle == True:
    rov.forward(0.4)

while detectCircle == False:
    while wasDetected == False:
        rov.wander()
    while wasDetected == True:
        rov.forward(0)
        rov.lateral(-0.5)



#bir daire görürken dairenin önce merkezinin konumunu bulacak, dairenin merkezinin konumunun kameranın aldığı görüntünün
# ortasının konumuna göre sağa veya sola hareket edecek, ayrıca uzaklığına bağlı olarak ileri hareket edecek
#daire görüntüden çıktığında robotun altında kalmış olacağından robot duracak, aşağı doğru inecek

#bu wander methodu tanımlanacak, robotun konumuna ve rotasyonuna göre robotun havuzun her tarafını tarayacak şekilde bir rota 
#düzenleyecek, bu rotayı takip ederken görmeye çalışacak
