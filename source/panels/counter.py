# a basic counter panel
#
# this panel shows the current countrate of a counter instrument (a dummy for
# this example). the refresh rate is given by the panel timer interval, it
# can be set when creating the panel. A time trace is shown in a special time
# trace plot (a line plot that only keeps a certain time of history and deletes
# all points before continously, so only the most recent history is visible)
# 
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

from panel import Panel
from ui_counter import Ui_Panel

from PyQt4 import QtCore
from PyQt4.Qwt5.Qwt import QwtPlot as Qwt

class CounterPanel(Panel):
    def __init__(self, parent, *arg, **kw):
        Panel.__init__(self, parent, *arg, **kw)

        # designer ui:
        # the visual appearance has been created with Qt Designer and then
        # converted into a python file by pyuic4. with these commands (import
        # above) we set up the GUI
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

        # set up the plot. the used properties are available for any plot,
        # although the used plot class is a TimeTracePlot
        self.ui.plot.set_name('Counter Trace')
        self.ui.plot.set_axis_label(Qwt.xBottom, 't [s]')
        self.ui.plot.set_axis_label(Qwt.yLeft, 'counts [Hz]')
        self.ui.plot.set_axis_format(Qwt.yLeft, format='E', precision=0)
        
        # read the instrument parameters (only one) and populate GUI elements
        self.ui.integration_time.setValue(self._ins.get_integration_time())

        # set other defaults (for the TimeTracePlot)
        self.ui.plot.set_t_range(30)
        self.ui.t_range.setValue(30)

        # connect signals/slots. can in principle also be done via Designer --
        # for an example see the scan2d panel example
        self.ui.t_range.valueChanged.connect(self.ui.plot.set_t_range)
        self.ui.integration_time.valueChanged.connect(self.integration_time_changed)

    # function to set the integration time in the instrument
    # every panel (if set up with one) has it's instrument stored in self._ins
    @QtCore.pyqtSlot(int)
    def integration_time_changed(self, t):
        self._ins.set_integration_time(t)

    # the timer event is called at every timer interval, which can be set in the
    # panel configuration file and defaults to 250ms
    def timerEvent(self, event):

        # always make sure to call the parent class function
        Panel.timerEvent(self, event)

        # call the countrate function, the return value will be called on
        # the function _counts_cb in order to keep the GUI responsive
        self._ins.get_countrate(callback=self._counts_cb)

    # the callback function actually sets the display and adds the point
    # to the plot
    def _counts_cb(self, cr, *args):
        self.ui.counts.setNum(cr)
        self.ui.plot.add_point(cr)
