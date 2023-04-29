class Volume:
    def __init__(self, height: int) -> int:
        self.height = height

    def cuboid(self, width: int, length: int) -> float:
        out = self.height * width * length
        return float(out)

    def cube(self) -> float:
        out = self.height * self.height * self.height
        return float(out)

    def cylinder(self, radius: int) -> float:
        out = radius * radius * 3.14 * self.height
        return out

    def cone(self, radius: int) -> float:
        out = radius * radius * 3.14 * self.height / 3
        return out
