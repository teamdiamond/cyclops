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


from cav1_coordinator import Cav1CoordinatorPanel
add_panel(Cav1CoordinatorPanel, title='Objective Control Panel', ins='setup_controller')

from cav1_mirror_coordinator import Cav1MirrorCoordinatorPanel
add_panel(Cav1MirrorCoordinatorPanel, title='Mirror Control Panel', ins='mirror_controller')

from optimize1d_counts_panel import Optimize1dCountsPanel
add_panel(Optimize1dCountsPanel, title='Optimize objective x', ins='opt1d_counts',
        dimension='x')
add_panel(Optimize1dCountsPanel, title='Optimize objective y', ins='opt1d_counts',
        dimension='y')
add_panel(Optimize1dCountsPanel, title='Optimize objective z', ins='opt1d_counts',
        dimension='z')

add_panel(Optimize1dCountsPanel, title='Optimize mirror x', ins='opt1d_counts_mirror',
        dimension='x')

add_panel(Optimize1dCountsPanel, title='Optimize mirror y', ins='opt1d_counts_mirror',
        dimension='y')

from cav_coarse_control_panel import CoarseControlPanel
add_panel(CoarseControlPanel, title = 'Cavity Coarse Control Panel', ins = 'jpe_coarse_stepper')

from cav_fine_control_panel import FineControlPanel
add_panel(FineControlPanel, title = 'Cavity Fine Control Panel', ins = 'master_of_cavity')

from cav_char_control_panel import CharControlPanel
add_panel(CharControlPanel, title = 'Cavity Characterization Control Panel', ins = 'master_of_char_cavity')

from cav_scan_panel import ScanPanel
add_panel(ScanPanel, title = 'Cavity Scan Panel', ins = 'cavity_scan_manager')


# from cav_control_panel import ControlPanel
# add_panel(ControlPanel, title = 'Cavity Control Panel', ins = 'master_of_cavity')

# from scan2d import Scan2dPanel
# add_panel(Scan2dPanel, title='Stage scan', sampling=500, iexns='scan2d')

# from scan2d_suppl import Scan2dSupplPanel
# add_panel(Scan2dSupplPanel, title='Stage scan - counts & supplemental', sampling=500, ins='scan2d_suppl')
