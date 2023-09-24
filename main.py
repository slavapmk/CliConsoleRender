import shutil
import time

import config
from config import MAX_FPS
from object3d import Cube3d, Point3d, Scene, Camera, Rotation3d


def resize_matrix(to_resize, new_height, new_width):
    original_height, original_width = len(to_resize), len(to_resize[0])
    resized_matrix = [[0.0] * new_width for _ in range(new_height)]
    for i in range(new_height):
        for j in range(new_width):
            x = int((i * (original_height - 1)) / (new_height - 1))
            y = int((j * (original_width - 1)) / (new_width - 1))
            a = (i * (original_height - 1)) / (new_height - 1) - x
            b = (j * (original_width - 1)) / (new_width - 1) - y
            resized_matrix[i][j] = (1 - a) * (1 - b) * to_resize[x][y]
            resized_matrix[i][j] += a * (1 - b) * to_resize[x + 1][y] if x + 1 < original_height else 0.0
            resized_matrix[i][j] += (1 - a) * b * to_resize[x][y + 1] if y + 1 < original_width else 0.0
            resized_matrix[i][j] += a * b * to_resize[x + 1][
                y + 1] if x + 1 < original_height and y + 1 < original_width else 0.0
    return resized_matrix


def parse_pixel(pixel: float):
    return config.GRADIENT[round((len(config.GRADIENT) - 1) * (1 - pixel))]


def process_scene(ticks: float, scene: Scene):
    scene.objects[0].rotate(Rotation3d(
        ticks, ticks, ticks
    ))


def run():
    last_fps_values = []

    d = Cube3d(Point3d(0, 3, 0), 1)
    game_scene = Scene(
        Camera(
            Point3d(0, 0, 0),
            Rotation3d(0, 0, 0)
        ),
        d
    )

    width, height = shutil.get_terminal_size()
    width -= 1

    last_render_time = time.time() - 0.1

    while True:
        start_render_time = time.time()
        from_last_frame = start_render_time - last_render_time
        last_render_time = start_render_time

        scene_render = game_scene.render(
            round(width / config.render_coefficient_axis),
            round(height / config.height_ratio / config.render_coefficient_axis)
        )
        process_scene(from_last_frame * 20, game_scene)
        matrix = resize_matrix(scene_render, height, width)
        h = []
        for y in range(len(matrix)):
            row = []
            for x in range(len(matrix[0])):
                row.append(parse_pixel(matrix[y][x]))
            h.append(''.join(row))
        render = '\n'.join(h)

        render_duration = time.time() - start_render_time
        if config.MAX_FPS > 0:
            delay_time = (1 / MAX_FPS) - render_duration
            if delay_time > 0:
                time.sleep(delay_time)

        if config.SHOW_FPS:
            elapsed_time = (time.time() - start_render_time)
            if elapsed_time != 0:
                fps = round(1 / elapsed_time)
                last_fps_values.append(fps)
                if len(last_fps_values) > 30:
                    last_fps_values.pop(0)
                average_fps = f' FPS: {round(sum(last_fps_values) / len(last_fps_values))} '
                render = average_fps + render[len(average_fps):]

        print('\n' + render, end='')


if __name__ == '__main__':
    run()
