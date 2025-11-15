'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
import svgwrite

from sailocus.geometry import point
from sailocus.geometry import line
from sailocus.geometry import triangle

from sailocus.svg import svg

from sailocus.server import server

from sailocus.sail import sail

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt


# TODO: create a main for running the server version
server.runApp()



# import sys
# from pathlib import Path
# ys.path.append(str(Path(__file__).parent))  # Add project root

peak = point.Point(213, 510)
throat = point.Point(10, 233)
tack = point.Point(0, 0) 
clew = point.Point(397, 29) 


xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
xsail.validateSail()
xsvg = svg.SVG()
pathToFile = "./simpleSailFromClass.svg"
off_set = point.Point(25,25)
xsvg.createSailSVG(xsail, pathToFile, True, off_set)



# now display in a window using PyQt
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("SVG Viewer")
window.resize(500, 500)

svg_widget = QSvgWidget(pathToFile)
svg_widget.setMinimumSize(500, 500)
window.setCentralWidget(svg_widget)

window.show()
sys.exit(app.exec_())
