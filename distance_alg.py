import numpy as np

#Normalde bu velocity ve time listeleri pixhawk'tan alınacak
velocity=[0, 1, 4, 9, 16, 25]
time = [3, 4, 5, 6, 7, 8]


def distance(t_initial, t_final, delta):
    pos_t_initial = -1
    pos_t_final = -1
    for i in range (len(time) - 1) :
        if abs(time[i] - t_initial) < delta:
            pos_t_initial = i

    print(pos_t_initial)

    for i in range (len(time) - 1) :
        if abs(time[i] - t_final) < delta:
            pos_t_initial = i

    print(pos_t_final)

    velocity_boundary = []

    for i in range(pos_t_initial, pos_t_final):
        velocity_boundary.append(velocity[i])

    return np.trapz(velocity_boundary, None, 1)


print(distance(4, 5))
print(distance(5, 6))
print(distance(4, 6))