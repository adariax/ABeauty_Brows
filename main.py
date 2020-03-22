import sys

from data import db_session
from data.__all_models import clients, paints, events

from interface.main_window import Ui_Form
from interface.add_client import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QWidget, QDialog  # QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt

Client = clients.Client
Paint = paints.Paint
Event = events.Event


class AddClient(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('interface/ico.png'))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

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

        self._mode = 'a'  # a = all clients, c = current client, p = paints

        db_session.global_init("database/brows_info.sqlite")
        self.session = db_session.create_session()

        self.setWindowIcon(QIcon('interface/ico.png'))

        self.add_button.clicked.connect(self.adding)
        self.action_button.clicked.connect(self.action)

        self.table.cellDoubleClicked.connect(self.client)
        self.table.cellClicked.connect(self.row_focus)

        self.load_clients()

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if mode == 'a':
            self.load_clients()
        elif mode == 'c':
            self.load_current_client(self.table.currentRow() + 1)
        elif mode == 'p':
            pass
        self._mode = mode
        self.change_buttons()

    def row_focus(self):
        for i in range(self.table.columnCount()):
            self.table.item(self.table.currentRow(), i).setSelected(True)

    def client(self):
        if self.mode == 'a':
            self.mode = 'c'

    def action(self):
        if self.mode == 'a':
            self.delete_client()
        elif self.mode == 'c':
            self.mode = 'a'
        elif self.mode == 'p':
            pass

    def adding(self):
        dialog = AddClient()
        dialog.exec()
        self.load_clients()

    def delete_client(self):
        client_id = self.table.currentRow() + 1
        self.session.query(Client).filter(Client.id == client_id).delete()
        for number, client in enumerate(self.session.query(Client).all()):
            client.id = number + 1
        self.session.query(Event).filter(Event.client_id == client_id).delete()
        self.session.commit()
        self.load_clients()

    def change_buttons(self):
        self.action_button.setText('Назад' if self.mode != 'a' else 'Удалить')

    def load_clients(self):
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Имя Фамилия клиента", ])
        self.table.setRowCount(0)

        for number, client in enumerate(self.session.query(Client).all()):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(number, 0, QTableWidgetItem(client.name_surname))
        self.table.setColumnWidth(0, 570)

    def load_current_client(self, client_id):
        client = self.session.query(Client).filter(Client.id == client_id).first()
        self.setWindowTitle("a.beauty / " + client.name_surname)

        self.table.clear()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Время посещения", "Примечания"])
        self.table.setRowCount(0)

        for row, event in enumerate(client.events):
            self.table.setRowCount(self.table.rowCount() + 1)
            for col, item in enumerate(event.get_items()):
                self.table.setItem(row, col, QTableWidgetItem(item))
        self.table.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MainW()
ex.show()
sys.exit(app.exec_())
