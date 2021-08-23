"""
Configuration file for global parameters
"""

import os
from os.path import expanduser
import platform



home = expanduser("~")
base_path = os.path.join(home, "Desktop/project.nosync/")
if platform.platform()[:5] == 'Linux':
    base_path = home
