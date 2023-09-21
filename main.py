import random
import shutil
import time

from config import MAX_FPS
from screen import Screen

all_fps = []

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
        random.randrange(30, 80) / 100
    )
    screen.set_pixel(-0.3, -0.3, 0.4)
    screen.set_pixel(0.3, 0.3, 0.4)
    screen.set_pixel(-0.3, 0.3, 0.4)
    screen.set_pixel(0.3, -0.3, 0.4)
    screen.set_pixel(0, -0.3, 0.4)
    screen.set_pixel(0, 0.3, 0.4)
    screen.set_pixel(0.3, 0, 0.4)
    screen.set_pixel(-0.3, 0, 0.4)
    render = screen.render()

    renderDuration = time.time() - startRenderTime
    if MAX_FPS > 0:
        time_ = (1 / MAX_FPS) - renderDuration
        if time_ > 0:
            time.sleep(time_)

    fps = round(1 / (time.time() - startRenderTime))
    all_fps.append(fps)
    if len(all_fps) > 50:
        all_fps.pop(0)

    average_fps = str(round(sum(all_fps) / len(all_fps)))

    render = '\n' + average_fps + ' ' + render[len(average_fps) + 1:]

    print(render, end='')
