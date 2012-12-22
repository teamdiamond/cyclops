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
from cyclops import config

config['plot_colors'] = {
	'colorplot_cmap': 'jet',
}

from counters import CounterPanel
add_panel(CounterPanel, title='Counts', sampling=200, ins='counters_demo')

# print sys.path
# 
# from counts_v2_panel import CountsV2
# add_panel(CountsV2, title='CountsV2', sampling=200, ins='cyclopean_counts_v2')

# an example 2d scan
# from scan2d import Scan2dPanel
# add_panel(Scan2dPanel, title='Scan', sampling=500, ins='scan2d_demo')

# a bit more complicated
#from whackyscan_panel import Whackyscan
# add_panel(Whackyscan, title='Complicated Scan', sampling=500, ins='whackyscan')

#from panels.example_panel import Example
#add_panel(Example, title='Example', ins='cyclopean_example')
