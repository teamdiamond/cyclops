# An abstract instrument that provides some default functionality for the
# Cyclops UI
#
# The main purpose is to provide some default parameters and functions that
# seem reasonable to have for all panels. By putting it into this base class
# we guarantee uniformity for all instruments that shall provided this kind of
# functionality.
#
# The Idea behind this:
# all (interactive) features for cyclops shall be mostly UI-independent, where
# the UI is only a convenient way to interact with the experiment.
# therefore, all functionality is implemented in (virtual) instruments, which
# can also contain certain types of measurements/data (i.e. a scan instrument
# contains the data and all tools to process/acquire it). For this, it can of
# course also make use of other, at some point of course, real, instruments.
# The UI is thought to monitor/display instrument changes, etc., and provide
# some convenient control functionality (but that really depends on what
# you want). In that sense, Cyclops has the same purpose as the standard GUI,
# but can be way more flexible. This requires you, of course, to program what
# you want :)
#
# The basic features for cyclops-goodness-enhanced instruments include
# at the moment:
# - param 'sampling_interval' that's used for an internal timer clock.
#   the function '_sampling_event' is called automatically every
#   'sampling_interval' ms.
#
# Plus the following features. They are stored as keys in a dictionary _supported
# when the value of an entry is True, the UI assumes the instruments supports it.
# (this is only for the autopanel. you can still use the functionality if
# implemented even if it's not indicated as featured)
# - get_running: the UI uses the get_is_running method to see whether the
#                instrument is active
# - set_running: the UI can start and stop the instrument
# - get_recording: can read whether the instrument is recording data
# - set_recording: can turn on/off data recording
# - save: the UI can call the method save on the instrument, and provide
#         a comment string. This is supposed to be used internally to save
#         locally stored data (in some instrument cache).
#
# calling set_is_running(bool) automatically invokes a function _start_running
# or _stop_running, depending on the truth value of the argument, that the
# instrument can use to implement functionality, by default it doesn't do
# anything.
# Same for set_is_recording and _start_recording and _stop_recording.
# Also, save is not implemented by default.
# 
# Please see the code and the provided examples on how to use.
#
# Author: Wolfgang Pfaff <w.pfaff@tudelft.nl>

from instrument import Instrument
import gobject
import types
import time

