import json
import time
import os

def welcome_msg(user):
    return

def get_real_file_path(local_str):
    prefix = '/mnt/cache/'
    nfs_prefix = '/mnt/nfs/cache/'
    test_prefix = '/mnt/test/'
    path_leaf = ''
    file_name = os.path.splitext(local_str)[0]
    if len(file_name) == 32:
        for i in range(8):
            path_leaf += file_name[i * 4: i * 4 + 4] + '/'

        path_leaf += local_str
        if os.path.exists(prefix + path_leaf):
            return prefix + path_leaf

        elif os.path.exists(nfs_prefix + path_leaf):
            return nfs_prefix + path_leaf

        elif os.path.exists(test_prefix + path_leaf):
            return test_prefix + path_leaf

        else:
            print ('Can not find both local directory for ' + path_leaf)
    else:
        print ('TODO: get_real_path', local_str)

    return local_str

print(get_real_file_path('a689da7055ae43378526647350f7b817'))




