# a dummy counter instrument
#
# has a default count rate of 1e5/s. depending on the set integration time,
# can provide counts and countrate, including some noise.
# New data is generated at every sampling event. This means the instrument can
# be run (from the console, or elsewhere) without being blocking. This principle
# can be used generally to achieve 'fake multithreading', i.e. many instruments
# can be operated simultaneously.

from instrument import Instrument
from cyclopean_instrument import CyclopeanInstrument
import types
import time
import math
from numpy import random

class dummy_counter(CyclopeanInstrument):
    def __init__(self, name, address=None):
        CyclopeanInstrument.__init__(self, name, tags=['measure', 'generate', 'virtual'])

        # relevant parameters
        self.add_parameter('integration_time',
                           type=types.FloatType,
                           flags=Instrument.FLAG_SET | Instrument.FLAG_SOFTGET,
                           units='ms',
                           minval=1.0, maxval=10000.0,
                           doc="""
                           How long to count to determine the rate.
                           """)

        self.add_parameter('counts',
                           type=types.IntType,
                           flags=Instrument.FLAG_GET,
                           units='counts',
                           tags=['measure'],
                           doc="""
                           Returns the counts acquired during the last counting period.
                           """)

        self.add_parameter('countrate',
                           type=types.IntType,
                           flags=Instrument.FLAG_GET,
                           units='Hz',
                           tags=['measure'],
                           doc="""
                           Returns the count rate based on the current count value.
                           """)

        # init parameters
        self.set_integration_time(20.0)
        self._counts = 0
        self._countrate = 0

        # instruments we need to access
        import qt
        self._ins_pos = qt.instruments['dummy_pos']

    def do_set_integration_time(self, val):
        self._integration_time = val

    def do_get_integration_time(self):
        return self._integration_time

    def do_get_counts(self):
        return self._counts

    def do_get_countrate(self):
        return self._countrate

    def _stop_running(self):
        self._counts = 0
        self._countrate = 0

    # if this function returns False, the sampling timer gets stopped.
    # it gets re-started once set_is_running(True) gets called again.
    def _sampling_event(self):
        if not self._is_running:
            return False
        
        self._read_counts()
        return True
        
    def _read_counts(self):
        self._counts = self._dummy_counts()
        self._countrate = self._counts / (self._integration_time*0.001)

    def _dummy_counts(self):
        from math import sqrt
        from numpy import random, sinc
        x = self._ins_pos.get_X_position()
        y = self._ins_pos.get_Y_position()
        r = sqrt(x**2 + y**2)
        perfect = 10000*abs(sinc(r)) * self._integration_time * 0.001
        noisy = perfect + sqrt(perfect)*random.standard_normal()
        return noisy
        
