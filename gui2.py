# Form implementation generated from reading ui file '.\mousemenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 796)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(28)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.MouseCamButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.MouseCamButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(196, 215, 255);")
        self.MouseCamButton.setCheckable(True)
        self.MouseCamButton.setObjectName("MouseCamButton")
        self.horizontalLayout.addWidget(self.MouseCamButton)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.CameraBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.CameraBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CameraBox.setObjectName("CameraBox")
        self.horizontalLayout.addWidget(self.CameraBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_label.setText(_translate("MainWindow", "Video Loading..."))
        self.label_2.setText(_translate("MainWindow", "🔴Status: Detection: Camera Feed Not Available 😨"))
        self.MouseCamButton.setText(_translate("MainWindow", "MouseCam is (OFF) ❌"))
        self.label.setText(_translate("MainWindow", "Camera:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
