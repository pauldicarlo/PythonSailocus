'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''


import svgwrite
from flask import Flask, Response, request, render_template

from sailocus.geometry import point
from sailocus.geometry import line
from sailocus.geometry import triangle

from sailocus.svg import svg

from sailocus.sail import sail


app = Flask(__name__, 
    static_folder="../../web/static",
    template_folder="../../web/templates")

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/sailocus', methods=['GET', 'POST'])
def sailocus():
    message = None
    if request.method == 'POST':
        peak_str = request.form['peak']
        throat_str = request.form['throat']
        tack_str = request.form['tack']
        clew_str = request.form['clew']

        peak = point.str_to_point(peak_str)
        throat = point.str_to_point(throat_str)
        tack = point.str_to_point(tack_str)
        clew = point.str_to_point(clew_str)

        xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
        xsail.validateSail()
        xsvg = svg.SVG()
        pathToFile = "./simpleSailFromClass.svg"
        off_set = point.Point(25,25)
        svg_content =  xsvg.createSailSVG(xsail, pathToFile, True, off_set)
        return render_template('sailocus.html', message=message, svg_content=svg_content.tostring())
        
    
    return render_template('sailocus.html', message=message)


#@app.route('/generate-svg')
@app.route('/generate-svg', methods=['POST'])
def generate_svg_endpoint():
    peak_str = request.args.get('peak')      # → "(1,2)"
    throat_str = request.args.get('throat')  # → "(1,2)"
    tack_str = request.args.get('tack')      # → "(1,2)"
    clew_str = request.args.get('clew')      # → "(1,2)"

    peak = point.str_to_point(peak_str)
    throat = point.str_to_point(throat_str)
    tack = point.str_to_point(tack_str)
    clew = point.str_to_point(clew_str)

    xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
    xsail.validateSail()
    xsvg = svg.SVG()
    pathToFile = "./simpleSailFromClass.svg"
    off_set = point.Point(25,25)
    svg_content =  xsvg.createSailSVG(xsail, pathToFile, True, off_set)

    return Response(svg_content.tostring(), mimetype='image/svg+xml')

def runApp():
    app.run(debug=True)
