import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QDialog
from mainwindow import Ui_AppWindow
from aboutwindow import Ui_AboutDialog
from successdialog import Ui_SuccessDialog
from warningdialog import Ui_WarningDialog
from program import run_app


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        self.ui.folder_select.clicked.connect(self.select_folder)
        self.ui.file_group.clicked.connect(self.group_files)
        self.ui.actionAbout.triggered.connect(self.show_about)

    def select_folder(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select a folder"))
        self.ui.folder_path.setText(path)

    def show_dialog(self, dialog_window):
        dialog = QDialog()
        dialog.ui = dialog_window()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def show_about(self):
        self.show_dialog(Ui_AboutDialog)

    def group_files(self):
        path = self.ui.folder_path.text()

        if path:
            run_app(path)
            self.ui.folder_path.setText("")
            self.show_dialog(Ui_SuccessDialog)
        else:
            self.show_dialog(Ui_WarningDialog)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
