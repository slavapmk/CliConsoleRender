class Point3d:
    x: float
    y: float
    z: float

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vector3d:
    point: Point3d
    direction: Point3d

    def __init__(self, xo, yo, zo, xd, yd, zd):
        self.point = Point3d(xo, yo, zo)
        self.direction = Point3d(xd, yd, zd)


class Polygon3d:
    a: Point3d
    b: Point3d
    c: Point3d

    def __init__(self, a: Point3d, b: Point3d, c: Point3d):
        self.a = a
        self.b = b
        self.c = c


class Object3d:
    center: Point3d
    model: list[Polygon3d]


class Cube3d(Object3d):
    center: Point3d
    model: list[Polygon3d]

    def __init__(self, center: Point3d, edge: float):
        self.center = center
        self.model = [
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge, ),
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge, ),
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge, ),
                Point3d(0.5 * edge, 0.5 * edge, -0.5 * edge, )
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge, ),
            ),
            Polygon3d(
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge, ),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge, ),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge, )
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
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge, ),
                Point3d(-0.5 * edge, 0.5 * edge, 0.5 * edge, ),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge, )
            ),
            Polygon3d(
                Point3d(-0.5 * edge, 0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, 0.5 * edge, -0.5 * edge)
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge, ),
                Point3d(-0.5 * edge, -0.5 * edge, 0.5 * edge, ),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge, )
            ),
            Polygon3d(
                Point3d(-0.5 * edge, -0.5 * edge, -0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, 0.5 * edge),
                Point3d(0.5 * edge, -0.5 * edge, -0.5 * edge)
            )
        ]


class Camera(Object3d):
    center: Point3d
    model: list[Polygon3d] = []
    direction: Vector3d

    def __init__(self, center: Point3d, direction: Vector3d):
        self.center = center
        self.direction = direction
