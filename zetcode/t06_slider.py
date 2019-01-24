"""
ZetCode PyQt5 tutorial

This example shows a QSlider widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../image/Status-audio-volume-muted-icon.png').scaled(30, 30))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('../image/Status-audio-volume-muted-icon.png').scaled(30, 30))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('../image/Status-audio-volume-low-icon.png').scaled(30, 30))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('../image/Status-audio-volume-medium-icon.png').scaled(30, 30))
        else:
            self.label.setPixmap(QPixmap('../image/Status-audio-volume-high-icon.png').scaled(30, 30))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


