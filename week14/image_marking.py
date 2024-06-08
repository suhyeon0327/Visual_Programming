import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.image import imread

from PySide6.QtWidgets import (
        QApplication, QMainWindow, QVBoxLayout, 
        QWidget, QPushButton, QFileDialog, QMessageBox
        )

class InteractivePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        # 창의 기본 설정: 그래프 영역, 캔버스, 그리기 도구 및 버튼 초기화
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')  # 축을 초기에 비활성화하여 이미지만 표시

        # 이미지 로드 버튼 설정 및 클릭 이벤트에 대한 연결 설정
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)

        # 메인 위젯 및 레이아웃 설정
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.canvas)
        layout.addWidget(self.load_button)

        # 마우스 드래그 상태 및 사각형 선택을 위한 변수 초기화
        self.dragging = False
        self.rect = None
        self.start_point = (0, 0)
        self.click_count = 0  # 클릭 횟수 카운트를 위한 변수
        self.image = None


        # 마우스 클릭 및 더블클릭 이벤트 연결
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)


    def load_image(self):
        # 사용자가 선택한 이미지 파일을 불러오고 캔버스에 표시
        file_name, _ = QFileDialog.getOpenFileName(self, 
                                                   "Open Image", 
                                                   "", 
                                                   "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.image = imread(file_name)
            print(type(self.image))
            self.ax.clear()
            self.ax.imshow(self.image)
            self.ax.axis('on')
            self.canvas.draw()

    def on_click(self, event):
        if self.image is None:
            return
        # 마우스 클릭 이벤트 핸들러: 더블클릭 검출을 위해 클릭 횟수 계산
        if event.button == 3:
            self.on_right_click(event)
        else:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.start_point = (event.xdata, event.ydata)
            self.rect = self.ax.add_patch(
                plt.Rectangle(self.
                              start_point, 
                              0, 0, 
                              fill=False, color='red')
                )
            self.canvas.draw()

    def on_right_click(self, event):
        if self.image is None:
            return
        #  우클릭 이벤트 핸들러: 클릭된 위치에 원을 그림
        if event.dblclick:
            self.ax.add_patch(
                plt.Circle(
                    (event.xdata, event.ydata), 
                    10, 
                    color='blue', fill=True)
                )
            self.canvas.draw()

    def on_drag(self, event):
        if self.image is None:
            return
        # 마우스 드래그 이벤트 핸들러: 사각형의 위치와 크기를 실시간으로 조정
        if not self.dragging or not event.inaxes:
            return
        if event.dblclick:
            return 
        x0, y0 = self.start_point
        x1, y1 = event.xdata, event.ydata
        self.rect.set_width(x1 - x0)
        self.rect.set_height(y1 - y0)
        self.rect.set_xy((min(x0, x1), min(y0, y1)))
        self.canvas.draw()

    def on_release(self, event):
        if self.image is None:
            return
        # 마우스 버튼 해제 이벤트 핸들러: 사용자가 사각형을 그린 후 마우스 버튼을 놓으면 호출됨.
        if event.button == 3: # 우클릭인 경우는 무시.
            return
        if self.dragging:
            self.dragging = False
            response = QMessageBox.question(self, 
                                            "Confirm", 
                                            "Keep the rectangle?", 
                                            QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.No:
                self.rect.remove()  # 사용자가 'No'를 선택했을 때 사각형 삭제
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = InteractivePlot()
    mwd.show()
    sys.exit(app.exec())