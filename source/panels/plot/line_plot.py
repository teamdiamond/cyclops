# Line plots
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

from PyQt4 import Qt, QtCore, QtGui
from PyQt4.Qwt5 import Qwt
from plot import Plot

class LinePlotCurve(Qwt.QwtPlotCurve):
    """
    Curve for 2D line plots. No extras so far, lacks functionality.
    Is, atm, only overloaded QwtPlotCurve with default color cyan.
    """

    def __init__(self, color=Qt.Qt.cyan, width=2,
                 style=Qwt.QwtPlotCurve.Lines):
        Qwt.QwtPlotCurve.__init__(self)

        pen = Qt.QPen(color)
        pen.setWidth(width)
        self.setPen(pen)
        self.setStyle(style)

class LinePlot(Plot):
    """
    Cyclops default line plot. Atm, only reimplementation of Plot.
    """
    def __init__(self, parent):
        Plot.__init__(self, parent)


    def add_curve(self, x, y, color=Qt.Qt.cyan, width=2,
                  style=Qwt.QwtPlotCurve.Lines):
        curve = LinePlotCurve(color, width, style)
        curve.attach(self)
        curve.setData(x, y)
        self.replot()
        
