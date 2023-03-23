from .point import Point
from math import isclose

class Line:
    """
    This class implements a line in two-dimensional space.
    The line is infinite.

    Example usage:
    >>> a = Line(Point(0, 0), Point(1, 1))
    >>> print(a)
    -x + y + 0 = 0
    >>> Point(2.4, 2.4) in a
    True
    >>> b = Line(Point(1, 4), Point(3, 0))
    >>> print(intersect(a, b))
    (2, 2)
    """

    def __init__(self, p1, p2):
        """
        Create an instance of a Line based on two Points.
        """
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError("arguments must be Points")
        # https://cp-algorithms.com/geometry/segment-to-line.html
        # line written in form ax + by + c = 0
        self._a = p1.y - p2.y
        self._b = p2.x - p1.x
        self._c = -self._a * p1.x - self._b * p1.y

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
    
    @property
    def c(self):
        return self._c

    def __repr__(self):
        """
        Return a representation of this Line.
        """
        return f"Line(a={self.a}, b={self.b}, c={self.c})"

    def __str__(self):
        """
        Return a readable representation of this Line.
        """
        # TODO: make representation prettier
        return f"({self.a}x) + ({self.b}y) + ({self.c}) = 0"

    def __contains__(self, pt):
        """
        Returns True iff pt is on this Line.
        """
        return isclose(self.a * pt.x + self.b * pt.y + self.c, 0)

    def intersect(self, l2):
        """
        Return the intersection of this line and l2.
        """
        # TODO: handle parallel, concurrent lines
        det = lambda a, b, c, d: a*d - b*c
        return Point(
            -det(self.c, self.b, l2.c, l2.b)/det(self.a, self.b, l2.a, l2.b),
            -det(self.a, self.c, l2.a, l2.c)/det(self.a, self.b, l2.a, l2.b),
            )
