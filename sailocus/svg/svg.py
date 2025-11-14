'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import svgwrite

from sailocus.geometry.triangle import Triangle
from sailocus.geometry.point import Point
from sailocus.geometry.line import intersection, Line

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
        transform_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")

        #dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='darkkhaki'))
        dwg.add(dwg.rect(insert=(0, 0), size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'), fill='darkseagreen'))

        # dwg.add(dwg.line((10, 50), (250, 100), stroke='blue', stroke_width=5))


        trapezoid = dwg.polygon(
            points=points,
            fill='ivory',
            stroke='black',
            stroke_width=1
        )
        transform_group.add(trapezoid)

        # draw line from throat to clew
        transform_group.add(dwg.line(sail.throat, sail.clew, stroke='black', stroke_width=1, stroke_dasharray='9,5'))


        # coe
        # dwg.add(dwg.circle(center=(sail.coe.center_of_effort[0], sail.coe.center_of_effort[1]), r=2, fill='blue', stroke='black', stroke_width=1))


        #for line_segment in sail.coe.centroid_line_segments:
        #    dwg.add(dwg.line(line_segment.point_a, line_segment.point_b, stroke='black', stroke_width=1))

        '''
        for triangle in sail.coe.triangles:
            tcoe = TriangleCenterOfEffort(triangle)
            trianglePoints = triangle.getAsPoints()
            svgTriangle = dwg.polygon(
                points=trianglePoints,
                fill='pink',
                stroke='black',
                stroke_width=1
            )
            transform_group.add(svgTriangle)
            transform_group.add(dwg.circle(center=(triangle.centroid), r=2, fill='blue', stroke='black', stroke_width=1))
        '''          


        for line_segment in sail.coe.lines_perpendicular_to_centroid_line_segments:
            transform_group.add(dwg.line(line_segment.point_a , line_segment.point_b, stroke='purple', stroke_width=2))


        # line from end point of vectors from perpendicuar lines
        transform_group.add(dwg.line(
            sail.coe.lines_perpendicular_to_centroid_line_segments[0].point_b,
            sail.coe.lines_perpendicular_to_centroid_line_segments[1].point_b,
            stroke='blue', stroke_width=1))

        # this will only work for a 4 sided sail...

        # line from one centroid to the other
        transform_group.add(dwg.line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid, stroke='red', stroke_width=1))


        text_group = transform_group.add(dwg.g(transform="scale(1, -1)"))  # Flip back!

        # Put labels out there
        # TODO: Need to flip them 
        text_group.add(dwg.text('tack', insert=(sail.tack.x+5, -1 *(sail.tack.y) - 250), fill='black', font_size='20px'))
        text_group.add(dwg.text('throat', insert=(10,-40), fill='black', font_size='20px'))
        text_group.add(dwg.text('clew', insert=(sail.clew.x-40, -sail.clew.y), fill='black', font_size='20px'))
        text_group.add(dwg.text('peak', insert=(sail.peak.x, -(sail.peak.y) +50 ), fill='black', font_size='20px'))


        # find sail COE...need intersection of 2 lines for 4 sided sail..
        #    1. line from one centroid to another
        #    2. line from endpoints of vectors from centroids of component triangles
        line_1 = Line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid)
        line_2 =  Line(sail.coe.lines_perpendicular_to_centroid_line_segments[0].point_b, sail.coe.lines_perpendicular_to_centroid_line_segments[1].point_b)
        sail_centroid_point = intersection(line_1, line_2)
        transform_group.add(dwg.circle(center=(sail_centroid_point), r=2, fill='blue', stroke='black', stroke_width=1))
        text_group.add(dwg.text('COE', insert=(sail_centroid_point.x, -sail_centroid_point.x), fill='black', font_size='20px'))


        # NOTE: Methodology here:  https://drive.google.com/file/d/1bCS8gZQXRBTjdJaQH7uB7qPAZpiGT_Ts/view?usp=sharing 


        # need intersection of: 
        #    1. transform_group.add(dwg.line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid, stroke='black', stroke_width=1))
        #    2.  transform_group.add(dwg.line(
        #           sail.coe.lines_perpendicular_to_centroid_line_segments[0].point_b,
        #           sail.coe.lines_perpendicular_to_centroid_line_segments[1].point_b,
        #           stroke='blue', stroke_width=2))

        dwg.add(transform_group)
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
