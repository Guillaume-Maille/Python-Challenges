class point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def ref_x(self):
        new_x = self.x * - 1
        return point(new_x, self.y)

    def slope(self):
        slope = self.y/self.x
        return slope

    def get_line(self, target):
        m = (target.y-self.y)/(target.x-self.x)
        c = self.y - m*self.x
        return point(m, c)
