# ================================================
# Import necessary modules.
import sys, os

from PySide6.QtWidgets import (QApplication, QWidget, 
                             QLabel, QPushButton)
from PySide6.QtGui import QFont,QIcon
from PySide6.QtCore import Qt,QSize

# ================================================
# 주요 클래스 정의
class MW(QWidget):    # main window 상속

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Set up the appliation's GUI"""
        self.setFixedSize(250,250) # 사이즈 250,250
        self.setWindowTitle('QPushButton Example')   # 제목
        self.setup_main_wnd()
        self.show() # main window는 보여주는 것이 일반적

    def setup_main_wnd(self):        # main window setting
        """Set up the Main Window"""
        # hello_label = QLabel('Hello, World and Qt!', self) # 아래 두 라인과 동일한 수행
        self.hello_label = QLabel(self)
        self.hello_label.setText('Hello, World and Qt!')
        self.hello_label.setFont(QFont('Arial',15))

        # 아래 두 줄을 주석해제하여 동작을 확인해 볼것.
        # hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        # hello_label.setStyleSheet("background-color: yellow")
        self.hello_label.move(10,20)

        # 이미지의 경로
        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'./img/sun.png')

        it_button = QPushButton("icon and text button",self)
        it_button.setIcon(QIcon(img_fstr))
        it_button.clicked.connect(self.it_btn_clicked) # signal slot의 핵심, 클릭했을 때 it_btn_clicked와 연결(ctrl + click)
        it_button.resize(150,50)
        it_button.move(50,70)

        # 텍스트는 없고 아이콘만 있음
        icon_button = QPushButton(self)
        icon_button.setIcon(QIcon(img_fstr))
        icon_button.clicked.connect(self.icon_btn_clicked)
        icon_button.setIconSize (QSize(120,30))
        icon_button.resize(150,50)
        icon_button.move(50,130)

        # 아이콘은 없고 텍스트만 있음
        text_button = QPushButton("icon button",self)
        text_button.clicked.connect(self.text_btn_clicked) 
        text_button.resize(150,50)
        text_button.move(50,190)

    # 클릭이 되면 label title을 바꿈
    def it_btn_clicked(self): # snake naming(내가 추가한 메소드)
        self.hello_label.setText("Icon and txt Button") # hello_label: 내가 만든 것, 최상단에 있는 라벨

    def icon_btn_clicked(self):
        self.hello_label.setText("Icon Button")

    def text_btn_clicked(self):
        self.hello_label.setText("text Button")


if __name__ == '__main__':         # 여기서 부터 3줄 항상 작성
    app = QApplication(sys.argv)   # QApplication 수행
    wnd = MW()
    sys.exit(app.exec())      # 반환값을 가지고 python을 종료