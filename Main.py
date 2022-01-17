import cv2, vehicle_detector


model = vehicle_detector.setup_model(accuracy_level=5)
cam = cv2.VideoCapture("a.mp4")

while True:
    _,img = cam.read()
    img = cv2.resize(img,(520,416))
    detected_boxes,detected_classes,detected_scores = vehicle_detector.detect_vehicles(img,model)
    vehicle_detector.display_vehicles(img,detected_boxes,detected_classes,detected_scores)

    cv2.imshow("detection",img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
