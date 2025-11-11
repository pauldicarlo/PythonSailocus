'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/geometry/test_point.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------
@pytest.fixture
def origin() -> Point:
    return Point(0.0, 0.0)


'''
@pytest.fixture
def p1() -> Point:
    return Point(3.0, 4.0)


@pytest.fixture
def p2() -> Point:
    return Point(-2.0, 5.0)
'''

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_point_creation():
    p = Point(1.5, -2.8)
    assert p.x == 1.5
    assert p.y == -2.8


'''
def test_point_default_constructor():
    p = Point()
    assert p.x == 0.0
    assert p.y == 0.0


def test_point_repr():
    p = Point(1.0, 2.0)
    assert repr(p) == "Point(x=1.0, y=2.0)"
    assert str(p) == "(1.0, 2.0)"


# -----------------------------
# Equality & hashing
# -----------------------------
def test_point_equality():
    assert Point(1.0, 2.0) == Point(1.0, 2.0)
    assert Point(1.0, 2.0) != Point(1.0, 3.0)
    assert Point(1.0, 2.0) != (1.0, 2.0)  # different type


def test_point_hashable():
    p = Point(1.0, 2.0)
    assert hash(p) == hash(Point(1.0, 2.0))
    # Useful for sets/dicts
    point_set = {Point(0, 0), Point(1, 1), Point(0, 0)}
    assert len(point_set) == 2


# -----------------------------
# Arithmetic operations
# -----------------------------
def test_addition(p1, p2):
    result = p1 + p2
    assert result == Point(1.0, 9.0)
    assert isinstance(result, Point)


def test_subtraction(p1, p2):
    result = p1 - p2
    assert result == Point(5.0, -1.0)


def test_scalar_multiplication(p1):
    assert p1 * 2.0 == Point(6.0, 8.0)
    assert 2.0 * p1 == Point(6.0, 8.0)  # __rmul__
    assert p1 * 2 == Point(6.0, 8.0)    # supports int too


def test_division(p1):
    assert p1 / 2.0 == Point(1.5, 2.0)


def test_in_place_operations(p1):
    p1 += Point(10, 20)
    assert p1 == Point(13.0, 24.0)

    p1 -= Point(3, 4)
    assert p1 == Point(10.0, 20.0)


# -----------------------------
# Geometric methods
# -----------------------------
def test_distance(origin, p1):
    assert origin.distance_to(p1) == 5.0
    assert p1.distance_to(origin) == 5.0
    # Should be symmetric
    assert p1.distance_to(Point(3, 4)) == 0.0


def test_magnitude(p1):
    assert p1.magnitude() == 5.0
    assert p1.length() == 5.0  # alias if you have it


def test_normalize(p1):
    normalized = p1.normalized()
    assert normalized.magnitude() == pytest.approx(1.0)
    assert normalized == Point(0.6, 0.8)


def test_dot_product(p1, p2):
    assert p1.dot(p2) == pytest.approx(14.0)  # 3*(-2) + 4*5


def test_cross_product_2d(p1, p2):
    # In 2D, cross product returns scalar (z-component)
    assert p1.cross(p2) == pytest.approx(23.0)  # 3*5 - 4*(-2)


# -----------------------------
# Edge cases & errors
# -----------------------------
def test_division_by_zero():
    p = Point(1, 2)
    with pytest.raises(ZeroDivisionError):
        p / 0.0


def test_invalid_coordinates():
    with pytest.raises(TypeError):
        Point("1", 2)  # type: ignore


# -----------------------------
# Parametrized tests (great for coverage)
# -----------------------------
@pytest.mark.parametrize(
    "x1,y1,x2,y2,expected_dist",
    [
        (0, 0, 3, 4, 5.0),
        (0, 0, -3, -4, 5.0),
        (1, 1, 1, 1, 0.0),
        (0, 0, 1, 0, 1.0),
    ],
)
def test_distance_parametrized(x1, y1, x2, y2, expected_dist):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    assert p1.distance_to(p2) == pytest.approx(expected_dist)
'''