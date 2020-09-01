class point:
    def __init__(self):
        self.y = 0
        self.x = 0

    def ref_x(self):
        new_x = self.x * - 1
        return point(new_x, self.y)
