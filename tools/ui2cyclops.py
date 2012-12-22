# ui2cyclops.py
#
# This script reads a .ui file created with Qt Designer and from that
# generates a frame for an instrument and a fitting panel.
#
# Wolfgang Pfaff <w.pfaff@tudelft.nl>, 2011
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# TODO: could move the masses of string constants to an external file.



"""
ui2cyclops.py
=============

Usage
-----

Invoke on a commandline with ``python ui2cyclops.py your_file.ui``.
This will try to read the UI elements in your designer file and from that
generate the panel and the appropriate cyclopean instrument. The resulting
files will be named, given your ui file has the name ``your_file.ui``,
``your_file_panel.py`` and ``ui_your_file_panel.py``, and
``cyclopean_your_file.py``.

Requirements
------------
*pyuic4.bat* (comes with PyQt, which you should have installed if cyclops is
working) must be in your path. This should be the case if you followed the
cyclops installatin instructions.

Working principle
-----------------

The resulting files are *bare*, meaning only a frame without any sophisticated
functionality is created. Although you can use them without errors just the
way they were created, for real use, you have to implement features yourself.

The following things are included automatically:
* Instrument file:
** for supported input widgets (see below), instrument parameters are added,
   as well as their get and set methods via *do_set_...* and *do_get_...*.
   A variable to hold the parameter within the instrument is also created.
** for action widgets, functions are added via add_function. Also, an empty
   function definition is added.
** The names of parameters and functions are given by the name of the respective
   widgets in Qt Designer.
** Moreover, some commonly inherited functions for cyclopean instruments are
   readily added.

* Panel:
** changes of instrument values are monitored and the new value is directly
   transmitted to the UI elements (values are updated whenever a set or get
   method of the instrument is called. if the instrument just changes the
   variable that holds the value with calling either of the two functions,
   nothing happens to the UI)
** changes in UI inputs result in autmatic calling of the respective instrument
   set method.

Remember: this is only a fast method of getting a new UI panel properly set up,
feel free to adopt this as excessively to your needs once the files are
created :)

Details
-------

Your ui file must have a *QWidget* element with objectName *Panel*. This, and
its contained elements, will be used as basis. Everything else will be ignored.

The following Types of widgets are recognized to hold parameters, with the
listed properties used in qtlab's *add_parameter*:

* QSpinBox (int)
* QDoubleSpinBox (float)
* QLineEdit (str)
* QSlider (int)
* QRadioButton (bool)
* QCheckBox (bool)

If maximum/minimum values have been specified for the fields designer,
these values will also be used for the maxval/minval options for the
respective parameters.

Supported function calling widgets are:

* QPushButton


"""

import sys, os, time
from xml.dom import minidom

VERSION = 'v20110215'

param_inputs = {
    'QSpinBox' : {
        'type' : 'types.IntType',
        'type_convert' : 'int',
        'default_value' : '0',
        'default_min' : '0',
        'default_max' : '99',
        'value_property' : 'value',
        'value_type' : 'number',
        'widget_set' : 'setValue',
        'widget_signal' : 'valueChanged',
        },
    'QDoubleSpinBox' : {
        'type' : 'types.FloatType',
        'type_convert' : 'float',
        'default_value' : '0.0',
        'default_min' : '0.0',
        'default_max' : '99.0',
        'value_property' : 'value',
        'value_type' : 'double',
        'widget_set' : 'setValue',
        'widget_signal' : 'valueChanged',
        },
    'QLineEdit' : {
        'type' : 'types.StringType',
        'type_convert' : 'str',
        'default_value' : "''",
        'default_min' : None,
        'default_max' : None,
        'value_property' : 'text',
        'value_type' : 'string',
        'widget_set' : 'setText',
        'widget_signal' : 'textEdited',
        },
    'QSlider' : {
        'type' : 'types.IntType',
        'type_convert' : 'int',
        'default_value' : '0',
        'default_min' : '0',
        'default_max' : '99',
        'value_property' : 'value',
        'value_type' : 'number',
        'widget_set' : 'setValue',
        'widget_signal' : 'sliderMoved',
        },
    'QRadioButton' : {
        'type' : 'types.BooleanType',
        'type_convert' : 'bool',
        'default_value' : 'False',
        'default_min' : None,
        'default_max' : None,
        'value_property' : 'checked',
        'value_type' : 'bool',
        'widget_set' : 'setChecked',
        'widget_signal' : 'toggled',
        },
    'QCheckBox' : {
        'type' : 'types.BooleanType',
        'type_convert' : 'bool',
        'default_value' : 'False',
        'default_min' : None,
        'default_max' : None,
        'value_property' : 'checked',
        'value_type' : 'bool',
        'widget_set' : 'setChecked',
        'widget_signal' : 'toggled',
        },
    }

function_callers = {
    'QPushButton' : {
        'widget_signal' : 'pressed'
        },
    }

