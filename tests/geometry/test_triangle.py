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
    return [ Point(0, 0), Point(20, 20), Point(40, 0) ]

    

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_triangle(triangle_points):
    tr1 = Triangle(triangle_points[0], triangle_points[1], triangle_points[2])

def test_triangle_area():
    triangle = Triangle( Point(0,0), Point(0,10), Point(10,0))
    area=10*10/2
    assert area == triangle.area()

    triangle = Triangle( Point(0,0), Point(10,10), Point(10,-10))
    area=20*10/2
    assert area == triangle.area()


def test_getCentroidLineSegments():
    vertex1 = Point(0,0)
    vertex2 = Point(0,10)
    vertex3 = Point(10,0)
    vertices = [vertex1, vertex2, vertex3]
    vertices_set = set(vertices)

    triangle = Triangle(vertex1, vertex2, vertex3) 
    lineSegments = triangle.getCentroidLineSegments()

    expected_vals = { 
        vertex1: Point(5,5),
        vertex2: Point(5,0),
        vertex3: Point(0,5,)
        }


    assert 3 == len(lineSegments)
    for lineSegment in lineSegments:
        # TODO:  right now we are relying on the vertex point being lineSegment.point_b
        assert lineSegment.point_b in vertices_set 
        assert lineSegment.point_a == expected_vals[lineSegment.point_b]
        vertices_set.remove(lineSegment.point_b)
        print('hello' + str(vertices_set))
    # at this point vertices_set 
    assert len(vertices_set) == 0  


def test_getCentroidPoint():
    vertex1 = Point(0,0)
    vertex2 = Point(0,10)
    vertex3 = Point(10,0)
    vertices = [vertex1, vertex2, vertex3]
    vertices_set = set(vertices)

    triangle = Triangle(vertex1, vertex2, vertex3) 
    x = triangle.getCentroidPoint