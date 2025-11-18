'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''

from sailocus.geometry.point import Point
from sailocus.geometry.line import newPointOnLine, getSlope


#############################################################################################
# For pointA, return a point weighed perpendicular to the linesegement as defined by pointb
#############################################################################################
def getPerpendicularLineSegmentPoint(pointA: Point, pointB: Point, weight) -> Point:
        print("__________________________________________________")
        theSlope = getSlope(pointA, pointB)

        if theSlope is None:
            perpendicularSlope = 0
        elif theSlope == 0:
            perpendicularSlope = None
        else:
            perpendicularSlope = float(-1/theSlope)

        if perpendicularSlope is None:
            newPoint = Point(pointA.x, pointA.y + weight)
        else:
            x = pointA.getX()+weight
            newPoint = newPointOnLine( perpendicularSlope, x, pointA )

        return newPoint

################################################################
#
################################################################
class LineSegment(object):
    
    ################################################################
    def __init__(self, point_a: Point, point_b: Point):
        
        if not isinstance(point_a, Point):
            raise ValueError("point_a is not a point: " + str(point_a))
        if not isinstance(point_b, Point):
            raise ValueError("point_b is not a point: " + str(point_b))
        
        self.point_a = point_a
        self.point_b = point_b
        
        self.validate()
        
    ################################################################
    def __str__(self):
        return "LineSegement=[" + str(self.point_a) + ", " + str(self.point_b) + "]"
        
    ################################################################
    def validate(self):
        if self.point_a is None or self.point_b is None:
            raise ValueError("LineSegement: both points must be non-null.  " + str(self))
    
    ################################################################    
    def getMidpoint(self) -> Point:
        self.validate()
        
        return Point(int((self.point_a.x+self.point_b.x)/2), int((self.point_a.y+self.point_b.y)/2))  
    
    
################################################################
# M A I N 
################################################################    
if __name__ == "__main__":
    print(str(LineSegment(Point(0,2), Point(0,4)).getMidpoint().isEqual(Point(0,3))))
    #assert(  False == LineSegment(Point(0,2), Point(0,4)).getMidpoint().isEqual(Point(0,3))), print("Yahoo")
    
