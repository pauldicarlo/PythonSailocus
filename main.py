'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
import svgwrite

from sailocus.geometry import point
from sailocus.svg import svg
from sailocus.sail import sail

# import sys
# from pathlib import Path
# ys.path.append(str(Path(__file__).parent))  # Add project root

peak = point.Point(213, 510)
throat = point.Point(10, 233)
tack = point.Point(0, 0) 
clew = point.Point(397, 29) 


xsail = sail.Sail(tack, clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
xsail.validateSail()

xsvg = svg.SVG()
pathToFile = "./simpleSailFromClass.svg"
off_set = point.Point(10,10)
xsvg.writeToFile(xsail, pathToFile, off_set)


