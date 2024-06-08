import sys
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

class CustomDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Hello, QDialog')
        
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # button에 해당하는 button 객체
        self.button_box = QDialogButtonBox(buttons)
        
        # QDialog의 메서드를 slot으로
        self.button_box.accepted.connect(self.accept)
        # QDialog의 메서드를 slot으로
        self.button_box.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel('Is something ok?')
        self.layout.addWidget(message)
        # QDialogButtonBox 객체 추가
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)
        
class MW(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")
        
        l_str = ['simple QDialog',
                 'Custom Dialog',
                 'QMessage.information',
                 'QMessage.warning',
                 'QMessage.critical',
                 'QMessage.about',
                 'QMessage.question']
        
        l_slot = [self.slot0,
                  self.slot1,
                  self.slot2,
                  self.slot3,
                  self.slot4,
                  self.slot5,
                  self.slot6]
        
        self.i = -1
        
        layout = QVBoxLayout()
        for idx, (i,s) in enumerate(zip(l_str, l_slot)):
            self.i = idx
            button = QPushButton(i)
            button.clicked.connect(s)
            # button.clicked.connect(self.button_clicked)
            layout.addWidget(button)
            
        a = QWidget()
        a.setLayout(layout)
        self.setCentralWidget(a)
        
    def slot0(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog Title")
        dlg.exec()
        
    def slot1(self):
        dlg = CustomDlg(self)
        if dlg.exec():
            print('ok')
        else:
            print("cancel")
            
    def slot2(self):
        QMessageBox.information(
            self,
            'Message',
            'This is an information message.'
        )
        
    def slot3(self):
        QMessageBox.warning(
            self,
            'Message',
            'This is an information message.'
        )
    
    def slot4(self):
        QMessageBox.critical(
            self,
            'Message',
            'This is an information message.'
        )
    
    def slot5(self):
        QMessageBox.about(
             self,              # parent
             "About This SW",   # title of about dialog.
             """<p>The example of QMessageBox</p>
             <p>version 0.1</p>"""
        )
    
    def slot6(self):
        QMessageBox.question(
        self,                 # parent
        "title of question",  # 질문 제목
        "cotent of question", # 질문 내용.
        QMessageBox.StandardButton.No | # \ 코드가 너무 길어서 한줄이라는 의미
        QMessageBox.StandardButton.Yes, # responses
        QMessageBox.StandardButton.Yes, # default response
        )
    
    def button_clicked(self, s):
        if self.i == 0:
            self.slot0()
        elif self.i == 1:
            self.slot1()
        elif self.i == 2:
            self.slot1()
        elif self.i == 3:
            self.slot1()
        elif self.i == 4:
            self.slot1()
        elif self.i == 5:
            self.slot1()
        elif self.i == 6:
            self.slot1()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()