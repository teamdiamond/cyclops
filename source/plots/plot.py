# Common plot elements for uniform layout of all plots
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

import numpy as np
from os.path import join
from PyQt4 import Qt, QtCore, QtGui
from PyQt4.Qwt5 import Qwt
from config import icon_dir


# The plot base class
class Plot(Qwt.QwtPlot):
    """
    Re-implementation of the qwt plot class for common look&feel.
    Provides a default toolbar with coordinate display and a zoom function.

    Other notable methods:

    - set_axis_format: to format axis display
    - set_axis_label
    - set_name: give the plot a name for identification (very optional)
    - update: refresh and redraw the plot
    """

    # signals
    crosshair_set = QtCore.pyqtSignal(float, float)

    def __init__(self, parent):
        Qwt.QwtPlot.__init__(self, parent)

        # common layout for all plots
        self.name = ''
        self.plotLayout().setSpacing(2)
        self.plotLayout().setMargin(2)
        self.setCanvasBackground(Qt.Qt.black)
        self.setCanvasLineWidth(1)

        # initialize all common plot components
        self._spy = PlotSpy(self.canvas())
        self._init_toolbar()
        self._init_axes()
        #self._init_zooming()
        self._init_tracking()
        #self._init_crosshair()

        # colors and color maps
        self._builtin_cmaps = {
            'jack': CmapJack,
            }

        self.cmaps = {}
        for k in self._builtin_cmaps:
            self.cmaps[k] = self._builtin_cmaps[k]


    ### Axis management ###
    def _init_axes(self):
        self._axes = [Qwt.QwtPlot.xBottom, Qwt.QwtPlot.yLeft, \
                         Qwt.QwtPlot.xTop, Qwt.QwtPlot.yRight]

        self._axis_limits = {
            Qwt.QwtPlot.xBottom : [0., 1.],
            Qwt.QwtPlot.yLeft : [0., 1.],
            Qwt.QwtPlot.xTop : [0., 1.],
            Qwt.QwtPlot.yRight : [0., 1.],
            }

        for a in self._axes:
            self.axisWidget(a).setTitle(Qwt.QwtText(''))
            self.set_axis_format(a)
            self.setAxisAutoScale(a)
            self.add_axis_context_menu(a)

    # overload the axis scale setting to include the limits dict
    def setAxisAutoScale(self, axis, auto=True):
        if auto:
            Qwt.QwtPlot.setAxisAutoScale(self, axis)
        else:
            self.setAxisScale(axis,
                         self._axis_limits[axis][0],
                         self._axis_limits[axis][1])
        self.replot()

    def setAxisScale(self, axis, min, max, step=0):
        Qwt.QwtPlot.setAxisScale(self, axis, min, max, step)

        self._axis_limits[axis] = [min, max]
        self.replot()

    def _set_axis_limit(self, axis, which, val):
        self._axis_limits[axis][which] = val

    def add_axis_context_menu(self, axis):
        self.axisWidget(axis).setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.axisWidget(axis).customContextMenuRequested.connect(
            lambda pos: self.create_axis_context_menu(axis, pos))

    def create_axis_context_menu(self, axis, pos):
        m = AxisContextMenu(self,
                            self.axisAutoScale(axis),
                            self._axis_limits[axis][0],
                            self._axis_limits[axis][1])
        m.auto_scale_set.connect(
            lambda auto: self.setAxisAutoScale(axis, auto))
        m.lower_limit_changed.connect(
            lambda val: self._set_axis_limit(axis, 0, val))
        m.upper_limit_changed.connect(
            lambda val: self._set_axis_limit(axis, 1, val))
        m.aboutToHide.connect(
            lambda: self.setAxisAutoScale(axis,
                                          self.axisAutoScale(axis)))
        m.exec_(self.axisWidget(axis).mapToGlobal(pos))

    ### Cross hair management ###
        
    # not used per default, user must enable
    def _init_crosshair(self):
        self._cross_picker = Qwt.QwtPlotPicker(
            Qwt.QwtPlot.xBottom,
            Qwt.QwtPlot.yLeft,
            Qwt.QwtPicker.PointSelection | Qwt.QwtPicker.DragSelection,
            Qwt.QwtPlotPicker.CrossRubberBand,
            Qwt.QwtPicker.AlwaysOn,
            self.canvas())
        self._cross_picker.setRubberBandPen(QtGui.QPen(Qt.Qt.green))
        self._cross_picker.setTrackerPen(QtGui.QPen(Qt.Qt.green))
        self._cross_picker.selected.connect(self._drag_cross_marker)
        self._cross_picker.setEnabled(False)

        self._cross_marker = Qwt.QwtPlotMarker()
        self._cross_marker.setLineStyle(Qwt.QwtPlotMarker.Cross)
        self._cross_marker.setLinePen(QtGui.QPen(Qt.Qt.yellow,
                                                 1,
                                                 Qt.Qt.SolidLine))
        self._cross_marker.setValue(0.0, 0.0)
        self._cross_marker.attach(self)
        self._cross_marker.hide()

        self._cross_btn = QtGui.QAction(
            QtGui.QIcon(join(icon_dir, 'goto_16.png')),
            'Set Crosshair',
            self.toolbar)
        self.toolbar.insertAction(self._coordinate_ico, self._cross_btn)
        self._cross_btn.setCheckable(True)
        self._cross_btn.toggled.connect(self._enable_crosshair)
        
    def _enable_crosshair(self, enable):
        if enable and hasattr(self, '_zoom_btn'):
            self._zoom_btn.setChecked(not enable)        
        
        self._cross_picker.setEnabled(enable)        
        if enable:
            self._cross_marker.show()
        else:
            self._cross_marker.hide()
        self.replot()
    
    def _drag_cross_marker(self, point):
        self._cross_marker.setValue(point)
        self._cross_marker.show()
        self.crosshair_set.emit(self._cross_marker.xValue(),
                                self._cross_marker.yValue())
        self.replot()

    def set_cross_marker(self, x, y):
        self._cross_marker.setValue(QtCore.QPointF(x, y))
        self.replot()
    
    ### Tool bar management ###    
    def _init_toolbar(self):
        window = self.parent().parent()
        self.toolbar = Qt.QToolBar(self)
        self.toolbar.setWindowTitle('Plot')       
        window.addToolBar(self.toolbar)

    def _init_tracking(self):
        self.connect(self._spy, Qt.SIGNAL('mouseMove'),
                     self._set_coordinates)

        self._coordinate_ico = self.toolbar.addAction(QtGui.QIcon(
                join(icon_dir, 'info_16.png')), 'Coordinates')
        self._coordinate_ico.setEnabled(False)
        self._coordinate_lbl = QtGui.QLabel(self.toolbar)
        self.toolbar.addWidget(self._coordinate_lbl) 

    # not enabled by default, user must do that
    def _init_zooming(self):
        # FIXME: zoom base should be set automatically. could solve this by
        # introducing a method for manual axis-updates that the user calls
        # and that sets then the zoom base

        self._zoomer = Qwt.QwtPlotZoomer(Qwt.QwtPlot.xBottom,
                                         Qwt.QwtPlot.yLeft,
                                         Qwt.QwtPicker.DragSelection,
                                         Qwt.QwtPicker.AlwaysOff,
                                         self.canvas())
        self._zoomer.setRubberBandPen(Qt.QPen(Qt.Qt.red))
        self._zoomer.setEnabled(False)

        self._zoom_btn = self.toolbar.addAction(QtGui.QIcon(\
                join(icon_dir, 'zoom_16.png')), 'Zooming')
        self._zoom_btn.setCheckable(True)
        self._zoom_btn.toggled.connect(self._enable_zooming)

    def _enable_zooming(self, enable):
        # cross hair not always available
        if enable and hasattr(self, '_cross_picker'):
            self._cross_btn.setChecked(not enable)

        self._zoomer.setEnabled(enable)
        if not enable:
            for a in self.axes:
                self.setAxisAutoScale(a)
                self.replot()

    def _set_coordinates(self, pos):
        self._coordinate_lbl.setText(
            'x = %+.4g, y = %.4g' % (
            self.invTransform(Qwt.QwtPlot.xBottom, pos.x()),
            self.invTransform(Qwt.QwtPlot.yLeft, pos.y())))

    def set_axis_format(self, axis, format='f', precision=1):
        """
        Arguments:
        ==========

        axis : an axis identifier (one of Qwt.QwtPlot.xBottom,
               Qwt.QwtPlot.yLeft, ...)

        format : the output format. See the Qt documentation.

        precision : integer
                    determines figures after the floating point.
        """
        self.setAxisScaleDraw(axis, ScaleDraw(format, precision))
        
    def set_axis_label(self, axis, label):
        """
        Arguments:
        ==========

        axis : a Qwt axis identifier

        label : string
          the new label for the axis

        """
        self.axisWidget(axis).setTitle(label)

    def set_name(self, name):
        self.name = name
        self.toolbar.setWindowTitle('Plot: '+ self.name)

    def update(self):
        self.replot()

