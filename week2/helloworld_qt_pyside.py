import PySide6.QtCore
from PySide6.QtWidgets import (QWidget, 
                               QApplication, 
                               QLabel
                               )
import sys

class MW(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PyQt")
        # self.setup_main_wnd()
        
        # hello_label = QLabel(self)
        # hello_label.setText('Hello, World and Qt!')
        # hello_label.move(150,90)
        
        self.show()
        
if __name__ == "__main__":
    # Event Loop 등을 위한 QApplication instance 생성.
    app = QApplication(sys.argv)
    # main window 생성 및 show 호출.
    window = MW()
    # Event Loop 시작.
    sys.exit(app.exec())   # =sys.exit(0)