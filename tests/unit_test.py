from pygeo2d import *

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
