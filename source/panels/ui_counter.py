# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/counts.ui'
#
# Created: Wed Nov 10 12:21:40 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.counts = HugeDisplay(Panel)
        self.counts.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.counts.setFont(font)
        self.counts.setObjectName("counts")
        self.verticalLayout.addWidget(self.counts)
        self.plot = TimeTracePlot(Panel)
        self.plot.setMinimumSize(QtCore.QSize(0, 150))
        self.plot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plot.setFrameShadow(QtGui.QFrame.Raised)
        self.plot.setObjectName("plot")
        self.verticalLayout.addWidget(self.plot)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Panel)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.t_range = QtGui.QSpinBox(Panel)
        self.t_range.setObjectName("t_range")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.t_range)
        self.label_2 = QtGui.QLabel(Panel)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.integration_time = QtGui.QSpinBox(Panel)
        self.integration_time.setObjectName("integration_time")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.integration_time)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(QtGui.QApplication.translate("Panel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.counts.setText(QtGui.QApplication.translate("Panel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Panel", "time span [s] (0: all time)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Panel", "integration time [ms]", None, QtGui.QApplication.UnicodeUTF8))

from panel import HugeDisplay
from plot.time_trace_plot import TimeTracePlot
