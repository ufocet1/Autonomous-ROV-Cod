import subprocess
import re
import cv2

inc=0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(int(cap.get(cv2.CAP_PROP_BUFFERSIZE)))

print(f"Camera input width: {width}, height: {height}")

cap.set(cv2.CAP_PROP_BUFFERSIZE, 10)

ret, frame = cap.read()

qq = 1
while qq:
    try:
        if frame == None:
            print("a")
            ret, frame = cap.read()
    except:
        qq=0

frame = cv2.resize(frame, (800, 600))

cv2.imwrite("".join(["img",str(inc),".jpg"]), frame)

cap.release()

weights_path = "runs/train/exp14/weights/best.pt"
source = "".join(["img",str(inc),".jpg"])
view_img = True
max_det = 1
conf_thres = 0.6

command = ["python", "detect_rov.py", "--weights", weights_path, "--source", source, "--max-det", str(max_det), "--conf-thres", str(conf_thres), "--save-txt"]

if view_img:
    command.append("--view-img")

process = subprocess.Popen(command, stdout=subprocess.PIPE)

stdout, stderr = process.communicate()

finalstd = stdout.decode('utf-8')

valuesr = finalstd.split('\r\n')
valuesr = list(filter(None, valuesr))

values = []
for i in valuesr:
    values.append(int(float(i)))
    
print(values)

if len(values):
    box_x=int((values[0]+values[2])/2)
    box_y=int((values[1]+values[3])/2)

    print(box_x,box_y)
    
    #area = [[(500,300),(1420,300),(1920,300)],[(500,780),(1420,780),(1920,780)],[(500,1080),(1420,1080),(1920,1080)]]
    area_x = [150,650]
    area_y = [100,500]
    
    place_x = 0
    place_y = 0
    
    if box_x <= area_x[0]:
        place_x=1
    elif box_x <= area_x[1]:
        place_x=2
    else:
        place_x=3
    
    if box_y <= area_y[0]:
        place_y=0
    elif box_x <= area_x[1]:
        place_y=1
    else:
        place_y=2
        
    place = (3*place_y) + place_x
    
    print(place)


# olay su:
#
# robot objeyi gorene kadar wander yapacak
#
# ben kamerayi 9a boldum
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9
#
# Robotun sunu yapmasi lazim:
#
# 1, 4 veya 7de obje var iken sola donup objeyi 2, 5 veya 8e almasi lazim
# 3, 5 veya 9da obje var iken saga donup objeyi 2, 5 veya 8e almasi lazim
# 
# diyelim ki obje 2 veya 5te,
#   makinenin objeyi 8e alana kadar ilerlemesi lazim
#
# 8e gelince ise robot objeyi goremeyene kadar yavasca ileri gitmeli
# 
# artik obje gorunurde yoksa robot 90 derece saga veya sola donecek, objeyi algilayip algilamadigina bakacak
#   eger 2 veya 5te gorurse (cok dusuk ve sacma bir olasilik), yine 8e gecene kadar ilerlemeli
#   eger 8de gorurse yavasca ilerlemeli az once yaptigi gibi algilamayana kadar
#   eger gormuyorsa sikinti yok
#
#   artik gorunurde degilse inis yapacak




