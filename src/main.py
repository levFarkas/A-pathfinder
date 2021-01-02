from graphics import *

from src.algorithm.AStar import AStar
from src.model.Map import Map


class Handler:

    def __init__(self):
        self.width = 500
        self.height = 500
        self.button_area = 200
        self.AStar = AStar
        self.win = GraphWin("A star algorithm", self.width, self.height + self.button_area)
        self.win.bind('<B1-Motion>', self.handle_event)
        self.m = Map(self.width, self.height, self.AStar)

    @staticmethod
    def does_contain(left_up_corner, right_bottom_corner, point) -> bool:
        if left_up_corner.getX() < point.x < right_bottom_corner.getX() and \
                left_up_corner.getY() < point.y < right_bottom_corner.getY():
            return True
        return False

    def handle(self):
        self.m.draw(self.win)
        button = Rectangle(Point(self.width / 2 - 50, self.height + self.button_area / 2 - 20),
                           Point(self.width / 2 + 50, self.height + self.button_area / 2 + 20))
        text = Text(Point(self.width / 2, self.height + self.button_area / 2), "Start")
        text.draw(self.win)

        button.draw(self.win)
        mouse_point = self.win.getMouse()
        while not self.does_contain(button.getP1(), button.getP2(), mouse_point):
            if self.does_contain(Point(0, 0), Point(self.width, self.height), mouse_point):
                self.map_handle_point(mouse_point)
            mouse_point = self.win.getMouse()

        self.AStar.run(self.m)
        self.win.getMouse()
        self.win.close()

    def handle_event(self, event):
        self.map_handle_point(Point(event.x, event.y))

    def map_handle_point(self, point: Point):
        self.m.handle_point(point)


if __name__ == '__main__':
    handler = Handler()
    handler.handle()
