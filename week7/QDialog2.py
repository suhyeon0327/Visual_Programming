import sys # 무조건 필요. sys.exit 때문에 필요
from PySide6.QtWidgets import ( QApplication,
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QMessageBox
)

class CustomDlg(QDialog): # class 선언 헤더
    def __init__(self, parent=None): # super class를 override하여 생성자 생성
        super().__init__(parent) # super class를 ~~하여 parent를 할당

        self.setWindowTitle('Hello, QDialog') # window title

        # button 설정
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel # OK와(int형)와 Cancel(int형) 버튼을 만들고 이들은 비트 연산(or)으로 사용됨
        # buttons에 해당하는 button객체
        self.button_box = QDialogButtonBox(buttons) # self: QDialogButtonBox # argument인 buttons을 통해 작동

        self.button_box.accepted.connect(self.accept) #QDialog의 메서드를 slot으로 # OK를 눌렀을 때
        self.button_box.rejected.connect(self.reject)    #QDialog의 메서드를 slot으로 # cancel을 눌렀을 때

        # layout manager 이용
        self.layout = QVBoxLayout() # layout 생성
        message = QLabel('Is something ok?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box) # QDialogButtonBox객체 추가.
        self.setLayout(self.layout)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__() # super class로 QMainWindow를 초기화
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked) # click이라는 signal을 button_clicked라는 slot에 연결
        
        self.setCentralWidget(button)

    def button_clicked(self, s):
        # print("click", s)
        # dlg = QDialog(self) # QDialog의 크기를 키우고 움직여도 main Widget의 중간에만 생성됨
        # # dlg = QDialog() # main widget과 상관없이 화면에 생김
        # dlg.setWindowTitle("QDialog Title") # QDialog Title 지정
        # dlg.exec() # event loop, modal dialog의 특징 # 없으면 안생김(modal dialog에 반드시 있어야 함)
        # -------------
        # for custom dlg
        # dlg = CustomDlg(self)
        # if dlg.exec(): # Modal Dialog
        #     print('ok')
        # else:
        #     print("cancel")
        
        # ------------------------
        # QMessage.information
        # result = QMessageBox.information( # 보통은 result로 안받고 사용
        #     self,
        #     'Message',
        #     'This is an information message.'
        # )
        # print(f'QMessage.information : {result}')
        
        # ------------------------
        # QMessage.about
        # QMessageBox.about(
        #      self,              # parent
        #      "About This SW",   # title of about dialog.
        #      """<p>The example of QMessageBox</p>
        #      <p>version 0.1</p>"""
        # )
        
        # ------------------------
        # QMessage.information
        # QMessageBox.warning( # 보통은 result로 안받고 사용
        #     self,
        #     'Message',
        #     'This is an information message.'
        # )
        
        
        ans = QMessageBox.question(
          self,                 # parent
          "title of question",  # 질문 제목
          "cotent of question", # 질문 내용.
          QMessageBox.StandardButton.No | # \ 코드가 너무 길어서 한줄이라는 의미
          QMessageBox.StandardButton.Yes, # responses
          QMessageBox.StandardButton.Yes, # default response
        )
        print(f'{ans=}')
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec() # event loop
    # event loop는 하나만 존재. 버튼을 클릭하면 dlg.exec()가 동작 끄면 app.exec()가 동작