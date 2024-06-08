import sys # 무조건 필요. sys.exit 때문에 필요
from PySide6.QtWidgets import ( QApplication,
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QGridLayout,
    QPushButton,
    QMessageBox,
    QWidget,
    QGroupBox,
    QButtonGroup,
    QCheckBox,
    QVBoxLayout
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
        
        layout = QGridLayout() # layout 생성
        
        # radio button 생성
        self.checks = QGroupBox("QCheckBox Grp")
        self.checks.setCheckable(True)   # enable/disable check box 생성
        self.checks.setChecked(False)   # 초기값이 disable
        self.radios = QGroupBox("QRadioButton Grp")
        layout.addWidget(self.checks)
        layout.addWidget(self.radios)
        self.set_checks()
        
    def set_checks(self):
        
        layout = QGridLayout()
        
        # self.items = []
        # for idx in range(7):
        #     self.items.append(idx)
        
        self.button_grp_checks = QButtonGroup()
        for idx in range(7):
            cb = QCheckBox()
            self.button_grp_checks.addButton(cb)
            layout.addWidget(cb)
        self.checks.setLayout(layout)
        self.button_grp_checks.setExclusive(False)
        self.button_grp_checks.buttonClicked.connect(self.toggle_check_box)
        # self.checks.clicked.connect(self.clk_checks)
        
        # Push button 생성
        button1 = QPushButton("QMessageBox.simple")
        layout.addWidget(button1,0,1)
        button1.clicked.connect(self.button1_clicked)
        self.button_grp_checks.addButton(button1)
        
        button2 = QPushButton("QMessageBox.CustomDlg")
        layout.addWidget(button2,1,1)
        button2.clicked.connect(self.button2_clicked)
        self.button_grp_checks.addButton(button2)
        
        button3 = QPushButton("QMessageBox.information")
        layout.addWidget(button3,2,1)
        button3.clicked.connect(self.button3_clicked)
        self.button_grp_checks.addButton(button3)
        
        button4 = QPushButton("QMessageBox.about")
        layout.addWidget(button4,3,1)
        button4.clicked.connect(self.button4_clicked)
        self.button_grp_checks.addButton(button4)
        
        button5 = QPushButton("QMessageBox.question")
        layout.addWidget(button5,4,1)
        button5.clicked.connect(self.button5_clicked)
        self.button_grp_checks.addButton(button5)
        
        button6 = QPushButton("QMessageBox.critical")
        layout.addWidget(button6,5,1)
        button6.clicked.connect(self.button6_clicked)
        self.button_grp_checks.addButton(button6)
        
        button7 = QPushButton("QMessageBox.warning")
        layout.addWidget(button7,6,1)
        button7.clicked.connect(self.button7_clicked)
        self.button_grp_checks.addButton(button7)
        
        self.label = QLabel("")
        layout.addWidget(self.label,8,0)

        dummy = QWidget()
        dummy.setLayout(layout)
        
        self.setCentralWidget(dummy)
    
    def toggle_check_box(self, button):
        tmp = ""
        tmp = button.text()
        
        print(tmp)
        self.label.setText(tmp)
    
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