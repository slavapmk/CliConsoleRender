import numpy as np


class Screen:
    matrix = [[1.0]]
    width: int = 0
    height: int = 0

    def __init__(self, width: int, height: int):
        self.matrix = np.zeros(shape=(height, width))
        self.width = width
        self.height = round(height / 2.57)

    gradient: str = 'ÆÑÊŒØMÉËÈÃÂWQBÅæ#NÁþEÄÀHKRŽœXgÐêqÛŠÕÔA€ßpmãâG¶øðé8ÚÜ$ëdÙýèÓÞÖåÿÒb¥FDñáZPäšÇàhû§ÝkŸ®S9žUTe6µOyxÎ¾f4õ5ôú&aü™2ùçw©Y£0VÍL±3ÏÌóC@nöòs¢u‰½¼‡zJƒ%¤Itocîrjv1lí=ïì<>i7†[¿?×}*{+()\/»«•¬|!¡÷¦¯—^ª„”“~³º²–°¹‹›;:’‘‚’˜ˆ¸…·¨´` '

    def parse_pixel(self, pixel: float):
        return self.gradient[round((len(self.gradient) - 1) * (1 - pixel))]

    def set_pixel(self, x: float, y: float, value: float):
        self.matrix[round((x + 1) / 2 * (self.width - 1))][round((y + 1) / 2 * (self.height - 1))] = value

    def fill(self, x_start: float, y_start: float, x_stop: float, y_stop: float, value: float):
        start_screen_x = round((x_start + 1) / 2 * (self.width - 1))
        start_screen_y = round((y_start + 1) / 2 * (self.height - 1))
        stop_screen_x = round((x_stop + 1) / 2 * (self.width - 1))
        stop_screen_y = round((y_stop + 1) / 2 * (self.height - 1))
        for screen_x in range(start_screen_x, stop_screen_x + 1):
            for screen_y in range(start_screen_y, stop_screen_y + 1):
                self.matrix[screen_x][screen_y] = value

    def render(self):
        canvas = ''
        for y in range(self.height):
            for x in range(self.width):
                canvas += self.parse_pixel(self.matrix[x][y])
            canvas += '\n'
        print(canvas)


screen = Screen(51, 51)
screen.fill(
    -1, -1,
    1, 1,
    0.01
)
screen.set_pixel(0, 0, 0.4)
screen.set_pixel(-1, -1, 0.4)
screen.set_pixel(1, 1, 0.4)
screen.set_pixel(-1, 1, 0.4)
screen.set_pixel(1, -1, 0.4)
screen.set_pixel(0, -1, 0.4)
screen.set_pixel(0, 1, 0.4)
screen.set_pixel(1, 0, 0.4)
screen.set_pixel(-1, 0, 0.4)
screen.render()
