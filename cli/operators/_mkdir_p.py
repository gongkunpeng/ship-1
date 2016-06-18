# coding: utf-8

"""
    _mkdir_p.py
    ```````````
"""
import os, errno


def _mkdir_p(abspath):
    try:
        os.makedirs(abspath)
    except OSError as e:
        if (e.errno == errno.EEXIST) and (os.path.isdir(abspath)):
            pass
        else: raise
