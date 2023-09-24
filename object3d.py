from functools import reduce
from math import sin, cos, radians

import config


class Point3d:
    x: float
    y: float
    z: float

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def rotate(self, rotation: 'Rotation3d', rotation_axis: 'Point3d') -> 'Point3d':
        rads = list(map(radians, [rotation.x_axis, 0, rotation.z_axis]))
        if rotation_axis == (0, 0, 0):
            rotation_axis = Point3d(0, 0, 0)
        x = self.x - rotation_axis.x
        y = self.y - rotation_axis.y
        z = self.z - rotation_axis.z
        new_x = (
                        x * cos(rads[1]) * cos(rads[2])
                        - y * sin(rads[2]) * cos(rads[1])
                        + z * sin(rads[1])
                ) + rotation_axis.x
        new_y = (
                        x * (sin(rads[0]) * sin(rads[1]) * cos(rads[2]) + sin(rads[2]) * cos(rads[0]))
                        + y * (- sin(rads[0]) * sin(rads[1]) * sin(rads[2]) + cos(rads[0]) * cos(rads[2]))
                        + z * (-sin(rads[0]) * cos(rads[1]))
                ) + rotation_axis.y
        new_z = (
                        x * (sin(rads[0]) * sin(rads[2]) - sin(rads[1]) * cos(rads[0]) * cos(rads[2]))
                        + y * (sin(rads[0]) * cos(rads[2]) + sin(rads[1]) * sin(rads[2]) * cos(rads[0]))
                        + z * cos(rads[0]) * cos(rads[1])
                ) + rotation_axis.z
        return Point3d(new_x, new_y, new_z)

    def add(self, addition: 'Point3d'):
        return Point3d(
            self.x + addition.x,
            self.y + addition.y,
            self.z + addition.z
        )


class Rotation3d:
    x_axis: float
    z_axis: float

    def __init__(self, x_axis, z_axis):
        self.x_axis = x_axis
        self.z_axis = z_axis

    def __str__(self):
        return f'({self.x_axis},{self.z_axis})'


class Direction3d:
    x: float
    y: float
    z: float

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def rotate(self, rotation: Rotation3d) -> 'Direction3d':
        rotate = Point3d(self.x, self.y, self.z).rotate(rotation, Point3d(0, 0, 0))
        return Direction3d(rotate.x, rotate.y, rotate.z)


class Vector3d:
    point: Point3d
    direction: Direction3d
    length: int

    def __init__(self, point: Point3d, direction: Direction3d, length: int):
        self.point = point
        self.direction = direction
        self.length = length


class Polygon3d:
    a: Point3d
    b: Point3d
    c: Point3d

    def __init__(self, a: Point3d, b: Point3d, c: Point3d):
        self.a = a
        self.b = b
        self.c = c


class Object3d:
    position: Point3d
    model: list[Polygon3d]
    rotation: Rotation3d

    def final_state(self) -> list[Polygon3d]:
        out = []
        for polygon in self.model:
            out.append(Polygon3d(
                polygon.a.rotate(self.rotation, Point3d(0, 0, 0)).add(self.position),
                polygon.b.rotate(self.rotation, Point3d(0, 0, 0)).add(self.position),
                polygon.c.rotate(self.rotation, Point3d(0, 0, 0)).add(self.position)
            ))
        return out

    def rotate(self, rotation: Rotation3d):
        self.rotation.x_axis = (self.rotation.x_axis + rotation.x_axis) % 360
        self.rotation.z_axis = (self.rotation.z_axis + rotation.z_axis) % 360


class Cube3d(Object3d):
    position: Point3d
    model: list[Polygon3d]
    rotation: Rotation3d

    def __init__(self, position: Point3d, edge: float, rotation=Rotation3d(0, 0)):
        self.position = position
        self.rotation = rotation
        self.model = [
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge),
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, -0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge),
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge)
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge)
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, -0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, -0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge)
            )
        ]


class Camera(Object3d):
    position: Point3d
    model: list[Polygon3d] = []
    rotation: Rotation3d
    fov: int = config.FOV

    def __init__(self, position: Point3d, direction: Rotation3d):
        self.position = position
        self.rotation = direction


