from numbers import Real

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
    """

    def __init__(self, x, y):
        """
        Create an instance of a Point.
        """
        if not(isinstance(x, Real) and isinstance(y, Real)):
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
        if not isinstance(scale, Real):
            raise TypeError("scale factor must be a real number")
        return Point(self.x * scale, self.y * scale)
    __rmul__ = __mul__

    def __div__(self, scale):
        """
        Divide each coordinate of this point by a factor.
        """
        if not isinstance(scale, Real):
            raise TypeError("scale factor must be a real number")
        return Point(self.x / scale, self.y / scale)

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
