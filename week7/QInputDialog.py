import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QLineEdit, QInputDialog)

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        
        
        layout = QVBoxLayout()
        self.l_buttons = ['getText', 'getMultilineText']
        for idx, c_str in enumerate(self.l_buttons):
            button0 = QPushButton('Test.')
            button0.clicked.connect(self.slot00)
            layout.addWidget(button0)

        self.ret_label = QLabel()
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        print(self.sender())
        sender = self.sender()
        
        tmp_str = sender.text()
        
        is_ok = False

        if tmp_str == self.l_buttons[0]:
            ret_text, is_ok = QInputDialog.getText(
                    self,
                    "Input Text",
                    "Enter Your Text!",
                    QLineEdit.PasswordEchoOnEdit,
                    "default text!",
                    )
        elif tmp_str == self.l_buttons[1]:
            ret_text, is_ok = QInputDialog(
                self,
                "Input Multi-Line Text",
                "Enter Your Multi-Lin Text!"
            )
        if is_ok:
            self.ret_label.setText(f'{ret_text}')    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())