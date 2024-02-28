import sys
from datetime import timedelta

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Rezerwacja pokoju")
        self.show()
        self.room_types = {
            "Ekologiczny": "Pokoj bez dachu brak toalety do dyspozyycji metalowe wiadro",
            "Harry Potter": "pokij na miotly",
            "Programistyczny": "Piwnica bez okien",
            "Krolewski": "Pokoj bez wad"
        }
        self.room_price = {
            "Ekologiczny": 100,
            "Harry Potter": 250,
            "Programistyczny": 500,
            "Krolewski": 1000
        }
        self.ui.typeofroom.currentIndexChanged.connect(self.type_description)
        self.type_description()
        self.ui.rezerwacja.clicked.connect(self.reserve_room)

    def type_description(self):
        text = self.ui.typeofroom.currentText()
        if text in self.room_types:
            self.ui.description.setText(self.room_types[text])
        else:
            self.ui.description.setText("")

    def reserve_room(self):
        type = self.ui.typeofroom.currentText()
        price = 0
        if type in self.room_price:
            price = self.room_price[type]
        total_price = price * int(self.ui.days.text())
        start_date = self.ui.calendar.selectedDate().toPyDate()
        end_date = start_date + timedelta(days=int(self.ui.days.text()))
        message = f"Zarejestrowano pokoj {type}: {start_date} - {end_date} cena: {total_price}"
        box = QMessageBox()
        box.setText(message)
        box.setWindowTitle("message")
        box.show()
        box.exec()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.setWindowTitle('Pracownicy')
    window.show()
    sys.exit(app.exec())
