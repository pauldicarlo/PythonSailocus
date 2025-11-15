'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
# Using Flask
from flask import Flask, Response, request

import svgwrite

from sailocus.geometry import point
from sailocus.geometry import line
from sailocus.geometry import triangle

from sailocus.svg import svg

from sailocus.sail import sail


app = Flask(__name__)


#@app.route('/generate-svg')
@app.route('/generate-svg', methods=['POST'])
def generate_svg_endpoint():
    peak = request.args.get('peak')      # → "(1,2)"
    #throat = request.args.get('peak')      # → "(1,2)"
    #tack = request.args.get('peak')      # → "(1,2)"
    #clew = request.args.get('clew')      # → "(1,2)"

    peak = point.Point(213, 510)
    throat = point.Point(10, 233)
    tack = point.Point(0, 0) 
    clew = point.Point(397, 29) 


    xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
    xsail.validateSail()
    xsvg = svg.SVG()
    pathToFile = "./simpleSailFromClass.svg"
    off_set = point.Point(25,25)
    svg_content =  xsvg.createSailSVG(xsail, pathToFile, True, off_set)




    return Response(svg_content.tostring(), mimetype='image/svg+xml')

def runApp():
    app.run(debug=True)
