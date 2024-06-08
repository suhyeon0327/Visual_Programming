import sys

from PySide6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QGridLayout, QSizePolicy,
                             QLineEdit, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QVBoxLayout and QSizePolicy")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QGridLayout()
        lm.setSpacing(1) # 수직, 수평 여백을 1px로

        self.label0 = QLabel('0,0')
        self.label0.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label0.setStyleSheet("background-color: red")
        self.label0.setFont(QFont("Arial",20))
        lm.addWidget(self.label0, 0, 0)

        self.label1 = QLabel('0,1')
        self.label1.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label1.setStyleSheet("background-color: blue")
        self.label1.setFont(QFont("Arial",20))
        lm.addWidget(self.label1, 0, 1)

        self.label2 = QLabel('0,2')
        self.label2.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label2.setStyleSheet("background-color: pink")
        self.label2.setFont(QFont("Arial",20))
        lm.addWidget(self.label2, 0, 2)

        self.label3 = QLabel('1,0')
        self.label3.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label3.setStyleSheet("background-color: white")
        self.label3.setFont(QFont("Arial",20))
        lm.addWidget(self.label3, 1, 0, 1, 3)

        self.label4 = QLabel('2,1')
        self.label4.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label4.setStyleSheet("background-color: yellow")
        self.label4.setFont(QFont("Arial",20))
        lm.addWidget(self.label4, 2, 1, 1, 2)

        # contents margin설정.
        lm.setContentsMargins(30,30,30,30)

        self.setLayout(lm)

    def print_qsize(self):

        print('==============================')
        print("label0's ideal size (=sizeHint)     :",self.label0.sizeHint())
        print("label1's ideal size (=sizeHint)     :",self.label1.sizeHint())
        print("label2's ideal size (=sizeHint)     :",self.label2.sizeHint())
        print("label3's ideal size (=sizeHint)     :",self.label3.sizeHint())
        print("label4's ideal size (=sizeHint)     :",self.label4.sizeHint())
        print('==============================')
        print("label0's size      :", self.label0.size()     , "/",
                     self.label0.sizePolicy().verticalPolicy(),"/",
                     self.label0.sizePolicy().horizontalPolicy())
        print("label1's size      :",self.label1.size()     ,"/",
                      self.label1.sizePolicy().verticalPolicy(),"/",
                      self.label1.sizePolicy().horizontalPolicy())
        print("label2's size      :",self.label2.size()     ,"/",
                      self.label2.sizePolicy().verticalPolicy(),"/",
                      self.label2.sizePolicy().horizontalPolicy())
        print("label3's size      :",self.label3.size()     ,"/",
                      self.label3.sizePolicy().verticalPolicy(),"/",
                      self.label3.sizePolicy().horizontalPolicy())
        print("label4's size      :",self.label4.size()     ,"/",
                      self.label4.sizePolicy().verticalPolicy(),"/",
                      self.label4.sizePolicy().horizontalPolicy())