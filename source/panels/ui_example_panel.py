# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Tue Feb 15 19:22:35 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(400, 300)
        Panel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.test_value = QtGui.QSpinBox(Panel)
        self.test_value.setGeometry(QtCore.QRect(9, 61, 33, 20))
        self.test_value.setMinimum(1)
        self.test_value.setMaximum(100)
        self.test_value.setSingleStep(2)
        self.test_value.setProperty("value", 10)
        self.test_value.setObjectName("test_value")
        self.float_test_value = QtGui.QDoubleSpinBox(Panel)
        self.float_test_value.setEnabled(False)
        self.float_test_value.setGeometry(QtCore.QRect(100, 80, 49, 21))
        self.float_test_value.setObjectName("float_test_value")
        self.string_test_value = QtGui.QLineEdit(Panel)
        self.string_test_value.setGeometry(QtCore.QRect(9, 217, 133, 20))
        self.string_test_value.setObjectName("string_test_value")
        self.slider_value = QtGui.QSlider(Panel)
        self.slider_value.setGeometry(QtCore.QRect(170, 40, 160, 21))
        self.slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.slider_value.setObjectName("slider_value")
        self.check_value = QtGui.QCheckBox(Panel)
        self.check_value.setGeometry(QtCore.QRect(200, 80, 70, 17))
        self.check_value.setObjectName("check_value")
        self.radio1 = QtGui.QRadioButton(Panel)
        self.radio1.setGeometry(QtCore.QRect(190, 150, 82, 17))
        self.radio1.setChecked(True)
        self.radio1.setObjectName("radio1")
        self.test_group = QtGui.QButtonGroup(Panel)
        self.test_group.setObjectName("test_group")
        self.test_group.addButton(self.radio1)
        self.radio2 = QtGui.QRadioButton(Panel)
        self.radio2.setGeometry(QtCore.QRect(190, 170, 82, 17))
        self.radio2.setObjectName("radio2")
        self.test_group.addButton(self.radio2)
        self.radio3 = QtGui.QRadioButton(Panel)
        self.radio3.setGeometry(QtCore.QRect(190, 200, 82, 17))
        self.radio3.setObjectName("radio3")
        self.test_group.addButton(self.radio3)
        self.do_something = QtGui.QPushButton(Panel)
        self.do_something.setGeometry(QtCore.QRect(70, 260, 75, 23))
        self.do_something.setObjectName("do_something")
        self.do_something_else = QtGui.QPushButton(Panel)
        self.do_something_else.setGeometry(QtCore.QRect(174, 250, 131, 23))
        self.do_something_else.setObjectName("do_something_else")

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(QtGui.QApplication.translate("Panel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.string_test_value.setText(QtGui.QApplication.translate("Panel", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.check_value.setText(QtGui.QApplication.translate("Panel", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.radio1.setText(QtGui.QApplication.translate("Panel", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radio2.setText(QtGui.QApplication.translate("Panel", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radio3.setText(QtGui.QApplication.translate("Panel", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.do_something.setText(QtGui.QApplication.translate("Panel", "Push me!", None, QtGui.QApplication.UnicodeUTF8))
        self.do_something_else.setText(QtGui.QApplication.translate("Panel", "Don\'t push me!", None, QtGui.QApplication.UnicodeUTF8))

