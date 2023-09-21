import random
import shutil
import time

import config
from config import MAX_FPS
from screen import Screen

all_fps = []
while True:
    (width, height) = shutil.get_terminal_size()
    screen = Screen(width - 1, height)

    startRenderTime = time.time()
    screen.fill(
        -1, -1,
        1, 1,
        0.1
    )
    screen.fill(
        -0.3, -0.3,
        0.3, 0.3,
        random.randrange(30, 80) / 100
    )
    screen.fill(
        -0.29, -0.29,
        -0.31, -0.31,
        0.9
    )
    screen.fill(
        -0.01, -0.29,
        0.01, -0.31,
        0.9
    )
    screen.fill(
        -0.29, -0.01,
        -0.31, 0.01,
        0.9
    )
    render = screen.render()

    renderDuration = time.time() - startRenderTime
    if config.MAX_FPS > 0:
        delayTime = (1 / MAX_FPS) - renderDuration
        if delayTime > 0:
            time.sleep(delayTime)

    if config.SHOW_FPS:
        fps = round(1 / (time.time() - startRenderTime))
        all_fps.append(fps)
        if len(all_fps) > 30:
            all_fps.pop(0)
        average_fps = f' FPS: {round(sum(all_fps) / len(all_fps))} '
        render = average_fps + render[len(average_fps):]

    print('\n' + render, end='')
