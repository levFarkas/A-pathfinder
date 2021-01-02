import time
from math import sqrt

from src.model.Map import Map


class AStar:
    @staticmethod
    def calculate_heuristics(m: Map):
        for row in m.map:
            for field in row:
                field.heuristic = sqrt(
                    pow(field.baseX - m.destination.baseX, 2) + pow(field.baseY - m.destination.baseY, 2))

    @staticmethod
    def run(m: Map):
        came_from_dict = {}
        current = m.source
        current.p = 0
        map_size = m.width * m.width
        investigated = []
        visited = []
        while current.heuristic != 0 or len(investigated) >= map_size:
            visited.append(current)
            for field in m.get_neighbours(current):
                if field not in investigated:
                    came_from_dict[field] = current
                    investigated.append(field)
                    if field.p == -1:
                        field.p = current.p + 1
            min_f = 100000
            min_field = None
            for field in investigated:
                if field.is_wall or field in visited:
                    continue
                f = field.p + field.heuristic
                if f <= min_f:
                    min_f = f
                    min_field = field
            current = min_field
            if current != m.destination:
                current.setFill("grey")
            time.sleep(0.1)
        search_for_source = current
        while search_for_source != m.source:
            search_for_source = came_from_dict[search_for_source]
            search_for_source.setFill("green")
            time.sleep(0.1)
