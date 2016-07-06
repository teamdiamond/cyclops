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

# from counters import CounterPanel
# add_panel(CounterPanel, title='Counts', sampling=200, ins='counters')

# from scan2d import Scan2dPanel
# add_panel(Scan2dPanel, title='Stage scan', sampling=500, ins='scan2d')

# from rt2_coordinator import RT2CoordinatorPanel
# add_panel(RT2CoordinatorPanel, title='Control Panel', ins='setup_controller')

 
# from optimize1d_counts_panel import Optimize1dCountsPanel
# add_panel(Optimize1dCountsPanel, title='Optimize z', ins='opt1d_counts',
#         dimension='z')
# add_panel(Optimize1dCountsPanel, title='Optimize x', ins='opt1d_counts',
#         dimension='x')
# add_panel(Optimize1dCountsPanel, title='Optimize y', ins='opt1d_counts',
#         dimension='y')

from qTelecom_panel import TempCtrlPanel 
add_panel(TempCtrlPanel , title='Temperature Controller', ins='qTelecom_manager')

from qTelecom_panel import TempCtrlMonitor
add_panel(TempCtrlMonitor , title='Temperature Monitor', ins='qTelecom_manager')

# from qTelecom_panel import DM_sweep_optimization
# add_panel(DM_sweep_optimization , title='Sweep DM pins', ins='qTelecom_manager')

# from qTelecom_plot_panel import TempCtrlPanel2 
# add_panel(TempCtrlPanel2 , title='Temperature Plotter', ins='qTelecom_plot_manager')