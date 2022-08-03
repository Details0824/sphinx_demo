import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(os.path.abspath('.'))

import pathlib
import sys
p = pathlib.Path(__file__).parents[2]
# p = p / 'swai'
print(p)