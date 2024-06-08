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
        
        self.lineEdit.returnPressed.connect(self.my_slot)
        
        self.show()
    
    def my_slot(self):
        c_txt = self.lineEdit.text()
        self.label.setText(c_txt)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MWWindow()
    sys.exit(app.exec())