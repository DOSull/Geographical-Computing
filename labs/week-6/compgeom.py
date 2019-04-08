# Computational geometry
#
# David O'Sullivan
# SGES, Auckland
# March 2005

# Updated to Python 3 March 2019

"""Module with Point, Line_segment, Vector, Polygon
and Bounding_box classes.  Supports simple computational
geometry operations."""

import math

class Point:
    """Simple 2D point with x and y coord"""
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def distance(self, p):
        """Distance to another point"""
        dx = p.x - self.x
        dy = p.y - self.y
        return math.sqrt(dx ** 2 + dy **2)

    def bounding_box(self):
        """Bounding box equivalent to point itself"""
        return Bounding_box(self.x, self.y, self.x, self.y)

    def __repr__(self):
        return "Point: %f %f" % (self.x, self.y)
        

class Line_segment:
    """Line segment defined by two Points"""
    def __init__(self, p1, p2):
        """Initialize from two Points"""
        self.p1 = p1
        self.p2 = p2

    def length(self):
        """Returns length of the line segment"""
        return self.p1.distance(self.p2)

    def dx(self):
        """Returns the x coord difference between end points"""
        return self.p2.x - self.p1.x

    def dy(self):
        """Returns the y coord difference between end points"""
        return self.p2.y - self.p1.y

    def side_value(self, p):
        """Returns a negative value if Point p is to the left
        of the line segment when moving from first point to the
        last point.  Returns a positive value if on the right
        side, and zero if collinear."""
        pA = Vector(self.p1.x - p.x, self.p1.y - p.y)
        pB = Vector(self.p2.x - p.x, self.p2.y - p.y)
        return pA.cross_product(pB)

    def is_collinear(self, p):
        """Returns True in Point p is collinear with the line segment"""
        return self.side_value(p) == 0

    def is_to_left(self, p):
        """Returns True if Point P lies in the left half-plane
        of this line segment"""
        return self.side_value(p) < 0

    def is_to_right(self, p):
        """Returns True if Point P lies in the right half-plane
        of this line segment"""
        return self.side_value(p) > 0

    def intersects(self, AB):
        """Returns true if Line_segment AB intersects this one"""
        A = AB.p1
        B = AB.p2
        v1 = self.side_value(A)
        v2 = self.side_value(B)
        v3 = AB.side_value(self.p1)
        v4 = AB.side_value(self.p2)
        return (v1 * v2) < 0 and (v3 * v4) < 0

    def touches(self, AB):
        """Returns True if Line_segment AB touches this one"""
        A = AB.p1
        B = AB.p2
        v1 = self.side_value(A)
        v2 = self.side_value(B)
        v3 = AB.side_value(self.p1)
        v4 = AB.side_value(self.p2)
        return (v1 * v2) == 0 or (v3 * v4) == 0

    def bounding_box(self):
        """Returns Bounding_box of this line segment"""
        bb = self.p1.bounding_box()
        bb.merge(self.p2.bounding_box())
        return bb

    def __repr__(self):
        return "Line_segment:\n\t%s\n\t%s" % (str(self.p1), str(self.p2))
        

class Vector:
    """Simple 2D vector"""
    dx = 0.0
    dy = 0.0

    def __init__(self, dx=0.0, dy=0.0):
        self.dx = float(dx)
        self.dy = float(dy)

    def cross_product(self, v2):
        """Returns the vector cross product self * v2"""
        return self.dx * v2.dy - self.dy * v2.dx

    def dot_product(self, v2):
        """Returns the vector cross product self * v2"""
        return self.dx * v2.dx + self.dy * v2.dy

    def length(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)

    def unit_vector(self):
        dx = self.dx / self.length()
        dy = self.dy / self.length()
        return Vector(dx, dy)

    def __repr__(self):
        return "Vector (%f, %f)" % (self.dx, self.dy)


class Polygon:
    """Simple one-part polygon stored as a list of Point objects.
    Closure of the polygon is implied, i.e. each point is only
    stored once."""
    points = []

    def __init__(self, pts):
        """Initialize from a list of Points"""
        self.points = list()
        for p in pts:
            self.points.append(p)

    def perimeter(self):
        """Returns the total perimeter of the polygon"""
        total = 0.0
        for i in range(len(self.points)):
            nextIndex = i + 1
            if nextIndex == len(self.points):
                nextIndex = 0
            total = total + self.points[i].distance(self.points[nextIndex])
        return total

    def area(self):
        """Returns total area of the polygon, calculated by the
        clockwise traversal trapezium method"""
        total = 0.0
        for i in range(len(self.points)):
            nextIndex = i + 1
            if nextIndex == len(self.points):
                nextIndex = 0
            xdiff = self.points[nextIndex].x - self.points[i].x
            ymean = 0.5 * (self.points[nextIndex].y + self.points[i].y)
            total = total + xdiff * ymean
        return total

    def bounding_box(self):
        """Returns a Bounding_box for this Polygon"""
        bb = self.points[0].bounding_box()
        for pt in self.points[1:]:
            bb.merge(pt.bounding_box())
        return bb

    def __repr__(self):
        s = "Polygon:\n"
        for i in range(len(self.points)):
            s = s + ("\t%s\n" % (str(self.points[i])))
        return s


class Bounding_box:
    """Bounding box recording min and max x and y coords for an object"""
    def __init__(self, min_x, min_y, max_x, max_y):
        """Initialize by explicit assignment of min x, min y, max x, max y"""
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def merge(self, bb):
        """Returns the result of merging this bounding box with
        another"""
        self.min_x = min([self.min_x, bb.min_x])
        self.min_y = min([self.min_y, bb.min_y])
        self.max_x = max([self.max_x, bb.max_x])
        self.max_y = max([self.max_y, bb.max_y])

    def contains(self, p):
        """Returns True if the supplied Point is inside this
        bounding box"""
        return self.min_x < p.x < self.max_x and \
               self.min_y < p.y < self.max_y

    def intersects(self, bb):
        """Returns True if this bounding box and the supplied
        bounding box bb intersect"""
        bb1 = Point(bb.min_x, bb.min_y)
        bb2 = Point(bb.min_x, bb.max_y)
        bb3 = Point(bb_max_x, bb.min_y)
        bb4 = Point(bb_max_x, bb.max_y)
        return self.contains(bb1) or self.contains(bb2) or \
               self.contains(bb3) or self.contains(bb4)

    def __repr__(self):
        return "Bounding box:\n\tW: %.2f\n\tS: %.2f\n\tE: %.2f\n\tN: %.2f\n" % (
            self.min_x, self.min_y, self.max_x, self.max_y)


# Some test cases

# A = Point(1,1)
# B = Point(1,4)
# C = Point(4,4)
# D = Point(4,1)
# AB = Line_segment(A, B)
# CD = Line_segment(C, D)
# ABCD = Polygon([A,B,C,D])
# print AB.length()
# print CD.length()

# print AB.intersects(CD)
# print AB.touches(CD)

# print ABCD.perimeter()
# print ABCD.area()

# print A.bounding_box()
# print AB.bounding_box()
# print ABCD.bounding_box()

print (__doc__)