def make_files(name, widgets):
    ins_header = _instrument_header(name)
    ins_param_add = ''
    ins_param_getset = ''
    ins_func_add = ''
    ins_func_implement = ''

    p_name = name + '_panel'
    p_file = p_name + '.py'
    p_ui_file = 'ui_' + p_file
    p_class_name = ''
    for s in name.split('_'):
        p_class_name += s.capitalize()

    p_header = _p_header(p_name, p_class_name, p_file, p_ui_file)
    p_set_ui_values = ''
    p_connect = ''
    p_connect_func = ''
    p_implement_func = ''
    p_set_ins_implement = ''
    p_ins_change = '\n    def _instrument_changed(self, changes):\n'
    p_internal = _p_internal_functions()

    # first generate python code for the panel from the ui file
    try:
        os.system('pyuic4.bat -o %s %s' % (p_ui_file, sys.argv[1]))
    except:
        print 'error executing pyuic4. please check your PATH settings.'
        print '(the Qt libs must also be in the PATH!)'
        sys.exit(0)
    
    for w in widgets:
        n = w.getAttribute('name')
        c = w.getAttribute('class')
        if w.getAttribute('class') in param_inputs:
            print '* found parameter:', n
            
            ins_param_add += _instrument_add_parameter(w)
            ins_param_getset += _instrument_getset_parameter(n)

            p_set_ui_values += _p_set_ui_values(n, c)
            p_connect += _p_connect(n, c)
            p_set_ins_implement += _p_implement_set(n)
            p_ins_change += _p_ins_changed(n, c)
            
        if w.getAttribute('class') in function_callers:
            print '* found function:', n
            
            ins_func_add += _instrument_add_function(n)
            ins_func_implement += _instrument_implement_function(n)

            p_connect_func += _p_connect_function(n, c)
            p_implement_func += _p_implement_function(n)
            
    ins_internal = _instrument_internal_functions()

    ins_name = 'cyclopean_' + name
    ins_file = ins_name + '.py'

    f = open(ins_file, 'w')
    f.write(ins_header + ins_param_add + ins_func_add + ins_param_getset + \
                ins_func_implement + ins_internal)
    f.close()

    f = open(p_file, 'w')
    f.write(p_header + p_set_ui_values + '\n' + p_connect + '\n' + \
        p_connect_func + p_implement_func + p_set_ins_implement + \
        p_ins_change)
    f.close()

    return ins_name, p_name, p_class_name
    
# def make_files

def _p_header(p_name, p_class_name, p_file, p_ui_file):
    s = """# %s
#
# auto-created by %s %s, %s
""" % (p_file, sys.argv[0], VERSION, time.asctime())

    s += """
from panel import Panel
from %s import Ui_Panel

from PyQt4 import QtCore
""" % (p_ui_file[:-3])

    s+= """
class %s(Panel):
    def __init__(self, parent, *arg, **kw):
        Panel.__init__(self, parent, *arg, **kw)

        # designer ui
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

""" % (p_class_name)
    return s

# def _p_header

def _p_set_ui_values(name, cls):
    s = """        self.ui.%s.%s(self._ins.get_%s())
""" % (name, param_inputs[cls]['widget_set'], name)
    return s

# def _p_set_ui_values

def _p_connect(name, cls):
    s = """        self.ui.%s.%s.connect(self._set_%s)
""" % (name, param_inputs[cls]['widget_signal'], name)
    return s

# def _p_connect

def _p_connect_function(name, cls):
    s = """        self.ui.%s.%s.connect(self._%s)
""" % (name, function_callers[cls]['widget_signal'], name)
    return s

# def _p_connect_function

def _p_implement_function(name):
    s = """
    def _%s(self):
        self._ins.%s()
        return
""" % (name, name)
    return s

# def _p_implement_function

def _p_implement_set(name):
    s = """
    def _set_%s(self, val):
        self._ins.set_%s(val)
        return
""" % (name, name)
    return s
# def _p_implement_set

def _p_ins_changed(name, cls):
    s = """
        if changes.has_key('%s'):
            self.ui.%s.%s(%s(changes['%s']))
""" % (name, name, param_inputs[cls]['widget_set'],
       param_inputs[cls]['type_convert'], name)
    return s

# def _p_ins_changed

def _p_internal_functions():
    s = """
    def timerEvent(self, event):
        return
"""
    
def _instrument_header(name):
    ins_name = 'cyclopean_' + name
    ins_file = ins_name + '.py'
    comment = """# %s
#
# auto-created by %s %s, %s
""" % (ins_file, sys.argv[0], VERSION, time.asctime())

    py_header = """
from instrument import Instrument
from cyclopean_instrument import CyclopeanInstrument
import types

class %s(CyclopeanInstrument):
    def __init__(self, name, address=None):
        CyclopeanInstrument.__init__(self, name, tags=[])

        self._supported = {
            'get_running': False,
            'get_recording': False,
            'set_running': False,
            'set_recording': False,
            'save': False,
            }
""" % (ins_name)  
    
    return comment + py_header

