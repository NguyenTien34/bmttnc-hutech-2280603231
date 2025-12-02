from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Plain text input
        self.label_plain = QtWidgets.QLabel(self.centralwidget)
        self.label_plain.setGeometry(QtCore.QRect(20, 20, 100, 20))
        self.label_plain.setObjectName("label_plain")
        self.label_plain.setText("Plain Text:")
        
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(20, 45, 360, 100))
        self.txt_plain_text.setObjectName("txt_plain_text")
        
        # Cipher text input/output
        self.label_cipher = QtWidgets.QLabel(self.centralwidget)
        self.label_cipher.setGeometry(QtCore.QRect(420, 20, 100, 20))
        self.label_cipher.setObjectName("label_cipher")
        self.label_cipher.setText("Cipher Text:")
        
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(420, 45, 360, 100))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        
        # Buttons for encryption/decryption
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(20, 160, 100, 30))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_encrypt.setText("Encrypt")
        
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(140, 160, 100, 30))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_decrypt.setText("Decrypt")
        
        # Key generation button
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(260, 160, 120, 30))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.btn_gen_keys.setText("Generate Keys")
        
        # Signature section
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(20, 220, 100, 20))
        self.label_info.setObjectName("label_info")
        self.label_info.setText("Message to Sign:")
        
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(20, 245, 360, 80))
        self.txt_info.setObjectName("txt_info")
        
        self.label_sign = QtWidgets.QLabel(self.centralwidget)
        self.label_sign.setGeometry(QtCore.QRect(420, 220, 100, 20))
        self.label_sign.setObjectName("label_sign")
        self.label_sign.setText("Signature:")
        
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(420, 245, 360, 80))
        self.txt_sign.setObjectName("txt_sign")
        
        # Signature buttons
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(20, 340, 100, 30))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_sign.setText("Sign")
        
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(140, 340, 100, 30))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_verify.setText("Verify")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
