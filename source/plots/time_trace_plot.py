# a plot type for live time traces
#
# Is essentially a line plot, but takes care of the x axis itself,
# and can continously remove the beginning of the internal buffer to
# always display the same time range.
#
# TODO: doesn't look great yet, because qwt autoscale doesn't fit the canvas
# precisely to the data. Do manually at some point.
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

import numpy as np
import time
from PyQt4 import QtCore 
from line_plot import LinePlot, LinePlotCurve

class TimeTracePlot(LinePlot):
    def __init__(self, parent):
        LinePlot.__init__(self, parent)

        # init members 
        self._trange = 0.0
        self._data = np.array([[0,0]])
        self._t0 = time.time()

        # set up plot lines
        self._curve = LinePlotCurve()
        self._curve.attach(self)

        # display update
        self.update()

    def add_point(self, y):
        """
        Adds a new point to the count rate curve. Removes continuously
        the first part of the data, to keep the points within the
        specified timerange.
        """
        # append the data points
        t = time.time()
        self._data = np.append(self._data, [[t-self._t0, y]], axis=0)
        
        # only keep latest points, specified by xrange
        if self._trange != 0.0:
            while t-self._t0-self._data[0][0] > self._trange:
                self._data = self._data[1:]

        # add to plot and redraw
        self._curve.setData(self._data[:, 0], \
                self._data[:, 1] )
        self.update()

    @QtCore.pyqtSlot(int)
    def set_t_range(self, t):
        """
        Sets the time range for the plot (seconds).
        """
        self._trange = int(t)

    def reset(self):
        """
        reset()

        deletes current data. 
        """
        self._data = np.array([[0,0]])
        self._t0 = time.time()
        self.update()
        
