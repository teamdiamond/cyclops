# A dummy 2D positioner. Stores and returns a position in x/y coordinates,
# units are microns.
# Further features: movement speed can be set, absolute and relative positions
# can be set.
#
# TODO: speed not implemented yet: can be set/get, but isn't used so far
#
# Author: Wolfgang Pfaff <w dot pfaff at tudelft dot nl>

from instrument import Instrument
from cyclopean_instrument import CyclopeanInstrument
import types
import time

class dummy_pos2d(CyclopeanInstrument):
    def __init__(self, name, address=None):
        CyclopeanInstrument.__init__(self, name, tags=['positioner', 'virtual'])

        self.add_parameter('position',
                           type=types.FloatType,
                           flags=Instrument.FLAG_GETSET,
                           units='um',
                           format='%.03f, %.03f',
                           channels=('X', 'Y'),
                           channel_prefix='%s_')

        self.add_parameter('speed',
                           type=types.FloatType,
                           flags=Instrument.FLAG_SET|Instrument.FLAG_SOFTGET,
                           format='%.01f, %.01f',
                           channels=('X', 'Y'),
                           channel_prefix='%s_')

        self.add_function('move_abs_xy')

        self._position = {'X': 0.0, 'Y': 0.0}
        self._speed = {'X': 1.0, 'Y': 1.0}

        self._supported = {
            'get_running': False,
            'get_recording': False,
            'set_running': False,
            'set_recording': False,
            'save': False,
            }

    def do_get_position(self, channel):
        return self._position[channel]

    def do_set_position(self, val, channel):
        self._position[channel] = val

    def do_get_speed(self, channel):
        return self._speed[channel]

    def do_set_speed(self, val, channel):
        self._speed[channel] = val

    def move_abs_xy(self, x, y):
        self.set_X_position(x)
        self.set_Y_position(y)

        
