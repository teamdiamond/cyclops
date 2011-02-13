# Line plots
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

from PyQt4 import Qt, QtCore, QtGui
from PyQt4.Qwt5 import Qwt
from plot import Plot

class LinePlotCurve(Qwt.QwtPlotCurve):
    """
    Curve for 2D line plots. No exptras so far, lacks functionality.
    Is, atm, only overloaded QwtPlotCurve with default color cyan.
    """

    def __init__(self, color=Qt.Qt.cyan):
        Qwt.QwtPlotCurve.__init__(self)

        pen = Qt.QPen(color)
        pen.setWidth(2)
        self.setPen(pen)

class LinePlot(Plot):
    """
    Cyclops default line plot. Atm, only reimplementation of Plot.
    """
    def __init__(self, parent):
        Plot.__init__(self, parent)
