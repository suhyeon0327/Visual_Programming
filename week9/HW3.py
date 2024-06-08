import sys
import psutil

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

from PySide6.QtCore import QTimer

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

matplotlib.use('QtAgg')

class MyCanvas(FigureCanvasQTAgg):   # FigureCanvasQTAgg을 상속받는 MyCanvas 클래스 생성

    def __init__(self, parent=None, figsize =(5,5), dpi=100):   # 초깃값으로 가로 5인치, 세로 5인치, dpi 100으로 설정
        
        # 1행 2열을 가지는 figure 생성
        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)   # MyCanvas를 상속받아 fig 생성

class MW(QMainWindow):   # QMainWindow를 상속받는 MW 클래스 생성

    def __init__(self):   # 초깃값 설정

        super().__init__()   # 부모클래스의 생성자 호출
        self.setWindowTitle('cpu usage & ram usage')   # 위젯의 제목을 'cpu usage & ram usage'로 설정

        self.plt_canvas = MyCanvas(self, (5,10), 100)   # plt.canvas에 가로 5인치, 세로 10인치, dpi 100으로 설정
        
        n_data = 10
        interval_ms = 10   # 10 miliseconds
        self.x_cpu = list(range(n_data))   # 10개의 리스트로 생성
        self.x_ram = list(range(n_data)) # 10개의 리스트로 생성
        self.y_cpu = [0] * 10   # 0으로 초기화된 길이가 10인 리스트 생성
        self.y_ram = [0] * 10   # 0으로 초기화된 길이가 10인 리스트 생성
         
        self.old_plot_ref1 = None   # old_plot_ref1을 생성, 초깃값은 None
        self.update_plot_cpu()   # update_plot_cpu 호출
        self.old_plot_ref2 = None   # old_plot_ref1을 생성, 초깃값은 None
        self.update_plot_ram()   # update_plot_ram 호출

        self.setCentralWidget(self.plt_canvas)   # 중앙 위젯 설정
        self.show()   # 화면에 보여주기

        # cpu usage 타이머 설정
        self.timer0 = QTimer()   # 타이머 생성
        self.timer0.setInterval(interval_ms) # 간격을 10 milliseconds로 설정
        self.timer0.timeout.connect(self.update_plot_cpu)   # timeout 시그널이 생성될때마다 update_plot_cpu 실행
        self.timer0.start()   # 타이머 시작

        # ram usage 타이머 설정
        self.timer1 = QTimer()   # 타이머 생성
        self.timer1.setInterval(interval_ms) # 간격을 10 milliseconds로 설정
        self.timer1.timeout.connect(self.update_plot_ram)   # timeout 시그널이 생성될때마다 update_plot_ram 실행
        self.timer1.start()   # 타이머 시작

    # cpu usage 그래프 나타내기
    def update_plot_cpu(self):
        self.y_cpu = [ *self.y_cpu[1:], psutil.cpu_percent(interval=1)]   # cpu usage 데이터 생성
        cpu_usage = psutil.cpu_percent(interval=1)   # cpu usage을 cpu_usage에 저장
        print(f"cpu usage: {cpu_usage}%")   # cpu usage 출력
        
        if self.old_plot_ref1 is not None:   # self.old_plot_ref1가 None이 아니면
            self.old_plot_ref1.set_ydata(self.y_cpu)   # 그래프의 y축 데이터 업데이트
        else:   # self.old_plot_ref1가 None이면
            self.old_plot_ref1 = self.plt_canvas.axes[0].plot(
                self.x_cpu, self.y_cpu
            )[0]   # cpu usage 그래프 생성
            self.plt_canvas.axes[0].grid()   # 그래프에 그리드 생성
            self.plt_canvas.axes[0].set_title('cpu usage (%)')   # 그래프 제목을 'cpu usage (%)'으로 설정
        self.plt_canvas.draw()

    # ram usage 그래프 나타내기
    def update_plot_ram(self):
        self.y_ram = [ *self.y_ram[1:], psutil.virtual_memory().percent]   # ram usage 데이터 생성
        ram_usage = psutil.virtual_memory()   # ram usage을 ram_usage에 저장
        print(f"ram usage: {ram_usage.percent}%")   # ram usage 출력
        
        if self.old_plot_ref2 is not None:   # self.old_plot_ref2가 None이 아니면
            self.old_plot_ref2.set_ydata(self.y_ram)   # 그래프의 y축 데이터 업데이트
        else:   # self.old_plot_ref2가 None이면
            self.old_plot_ref2 = self.plt_canvas.axes[1].plot(
                self.x_ram, self.y_ram
            )[0]   # ram usage 그래프 생성
            self.plt_canvas.axes[1].grid()   # 그래프에 그리드 생성
            self.plt_canvas.axes[1].set_title('ram usage (%)')   # 그래프 제목을 'ram usage (%)'으로 설정
        self.plt_canvas.draw()

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())