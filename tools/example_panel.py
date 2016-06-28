# example_panel.py
#
# auto-created by ui2cyclops.py v20110215, Thu Dec 04 10:19:18 2014

from panel import Panel
from ui_example_panel import Ui_Panel

from PyQt4 import QtCore

class Example(Panel):
    def __init__(self, parent, *arg, **kw):
        Panel.__init__(self, parent, *arg, **kw)

        # designer ui
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

        self.ui.test_value.setValue(self._ins.get_test_value())
        self.ui.float_test_value.setValue(self._ins.get_float_test_value())
        self.ui.string_test_value.setText(self._ins.get_string_test_value())
        self.ui.slider_value.setValue(self._ins.get_slider_value())
        self.ui.check_value.setChecked(self._ins.get_check_value())
        self.ui.radio1.setChecked(self._ins.get_radio1())
        self.ui.radio2.setChecked(self._ins.get_radio2())
        self.ui.radio3.setChecked(self._ins.get_radio3())

        self.ui.test_value.valueChanged.connect(self._set_test_value)
        self.ui.float_test_value.valueChanged.connect(self._set_float_test_value)
        self.ui.string_test_value.textEdited.connect(self._set_string_test_value)
        self.ui.slider_value.sliderMoved.connect(self._set_slider_value)
        self.ui.check_value.toggled.connect(self._set_check_value)
        self.ui.radio1.toggled.connect(self._set_radio1)
        self.ui.radio2.toggled.connect(self._set_radio2)
        self.ui.radio3.toggled.connect(self._set_radio3)

        self.ui.do_something.pressed.connect(self._do_something)
        self.ui.do_something_else.pressed.connect(self._do_something_else)

    def _do_something(self):
        self._ins.do_something()
        return

    def _do_something_else(self):
        self._ins.do_something_else()
        return

    def _set_test_value(self, val):
        self._ins.set_test_value(val)
        return

    def _set_float_test_value(self, val):
        self._ins.set_float_test_value(val)
        return

    def _set_string_test_value(self, val):
        self._ins.set_string_test_value(val)
        return

    def _set_slider_value(self, val):
        self._ins.set_slider_value(val)
        return

    def _set_check_value(self, val):
        self._ins.set_check_value(val)
        return

    def _set_radio1(self, val):
        self._ins.set_radio1(val)
        return

    def _set_radio2(self, val):
        self._ins.set_radio2(val)
        return

    def _set_radio3(self, val):
        self._ins.set_radio3(val)
        return

    def _instrument_changed(self, changes):

        if changes.has_key('test_value'):
            self.ui.test_value.setValue(int(changes['test_value']))

        if changes.has_key('float_test_value'):
            self.ui.float_test_value.setValue(float(changes['float_test_value']))

        if changes.has_key('string_test_value'):
            self.ui.string_test_value.setText(str(changes['string_test_value']))

        if changes.has_key('slider_value'):
            self.ui.slider_value.setValue(int(changes['slider_value']))

        if changes.has_key('check_value'):
            self.ui.check_value.setChecked(bool(changes['check_value']))

        if changes.has_key('radio1'):
            self.ui.radio1.setChecked(bool(changes['radio1']))

        if changes.has_key('radio2'):
            self.ui.radio2.setChecked(bool(changes['radio2']))

        if changes.has_key('radio3'):
            self.ui.radio3.setChecked(bool(changes['radio3']))
