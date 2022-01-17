import cv2

def setup_model(accuracy_level):
    net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
    model = cv2.dnn_DetectionModel(net)

    # 256 - 288 - 320 - 416,256 - 416 - 512 - 608 - 640 - 832
    if accuracy_level == 9:
        model.setInputParams(size=(832,832), scale=1/255)    # 2 FPS on PC
    elif accuracy_level == 8:
        model.setInputParams(size=(640,640), scale=1/255)    # 3 FPS on PC
    elif accuracy_level == 7:
        model.setInputParams(size=(608,608), scale=1/255)    # 4 FPS on PC
    elif accuracy_level == 6:
        model.setInputParams(size=(512,512), scale=1/255)    # 6 FPS on PC
    elif accuracy_level == 5:
        model.setInputParams(size=(416,416), scale=1/255)    # 8 FPS on PC
    elif accuracy_level == 4:
        model.setInputParams(size=(416,256), scale=1/255)    # 12 FPS on PC
    elif accuracy_level == 3:
        model.setInputParams(size=(320,320), scale=1/255)    # 12 FPS on PC
    elif accuracy_level == 2:
        model.setInputParams(size=(288,288), scale=1/255)    # 15 FPS on PC
    elif accuracy_level == 1:
        model.setInputParams(size=(256,256), scale=1/255)    # 19 FPS on PC
    else:
        model.setInputParams(size=(416,416), scale=1/255)

    """ CLASSES;
    3: 'car'
    6: 'bus'
    8: 'truck'
    """
    return model

def detect_vehicles(img,model):

    detected_boxes = []
    detected_classes = []
    detected_scores = []

    class_ids, scores, boxes = model.detect(img, nmsThreshold=0.4)
    for class_id, score, box in zip(class_ids, scores, boxes):
        #if score < 0.1:
        #    continue

        alan = box[2] * box[3]
        if alan > 12000:
            continue

        detected_boxes.append(box)
        detected_classes.append(int(class_id)+1)
        detected_scores.append(score)

    return (detected_boxes,detected_classes,detected_scores)

def display_vehicles(img,detected_boxes,detected_classes,detected_scores):

    for i in range(len(detected_boxes)):
        x, y, w, h = detected_boxes[i]
        skor = str(detected_scores[i])
        skor = int(float(skor[1:5])*100)
        if detected_classes[i] == 3:
            cv2.rectangle(img, (x, y), (x+w, y+h), [255, 0, 0], 2)
            cv2.putText(img, "Araba" + " %" + str(skor), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 0, 0], 2)
        elif detected_classes[i] == 6 or detected_classes[i] == 8:
            cv2.rectangle(img, (x, y), (x+w, y+h), [0, 255, 0], 2)
            cv2.putText(img, "Agir Arac" + " %" + str(skor), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [0, 255, 0], 2)
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), [0, 255, 0], 2)
            cv2.putText(img, "Diger" + " %" + str(skor), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 2)

        




