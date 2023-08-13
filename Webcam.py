import cv2
import os

def detect_sticker(image, sticker_template_path):
    # Load the image and the sticker template
    
    template = cv2.imread(sticker_template_path)

    # Get template width and height
    template_height, template_width = template.shape[:2]

    # Match the template in the image
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Extract coordinates of the detected sticker
    top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

    #showing image
    
    cv2.rectangle(image,top_left,bottom_right,(0,255,0),1)
    cv2.imshow("",image)
    cv2.waitKey(1)
    
    return top_left, bottom_right

cam=cv2.VideoCapture(0)
template_path = r"C:\Users\toby\OneDrive\Documents\Python\hello\Dads Work\Amount moved\Video\Logo.jpg" 

while True:
    ret,frame=cam.read()
    top_left,bottom_right=detect_sticker(frame,template_path)