import sys # 무조건 필요. sys.exit 때문에 필요
from PySide6.QtWidgets import ( QApplication,
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QWidget
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
        
        layout = QVBoxLayout() # layout 생성
        
        button1 = QPushButton("QMessageBox.simple")
        layout.addWidget(button1)
        button1.clicked.connect(self.button1_clicked)
        
        button2 = QPushButton("QMessageBox.CustomDlg")
        layout.addWidget(button2)
        button2.clicked.connect(self.button2_clicked)
        
        button3 = QPushButton("QMessageBox.information")
        layout.addWidget(button3)
        button3.clicked.connect(self.button3_clicked)
        
        button4 = QPushButton("QMessageBox.about")
        layout.addWidget(button4)
        button4.clicked.connect(self.button4_clicked)
        
        button5 = QPushButton("QMessageBox.question")
        layout.addWidget(button5)
        button5.clicked.connect(self.button5_clicked)
        
        button6 = QPushButton("QMessageBox.critical")
        layout.addWidget(button6)
        button6.clicked.connect(self.button6_clicked)
        
        button7 = QPushButton("QMessageBox.warning")
        layout.addWidget(button7)
        button7.clicked.connect(self.button7_clicked)

        dummy = QWidget()
        dummy.setLayout(layout)
        
        self.setCentralWidget(dummy)
    
    def button1_clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog Title")
        dlg.exec()
            
    def button2_clicked(self):
        dlg = CustomDlg(self)
        if dlg.exec(): # Modal Dialog
            print('ok')
        else:
            print("cancel")
        
    def button3_clicked(self):
        QMessageBox.information(
            self,
            'Message',
            'This is an information message.'
        )
        
    def button4_clicked(self):
        QMessageBox.about(
             self,              # parent
             "About This SW",   # title of about dialog.
             """<p>The example of QMessageBox</p>
             <p>version 0.1</p>"""
        )
    
    def button5_clicked(self):
        QMessageBox.question(
        self,                 # parent
        "title of question",  # 질문 제목
        "cotent of question", # 질문 내용.
        QMessageBox.StandardButton.No | # \ 코드가 너무 길어서 한줄이라는 의미
        QMessageBox.StandardButton.Yes, # responses
        QMessageBox.StandardButton.Yes, # default response
        )
    
    def button6_clicked(self):
        QMessageBox.warning(
            self,
            'Message',
            'This is an information message.'
        )
        
    def button7_clicked(self):
        QMessageBox.warning(
            self,
            'Message',
            'This is an information message.'
        )
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec() # event loop
    # event loop는 하나만 존재. 버튼을 클릭하면 dlg.exec()가 동작 끄면 app.exec()가 동작