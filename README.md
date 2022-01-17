# YOLO V4 Araç Kontrol Algoritması
May 2021 – Tem 2021

Trafik Koordinatörü sistemimizde geliştirdiğim yazılım parçasıdır. Python OpenCV araçları ve YOLO V4 Tiny Nesne Tespit Algoritması kullanarak yazmış olduğum yazılım,
yoldaki araçları algılayabilmekte ve sınıflandırabilmektedir. Buna bağlı olarak araç sayımı yapabilmektedir. Böylece bölgede trafik yoğunluğunun belirlenmesi 
ve denetlenmesi gerçekleştirilmektedir.

![resim](https://github.com/mehmet-engineer/YOLO_V4_Arac_Kontrol_Algoritmasi/blob/master/b2.png)

Video -> https://drive.google.com/file/d/1G6K9SgUoOB3I9zqJPsNp_BHZZqQMZxao/view

Bu uygulamada temeli Evrişimsel Sinir Ağlarına dayanan “YOLOv4-tiny” algoritması kullanılmıştır. Söz konusu algoritmanın düşük kayıp (loss) değerlerine sahip olması önemli bir avantajdır. Evrişimsel Sinir Ağları öğretilmek istenilen nesnenin resmine Konvolüsyon işlemi uygular, bu sayede nesnenin özniteliklerini çıkartır. Öznitelikler nesnelere has ve ayırt edici özelliklerdir. Bu sayede sistem, kendisine öğretilen nesneyi diğer nesnelerden ayırt ederek tespit işlemini gerçekleştirir. Araç kontrol algoritmasında nesne eğitimi için COCO veri seti kullanılmıştır. YOLOv4-tiny algoritması resimleri 416x416 piksel boyutunda kabul etmekte ve resimleri nxn gibi boyutlarda bölgelere bölmektedir. Her bölgeye, o bölgede nesne olup olmaması durumuna göre güven puanı belirler. Daha sonra nesnelerin güven puanının yüksek olduğu bölgelere evrişim işlemi uygulayarak nesneyi tespit etmiş olur.
Aşağıda bazı nesne tespit algoritmalarının doğruluk (accuracy) ve hız (fps) değerleri verilmiştir.

![resim](https://github.com/mehmet-engineer/YOLO_V4_Arac_Kontrol_Algoritmasi/blob/master/algorithms.jpg)
