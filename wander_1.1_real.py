from rovpy import rovpy
import time
import numpy as np

#Yaw yaparken pozitif saat yönü mü tersi mi oluyo öğrenmem gerek deneyip
#Zaman nasıl alınacak bilmiyorum
#Rovinfo denenmeli
time_record = []
velocity_record = []

sleep_duration = 0.5
while True:
    time_record.append(time.time())
    velocity_record.append(rovpy.hiz())
    time.sleep(sleep_duration)

delta = sleep_duration

def wander_1_1_real():
    direction = "null"
    speed = 0.7
    while direction == "null":
        while detectWall == True:
            rovpy.yaw(0.5)
        if detectWall == False:
            direction = "right"
            origin_angle = rovpy.rovinfo()

    while direction == "right":
        while detectWall == False:
            #rov.move(-45, thrust, "force")
            rovpy.forward(speed)
            rovpy.lateral(speed)
        if detectWall == True and rovpy.hiz() != 0:
            t_initial = time.time()  # Current_time pixhawk'tan alınacak
        while detectWall == True and rovpy.hiz() != 0:  # Current_speed pixhawk'tan alınacak
            # rov.move(-45, thrust, "force")
            rovpy.forward(speed)
            rovpy.lateral(speed)
        if detectWall == True and rovpy.hiz() == 0:
            t_final = time.time()
            range_of_vision = distance(t_initial, t_final, delta)
            #rov.rotate(90)
            while rovpy.rovinfo() -origin_angle!= 90:#BURASI DEĞİŞTİRİLECEK YANİ belli bi yöne bakana kadar döncek olarak VEYA belli bi hızda belli bi süre boyunca
                rovpy.yaw(0.5)

            """t_new_initial = time.time()
            t_new_final = time.time()
            while distance(t_new_initial, t_new_final)!= range_of_vision:
                rovpy.forward(speed)
                rovpy.lateral(speed)  (BU DA KULLANILABİLİR DAHA BİLE KOLAY OLUR ASLINDA"""

            timer = Boolean.Timer(1.0)
            timer.start()
            while timer:
                rovpy.forward(speed)
                rovpy.lateral(speed)
                time.sleep(0.01)
                if not time:
                    break
                time.sleep(0.01)
            direction = "left"

    while direction == "left":
        while detectWall == False:
            #rov.move(45, thrust, "force")
            rovpy.forward(speed)
            rovpy.lateral(-speed)
        if detectWall == True:
            t_initial = rovpy.rovinfo()  # Current_time pixhawk'tan alınacak
        while detectWall == True and rovpy.hiz() != 0:  # Current_speed pixhawk'tan alınacak
            # rov.move(45, thrust, "force")
            rovpy.forward(speed)
            rovpy.lateral(speed)
        if detectWall == True and rovpy.hiz() == 0:
            t_final = rovpy.info()
            range_of_vision = distance(t_initial, t_final, delta)
            #rov.rotate(-90)
            while rovpy.rovinfo() - origin_angle != -90:#BURASI DEĞİŞTİRİLECEK YANİ belli bi yöne bakana kadar döncek olarak VEYA belli bi hızda belli bi süre boyunca
                rovpy.yaw(-0.5)
            a = 0
            timer = BoolTimer(1.0)
            timer.start()
            while timer:
                rovpy.forward(speed)
                rovpy.lateral(-speed)
                time.sleep(0.01)
                if not time:
                    break
                time.sleep(0.01)
            direction = "left"