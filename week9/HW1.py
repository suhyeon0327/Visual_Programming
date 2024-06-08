# 1. Hello World 과 표시되면서, 
# 아래에 해당 main script의 디렉토리 경로를 출력하는 code.
import sys, os
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QVBoxLayout, QLabel, QWidget)


class MW(QMainWindow):   # QMainWindow를 상속받는 MW 클래스 생성
    def __init__(self):   # 초깃값 설정
        super().__init__()   # 부모클래스의 생성자 호출
        self.init_ui()   # init_ui 함수 호출
    
    def init_ui(self):   # init_ui 함수 생성
        
        lm = QVBoxLayout()   # 수직으로 레이아웃 생성
        
        self.setGeometry(200, 200, 300, 200)   # 위젯을 x=200, y=200, width=300, height=200으로 설정
        self.setWindowTitle("Hello World")   # 위젯의 제목을 'Hello World'로 설정
        
        label1 = QLabel("Hello World!")   # 'Hello World'를 출력하는 Label1 생성
        lm.addWidget(label1)   # 레이아웃에 label1 추가
        
        self.fstr = os.path.dirname(
            os.path.abspath(__file__)
        )   # 절대경로를 self.fstr에 저장
        print(self.fstr)   # 절대경로 출력
        
        label2 = QLabel(self.fstr)   # 절대경로를 출력하는 Label2 생성
        lm.addWidget(label2)   # 레이아웃에 label2 추가
        
        container = QWidget()   # 컨테이너 생성
        container.setLayout(lm)   # 컨테이너의 layout manager를 lm으로 설정

        self.setCentralWidget(container)   # 추가한 위젯 표시
        
        self.show()   # 화면에 보여주기

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())