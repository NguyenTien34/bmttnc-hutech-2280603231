# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['PYQT5_QT_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 360)   # Tăng kích thước cửa sổ

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ===================== BUTTONS =====================
        self.EncryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.EncryptButton.setGeometry(QtCore.QRect(100, 260, 80, 30))
        self.EncryptButton.setObjectName("EncryptButton")

        self.DecryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.DecryptButton.setGeometry(QtCore.QRect(220, 260, 80, 30))
        self.DecryptButton.setObjectName("DecryptButton")

        # ===================== LABELS =====================
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 100, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 100, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 100, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # ===================== TEXT FIELDS =====================

        # Plain text
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 60, 230, 80))
        self.plainTextEdit.setObjectName("plainTextEdit")

        # Key input (QLineEdit – đúng)
        self.keyEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.keyEdit.setGeometry(QtCore.QRect(120, 160, 230, 25))
        self.keyEdit.setObjectName("keyEdit")

        # Cipher text
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 200, 230, 50))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 20))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher Tool"))
        self.EncryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.DecryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.label.setText(_translate("MainWindow", "Plain text"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "Cipher text"))
        self.label_4.setText(_translate("MainWindow", "Caesar Cipher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
