# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created: Sat Mar 16 20:26:15 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from MainWindowLoad import Ui_load

class Ui_create(object):
    def setupUi(self, create):
        create.setObjectName("create")
        create.resize(673, 645)
        self.label_33 = QtGui.QLabel(create)
        self.label_33.setGeometry(QtCore.QRect(170, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(75)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.layoutWidget = QtGui.QWidget(create)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 651, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PortA_frame = QtGui.QFrame(self.layoutWidget)
        self.PortA_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PortA_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.PortA_frame.setObjectName("PortA_frame")
        self.PinA_1_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_1_ddr_combo.setGeometry(QtCore.QRect(80, 74, 113, 17))
        self.PinA_1_ddr_combo.setObjectName("PinA_1_ddr_combo")
        self.PinA_1_ddr_combo.addItem("")
        self.PinA_1_ddr_combo.addItem("")
        self.PinA_1_ddr_combo.addItem("")
        self.PinA_3_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_3_ddr_combo.setGeometry(QtCore.QRect(80, 120, 113, 17))
        self.PinA_3_ddr_combo.setObjectName("PinA_3_ddr_combo")
        self.PinA_3_ddr_combo.addItem("")
        self.PinA_3_ddr_combo.addItem("")
        self.PinA_3_ddr_combo.addItem("")
        self.label_5 = QtGui.QLabel(self.PortA_frame)
        self.label_5.setGeometry(QtCore.QRect(10, 211, 48, 17))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtGui.QLabel(self.PortA_frame)
        self.label_8.setGeometry(QtCore.QRect(10, 165, 47, 17))
        self.label_8.setObjectName("label_8")
        self.label = QtGui.QLabel(self.PortA_frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 48, 17))
        self.label.setObjectName("label")
        self.PinA_5_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_5_ddr_combo.setGeometry(QtCore.QRect(80, 166, 113, 16))
        self.PinA_5_ddr_combo.setObjectName("PinA_5_ddr_combo")
        self.PinA_5_ddr_combo.addItem("")
        self.PinA_5_ddr_combo.addItem("")
        self.PinA_5_ddr_combo.addItem("")
        self.label_4 = QtGui.QLabel(self.PortA_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 119, 47, 17))
        self.label_4.setObjectName("label_4")
        self.PinA_2_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_2_ddr_combo.setGeometry(QtCore.QRect(80, 97, 113, 17))
        self.PinA_2_ddr_combo.setObjectName("PinA_2_ddr_combo")
        self.PinA_2_ddr_combo.addItem("")
        self.PinA_2_ddr_combo.addItem("")
        self.PinA_2_ddr_combo.addItem("")
        self.label_3 = QtGui.QLabel(self.PortA_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 96, 47, 17))
        self.label_3.setObjectName("label_3")
        self.PinA_6_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_6_ddr_combo.setGeometry(QtCore.QRect(80, 188, 113, 17))
        self.PinA_6_ddr_combo.setObjectName("PinA_6_ddr_combo")
        self.PinA_6_ddr_combo.addItem("")
        self.PinA_6_ddr_combo.addItem("")
        self.PinA_6_ddr_combo.addItem("")
        self.label_7 = QtGui.QLabel(self.PortA_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 142, 48, 17))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtGui.QLabel(self.PortA_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 73, 47, 17))
        self.label_2.setObjectName("label_2")
        self.PinA_0_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_0_ddr_combo.setGeometry(QtCore.QRect(80, 51, 113, 17))
        self.PinA_0_ddr_combo.setObjectName("PinA_0_ddr_combo")
        self.PinA_0_ddr_combo.addItem("")
        self.PinA_0_ddr_combo.addItem("")
        self.PinA_0_ddr_combo.addItem("")
        self.label_6 = QtGui.QLabel(self.PortA_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 188, 48, 17))
        self.label_6.setObjectName("label_6")
        self.PinA_4_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_4_ddr_combo.setGeometry(QtCore.QRect(80, 143, 113, 17))
        self.PinA_4_ddr_combo.setObjectName("PinA_4_ddr_combo")
        self.PinA_4_ddr_combo.addItem("")
        self.PinA_4_ddr_combo.addItem("")
        self.PinA_4_ddr_combo.addItem("")
        self.PinA_7_ddr_combo = QtGui.QComboBox(self.PortA_frame)
        self.PinA_7_ddr_combo.setGeometry(QtCore.QRect(80, 211, 113, 17))
        self.PinA_7_ddr_combo.setObjectName("PinA_7_ddr_combo")
        self.PinA_7_ddr_combo.addItem("")
        self.PinA_7_ddr_combo.addItem("")
        self.PinA_7_ddr_combo.addItem("")
        self.label_17 = QtGui.QLabel(self.PortA_frame)
        self.label_17.setGeometry(QtCore.QRect(60, 10, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtGui.QLabel(self.PortA_frame)
        self.label_18.setGeometry(QtCore.QRect(10, 30, 31, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtGui.QLabel(self.PortA_frame)
        self.label_19.setGeometry(QtCore.QRect(80, 30, 111, 17))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtGui.QLabel(self.PortA_frame)
        self.label_20.setGeometry(QtCore.QRect(210, 30, 61, 17))
        self.label_20.setObjectName("label_20")
        self.layoutWidget1 = QtGui.QWidget(self.PortA_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 50, 101, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PinA_0_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_0_val_combo.setObjectName("PinA_0_val_combo")
        self.PinA_0_val_combo.addItem("")
        self.PinA_0_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_0_val_combo)
        self.PinA_1_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_1_val_combo.setObjectName("PinA_1_val_combo")
        self.PinA_1_val_combo.addItem("")
        self.PinA_1_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_1_val_combo)
        self.PinA_2_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_2_val_combo.setObjectName("PinA_2_val_combo")
        self.PinA_2_val_combo.addItem("")
        self.PinA_2_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_2_val_combo)
        self.PinA_3_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_3_val_combo.setObjectName("PinA_3_val_combo")
        self.PinA_3_val_combo.addItem("")
        self.PinA_3_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_3_val_combo)
        self.PinA_4_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_4_val_combo.setObjectName("PinA_4_val_combo")
        self.PinA_4_val_combo.addItem("")
        self.PinA_4_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_4_val_combo)
        self.PinA_5_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_5_val_combo.setObjectName("PinA_5_val_combo")
        self.PinA_5_val_combo.addItem("")
        self.PinA_5_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_5_val_combo)
        self.PinA_6_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_6_val_combo.setObjectName("PinA_6_val_combo")
        self.PinA_6_val_combo.addItem("")
        self.PinA_6_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_6_val_combo)
        self.PinA_7_val_combo = QtGui.QComboBox(self.layoutWidget1)
        self.PinA_7_val_combo.setObjectName("PinA_7_val_combo")
        self.PinA_7_val_combo.addItem("")
        self.PinA_7_val_combo.addItem("")
        self.verticalLayout.addWidget(self.PinA_7_val_combo)
        self.gridLayout.addWidget(self.PortA_frame, 0, 0, 1, 1)
        self.PortC_frame = QtGui.QFrame(self.layoutWidget)
        self.PortC_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PortC_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.PortC_frame.setObjectName("PortC_frame")
        self.PinC_1_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_1_ddr_combo.setGeometry(QtCore.QRect(80, 74, 113, 17))
        self.PinC_1_ddr_combo.setObjectName("PinC_1_ddr_combo")
        self.PinC_1_ddr_combo.addItem("")
        self.PinC_1_ddr_combo.addItem("")
        self.PinC_1_ddr_combo.addItem("")
        self.PinC_3_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_3_ddr_combo.setGeometry(QtCore.QRect(80, 120, 113, 17))
        self.PinC_3_ddr_combo.setObjectName("PinC_3_ddr_combo")
        self.PinC_3_ddr_combo.addItem("")
        self.PinC_3_ddr_combo.addItem("")
        self.PinC_3_ddr_combo.addItem("")
        self.label_58 = QtGui.QLabel(self.PortC_frame)
        self.label_58.setGeometry(QtCore.QRect(10, 211, 48, 17))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtGui.QLabel(self.PortC_frame)
        self.label_59.setGeometry(QtCore.QRect(10, 165, 47, 17))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtGui.QLabel(self.PortC_frame)
        self.label_60.setGeometry(QtCore.QRect(10, 50, 48, 17))
        self.label_60.setObjectName("label_60")
        self.PinC_5_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_5_ddr_combo.setGeometry(QtCore.QRect(80, 166, 113, 16))
        self.PinC_5_ddr_combo.setObjectName("PinC_5_ddr_combo")
        self.PinC_5_ddr_combo.addItem("")
        self.PinC_5_ddr_combo.addItem("")
        self.PinC_5_ddr_combo.addItem("")
        self.label_61 = QtGui.QLabel(self.PortC_frame)
        self.label_61.setGeometry(QtCore.QRect(10, 119, 47, 17))
        self.label_61.setObjectName("label_61")
        self.PinC_2_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_2_ddr_combo.setGeometry(QtCore.QRect(80, 97, 113, 17))
        self.PinC_2_ddr_combo.setObjectName("PinC_2_ddr_combo")
        self.PinC_2_ddr_combo.addItem("")
        self.PinC_2_ddr_combo.addItem("")
        self.PinC_2_ddr_combo.addItem("")
        self.label_62 = QtGui.QLabel(self.PortC_frame)
        self.label_62.setGeometry(QtCore.QRect(10, 96, 47, 17))
        self.label_62.setObjectName("label_62")
        self.PinC_6_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_6_ddr_combo.setGeometry(QtCore.QRect(80, 188, 113, 17))
        self.PinC_6_ddr_combo.setObjectName("PinC_6_ddr_combo")
        self.PinC_6_ddr_combo.addItem("")
        self.PinC_6_ddr_combo.addItem("")
        self.PinC_6_ddr_combo.addItem("")
        self.label_63 = QtGui.QLabel(self.PortC_frame)
        self.label_63.setGeometry(QtCore.QRect(10, 142, 48, 17))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtGui.QLabel(self.PortC_frame)
        self.label_64.setGeometry(QtCore.QRect(10, 73, 47, 17))
        self.label_64.setObjectName("label_64")
        self.PinC_0_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_0_ddr_combo.setGeometry(QtCore.QRect(80, 51, 113, 17))
        self.PinC_0_ddr_combo.setObjectName("PinC_0_ddr_combo")
        self.PinC_0_ddr_combo.addItem("")
        self.PinC_0_ddr_combo.addItem("")
        self.PinC_0_ddr_combo.addItem("")
        self.label_65 = QtGui.QLabel(self.PortC_frame)
        self.label_65.setGeometry(QtCore.QRect(10, 188, 48, 17))
        self.label_65.setObjectName("label_65")
        self.PinC_4_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_4_ddr_combo.setGeometry(QtCore.QRect(80, 143, 113, 17))
        self.PinC_4_ddr_combo.setObjectName("PinC_4_ddr_combo")
        self.PinC_4_ddr_combo.addItem("")
        self.PinC_4_ddr_combo.addItem("")
        self.PinC_4_ddr_combo.addItem("")
        self.PinC_7_ddr_combo = QtGui.QComboBox(self.PortC_frame)
        self.PinC_7_ddr_combo.setGeometry(QtCore.QRect(80, 211, 113, 17))
        self.PinC_7_ddr_combo.setObjectName("PinC_7_ddr_combo")
        self.PinC_7_ddr_combo.addItem("")
        self.PinC_7_ddr_combo.addItem("")
        self.PinC_7_ddr_combo.addItem("")
        self.label_66 = QtGui.QLabel(self.PortC_frame)
        self.label_66.setGeometry(QtCore.QRect(60, 10, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtGui.QLabel(self.PortC_frame)
        self.label_67.setGeometry(QtCore.QRect(10, 30, 31, 17))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtGui.QLabel(self.PortC_frame)
        self.label_68.setGeometry(QtCore.QRect(80, 30, 111, 17))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtGui.QLabel(self.PortC_frame)
        self.label_69.setGeometry(QtCore.QRect(210, 30, 61, 17))
        self.label_69.setObjectName("label_69")
        self.layoutWidget_4 = QtGui.QWidget(self.PortC_frame)
        self.layoutWidget_4.setGeometry(QtCore.QRect(210, 50, 101, 181))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PinC_0_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_0_val_combo.setObjectName("PinC_0_val_combo")
        self.PinC_0_val_combo.addItem("")
        self.PinC_0_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_0_val_combo)
        self.PinC_1_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_1_val_combo.setObjectName("PinC_1_val_combo")
        self.PinC_1_val_combo.addItem("")
        self.PinC_1_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_1_val_combo)
        self.PinC_2_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_2_val_combo.setObjectName("PinC_2_val_combo")
        self.PinC_2_val_combo.addItem("")
        self.PinC_2_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_2_val_combo)
        self.PinC_3_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_3_val_combo.setObjectName("PinC_3_val_combo")
        self.PinC_3_val_combo.addItem("")
        self.PinC_3_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_3_val_combo)
        self.PinC_4_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_4_val_combo.setObjectName("PinC_4_val_combo")
        self.PinC_4_val_combo.addItem("")
        self.PinC_4_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_4_val_combo)
        self.PinC_5_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_5_val_combo.setObjectName("PinC_5_val_combo")
        self.PinC_5_val_combo.addItem("")
        self.PinC_5_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_5_val_combo)
        self.PinC_6_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_6_val_combo.setObjectName("PinC_6_val_combo")
        self.PinC_6_val_combo.addItem("")
        self.PinC_6_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_6_val_combo)
        self.PinC_7_val_combo = QtGui.QComboBox(self.layoutWidget_4)
        self.PinC_7_val_combo.setObjectName("PinC_7_val_combo")
        self.PinC_7_val_combo.addItem("")
        self.PinC_7_val_combo.addItem("")
        self.verticalLayout_5.addWidget(self.PinC_7_val_combo)
        self.gridLayout.addWidget(self.PortC_frame, 0, 1, 1, 1)
        self.PortB_frame = QtGui.QFrame(self.layoutWidget)
        self.PortB_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PortB_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.PortB_frame.setObjectName("PortB_frame")
        self.PinB_1_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_1_ddr_combo.setGeometry(QtCore.QRect(80, 74, 113, 17))
        self.PinB_1_ddr_combo.setObjectName("PinB_1_ddr_combo")
        self.PinB_1_ddr_combo.addItem("")
        self.PinB_1_ddr_combo.addItem("")
        self.PinB_1_ddr_combo.addItem("")
        self.PinB_3_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_3_ddr_combo.setGeometry(QtCore.QRect(80, 120, 113, 17))
        self.PinB_3_ddr_combo.setObjectName("PinB_3_ddr_combo")
        self.PinB_3_ddr_combo.addItem("")
        self.PinB_3_ddr_combo.addItem("")
        self.PinB_3_ddr_combo.addItem("")
        self.label_34 = QtGui.QLabel(self.PortB_frame)
        self.label_34.setGeometry(QtCore.QRect(10, 211, 48, 17))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtGui.QLabel(self.PortB_frame)
        self.label_35.setGeometry(QtCore.QRect(10, 165, 47, 17))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtGui.QLabel(self.PortB_frame)
        self.label_36.setGeometry(QtCore.QRect(10, 50, 48, 17))
        self.label_36.setObjectName("label_36")
        self.PinB_5_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_5_ddr_combo.setGeometry(QtCore.QRect(80, 166, 113, 16))
        self.PinB_5_ddr_combo.setObjectName("PinB_5_ddr_combo")
        self.PinB_5_ddr_combo.addItem("")
        self.PinB_5_ddr_combo.addItem("")
        self.PinB_5_ddr_combo.addItem("")
        self.label_37 = QtGui.QLabel(self.PortB_frame)
        self.label_37.setGeometry(QtCore.QRect(10, 119, 47, 17))
        self.label_37.setObjectName("label_37")
        self.PinB_2_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_2_ddr_combo.setGeometry(QtCore.QRect(80, 97, 113, 17))
        self.PinB_2_ddr_combo.setObjectName("PinB_2_ddr_combo")
        self.PinB_2_ddr_combo.addItem("")
        self.PinB_2_ddr_combo.addItem("")
        self.PinB_2_ddr_combo.addItem("")
        self.label_38 = QtGui.QLabel(self.PortB_frame)
        self.label_38.setGeometry(QtCore.QRect(10, 96, 47, 17))
        self.label_38.setObjectName("label_38")
        self.PinB_6_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_6_ddr_combo.setGeometry(QtCore.QRect(80, 188, 113, 17))
        self.PinB_6_ddr_combo.setObjectName("PinB_6_ddr_combo")
        self.PinB_6_ddr_combo.addItem("")
        self.PinB_6_ddr_combo.addItem("")
        self.PinB_6_ddr_combo.addItem("")
        self.label_39 = QtGui.QLabel(self.PortB_frame)
        self.label_39.setGeometry(QtCore.QRect(10, 142, 48, 17))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtGui.QLabel(self.PortB_frame)
        self.label_40.setGeometry(QtCore.QRect(10, 73, 47, 17))
        self.label_40.setObjectName("label_40")
        self.PinB_0_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_0_ddr_combo.setGeometry(QtCore.QRect(80, 51, 113, 17))
        self.PinB_0_ddr_combo.setObjectName("PinB_0_ddr_combo")
        self.PinB_0_ddr_combo.addItem("")
        self.PinB_0_ddr_combo.addItem("")
        self.PinB_0_ddr_combo.addItem("")
        self.label_41 = QtGui.QLabel(self.PortB_frame)
        self.label_41.setGeometry(QtCore.QRect(10, 188, 48, 17))
        self.label_41.setObjectName("label_41")
        self.PinB_4_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_4_ddr_combo.setGeometry(QtCore.QRect(80, 143, 113, 17))
        self.PinB_4_ddr_combo.setObjectName("PinB_4_ddr_combo")
        self.PinB_4_ddr_combo.addItem("")
        self.PinB_4_ddr_combo.addItem("")
        self.PinB_4_ddr_combo.addItem("")
        self.PinB_7_ddr_combo = QtGui.QComboBox(self.PortB_frame)
        self.PinB_7_ddr_combo.setGeometry(QtCore.QRect(80, 211, 113, 17))
        self.PinB_7_ddr_combo.setObjectName("PinB_7_ddr_combo")
        self.PinB_7_ddr_combo.addItem("")
        self.PinB_7_ddr_combo.addItem("")
        self.PinB_7_ddr_combo.addItem("")
        self.label_42 = QtGui.QLabel(self.PortB_frame)
        self.label_42.setGeometry(QtCore.QRect(60, 10, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtGui.QLabel(self.PortB_frame)
        self.label_43.setGeometry(QtCore.QRect(10, 30, 31, 17))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtGui.QLabel(self.PortB_frame)
        self.label_44.setGeometry(QtCore.QRect(80, 30, 111, 17))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtGui.QLabel(self.PortB_frame)
        self.label_45.setGeometry(QtCore.QRect(210, 30, 61, 17))
        self.label_45.setObjectName("label_45")
        self.layoutWidget_2 = QtGui.QWidget(self.PortB_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(210, 50, 101, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PinB_0_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_0_val_combo.setObjectName("PinB_0_val_combo")
        self.PinB_0_val_combo.addItem("")
        self.PinB_0_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_0_val_combo)
        self.PinB_1_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_1_val_combo.setObjectName("PinB_1_val_combo")
        self.PinB_1_val_combo.addItem("")
        self.PinB_1_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_1_val_combo)
        self.PinB_2_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_2_val_combo.setObjectName("PinB_2_val_combo")
        self.PinB_2_val_combo.addItem("")
        self.PinB_2_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_2_val_combo)
        self.PinB_3_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_3_val_combo.setObjectName("PinB_3_val_combo")
        self.PinB_3_val_combo.addItem("")
        self.PinB_3_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_3_val_combo)
        self.PinB_4_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_4_val_combo.setObjectName("PinB_4_val_combo")
        self.PinB_4_val_combo.addItem("")
        self.PinB_4_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_4_val_combo)
        self.PinB_5_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_5_val_combo.setObjectName("PinB_5_val_combo")
        self.PinB_5_val_combo.addItem("")
        self.PinB_5_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_5_val_combo)
        self.PinB_6_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_6_val_combo.setObjectName("PinB_6_val_combo")
        self.PinB_6_val_combo.addItem("")
        self.PinB_6_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_6_val_combo)
        self.PinB_7_val_combo = QtGui.QComboBox(self.layoutWidget_2)
        self.PinB_7_val_combo.setObjectName("PinB_7_val_combo")
        self.PinB_7_val_combo.addItem("")
        self.PinB_7_val_combo.addItem("")
        self.verticalLayout_3.addWidget(self.PinB_7_val_combo)
        self.gridLayout.addWidget(self.PortB_frame, 1, 0, 1, 1)
        self.PortD_frame = QtGui.QFrame(self.layoutWidget)
        self.PortD_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PortD_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.PortD_frame.setObjectName("PortD_frame")
        self.PinD_1_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_1_ddr_combo.setGeometry(QtCore.QRect(80, 74, 113, 17))
        self.PinD_1_ddr_combo.setObjectName("PinD_1_ddr_combo")
        self.PinD_1_ddr_combo.addItem("")
        self.PinD_1_ddr_combo.addItem("")
        self.PinD_1_ddr_combo.addItem("")
        self.PinD_3_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_3_ddr_combo.setGeometry(QtCore.QRect(80, 120, 113, 17))
        self.PinD_3_ddr_combo.setObjectName("PinD_3_ddr_combo")
        self.PinD_3_ddr_combo.addItem("")
        self.PinD_3_ddr_combo.addItem("")
        self.PinD_3_ddr_combo.addItem("")
        self.label_46 = QtGui.QLabel(self.PortD_frame)
        self.label_46.setGeometry(QtCore.QRect(10, 211, 48, 17))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtGui.QLabel(self.PortD_frame)
        self.label_47.setGeometry(QtCore.QRect(10, 165, 47, 17))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtGui.QLabel(self.PortD_frame)
        self.label_48.setGeometry(QtCore.QRect(10, 50, 48, 17))
        self.label_48.setObjectName("label_48")
        self.PinD_5_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_5_ddr_combo.setGeometry(QtCore.QRect(80, 166, 113, 16))
        self.PinD_5_ddr_combo.setObjectName("PinD_5_ddr_combo")
        self.PinD_5_ddr_combo.addItem("")
        self.PinD_5_ddr_combo.addItem("")
        self.PinD_5_ddr_combo.addItem("")
        self.label_49 = QtGui.QLabel(self.PortD_frame)
        self.label_49.setGeometry(QtCore.QRect(10, 119, 47, 17))
        self.label_49.setObjectName("label_49")
        self.PinD_2_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_2_ddr_combo.setGeometry(QtCore.QRect(80, 97, 113, 17))
        self.PinD_2_ddr_combo.setObjectName("PinD_2_ddr_combo")
        self.PinD_2_ddr_combo.addItem("")
        self.PinD_2_ddr_combo.addItem("")
        self.PinD_2_ddr_combo.addItem("")
        self.label_50 = QtGui.QLabel(self.PortD_frame)
        self.label_50.setGeometry(QtCore.QRect(10, 96, 47, 17))
        self.label_50.setObjectName("label_50")
        self.PinD_6_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_6_ddr_combo.setGeometry(QtCore.QRect(80, 188, 113, 17))
        self.PinD_6_ddr_combo.setObjectName("PinD_6_ddr_combo")
        self.PinD_6_ddr_combo.addItem("")
        self.PinD_6_ddr_combo.addItem("")
        self.PinD_6_ddr_combo.addItem("")
        self.label_51 = QtGui.QLabel(self.PortD_frame)
        self.label_51.setGeometry(QtCore.QRect(10, 142, 48, 17))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtGui.QLabel(self.PortD_frame)
        self.label_52.setGeometry(QtCore.QRect(10, 73, 47, 17))
        self.label_52.setObjectName("label_52")
        self.PinD_0_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_0_ddr_combo.setGeometry(QtCore.QRect(80, 51, 113, 17))
        self.PinD_0_ddr_combo.setObjectName("PinD_0_ddr_combo")
        self.PinD_0_ddr_combo.addItem("")
        self.PinD_0_ddr_combo.addItem("")
        self.PinD_0_ddr_combo.addItem("")
        self.label_53 = QtGui.QLabel(self.PortD_frame)
        self.label_53.setGeometry(QtCore.QRect(10, 188, 48, 17))
        self.label_53.setObjectName("label_53")
        self.PinD_4_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_4_ddr_combo.setGeometry(QtCore.QRect(80, 143, 113, 17))
        self.PinD_4_ddr_combo.setObjectName("PinD_4_ddr_combo")
        self.PinD_4_ddr_combo.addItem("")
        self.PinD_4_ddr_combo.addItem("")
        self.PinD_4_ddr_combo.addItem("")
        self.PinD_7_ddr_combo = QtGui.QComboBox(self.PortD_frame)
        self.PinD_7_ddr_combo.setGeometry(QtCore.QRect(80, 211, 113, 17))
        self.PinD_7_ddr_combo.setObjectName("PinD_7_ddr_combo")
        self.PinD_7_ddr_combo.addItem("")
        self.PinD_7_ddr_combo.addItem("")
        self.PinD_7_ddr_combo.addItem("")
        self.label_54 = QtGui.QLabel(self.PortD_frame)
        self.label_54.setGeometry(QtCore.QRect(60, 10, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtGui.QLabel(self.PortD_frame)
        self.label_55.setGeometry(QtCore.QRect(10, 30, 31, 17))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtGui.QLabel(self.PortD_frame)
        self.label_56.setGeometry(QtCore.QRect(80, 30, 111, 17))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtGui.QLabel(self.PortD_frame)
        self.label_57.setGeometry(QtCore.QRect(210, 30, 61, 17))
        self.label_57.setObjectName("label_57")
        self.layoutWidget_3 = QtGui.QWidget(self.PortD_frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(210, 50, 101, 181))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.PinD_0_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_0_val_combo.setObjectName("PinD_0_val_combo")
        self.PinD_0_val_combo.addItem("")
        self.PinD_0_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_0_val_combo)
        self.PinD_1_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_1_val_combo.setObjectName("PinD_1_val_combo")
        self.PinD_1_val_combo.addItem("")
        self.PinD_1_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_1_val_combo)
        self.PinD_2_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_2_val_combo.setObjectName("PinD_2_val_combo")
        self.PinD_2_val_combo.addItem("")
        self.PinD_2_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_2_val_combo)
        self.PinD_3_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_3_val_combo.setObjectName("PinD_3_val_combo")
        self.PinD_3_val_combo.addItem("")
        self.PinD_3_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_3_val_combo)
        self.PinD_4_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_4_val_combo.setObjectName("PinD_4_val_combo")
        self.PinD_4_val_combo.addItem("")
        self.PinD_4_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_4_val_combo)
        self.PinD_5_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_5_val_combo.setObjectName("PinD_5_val_combo")
        self.PinD_5_val_combo.addItem("")
        self.PinD_5_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_5_val_combo)
        self.PinD_6_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_6_val_combo.setObjectName("PinD_6_val_combo")
        self.PinD_6_val_combo.addItem("")
        self.PinD_6_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_6_val_combo)
        self.PinD_7_val_combo = QtGui.QComboBox(self.layoutWidget_3)
        self.PinD_7_val_combo.setObjectName("PinD_7_val_combo")
        self.PinD_7_val_combo.addItem("")
        self.PinD_7_val_combo.addItem("")
        self.verticalLayout_4.addWidget(self.PinD_7_val_combo)
        self.gridLayout.addWidget(self.PortD_frame, 1, 1, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(create)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 588, 651, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_70 = QtGui.QLabel(self.layoutWidget2)
        self.label_70.setObjectName("label_70")
        self.horizontalLayout.addWidget(self.label_70)
        self.txt_lineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.txt_lineEdit.setObjectName("txt_lineEdit")
        self.horizontalLayout.addWidget(self.txt_lineEdit)
        self.btn_save = QtGui.QPushButton(self.layoutWidget2)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_exit = QtGui.QPushButton(self.layoutWidget2)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)

        self.retranslateUi(create)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL("clicked()"), self.LoadConfigurationFromFile)
        QtCore.QObject.connect(self.btn_save, QtCore.SIGNAL("clicked()"), self.StoreConfigurations)
        QtCore.QMetaObject.connectSlotsByName(create)

    def WriteInFile(self,list):
        ##############################################################################
        #  this function will write in file Data Direction Register Configurations   #
        #  INPUT :                                                                   #
        #      list : this is a list of DDR States                                   #
        #  OUTPUT :                                                                  #
        #      the function will write in Text file                                  # 
        #      The configurations based on list content                              #
        ##############################################################################
        fileName= self.txt_lineEdit.text()
        # handel if file name is empty 
        try : 
            with open(fileName, 'w') as f:
                f.write("/*   Configure initial pins directions   */\n")
                list_length = len(list)
                Input_type = ''
                for i in range(list_length):
                    if list[i] == 'Output' :
                        Input_type='DIO_PIN_INIT_OUTPUT'
                    elif list[i] == 'Input':
                        Input_type='DIO_PIN_INIT_INPUT'
                    elif list[i] == 'Input_Pullup':
                        Input_type='DIO_PIN_INIT_INPUT_PULLUP'
                    if i < 10 : 
                        f.write("#define DIO_u8_PIN"+str(i)+"_DDR         "+Input_type+"\n")
                    else : 
                        f.write("#define DIO_u8_PIN"+str(i)+"_DDR        "+Input_type+"\n")
        except IOError:
            print('please enter file name ')


