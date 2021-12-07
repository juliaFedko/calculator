import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout, QHBoxLayout, \
    QLabel, QStyleFactory


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setLayout(QVBoxLayout())

        self.fields()
        self.keypad()
        self.show()

        self.a_list = []
        self.b_list = []


        self.a = 0
        self.sign = "+"
        self.b = 0
        self.c = 0

        self.b0.clicked.connect(self.button_click)

    def button_click(self):
        current_1text = self.first_num.text()
        current_2text = self.first_num.text()
        current_sign = self.sign.title()
        print('Przycisk zostal nacisniety')
        if current_sign == "":
            self.first_num.setText("0")
        else:
            self.second_num.setText("0")

    def fields(self):
        fields = QWidget()
        fields.setLayout(QHBoxLayout())

        self.first_num = QLineEdit("")
        self.sign = QLineEdit("___")
        self.second_num = QLineEdit("")
        self.equal_to = QLabel("  =  ")
        self.result = QLabel("")

        fields.layout().addWidget(self.first_num)
        fields.layout().addWidget(self.sign)
        fields.layout().addWidget(self.second_num)
        fields.layout().addWidget(self.equal_to)
        fields.layout().addWidget(self.result)

        self.layout().addWidget(fields)

    def keypad(self):
        keypad = QWidget()
        keypad.setLayout(QGridLayout())

        self.b0 = QPushButton("0")
        self.b1 = QPushButton("1")
        self.b2 = QPushButton("2")
        self.b3 = QPushButton("3")
        self.b4 = QPushButton("4")
        self.b5 = QPushButton("5")
        self.b6 = QPushButton("6")
        self.b7 = QPushButton("7")
        self.b8 = QPushButton("8")
        self.b9 = QPushButton("9")
        self.plus = QPushButton("+")
        self.minus = QPushButton("-")
        self.mult = QPushButton("*")
        self.divd = QPushButton("÷")
        self.equt = QPushButton("=")

        keypad.layout().addWidget(self.b0, 0, 0)
        keypad.layout().addWidget(self.b1, 0, 1)
        keypad.layout().addWidget(self.b2, 0, 2)
        keypad.layout().addWidget(self.b3, 0, 3)
        keypad.layout().addWidget(self.b4, 0, 4)
        keypad.layout().addWidget(self.b5, 1, 0)
        keypad.layout().addWidget(self.b6, 1, 1)
        keypad.layout().addWidget(self.b7, 1, 2)
        keypad.layout().addWidget(self.b8, 1, 3)
        keypad.layout().addWidget(self.b9, 1, 4)
        keypad.layout().addWidget(self.plus, 2, 0)
        keypad.layout().addWidget(self.minus, 2, 1)
        keypad.layout().addWidget(self.mult, 2, 2)
        keypad.layout().addWidget(self.divd, 2, 3)
        keypad.layout().addWidget(self.equt, 2, 4)

        self.layout().addWidget(keypad)


app = QApplication(sys.argv)
calculator = Calculator()
app.setStyle(QStyleFactory.create("Fusion"))
app.exec_()
