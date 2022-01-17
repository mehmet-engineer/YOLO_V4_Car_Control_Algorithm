import cv2
import time

kamera = cv2.VideoCapture(0)

previous = 0
current = 0

while True:
    _,img = kamera.read()
    img = cv2.resize(img,(720,480))
    
    current = time.time()
    fps = 1 / (current-previous)
    previous = current

    fps = int(fps)
    
    if fps < 30:
        cv2.putText(img,"FPS: {}".format(str(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,[0,0,255],2)
    else:
        cv2.putText(img,"FPS: {}".format(str(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,[255,0,0],2)
    
    cv2.imshow("img",img)

    if cv2.waitKey(1) == 27:
        break

kamera.release()
cv2.destroyAllWindows()
