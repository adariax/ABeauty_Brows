import sqlite3
import sys

from data.window import Ui_Form

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MainW(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('data/ico.png'))
        self.mode = ''


app = QApplication(sys.argv)
ex = MainW()
ex.show()
sys.exit(app.exec_())
