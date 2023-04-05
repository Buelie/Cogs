class Volume:
    def __init__(self, height: int):
        self.height = height

    def cuboid(self, width: int, length: int):
        out = self.height * width * length
        return out

    def cube(self):
        out = self.height * self.height * self.height
        return out

    def cylinder(self, radius: int):
        out = radius * radius * 3.14 * self.height
        return out
