import cv2
import os

def detect_sticker(image_path, sticker_template_path):
    # Load the image and the sticker template
    image = cv2.imread(image_path)
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
    cv2.waitKey(0)
    
    return top_left, bottom_right

dirPath=r"C:\Users\toby\OneDrive\Documents\Python\hello\Dads Work\Amount moved\Video\Pictures\Test Pictures\\"
template_path = r"C:\Users\toby\OneDrive\Documents\Python\hello\Dads Work\Amount moved\Video\Logo.jpg" 

for file in os.listdir(dirPath):
    image_path=dirPath+file
    top_left, bottom_right = detect_sticker(image_path, template_path)
    print("Top Left Coordinates:", top_left)
    print("Bottom Right Coordinates:", bottom_right)






