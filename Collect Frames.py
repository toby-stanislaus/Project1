import cv2

cap = cv2.VideoCapture(r"Video\Video.mp4")

frameNum=115
i=0

while True:
    frameNum+=1
    ret, frame = cap.read()
    if not ret:
        break
    if frameNum%339==0:
        i+=1
        if i%2!=0:
            cv2.imwrite(r"Video\Pictures\Left\\"+str(i)+".jpg",frame)
        else:
            cv2.imwrite(r"Video\Pictures\Right\\"+str(i)+".jpg",frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(frameNum)  