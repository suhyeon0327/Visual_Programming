import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QVBoxLayout, 
                               QSlider)
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        # main window 관련 설정.
        self.setWindowTitle("QSlider Ex.")
        self.setGeometry(100, 100, 300, 200)

        # central widget 생성
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # vertical box layout 생성
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QSlider 생성 및 설정
        # slider = QSlider(Qt.Horizontal)
        slider = QSlider(Qt.Vertical)

        slider.setMinimum(0)
        slider.setMaximum(255)
        slider.setValue(0)
        slider.setTickInterval(10)  # 간격을 10으로 설정
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setSingleStep(1)  # 값이 한 번에 변경되는 단위를 1로 설정
        slider.setPageStep(10)  # 키보드로 이동할 때 한 번에 이동하는 페이지 크기를 10으로 설정


        # QSlider 인스턴스 값 변경 시 이벤트 처리
        slider.valueChanged.connect(self.on_change_bg_color)

        # layout manager에 QSlider 인스턴스 추가
        layout.addWidget(slider)

    def on_change_bg_color(self, value):
        # MW의 central widget의 배경색을 바꿈.
        self.centralWidget().setStyleSheet(f"background-color: rgb({value}, {value}, {value});")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MW()
    sys.exit(app.exec())