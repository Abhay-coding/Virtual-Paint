import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

myColors = [[83, 114, 58, 255, 181, 255]]

myColorVal = [[245,152,66]]#BGR


myPoints =   []            #[x , y , colorid]

def findColors(img, myColors,mycolorVal):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgresult,(x,y),10,mycolorVal[count],cv2.FILLED)
        if x!=0 or y!=0:
            myPoints.append([x,y,count])

        count+=1
        # cv2.imshow("Image", mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            # cv2.drawContours(imgresult, cnt, -1, (0, 0, 255), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(mypoints,mycolors,mycolorVal):
    for point in mypoints:
        cv2.circle(imgresult, (point[0], point[1]), 10, mycolorVal[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgresult=img.copy()
    if not success:
        break
    newPoints = findColors(img, myColors,myColorVal)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColors,myColorVal)


    cv2.imshow("Video", img)
    cv2.imshow("Result", imgresult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
