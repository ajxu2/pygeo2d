.. pygeo2d documentation master file, created by
   sphinx-quickstart on Thu Mar 23 01:28:42 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pygeo2d's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   point
   line
   circle
   utility
   example


pygeo2d is, as the name suggests, a library for **2-d**\imensional **geo**\metry in **Py**\thon.

Features include:
   - Points (really vectors, implemented as the ``Point`` class)
   - Vector addition and subtraction
   - Distances between points
   - Lines (implemented as the ``Line`` class)
   - Intersections of lines
   - Circles (implemented as the ``Circle`` class)
   - Intersections between circles and lines
   - Basic constructions, including midpoint, perpendicular bisector, etc. (todo)
   - Triangle constructions: circumcenter, circumcircle, incenter, incircle, etc. (todo)

Example usage:

>>> from pygeo2d import * # "kitchen sink" usage
>>> A = Point(2, 3)
>>> B = Point(4, 5)
>>> print(B - A)
(2, 2)
>>> l = Line(A, B)
>>> print(l)
(-2x) + (2y) + (-2) = 0
>>> intersect(l, Line(Point(0, 0), Point(1, -1)))
Point(-0.5, 0.5)
>>> c = Circle(Point(0, 0), 5)
>>> intersect(c, l)
[Point(3.0, 4.0), Point(-4.0, -3.0)]

Installation
============

Installation is easy with `pip <https://pypi.org/project/pip/>`_::

   $ pip install -i https://test.pypi.org/simple/ pygeo2d
