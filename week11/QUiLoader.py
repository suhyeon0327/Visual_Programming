import os, sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class DsApp:
    def __init__(self, argv, ui_fstr):
        self.app = QApplication(argv)
        self.wnd = self.ds_get_wnd_from_ui(ui_fstr)
        self.ds_setup()
        self.wnd.show()

    def exec(self):
        return self.app.exec()

    def ds_setup(self):
        self.wnd.lineEdit.returnPressed.connect(self.ds_update_label)

    def ds_update_label(self):
        self.wnd.label.setText(f'Hello, {self.wnd.lineEdit.text()}')

    def ds_get_wnd_from_ui(self, ui_fstr):
        ui_loader = QUiLoader()
        root_dir = os.path.dirname(__file__)
        ui_path = os.path.join(root_dir, ui_fstr)

        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        wnd = ui_loader.load(ui_file, None)
        ui_file.close()

        return wnd

if __name__ == '__main__':    
    app = DsApp(sys.argv, 'Ex0_QtDesigner.ui')
    sys.exit(app.exec())