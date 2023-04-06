Circle
======

.. class:: Circle
    
    A circle in a two-dimensional plane.

    .. method:: __init__(center, radius)

        Create an instance of a Circle based on a center and radius.

        :param Point center: the center of the circle
        :param radius: the radius of the circle

    .. property:: center

        The center of the circle.

    .. property:: radius

        The radius of the circle.

    .. method:: __repr__()

        Return string representation of this circle.

        >>> a = Circle(Point(0, 0), 5)
        >>> a
        Circle(center=(0, 0), radius=5)

        :return: string representation of this circle

    .. method:: __str__()

        Return string representation of this circle, in the form of an equation.

        >>> a = Circle(Point(0, 0), 5)
        >>> print(a)
        (x-(0))^2 + (y-(0))^2 = (5)^2

        :return: string representation of this circle in an equation

    .. method:: __contains__(pt)

        Return whether or not *pt* is on this circle.

        >>> a = Circle(Point(0, 0), 5)
        >>> Point(3, -4) in a
        True
        >>> Point(4, -4) in a
        False

        :param Point pt: the point to test
        :return: whether the point is on this circle

    .. method:: intersect(l)

        Return a list of intersection point(s) between this circle and a line.

        >>> a = Circle(Point(3, 4), 5)
        >>> a.intersect(Line(Point(0, 10), Point(1, 10)))
        []
        >>> a.intersect(Line(Point(0, 9), Point(1, 9)))
        [Point(3, 9)]
        >>> a.intersect(Line(Point(0, 0), Point(1, 0)))
        [Point(6, 0), Point(0, 0)]

        :param Line l: the line to intersect with
        :return: a list of intersection point(s)
