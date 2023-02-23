from .point import Point, dist
from numbers import Real
from math import isfinite, isclose

def real_finite(x):
    return isinstance(x, Real) and isfinite(x)

class Circle:
    """
    This class implements a circle in two-dimensional space.
    Example usage:
    >>> a = Circle(Point(0, 0), 5)
    >>> Point(3, -4) in a
    True
    >>> # TODO: add next part
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
        # TODO: possibly make these readonly attributes?
        self.center = center
        self.radius = radius

    def __repr__(self):
        """
        Return a representation of this Circle.
        """
        return f"Circle(center={self.center}, radius={self.radius})"

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
        if not isinstance(pt, Point):
            raise TypeError("argument must be Point")
        return isclose(dist(pt, self.center), self.radius)
