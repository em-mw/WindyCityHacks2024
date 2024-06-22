import threading, gui
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class frame:
    def cam(self, window):
        vid = cv2.VideoCapture(0)
        while True:
            ret, frame = vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
    #x.join()
    MainWindow.show()
    try:
        sys.exit(app.exec())
    except:
        dead=True