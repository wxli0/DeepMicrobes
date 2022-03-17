"""
Replaces file names in a directorywith space by underscore

:param argv[0]: dir. the directory
"""

import os
import sys

dir = sys.argv[1]

for file in os.listdir(dir):
    os.rename(os.path.join(dir,file), os.path.join(dir, file.replace(" ", "_")))
    