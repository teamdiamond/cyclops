# dataflash.py
#
# Main program file of the data viewer/administrator dataflash.


import sys,os

# consants
FILE_TYPES = ['.npy', '.npz', '.dat']

# basic settings that will be put into an rc file at some point
DATA_DIR = 'd:\\qtlab+cyclops_rt2_wolfgang\\data\\'



def get_data_tree(data_dir):
    """
    Returns a list of data files in the data directory. The files are only
    included on basis of their ending (all supported) and not filtered.
    The returned value is a dictionary with keys being the names
    of the (sub)directories. For subdirs a dir dictionary will contain
    more subdictinaries, one per subdir. The returned dict thus resembles
    the full data dir tree, where only branches that end with data files
    are actually included.
    """
    tree = {}
    for f in os.listdir(data_dir):
        if os.path.splitext(f)[1] in FILE_TYPES:
            tree[f] = {}
            stat = os.stat(os.path.join(data_dir, f))
            tree[f]['size_kibibyte'] = stat.st_size / 1024
            tree[f]['creation_date'] = stat.st_ctime
            
        elif os.path.isdir(os.path.join(data_dir, f)):
            has_data, subtree = get_data_tree(os.path.join(data_dir, f))
            if has_data:
                tree[f] = subtree

    return len(tree.keys())>0, tree


if __name__ == '__main__':
    print get_data_tree(DATA_DIR)
