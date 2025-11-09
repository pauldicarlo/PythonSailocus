'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
from sailocus.geometry.point import Point
from sailocus.sail.sail import Sail

class SVG():

    def __init__(sel ):
        pass

    def writeToFile(self, sail, margin, pathToFile):
        self.sail = sail
        self.margin = margin
        self.pathToFile = pathToFile

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