# color maps
class Cmap (Qwt.QwtLinearColorMap):
    def __init__(self, color_lo, color_hi):
        Qwt.QwtLinearColorMap.__init__(self, color_lo, color_hi)

        self.color_lo = color_lo
        self.color_hi = color_hi

class CmapJack(Cmap):
    """
    A color map that ranges from blue to red with white in between.
    Colors:
    0 = blue
    0.5 = white
    1 = red
    """
    def __init__(self):
        """
        The init method only calls the parent's constructor and sets the
        colors.
        """
        Cmap.__init__(self, Qt.Qt.darkBlue, Qt.Qt.darkRed)
        self.addColorStop(0.5, Qt.Qt.white)

# Plot Elements/Components
class ScaleDraw(Qwt.QwtScaleDraw):
    """
    Axis for plots. Propagates specified formatting options, for regular
    or E-Notation, and floating-point precision. See the Qt
    documentation for format and precision arguments.
    """
    def __init__(self, format='f', precision=1):
        Qwt.QwtScaleDraw.__init__(self)

        self.format = format
        self.precision = precision

    def label(self, value):
        s = QtCore.QString()
        s.setNum(value, self.format, self.precision)
        return Qwt.QwtText(s)
    
# class ScaleDraw

class PlotSpy(Qt.QObject):
    """
    This class is an event filter for the canvas. It is installed
    in the plot, parent is the canvas. It takes care of basic Qt events
    that require an event filter, like mouse tracking.
    """
    
    def __init__(self, parent):
        Qt.QObject.__init__(self, parent)
        parent.setMouseTracking(True)
        parent.installEventFilter(self)

    # __init__()
        
    def eventFilter(self, _, event):
        if event.type() == Qt.QEvent.MouseMove:
            self.emit(Qt.SIGNAL("mouseMove"), event.pos())
        return False
    
    # eventFilter()