# ---------------------------------------------- Store in file functions -----------------------
    def StoreDDRCompoStates(self):
        ##############################################################################
        #  this function set status of current configurations for pis in the script  #
        #  INPUT :                                                                   #
        #      This function take no arguements except self                          #
        #  OUTPUT :                                                                  #
        #      the function will store the state of current configuratiions in list  # 
        #      Then passing this list to WriteInFile function to Write them          #
        ##############################################################################
        states = [] # create list to store states of pins 
        # get status of portA 
        states.append(self.PinA_0_ddr_combo.currentText())
        states.append(self.PinA_1_ddr_combo.currentText())
        states.append(self.PinA_2_ddr_combo.currentText())
        states.append(self.PinA_3_ddr_combo.currentText())
        states.append(self.PinA_4_ddr_combo.currentText())
        states.append(self.PinA_5_ddr_combo.currentText())
        states.append(self.PinA_6_ddr_combo.currentText())
        states.append(self.PinA_7_ddr_combo.currentText())        
        # get status of portB 
        states.append(self.PinB_0_ddr_combo.currentText())
        states.append(self.PinB_1_ddr_combo.currentText())
        states.append(self.PinB_2_ddr_combo.currentText())
        states.append(self.PinB_3_ddr_combo.currentText())
        states.append(self.PinB_4_ddr_combo.currentText())
        states.append(self.PinB_5_ddr_combo.currentText())
        states.append(self.PinB_6_ddr_combo.currentText())
        states.append(self.PinB_7_ddr_combo.currentText()) 
        # get status of portC 
        states.append(self.PinC_0_ddr_combo.currentText())
        states.append(self.PinC_1_ddr_combo.currentText())
        states.append(self.PinC_2_ddr_combo.currentText())
        states.append(self.PinC_3_ddr_combo.currentText())
        states.append(self.PinC_4_ddr_combo.currentText())
        states.append(self.PinC_5_ddr_combo.currentText())
        states.append(self.PinC_6_ddr_combo.currentText())
        states.append(self.PinC_7_ddr_combo.currentText()) 
        # get status of portD 
        states.append(self.PinD_0_ddr_combo.currentText())
        states.append(self.PinD_1_ddr_combo.currentText())
        states.append(self.PinD_2_ddr_combo.currentText())
        states.append(self.PinD_3_ddr_combo.currentText())
        states.append(self.PinD_4_ddr_combo.currentText())
        states.append(self.PinD_5_ddr_combo.currentText())
        states.append(self.PinD_6_ddr_combo.currentText())
        states.append(self.PinD_7_ddr_combo.currentText()) 

     # Send this list to WriteInFile Function to write it in file 
        self.WriteInFile(states)

    def AppendToFile(self,list):
        ##############################################################################
        #  this function will append in file Ports Direction Register Configurations #
        #  INPUT :                                                                   #
        #      list : this is a list of PORTS States                                 #
        #  OUTPUT :                                                                  #
        #      the function will append in Text file                                 # 
        #      The configurations based on list content                              #
        ##############################################################################
        fileName= self.txt_lineEdit.text()
        try : 
            with open(fileName, 'a+') as f:
                list_length = len(list)
                PIN_VALUE = ''
                f.write("\n\n\n\n\n\n\n\n\n\n")
                f.write("/*   Configure initial pins values   */\n")
                for i in range(list_length):
                    if list[i] == 'HIGH' :
                        PIN_VALUE='DIO_PIN_INIT_HIGH'
                    elif list[i] == 'LOW':
                        PIN_VALUE='DIO_PIN_INIT_LOW'
                    if i < 10 : 
                        f.write("#define DIO_u8_PIN"+str(i)+"_VALUE         "+PIN_VALUE+"\n")
                    else : 
                        f.write("#define DIO_u8_PIN"+str(i)+"_VALUE        "+PIN_VALUE+"\n")
        except IOError : 
            print(" ")


    def StoreVALCompoStates(self):
        ##############################################################################
        #  this function get status of current configurations for pis in the script  #
        #  INPUT :                                                                   #
        #      This function take no arguements except self                          #
        #  OUTPUT :                                                                  #
        #      the function will store the state of current configuratiions in list  # 
        #      Then passing this list to AppendToFile function to Write them         #
        ##############################################################################
     #1- get DDR combobox state 
        states = [] # create list to store states of pins 
        # get status of portA 
        states.append(self.PinA_0_val_combo.currentText())
        states.append(self.PinA_1_val_combo.currentText())
        states.append(self.PinA_2_val_combo.currentText())
        states.append(self.PinA_3_val_combo.currentText())
        states.append(self.PinA_4_val_combo.currentText())
        states.append(self.PinA_5_val_combo.currentText())
        states.append(self.PinA_6_val_combo.currentText())
        states.append(self.PinA_7_val_combo.currentText())        
        # get status of portB 
        states.append(self.PinB_0_val_combo.currentText())
        states.append(self.PinB_1_val_combo.currentText())
        states.append(self.PinB_2_val_combo.currentText())
        states.append(self.PinB_3_val_combo.currentText())
        states.append(self.PinB_4_val_combo.currentText())
        states.append(self.PinB_5_val_combo.currentText())
        states.append(self.PinB_6_val_combo.currentText())
        states.append(self.PinB_7_val_combo.currentText()) 
        # get status of portC 
        states.append(self.PinC_0_val_combo.currentText())
        states.append(self.PinC_1_val_combo.currentText())
        states.append(self.PinC_2_val_combo.currentText())
        states.append(self.PinC_3_val_combo.currentText())
        states.append(self.PinC_4_val_combo.currentText())
        states.append(self.PinC_5_val_combo.currentText())
        states.append(self.PinC_6_val_combo.currentText())
        states.append(self.PinC_7_val_combo.currentText()) 
        # get status of portD 
        states.append(self.PinD_0_val_combo.currentText())
        states.append(self.PinD_1_val_combo.currentText())
        states.append(self.PinD_2_val_combo.currentText())
        states.append(self.PinD_3_val_combo.currentText())
        states.append(self.PinD_4_val_combo.currentText())
        states.append(self.PinD_5_val_combo.currentText())
        states.append(self.PinD_6_val_combo.currentText())
        states.append(self.PinD_7_val_combo.currentText()) 

     #2 - write states to file 
        self.AppendToFile(states)

    def StoreConfigurations(self):
        ##############################################################################
        #  this is the main function that control all script through two functions   #
        #   1- StoreDDRCompoStates :                                                 #
        #        Store the state of DDRs Configurations                              #
        #    2- StoreVALCompoStates :                                                #
        #       Store the state of PORTs Configurations                              #
        #  INPUT :                                                                   #
        #      This function take no arguements except self                          #
        #  OUTPUT :                                                                  #
        #      the function will call these two functions to store your              #
        #        configurations                                                       # 
        ##############################################################################
        self.StoreDDRCompoStates()
        self.StoreVALCompoStates()
