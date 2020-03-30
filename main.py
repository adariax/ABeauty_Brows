import sys
import datetime

from data import db_session
from data.__all_models import clients, paints, events

from interface.main_window import Ui_Form
from interface.add_client import Ui_Dialog_C
from interface.add_paint import Ui_Dialog_P
from interface.add_event import Ui_Dialog_E

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt, QDate

Client = clients.Client
Paint = paints.Paint
Event = events.Event


class AddEvent(QDialog, Ui_Dialog_E):
    def __init__(self, client_id):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('interface/ico.png'))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.add_btn.clicked.connect(self.add_to_db)

        self.session = db_session.create_session()
        self.client = client_id

        self.get_date()
        self.load_cb()

    def get_date(self):
        date_now = list(map(int, str(datetime.datetime.now()).split()[0].split('-')))
        self.date.setDate(QDate(*date_now))

    def load_cb(self):
        self.paints.addItem('')
        for paint in self.session.query(Paint).all():
            self.paints.addItem(paint.title)

    def add_to_db(self):
        event = Event()
        event.client_id = self.client
        event.note = self.text.toPlainText()
        event.created_date = datetime.date(*map(int,
                                                self.date.date().toPyDate().isoformat().split('-')))
        event.paint_id = self.paints.currentIndex()
        if event.paint_id == 0:
            QMessageBox.warning(self, 'Ошибка', 'Не выбран краситель')
        elif event.note == '':
            QMessageBox.question(self, 'Ошибка', 'Примечания пусты, если их нет, поставьте прочерк')
        else:
            self.session.add(event)
            self.session.commit()

            self.close()


class AddPaint(QDialog, Ui_Dialog_P):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('interface/ico.png'))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.acccept.clicked.connect(self.add_to_db)

    def add_to_db(self):
        session = db_session.create_session()
        paint = Paint()
        paint.title = self.text.text()
        session.add(paint)
        session.commit()

        self.close()


class AddClient(QDialog, Ui_Dialog_C):
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
        self.change_mode.clicked.connect(self.changing_mode)

        self.table.cellDoubleClicked.connect(self.client)
        self.table.cellClicked.connect(self.row_focus)

        self.curr_client = None

        self.loading(self.mode)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if mode == 'a':
            self.change_mode.setText('Перейти')
        elif mode == 'c':
            self.curr_client = self.table.currentRow() + 1
        elif mode == 'p':
            self.change_mode.setText('Назад')
        self.change_mode.setVisible(True if mode != 'c' else False)
        self.label_2.setVisible(True if mode != 'c' else False)
        self._mode = mode
        self.loading(self.mode) if mode != 'c' else self.load_current_client(self.curr_client)
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
            self.delete_paint()

    def adding(self):
        dialog = None
        if self.mode == 'a':
            dialog = AddClient()
        elif self.mode == 'c':
            self.add_event()
            return
        elif self.mode == 'p':
            dialog = AddPaint()
        dialog.exec()
        self.loading(self.mode)

    def add_event(self):
        dialog = AddEvent(self.curr_client)
        dialog.exec()
        self.load_current_client(self.curr_client)

    def changing_mode(self):
        self.mode = 'p' if self.mode == 'a' else 'a'

    def change_buttons(self):
        self.action_button.setText('Назад' if self.mode == 'c' else 'Удалить')

    def delete_client(self):
        client_id = self.table.currentRow() + 1
        self.session.query(Client).filter(Client.id == client_id).delete()
        self.session.query(Event).filter(Event.client_id == client_id).delete()
        for number, client in enumerate(self.session.query(Client).all()):
            client.id = number + 1
        self.session.commit()
        self.loading(self.mode)

    def delete_paint(self):
        paint_id = self.table.currentRow() + 1
        self.session.query(Paint).filter(Paint.id == paint_id).delete()
        self.session.commit()
        self.loading(self.mode)

    def load_current_client(self, client_id):
        client = self.session.query(Client).filter(Client.id == client_id).first()
        self.setWindowTitle("a.beauty / " + client.name_surname)

        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Дата", "Краситель", "Примечания", ])
        self.table.setRowCount(0)

        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 125)
        self.table.setColumnWidth(2, 300)

        for row, event in enumerate(client.events):
            self.table.setRowCount(self.table.rowCount() + 1)
            for col, item in enumerate((event.created_date, event.paint_id, event.note)):
                if col == 1:
                    item = self.session.query(Paint).filter(Paint.id == item).first()
                    item = item.title if item else 'Краситель удален'
                self.table.setItem(row, col, QTableWidgetItem(str(item)))
                self.table.setRowHeight(row, 50)

    def loading(self, mode):
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Назваине красителя", ] if mode == 'p'
                                             else ["Имя Фамилия клиента", ])
        self.table.setRowCount(0)

        for number, item in enumerate(self.session.query(Paint if mode == 'p' else Client).all()):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(number, 0, QTableWidgetItem(item.title if mode == 'p'
                                                           else item.name_surname))
        self.table.setColumnWidth(0, 570)


app = QApplication(sys.argv)
ex = MainW()
ex.show()
sys.exit(app.exec_())
