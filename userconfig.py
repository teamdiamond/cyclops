import sys, os

# user configuration of cyclops
from cyclops import config

# folders
# location of qtlab
config['qtlab_dir'] = os.path.join(os.getcwd(), '..', 'qtlab')

# need some modules from qtlab
sys.path.insert(0, config['qtlab_dir'])
sys.path.insert(1, os.path.join(config['qtlab_dir'], 'source'))

# location of panels 
config['panels_dirs'] = [
    'panels', 'source/panels', '../measurement/panels' ]

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
