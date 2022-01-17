import cv2

def observe_vehicles(detected_boxes,detected_classes):

    arac_durum = False
    arac_tipi = ""

    for i in range(len(detected_boxes)):
        x, y, w, h = detected_boxes[i]
        center = (int(x+w/2),int(y+h/2))
        #cv2.circle(img,center,2,[0,0,255],-1)

        # center[1] yani y degeri 320 civari hizada olursa;
        esik = 5
        if center[1] > 320-esik and center[1] < 320+esik:
            arac_durum = True
            arac_tipi = "araba"    #gecici

            #if detected_classes[i] == 3:
            #    arac_tipi = "araba"
            #elif detected_classes[i] == 6 or detected_classes[i] == 8:
            #    arac_tipi = "agir"
            #else:
            #    arac_tipi = "diger"

    return (arac_durum,arac_tipi)

def display_vehicle_count(img,arac_sayaci,arac_durum,arac_tipi):

    cv2.rectangle(img,(320,30),(320+150,30+70),[240,240,240],-1)

    if arac_durum == False:
        cv2.line(img,(40,320),(480,320),[0,0,150],2)
        cv2.putText(img,"Araba:"+str(arac_sayaci[0]),(330,50),cv2.FONT_HERSHEY_SIMPLEX,0.6,[0,0,0],1)
        cv2.putText(img,"Agir Arac:"+str(arac_sayaci[1]),(330,80),cv2.FONT_HERSHEY_SIMPLEX,0.6,[0,0,0],1)

    if arac_durum == True:
        cv2.line(img,(40,320),(480,320),[0,0,255],3)

        if arac_tipi == "araba":
            arac_sayaci[0] = arac_sayaci[0] + 1
            cv2.putText(img,"Araba:"+str(arac_sayaci[0]),(330,50),cv2.FONT_HERSHEY_SIMPLEX,0.6,[0,0,0],1)
        elif arac_tipi == "agir":
            arac_sayaci[1] = arac_sayaci[1] + 1
            cv2.putText(img,"Agir Arac:"+str(arac_sayaci[1]),(330,80),cv2.FONT_HERSHEY_SIMPLEX,0.6,[0,0,0],1)
        else: # arac tipi --> diger
            arac_sayaci[1] = arac_sayaci[1] + 1
            cv2.putText(img,"Agir Arac:"+str(arac_sayaci[1]),(330,80),cv2.FONT_HERSHEY_SIMPLEX,0.6,[0,0,0],1)

    return arac_sayaci
    

    

    