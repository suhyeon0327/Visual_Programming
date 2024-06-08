import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget)
from PySide6.QtCore import Qt

class MW(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100,100,400,400)
        self.setWindowTitle('Event Handling Ex.')
        
        self.set_main_wnd()
        self.show()
        
    def set_main_wnd(self):
        label = QLabel(
        """<p>Press the <b>ESC</b> key
        to quit this program.</p>"""
        )
        self.setCentralWidget(label)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        # super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Escape:
            print('ESC Key Pressed')
            self.close()
        if event.key() == Qt.Key.Key_A:
            self.subwindow = subwindow()
            self.subwindow.show()
            
class subwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setGeometry(200,200,600,600)
        self.setWindowTitle('Event Handling Ex.')
        
        self.set_main_wnd()
        
    def keyPressEvent(self, event):    
        if event.key() == Qt.Key.Key_Q:
            self.close()
        
    def set_main_wnd(self):
        label = QLabel('a')
        self.setCentralWidget(label)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MW()
    sys.exit(app.exec())