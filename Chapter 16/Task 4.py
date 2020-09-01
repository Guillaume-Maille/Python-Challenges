def contains(self, point):
    if 0 <= point.x - self.corner.x < self.width and 0 <= point.y - self.corner.y < self.height:
        return True
    else:
        return False
