import shutil
import time

from config import MAX_FPS
from screen import Screen

while True:
    (width, height) = shutil.get_terminal_size()
    screen = Screen(width - 1, height - 1)

    startRenderTime = time.time()
    screen.fill(
        -1, -1,
        1, 1,
        0.01
    )
    screen.fill(
        -0.1, -0.1,
        0.1, 0.1,
        0.7
    )
    # screen.set_pixel(0, 0, 0.4)
    # screen.set_pixel(-1, -1, 0.4)
    # screen.set_pixel(1, 1, 0.4)
    # screen.set_pixel(-1, 1, 0.4)
    # screen.set_pixel(1, -1, 0.4)
    # screen.set_pixel(0, -1, 0.4)
    # screen.set_pixel(0, 1, 0.4)
    # screen.set_pixel(1, 0, 0.4)
    # screen.set_pixel(-1, 0, 0.4)
    screen.render()

    renderDuration = time.time() - startRenderTime
    time_ = (1 / MAX_FPS) - renderDuration
    if time_ > 0:
        time.sleep(time_)
