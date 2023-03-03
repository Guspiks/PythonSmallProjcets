import cv2
import numpy as np
im = cv2.imread("test1.jpg")
out = im.copy()
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret, tresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

czcionka = cv2.FONT_ITALIC
texted = True

for k in contours:
    x,y,w,h= cv2.boundingRect(k)

    if w>10 and h>10:
        if x==0 and y==0:
            continue
        rogi = cv2.approxPolyDP(k, 0.02*cv2.arcLength(k, True), True)

        col = (0,0,0)
        text=""

        if len(rogi) == 4:
            col = (255,0,0)
            text = "prostokat"
        elif len(rogi) == 3:
            col = (0,255,0)
            text = "trojkat"
        elif len(rogi)>4:
            col = (0,0,255)
            text = "wielokat"

        cv2.drawContours(out, [rogi], 0, col, 2)

        if texted:
            cv2.putText(out, text, (x,y), czcionka, 0.7, (100,100,100), 2)

cv2.imshow("ksztalty", out)
cv2.waitKey(0)
cv2.destroyAllWindows()