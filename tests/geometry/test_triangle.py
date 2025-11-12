'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_triangle.py

import pytest

from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.triangle import Triangle  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------
@pytest.fixture
def triangle_points() -> list[Point]:
    return [ Point(0.0, 0.0), Point(20, 20), Point(40, 40) ]

    

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_triangle(triangle_points):
    tr1 = Triangle(triangle_points[0], triangle_points[1], triangle_points[2])