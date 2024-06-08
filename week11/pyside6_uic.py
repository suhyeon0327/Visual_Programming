import sys, os
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication
)
from output import Ui_MainWindow

class MWWindow(QMainWindow, Ui_MainWindow): # 중복으로 상속.
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 반드시 호출
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MWWindow()
    sys.exit(app.exec())