from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

import sys
import os

class main_wnd (QWidget):
    
    def __init__(self):
        super().__init__()
        
        # Main Wnd의 크기 등을 설정
        self.setGeometry(100,200,600,300)
        # self.setFixedSize(600,300)
        
        self.ds_set_mwd()
        
        self.show()
    
    def ds_set_mwd(self):
        # Main Wnd에 포함되는 Widgets을 생성 및 추가
        label0=QLabel('Hello, World!',self)
        label0.setFont(QFont('Arial',20))
        label0.setStyleSheet('background-color: red')
        label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label0.move(30,30)
        
        self.ds_set_label1()
        
    def ds_set_label1(self):
        
        label1 = QLabel(self)
        
        fstr = os.path.realpath(__file__)
        pstr = os.path.dirname(fstr)
        istr = os.path.join(pstr, './week4/img/sun.png')
        
        print(istr)
        pixmap=QPixmap(istr)
        
        # label.setPixamap.QPixmap('./Visual Programming/sun.png')
        pixmap = QPixmap('./week4/img/sun.png')
        pixmap = pixmap.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio)
        label1.setPixmap(pixmap)
        label1.setScaledContents(True)
        
        label1.move(120,120)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 내가 만든 Qt 관련 main window 인스턴스를 만들어줘야한다.
    mw = main_wnd()
    
    sys.exit(app.exec())