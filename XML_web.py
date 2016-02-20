__author__ = 'Joshua'


import numpy as np
import cv2
import xml.etree.ElementTree as ET


#Reading XML
recipe=ET.parse('../TNE.xml')
root=recipe.getroot()
ings = []
directions=[]
for child in root.iter('ingredients'):
    for ing in child:
        item = ing.find('item').text
        amt = ing.find('amt').find('qty').text
        if(ing.find('amt').find('unit')!=None):
            unit=ing.find('amt').find('unit').text
        else:
            unit=""
        iing=(item,amt,unit)
        ings.append(iing)

count=0
for child in root.iter("direstions"):
    for step in child:
        st=step.text
        if 'action' in step.attrib:
            action=step.get('action')
        else:
            action=""
        if 'ing' in step.attrib:
            ing=step.get('ing')
        else:
            ing=""
        if 'time' in step.attrib:
            t=step.get("time")
        else:
            t='0'
        #print st+" act "+action+" ing "+ing+" time "+t
        direction=(count,st,action,ing,t)
        count +=1
        directions.append(direction)


# Camera control
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
        gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
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
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            gray =  cv2.GaussianBlur(gray,(15,15),0)
            #ret3,ref = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            ref = cv2.pyrDown(gray)
            cv2.imshow('ori',ref)




    if imgprocess == 1:
        cv2.imshow('frame',process)




cap.release()
cv2.destoryAllWindows()
