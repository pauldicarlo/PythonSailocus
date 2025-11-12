'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import svgwrite

from sailocus.geometry.triangle import Triangle
from sailocus.geometry.point import Point

from sailocus.sail.sail import Sail
from sailocus.sail.sail import TriangleCenterOfEffort

class SVG():

    def __init__(sel ):
        pass

    def writeToFile(self, sail, pathToFile, off_set=0):
        points = sail.getAsPoints()

        #TODO - need to handle offest for entire set of points/polygons/etc
        off_set = (0,0)

        canvas_size, points = recalculate(points, off_set)
        width, height = canvas_size

        dwg = svgwrite.Drawing(pathToFile, size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'))
        cartesian_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")

        #dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='darkkhaki'))
        dwg.add(dwg.rect(insert=(0, 0), size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'), fill='darkseagreen'))

        # dwg.add(dwg.line((10, 50), (250, 100), stroke='blue', stroke_width=5))


        trapezoid = dwg.polygon(
            points=points,
            fill='ivory',
            stroke='black',
            stroke_width=1
        )
        cartesian_group.add(trapezoid)




        # coe
        # dwg.add(dwg.circle(center=(sail.coe.center_of_effort[0], sail.coe.center_of_effort[1]), r=2, fill='blue', stroke='black', stroke_width=1))


        #for line_segment in sail.coe.centroid_line_segments:
        #    dwg.add(dwg.line(line_segment.point_a, line_segment.point_b, stroke='black', stroke_width=1))

        for triangle in sail.coe.triangles:
            tcoe = TriangleCenterOfEffort(triangle)
            trianglePoints = triangle.getAsPoints()
            svgTriangle = dwg.polygon(
                points=trianglePoints,
                fill='pink',
                stroke='black',
                stroke_width=1
            )
            cartesian_group.add(svgTriangle)
            cartesian_group.add(dwg.circle(center=(triangle.centroid), r=2, fill='blue', stroke='black', stroke_width=1))
            

        # this will only work for a 4 sided sail...

        cartesian_group.add(dwg.line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid, stroke='black', stroke_width=1))


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
