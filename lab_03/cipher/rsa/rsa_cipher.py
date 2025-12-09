import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from rsa_ui import Ui_MainWindow
import requests
import rsa
import base64

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
    
    def generate_keys(self):
        (self.public_key, self.private_key) = rsa.newkeys(2048)
        
        # Lưu keys vào file
        with open('cipher/rsa/keys/public_key.pem', 'wb') as f:
            f.write(self.public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/private_key.pem', 'wb') as f:
            f.write(self.private_key.save_pkcs1('PEM'))
    
    def load_keys(self):
        try:
            with open('cipher/rsa/keys/public_key.pem', 'rb') as f:
                self.public_key = rsa.PublicKey.load_pkcs1(f.read())
            with open('cipher/rsa/keys/private_key.pem', 'rb') as f:
                self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
            return self.private_key, self.public_key
        except FileNotFoundError:
            return None, None
    
    def encrypt(self, message, key):
        if isinstance(key, rsa.PublicKey):
            encrypted = rsa.encrypt(message.encode(), key)
            return encrypted
        else:
            raise ValueError("Public key required for encryption")
    
    def decrypt(self, ciphertext, key):
        if isinstance(key, rsa.PrivateKey):
            decrypted = rsa.decrypt(ciphertext, key)
            return decrypted.decode()
        else:
            raise ValueError("Private key required for decryption")
    
    def sign(self, message, private_key):
        if isinstance(private_key, rsa.PrivateKey):
            signature = rsa.sign(message.encode(), private_key, 'SHA-256')
            return signature
        else:
            raise ValueError("Private key required for signing")
    
    def verify(self, message, signature, public_key):
        if isinstance(public_key, rsa.PublicKey):
            try:
                rsa.verify(message.encode(), signature, public_key)
                return True
            except:
                return False
        else:
            raise ValueError("Public key required for verification")

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error while calling API")
            print("Error: %s" % e.message)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        ciphertext = (
            self.ui.txt_cipher_text.toPlainText()
            .strip()
            .replace("\n", "")
            .replace(" ", "")
        )

        payload = {
            "ciphertext": ciphertext,
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Fail")
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
