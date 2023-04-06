Point
=====

.. class:: Point

    A point in a two-dimensional plane.

    .. method:: __init__(x, y)

        Creates a new Point object from Cartesian coordinates.

        :param x: the x-coordinate of the point
        :param y: the y-coordinate of the point

    .. property:: x

        The x-coordinate of the point.

    .. property:: y

        The y-coordinate of the point.

    .. method:: __add__(other)

        Add this point to another point with vector addition.
        (In other words, the individual coordinates are added.)

        >>> Point(1, 2) + Point(3, 4)
        Point(4, 6)

        :param Point other: the point to add
        :return: the result of the addition

    .. method:: __sub__(other)

        Subtract two points with vector subtraction.
        (In other words, the individual coordinates are subtracted.)

        >>> Point(1, 2) - Point(3, 4)
        Point(-2, -2)

        :param Point other: the point to subtract
        :return: the result of the subtraction

    .. method:: __mul__(scale)

        Scale this point up from the origin by a certain scale factor.
        (In other words, each coordinate is multiplied by *scale*.)

        >>> Point(1, 2) * 3
        Point(3, 6)

        :param scale: the scale factor
        :return: the result of the multiplication

    .. method:: __rmul__(scale)

        Equivalent to :meth:`__mul__`, but in the reverse order.

        >>> 3 * Point(1, 2)
        Point(3, 6)

        :param scale: the scale factor
        :return: the result of the multiplication

    .. method:: __truediv__(scale)

        Scale this point down from the origin by a certain scale factor.
        (In other words, each coordinate is divided by *scale*.)

        >>> Point(3, 6) / 3
        Point(1.0, 2.0)

        :param scale: the scale factor
        :return: the result of the division

    .. method:: __neg__()

        Rotate this point by 180 degrees about the origin. 
        Equivalent to negating both coordinates.

        >>> -Point(1, 2)
        Point(-1, -2)

        :return: the negated point

    .. method:: __pos__()

        Return this point.

        >>> +Point(1, 2)
        Point(1, 2)

        :return: the same point

    .. method:: __abs__()

        Return the Euclidean distance from this point to the origin.

        >>> abs(Point(3, -4))
        5.0

        :return: the distance from the point to the origin

    .. method:: __repr__()

        Return string representation of this point.

        :return: string representation of this point

    .. method:: __str__()

        Return string representation of this point, 
        but formatted like a tuple.

        >>> print(Point(1, 2))
        (1, 2)

        :return: string representation of this point, formatted like tuple

    .. method:: __eq__(other)

        Returns whether or not two points are located at the same place
        in the Cartesian plane. (Internally, this function uses ``math.isclose``.)

        >>> Point(3, 4) - Point(1, 1) == Point(2, 3)
        True

        :param Point other: the point to test for equality
        :return: whether or not the two points are located at the same place

    .. method:: dist(other)

        Return the Euclidean distance from this point to *other*.
        Equivalent to ``abs(other-self)``.

        >>> Point(2, 3).dist(Point(5, 7))
        5.0

        :param Point other: the point to take the distance to
        :return: the computed distance

    .. method:: dot(other)

        Return the `dot product <https://en.wikipedia.org/wiki/Dot_product>`_ of this vector and *other*.

        >>> Point(2, 6).dot(Point(5, 2))
        22

        :param Point other: the point to dot with
        :return: the dot product

    .. method:: cross(other)

        Return the *magnitude* of the `cross product <https://en.wikipedia.org/wiki/Cross_product>`_ of this vector and *other*.
        A positive result indicates that the cross product points upwards from the plane,
        while a negative result indicates the opposite.

        >>> Point(2, 6).cross(Point(5, 2))
        -26

        :param Point other: the point to cross with
        :return: the cross product
