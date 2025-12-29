from sailocus.sail import sail
from sailocus.geometry import point
from sailocus.svg import svg

import argparse
import json

# we're making a 4-sided sail here so we need
# to have the peak, throat, take, and clew...
# Point(x,y) where x/y are millimeters and ints
peak = point.Point(213, 510)
throat = point.Point(10, 233)
tack = point.Point(0, 0) 
clew = point.Point(397, 29) 


# Load in a supplied sample file, or use default above
parser = argparse.ArgumentParser(description="A sample command line tool.")
parser.add_argument('--input-file', type=str, help='The path to the input file.')
args = parser.parse_args()
if args.input_file:
    print(f"Processing file: {args.input_file}")


# create a Sail with the points
xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sail_name = "Four sided sail")
xsail.validateSail()

# Create SVG file of sail and its CoE
xsvg = svg.SVG()
pathToFile = "./simpleSailFromClass.svg"
off_set = point.Point(25,25)
xsvg.createSailSVG(xsail, pathToFile, True, off_set)

# TODO - get rid of following two lines
json_string = json.dumps(xsail.__dict__, indent=4)
print(json_string)
