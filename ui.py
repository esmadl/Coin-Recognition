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
        # Create a drop -down menu
        self.menu = QLineEdit(self)
        self.menu.move(20, 20)
        self.menu.resize(250, 40)

        
        # Sürükle bırak yeri oluştur
        self.label = QLabel(self)
        self.label.setAcceptDrops(True)
        self.label.move(20, 80)
        self.label.resize(640, 480) 
        

        # Creta buttons
        self.btn1 = QPushButton("Browse", self)
        self.btn1.move(300, 20)
        self.btn1.resize(120, 40)
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton("Run", self)
        self.btn2.move(430, 20)
        self.btn2.resize(120, 40)
        self.btn2.clicked.connect(self.processImage)

        self.btn3 = QPushButton("Save", self)
        self.btn3.move(560, 20)
        self.btn3.resize(120, 40)
        self.btn3.clicked.connect(self.save_image)

        #Place where the results will be written
        self.result = QLabel(self)
        self.result.move(680, 20)
        self.result.resize(200, 560)
        self.result.setWordWrap(True)
        self.result.setStyleSheet("background-color: #B0B0B0")

        # Window setting
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Coin recognition')
        self.show()

    def showDialog(self):
        # Choose a photo from the user
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            self.menu.setText(fname[0])

    def processImage(self):
        # Run and show the selected photo
        self.image_path = self.menu.text()
        self.image = cv2.imread(self.image_path)
    
        #imagefunc.scan_image(image)
        result, total,coin_count = imagefunc.scan_image(self.image)


        # Upload the scanning result to Label
        self.result.setText(f"       Total value: {round(float(total),3)}TL\n\n         {coin_count[0]} piece 1 coin\n         {coin_count[1]} piece 0.5 coin\n         {coin_count[2]} piece 0.25 coin\n         {coin_count[3]} piece 0.10 coin\n         {coin_count[4]} piece 0.05 coin")
        self.result.setStyleSheet("color: #282828; background-color: #B0B0B0; font-weight: 500")

        # Upload the photo processed to Label
        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image", "","Images (*.jpg *.png *.bmp);;All Files (*)", options=options)
        if fileName:
            cv2.imwrite(fileName, self.image)  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(900,600)
    sys.exit(app.exec_())
