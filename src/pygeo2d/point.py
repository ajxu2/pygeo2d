from numbers import Real
from math import isfinite, sqrt

def real_finite(x):
    return isinstance(x, Real) and isfinite(x)

class Point:
    """
    This class implements a point in two-dimensional space.
    (More accurately, it acts as a two-dimensional vector,
    but it's easier to think about it as a point.)

    Example usage:
    >>> a = Point(1, 2)
    >>> print(a.x)
    1
    >>> print(a)
    (1, 2)
    >>> a += Point(3, 5)
    >>> print(a)
    (4, 7)
    >>> a *= 5
    >>> print(a)
    (20, 35)
    """

    def __init__(self, x, y):
        """
        Create an instance of a Point.
        """
        if not (real_finite(x) and real_finite(y)):
            raise TypeError("point coordinates must be real numbers")
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Add a Point to another Point.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtract a Point from this Point.
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """
        Multiply each coordinate of this point by a factor.
        """
        if not real_finite(scale):
            raise TypeError("scale factor must be a real number")
        return Point(self.x * scale, self.y * scale)
    __rmul__ = __mul__

    def __truediv__(self, scale):
        """
        Divide each coordinate of this point by a factor.
        """
        if not real_finite(scale):
            raise TypeError("scale factor must be a real number")
        return Point(self.x / scale, self.y / scale)

    def __neg__(self):
        """
        Negate both coordinates of this point (180 degree rotation).
        """
        return Point(-self.x, -self.y)

    def __pos__(self):
        """
        Return this point (???).
        """
        return self
        
    def __abs__(self):
        """
        Return the distance from this point to 0.
        """
        return sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self):
        """
        Return an internal representation of this Point.
        """
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """
        Return a readable representation of this Point.
        """
        return f"({self.x}, {self.y})"
