'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: paul.dicarlo@gmail.com
'''
# tests/sail/test_sail.py

import pytest
from sailocus.geometry.point import Point  # direct import works thanks to python_paths
from sailocus.geometry.line import Line  # direct import works thanks to python_paths
from sailocus.sail import sail  # direct import works thanks to python_paths

# -----------------------------
# Fixtures (if needed)
# -----------------------------

# -----------------------------
# Basic construction & repr
# -----------------------------
def test_line_creation():
    peak = Point(213, 510)
    throat = Point(10, 233)
    tack = Point(0, 0) 
    clew = Point(397, 29) 

    xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sail_name = "Four sided sail")
    xsail.validateSail()