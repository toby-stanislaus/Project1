import cv2
import time
import os

cam=cv2.VideoCapture(r"Video/Video.mp4")
totalDiff=0
amount=0
while True:
    
    start=time.time()
    ret,img=cam.read()
    cv2.imshow("",img)
    cv2.waitKey(1)
    end=time.time()
    diff=end-start
    diff*=10
    totalDiff+=diff
    totalDiff*10
    amount+=1
    
    avgTime=totalDiff/amount
    os.system("cls")
    print("Average processing time is:",avgTime/10,"seconds")