from pygeo2d import *
from math import isclose
from random import uniform

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

def test_line():
    """
    test the functionalities of the Line class
    """
    a = Line(Point(0, 0), Point(1, 1))
    assert Point(2.4, 2.4) in a
    b = Line(Point(1, 4), Point(3, 0))
    assert intersect(a, b) == Point(2, 2)

def test_line_ceva():
    """
    test Ceva's theorem
    """
    for i in range(1000):
        # First, select 3 random points as our triangle.
        A = Point(uniform(-10, 10), uniform(-10, 10))
        B = Point(uniform(-10, 10), uniform(-10, 10))
        C = Point(uniform(-10, 10), uniform(-10, 10))
        # Next, select a random point which the three lines will concur at.
        P = Point(uniform(-10, 10), uniform(-10, 10))
        # Draw the cevians.
        a = Line(A, P)
        b = Line(B, P)
        c = Line(C, P)
        # Intersect cevians with sides of triangle.
        D = intersect(a, Line(B, C))
        E = intersect(b, Line(A, C))
        F = intersect(c, Line(A, B))
        # Check Ceva's!
        assert isclose(dist(A,F)/dist(F,B)*dist(B,D)/dist(D,C)*dist(C,E)/dist(E,A), 1)

def test_circle():
    a = Circle(Point(0, 0), 5)
    #assert intersect(Line(Point(0, 6), Point(1, 6)), a) == []
    #assert intersect(Line(Point(0, 5), Point(1, 5)), a) == [Point(0, 5)]
    #assert intersect(Line(Point(0, 0), Point(1, 0)), a) == [Point(-5, 0), Point(5, 0)]
    assert Point(3, -4) in a
