# User configuration for panels at startup
# 
# add_panel(your_panel_class, option1, option2, ...)

# an example counter
# set a window title that fits somehow
# set a timer to 200ms. This means that the class' method timerEvent(event)
# will be called every 200ms automatically. Can be used for updating, or
# whatever seems desirable. Default is 250ms.
# connect a dummy counter instrument automatically, its available
# as self._ins within the panel class
from panels.counter import CounterPanel
add_panel(CounterPanel, title='APD#1', sampling=200, ins='dummy_count')

# an example 2d scan
from panels.scan2d import Scan2dPanel
add_panel(Scan2dPanel, title='APD#1 via stage', sampling=500, ins='dummy_scan')
