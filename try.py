import cv2
from matplotlib import pyplot as plt
img = cv2.imread('img-1.jpeg')
# Scale down to 25%
p = 0.25
w = int(img.shape[1] * p)
h = int(img.shape[0] * p)
new_img = cv2.resize(img, (5000, 5000))

cv2.imshow("old",img)
cv2.imshow("new",new_img)
cv2.waitKey()
