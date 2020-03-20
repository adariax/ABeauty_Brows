import sqlalchemy
import sys

from data import db_session
from data.__all_models import clients, paints

from interface.main_window import Ui_Form
from interface.add_client import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon


db_session.global_init("database/brows_info.sqlite")

Client = clients.Client
Paint = paints.Paint


class AddClient(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.acccept.clicked.connect(self.add_to_db)

    def add_to_db(self):
        session = db_session.create_session()
        client = Client()
        client.name_surname = self.name_surname.text()
        session.add(client)
        session.commit()

        self.close()


class MainW(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.session = db_session.create_session()

        self.setWindowIcon(QIcon('data/ico.png'))
        self.mode = ''

        self.add_button.clicked.connect(self.adding_client)

    def load_clients(self):
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Имя Фамилия клиента", ])
        self.table.setRowCount(0)

        for number, client in enumerate(self.session.query(Client).all()):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(number, 0, QTableWidgetItem(client.name_surname))
        self.table.setColumnWidth(0, self.table.width())

    def adding_client(self):
        dialog = AddClient()
        dialog.exec()
        self.load_clients()


app = QApplication(sys.argv)
ex = MainW()
ex.show()
sys.exit(app.exec_())
