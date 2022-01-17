import cv2
import numpy as np 

kamera = cv2.VideoCapture(1)

cam_width = kamera.get(3)   #640
cam_boy = kamera.get(4)     #480
cam_fps = kamera.get(5)     #30 FPS

#video formatını ayarlama --> *"MJPG" = mp4, *"DIVX" = avi, *"X264" = mkv
format = cv2.VideoWriter_fourcc(*"MJPG")
kayit = cv2.VideoWriter("my_video.avi",format, 15, (640,480) )

counter = 0
while True:
    red,kare = kamera.read()    
    cv2.imshow("Kamera",kare)

    kayit.write(kare)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

    counter = counter + 1

    if counter == 108000:
        break

kayit.release()
kamera.release()
cv2.destroyAllWindows()