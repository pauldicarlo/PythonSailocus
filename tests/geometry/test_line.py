'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_line.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.line import Line  # direct import works thanks to python_paths

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
    line1 = Line(p1, p2)
    assert line1.slope == 1.0


    p1b = Point(1.0, 1.0)
    p2b = Point(1.0, 7.0)
    line2 = Line(p1b, p2b)
    assert line2.slope == None



