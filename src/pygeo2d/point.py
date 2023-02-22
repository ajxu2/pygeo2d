from numbers import Real
from math import isfinite, sqrt, isclose

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
        self._x = x
        self._y = y

    """
    Properties of this Point, namely the x and y coordinates.
    """
    @property
    def x(self):
        """
        The x-coordinate of this Point.
        """
        return self._x

    @property
    def y(self):
        """
        The y-coordinate of this Point.
        """
        return self._y

    def __add__(self, other):
        """
        Add a Point to another Point.
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """
        Subtract a Point from this Point.
        """
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scale):
        """
        Multiply each coordinate of this point by a factor.
        """
        if not isinstance(scale, Real):
            return NotImplemented
        if not isfinite(scale):
            raise TypeError("scale factor must be a real number")
        return Point(self.x * scale, self.y * scale)
    __rmul__ = __mul__

    def __truediv__(self, scale):
        """
        Divide each coordinate of this point by a factor.
        """
        if not isinstance(scale, Real):
            return NotImplemented
        if not isfinite(scale):
            raise TypeError("scale factor must be a real number")
        return Point(self.x / scale, self.y / scale)

    def __neg__(self):
        """
        Negate both coordinates of this point (180 degree rotation).
        """
        return Point(-self.x, -self.y)

    def __pos__(self):
        """
        Return a point identical to this point.
        """
        return Point(self.x, self.y)
        
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

    def __eq__(self, other):
        """
        Test for equality. (Note that since our coordinates can be floats,
        we use the isclose function in the math module.)
        """
        return isclose(self.x, other.x) and isclose(self.y, other.y)

def dist(p1, p2):
    """
    Return the distance between two points, p1 and p2.
    """
    if not isinstance(p1, Point) or not isinstance(p2, Point):
        raise TypeError("arguments must be Points")
    return abs(p2-p1)

def dot(p1, p2):
    """
    Return the dot product of the two vectors p1 and p2.
    """
    if not isinstance(p1, Point) or not isinstance(p2, Point):
        raise TypeError("arguments must be Points")
    return p1.x * p2.x + p1.y * p2.y

def cross(p1, p2):
    """
    Return the cross product of the two vectors p1 and p2 as a scalar.
    Specifically, the absolute value of this result is the magnitude of the
    cross product. A positive sign indicates that it points upwards from the
    x-y plane, while a negative sign indicates the opposite.
    """
    if not isinstance(p1, Point) or not isinstance(p2, Point):
        raise TypeError("arguments must be Points")
    return p1.x * p2.y - p2.x * p1.y
