import sys, os
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication
)
from homework import Ui_MainWindow   # homework_plus 파일의 Ui_MainWindow 클래스를 임포트

class MWWindow(QMainWindow, Ui_MainWindow): # 중복으로 상속.
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 반드시 호출
        self.show()   # 화면에 보여주기

# 애플리케이션 설정    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MWWindow()
    sys.exit(app.exec())