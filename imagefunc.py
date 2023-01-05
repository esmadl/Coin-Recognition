import cv2 as cv
import numpy as np

#img = cv.imread("images/img-8.jpeg")

def scan_image(img):

    #img = cv.imread(img1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #This line of code converts the input image from the BGR color space to grayscale. 
                                               #This is done because the Hough Circle Transform works better on grayscale images, 
                                               #as it only requires a single channel of data (i.e., intensity values) as input.
        
    
    
    gray = cv.GaussianBlur(gray, (15, 15), 0) #The Gaussian blur is a smoothing filter that helps to reduce noise and other irregularities in the image, 
                                            #which can improve the accuracy of the circle detection. 
                                            # The blur is applied using a kernel of size (15, 15), 
                                            # and the sigma value (i.e., the standard deviation of the Gaussian distribution) is set to 0.
        
        
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,    
                                param1=10, param2=30,
                                minRadius=0, maxRadius=300) #The Hough Circle Transform is an algorithm that can detect circles in images by looking 
                                                            #for circular shapes in the image that meet certain criteria. 
                                                            #The Hough Circle Transform takes the following arguments:

                                
    
    """
    param1 is the threshold for the gradient magnitude. It is used in the edge detection stage of the circle detection process. 
    A higher value of param1 means that the algorithm will only consider strong edges as possible circle boundaries, 
    while a lower value means that it will consider weaker edges as well.
    param2 is the threshold for the circle center detection. It is used in the circle center detection stage of the process. 
    A higher value of param2 means that the algorithm will only consider circle centers that are strongly supported by the detected edges, 
    while a lower value means that it will consider weaker evidence as well.
    """
    
    """
    This code looks at the circles detected by the Hough Circle Transform, and it classifies them based on their radius. 
    It then counts the number of coins of each type, and calculates the total value of all the coins.
    """
    total=0
    coin = [0,0,0,0,0]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            cv.circle(img, center, 1, (96, 150, 249), 4)
            radius = i[2] #çap
            cv.circle(img, center, radius, (99, 169, 231), 4)
            """
            There are two cv.circle() function calls in this code because they serve different purposes.
            The first cv.circle() function call is used to draw a small circle at the center of each detected circle, 
            and the second cv.circle() function call is used to draw a circle around each detected circle
            """

            if radius>100:
                total+=1
                coin[0]=+1
                cv.putText(img,"Coin : 1",center,cv.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 0),thickness=3)
            elif radius>90 and radius<100:
                coin[1]=+1
                total+=0.5
                cv.putText(img,"Coin : 0.5",center,cv.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 0),thickness=3)
            elif radius>78 and radius<90:
                coin[2]=+1
                total+=0.25
                cv.putText(img,"Coin : 0.25",center,cv.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 0),thickness=3)
            elif radius>74 and radius<=78:
                coin[3]=+1
                total+=0.10
                cv.putText(img,"Coin : 0.10",center,cv.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 0),thickness=3)
            elif radius<=73:
                coin[4]=+1
                total+=0.05
                cv.putText(img,"Coin : 0.05",center,cv.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 0),thickness=3)


    return cv.putText(img, f'Total: {total}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 
                    1, (50, 50), 2, cv.LINE_AA),str(total),coin


    #cv.imshow("detected circles", img) /Users/esmanur/Desktop/Coin-Recognition/images/img-3.jpeg
    #cv.waitKey()


#scan_image("images/img-6.jpeg")    