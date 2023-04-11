Line
====

.. class:: Line
    
    A line in a two-dimensional plane. The line extends to infinity in both directions.

    .. method:: __init__(p1, p2)

        Create an instance of a Line based on two points.

        >>> print(Line(Point(0, 0), Point(1, 1)))
        (-1x) + (1y) + (0) = 0

        :param Point p1: a point on the line
        :param Point p2: another point on the line

    .. property:: a

        The value of a when the line is written in the form ax + by + c = 0.

    .. property:: b

        The value of b when the line is written in the form ax + by + c = 0.

    .. property:: c

        The value of c when the line is written in the form ax + by + c = 0.

    .. property:: p1

        A point on the line. Mostly intended for internal use.

    .. property:: p2

        Another point on the line. Mostly intended for internal use.

    .. method:: __repr__()

        Return string representation of this line.

        >>> a = Line(Point(0, 0), Point(1, 1))
        >>> a
        Line(p1=Point(0, 0), p2=Point(1, 1))

    .. method:: __str__()

        Return string representation of this line, written as an equation.

        >>> a = Line(Point(0, 0), Point(1, 1))
        >>> print(a)
        (-1x) + (1y) + (0) = 0

    .. method:: __contains__(pt)

        Return whether or not *pt* is on this line.

        >>> a = Line(Point(0, 0), Point(1, 1))
        >>> Point(2.4, 2.4) in a
        True
        >>> Point(2.4, 2.5) in a
        False

        :param Point pt: the point to test
        :return: whether the point is on this line

    .. method:: intersect(l)

        Return the intersection point of this line and *l*.

        >>> a = Line(Point(0, 0), Point(1, 1))
        >>> b = Line(Point(2, 1), Point(3, 0))
        >>> a.intersect(b)
        Point(1.5, 1.5)

        :param Line l: the line to intersect with
        :raise ZeroDivisionError: if this line and *l* are parallel or concurrent
        :return: the intersection point
