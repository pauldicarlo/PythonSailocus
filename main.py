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

from sailocus.sail import sail

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

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
off_set = point.Point(25,25)
xsvg.writeToFile(xsail, pathToFile, off_set)



lineX = line.Line(point.Point(0,0), point.Point(400,0))

triangleX = triangle.Triangle(point.Point(0,0), point.Point (30,400), point.Point(350,0))


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("SVG Viewer")
window.resize(500, 500)

svg_widget = QSvgWidget(pathToFile)
svg_widget.setMinimumSize(500, 500)
window.setCentralWidget(svg_widget)

window.show()
sys.exit(app.exec_())
