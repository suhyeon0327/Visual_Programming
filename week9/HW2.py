# 2. Enter키가 입력되는 경우, my_signal 이라는 커스텀 시그널이 발생하고
# 이를 연결한 slot을 통해 int값을 입력받는 modal dialog가 뜨는 code.

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QLabel, QVBoxLayout, QInputDialog)
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt, Signal

class MW(QMainWindow): # QMainWindow를 상속받는 MW 클래스 생성

    my_signal = Signal(int) # int를 사용하는 신호를 my_signal에 정의
    
    def __init__(self):   # 초깃값 설정
        super().__init__()   # 부모클래스의 생성자 호출
        self.init_ui()   # init_ui 함수 호출

    def init_ui(self):   # init_ui 함수 생성
        self.setGeometry(200, 200, 200, 200)   # 위젯을 x=200, y=200, width=200, height=200으로 설정
        self.setWindowTitle("Custom Signal")   # 위젯의 제목을 'Custom Signal'로 설정
        self.setup_main_wnd()   # setup_main_wnd 함수 호출
        self.show()   # 화면에 보여주기

    def setup_main_wnd(self):   # setup_main_wnd 함수 생성
        
        self.my_signal.connect(self.slot)   # my_signal을 slot에 연결
        
        lm = QVBoxLayout()   # 수직으로 레이아웃 생성

        label1 = QLabel("Press Enter key")   # 'Press Enter key'를 출력하는 Label1 생성
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)   # label1을 중앙에 배치
        lm.addWidget(label1)   # 레이아웃에 label1 추가
        
        self.label2 = QLabel()   # label2 생성
        lm.addWidget(self.label2)   # 레이아웃에 label2 추가

        container = QWidget()   # 컨테이너 생성
        container.setLayout(lm)   # 컨테이너의 layout manager를 lm으로 설정

        self.setCentralWidget(container)   # 추가한 위젯 표시


    def keyPressEvent(self, event: QKeyEvent):   # keyevent를 나태내는 keyPressEvent 함수 생성
        
        if event.key() == Qt.Key.Key_Return:   # 엔터키가 입력되는 경우
            self.my_signal.emit(1)   # custom signal을 발생해야하는 부분에 emit 메서드 호출
        
        return super().keyPressEvent(event)   # 상위클래스에 keyevent 반환
        
    def slot(self):   # slot 함수 생성
        # 사용자로부터 정수 입력을 받는 dialog 생성
        ret_int, is_ok = QInputDialog.getInt(
                    self,   # 부모 위젯
                    "Input Integer",   # dialog 제목
                    "Enter Your Int Value!",   # label 제목
                    0,   # 기본 text 값
                    0, 100,   # 최소값:0, 최대값 100
                    1   # 정수가 1씩 증감
                    )
        if is_ok:   # ok 버튼을 누르면
            self.label2.setText(f'{ret_int}')   # label2에 입력된 정수 출력
        
# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())