# Importing all modules
import cv2
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format
lowerBlue = np.array([110, 50, 50])
upperBlue = np.array([145, 255, 255]) # (These ranges will detect Blue)

lowerYellow = np.array([30, 150, 50])
upperYellow = np.array([32, 255, 255])

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while webcam_video.isOpened():
    success, video = webcam_video.read() # Reading webcam footage
    
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format
    
   
    maskBlue = cv2.inRange(img, lowerBlue, upperBlue) # Masking the image to find our color
    maskYellow = cv2.inRange(img, lowerYellow, upperYellow)


    mask_contoursBlue, hierarchy = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    mask_contoursYellow, hierarchy = cv2.findContours(maskYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    # Finding position of all contours blue
    if len(mask_contoursBlue) != 0:
        for mask_contourBlue in mask_contoursBlue:
            if cv2.contourArea(mask_contourBlue) > 200:
                x, y, w, h = cv2.boundingRect(mask_contourBlue)
                cv2.rectangle(video, (x, y), (x + w, y + h), (128, 0, 0), -1) #drawing rectangle
                #video[x: x + w, y: y + h] = 128,0,0
                
    # Finding position of all contours yellow
    if len(mask_contoursYellow) != 0:
        for mask_contourYellow in mask_contoursYellow:
            if cv2.contourArea(mask_contourYellow) > 200:
                x, y, w, h = cv2.boundingRect(mask_contourYellow)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 255), -1) #drawing rectangle
                #video[x: x + w, y: y + h] = 128,0,0           
                
                

    #cv2.imshow("mask image blue", maskBlue) # Displaying mask image
    cv2.imshow("mask image yellow", maskYellow) # Displaying mask image
    
    cv2.imshow("window", video) # Displaying webcam image
    if cv2.waitKey(1) & 0xFF == ord('q'):  #if q is pressed, program is stopped
        break
    
webcam_video.release()
cv2.destroyAllWindows()
