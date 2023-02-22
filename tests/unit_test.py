from pygeo2d import *
from math import isclose

def test_point():
    """
    test the functionalities of the Point class
    """
    a = Point(1, 2)
    assert a.x == 1
    assert str(a) == "(1, 2)"
    a += Point(3, 5)
    assert a == Point(4, 7)
    a *= 5
    assert a == Point(20, 35)
    a /= 5
    assert a == Point(4, 7)
    a -= Point(2, 1)
    assert a == Point(2, 6)
    b = Point(5, 2)
    assert isclose(dist(a, b), 5)
    assert isclose(dot(a, b), 22)
    assert isclose(cross(a, b), -26)
