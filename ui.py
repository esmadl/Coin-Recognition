import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLineEdit
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt
import cv2
import imagefunc

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Açılır menü oluştur
        self.menu = QLineEdit(self)
        self.menu.move(20, 20)
        self.menu.resize(250, 40)
    
        # Sürükle bırak yeri oluştur
        self.label = QLabel(self)
        self.label.setAcceptDrops(True)
        self.label.move(20, 80)
        self.label.resize(640, 480) 
        

        # Buttonlar oluştur
        self.btn1 = QPushButton("Browse", self)
        self.btn1.move(300, 20)
        self.btn1.resize(120, 40)
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton("Run", self)
        self.btn2.move(430, 20)
        self.btn2.resize(120, 40)
        self.btn2.clicked.connect(self.processImage)

        #Sonuçların yazılacağı yer
        self.result = QLabel(self)
        self.result.move(680, 20)
        self.result.resize(200, 640)
        self.result.setWordWrap(True)

        # Pencere ayarları
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Coin recognition')
        self.show()

    def showDialog(self):
        # Kullanıcıdan bir fotoğraf seç
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.menu.setText(fname[0])

    def processImage(self):
        # Seçilen fotoğrafı işle ve göster
        image_path = self.menu.text()
        image = cv2.imread(image_path)
    
        #imagefunc.scan_image(image)
        result, total,coin_count = imagefunc.scan_image(image)


        # Taraman sonucunu label'e yükle
        self.result.setText(f"Toplam değer: {round(float(total),3)} TL\n\n{coin_count[0]} adet 1 coin\n{coin_count[1]} adet 0.5 coin\n{coin_count[2]} adet 0.25 coin\n{coin_count[3]} adet 0.1 coin\n{coin_count[4]} adet 0.05 coin")
        self.result.setStyleSheet("QLabel {color: black; font-size: 15pt; font-weight: bold; }")
        # İşlenen fotoğrafı label'e yükle
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(900,600)
    sys.exit(app.exec_())
