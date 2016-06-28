# cyclopean_example.py
#
# auto-created by ui2cyclops.py v20110215, Thu Dec 04 10:19:18 2014

from instrument import Instrument
from cyclopean_instrument import CyclopeanInstrument
import types

class cyclopean_example(CyclopeanInstrument):
    def __init__(self, name, address=None):
        CyclopeanInstrument.__init__(self, name, tags=[])

        self._supported = {
            'get_running': False,
            'get_recording': False,
            'set_running': False,
            'set_recording': False,
            'save': False,
            }

        self.add_parameter('test_value',
                           type=types.IntType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           minval=1,
                           maxval=100,
                           doc='')
        self._test_value = 10

        self.add_parameter('float_test_value',
                           type=types.FloatType,
                           flags=Instrument.FLAG_GET,
                           units='',
                           minval=0.0,
                           maxval=99.0,
                           doc='')
        self._float_test_value = 0.0

        self.add_parameter('string_test_value',
                           type=types.StringType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc='')
        self._string_test_value = 'Test'

        self.add_parameter('slider_value',
                           type=types.IntType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           minval=0,
                           maxval=99,
                           doc='')
        self._slider_value = 0

        self.add_parameter('check_value',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc='')
        self._check_value = False

        self.add_parameter('radio1',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc='')
        self._radio1 = True

        self.add_parameter('radio2',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc='')
        self._radio2 = False

        self.add_parameter('radio3',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc='')
        self._radio3 = False

        self.add_function('do_something')

        self.add_function('do_something_else')

    def do_get_test_value(self):
        return self._test_value

    def do_set_test_value(self, val):
        self._test_value = val

    def do_get_float_test_value(self):
        return self._float_test_value

    def do_set_float_test_value(self, val):
        self._float_test_value = val

    def do_get_string_test_value(self):
        return self._string_test_value

    def do_set_string_test_value(self, val):
        self._string_test_value = val

    def do_get_slider_value(self):
        return self._slider_value

    def do_set_slider_value(self, val):
        self._slider_value = val

    def do_get_check_value(self):
        return self._check_value

    def do_set_check_value(self, val):
        self._check_value = val

    def do_get_radio1(self):
        return self._radio1

    def do_set_radio1(self, val):
        self._radio1 = val

    def do_get_radio2(self):
        return self._radio2

    def do_set_radio2(self, val):
        self._radio2 = val

    def do_get_radio3(self):
        return self._radio3

    def do_set_radio3(self, val):
        self._radio3 = val

    def do_something(self, *arg, **kw):
        pass

    def do_something_else(self, *arg, **kw):
        pass

    def save(self, meta=""): # inherited doesn't do any saving. Implement.
        CyclopeanInstrument.save(self, meta)

        return

    def _start_running(self):
        CyclopeanInstrument._start_running(self)

        return

    def _stop_running(self):
        CyclopeanInstrument._start_running(self)

        return

    def _sampling_event(self):
        return True # sampling timer runs until return value of this is False
