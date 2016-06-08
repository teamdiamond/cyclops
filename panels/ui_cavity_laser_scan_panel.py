# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cavity_laser_scan.ui'
#
# Created: Thu Dec 04 11:44:47 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName(_fromUtf8("Panel"))
        Panel.resize(701, 643)
        Panel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_scan_button = QtGui.QPushButton(Panel)
        self.start_scan_button.setGeometry(QtCore.QRect(30, 580, 121, 41))
        self.start_scan_button.setObjectName(_fromUtf8("start_scan_button"))
        self.stop_scan_button = QtGui.QPushButton(Panel)
        self.stop_scan_button.setGeometry(QtCore.QRect(260, 580, 121, 41))
        self.stop_scan_button.setObjectName(_fromUtf8("stop_scan_button"))
        self.save_scan_button = QtGui.QPushButton(Panel)
        self.save_scan_button.setGeometry(QtCore.QRect(500, 580, 121, 41))
        self.save_scan_button.setObjectName(_fromUtf8("save_scan_button"))
        self.doubleSpinBox_start_F = QtGui.QDoubleSpinBox(Panel)
        self.doubleSpinBox_start_F.setGeometry(QtCore.QRect(170, 540, 62, 22))
        self.doubleSpinBox_start_F.setObjectName(_fromUtf8("doubleSpinBox_start_F"))
        self.label_2 = QtGui.QLabel(Panel)
        self.label_2.setGeometry(QtCore.QRect(50, 540, 131, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Panel)
        self.label_3.setGeometry(QtCore.QRect(280, 540, 111, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Panel)
        self.label_4.setGeometry(QtCore.QRect(530, 540, 61, 23))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.doubleSpinBox_stop_f = QtGui.QDoubleSpinBox(Panel)
        self.doubleSpinBox_stop_f.setGeometry(QtCore.QRect(390, 540, 62, 22))
        self.doubleSpinBox_stop_f.setObjectName(_fromUtf8("doubleSpinBox_stop_f"))
        self.doubleSpinBox_step_f = QtGui.QDoubleSpinBox(Panel)
        self.doubleSpinBox_step_f.setGeometry(QtCore.QRect(590, 540, 62, 22))
        self.doubleSpinBox_step_f.setObjectName(_fromUtf8("doubleSpinBox_step_f"))
        self.doubleSpinBox_coarse_wav = QtGui.QDoubleSpinBox(Panel)
        self.doubleSpinBox_coarse_wav.setGeometry(QtCore.QRect(230, 490, 62, 22))
        self.doubleSpinBox_coarse_wav.setObjectName(_fromUtf8("doubleSpinBox_coarse_wav"))
        self.doubleSpinBox_int_time = QtGui.QDoubleSpinBox(Panel)
        self.doubleSpinBox_int_time.setGeometry(QtCore.QRect(480, 490, 62, 22))
        self.doubleSpinBox_int_time.setObjectName(_fromUtf8("doubleSpinBox_int_time"))
        self.label_5 = QtGui.QLabel(Panel)
        self.label_5.setGeometry(QtCore.QRect(110, 490, 121, 23))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Panel)
        self.label_6.setGeometry(QtCore.QRect(350, 490, 111, 23))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(_translate("Panel", "Form", None))
        self.start_scan_button.setText(_translate("Panel", "START SCAN", None))
        self.stop_scan_button.setText(_translate("Panel", "STOP SCAN", None))
        self.save_scan_button.setText(_translate("Panel", "SAVE", None))
        self.label_2.setText(_translate("Panel", "start frequency [GHz]", None))
        self.label_3.setText(_translate("Panel", "Stop frequency [GHz]", None))
        self.label_4.setText(_translate("Panel", "Step [GHz]", None))
        self.label_5.setText(_translate("Panel", "coarse wavlength [nm]", None))
        self.label_6.setText(_translate("Panel", "integration time [msec]", None))

from chaco_plot import TimeTracePlot