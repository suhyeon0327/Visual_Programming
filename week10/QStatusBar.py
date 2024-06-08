import sys, os
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QStatusBar,
    QLabel,
    QProgressBar,
    QPushButton,
)

from PySide6.QtCore import QTimer

class MW(QMainWindow):

    def __init__(self):

        super(MW, self).__init__()   # super() 안에 self만 넣어줘도 되지만 (MW, self)로 쓰는 것이 원칙

        # set status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # set timer to display time by permanent widget
        self.timer0 = QTimer(self)
        self.timer0.timeout.connect(self.update_clk)   # 시계를 업데이트 해주는 widget과 연결
        self.timer0.start(1000) # 1 sec

        # permanent widget: clock
        self.clk_label = QLabel()
        self.status_bar.addPermanentWidget(self.clk_label)

        # temporary widget: progressbar
        self.progress_bar = QProgressBar(self, minimum=0, maximum =100)
        self.status_bar.addWidget(self.progress_bar, 1)   # 숫자 바꿔서 확인해보기

        # start button for progressbar
        self.btn = QPushButton('Start Progress!')
        self.btn.clicked.connect(self.start_progress)   # 시간에 따라 ProgressBar가 업데이트 되도록 함
        self.setCentralWidget(self.btn)

        # timer for progressbar
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_progress)
        self.progress_value = 0

        self.show()

    def start_progress(self):
        self.progress_value = 0
        self.progress_bar.reset()
        self.progress_bar.setValue(self.progress_value)
        self.timer1.start(100)
        self.status_bar.showMessage('Progress started...', 2000)

    def update_clk(self):
        now = datetime.now()
        now_str = now.strftime('%H:%M:%S')   # string formatting time 시간을 스트링으로 나타냄
        self.clk_label.setText(now_str)

        # current_time = QTime.currentTime()

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer1.stop()
            self.status_bar.showMessage('Progress completed...', 2000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())