import numpy as np

from config import HEIGHT_RATIO


class Screen:
    matrix = [[1.0]]
    width: int = 0
    height: int = 0

    def __init__(self, width: int, height: int):
        self.matrix = np.zeros(shape=(width, height))
        self.width = width
        self.height = height

    gradient: str = 'ÆÑÊŒØMÉËÈÃÂWQBÅæ#NÁþEÄÀHKRŽœXgÐêqÛŠÕÔA€ßpmãâG¶øðé8ÚÜ$ëdÙýèÓÞÖåÿÒb¥FDñáZPäšÇàhû§ÝkŸ®S9žUTe6µOyxÎ¾f4õ5ôú&aü™2ùçw©Y£0VÍL±3ÏÌóC@nöòs¢u‰½¼‡zJƒ%¤Itocîrjv1lí=ïì<>i7†[¿?×}*{+()\/»«•¬|!¡÷¦¯—^ª„”“~³º²–°¹‹›;:’‘‚’˜ˆ¸…·¨´` '

    def parse_pixel(self, pixel: float):
        return self.gradient[round((len(self.gradient) - 1) * (1 - pixel))]

    def set_pixel(self, x: float, y: float, value: float):
        self.matrix[round((x + 1) / 2 * (self.width - 1))][round((y * HEIGHT_RATIO + 1) / 2 * (self.height - 1))] = value

    def fill(self, x_start: float, y_start: float, x_stop: float, y_stop: float, value: float):
        start_screen_x = round((x_start + 1) / 2 * (self.width - 1))
        start_screen_y = round((y_start * HEIGHT_RATIO + 1) / 2 * (self.height - 1))
        stop_screen_x = round((x_stop + 1) / 2 * (self.width - 1))
        stop_screen_y = round((y_stop * HEIGHT_RATIO + 1) / 2 * (self.height - 1))
        for screen_x in range(min(start_screen_x, stop_screen_x), max(start_screen_x, stop_screen_x) + 1):
            for screen_y in range(min(start_screen_y, stop_screen_y), max(start_screen_y, stop_screen_y) + 1):
                if 0 < screen_x < self.width and 0 < screen_y < self.height:
                    self.matrix[screen_x][screen_y] = value

    def render(self):
        canvas = '\n'
        for y in range(self.height):
            for x in range(self.width):
                canvas += self.parse_pixel(self.matrix[x][y])
            canvas += '\n'
        print(canvas, end='')
