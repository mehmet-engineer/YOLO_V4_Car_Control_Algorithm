import cv2, time, os, argparse
"""from dronekit import Battery, connect, VehicleMode
#from pymavlink import mavutil
#import dronekit"""
import functions, jetson, FPS, vehicle_detector, vehicle_counter, line_detector, line_controller
import my_mail, mission_timer, raporlayici

"""
# IHA ile baglanti kur
print("Baglanti kuruluyor...")
drone = connect("/dev/serial0",baud=57600,wait_ready=True)
print("Baglanti saglandi, mavlink protokolu hazir.")

# ARM ol, hazirlan ve komut bekle
functions.ARM_OL(drone)

# 10 metre irtifaya ulas
functions.take_off(drone,irtifa=10)

# Yolu ortala
functions.Yolu_Ortala(drone)

# Kamera ile baglanti kur
cam = jetson.cam_launching()
"""

# FPS tanimlarini yap
previousTime = 0
currentTime = 0

# Gorev sayaci tanimlarini yap
previous = 0
current = 0
toplam_sure = 0
saniye_sayaci = 0

# Raporlayiciyi hazirla
dosya_1 = open("raporlar\\rapor.txt", "w")
dosya_2 = open("ihlal_fotolar\\ihlaller.txt", "w")

# Yapay zeka modelini kur
arac_sayaci = [0,0]
model = vehicle_detector.setup_model(accuracy_level=1)

cam = cv2.VideoCapture("a.mp4")   #denemeler için geçici

"""
#Video Kayit
format = cv2.VideoWriter_fourcc(*"MJPG")
kayit = cv2.VideoWriter("video_kayit\\my_video.avi",format, 9, (640,480))
"""

# Tespit dongusu
print("Tespit dongusune giriliyor...")
while True:
    red,img = cam.read()
    if red == True:
        
        img = cv2.resize(img,(520,416))

        # Araclari tespit et
        detected_boxes,detected_classes,detected_scores = vehicle_detector.detect_vehicles(img,model)

        # Seritleri tespit et
        lines = line_detector.detect_lines(img)

        # Serit ihlallerini denetle
        main_left_line,main_right_line = line_controller.process(img,lines)
        line_controller.compare_line_cars(img,cam,detected_boxes,main_left_line,main_right_line,dosya_2)

        # Araclari goster
        vehicle_detector.display_vehicles(img,detected_boxes,detected_classes,detected_scores)

        # Arac sayimini denetle
        arac_durum,arac_tipi = vehicle_counter.observe_vehicles(detected_boxes,detected_classes)
        arac_sayaci = vehicle_counter.display_vehicle_count(img,arac_sayaci,arac_durum,arac_tipi)

        # FPS hesapla
        fps,previousTime = FPS.calculate_fps(previousTime)
        FPS.display_fps(img,fps,esik=10)

        # Gorev suresini say
        durum,saniye_sayaci,toplam_sure,previous = mission_timer.gorev_hesapla(saniye_sayaci,toplam_sure,previous)
        
        # Ilerle 
        if durum == True:
            #functions.Ilerle(drone,hiz=1)
            pass
        if saniye_sayaci == 20:
            print("Gorev dongusu tamamlandi.")
            break

        #kayit.write(img)

    cv2.imshow("Detection", img)
    if cv2.waitKey(1) == 27:
        break

#kayit.release()
cam.release()
cv2.destroyAllWindows()

# Verileri Raporla
raporlayici.report(dosya_1,dosya_2,arac_sayaci)

# Yol kenarina git
#functions.Yol_kenari(drone)

# Inis yap
#functions.LAND(drone)

# Dronu kapat
#drone.close()