def if_collision(self, rect2):
    collision = abs(self.corner.x - rect2.corner.x) < max(self.width, rect2.width) and \
           abs(self.corner.y - rect2.corner.y) < max(self.height, rect2.height)
    return collision
