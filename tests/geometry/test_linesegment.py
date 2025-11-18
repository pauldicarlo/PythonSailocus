'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_linesegment.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.linesegment import LineSegment, getPerpendicularLineSegmentPoint  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_line_creation():
    # Simple case where slope would be 1.0
    p1 = Point(1.0, 1.0)
    p2= Point(7.5, 7.5)
    linesegment1 = LineSegment(p1, p2)
    assert linesegment1.point_a.x == 1.0
    assert linesegment1.point_a.y == 1.0
    assert linesegment1.point_b.x == 7.5
    assert linesegment1.point_b.y == 7.5


def test_getPerpendicularLineSegmentPoint():

    # for a line segment with an undefined slope 
    point_a = Point(0,0)
    point_b = Point(0, 8)
    p = getPerpendicularLineSegmentPoint( point_a, point_b, weight = 30)
    print(str(p))
    assert Point(30, 0) == p

    # for a line segement with a slope of 0
    point_a = Point(0,8)
    point_b = Point(8, 8)
    p = getPerpendicularLineSegmentPoint( point_a, point_b, weight = 30)
    assert Point(0, 38) == p

    # for a line segment with a postitive slope
    point_a = Point(0,0)
    point_b = Point(10, 10)
    p = getPerpendicularLineSegmentPoint( point_a, point_b, weight = 10)
    assert Point(10, -10) == p

    # TODO:  This doesn't look right
    # for a line segment with a negative slope
    point_a = Point(0, 0)
    point_b = Point(10,-10)
    p = getPerpendicularLineSegmentPoint( point_a, point_b, weight = 10)
    assert Point(10, 10) == p