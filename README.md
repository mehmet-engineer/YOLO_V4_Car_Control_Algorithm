# Vehicle Control Algorithm with YOLO V4
May 2021 – Jul 2021

Traffic Coordinator is the piece of software I developed in our system. The software I wrote using Python OpenCV tools and YOLO V4 Tiny Object Detection Algorithm can detect and classify vehicles on the road. Accordingly, it can count vehicles. Thus, the traffic density in the region is determined and controlled.

![resim](https://github.com/mehmet-engineer/YOLO_V4_Car_Control_Algorithm/blob/master/b2.png)

Video -> https://drive.google.com/file/d/1G6K9SgUoOB3I9zqJPsNp_BHZZqQMZxao/view

In this application, the “YOLOv4-tiny” algorithm based on Convolutional Neural Networks is used. It is an important advantage that the algorithm in question has low loss values. Convolutional Neural Networks apply Convolution operation to the picture of the object to be taught, thus extracting the attributes of the object. Attributes are unique and distinctive features of objects. In this way, the system performs the detection process by distinguishing the taught object from other objects. COCO dataset is used for object training in vehicle control algorithm. The YOLOv4-tiny algorithm accepts images as 416x416 pixels and divides the images into regions with sizes such as nxn. It determines a trust score for each region according to whether there is an object in that region or not. Then, it detects the object by applying the convolution process to the regions with high confidence scores.
Accuracy and speed (fps) values ​​of some object detection algorithms are given below.

![resim](https://github.com/mehmet-engineer/YOLO_V4_Car_Control_Algorithm/blob/master/algorithms.jpg)
