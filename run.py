from src import *

import sys
import os
day = 0
try:
    day = sys.argv[1]
except IndexError:
    print('Not yet implemented')
    exit(1)
if day == 0:
    exit(1)

_ROOTDIR = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_ROOTDIR, 'src')
_RUN = os.path.join(_SRC, str(day))
os.chdir(_RUN)
cmd = 'python handler.py'
os.system(cmd)
