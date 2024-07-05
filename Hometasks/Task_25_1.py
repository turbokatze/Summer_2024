from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Clicker')
        self.button = QPushButton("Press \n") #перенос строки для будущей замены текста кнопки

        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.count = 0
        self.setFixedSize(QSize(200, 150))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print(self.count)
        self.count += 1
        self.setWindowTitle(f'Clicked {self.count} times!')
        # self.button.setText(f'Press \n Clicked {self.count} times!') #меняет название кнопки на число нажатий



app, window = QApplication([]), MainWindow(); window.show(); app.exec()
