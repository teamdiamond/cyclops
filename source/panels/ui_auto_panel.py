# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/auto_panel.ui'
#
# Created: Wed Nov 10 22:46:16 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AutoPanel(object):
    def setupUi(self, AutoPanel):
        AutoPanel.setObjectName("AutoPanel")
        AutoPanel.resize(304, 229)
        self.verticalLayout = QtGui.QVBoxLayout(AutoPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panelBox = QtGui.QGroupBox(AutoPanel)
        self.panelBox.setCheckable(False)
        self.panelBox.setChecked(False)
        self.panelBox.setObjectName("panelBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.panelBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panel_sampling_lbl = QtGui.QLabel(self.panelBox)
        self.panel_sampling_lbl.setObjectName("panel_sampling_lbl")
        self.horizontalLayout.addWidget(self.panel_sampling_lbl)
        self.panel_sampling = QtGui.QSpinBox(self.panelBox)
        self.panel_sampling.setMinimum(100)
        self.panel_sampling.setMaximum(10000)
        self.panel_sampling.setObjectName("panel_sampling")
        self.horizontalLayout.addWidget(self.panel_sampling)
        self.panel_enabled = QtGui.QCheckBox(self.panelBox)
        self.panel_enabled.setObjectName("panel_enabled")
        self.horizontalLayout.addWidget(self.panel_enabled)
        self.verticalLayout.addWidget(self.panelBox)
        self.instrumentBox = QtGui.QGroupBox(AutoPanel)
        self.instrumentBox.setObjectName("instrumentBox")
        self.gridLayout = QtGui.QGridLayout(self.instrumentBox)
        self.gridLayout.setObjectName("gridLayout")
        self.instrument_running = QtGui.QCheckBox(self.instrumentBox)
        self.instrument_running.setObjectName("instrument_running")
        self.gridLayout.addWidget(self.instrument_running, 0, 0, 1, 1)
        self.instrument_recording = QtGui.QCheckBox(self.instrumentBox)
        self.instrument_recording.setObjectName("instrument_recording")
        self.gridLayout.addWidget(self.instrument_recording, 0, 1, 1, 1)
        self.instrument_save = QtGui.QPushButton(self.instrumentBox)
        self.instrument_save.setObjectName("instrument_save")
        self.gridLayout.addWidget(self.instrument_save, 0, 2, 1, 1)
        self.instrument_meta = QtGui.QPlainTextEdit(self.instrumentBox)
        self.instrument_meta.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("TlwgTypewriter")
        self.instrument_meta.setFont(font)
        self.instrument_meta.setObjectName("instrument_meta")
        self.gridLayout.addWidget(self.instrument_meta, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.instrumentBox)

        self.retranslateUi(AutoPanel)
        QtCore.QMetaObject.connectSlotsByName(AutoPanel)

    def retranslateUi(self, AutoPanel):
        AutoPanel.setWindowTitle(QtGui.QApplication.translate("AutoPanel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.panelBox.setTitle(QtGui.QApplication.translate("AutoPanel", "Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.panel_sampling_lbl.setText(QtGui.QApplication.translate("AutoPanel", "update interval [ms]", None, QtGui.QApplication.UnicodeUTF8))
        self.panel_enabled.setText(QtGui.QApplication.translate("AutoPanel", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.instrumentBox.setTitle(QtGui.QApplication.translate("AutoPanel", "Instrument", None, QtGui.QApplication.UnicodeUTF8))
        self.instrument_running.setText(QtGui.QApplication.translate("AutoPanel", "Running", None, QtGui.QApplication.UnicodeUTF8))
        self.instrument_recording.setText(QtGui.QApplication.translate("AutoPanel", "Recording", None, QtGui.QApplication.UnicodeUTF8))
        self.instrument_save.setText(QtGui.QApplication.translate("AutoPanel", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.instrument_meta.setPlainText(QtGui.QApplication.translate("AutoPanel", "Metadata...", None, QtGui.QApplication.UnicodeUTF8))

