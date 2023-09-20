import json
from typing import List


class Screen:
    matrix: List[List[float]]

    def __init__(self, width: int, height: int):
        self.matrix = [[0] * width] * height

    def render(self):
        print(json.dumps(self.matrix))


Screen(20, 100).render()
