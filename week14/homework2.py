import sys, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.image import imread
import matplotlib.image as mpimg

from PySide6.QtWidgets import (
        QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QListWidget,
        QWidget, QPushButton, QFileDialog, QMessageBox, QStatusBar, QListWidgetItem
        )
from PySide6.QtGui import QAction, QKeyEvent, QPixmap
from PySide6.QtCore import Qt, Signal, QSize

class InteractivePlot(QMainWindow):
    
    change_file = Signal(int)
    
    def __init__(self):
        super().__init__()
        
        self.path = os.path.dirname(
            os.path.abspath(__file__)
        )
        
        # self.idx = 0
        self.change_file.connect(self.change_file_handler)
        
        # 창의 기본 설정: 그래프 영역, 캔버스, 그리기 도구 및 버튼 초기화
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')  # 축을 초기에 비활성화하여 이미지만 표시

        # 메뉴바 생성
        self.load_act = QAction("Directory")
        self.load_act.setShortcut("Ctrl+D")
        self.load_act.triggered.connect(self.open_directory)
        self.create_menu()
        
        # 상태바 생성
        self.statusbar = QStatusBar()   # Qstatusbar 생성
        self.setStatusBar(self.statusbar)   # 상태표시줄로 설정
        
        # NavigationToolbar 생성
        self.toolkit = NavigationToolbar(self.canvas, self)

        # QListWidget 생성
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        
        # 메인 위젯 및 레이아웃 설정
        layout = QHBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.list_widget)
        
        right_layout = QVBoxLayout()
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        right_layout.addWidget(self.toolkit)
        right_layout.addWidget(self.canvas)
        
        layout.addWidget(right_widget)
        
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
    
    def create_menu(self):
        # 어플리케이션의 menu bar를 만드는 method.
        mb = self.menuBar()
        menu_item = mb.addMenu("Select")
        menu_item.addAction(self.load_act)
    
    def open_directory(self):
        # 디렉토리 선택 다이얼로그 열기
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.list_widget.clear()
            # 디렉토리의 png 파일 목록 가져오기
            png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
            for png_file in png_files:
                item = QListWidgetItem(png_file)
                item.setData(Qt.UserRole, os.path.join(directory, png_file))
                self.list_widget.addItem(item)
    
    def on_item_clicked(self, item):
        # 선택된 아이템의 파일 경로를 가져와서 이미지 표시
        file_path = item.data(Qt.UserRole)
        self.image = imread(file_path)
        self.ax.clear()
        self.ax.imshow(self.image)
        self.ax.axis('off')
        self.canvas.draw()
        self.statusbar.showMessage(file_path)
    
    def tool_active(self):
        return self.toolkit.mode == 'zoom rect' or self.toolkit.mode == 'pan/zoom'
        
    def on_click(self, event):
        if self.image is None:
            return
        if self.tool_active():
            return
        else:
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
        if self.tool_active():
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

    def on_item_clicked(self, item):
        # 선택된 아이템의 파일 경로를 가져와서 이미지 표시
        file_path = item.data(Qt.UserRole)
        self.image = imread(file_path)
        self.ax.clear()
        self.ax.imshow(self.image)
        self.ax.axis('off')
        self.canvas.draw()
        self.statusbar.showMessage(file_path)
    
    def keyPressEvent(self, event: QKeyEvent, item):
        
        dic = {}
        directory_path = item.data(Qt.UserRole)
        files = os.listdir(directory_path)
        idx = len(files)
        for key, value in zip(files, idx):
            dic[key] = value
        
        # 3번 custom signal을 발생해야하는 부분에 emit메서드 호출.
        if event.key() == Qt.Key.Key_Right:
            self.change_file.emit(1)
        elif event.key() == Qt.Key.Key_Left:
            self.change_file.emit(-1)

        return super().keyPressEvent(event) 

    def change_file_handler(self):
        pixmap = QPixmap(f"{Qt.UserRole}/img/{self.idx}.png")
        self.img_label.setPixmap(pixmap.scaled(
            QSize(180,250),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = InteractivePlot()
    mwd.show()
    sys.exit(app.exec())