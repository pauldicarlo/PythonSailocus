'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import uuid
from typing import List

from sailocus.geometry.point import Point
from sailocus.geometry.triangle import Triangle

class Sail(object):
    ################################################################
    def __init__(self, tack, clew, head=None, peak=None, throat=None, sail_name = None):
        '''
        All units are in millimeters.
        For a 4-sided sail, tehe following must be supplied:  tack, throat, peak, clew
        '''

        # Every sail will have unique id 
        self.sail_uuid = str(uuid.uuid4())

        self.sail_name = sail_name 
        
        params = "tack="+str(tack)+", clew="+str(clew)+", head="+str(head)+", peak="+str(peak)+", throat="+str(throat)
        #print(params)
        
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

