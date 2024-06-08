import sys
from PySide6.QtWidgets import (QApplication, QWidget,
                               QLabel, QGridLayout,
                               QMainWindow)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def  init_ui(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 500)
        self.setWindowTitle("QGridLayout Example")
        self.setup_mw()
        self.show()

    def  setup_mw(self):
        colors = ['white','gray','blue','red','yellow']
        labels = []
        for  i  in  range(5):
            label = QLabel(f"label {i}")
            label.setFont(QFont("Arial", 20))
            label.setStyleSheet(f"background-color:{colors[i]}")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            labels.append(label)

        # QGridLayout 설정.
        self.main_grid = QGridLayout()

        # 위치만 지정
        self.main_grid.addWidget(labels[0], 0, 0)       
        # 위치와 얼마나 차지할지 지정
        self.main_grid.addWidget(labels[1], 1, 0, 3, 3)

        # 차지하는 크기를 1,1로 지정시 생략한 것과 같음.
        self.main_grid.addWidget(labels[2], 4, 0, 2, 1)
        self.main_grid.addWidget(labels[3], 4, 1, 1, 2)
        self.main_grid.addWidget(labels[4], 5, 2)

        # main window의 Layout Manager로 설정.
        central_widget = QWidget()
        central_widget.setLayout(self.main_grid)
        self.setCentralWidget(central_widget)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MW()
    wd.main_grid.itemAtPosition
    sys.exit(app.exec())