import cv2


cam=cv2.VideoCapture(r"Video/Video.mp4")

while True:
    ret,img=cam.read()
    cv2.imshow("",img)
    cv2.waitKey(1)