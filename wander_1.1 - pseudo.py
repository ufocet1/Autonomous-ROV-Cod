"""Bu wander kodu "detectCircle == false" durumunda çalışıyor olacak, kendi içerisine eklemiyorum"""
"""BULUNACAK: rov.move(a,b,c ), robotun düz yönünden a derecede ; c "force" ise b gücüyle itki, "distance" ise b mesafe ;  gidecek"""
"""TANIMLANACAK: distance(a,b) t=a ile t=b arasında hızın integralini alacak"""
"""BULUNACAK: rotate(a) a derece döndürecek, 90 ise ccw dönüp sola, -90 ise cw dönüp sağa vs."""
def wander_1_1():
    direction = "right" #Robot o esnada hangi yöne gidecekse
    thrust = 10  #BUNU DEĞİŞTİRİN HIZA GÖRE

    #Sağa doğru hareket ettiği kod
    while direction == "right":
        while detectWall == False:
            rov.move(-45, thrust, "force")
        if detectWall == True:
            t_initial = current_time #Current_time pixhawk'tan alınacak
        while detectWall == True and current_speed != 0: #Current_speed pixhawk'tan alınacak
            rov.move(-45,thrust, "force")
        if detectWall == True and current_speed == 0:
            t_final = current_time
            range_of_vision = distance(t_initial, t_final)
            rov.rotate(90)
            rov.move(-45, range_of_vision, "distance")
            direction = "left"

    #Sola doğru hareket ettiği kod
    while direction == "left":
        while detectWall == False:
            rov.move(45, thrust, "force")
        if detectWall == True:
            t_initial = current_time  # Current_time pixhawk'tan alınacak
        while detectWall == True and current_speed != 0:  # Current_speed pixhawk'tan alınacak
            rov.move(45, thrust, "force")
        if detectWall == True and current_speed == 0:
            t_final = current_time
            range_of_vision = distance(t_initial, t_final)
            rov.rotate(-90)
            rov.move(45, range_of_vision, "force")
            direction = "right"



