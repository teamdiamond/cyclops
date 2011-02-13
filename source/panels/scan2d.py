# a 2d scan panel
#
# An example of a 2d scanner that scans an area line by line.
# if the instrument is running, the panel gets notified that new
# data is available and gets it from the instrument and caches is
# locally. since this costs cpu runtime, the 2d scan plot is not
# updated on demand, but slower, triggered by the panel timer.
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>
import numpy

from panel import Panel
from ui_scan2d import Ui_Panel

from PyQt4 import QtCore
from PyQt4.Qwt5.Qwt import QwtPlot as Qwt

class Scan2dPanel(Panel):
    def __init__(self, parent, *arg, **kw):
        Panel.__init__(self, parent, *arg, **kw)

        # designer ui  
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

        # setting up the basic plot properties
        # the name is not absolutely required, but gives
        # the plot toolbar a name
        self.ui.plot.set_name('2D Scan')
        self.ui.plot.set_axis_label(Qwt.xBottom, 'x [um]')
        self.ui.plot.set_axis_label(Qwt.yLeft, 'y [um]')

        # enable the cross hair positioning
        # FIXME: also set the crosshair via signal to reflect changes from
        # outside
        self.ui.plot._init_crosshair()
        self.ui.plot.crosshair_set.connect(self._ins.move_abs_xy)
        

        # read the instrument parameters and set the input
        # fields accordingly
        self.ui.xstart.setValue(self._ins.get_xstart())
        self.ui.xstop.setValue(self._ins.get_xstop())
        self.ui.xsteps.setValue(self._ins.get_xsteps())
        self.ui.ystart.setValue(self._ins.get_ystart())
        self.ui.ystop.setValue(self._ins.get_ystop())
        self.ui.ysteps.setValue(self._ins.get_ysteps())
        self.ui.pxtime.setValue(self._ins.get_pixel_time())

        # the reset function prepares the local data cache
        self._reset(True)

        # this flag indicates whether the plot needs to be updated
        self._do_update = False

    # this (slot-)function gets called when the start scan-button
    # is pressed. this connection has already been created in the
    # designer file, but of course the function still needs to be
    # implemented.
    # The function takes into account user input in the fields by
    # sending it to the instrument and making the instrument resize
    # it's data field. Besides that the instrument is only set into
    # a running state, which makes it start the scan (turns off automatically
    # once finished with the scan). This guarantees that operation from
    # the client gives the same result as starting the scan directly
    # at the instrument. Ergo, the panel also monitors the instrument
    # when it's operated from a script, etc.
    def start_scan(self):
        self._ins.set_xstart(self.ui.xstart.value())
        self._ins.set_xstop(self.ui.xstop.value())
        self._ins.set_xsteps(self.ui.xsteps.value())
        self._ins.set_ystart(self.ui.ystart.value())
        self._ins.set_ystop(self.ui.ystop.value())
        self._ins.set_ysteps(self.ui.ysteps.value())
        self._ins.set_pixel_time(self.ui.pxtime.value())
        self._ins.setup_data()

        # FIXME: depending on how the scan device will operate, need
        # also to set a reasonable sampling interval (depends on the
        # blocking routines)
        self._ins.set_is_running(True)

    # To be implemented. So far, the zoom button does not do anything.
    def zoom(self):
        return

    # this method automatically gets called when instrument parameters take
    # a new value, i.e. any get_* or set_* function of the instrument has been
    # called. our instrument calls the get_latest_line_index method on itself
    # after each line scan to make all clients aware that new data is ready.
    # (this value just holds the array index of the newest scanned data line.)
    def _instrument_changed(self, changes):

        # this means that the instrument has just been set on, meaning that
        # we need to reset the local data cache
        if changes.has_key('is_running'):
            self._reset(bool(changes['is_running']))

        # new data is available, processing will take place in another method
        if changes.has_key('last_line_index'):
            self._new_data(int(changes['last_line_index']))

    # the latest available data is in line 'line'. We check what our newest
    # local data is, and get all lines in between. results get picked up by
    # a callback function (non-blocking), then we update the latest data line.
    def _new_data(self, line):
        lines = numpy.arange(self._ins_line + 1, line + 1)
        for l in lines:
            self._ins.get_line(l, callback=self._new_data_cb)
        self._ins_line = line

    # where new data is processed. We add it to the local cache. We use a
    # different counter for the lines than in the new_data function, since
    # they are invoked asynchronously
    def _new_data_cb(self, data, *args):
        self._data[self._local_line+1] = data
        self._local_line += 1
        self._do_update = True

    # preparation of the local data copy (cache).
    def _reset(self, reset):
        if reset:
            self._ins_line = -1
            self._local_line = -1

            self._xvals = self._ins.get_x()
            self._yvals = self._ins.get_y()
            self._data = numpy.zeros((self._xvals.size, self._yvals.size))

            self.ui.plot.set_data(self._data,
                                  self._xvals,
                                  self._yvals)

    # every time the panel timer is called, we update the plot data with
    # the locally cached data
    def timerEvent(self, event):
        if self._do_update:
            self.ui.plot.set_data(self._data, self._xvals, self._yvals)
            self._do_update = False


            
