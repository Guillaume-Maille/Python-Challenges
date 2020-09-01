class point:

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, posn, w, h):
        self.height = h
        self.corner = posn
        self.width = w

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height