# class PlotSpy

class AxisContextMenu(QtGui.QMenu):

    auto_scale_set = QtCore.pyqtSignal(bool)
    lower_limit_changed = QtCore.pyqtSignal(float)
    upper_limit_changed = QtCore.pyqtSignal(float)
    
    def __init__(self, parent, auto, lim_lo, lim_hi):
        QtGui.QMenu.__init__(self, parent)

        self.lim_lo = lim_lo
        self.lim_hi = lim_hi
        self.setTitle('Limits')
        
        self.auto = QtGui.QAction('Autoscale', self)
        self.auto.setCheckable(True)
        self.auto.setChecked(auto)
        self.auto.toggled.connect(self.set_auto_limit)
        self.addAction(self.auto)

        self.lim1 = AxisContextLineEdit(self, str(lim_lo))
        self.lim1.value_changed.connect(self.set_lower_limit)
        self.addAction(self.lim1)

        self.lim2 = AxisContextLineEdit(self, str(lim_hi))
        self.lim2.value_changed.connect(self.set_upper_limit)
        self.addAction(self.lim2)
        
    def set_auto_limit(self, val):
        self.auto_scale_set.emit(val)

    def set_lower_limit(self, val):
        if val == '': val = 0
        self.lim_lo = float(val)
        self.lower_limit_changed.emit(self.lim_lo)

    def set_upper_limit(self, val):
        if val == '': val = 0
        self.lim_hi = float(val)
        self.upper_limit_changed.emit(self.lim_hi)

# class AxisContextMenu
        
class AxisContextLineEdit(QtGui.QWidgetAction):

    value_changed = QtCore.pyqtSignal(str)

    def __init__(self, parent, value):
        QtGui.QWidgetAction.__init__(self, parent)
        self._value = value
        self._parent = parent

    def createWidget(self, parent):
        w = QtGui.QLineEdit(self._value, parent)
        w.textEdited.connect(self.set_value)
        w.editingFinished.connect(self.confirm_value)
        return w

    def set_value(self, val):
        self._value = val

    def confirm_value(self):
        self.value_changed.emit(self._value)
        
# class AxisContextLineEdit
