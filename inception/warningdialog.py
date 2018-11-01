# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warningdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WarningDialog(object):
    def setupUi(self, WarningDialog):
        WarningDialog.setObjectName("WarningDialog")
        WarningDialog.resize(450, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WarningDialog.sizePolicy().hasHeightForWidth())
        WarningDialog.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(WarningDialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.warning_close = QtWidgets.QPushButton(WarningDialog)
        self.warning_close.setGeometry(QtCore.QRect(340, 100, 89, 25))
        self.warning_close.setObjectName("warning_close")

        self.retranslateUi(WarningDialog)
        self.warning_close.clicked.connect(WarningDialog.close)
        QtCore.QMetaObject.connectSlotsByName(WarningDialog)

    def retranslateUi(self, WarningDialog):
        _translate = QtCore.QCoreApplication.translate
        WarningDialog.setWindowTitle(_translate("WarningDialog", "Warning"))
        self.label.setText(_translate("WarningDialog", "Please select a folder before you click on \'Group files\'"))
        self.warning_close.setText(_translate("WarningDialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WarningDialog = QtWidgets.QDialog()
    ui = Ui_WarningDialog()
    ui.setupUi(WarningDialog)
    WarningDialog.show()
    sys.exit(app.exec_())

