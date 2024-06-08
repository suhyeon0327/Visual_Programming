import sys

from PySide6.QtWidgets import (
    QApplication, # event loop, 한개만 가질 수 있음
    QMainWindow, # 보통 하나
    QProgressBar, 
    QPushButton,
    QWidget, QVBoxLayout,
)
from PySide6.QtCore import QTimer 
# QTimer: 어떤 interval 간격으로 time out 시그널을 보냄
# 정해진 시간에 time out signal을 보냄, slot을 연결하면 time out이 될때마다 동작

class MW(QMainWindow):

    def __init__(self): # self가 첫번째 파라미터일때: instance 메소드
        super(MW, self).__init__() # MainWindow가 가지고 있는 기능들을 재사용, overriding 시킴, super()안에 self만 적어도 가능
        self.setWindowTitle("ex: QProgressBar")
        self.setGeometry(200, 200, 300, 150)

        self.progressBar = QProgressBar(self, minimum=9, maximum=20)
        self.progressValue = self.progressBar.minimum() # 초기화
        # self.progressBar.setGeometry(50, 50, 200, 30) # 생략가능

        self.startButton = QPushButton("start", self)
        # self.startButton.setGeometry(100, 100, 100, 30) # 생략가능
        self.startButton.clicked.connect(self.startProgress)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress) # self.timeout으로 쓰면 local 스코프로 생성됨, 이러면 지속되지 않고 사라짐

        lm = QVBoxLayout()
        lm.addWidget(self.progressBar)
        lm.addWidget(self.startButton)

        tmp = QWidget()
        tmp.setLayout(lm)

        self.setCentralWidget(tmp)
        self.show()

    def startProgress(self):
        self.progressBar.reset()
        # self.progressValue = self.progressBar.value() # getter, camel 네이밍
        self.progressValue = 0 # 최소값보다 작은 값을 입력하면 시간이 지난후 작동
        self.startButton.setEnabled(False) # start 버튼이 disable됨
        # self.progressBar.setValue(self.progressValue)
        self.timer.start(100)  # 100 milliseconds마다 타이머 발생, stop하기 전까지 타이머는 죽지 않음, 환경에 따라 시간이 정확하지 않을 수 있음

    def updateProgress(self):
        self.progressValue += 1 # 하나씩 증가
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= self.progressBar.maximum():
            self.timer.stop() # 타이머 정지
            self.progressBar.reset() # reset을 하지 않으면 다 채워져 있는 상태
            self.startButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())