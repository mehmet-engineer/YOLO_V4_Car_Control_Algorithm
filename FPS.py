import cv2
import time

def calculate_fps(previousTime):
    
    currentTime = time.time()
    try:
        fps = 1 / (currentTime - previousTime)
    except:
        pass
    
    fps = int(fps)
    previousTime = currentTime

    return (fps,previousTime)
    
def display_fps(img,fps,esik=20):

    if fps < esik:
        cv2.putText(img,"FPS: {}".format(str(fps)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    if fps >= esik:
        cv2.putText(img,"FPS: {}".format(str(fps)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)