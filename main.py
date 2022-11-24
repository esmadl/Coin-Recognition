import cv2 as cv
import numpy as np

img = cv.imread("img-2.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    
gray = cv.medianBlur(gray, 5)
    
    
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=50, param2=40,
                               minRadius=17, maxRadius=300)
    
    
total = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    print(circles)
    for i in circles[0, :]:
        center = (i[0], i[1])
        print(center)
        cv.putText(img,f"center {i[0]}",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        cv.circle(img, center, 1, (0, 100, 100), 3)
        radius = i[2] #çap
        radi = radius
        print(radius)
        cv.circle(img, center, radius, (255, 0, 255), 3)
        sub = 13 - int(radi[0])*0.1
        rad = int(radi[0])*0,1+ sub
        if rad>13:
            total+=1.0
        elif rad<13 and rad>11:
            total+=0.5
        elif rad<13 and rad>11:
            total+=0.25     
        elif rad<11 and rad>9:
            total+=0.10  
        else:
            total4=0.05           
    
print(total)
cv.imshow("detected circles", img)
cv.waitKey()


