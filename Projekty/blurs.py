import cv2 as cv
import numpy as np

img = cv.imread("testt.png",0)
scale_per = 100
width=int(img.shape[1] * scale_per/100)
height=int(img.shape[0] * scale_per/100)
dim= (width, height)
resized = cv.resize(img, dim, interpolation= cv.INTER_AREA)
cv.imshow("resized.jpg", resized)
cv.imwrite("monotest.png", resized)
#blur = cv.blur(resized, (7,7))
#cv.imshow("meanblur", blur)

#gauss = cv.GaussianBlur(resized, (5,5), 0.76)
#cv.imshow("Gausian blur", gauss)

#median = cv.medianBlur(resized, 5)
#cv.imshow("Gausian blur", gauss)

#kernel1 = np.array([[-1,-1,-1],
#                   [-1, 9,-1],
#                   [-1,-1,-1]])
#imgsharp = cv.filter2D(resized, -1, kernel1)
#cv.imshow("Wyostrzenie", imgsharp)

#kernel2 = np.array([[0,0,0],
#                  [-1, 1,0],
#                  [0,0,0]])
#imgshift = cv.filter2D(resized, -1, kernel2)
#cv.imshow("przeniesienie", imgshift)

#kernel3 = np.array([[0,-1,0],
#                   [-1,4,-1],
#                   [0,-1,0]])
#imggradshif = cv.filter2D(resized, -1, kernel3)
#cv.imshow("LAP1", imggradshif)

#kernel4 = np.array([[-1,0,-1],
#                   [0,4,0],
#                   [-1,0,-1]])
#imglapu = cv.filter2D(resized, -1, kernel4)
#cv.imshow("LAPU", imglapu)

#kernelsob = np.array([[-1,0,1],
#                   [-1,0,2],
 #                  [-1,0,1]])
#imgsob = cv.filter2D(resized, -1, kernelsob)
#cv.imshow("sob", imgsob)
#
#kernelsob2 = np.array([ [0,1,1],
  #                      [-1,0,1],
 #                       [-2,-1,0]])
#imgsob2 = cv.filter2D(resized, -1, kernelsob2)
#cv.imshow("sob2", imgsob2)

#kernelsob3 = np.array([[1,2,1],
 #                  [0,0,0],
  #                 [-1,-2,-1]])
#imgsob3 = cv.filter2D(resized, -1, kernelsob3)
#cv.imshow("sob3", imgsob3)

#imgsob4 = cv.filter2D(imgsob3, -1, kernelsob)
#cv.imshow("sobel pozomy i pionowy", imgsob4)

edges = cv.Canny(resized, 60, 100)
cv.imshow("edges",edges)

cv.waitKey(0)
cv.destroyAllWindows()