class Scene:
    objects: list[Object3d] = []
    camera: Camera

    def __init__(self, camera: Camera, *objects: Object3d):
        self.camera = camera
        self.objects = list(objects)

    def render(self, width: int, height: int):
        density: int = max(width, height)
        polygons = [
            Polygon3d(
                Point3d(-1, 15, -1),
                Point3d(1, 15, -1),
                Point3d(0, 15, 1)
            )
        ]
        if len(self.objects) != 0:
            polygons = reduce(lambda a, b: a + b, map(lambda x: x.final_state(), self.objects))
        output = []
        for yp in range(height):
            row = []
            for xp in range(width):
                x_degrees = (xp - (width - 1) / 2) / (density - 1) * self.camera.fov
                y_degrees = (yp - (height - 1) / 2) / (density - 1) * self.camera.fov

                direction = Direction3d(0, 1, 0).rotate(Rotation3d(
                    -(self.camera.rotation.x_axis + y_degrees),
                    -(self.camera.rotation.z_axis + x_degrees),
                ))
                a = 0
                for polygon in polygons:
                    intersection = intersect_triangle(
                        polygon,
                        self.camera.position,
                        direction
                    )
                    if intersection is not None:
                        a = 1
                        break
                row.append(a)
            output.append(row)
        return output


def scalar_intersect(edge, intersect, polygon_point: Point3d):
    return (edge[1] * (intersect.z - polygon_point.z) - edge[2] * (intersect.y - polygon_point.y),
            edge[2] * (intersect.x - polygon_point.x) - edge[0] * (intersect.z - polygon_point.z),
            edge[0] * (intersect.y - polygon_point.y) - edge[1] * (intersect.x - polygon_point.x))


def intersect_triangle(polygon: Polygon3d, ray_origin: Point3d, ray_direction: Direction3d):
    normal = (
        (polygon.b.y - polygon.a.y) * (polygon.c.z - polygon.a.z)
        - (polygon.c.y - polygon.a.y) * (polygon.b.z - polygon.a.z),
        (polygon.b.z - polygon.a.z) * (polygon.c.x - polygon.a.x)
        - (polygon.c.z - polygon.a.z) * (polygon.b.x - polygon.a.x),
        (polygon.b.x - polygon.a.x) * (polygon.c.y - polygon.a.y)
        - (polygon.c.x - polygon.a.x) * (polygon.b.y - polygon.a.y)
    )

    dot_product = normal[0] * ray_direction.x + normal[1] * ray_direction.y + normal[2] * ray_direction.z
    if abs(dot_product) < 1e-6:
        return None

    d = normal[0] * polygon.a.x + normal[1] * polygon.a.y + normal[2] * polygon.a.z
    t = (d - normal[0] * ray_origin.x - normal[1] * ray_origin.y - normal[2] * ray_origin.z) / dot_product

    if t < 0:
        return None

    x = ray_origin.x + ray_direction.x * t
    y = ray_origin.y + ray_direction.y * t
    z = ray_origin.z + ray_direction.z * t
    intersect = Point3d(x, y, z)

    edge0 = (polygon.b.x - polygon.a.x, polygon.b.y - polygon.a.y, polygon.b.z - polygon.a.z)
    edge1 = (polygon.c.x - polygon.b.x, polygon.c.y - polygon.b.y, polygon.c.z - polygon.b.z)
    edge2 = (polygon.a.x - polygon.c.x, polygon.a.y - polygon.c.y, polygon.a.z - polygon.c.z)

    cp0 = scalar_intersect(edge0, intersect, polygon.a)
    cp1 = scalar_intersect(edge1, intersect, polygon.b)
    cp2 = scalar_intersect(edge2, intersect, polygon.c)

    if (cp0[0] * normal[0] + cp0[1] * normal[1] + cp0[2] * normal[2] >= 0 and
            cp1[0] * normal[0] + cp1[1] * normal[1] + cp1[2] * normal[2] >= 0 and
            cp2[0] * normal[0] + cp2[1] * normal[1] + cp2[2] * normal[2] >= 0):
        return intersect
    else:
        return None
