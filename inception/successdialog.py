# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuccessDialog(object):
    def setupUi(self, SuccessDialog):
        SuccessDialog.setObjectName("SuccessDialog")
        SuccessDialog.resize(363, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuccessDialog.sizePolicy().hasHeightForWidth())
        SuccessDialog.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(SuccessDialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 341, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.success_close = QtWidgets.QPushButton(SuccessDialog)
        self.success_close.setGeometry(QtCore.QRect(260, 100, 89, 25))
        self.success_close.setObjectName("success_close")

        self.retranslateUi(SuccessDialog)
        self.success_close.clicked.connect(SuccessDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SuccessDialog)

    def retranslateUi(self, SuccessDialog):
        _translate = QtCore.QCoreApplication.translate
        SuccessDialog.setWindowTitle(_translate("SuccessDialog", "Success"))
        self.label.setText(_translate("SuccessDialog", "Files grouped successfully"))
        self.success_close.setText(_translate("SuccessDialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuccessDialog = QtWidgets.QDialog()
    ui = Ui_SuccessDialog()
    ui.setupUi(SuccessDialog)
    SuccessDialog.show()
    sys.exit(app.exec_())

