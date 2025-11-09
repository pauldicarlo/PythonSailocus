'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import svgwrite

from sailocus.geometry.point import Point
from sailocus.sail.sail import Sail

class SVG():

    def __init__(sel ):
        pass

    def writeToFile(self, sail, pathToFile, off_set=0):
        points = sail.getAsPoints()

        canvas_size, points = recalculate(points, off_set)
        width, height = canvas_size

        dwg = svgwrite.Drawing(pathToFile, size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'))
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
        
def recalculate(points, off_set):

    maxX = 0
    maxY = 0

    updated_points = []

    # TODO ensure that points are in sequence and make sense 

    off_set_x, off_set_y = off_set

    for x,y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y        
        updated_points.append((x+off_set_x, y+off_set_y))

    print("maxX=", maxX, " maxY=", maxY)

    canvas_size = (maxX + 2*off_set_x, maxY + 2*off_set_y)

    return canvas_size, updated_points