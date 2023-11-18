import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from random import randrange
from PyQt5.QtCore import Qt


class Yellow_circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        width = self.size().width()
        height = self.size().height()
        x = randrange(width)
        y = randrange(height)
        d = randrange(1, 400)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(x, y, d, d)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Yellow_circles()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())