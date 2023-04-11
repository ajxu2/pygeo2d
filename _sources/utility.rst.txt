Utility functions
=================

These are functions that would normally be called via instance methods.
They have been converted into functions to preserve the elegance of symmetry.

.. function:: dist(a, b)

    Returns the Euclidean distance between *a* and *b*.
    Equivalent to either ``a.dist(b)`` or ``b.dist(a)``.

    :param a: the first object
    :param b: the second object
    :return: the Euclidean distance between the objects

.. function:: intersect(a, b)

    Returns the intersection of *a* and *b*.
    Equivalent to either ``a.intersect(b)`` or ``b.intersect(a)``.

    :param a: the first object
    :param b: the second object
    :return: the intersection of the two objects

.. function:: dot(a, b)

    Returns the dot product of *a* and *b*.
    Equivalent to ``a.dot(b)``.

    :param a: the first object
    :param b: the second object
    :return: the dot product of the two objects

.. function:: cross(a, b)

    Returns the cross product of *a* and *b*.
    Equivalent to ``a.cross(b)``.

    :param a: the first object
    :param b: the second object
    :return: the magnitude of the cross product of the two objects
