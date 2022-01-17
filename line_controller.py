import cv2, math, random, datetime
import my_mail

def process(img,lines):

    img_width = img.shape[1]

    left_lines = []
    right_lines = []
    lengths_left = []
    lengths_right = []
    main_left_line = 0
    main_right_line = 0

    if lines is not None:
        for line in lines:  
            for x1,y1,x2,y2 in line:
                X = (x1+x2)/2

                if X < img_width/2:
                    length = math.sqrt((y2-y1) ** 2 + (x2-x1) ** 2)
                    left_lines.append((length,x1,y1,x2,y2))
                else:
                    length = math.sqrt((y2-y1) ** 2 + (x2-x1) ** 2)
                    right_lines.append((length,x1,y1,x2,y2))
    
    for line in left_lines:
        lengths_left.append(line[0])

    for line in right_lines:
        lengths_right.append(line[0])

    if len(lengths_left) != 0:
        main_left_line_idx = lengths_left.index(max(lengths_left))
        _,l_x1,l_y1,l_x2,l_y2 = left_lines[main_left_line_idx]
        cv2.line(img,(l_x1,l_y1),(l_x2,l_y2),[0,127,255],3)
        main_left_line = (l_x1,l_y1,l_x2,l_y2)
    if len(lengths_right) != 0:
        main_right_line_idx = lengths_right.index(max(lengths_right))
        _,r_x1,r_y1,r_x2,r_y2 = right_lines[main_right_line_idx]
        cv2.line(img,(r_x1,r_y1),(r_x2,r_y2),[0,127,255],3)
        main_right_line = (r_x1,r_y1,r_x2,r_y2)

    return (main_left_line,main_right_line)


def compare_line_cars(img,cam,detected_boxes,main_left_line,main_right_line,dosya_2):

    img_width = img.shape[1]
    if main_left_line != 0:
        l_x1,l_y1,l_x2,l_y2 = main_left_line
    if main_right_line != 0:
        r_x1,r_y1,r_x2,r_y2 = main_right_line

    for i in range(len(detected_boxes)):
        x, y, w, h = detected_boxes[i]
        center = (int(x+w/2),int(y+h/2))  #center
        cv2.circle(img,center,4,[0,0,250],-1)
        x3 = center[0]
        y3 = y4 = center[1]

        if x3 < img_width/2:  #soldaki araclar
            if main_left_line == 0:
                continue
            x4 = int(l_x2 - ((l_y2-y4)*(l_x2-l_x1))/(l_y2-l_y1))
            
            if x4 > x3: # ihlal var demektir ----------------------------------------------
                cv2.line(img,(x4,y4),(x3,y3),[0,0,250],1)
                print("Ihlal tespit edildi.")
                _,new_img = cam.read()
                new_img_h = new_img.shape[0]
                new_img_w = new_img.shape[1]
                img_h = img.shape[0]
                img_w = img.shape[1]
                
                oran_h = new_img_h / img_h
                oran_w = new_img_w / img_w

                esik_1 = 10
                esik_2 = 30
                a = int(x*oran_w) - esik_1
                b = int(y*oran_h) - esik_1
                c = int(a+w*oran_w) + esik_2
                d = int(b+h*oran_h) + esik_2

                cv2.rectangle(new_img,(a,b),(c,d),[0,0,255],2)
    
                sayi = random.randint(0,10000)
                filename = "ihlal_tespit_{}.jpg".format(sayi)
                cv2.imwrite("ihlal_fotolar/" + filename,new_img)
                #my_mail.tespit_mail(filename)

                zaman = datetime.datetime.now()
                saat = zaman.hour
                dk = zaman.minute
                sn = zaman.second
                if saat < 10:
                    hour = "0" + str(saat)
                else:
                    hour = saat
                if dk < 10:
                    minute = "0" + str(dk)
                else:
                    minute = dk
                if sn < 10:
                    second = "0" + str(dk)
                else:
                    second = sn
                string = "Saat {}:{}:{} --> ihlal_fotolar/".format(hour,minute,second) + filename + "\n"
                dosya_2.writelines(string)
            
            else: # -----------------------------------------------------------------------
                cv2.line(img,(x4,y4),(x3,y3),[250,250,250],1)

            cv2.circle(img,(x4,y4),4,[0,0,250],-1)
    
        else:   #sagdaki araclar
            if main_right_line == 0:
                continue
            x4 = int(r_x2 - ((r_y2-y4)*(r_x2-r_x1))/(r_y2-r_y1))

            if x3 > x4: # ihlal var demektir ----------------------------------------------
                print("Ihlal tespit edildi.")
                cv2.line(img,(x4,y4),(x3,y3),[0,0,250],1)
                _,new_img = cam.read()
                new_img_h = new_img.shape[0]
                new_img_w = new_img.shape[1]
                img_h = img.shape[0]
                img_w = img.shape[1]
                
                oran_h = new_img_h / img_h
                oran_w = new_img_w / img_w

                esik_1 = 10
                esik_2 = 30
                a = int(x*oran_w) - esik_1
                b = int(y*oran_h) - esik_1
                c = int(a+w*oran_w) + esik_2
                d = int(b+h*oran_h) + esik_2

                cv2.rectangle(new_img,(a,b),(c,d),[0,0,255],2)
    
                sayi = random.randint(0,10000)
                filename = "ihlal_tespit_{}.jpg".format(sayi)
                cv2.imwrite("ihlal_fotolar/" + filename,new_img)
                #my_mail.tespit_mail(filename)

                zaman = datetime.datetime.now()
                saat = zaman.hour
                dk = zaman.minute
                sn = zaman.second
                if saat < 10:
                    hour = "0" + str(saat)
                else:
                    hour = saat
                if dk < 10:
                    minute = "0" + str(dk)
                else:
                    minute = dk
                if sn < 10:
                    second = "0" + str(dk)
                else:
                    second = sn
                string = "Saat {}:{}:{} --> ihlal_fotolar/".format(hour,minute,second) + filename + "\n"
                dosya_2.writelines(string)
            
            else: # -----------------------------------------------------------------------
                cv2.line(img,(x4,y4),(x3,y3),[250,250,250],2)

            cv2.circle(img,(x4,y4),4,[0,0,250],-1)

    

    

