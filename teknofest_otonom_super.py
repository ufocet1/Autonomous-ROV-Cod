import time
from pymavlink import mavutil
import cv2
import random

cam = cv2.VideoCapture(0)
cnt = 1

try:
    master = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)
except:
    master = mavutil.mavlink_connection("/dev/ttyACM1", baud=115200)

boot_time = time.time()
mode = "MANUAL"

mode_id = master.mode_mapping()[mode]
master.mav.set_mode_send(master.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)

master.wait_heartbeat()

master.mav.request_data_stream_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_POSITION,
    1, # Hz
    1 # Start sending
)

print("1")

def det():
    colorLower = (100, 100, 100) 
    colorUpper = (120, 255, 255)
    #converter.py ile convert ettiğiniz rengi buraya giriniz
    while True: #yazılımımız çalıştığı sürece aşağıdaki işlemleri tekrarla

        
        (grabbed, frame) = cap.read() # grabbed ve frame değişkenini camera.read olarak tanımlıyoruz.

        frame = imutils.resize(frame, width=600) # görüntü genişliğini 600p yapıyoruz
        frame = imutils.rotate(frame, angle=180) # görüntüyü 180 derece döndürüyoruz

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # görüntüyü hsv formatına çeviriyoruz
    
        
        mask = cv2.inRange(hsv, colorLower, colorUpper) # hsv formatına dönen görüntünün bizim belirttiğimiz renk sınırları içerisinde olanları belirliyor
        mask = cv2.erode(mask, None, iterations=2) # bizim renklerimizi işaretliyor
        mask = cv2.dilate(mask, None, iterations=2) # bizim renklerimizin genişliğini alıyor
        
        
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None


        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            if radius > 10: #algılanacak hedefin minumum boyutu,
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

            print("x : ")
            print(x) # kameradan gelen görüntüde bizim rengimiz varsa x kordinatı
            print("y : ")
            print(y) # kameradan gelen görüntüde bizim rengimiz varsa y kordinatı
            print()
        
        else:
            print("no")

def capt():
    global cnt
    result, image = cam.read()
    if result:
        cv2.imwrite("real_1_"+str(cnt)+".png", image)
        cnt += 1
        print("nice")

def getvel():
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)

    vx = msg.vx / 100.0  # m/s
    vy = msg.vy / 100.0  # m/s
    vz = msg.vz / 100.0  # m/s
    
    # Print the velocity data
    print(f"Velocity: ({vx}, {vy}, {vz}) m/s")

failsafe = True

if failsafe:
    failsafe_params = {
    'FS_GCS_ENABLE': 0,
    'FS_EKF_THRESH': 0,
    #'FS_BATT_ENABLE': 0,
    #'FS_THR_ENABLE': 0,
    #'FS_GPS_ENABLE': 0,
    #'FS_GCS_FAIL': 0,
    #'FS_EKF_FAIL': 0,
    #'FS_BATT_VOLTAGE': 0,
    #'FS_BATT_MAH': 0,
    #'FS_BATT_CURR': 0,
    #'FS_BATT_TIME': 0,
    #'FS_GCS_SIGNAL': 0,
    #'FS_PID_ENABLE': 0,
    'FS_CRASH_CHECK': 0,
    #'FS_CRASH_TIME': 0,
    #'FS_FWDDIR_ENABLE': 0,
    }

    qqq=0

    for param_id, param_value in failsafe_params.items():
        if qqq:
            qqq=0
            break
        master.mav.param_set_send(
            master.target_system, master.target_component,
            param_id.encode('utf-8'), param_value,
            mavutil.mavlink.MAV_PARAM_TYPE_INT32)
        print(5)
        # Wait for parameter to be set
        start_time = time.time()
        while True:
            
            msg = master.recv_match(type='PARAM_VALUE', blocking=True)
            print(msg.get_type(),msg.param_id,param_id.encode('utf-8'))
            if msg.get_type() == 'PARAM_VALUE':
                if msg.param_value == param_value:
                    print(f"{param_id} set to {param_value}")
                    print("2")
                    break
                else:
                    print(":(")
            else:
                print(":( 2")

            # Timeout after 5 seconds
            if time.time() - start_time > 5:
                print("Timed out waiting for parameter set")
                qqq=1
                break
            
            time.sleep(0.1)

    print("3")


#master.reboot_autopilot()

master.arducopter_arm()

vx = 1  # 1 m/s forward speed

# Send the SET_POSITION_TARGET_LOCAL_NED message to move the ROV forward
print("input lol")

if True:

    getvel()


    #master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, z, 1500, x, r, 1500, y)
    #X: 1000-1500 ileri, 1500-2000 geri
    #Y: 1000-1500 sol, 1500-2000 sag
    #Z: 1000-1500 asagi, 1500-2000 yukari
    #R: 1000-1500 sag, 1500-2000 sol

    #ileri:

    master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1000, 1500, 1500, 1500)
    time.sleep(random.randint(1,6))
    master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
    time.sleep(2)

    for i1 in range(random.randint(4,12)):
        
        a = random.randint(1,5)

        if a == 1:

            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1400, 1500, 1500)
            time.sleep(random.randint(2,4))
            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)

        elif a == 2:

            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1200, 1500, 1500, 1500)
            time.sleep(random.randint(2,4))
            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
        
        elif a == 3:

            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1300)
            time.sleep(random.randint(2,4))
            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)  

        elif a == 4:

            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1600, 1500, 1500, 1500)
            time.sleep(random.randint(2,5))
            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
        
        elif a == 5:

            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1600, 1500, 1500)
            time.sleep(random.randint(2,5))
            master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)

        master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1600, 1500, 1500, 1500, 1500, 1500)
        time.sleep(2)
        master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)

    master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1000, 1500, 1500, 1500, 1500, 1500)
    time.sleep(20)
    master.mav.rc_channels_override_send(master.target_system, master.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)

master.arducopter_disarm()
master.motors_disarmed_wait()
print("DONE")