# The Cyclops main window
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

import os, sys
from PyQt4 import QtCore, QtGui
from lib import config as _cfg
from ui_main_window import Ui_mainWindow
from panels.panel import Panel, PanelDialog

# some constants
PANEL_CFG = 'user_panels.py'


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # import designer interface
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # load the user panel config
        self._cyclops_dir = os.path.join(os.getcwd(), 'source/gui/cyclops')
        self.load_user_panels()

        # set full screen
        self.setWindowState(QtCore.Qt.WindowMaximized)
 
    def add_panel(self, panel, *arg, **kw):
        p = PanelDialog(panel, *arg, **kw)
        self.ui.mdiArea.addSubWindow(p)

    def load_user_panels(self):
        """
        Loads the user script in which the start-up panel configuration
        is specified.
        """
        add_panel = self.add_panel

        # process the command line args. try to load anything as panel config that
        # ends with .py. if there's no such thing, load the default user config
        args = 0
        for f in sys.argv[1:]:
            if f[-3:] == '.py':
                args += 1
                execfile(f)
        if args == 0:
            execfile(self._cyclops_dir + '/' + PANEL_CFG)
        
