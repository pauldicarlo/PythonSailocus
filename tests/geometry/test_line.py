'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_line.py

from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.line import Line # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_line_creation():
    # Simple case where slope would be 1
    p1 = Point(10, 10)
    p2= Point(75, 75)
    line1 = Line(p1, p2)
    assert line1.slope == 1

    # negative slope
    p1 = Point(10, 75)
    p2= Point(75, 0)
    line = Line(p1, p2)
    assert line.slope is not None
    assert line.slope < 0 


    # Slope is undefined/None
    p1 = Point(10, 10)
    p2 = Point(10, 70)
    line = Line(p1, p2)
    assert line.slope is None

    # Slope = 0
    y = 50
    p1 = Point(10, y)
    p2 = Point(50, y)
    line = Line(p1, p2)
    assert line.slope == 0
