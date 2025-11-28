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

    # For a given Sail object, write a diagram of it with the COE to a SVG file.
    def createSailSVG(self, sail:Sail, path_to_file: str, write_file: bool, margin_off_set= Point(0,0)) -> svgwrite.Drawing:
        points = sail.getAsPoints()

        if sail is None:
            raise ValueError("Sail must not be done")

        #TODO - need to handle offest for entire set of points/polygons/etc

        # We need to calcute the canvas size, we create a point to service as the
        # margin, it's offset from (0,0) will be used in all four corners.
        canvas_size = calculateCanvasSize(points, margin_off_set)
        width, height = canvas_size

        dwg = svgwrite.Drawing(path_to_file, size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'))
        transform_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")

        # Background color
        dwg.add(dwg.rect(insert=(0, 0), size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'), fill='darkseagreen'))

        # Basic sail shape
        trapezoid = dwg.polygon(
            points=points,
            fill='ivory',
            stroke='black',
            stroke_width=1
        )
        transform_group.add(trapezoid)
        # draw line from throat to clew
        transform_group.add(dwg.line(sail.throat, sail.clew, stroke='black', stroke_width=1, stroke_dasharray='9,5'))

        # NOTE: this will only work for a 4 sided sail...

        # NOTE: Methodology here:  https://drive.google.com/file/d/1bCS8gZQXRBTjdJaQH7uB7qPAZpiGT_Ts/view?usp=sharing 
        # Sail.coe has all of the following lines and coe calculated.  
        # Here we just put them into the SVG
        # line from one triangle of the sail centroid to the other
        transform_group.add(dwg.line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid, stroke='red', stroke_width=1))
        # then get the lines perpendicular to that line between centroids...
        for line_segment in sail.coe.lines_perpendicular_to_centroid_line_segments:
            transform_group.add(dwg.line(line_segment.point_a , line_segment.point_b, stroke='purple', stroke_width=2))
        # and the line from end point of vectors from perpendicuar lines
        transform_group.add(dwg.line(
            sail.coe.lines_perpendicular_to_centroid_line_segments[0].point_b,
            sail.coe.lines_perpendicular_to_centroid_line_segments[1].point_b,
            stroke='blue', stroke_width=1))
        # at this point, we have an intersection of the following:
        #      1. line from one triangle of the sail centroid to the other 
        #     2. ine from end point of vectors from perpendicuar lines
        # the intersection of which gives us sail.coe.center_of_effort which has already been calculated

        transform_group.add(dwg.circle(center=(sail.coe.center_of_effort), r=2, fill='blue', stroke='black', stroke_width=1))

        # Need an inner group that flips again so text will be in right orientation 
        text_group = transform_group.add(dwg.g(transform="scale(1, -1)"))  # Flip back!

        if sail.throat is None:
            raise ValueError("sail.throat cannot be None")
        if sail.peak is None:
            raise ValueError("sail.peak cannot be None")
        if sail.coe is None:
            raise ValueError("sail.coecannot be None")
        if sail.coe.center_of_effort is None:
            raise ValueError("sail.coecannot.center_of_effort be None")

        # TODO: Make this better.
        labelPoint(dwg, text_group, [sail.POINT_NAME_TACK, str(sail.tack)], 
                   Point(sail.tack.x, -1*sail.tack.y-40), 'black', '20px' )
        labelPoint(dwg, text_group, [sail.POINT_NAME_THROAT, str(sail.throat)], 
                   Point(sail.throat.x, -240), 'black', '20px' )
        labelPoint(dwg, text_group, [sail.POINT_NAME_CLEW, str(sail.clew)], 
                   Point(sail.clew.x-75, -sail.clew.y), 'black', '20px' )
        labelPoint(dwg, text_group, [sail.POINT_NAME_PEAK, str(sail.peak)], 
                   Point(sail.peak.x, -(sail.peak.y) + 50), 'black', '20px' )
        labelPoint(dwg, text_group, [sail.POINT_NAME_COE +  ': ' + str(sail.coe.center_of_effort)], 
                   Point(sail.coe.center_of_effort.x, -sail.coe.center_of_effort.x), 'black', '20px' )

        relocation_group = dwg.g(transform=f"translate("+str(margin_off_set.x) +",-"+str(margin_off_set.y)+")")
        relocation_group.add(transform_group)

        dwg.add(relocation_group)

        if write_file:
            dwg.save()

        return dwg

def labelPoint(dwg, dwg_group, text_lines:list[str], insert_point: Point, fill_color: str, font_size:str): 

    next_start_point = insert_point    
    for text_line in text_lines:
        dwg_group.add(dwg.text(text_line, insert=next_start_point, fill=fill_color, font_size=font_size  ))
        next_start_point = Point(next_start_point.x, next_start_point.y+20)

        
def calculateCanvasSize(points: list[Point], off_set: Point):

    # Find the maximum X and Y from the points supplied
    maxX = 0
    maxY = 0
    for x,y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y        

    # Using off_set, we set a canvas size to use which has room for borders based on off_set Point
    off_set_x, off_set_y = off_set
    canvas_size = (maxX + 2*off_set_x, maxY + 2*off_set_y)

    return canvas_size
