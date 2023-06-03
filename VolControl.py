import cv2
import time
import numpy as np
from hand_track_module import HandDetector
from math import hypot
from subprocess import call

###################################################
wCam, hCam = 1280, 720
###################################################
i=0

#time set up for fps
pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = HandDetector(detectionConf=0.7)

def lengthToVolume(length):
    #len ranges from 20 to 400
    if ((length-20)/380) * 100 > 100:
        return 100
    elif ((length-20)/380) * 100 < 0:
        return 0
    return ((length-20)/380) * 100

while 1:
    success, img = cap.read()
    img = cv2.flip(img,1) #this line makes the camera act as a mirror

    img = detector.getHands(img)
    lmList = detector.getPos(img, draw=False)

    if len(lmList) != 0:
        #print(lmList[4], lmList[8])

        cv2.circle(img, (lmList[4][1], lmList[4][2]), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (lmList[8][1], lmList[8][2]), 5, (255, 0, 0), cv2.FILLED)

        cv2.line(img, (lmList[4][1], lmList[4][2]), (lmList[8][1], lmList[8][2]), (255, 0, 0), 5)

        cx, cy = (lmList[4][1] + lmList[8][1])//2, (lmList[4][2] + lmList[8][2])//2
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        length = hypot((lmList[8][1] - lmList[4][1]), (lmList[8][2] - lmList[4][2]))
        vol = int(lengthToVolume(length))

        if length<50:
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
        
        volScript = 'set volume output volume ' + str(vol)
        script = "osascript -e \'" + volScript + "\'"

    if i == 5:
        if len(lmList) != 0:
            call([script], shell=True)
        i = 0
    else:
        i = i + 1

    #getting fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #show fps on screen
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)