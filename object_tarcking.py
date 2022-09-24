# Kütüphanlerin yüklenmesi ve kullanılması
from statistics import median
import cv2
from matplotlib.backend_bases import FigureManagerBase
from tblib import Frame
import numpy as np
cap=cv2.imread(herhangigörsel.jpg')
# Görsel inputu verilmesi
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgmask = fgbg.apply(cap)
# Görseli mask almak
# Videodaki hareketli objenin mask oluşturulması
cv2.imshow('frame',fgmask)
# Kod:
from statistics import median
import cv2
from matplotlib.backend_bases import FigureManagerBase
from tblib import Frame
cap = cv2.VideoCapture('herhangivideo.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
# Videoyu okuyup blur hale getirelim. Bu durum track daha stail çalışmasını 
sağlaycaktır
while(1):
ret, frame = cap.read()
fgmask = fgbg.apply(frame)
median = cv2.medianBlur(fgmask,3)
(contours,hierarchy) = cv2.findContours(median.copy(), 
cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
if cv2.contourArea(c) < 1000:
continue
(x,y,w,h)=cv2.boundingRect(c)
cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
# Arka planda gerçekleşen hareketli objenin algılanması
background=cv2.resize(median,(1000,800))
frame1 = cv2.resize(frame,(1000,800))
cv2.imshow('background',background)
cv2.imshow('frame',frame1)
k=cv2.waitKey(1) & 0xff
if k==120:
break
cap.release()
cv2.destroyAllWindows()
