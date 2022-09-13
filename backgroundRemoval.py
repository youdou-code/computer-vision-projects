
import cv2
import numpy as np
import cvzone
import mediapipe as mp
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation()
img = cv2.imread("images/bg.jpg")
img_resized = cv2.resize(img, (640,480))
fps = cvzone.FPS()
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    output_frame = segmentor.removeBG(frame,img_resized,threshold=0.85)
    stack_img = np.hstack((frame,output_frame))
    _,fps_stack = fps.update(stack_img)




    # cv2.imshow('Output', frame)
    cv2.imshow('frame', stack_img )
    if cv2.waitKey(10) == ord('q'):
        break
