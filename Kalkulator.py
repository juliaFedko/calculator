import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout, QHBoxLayout, QStyleFactory


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setLayout(QVBoxLayout())

        self.fields()
        self.keypad()
        self.show()

    def fields(self):
        fields = QWidget()
        fields.setLayout(QHBoxLayout())

        self.textbox = QLineEdit("")

        fields.layout().addWidget(self.textbox)

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
        self.divd = QPushButton("/")
        self.equt = QPushButton("=")
        self.back = QPushButton("Delete")

        self.b0.clicked.connect(self.b0_click)
        self.b1.clicked.connect(self.b1_click)
        self.b2.clicked.connect(self.b2_click)
        self.b3.clicked.connect(self.b3_click)
        self.b4.clicked.connect(self.b4_click)
        self.b5.clicked.connect(self.b5_click)
        self.b6.clicked.connect(self.b6_click)
        self.b7.clicked.connect(self.b7_click)
        self.b8.clicked.connect(self.b8_click)
        self.b9.clicked.connect(self.b9_click)
        self.plus.clicked.connect(self.plus_click)
        self.minus.clicked.connect(self.minus_click)
        self.mult.clicked.connect(self.mult_click)
        self.divd.clicked.connect(self.divd_click)
        self.equt.clicked.connect(self.equt_click)
        self.back.clicked.connect(self.back_click)

        keypad.layout().addWidget(self.b0, 3, 0)
        keypad.layout().addWidget(self.b1, 0, 0)
        keypad.layout().addWidget(self.b2, 0, 1)
        keypad.layout().addWidget(self.b3, 0, 2)
        keypad.layout().addWidget(self.b4, 1, 0)
        keypad.layout().addWidget(self.b5, 1, 1)
        keypad.layout().addWidget(self.b6, 1, 2)
        keypad.layout().addWidget(self.b7, 2, 0)
        keypad.layout().addWidget(self.b8, 2, 1)
        keypad.layout().addWidget(self.b9, 2, 2)
        keypad.layout().addWidget(self.plus, 1, 3)
        keypad.layout().addWidget(self.minus, 2, 3)
        keypad.layout().addWidget(self.mult, 3, 2)
        keypad.layout().addWidget(self.divd, 3, 1)
        keypad.layout().addWidget(self.equt, 3, 3)
        keypad.layout().addWidget(self.back, 0, 3)

        self.layout().addWidget(keypad)

    def b0_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "0")

    def b1_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "1")

    def b2_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "2")

    def b3_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "3")

    def b4_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "4")

    def b5_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "5")

    def b6_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "6")

    def b7_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "7")

    def b8_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "8")

    def b9_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + "9")

    def plus_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + " + ")

    def minus_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + " - ")

    def mult_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + " * ")

    def divd_click(self):
        text = self.textbox.text()
        self.textbox.setText(text + " / ")

    def equt_click(self):
        equation = self.textbox.text()
        try:
            ans = eval(equation)
            self.textbox.setText(str(ans))
        except:
            self.textbox.setText("Wrong Input")

    def back_click(self):
        text = self.textbox.text()
        text = text[:len(text) - 1]
        self.textbox.setText(str(text))



App = QApplication(sys.argv)
calculator = Calculator()
App.setStyle(QStyleFactory.create("Fusion"))
sys.exit(App.exec())
