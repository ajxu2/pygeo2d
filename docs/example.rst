Example
=======

Let's test `Ceva's theorem <https://en.wikipedia.org/wiki/Ceva%27s_theorem>`_, a well-known result in geometry that is known to be correct.

First, we can make a function that does one test of Ceva's using random points:

.. code-block:: python

    from pygeo2d import *
    from random import uniform
    from math import isclose

    def test_ceva():
        # First, select 3 random points as our triangle.
        A = Point(uniform(-10, 10), uniform(-10, 10))
        B = Point(uniform(-10, 10), uniform(-10, 10))
        C = Point(uniform(-10, 10), uniform(-10, 10))

        # Next, select a random point which the three lines will concur at.
        P = Point(uniform(-10, 10), uniform(-10, 10))

        # Draw the cevians.
        a = Line(A, P)
        b = Line(B, P)
        c = Line(C, P)

        # Intersect cevians with sides of triangle.
        D = intersect(a, Line(B, C))
        E = intersect(b, Line(A, C))
        F = intersect(c, Line(A, B))

        # Check Ceva's!
        # If Ceva's Theorem is true (which it is), the following should always be True.
        return dist(A,F)/dist(F,B)*dist(B,D)/dist(D,C)*dist(C,E)/dist(E,A) == 1

Now, let's just run that function some large number of times:

.. code-block:: python

    num_correct = 0
    num_tests = 10000
    for i in range(num_tests):
        if test_ceva():
            num_correct += 1

    print(f"{num_correct} out of {num_tests} matched the expected outcome")

and as expected...

.. code-block::

    10000 out of 100000 matched the expected outcome

As you can see, Ceva's theorem does seem to be true! (Alternatively, if you look at it from the perspective of a geometer, these tests have told us that pygeo2d is unlikely to be flawed.)
