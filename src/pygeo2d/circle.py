from .point import Point
from .line import Line
from .util import dist
from numbers import Real
from math import isfinite, isclose, sqrt

def real_finite(x):
    return isinstance(x, Real) and isfinite(x)

class Circle:
    """
    This class implements a circle in two-dimensional space.
    Example usage:
    >>> a = Circle(Point(0, 0), 5)
    >>> Point(3, -4) in a
    True
    >>> intersect(Line(Point(0, 6), Point(1, 6)), a)
    []
    >>> intersect(Line(Point(0, 5), Point(1, 5)), a)
    [Point(0, 5)]
    >>> intersect(Line(Point(0, 0), Point(1, 0)), a)
    [Point(-5, 0), Point(5, 0)]
    """
    def __init__(self, center, radius):
        """
        Create a new instance of a Circle based on a center and radius.
        """
        if not isinstance(center, Point):
            raise TypeError("center argument must be a Point")
        if not real_finite(radius):
            raise TypeError("radius must be a real number")
        self._center = center
        self._radius = radius

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def __repr__(self):
        """
        Return a representation of this Circle.
        """
        return f"Circle(center={repr(self.center)}, radius={self.radius})"

    def __str__(self):
        """
        Return a readable representation of this Circle.
        TODO: make prettier
        """
        return (f"(x-({self.center.x}))^2 + (y-({self.center.y}))^2"
            f" = ({self.radius})^2"
            )

    def __contains__(self, pt):
        """
        Returns True iff pt is on this Circle.
        """
        return isclose(dist(pt, self.center), self.radius)

    def intersect(self, l):
        """
        Calculate the intersection point(s) between this Circle and a Line.
        """
        # https://cp-algorithms.com/geometry/circle-line-intersection.html
        # translate circle and line to (0, 0)
        r = self.radius
        nl = Line(l.p1 - self.center, l.p2 - self.center) # new line
        d0 = abs(nl.c) / sqrt(nl.a*nl.a + nl.b*nl.b) # shortest distance from line to origin
        x0 = -nl.a*nl.c / (nl.a*nl.a + nl.b*nl.b)
        y0 = -nl.b*nl.c / (nl.a*nl.a + nl.b*nl.b)
        if isclose(d0, r):
            # 1 solution
            return [Point(x0, y0) + self.center]
        elif d0 > r:
            # 0 solutions
            return []
        # 2 solutions
        d = sqrt(r*r - nl.c*nl.c / (nl.a*nl.a + nl.b*nl.b)) # half the length of the chord
        m = sqrt(d*d / (nl.a*nl.a + nl.b*nl.b))
        ax = x0 + nl.b * m
        ay = y0 - nl.a * m
        bx = x0 - nl.b * m
        by = y0 + nl.a * m
        return [Point(ax, ay) + self.center, Point(bx, by) + self.center]
