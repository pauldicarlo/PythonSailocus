'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
################################################################
# class Point corresponds to the x,y coordinates of the corners 
# of a 3 or 4 sided sail (Tack, Clew, Head, Peak, and Throat)
################################################################
class Point(tuple):

    ################################################################   
#    def __str__(self):
#        return "----->("+str(self.x)+","+str(self.y)+")"

    ################################################################
    def getX(self):
        return self.x

    ################################################################
    def getY(self):
        return self.y

    ################################################################
    def isEqual(self, some_point):
        if (self.x != some_point.x):
            return False
        if (self.y != some_point.y):
            return False
        return True

    def __new__(cls, x=0, y=0):
        return super().__new__(cls, (x, y))
        
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Optional: prevent accidental creation with wrong number of args
    @classmethod
    def _validate(cls, *args):
        if len(args) != 2:
            raise ValueError(f"{cls.__name__} requires exactly 2 values, got {len(args)}")

        # You can override __new__ more strictly if desired
