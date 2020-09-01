import math


class point:
    def __init__(self):
        self.y = 0
        self.x = 0


def distance(p1, p2):
    return math.sqrt((p2.y-p1.y)**2 + (p2.x-p1.x)**2)