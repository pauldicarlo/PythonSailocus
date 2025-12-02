'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from .sail import Sail
from ..geometry.point import  Point

# All units are in millimeters
SortOfOptimistSail = Sail( 
    tack=Point(0,0), 
    throat=Point(10,233), 
    peak=Point(213,510), 
    clew=Point(397,29),
    sail_name="Sort of Optimist Dinghy")
