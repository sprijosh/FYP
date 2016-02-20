__author__ = 'Joshua'


import numpy as np
import cv2

cap = cv2.VideoCapture(0)
imgprocess = 1
none,process = cap.read()
process = cv2.pyrDown(process)

while(True):
    key = cv2.waitKey(1)

    if  key == ord('q'):
        break
    elif key == ord('2'):
        ret, frame2  = cap.read()
        gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        #blur2 =  cv2.GaussianBlur(gray2,(5,5),0)
        #ret3,ref2 = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        ref2 = cv2.pyrDown(gray2)
        cv2.imshow('ref2',ref2)
        gray2 =  cv2.GaussianBlur(gray2,(15,15),0)

        process = cv2.absdiff(gray,gray2)
        process = cv2.pyrDown(process)
        process = cv2.cvtColor(process,cv2.COLOR_BGR2GRAY)
        process =  cv2.GaussianBlur(process,(15,15),0)
        ret3,process = cv2.threshold(process,20,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #gray  = cv2.subtract(gray,gray2)
    elif key == ord('1'):
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            gray =  cv2.GaussianBlur(gray,(15,15),0)
            #ret3,ref = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            ref = cv2.pyrDown(gray)
            cv2.imshow('ori',ref)




    if imgprocess == 1:
        cv2.imshow('frame',process)




cap.release()
cv2.destoryAllWindows()