#------------------------------------------ End of Store in file functions ---------------------

# ------------------------------------------start read from file function ----------------------


    def FillDDRCombos(self, index , type):
        ##############################################################################
        #  this function Fill fields of Script combo boxes related to DDRs           #
        #  INPUT :                                                                   #
        #      index :                                                               #
        #            this represend parsed line index to define which combobox will  #
        #            be effected                                                     #
        #        type :                                                              #
        #            define which state will the combobox will change to             #
        #  OUTPUT :                                                                  #
        #        Change states of DDRs Compoboxs                                     #
        ##############################################################################
            #------------------------------fill DDR A ------------------------------#
            if index == 1 : 
                index = self.PinA_0_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_0_ddr_combo.setCurrentIndex(index)
            if index == 2 : 
                index = self.PinA_1_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_1_ddr_combo.setCurrentIndex(index)
            if index == 3 : 
                index = self.PinA_2_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_2_ddr_combo.setCurrentIndex(index)
            if index == 4 : 
                index = self.PinA_3_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_3_ddr_combo.setCurrentIndex(index)
            if index == 5 : 
                index = self.PinA_4_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_4_ddr_combo.setCurrentIndex(index)
            if index == 6 : 
                index = self.PinA_5_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_5_ddr_combo.setCurrentIndex(index)
            if index == 7 : 
                index = self.PinA_6_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_6_ddr_combo.setCurrentIndex(index)
            if index == 8 : 
                index = self.PinA_7_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_7_ddr_combo.setCurrentIndex(index)
            # -----------------------------fill DDR B -------------------------------#
            if index == 9 : 
                index = self.PinB_0_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_0_ddr_combo.setCurrentIndex(index)
            if index == 10 : 
                index = self.PinB_1_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_1_ddr_combo.setCurrentIndex(index)
            if index == 11 : 
                index = self.PinB_2_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_2_ddr_combo.setCurrentIndex(index)
            if index == 12 : 
                index = self.PinB_3_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_3_ddr_combo.setCurrentIndex(index)
            if index == 13 : 
                index = self.PinB_4_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_4_ddr_combo.setCurrentIndex(index)
            if index == 14 : 
                index = self.PinB_5_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_5_ddr_combo.setCurrentIndex(index)
            if index == 15 : 
                index = self.PinB_6_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_6_ddr_combo.setCurrentIndex(index)
            if index == 16 : 
                index = self.PinB_7_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_7_ddr_combo.setCurrentIndex(index) 

            # --------------------------------fill DDR C -------------------------------#
            if index == 17 : 
                index = self.PinC_0_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_0_ddr_combo.setCurrentIndex(index)
            if index == 18 : 
                index = self.PinB_1_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_1_ddr_combo.setCurrentIndex(index)
            if index == 19 : 
                index = self.PinC_2_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_2_ddr_combo.setCurrentIndex(index)
            if index == 20 : 
                index = self.PinC_3_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_3_ddr_combo.setCurrentIndex(index)
            if index == 21 : 
                index = self.PinC_4_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_4_ddr_combo.setCurrentIndex(index)
            if index == 22 : 
                index = self.PinC_5_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_5_ddr_combo.setCurrentIndex(index)
            if index == 23 : 
                index = self.PinC_6_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_6_ddr_combo.setCurrentIndex(index)
            if index == 24 : 
                index = self.PinC_7_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_7_ddr_combo.setCurrentIndex(index) 

            # -----------------------------fill DDR D --------------------------------#
            if index == 25 : 
                index = self.PinD_0_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_0_ddr_combo.setCurrentIndex(index)
            if index == 26 : 
                index = self.PinB_1_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_1_ddr_combo.setCurrentIndex(index)
            if index == 27 : 
                index = self.PinD_2_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_2_ddr_combo.setCurrentIndex(index)
            if index == 28 : 
                index = self.PinD_3_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_3_ddr_combo.setCurrentIndex(index)
            if index == 29 : 
                index = self.PinD_4_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_4_ddr_combo.setCurrentIndex(index)
            if index == 30 : 
                index = self.PinD_5_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_5_ddr_combo.setCurrentIndex(index)
            if index == 31 : 
                index = self.PinD_6_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_6_ddr_combo.setCurrentIndex(index)
            if index == 32 : 
                index = self.PinD_7_ddr_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_7_ddr_combo.setCurrentIndex(index) 


    def FillVALCombos(self, index , type):
        ##############################################################################
        #  this function Fill fields of Script combo boxes related to PORTS          #
        #  INPUT :                                                                   #
        #      index :                                                               #
        #            this represend parsed line index to define which combobox will  #
        #            be effected                                                     #
        #        type :                                                              #
        #            define which state will the combobox will change to             #
        #  OUTPUT :                                                                  #
        #        Change states of PORTs Compoboxs                                    #
        ##############################################################################
             # -----------------------------fill port A --------------------------------#
            if index == 1 : 
                index = self.PinA_0_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_0_val_combo.setCurrentIndex(index)
            if index == 2 : 
                index = self.PinA_1_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_1_val_combo.setCurrentIndex(index)
            if index == 3 : 
                index = self.PinA_2_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_2_val_combo.setCurrentIndex(index)
            if index == 4 : 
                index = self.PinA_3_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_3_val_combo.setCurrentIndex(index)
            if index == 5 : 
                index = self.PinA_4_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_4_val_combo.setCurrentIndex(index)
            if index == 6 : 
                index = self.PinA_5_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_5_val_combo.setCurrentIndex(index)
            if index == 7 : 
                index = self.PinA_6_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_6_val_combo.setCurrentIndex(index)
            if index == 8 : 
                index = self.PinA_7_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinA_7_val_combo.setCurrentIndex(index)
             # -----------------------------fill port B --------------------------------#
            if index == 9 : 
                index = self.PinB_0_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_0_val_combo.setCurrentIndex(index)
            if index == 10 : 
                index = self.PinB_1_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_1_val_combo.setCurrentIndex(index)
            if index == 11 : 
                index = self.PinB_2_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_2_val_combo.setCurrentIndex(index)
            if index == 12 : 
                index = self.PinB_3_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_3_val_combo.setCurrentIndex(index)
            if index == 13 : 
                index = self.PinB_4_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_4_val_combo.setCurrentIndex(index)
            if index == 14 : 
                index = self.PinB_5_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_5_val_combo.setCurrentIndex(index)
            if index == 15 : 
                index = self.PinB_6_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_6_val_combo.setCurrentIndex(index)
            if index == 16 : 
                index = self.PinB_7_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinB_7_val_combo.setCurrentIndex(index) 

             # -----------------------------fill port B --------------------------------#
            if index == 17 : 
                index = self.PinC_0_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_0_val_combo.setCurrentIndex(index)
            if index == 18 : 
                index = self.PinB_1_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_1_val_combo.setCurrentIndex(index)
            if index == 19 : 
                index = self.PinC_2_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_2_val_combo.setCurrentIndex(index)
            if index == 20 : 
                index = self.PinC_3_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_3_val_combo.setCurrentIndex(index)
            if index == 21 : 
                index = self.PinC_4_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_4_val_combo.setCurrentIndex(index)
            if index == 22 : 
                index = self.PinC_5_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_5_val_combo.setCurrentIndex(index)
            if index == 23 : 
                index = self.PinC_6_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_6_val_combo.setCurrentIndex(index)
            if index == 24 : 
                index = self.PinC_7_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinC_7_val_combo.setCurrentIndex(index) 

             # -----------------------------fill port D --------------------------------#
            if index == 25 : 
                index = self.PinD_0_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_0_val_combo.setCurrentIndex(index)
            if index == 26 : 
                index = self.PinB_1_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_1_val_combo.setCurrentIndex(index)
            if index == 27 : 
                index = self.PinD_2_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_2_val_combo.setCurrentIndex(index)
            if index == 28 : 
                index = self.PinD_3_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_3_val_combo.setCurrentIndex(index)
            if index == 29 : 
                index = self.PinD_4_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_4_val_combo.setCurrentIndex(index)
            if index == 30 : 
                index = self.PinD_5_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_5_val_combo.setCurrentIndex(index)
            if index == 31 : 
                index = self.PinD_6_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_6_val_combo.setCurrentIndex(index)
            if index == 32 : 
                index = self.PinD_7_val_combo.findText(type, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.PinD_7_val_combo.setCurrentIndex(index) 


    def LoadConfigurationFromFile(self):
        ##############################################################################
        #  This function load configuration from text file  to configure script GUI  #
        #  INPUT :                                                                   #
        #      This function take no arguements except self                          #
        #  OUTPUT :                                                                  #
        #      this function will load the content of file and parsing it then call  # 
        #      two functions :                                                       #
        #            - function to fill DDRD Configuration                           #
        #            - function to fill PORT Configurations                          #
        ##############################################################################
        # get file name from text line 
        fileName=self.txt_lineEdit.text()
        try : 
            # check if the file exist or not 
            file = open(fileName, "r")
            lines = file.readlines()
            file.close()
            print(len(lines))
            # update DDR combo boxes 
            i = 1;
            for line in lines[1:33] : 
                line = line.strip()
                if line.find("DIO_PIN_INIT_INPUT") != -1 :
                    print("Input"+ "   " + str(i))
                    self.FillDDRCombos(i , "Input")
                elif line.find("DIO_PIN_INIT_OUTPUT") != -1 : 
                    self.FillDDRCombos(i , "Output")
                else : 
                    print ("other"+ "   " + str(i))
                i+=1
            
            #udpate PIN Values Comboxes 
            i = 45 
            for line in lines [44:78] :
                line = line.strip()
                if line.find("DIO_PIN_INIT_LOW") != -1 :
                    self.FillVALCombos(i-44 , "LOW")
                elif line.find("DIO_PIN_INIT_HIGH") != -1 : 
                    self.FillVALCombos(i-44 , "HIGH")
                else : 
                    print ("other"+ "   " + str(i))
                i+=1

        except IOError:
            #file does not exist 
            print("File not found ") 









#-------------------------------------------End read from file function ---------------------------

    def retranslateUi(self, create):
        create.setWindowTitle(QtGui.QApplication.translate("create", "Dio Configurator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("create", "AVR DIO Pin Configurations ", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_1_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_1_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_1_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_3_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_3_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_3_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("create", "PinA_7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("create", "PinA_5", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("create", "PinA_0", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_5_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_5_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_5_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("create", "PinA_3", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_2_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_2_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_2_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("create", "PinA_2", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_6_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_6_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_6_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("create", "PinA_4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("create", "PinA_1", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_0_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_0_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_0_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("create", "PinA_6", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_4_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_4_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_4_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_7_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_7_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_7_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("create", "Port A configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("create", "PIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("create", "DDR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("create", "VALUE", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_0_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_0_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_1_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_1_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_2_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_2_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_3_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_3_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_4_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_4_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_5_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_5_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_6_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_6_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_7_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinA_7_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_1_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_1_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_1_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_3_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_3_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_3_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setText(QtGui.QApplication.translate("create", "PinC_7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setText(QtGui.QApplication.translate("create", "PinC_5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setText(QtGui.QApplication.translate("create", "PinC_0", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_5_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_5_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_5_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setText(QtGui.QApplication.translate("create", "PinC_3", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_2_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_2_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_2_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setText(QtGui.QApplication.translate("create", "PinC_2", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_6_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_6_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_6_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setText(QtGui.QApplication.translate("create", "PinC_4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setText(QtGui.QApplication.translate("create", "PinC_1", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_0_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_0_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_0_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setText(QtGui.QApplication.translate("create", "PinC_6", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_4_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_4_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_4_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_7_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_7_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_7_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setText(QtGui.QApplication.translate("create", "Port C configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_67.setText(QtGui.QApplication.translate("create", "PIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_68.setText(QtGui.QApplication.translate("create", "DDR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_69.setText(QtGui.QApplication.translate("create", "VALUE", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_0_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_0_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_1_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_1_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_2_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_2_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_3_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_3_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_4_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_4_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_5_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_5_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_6_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_6_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_7_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinC_7_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_1_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_1_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_1_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_3_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_3_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_3_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("create", "PinB_7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("create", "PinB_5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("create", "PinB_0", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_5_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_5_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_5_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("create", "PinB_3", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_2_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_2_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_2_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("create", "PinB_2", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_6_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_6_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_6_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("create", "PinB_4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("create", "PinB_1", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_0_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_0_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_0_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("create", "PinB_6", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_4_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_4_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_4_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_7_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_7_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_7_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("create", "Port B configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("create", "PIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("create", "DDR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("create", "VALUE", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_0_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_0_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_1_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_1_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_2_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_2_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_3_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_3_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_4_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_4_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_5_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_5_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_6_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_6_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_7_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinB_7_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_1_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_1_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_1_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_3_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_3_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_3_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("create", "PinD_7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("create", "PinD_5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate("create", "PinD_0", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_5_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_5_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_5_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_49.setText(QtGui.QApplication.translate("create", "PinD_3", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_2_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_2_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_2_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("create", "PinD_2", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_6_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_6_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_6_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_51.setText(QtGui.QApplication.translate("create", "PinD_4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("create", "PinD_1", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_0_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_0_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_0_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("create", "PinD_6", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_4_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_4_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_4_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_7_ddr_combo.setItemText(0, QtGui.QApplication.translate("create", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_7_ddr_combo.setItemText(1, QtGui.QApplication.translate("create", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_7_ddr_combo.setItemText(2, QtGui.QApplication.translate("create", "Input_Pullup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate("create", "Port D configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("create", "PIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("create", "DDR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("create", "VALUE", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_0_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_0_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_1_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_1_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_2_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_2_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_3_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_3_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_4_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_4_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_5_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_5_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_6_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_6_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_7_val_combo.setItemText(0, QtGui.QApplication.translate("create", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.PinD_7_val_combo.setItemText(1, QtGui.QApplication.translate("create", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_70.setText(QtGui.QApplication.translate("create", "File Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("create", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("create", "load", None, QtGui.QApplication.UnicodeUTF8))

