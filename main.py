import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QPen, QPainter, QColor, QPolygon, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.button_click)
        self.r = -1
        self.x, self.y = 0, 0

    def button_click(self):
        self.r = randint(40, 600)
        self.x = randint(10, self.width())
        self.y = randint(10, self.height())

    def paintEvent(self, event):
        if self.r != -1:
            qp = QPainter()
            qp.begin(self)
        
            self.drawC(qp)
            qp.end()

    def drawC(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPoint(self.x, self.y), self.r, self.r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mv = MainWindow()
    mv.show()
    sys.exit(app.exec_())