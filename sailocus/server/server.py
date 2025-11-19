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
        peak_x_str = request.form['peak_x']
        peak_y_str = request.form['peak_y']
        throat_x_str = request.form['throat_x']
        throat_y_str = request.form['throat_y']
        tack_x_str = request.form['tack_x']
        tack_y_str = request.form['tack_y']
        clew_x_str = request.form['clew_x']
        clew_y_str = request.form['clew_y']

        try:
            peak_x = int(peak_x_str)
            peak_y = int(peak_y_str)
            throat_x = int(throat_x_str)
            throat_y = int(throat_y_str)
            tack_x = int(tack_x_str)
            tack_y = int(tack_y_str)
            clew_x = int(clew_x_str)
            clew_y = int(clew_y_str)
        except ValueError:
            message = "Invalid input. Please enter a positive or negative integer."


        peak = point.Point(peak_x, peak_y)
        throat = point.Point(throat_x, throat_y)
        tack = point.Point(tack_x, tack_y)
        clew = point.Point(clew_x, clew_y)

        xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
        xsail.validateSail()
        xsvg = svg.SVG()
        pathToFile = "./simpleSailFromClass.svg"
        off_set = point.Point(25,25)
        svg_content =  xsvg.createSailSVG(xsail, pathToFile, True, off_set)
        return render_template('sailocus.html', 

            initial_value_tack_x=tack_x,
            initial_value_tack_y=tack_y,
            initial_value_throat_x=throat_x,
            initial_value_throat_y=throat_y,
            initial_value_peak_x=peak_x,
            initial_value_peak_y=peak_y,
            initial_value_clew_x=clew_x,
            initial_value_clew_y=clew_y,

            message=message, 
            svg_content=svg_content.tostring())
    
    return render_template('sailocus.html', 
            initial_value_tack_x=0,
            initial_value_tack_y=0,
            initial_value_throat_x=10,
            initial_value_throat_y=233,
            initial_value_peak_x=213,
            initial_value_peak_y=510,
            initial_value_clew_x=397,
            initial_value_clew_y=29,
            message=message)

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
