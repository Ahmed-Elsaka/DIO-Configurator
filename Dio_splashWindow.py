# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat Mar 16 20:27:18 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from Dio_MainWindow import Ui_create
from MainWindowLoad import Ui_load

class Ui_MainWindow(object):
    def showConfigurationWindow(self):
        self.window = QtGui.QWidget()
        self.ui = Ui_create()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()


    def showLoadConfigurationWindow(self):
        self.window = QtGui.QWidget()
        self.ui = Ui_load()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 286)
        self.btn_create = QtGui.QPushButton(MainWindow)
        self.btn_create.setGeometry(QtCore.QRect(100, 100, 191, 61))
        self.btn_create.setObjectName("btn_create")
        self.btn_load = QtGui.QPushButton(MainWindow)
        self.btn_load.setGeometry(QtCore.QRect(100, 170, 191, 61))
        self.btn_load.setObjectName("btn_load")
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(70, 20, 261, 51))
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_create, QtCore.SIGNAL("clicked()"), self.showConfigurationWindow)
        QtCore.QObject.connect(self.btn_load, QtCore.SIGNAL("clicked()"), self.showConfigurationWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main Window", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create.setText(QtGui.QApplication.translate("MainWindow", "Create New Configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_load.setText(QtGui.QApplication.translate("MainWindow", "Load Configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "AVR ATmega32 Pin Configuration Tool", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

