def wander():
    n=0
    while detectCircle == False:
        while n == 0:
            while detectWall == True:
                rov.rotate_cw()
            n=1
        while n==1:
            while detectWall==False:
                rov.move(-45,  speed):
            if detectWall == True:
                initial_position = current_location
            while detectWall == True:
                rov.move(-45, speed)
                    if touchingWall == True:
                        final_position = current_location
                        n=2
                    while touchingWall== True:
                        rov.rotate_ccw()
            r= dist(final_position-initial_position)
        if n==2:
            rov.move(-45, r)
            n=3
        while n==3:
            while detectWall == False:
                rov.move(45, speed):
            if detectWall == True:
                initial_position = current_location
            while detectWall == True:
                rov.move(45, speed)
                if touchingWall == True:
                    final_position = current_location
                    n = 2
                while touchingWall == True:
                    rov.rotate_ccw()
            r = dist(final_position - initial_position)
