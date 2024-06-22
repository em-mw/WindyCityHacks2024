import time
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
        cam_no = int(window.CameraBox.value())
        try:vid = cv2.VideoCapture(cam_no)
        except:
            print("error")
            vid = cv2.VideoCapture(cam_no)
        hand = mp.solutions.hands.Hands()
        point = mp.solutions.drawing_utils
        #p1 = threading.Thread(target=iclean.running, args=(window,))
        #p1.start()
        while True:
            try: 
                if cam_no != int(window.CameraBox.value()): cam_no = int(window.CameraBox.value())
            except: 
                window.label_2.setText("❗📷➡️🧾❗SET CAM AS NUMBER NOT TEXT")
            _, frame = vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_height, frame_width, _ = frame.shape
            hand_output = hand.process(frame)
            hands_disp = hand_output.multi_hand_landmarks
            #print(hands_disp)
            if hands_disp and window.MouseCamButton.isChecked():
                for point_data in hands_disp:
                    point.draw_landmarks(frame, point_data, mp.solutions.hands.HAND_CONNECTIONS)
                    landmarks = point_data.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x*frame_width)
                        y = int(landmark.y*frame_height)
                        print(f"{x}, {y}")
                        if id == 8:
                            window.label_2.setText(f"🟢 Status: Detection ({x}, {y})")
                            #cv2.circle(img=frame, center=(x,y), radius=12, color=(0,255,0))
                        
            else:window.label_2.setText("🟡 Status: Detection (pending hand input...)")

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