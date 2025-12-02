'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from typing import Optional, List

from sailocus.geometry.line import Line, intersection
from sailocus.geometry.triangle import Triangle
from sailocus.geometry.linesegment import LineSegment
from sailocus.geometry.linesegment import getPerpendicularLineSegmentPoint
from sailocus.geometry.point import Point

class Sail(object):
    ################################################################
    def __init__(self, tack, clew, head=None, peak=None, throat=None, sail_name = None):
        '''
        All units are in millimeters.
        For a 4-sided sail, tehe following must be supplied:  tack, throat, peak, clew
        '''
    
        self.sail_name = sail_name 
        
        params = "tack="+str(tack)+", clew="+str(clew)+", head="+str(head)+", peak="+str(peak)+", throat="+str(throat)
        print(params)
        
        # Some basic checks...we could have a 3 or 4 sided sail, so need to make sure we have consistnt points provided
        headSupplied = head is not None
        peakSupplied = peak is not None
        throatSupplied = throat is not None
        if all(x == headSupplied for x in (headSupplied, peakSupplied, throatSupplied)):
            raise ValueError('Sail constructor: head, peak, and throat cannot all populated or non empty.  params=' + params)
        if not ( peakSupplied == throatSupplied ):
            raise ValueError('Sail constructor: If peak or throat is populated, then both must be. params=' + params)

        self.peak = peak
        self.throat = throat
        self.tack = tack
        self.clew = clew
        self.head = head
        
        self.POINT_NAME_PEAK = "Peak"
        self.POINT_NAME_THROAT = "Throat"
        self.POINT_NAME_TACK = "Tack"
        self.POINT_NAME_CLEW = "Clew"
        self.POINT_NAME_HEAD = "Head"
        self.POINT_NAME_COE = "CoE" # Center of Effort

        self.coe = CenterOfEffort(self)

    ################################################################
    def __str__(self):
        return "[peak=" + str(self.peak) + ",throat=" + str(self.throat) + \
            ", tack=" + str(self.tack) + ", clew=" + str(self.clew) + ", head=" + str(self.head) +"]"

    ################################################################
    # peak throat
    # tack clew
    def validateSail(self):
        if self.peak is None or self.tack is None or self.clew is None:
            raise TypeError("Peak and Tack and Clew must be set")
        if self.peak.y <= self.tack.y or self.peak.y <= self.clew.y:
            raise ValueError("Peak must have y value greater than tack or clew. \n" +str(self) )
        return

    ################################################################
    # Returns the number of sides.  3 it's a triangle.
    # 4 it's a sprit or lug or something like that
    def getNumSides(self) -> int:
        if self.head is None:
            return 4
        return 3

    ################################################################
    def calculateCenterOfEffort(self) : # TODO uncomment and fix w/mypy -> CenterOfEffort:
        return CenterOfEffort(self)

    def getAsPoints(self) -> list[Point]:
        points = []

        points.append(self.peak)
        points.append(self.throat)
        points.append(self.tack)
        points.append(self.clew)

        return points

    ################################################################
    def getComponentTriangles(self) -> List[Triangle]:
        componentTriangles = []
        if ( 4 == self.getNumSides()):
            componentTriangles.append(Triangle(self.peak, self.throat, self.clew))
            componentTriangles.append(Triangle(self.throat, self.clew, self.tack))
        else:
            componentTriangles.append(Triangle(self.head, self.clew, self.tack))
        return componentTriangles



################################################################
#
################################################################
class CenterOfEffort(object):
    
    ################################################################
    def __init__(self, sail: Sail):
        
        self.sail = sail
        #self.sail.validateSail()
        
        
        ###### KEY MEMBER ATTRIBUTES *******
        self.center_of_effort = None
        self.component_centers_of_effort = []
        self.centroid_line_segments = []
        self.lines_perpendicular_to_centroid_line_segments = []
        self.lines_connecting_centroid_line_segments = []
        ###### KEY MEMBER ATTRIBUTES *******

        self.triangles = sail.getComponentTriangles()
        
        # OK... Now get the 
        for triangle in self.triangles:
            for lineSegment in triangle.getCentroidLineSegments():
                self.centroid_line_segments.append(LineSegment(lineSegment.point_a, lineSegment.point_b))
            
            center_of_effort = triangle.getCentroidPoint()

            self.component_centers_of_effort.append(center_of_effort)
            print("new center_of_effort: " + str(center_of_effort) + " size=" + str(len(self.component_centers_of_effort)))
            
        for i in self.component_centers_of_effort:
            print("\t center_of_effort is " + str(i))    
            
                
        if len(self.component_centers_of_effort) > 1: 
            print("a=" + str(self.component_centers_of_effort[0]) + ", b=" + str(self.component_centers_of_effort[1]) )
            self.lines_connecting_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[0], self.component_centers_of_effort[1]))
        else:
            self.center_of_effort = self.component_centers_of_effort[0]
            return # 3 pointed sail, so easy, we are done and can return


        triangleArea1 =  Triangle(self.sail.throat,self.sail.clew,self.sail.peak).area()
        triangleArea2 = Triangle(self.sail.throat, self.sail.clew, self.sail.tack).area()
        print("triangleArea1="+str(triangleArea1) + ", triangleArea2="+str(triangleArea2))
        
        
        tp1 = getPerpendicularLineSegmentPoint(self.component_centers_of_effort[0], self.component_centers_of_effort[1], int(triangleArea2/1000))
        self.lines_perpendicular_to_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[0], tp1))
        tp2 = getPerpendicularLineSegmentPoint(self.component_centers_of_effort[1], self.component_centers_of_effort[0], int(-1*triangleArea1/1000))
        self.lines_perpendicular_to_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[1], tp2))
        
        self.tp_lineSegment = LineSegment(tp1, tp2)


        line1 = Line(self.lines_connecting_centroid_line_segments[0].point_b, self.lines_connecting_centroid_line_segments[0].point_a)
        line2 = Line(tp1, tp2)
        
        self.center_of_effort = intersection(line1, line2)
        


class TriangleCenterOfEffort(object):
    ################################################################
    def __init__(self, triangle):
        assert triangle.getNumSides() == 3