class CyclopeanInstrument(Instrument):
    def __init__(self, name, tags=None, use={}):
        Instrument.__init__(self, name, tags=tags)

        # some standard parameters
        self.add_parameter('sampling_interval',
                           type=types.IntType,
                           flags=Instrument.FLAG_GETSET,
                           units='ms',
                           minval=1.0, maxval=10000.0,
                           doc="""
                           Gives the cycle frequency of the internal timer that can be used
                           for pseudo-asynchronous operations.
                           """)
        
        self.add_parameter('is_running',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc="""
                           Used to indicate whether the instrument is currently running.
                           What 'running' exactly is, depends on the instrument and its
                           implementation.
                           """)
        
        self.add_parameter('is_recording',
                           type=types.BooleanType,
                           flags=Instrument.FLAG_GETSET,
                           units='',
                           doc="""
                           Used to indicate whether data is currently saved via the qtlab
                           measurement functionality.
                           """)

        # relevant methods
        # method for the UI to determine which functionality is provided
        self.add_function('is_supported')
        self.add_function('supported')

        # save internally stored data (via a qtlab measurement)
        self.add_function('save')

        # common cyclops attributes
        #self.CYCLOPEAN_PARAMS = ['sampling_interval', 'is_running', 'is_recording']
        #self.CYCLOPEAN_FUNCS = ['save', 'is_supported', 'supported']

        # to be able to make use of other, already existing instruments
        self._instruments = {}
        for i in use:
            self._use_instrument(i, use[i])


        # internal data fields, especially interesting for transfer of plot
        # data
        #
        # dictionary that holds the data; format: {'data_name' : array-like, }
        # instrument administers this by itself
        self._data = {}

        # tuple that holds ('data_name', (coordinates of most recent data))
        # instrument should set accordingly after putting data, then
        # call get_data_update_index to let connected methods know
        # they can get new data
        self._data_update_index = ('', ())

        # returns data by name; if a set of slices is given, returns the
        # sliced data; number of slices must match the dimensions of the data
        self.add_function('get_data')
        self.add_function('get_data_shape')
        self.add_parameter('data_update_index',
                type=types.TupleType,
                flags=Instrument.FLAG_GET)

        # debug output for data update index
        self.connect('changed', self._debug_data_update_index)
        
        # default values
        self.set_sampling_interval(100)
        self._is_running = False
        self._is_recording = False

        # adapt this to your needs when inheriting
        self._supported = {
            'get_running': True,
            'get_recording': True,
            'set_running': False,
            'set_recording': False,
            'save': False,
            }

    ### methods for data transfer
    def get_data(self, name, slices=None):
        d = self._data[name]
        if slices == None:
            return d
        return d[slices]

    def get_data_shape(self, name):
        return self._data[name].shape

    def do_get_data_update_index(self):
        return self._data_update_index

    def _debug_data_update_index(self, unused, changes, *arg, **kw):
        if 'data_update_index' in changes:
            print changes['data_update_index']


    ### Get and set for the common parameters
    def do_set_sampling_interval(self, val):
        self._sampling_interval = val
    
    def do_get_sampling_interval(self):
        return self._sampling_interval
    
    def do_set_is_running(self, val):
        self._is_running = val
        if val: self._start_running()
        else: self._stop_running()
    
    def do_get_is_running(self):
        return self._is_running
    
    def do_set_is_recording(self, val):
        self._is_recording = val
        if val: self._start_recording()
        else: self._stop_recording()
    
    def do_get_is_recording(self):
        return self._is_recording    
    
    # publicly available methods
    # returns whether a certain feature has been implemented
    def is_supported(self, s):
        if self._supported.has_key(s):
            return self._supported[s]
        else:
            return False
        
    def supported(self):
        return self._supported
    
    def save(self, meta=""):
        pass # not implemented by default
        

    # internal methods
    def _sampling_event(self):
        pass
    
    def _start_running(self):
        gobject.timeout_add(self._sampling_interval, self._sampling_event)

    def _stop_running(self):
        pass

    def _start_recording(self):
        pass

    def _stop_recording(self):
        pass

    def _use_instrument(self, name, alias):
        from qt import instruments
        
        self._instruments[alias] = instruments[name]
        print ' * using', instruments[name].get_name(), 'from', self.get_name()
    
        i = self._instruments[alias]
    
        # iterate through parameters:
        # we need a local variable and the get/set functions
        params = i.get_parameters()
        for p in params:
            p_name = alias + '_' + p
            var_name = '_' + p_name
            # local variable
            if 'get_func' in params[p]:
                setattr(self, var_name, getattr(i, 'get_' + p)())
            else:
                setattr(self, var_name, None)
    
            # define the get and set functions
            if 'get_func' in params[p]:
                self._make_get(alias, p)
                    
            if 'set_func' in params[p]:
                self._make_set(alias, p)
    
            # add the parameter, qtlab style
            units = ''
            type = types.NoneType
            if 'units' in params[p]: units = params[p]['units']
            if 'type' in params[p]: type = params[p]['type']
               
            self.add_parameter(p_name,
                               flags = params[p]['flags'],
                               type = type,
                               units = units)
    
        # connect, so changes become visible here immediately
        def f(unused, changes, *arg, **kw):
            for c in changes:
                p_name = alias + '_' + c
                var_name = '_' + p_name
                get_name = 'get' + var_name
                if hasattr(self, get_name):
                    setattr(self, var_name, changes[c])
                    getattr(self, get_name)()
        i.connect('changed', f)
    
        # also make the functions accessible
        funcs = i.get_function_names()
        for f in funcs:
            self._make_func(alias, f)                
    
        return
    
    def _make_get(self, name, param):
        p_name = name + '_' + param
        var_name = '_' + p_name
        setattr(self, 'do_get' + var_name,
                lambda: getattr(self, var_name))
        return
    
    def _make_set(self, name, param):
        p_name = name + '_' + param
        var_name = '_' + p_name 
        def f(val):
            setattr(self, var_name, val)
            getattr(self._instruments[name], 'set_' + param)(val)
        f.__name__ = 'do_set' + var_name
        setattr(self, 'do_set' + var_name, f)
        return
    
    def _make_func(self, name, func):
        f_name = name + '_' + func
        setattr(self, f_name,
                lambda *arg, **kw: getattr(self._instruments[name], func)())
        self.add_function(f_name)
        return

