#basic_window.py
#import necessary modules
import sys  #시스템에 관련된 패키지

PYSIDE = True #PYSIDE로 돌아가는지 다른(PyQt)로 돌아가는지에 따라 조금씩 달라지므로 표현
try:
   import PySide6.QtCore  #그림을 그리거나 아이콘을 그리는 것 들을 제외한 핵심 코어
   from PySide6.QtWidgets import (QApplication, QWidget, QLabel) #QtWidgets: 체크박스 등의 위젯을 구현하기 위한 제공?
# 또다른 QtGUI는 직접 그리는 것(Font등)

except:
   PYSIDE = False #False인 경우는 주로 설치가 되지 않았을 때

PYQT = True
try:
   import PySide6.QtCore  #그림을 그리거나 아이콘을 그리는 것 들을 제외한 핵심 코어
   from PySide6.Qtwidgets import (QApplication, QWidget, QLabel) #QtWidgets: 체크박스 등의 위젯을 구현하기 위한 제공?
# 또다른 QtGUI는 직접 그리는 것(Font등)
#PYSIDE와 PYQT 코드는 유사함

#super 클래스는 부모
except:
   PYQT = False #False인 경우는 주로 설치가 되지 않았을 때

class MW(QWidget): #MW의 부모는 QWIdget
   def __init__(self):  #__init__ 은 생성자, 객채가 만들어지면 자동으로 실행됨
      """ Constructor for Empty Window Class """
      super().__init__()
      self.initializeUI()
   def initializeUI(self): #window 창 셍성 과정
      """set up the application.""" 
      #여기서 self는 MW
      self.setGeometry(200,100,400,200) #window 창 설정
      #카멜(낙타) 타이핑-> 중요한 네이밍 규칙,첫 단어는 소문자
      self.setWindowTitle("Main Window in PyQt") 
      self.setup_main_wnd() #이건 카멜타이핑이 아닌 기본 제공 카멜 타이핑과 구분되기 위해서
      self.show() # Display the window on the screen #화면에 윈도우 창을 보임

   def setup_main_wnd(self):  # window 창의 기능을 설정
      """set up the main swindow.'"""
      # 여기서 self는 MW의 객체, 컨데이너 역할
      hello_label = QLabel(self) # self = MW
      hello_label.setText('Hello, World and Qt!')
      hello_label.move(150,90) #글씨 보여주기? 사이즈 조절?


# Run the program
if __name__ == '__main__': # gui나 프로그램을 수행할 때 반드시 써야 함

   if PYSIDE:
      print(PySide6.__version__)
      print(PySide6.QtCore.__version__)
   if PYQT:
      print(PyQt6.QtCore.qVersion())
   
   window = MW()

   app = QApplication(sys.argv) # 01 # 여기에 쓰면 오류가 뜸(쓰면 안됨)  #QApplication을 맨 위에서 수행하면 프로그램 실행?
   # app01 = QApplication(sys.argv) # QApplication은 프로그램에서 하나만 존재
   print(sys.argv)
   window = MW() #모든 GUI에는 window가 하나 # 02
   sys.exit(app.exec()) # 03 #종료하기 위한 반환 값이 입력되면 python 인터프리터 종료, 종료하기 위한 반환 값은 X표시 클릭 등의 이벤트가 일어나면 종료하는 값 반환
# 1 more line; before #4 1 second ago
   # ret_v = app.exec()
   # print(type(ret_v), ret_v)
   # sys.exit(ret_v)