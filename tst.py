import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, uic

class MyPillow(QMainWindow):
    def __init__(self):
        super(MyPillow, self).__init__()
        uic.loadUi('idk.ui', self)
        self.app = app

        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        self.orig_image = Image.open(self.filename)
        self.curr_image = Image.open(self.filename)
        self.degree = 0
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        # for button in [self.B, self.push]

    def set_channel(self):
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if self.sender().text == 'R':
                    pixels[i, j] = r, 0, 0
                if self.sender().text == 'G':
                    pixels[i, j] = 0, g, 0
                if self.sender().text == 'B':
                    pixels[i, j] = 0, 0, b
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.label.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.pushButton_2:
            self.degree -= 90
            degree = -90
        else:
            self.degree += 90
            degree = 90
        self.degree %= 360
        self.curr_image = self.curr_image.rotate(degree, expand=True)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
