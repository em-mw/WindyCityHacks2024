import cv2, os
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from math import ceil

capture = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)


imgsize = 300

indi = 0
while True:
    _, frame = capture.read()
    hands, frame = detector.findHands(frame)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        x, y = x-20, y-20
        w, h = w+40, h+40
        imgWhite = background = np.zeros((imgsize+500, imgsize+500, 3), dtype=np.uint8)*255 #the thing crashes if there it goes beyond the border
        imgCrop = frame[y:y+h, x:x+w]
        ImageCropShape = imgCrop.shape
        

        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgsize / h
            wCal = ceil(k * w)
            try:imgResize = cv2.resize(imgCrop, (wCal, imgsize))
            except:pass
            imgResizeShape = imgResize.shape
            wGap = ceil((imgsize - wCal) / 2)
            imgWhite = imgResize
        else:
            k = imgsize / w
            hCal = ceil(k * h)
            try:imgResize = cv2.resize(imgCrop, (imgsize, hCal))
            except:pass
            imgResizeShape = imgResize.shape
            hGap = ceil((imgsize - hCal) / 2)
            imgWhite = imgResize

        cv2.imshow("crop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)
        
    cv2.imshow("ima", frame)
    key = cv2.waitKey(1)

    if key == ord("s"):
        print(cv2.imwrite(f"train_img/{indi}.png", imgWhite))
        print("saved")
        indi+=1
