__author__ = 'Joshua'


import numpy as np
import cv2
import xml.etree.ElementTree as ET
import sys

color_mode=cv2.COLOR_BGR2XYZ
ings = []
directions=[]

cap = cv2.VideoCapture(int(sys.argv[1]))
#read XML and parse it into array
recipe=ET.parse('../TNE.xml')
root=recipe.getroot()

for child in root.iter('ingredients'):
    for ing in child:
        item = ing.find('item').text
        code = ing.find('item').get('value')
        amt = ing.find('amt').find('qty').text
        if(ing.find('amt').find('unit')!=None):
            unit=ing.find('amt').find('unit').text
        else:
            unit=""

        iing=(item,amt,unit,code)
        ings.append(iing) #List will be iteam, amount, unit, item code)

for i in ings:
    print i

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
imgprocess = 1
none,process = cap.read()
process = cv2.pyrDown(process)

while(True):
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('2'):   #Take current frame
        _, frm_ref = cap.read()
        frm_ref = cv2.cvtColor(frm_ref, color_mode)
        #blur2 =  cv2.GaussianBlur(gray2,(5,5),0)
        #ret3,ref2 = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        cv2.imshow('ref2',cv2.pyrDown(frm_ref))
        frm_ref = cv2.GaussianBlur(frm_ref, (15, 15), 0)

        process = cv2.absdiff(frame, frm_ref)
        process = cv2.pyrDown(process)
        process = cv2.cvtColor(process,cv2.COLOR_BGR2GRAY)
        process =  cv2.GaussianBlur(process,(15,15),0)
        _,process = cv2.threshold(process,20,255,cv2.THRESH_BINARY)

        _,contours, hierarchy = cv2.findContours(process,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        hig,wid=process.shape[:2]
        img = np.zeros((hig,wid,3), np.uint8)
        print contours
        for cnt in contours[:3]:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('output',img)
    elif key == ord('1'):   #Take references frame
            ret,frame = cap.read()
            frame = cv2.cvtColor(frame,color_mode)
            frame = cv2.GaussianBlur(frame,(15,15),0)
            #ret3,ref = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            cv2.imshow('ori',cv2.pyrDown(frame))
    if imgprocess == 1:
        cv2.imshow('Processed',process)




cap.release()