# def _instrument_header

def _instrument_add_parameter(w):
    name = w.getAttribute('name')
    classname = w.getAttribute('class')
    minval = param_inputs[classname]['default_min']
    maxval = param_inputs[classname]['default_max']
    flags = 'Instrument.FLAG_GETSET'
    default = param_inputs[classname]['default_value']

    # some types of properties are used by this scripts, find them
    for p in w.getElementsByTagName('property'):

        # minimum value
        if p.getAttribute('name') == 'minimum':
            minval = p.getElementsByTagName(
                param_inputs[classname]['value_type'])[0].firstChild.data


        # maximum value
        if p.getAttribute('name') == 'maximum':
            maxval = p.getElementsByTagName(
                param_inputs[classname]['value_type'])[0].firstChild.data
            
        # enabled (if not, we treat as read-only parameter)
        if p.getAttribute('name') == 'enabled':
            if p.getElementsByTagName('bool')[0].firstChild.data == 'false':
                flags = 'Instrument.FLAG_GET'

        # value (if set, this will be the instrument default)
        if p.getAttribute('name') == param_inputs[classname]['value_property']:
            default = p.getElementsByTagName(
                param_inputs[classname]['value_type'])[0].firstChild.data
            if default == 'true' or default == 'false':
                default = default.capitalize()

    type = param_inputs[w.getAttribute('class')]['type']
    units = ''    

    param_add = """
        self.add_parameter('%s',
                           type=%s,
                           flags=%s,
                           units='%s',
""" % (name, type, flags, units)

    if minval != None:
        param_add += """                           minval=%s,
""" % (minval)

    if maxval != None:
        param_add += """                           maxval=%s,
""" % (maxval)


    if param_inputs[classname]['type_convert'] == 'str':
        param_add += """                           doc='')
        self._%s = '%s'
""" % (name, default)
    else:
        param_add += """                           doc='')
        self._%s = %s
""" % (name, default)

    return param_add

# def _instrument_add_parameter

def _instrument_add_function(name):
    ret = """
        self.add_function('%s')
""" % (name)
    return ret

# def _instrument_add_function

def _instrument_getset_parameter(name):
    getset = """
    def do_get_%s(self):
        return self._%s

    def do_set_%s(self, val):
        self._%s = val
""" % (name, name, name, name)
    return getset

# def _instrument_getset_parameter

def _instrument_implement_function(name):
    ret = """
    def %s(self, *arg, **kw):
        pass
""" % (name)
    return ret

# def _instrument_implement_function

def _instrument_internal_functions():
    s = """
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
"""
    return s

# def _instrument_internal_functions

if __name__ == '__main__':
    if '--help' in sys.argv:
        print __doc__
        sys.exit(1)
    if len(sys.argv) != 2:
        print 'invalid no of arguments given!'
        print 'python ui2cyclops.py --help for more details.'
        sys.exit(1)
    if sys.argv[1][-3:] != '.ui':
        print 'argument has to be a ui file!'
        print 'python ui2cyclops.py --help for more details.'
        sys.exit(1)

    try:
        f = minidom.parse(sys.argv[1])
    except:
        print 'file is not valid xml!'
        sys.exit(0)

    ui_node = None
    for c in f.childNodes:
        if c.tagName == 'ui':
            if c.getAttribute('version') == '4.0':
                ui_node = c
    if ui_node == None:
        print 'no valid ui found in your file!'
        sys.exit(0)

    panel_widget = None
    widgets = ui_node.getElementsByTagName('widget')
    for w in widgets:
        if w.getAttribute('class') == 'QWidget' and \
                w.getAttribute('name') == 'Panel':
            panel_widget = w
            print '* found Panel widget...'
    if panel_widget == None:
        print 'could not find Panel widget!'
        sys.exit(0)

    ins, panel, panel_class = make_files(sys.argv[1][:-3], widgets)

    print """
Finished processing.

To make sure you can properly use cyclopean instruments, be sure that at the
moment of instrument creation, the cyclops source path is in sys.path.
You can do this, for instance, by adding this to the top of your
create_instrument init script:

import os, sys
cyclops_dir = os.path.join(os.getcwd(), 'cyclops', 'source')
if not cyclops_dir in sys.path:
    sys.path.append(cyclops_dir)
"""
    print """
To make use of the generated instrument, copy the
instrument file to your user_instrument folder. Then enable it by adding this
to your create_instrument init script:

%s = qt.instruments.create('%s', '%s')
""" % (ins, ins, ins)
    print """
To use your panel in cyclops, copy the two panel files to the
cyclops/source/panel folder. Then add the panel to your panel configuration
script:

from panels.%s import %s
add_panel(%s, title='a window title', ins='%s')
""" % (panel, panel_class, panel_class, ins)
    

    

    
