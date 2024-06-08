import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.addItem("Item 1")
        self.listWidget.addItem("Item 2")
        self.listWidget.addItem("Item 3")

        self.layout.addWidget(self.listWidget)

        self.button = QPushButton("Print Selected Item")
        self.button.clicked.connect(self.printSelectedItem)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.setWindowTitle('QListWidget Example')
        self.show()

    def printSelectedItem(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            print(f"Selected item: {selected_item.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())