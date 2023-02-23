from .point import Point

class Line:
    """
    This class implements a line in two-dimensional space.
    The line is infinite.

    Example usage:
    >>> a = Line(Point(0, 0), Point(1, 1))
    >>> print(a)
    -x + y + 0 = 0
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

    def __repr__(self):
        """
        Return a representation of this Line.
        """
        return f"Line(a={self._a}, b={self._b}, c={self._c})"

    def __str__(self):
        """
        Return a readable representation of this Line.
        """
        # TODO: make representation prettier
        return f"({self._a}x) + ({self._b}y) + ({self._c}) = 0"

def det(a, b, c, d): return a*d - b*c # determinant

def intersect(l1, l2):
    """
    Return the intersection point of two lines.
    """
    if not isinstance(l1, Line) or not isinstance(l2, Line):
        raise TypeError("arguments must be Lines")
    # https://cp-algorithms.com/geometry/lines-intersection.html
    return Point(
        -det(l1._c, l1._b, l2._c, l2._b)/det(l1._a, l1._b, l2._a, l2._b),
        -det(l1._a, l1._c, l2._a, l2._c)/det(l1._a, l1._b, l2._a, l2._b),
        )
