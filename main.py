from math import ceil
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import mediapipe as mp
import threading, gui
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import cv2, pyautogui
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
    

class frame:  
    def cam(self, window) -> None:
        detector = HandDetector(maxHands=1)
        cam_no = int(window.CameraBox.value())
        try:vid = cv2.VideoCapture(cam_no)
        except:
            print("error")
            #vid = cv2.VideoCapture(cam_no)
        hand = mp.solutions.hands.Hands()
        point = mp.solutions.drawing_utils
        imgsize = 300
        labels = ["A", "B", "C", "D", "E", "F", "G"]
        #p1 = threading.Thread(target=iclean.running, args=(window,))
        #p1.start()
        while True:
            try: 
                if cam_no != int(window.CameraBox.value()): cam_no = int(window.CameraBox.value())
            except: 
                window.label_2.setText("❗📷➡️🧾❗SET CAM AS NUMBER NOT TEXT")
            _, frame = vid.read()
            
            hands, frame = detector.findHands(frame)
            classifier = Classifier("Model/keras_model.h5", "Model/label.txt")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
                prediction, index = classifier.getPrediction(frame)
            else:
                k = imgsize / w
                hCal = ceil(k * h)
                try:imgResize = cv2.resize(imgCrop, (imgsize, hCal))
                except:pass
                imgResizeShape = imgResize.shape
                hGap = ceil((imgsize - hCal) / 2)
                imgWhite = imgResize
                #classifier.getPrediction(frame)
            
                        
            #else:window.label_2.setText("🟡 Status: Detection (pending hand input...)")

            h, w, ch = frame.shape
            bytes_per_line = ch * w
            #image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0])
            convert_to_Qt_format = QImage(frame.data, int(w), int(h), bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(convert_to_Qt_format)
            #self.image_label.setPixmap(pixmap)
            window.image_label.setPixmap(pixmap)
            window.image_label.setScaledContents(False)
            if dead: break
    
if __name__ == "__main__":
    import sys
    global dead
    dead=False
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    iframe = frame()
    x = threading.Thread(target=iframe.cam, args=(ui,))
    x.start()
    MainWindow.show()
    try:
        sys.exit(app.exec())
    except:
        dead=True