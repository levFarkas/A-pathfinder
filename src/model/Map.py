from typing import List

from graphics import *

from src.model.Field import Field


class Map:
    def __init__(self, width, height, astar):
        self.destination: Field = None
        self.source: Field = None
        assert width == height
        self.width = width
        self.AStar = astar
        self.area_size = 25
        self.area_count = width // self.area_size
        self.map = [
            [
                Field(
                    Point(i * self.area_size, j * self.area_size),
                    Point(i * self.area_size + self.area_size, j * self.area_size + self.area_size),
                    i,
                    j
                )
                for i in range(self.area_count)
            ]
            for j in range(self.area_count)
        ]

    def draw(self, win):
        for row in self.map:
            for rect in row:
                rect.draw(win)

    @staticmethod
    def _color_field(rect: Field, color: str):
        rect.setFill(color)

    def _get_field_by_point(self, point: Point) -> Field:
        return self.map[
            int(point.getY() // self.area_size)
        ][
            int(point.getX() // self.area_size)
        ]

    def handle_point(self, point: Point):
        field = self._get_field_by_point(point)

        if not self.source:
            self.source = field
            self._color_field(field, "green")
            return
        if not self.destination:
            self.destination = field
            self._color_field(field, "green")
            self.AStar.calculate_heuristics(self)
            return

        if field != self.source and field != self.destination:
            self._color_field(field, "black")
            field.is_wall = True

    def get_neighbours(self, field: Field) -> List[Field]:
        fields = []
        if field.baseY > 0:
            fields.append(self.map[field.baseY - 1][field.baseX])
        if field.baseY < self.width // self.area_size - 1:
            fields.append(self.map[field.baseY + 1][field.baseX])
        if field.baseX > 0:
            fields.append(self.map[field.baseY][field.baseX - 1])
        if field.baseX < self.width // self.area_size - 1:
            fields.append(self.map[field.baseY][field.baseX + 1])
        if field.baseX < self.width // self.area_size - 1 and field.baseY < self.width // self.area_size - 1:
            fields.append(self.map[field.baseY + 1][field.baseX + 1])
        if field.baseY > 0.and field.baseX < self.width // self.area_size - 1:
            fields.append(self.map[field.baseY - 1][field.baseX + 1])
        if field.baseY < self.width // self.area_size - 1 and field.baseX > 0:
            fields.append(self.map[field.baseY + 1][field.baseX - 1])
        if field.baseX > 0 and field.baseY > 0:
            fields.append(self.map[field.baseY - 1][field.baseX - 1])
        return fields
