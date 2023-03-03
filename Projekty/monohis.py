import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("pies.jpg",0)
scale_per = 20
width=int(img.shape[1] * scale_per/100)
height=int(img.shape[0] * scale_per/100)
dim= (width, height)
resized = cv.resize(img, dim, interpolation= cv.INTER_AREA)
cv.imshow("resized.jpg", resized)


plt.hist(resized.ravel(), 256, [0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()