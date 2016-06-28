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
# appearance
config['plot_colors'] = {
        'colorplot_cmap': 'gist_earth',
}

from counters import CounterPanel
add_panel(CounterPanel, title='Counts', sampling=200, ins='counters')

from scan2d import Scan2dPanel
add_panel(Scan2dPanel, title='Stage scan', sampling=500, ins='scan2d')

from cav1_coordinator import Cav1CoordinatorPanel
add_panel(Cav1CoordinatorPanel, title='Control Panel', ins='setup_controller')

 
from optimize1d_counts_panel import Optimize1dCountsPanel
add_panel(Optimize1dCountsPanel, title='Optimize x', ins='opt1d_counts',
        dimension='x')
add_panel(Optimize1dCountsPanel, title='Optimize y', ins='opt1d_counts',
        dimension='y')

from cav_control_panel import ControlPanel
add_panel(ControlPanel, title = 'Cavity Control Panel', ins = 'master_of_cavity')

from cav_scan_panel import ScanPanel
add_panel(ScanPanel, title = 'Cavity Scan Panel', ins = 'cavity_scan_manager')