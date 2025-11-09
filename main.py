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


def recalculate(points):
    margin = 10

    maxX = 0
    maxY = 0

    updated_points = []

    # TODO ensure that points are in sequence and make sense 


    for x,y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y        
        updated_points.append((x+margin, y+margin))

    print("maxX=", maxX, " maxY=", maxY)

    canvas_size = (maxX + 2*margin, maxY + 2*margin)

    return canvas_size, margin, updated_points

def create_four_sided_sail(points, fileName):

    canvas_size, margin, points = recalculate(points)
    width, height = canvas_size

    dwg = svgwrite.Drawing(fileName, size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'))
    cartesian_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")

    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='darkseagreen'))

    trapezoid = dwg.polygon(
        points=points,
        fill='ivory',
        stroke='black',
        stroke_width=3
    )

    cartesian_group.add(trapezoid)
    dwg.add(cartesian_group)
    
    dwg.save()

peak = point.Point(213, 510)
throat = point.Point(10, 233)
tack = point.Point(0, 0) 
clew = point.Point(397, 29) 

four_sided_sail_points = [ peak, throat, tack, clew]

xsail = sail.Sail(tack, clew, head=None, peak=peak, throat=throat, sailName = "Four sided sail")
xsail.validateSail()

create_four_sided_sail(four_sided_sail_points, "simplesail.svg")

xsvg = svg.SVG()

pathToFile = "./simpleSail.svg"
margin = point.Point(10,10)
xsvg.writeToFile(xsail, margin, pathToFile)


