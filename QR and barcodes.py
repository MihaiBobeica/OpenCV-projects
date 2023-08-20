import cv2 #might require pip install
import numpy as np
from pyzbar.pyzbar import decode #might require pip install

video = cv2.VideoCapture(0) #getting the image from the camera

#resizing the image
video.set(3,640) 
video.set(4,480)

while video.isOpened():
    succes, img = video.read() # succes shows if the image was read succesfully, img is the image
    
    if not succes:
        break
    
    for barcode in decode(img):
        
        #create the outline of the code
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img, [pts], True, (255, 0, 0), 3)
       
       #adds text
        myData = barcode.data.decode('utf-8')
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 0), 2)
        
    #output final image image 
    cv2.imshow("Result", img)    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #if q is pressed, program is stopped
        break
    
video.release()
cv2.destroyAllWindows()