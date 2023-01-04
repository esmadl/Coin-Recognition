import cv2 as cv
import numpy as np

img = cv.imread("images/img-8.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
gray = cv.GaussianBlur(gray, (15, 15), 0)
    
    
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=10, param2=30,
                               minRadius=0, maxRadius=300)

                               
total=0
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv.circle(img, center, 1, (0, 100, 100), 3)
        radius = i[2] #çap
        cv.circle(img, center, radius, (255, 0, 255), 3)

        if radius>100:
            total+=1
            cv.putText(img,"Coin : 1",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        elif radius>90 and radius<100:
            total+=0.5
            cv.putText(img,"Coin : 0.5",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        elif radius>80 and radius<90:
            total+=0.25
            cv.putText(img,"Coin : 0.25",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        elif radius>75 and radius<=80:
            total+=0.10
            cv.putText(img,"Coin : 0.10",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        elif radius<75:
            total+=0.05
            cv.putText(img,"Coin : 0.05",center,cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))


cv.putText(img, f'Total: {total}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 
                   1, (50, 50), 2, cv.LINE_AA)
print(total)
cv.imshow("detected circles", img)
cv.waitKey()