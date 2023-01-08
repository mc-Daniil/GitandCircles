import sys
from random import randint
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.f = False

    def run(self):
        self.f = True
        self.repaint()
        self.f = False

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.circles(qp)
            qp.end()

    def circles(self, qp):
        for _ in range(randint(1, 10)):
            r = randint(100, 800)
            qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
            qp.drawEllipse(randint(100, 800), randint(100, 800), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())