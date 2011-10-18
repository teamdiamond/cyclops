import sys, os

# user configuration of cyclops
from cyclops import config

# folders
# location of qtlab
config['qtlab_dir'] = '/home/wp/measuring/qtlab'

# need some modules from qtlab
sys.path.append(config['qtlab_dir'])
sys.path.append(os.path.join(config['qtlab_dir'], 'source'))

# location of panels 
config['panels_dirs'] = [
    'panels', 'source/panels', '/home/wp/measuring/user/panels' ]

for d in config['panels_dirs']:
    sys.path.append(d)
    
# location of plots
config['plots_dirs'] = [
    'plots', 'source/plots' ]

for d in config['plots_dirs']:
    sys.path.append(d)

# appearance
config['plot_colors'] = {
	'colorplot_cmap': 'hot',
}
