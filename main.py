import cv2 #opencv kutuphanesi
import numpy as np

kamera = cv2.VideoCapture(0,cv2.CAP_DSHOW) #bu bilgisayar kamerasını kullanmak için "0" değerini veriyoruz.

while True:
    ret, kare = kamera.read()#kameranın çalışıp çalışmadığını kontrol ediyor.
    gri_nesne = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY) #nesneyi kolay algılaması  için gri renge cevırıyoruz.
    nesne = cv2.imread("telefon.jpg",1)
    #w = int(nesne.get(cv2.CAP_PROP_FRAME_WIDTH))
    #h = int(nesne.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w,h = nesne.shape
    res = cv2.matchTemplate(gri_nesne,nesne,cv2.TM_CCOEFF_NORMED)  #bu kamera taramasının yapıldıgı kısım
    #sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # Bulunan Objenin Koordinatlarini Bul
    #Ust_Sol = max_loc  # Bulunan Objenin Ust ve Sol Uzakligi
    #Alt_Sag = (Ust_Sol[0] + 50, Ust_Sol[1] + 50)
    esik_degeri = 0.8 #bu eşik degerini iyi ayarlamak gerek oda oluşturduğumuz .jpeg dosyasının boyutlarına göre deneyerek buluyoruz.
    loc = np.where(res > esik_degeri)
    for n in zip(*loc[::-1]):
        cv2.rectangle(kare, n, (n[0] + h, n[1] + w), (0, 255, 0),2)  # burada bulduğu nesneyi dikdörtgen içine alıyor.
    #cv2.rectangle(kare, Ust_Sol, Alt_Sag, (0, 255, 0), 2)
    cv2.imshow("screen", kare)# kamera açılır video şeklinde

    if cv2.waitKey(30) & 0xFF == ord("e"): #kamerayı durdurmak için ya da programdan çıkmak için
        break

kamera.release()
cv2.destroyAllWindow()

