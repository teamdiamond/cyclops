# A dummy linescanner. Returns function values (in this case of a dummy-function)
# that are lying in the XY plane. The positions for the return values are
# specified via a start point in the plane, an angle (0=positive x,
# 90=positive y, and so on), a length, and the nr of points (start and end point
# included). Also, a pixel time can be specified (implemented as sleep)
#
# Author: Wolfgang Pfaff <w dot pfaff at tudelft dot nl>

from instrument import Instrument
from cyclopean_instrument import CyclopeanInstrument
import types
import time

class dummy_linescan(CyclopeanInstrument):
    def __init__(self, name, address=None):
        CyclopeanInstrument.__init__(self, name, tags=['measure', 'virtual'])


        # TODO: maybe add channel functionality (with dictionaries, see dummy_pos2d)
        # TODO: add more possibilites/convenience functions on how to specify the line
        # (e.g., with start/end points)
        self.add_parameter('start',
                           type=types.TupleType,
                           flags=Instrument.FLAG_GETSET,
                           units='um')

        self.add_parameter('angle',
                           type=types.FloatType,
                           flags=Instrument.FLAG_GETSET,
                           units='')

        self.add_parameter('length',
                           type=types.FloatType,
                           flags=Instrument.FLAG_GETSET,
                           units='um')

        self.add_parameter('nr_of_points',
                           type=types.IntType,
                           flags=Instrument.FLAG_GETSET,
                           units='')

        self.add_parameter('points',
                           type=types.ListType,
                           flags=Instrument.FLAG_GET,
                           units='um',
                           channels=('X', 'Y'))

        self.add_parameter('pixel_time',
                           type=types.IntType,
                           flags=Instrument.FLAG_GETSET,
                           units='ms')

        self.add_parameter('values',
                           type=types.ListType,
                           flags=Instrument.FLAG_GET,
                           units='')

        self._points = ( [0., 0.5, 1.], [0., 0., 0.] )
        self._values = [0., 0., 0.]
        self._start = (0., 0.)

        self.set_angle(0)
        self.set_length(1)
        self.set_nr_of_points(3)
        self.set_pixel_time(1)

        self._supported = {
            'get_running': True,
            'get_recording': False,
            'set_running': False,
            'set_recording': False,
            'save': False,
            }

    def do_get_start(self):
        return self._start

    def do_set_start(self, val):
        self._start = val

    def do_get_angle(self):
        return self._angle

    def do_set_angle(self, val):
        self._angle = val

    def do_get_length(self):
        return self._length

    def do_set_length(self, val):
        self._length = val

    def do_get_nr_of_points(self):
        return self._nr_of_points

    def do_set_nr_of_points(self, val):
        self._nr_of_points = val

    def do_get_pixel_time(self):
        return self._pixel_time

    def do_set_pixel_time(self, val):
        self._pixel_time = val

    def do_get_points(self, channel):
        return self._points[channel]

    def do_get_values(self):
        return self._values


    # internal functions
    def _start_running(self):
        CyclopeanInstrument._start_running(self)
        # determine points of the line in x/y space
        self._calc_points()
        # pre-allocate a list and populate
        self._values = list(range(self._nr_of_points))
        for i in range(self._nr_of_points):
            self._values[i] = self._calc_val(self._points[0][i],
                                             self._points[1][i])
            time.sleep(self._pixel_time/1000.0)

        # force signal-emit
        self.get_values()

        # debug
        # print self.get_values()
        
        self.do_set_is_running(False)

    # function to determine the points in x-y space that will be used
    def _calc_points(self):
        from math import pi, sin, cos
        from numpy import r_
        angle_rad = self._angle / 180 * pi
        x_unit, y_unit = cos(angle_rad), sin(angle_rad)
        steps = r_[0.:self._length:1j*self._nr_of_points]
        x_points = list(range(self._nr_of_points))
        y_points = list(range(self._nr_of_points))
        for i in range(self._nr_of_points):
            x_points[i] = self._start[0] + steps[i]*x_unit
            y_points[i] = self._start[1] + steps[i]*y_unit
        self._points = (x_points, y_points)

        # debug
        # print x_unit, y_unit, self._points

    def _calc_val(self, x, y):
        from math import sqrt
        from numpy import random, sinc
        r = sqrt(x**2 + y**2)
        perfect = 10000*abs(sinc(r))
        noisy = perfect + sqrt(perfect)*random.standard_normal()
        #time.sleep(self._pixel_time/1000.0)
        return noisy
