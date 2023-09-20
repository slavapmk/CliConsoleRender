import json
from typing import List


class Screen:
    matrix: List[List[float]]
    width: int = 0
    height: int = 0

    def __init__(self, width: int, height: int):
        self.matrix = [[0] * width] * height
        self.width = width
        self.height = height

    def render(self):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                

        print(json.dumps(self.matrix))


Screen(20, 100).render()
