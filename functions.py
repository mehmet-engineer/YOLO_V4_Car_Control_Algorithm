from dronekit import Battery, connect, VehicleMode
from pymavlink import mavutil
import time

def condition_yaw(drone, angle, velocity, direction):
    is_relative=0 #yaw is an absolute angle (False)
    if direction == "cw":
        direction = 1
    else:
        direction = -1
    # create the CONDITION_YAW command using command_long_encode()
    msg = drone.message_factory.command_long_encode(
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0, #confirmation
        angle,    # param 1, yaw in degrees
        velocity,     # param 2, yaw speed deg/s
        direction,      # param 3, direction -1 ccw, 1 cw
        is_relative, # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    drone.send_mavlink(msg)

def ARM_OL(drone):
    print("Arm izini: ", drone.is_armable)
    print("Guncel Mod: ", drone.mode.name)

    while True:
        print("Otonom baslatma komutu bekleniyor...")
        if drone.mode.name == "GUIDED":
            print("GUIDED moda gecildi.")
            break
        time.sleep(0.8)
    
    drone.armed = True
    while drone.armed == False:
        print("Drone ARM ediliyor...")
        time.sleep(0.8)
    print("Drone ARM edildi.")

def take_off(drone,irtifa=10):
    while drone.armed != True:
        print("ARM bekleniyor...")
        time.sleep(0.8)
    
    print("Kalkis yapiliyor...")
    drone.simple_takeoff(irtifa)

    sayac = 0
    while True:
        try:
            print("Irtifa: {} metre".format(str(round(drone.location.global_relative_frame.alt,2))))
        except:
            print("beklenmeyen deger")

        sayac = sayac + 1
        time.sleep(1)

        if round(drone.location.global_relative_frame.alt) == irtifa:
            print("hedef irtifaya ulasildi")
            break
        if sayac == 12:
            print("hedef irtifaya ulasilmadan donguden cikildi")
            break


def goto_position_target_local_ned(drone, north, east, down):
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        north, east, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    drone.send_mavlink(msg)

def goto_position_target_global_body(drone, x, y, z):
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, # frame
        0b0000011111000111, # type_mask (only positions enabled)
        0, 0, 0,
        x, y, z, # x, y, z velocity in m/s  
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    drone.send_mavlink(msg)

def Yolu_Ortala(drone,sag_metre):
    kuzey = drone.location.local_frame.north
    irtifa = drone.location.local_frame.down
    condition_yaw(drone, angle=90, velocity=30, direction="cw")
    print("Yol ortalaniyor...")
    time.sleep(3)
    goto_position_target_local_ned(drone, kuzey, sag_metre, irtifa)

    sayac = 0
    while True:
        print("yol ortalama --> {} metre".format(str(round(drone.location.local_frame.east,2))))
        time.sleep(1)
        sayac = sayac + 1
        if round(drone.location.local_frame.east) == sag_metre:
            print("hedef yol ortalamaya ulasildi")
            break
        if sayac == sag_metre+5:
            break

    condition_yaw(drone, angle=0, velocity=30, direction="ccw")
    time.sleep(3)

def Yolu_Ortala_Global(drone,sag_metre):
    #condition_yaw(drone, angle=90, velocity=30, direction="cw")
    print("Yol ortalaniyor...")
    #time.sleep(3)

    for i in range(sag_metre):
        goto_position_target_global_body(drone, 0, 1, 0)
        time.sleep(1)
        print("{} metre yol ortalandi".format(str(i+1)))
    
    goto_position_target_global_body(drone,0,0,0)

    condition_yaw(drone, angle=0, velocity=30, direction="ccw")
    time.sleep(3)

def Ilerle(drone,hiz):

    velocity_y = velocity_z = 0
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        hiz, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 
    
    drone.send_mavlink(msg)

def Ilerle_Global(drone,hiz):

    velocity_y = velocity_z = 0
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        hiz, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 
    
    drone.send_mavlink(msg)

def Yol_kenari(drone,sol_metre):
    print("Yol kenarina geciliyor...")
    kuzey = drone.location.local_frame.north
    irtifa = drone.location.local_frame.down
    dogu = round(drone.location.local_frame.east)

    #condition_yaw(drone, angle=270, velocity=30, direction="ccw")
    time.sleep(3)
    goto_position_target_local_ned(drone,kuzey,dogu-sol_metre,irtifa)

    sayac = 0
    while True:
        print(round(drone.location.local_frame.east,2))
        time.sleep(1)
        sayac = sayac + 1

        if round(drone.location.local_frame.east) == dogu-sol_metre:
            print("hedef yol ortalamaya ulasildi")
            break

        if sayac == sol_metre+5:
            print("hedef yol ortalamaya ulasilmadan donguden cikildi")
            break

def Yol_kenari_Global(drone,sol_metre):
    print("Yol kenarina geciliyor...")
    
    for i in range(sol_metre):
        goto_position_target_global_body(drone, 0, -1, 0)
        time.sleep(1)
        print("{} metre yol ortalandi".format(str(i+1)))
    
    goto_position_target_global_body(drone,0,0,0)


def LAND(drone):
    time.sleep(1)
    print("LAND Moda geciliyor...")
    drone.mode = VehicleMode("LAND")
    time.sleep(2)
        
    while drone.mode.name != "LAND":
        print("LAND moduna geciliyor...")
        time.sleep(1)

    while True:
        try:
            print("Irtifa: {} metre".format(str(round(drone.location.global_relative_frame.alt,2))))
        except:
            print("beklenmeyen deger")
        
        time.sleep(1)

        if round(drone.location.global_relative_frame.alt,2) <= 0.3:
            print("basariyla inis yapildi...")
            break

    while True:
        print("DISARM ediliyor...")
        time.sleep(1)

        if drone.armed == False:
            break
    
    print("Inis yapildi")
    print("BASARILI ...")
