"""
Utility functions to be used in place of instance methods.
"""

def dist(obj1, obj2):
    try:
        return obj1.dist(obj2)
    except:
        pass
    try:
        return obj2.dist(obj1)
    except:
        raise TypeError("Unable to get distance between objects")

def intersect(obj1, obj2):
    try:
        return obj1.intersect(obj2)
    except:
        pass
    try:
        return obj2.intersect(obj1)
    except:
        raise TypeError("Unable to calculate intersection point between objects")

def dot(p1, p2):
    try:
        return p1.dot(p2)
    except:
        raise TypeError("Unable to calculate dot product")

def cross(p1, p2):
    try:
        return p1.cross(p2)
    except:
        raise TypeError("Unable to calculate cross product")
