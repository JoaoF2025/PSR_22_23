#!/usr/bin/env python3
#Test examples for Exercise 3

import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('/home/joaof2025/PSR_22.23/PSR_Solutions/Aula06/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(30, 30)
    )
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
        
    cv2.imshow('video',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()