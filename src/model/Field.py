from graphics import Rectangle, Point


class Field(Rectangle):
    def __init__(self, p1: Point, p2: Point, base_x: int, base_y):
        super().__init__(p1, p2)
        self.baseX = base_x
        self.baseY = base_y
        self.heuristic = 0
        self.p = -1
        self.is_wall = False
