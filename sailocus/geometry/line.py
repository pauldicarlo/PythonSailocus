'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''


from sailocus.geometry.point import Point

from typing import Optional

#########################################################
# For a given line defined by two points,
# return the slope.
#########################################################
def getSlope(point_a: Point, point_b: Point) -> float:
    method="getSlope():"

    if point_a is None or point_b is None:
        raise ValueError("Both points in parameters must not be None: point_a=" + str(point_a) + ", point_b=" + str(point_b))

    if point_a == point_b:
        raise ValueError("Both points cannot be identical for calculating line slope: point_a=" + str(point_a) + ", point_b=" + str(point_b))

    try:
        theSlope = (float(point_b.getY()-point_a.getY())) /   (float(point_b.getX()-point_a.getX()))
        print( method +" slope=" + str(theSlope) + "=  ( (" +  str(point_b.getY()) +")-("+str(point_a.getY()) + ") ) / ( (" +  str(point_b.getX()) +")-("+str(point_a.getX()) +"))" )
        return (theSlope )
    except ZeroDivisionError:
        # TODO: zero devision is slope of 0
        # return None #slope is undefined
        return 0


#########################################################
# Given a slope an an existing point, find the y intercept
#########################################################
def yIntercept(slope: float, point: Point) -> float:
    
    if slope is None:
        return None
    
    #y=mx+b
    #b=mx-y
    intercept = float(float(point.getY()) - float(slope*point.getX()))
    return intercept



#########################################################
# For a given X, calculate th
# 
# ====> y=mx+b
# ====> y=slope*x + b
#########################################################
def newPointOnLine(slope, newX, existingPoint: Point) -> Point:
    # TODO - need to be able to handled slope=NONE (undefined)

    # TODO 
    if slope is None or newX is None or existingPoint is None:
        raise ValueError("newPointOnLine(slope, newX, ExistingPoint): <-- none of args may be None!")

    #y=slope*x+b  <-- we need to determine what B is ==> b=y-slope*x
    # that's why we needed an existing point to start with.
    b= float(existingPoint.getY())-float(slope)*float(existingPoint.getX())
    #y=mx+b
    newY = slope*newX+int(b)
    return Point(newX, int(newY))


#########################################################
#Class Line - represents a line.
#########################################################
class Line(object):

    #########################################################
    def __init__(self, point_a, point_b, slope = None):
    
        self.point_a = point_a
        self.point_b = point_b
        self.slope = slope
        
        if self.point_a is None or ( self.point_b is None and self.slope is None ):
            raise ValueError("Line: Constructor parameters require at least point a and ( point b or slope):" + str(self))
            
        if slope is None:  # calculate the slope:
            self.slope = getSlope(self.point_a, self.point_b)
            
        self.validate()

    #########################################################
    def validate(self):
        #validate that the two points and slope are consistent.  For some new x value...
        if self.slope is None:
            if (self.point_a.x != self.point_b.x):
                raise ValueError('Bad slope for points of Line')
            else:
                pass # vertical line
        else:    
            newPointA= newPointOnLine(self.slope, self.point_a.x+10, self.point_b)
            newPointB = newPointOnLine(self.slope, self.point_b.x+10, self.point_a)
            if (( self.point_a.isEqual(newPointA)) or ( self.point_b.isEqual(newPointB))):
                raise ValueError("Validation of points and slope do not work out. line=" + str(self) +
                    " calculated newPointA=" + str(self.point_a) + " and newPointB=" + str(self.point_b))

    #########################################################
    def __str__(self):
        return str("["+str(self.point_a) + ", " + str(self.point_b) + ", slope=" + str(self.slope) + "]")        
        
        
        


#########################################################
#
# Given two sets of points, a line defined by each set, find the point at which they intersect.
#
# https://stackoverflow.com/questions/31506740/java-find-intersection-of-two-lines
#########################################################
def intersection(line_a: Line, line_b: Line) -> Optional[Point]:
    method="intersection"
    
    # y = mx + b
    
    m1=line_a.slope
    m2=line_b.slope
    
    #print("slope1="+str(m1))
    #print("slope2="+str(m2))
    
    b1=yIntercept(m1, line_a.point_a);
    b2=yIntercept(m2, line_b.point_b);
    
    #print("yIntercept1="+str(b1))
    #print("yIntercept2="+str(b2))
    
    #print(type(m1))
    #print(type(b1))
    
    # To find the midpoint
    # y = mx + b
    print(method + ": b1="+str(b1)+", b2="+str(b2) + ", m1=" + str(m1) + ", m2=" + str(m2))
    
    # TODO: Need to get this working for undefined slopes.  Needs better/more clean logic for all situations
    # if Slopes are the same, 
    # lines never intersect...
    # or at least have no single point of intersect
    if (m1 == m2):  
        return None
    if m1 is None:
        pass
    if m2 is None:
        pass

    if b1 == None:
        pass
    if b2 == None:
        pass
    
    x = int((b2 -b1)/(m1-m2))
    y = int(m1*(float(b2-b1)/float(m1-m2)) + float(b1))
    return Point(x,y)



        
#########################################################
# M A I N 
#########################################################
if __name__ == "__main__":
    # just some tests...
    l = Line(Point(1,1),Point(4,4))
    print(l)
    
    #print (Line (None, None, None))
    print(str(getSlope(Point(50,10), Point(24,115))))
    try:
        print( str (Line(Point(1,1), None, 1.0)))
        raise ValueError("Expected a value error here!!!")
    except ValueError:
        print('Expected error')

    
    
