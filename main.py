import sys

from PyQt6.QtWidgets import QDialog, QApplication

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
        self.ui.typeofroom.currentIndexChanged.connect(self.type_description)

    def type_description(self):
        text = self.ui.typeofroom.currentText()
        if text in self.room_types:
            self.ui.description.setText(self.room_types[text])
        else:
            self.ui.description.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.setWindowTitle('Pracownicy')
    window.show()
    sys.exit(app.exec())
