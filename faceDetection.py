import cv2
import numpy as np


faceCascade = cv2.CascadeClassifier("Ress/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(1)
# resized = cv2.resize(img,(400,700))

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img_gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("img",img)
    if cv2.waitKey(10) == ord('q'):
        break
