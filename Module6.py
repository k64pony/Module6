class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return  "({0}, {1}, {2})"
        format(self.corner, self.width, self.height)

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)


class Point(object):
    """Represents a point"""

class Rectangle(object):
    """Represents a rectangle attributes: width, height, corner."""

def create_rectangle(x, y, width, height):
    pt = Point()
    pt.x = x
    pt.y = y
    r = Rectangle()
    r.width = width
    r.height = height
    r.corner = pt
    return r

def str_rectangle(rect):
    return "(%.3f, %.3f, %.3f, %.3f)" % (rect.corner.x, rect.corner.y,
                                         rect.width, rect.height)

def shift_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def offset_rectangle(rect, dx, dy):
    x = rect.corner.x + dx
    y = rect.corner.y + dy
    return create_rectangle(x, y, rect.width, rect.height)

r1 = create_rectangle(10, 20, 30, 40)
print (r1)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1))
print(str_rectangle(r2))



