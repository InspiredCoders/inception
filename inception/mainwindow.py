# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(360, 180)
        AppWindow.setMaximumSize(QtCore.QSize(360, 180))
        self.centralwidget = QtWidgets.QWidget(AppWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.folder_path = QtWidgets.QLineEdit(self.centralwidget)
        self.folder_path.setEnabled(False)
        self.folder_path.setReadOnly(True)
        self.folder_path.setObjectName("folder_path")
        self.gridLayout.addWidget(self.folder_path, 0, 0, 1, 1)
        self.folder_select = QtWidgets.QPushButton(self.centralwidget)
        self.folder_select.setObjectName("folder_select")
        self.gridLayout.addWidget(self.folder_select, 0, 1, 1, 1)
        self.file_group = QtWidgets.QPushButton(self.centralwidget)
        self.file_group.setObjectName("file_group")
        self.gridLayout.addWidget(self.file_group, 1, 1, 1, 1)
        AppWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AppWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AppWindow)
        self.statusbar.setObjectName("statusbar")
        AppWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(AppWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(AppWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AppWindow)
        self.actionExit.triggered.connect(AppWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "Inception"))
        self.folder_select.setText(_translate("AppWindow", "Select Folder"))
        self.file_group.setText(_translate("AppWindow", "Group files"))
        self.menuFile.setTitle(_translate("AppWindow", "File"))
        self.menuHelp.setTitle(_translate("AppWindow", "Help"))
        self.actionExit.setText(_translate("AppWindow", "Exit"))
        self.actionAbout.setText(_translate("AppWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppWindow = QtWidgets.QMainWindow()
    ui = Ui_AppWindow()
    ui.setupUi(AppWindow)
    AppWindow.show()
    sys.exit(app.exec_())

