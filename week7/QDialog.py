import sys # 무조건 필요. sys.exit 때문에 필요
from PySide6.QtWidgets import ( QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__() # super class로 QMainWindow를 초기화
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked) # click이라는 signal을 button_clicked라는 slot에 연결

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = QDialog(self) # QDialog의 크기를 키우고 움직여도 main Widget의 중간에만 생성됨
        # dlg = QDialog() # main widget과 상관없이 화면에 생김
        dlg.setWindowTitle("QDialog Title") # QDialog Title 지정
        dlg.exec() # event loop, modal dialog의 특징 # 없으면 안생김(modal dialog에 반드시 있어야 함)
          # -------------
        # for custom dlg
        # dlg = CustomDlg(self)
        # if dlg.exec(): # Modal Dialog
        #     print('ok')
        # else:
        #     print("cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec() # event loop
    # event loop는 하나만 존재. 버튼을 클릭하면 dlg.exec()가 동작 끄면 app.exec()가 동작