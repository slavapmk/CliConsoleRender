from render import Renderable3d, Point3d, Rotation3d, Polygon3d
import re

pattern = re.compile(r'v\d')


class ObjModel(Renderable3d):
    def __init__(self, file: str, position: Point3d, rotation: Rotation3d = None):
        points: dict[str, Point3d] = {}
        model: list[Polygon3d] = []
        with open(file, 'r') as obj:
            for line in obj.readlines():
                split = line.split(' ')
                if split[0] == 'v':
                    points[f"v{len(points) + 1}"] = Point3d(split[1], split[2], split[3])
                elif split[1] == 'f':
                    points_names = []
                    for e in split[1:]:
                        points_names.append(
                            str(list(map(lambda point: pattern.match(point), e.split('/')))[0])
                        )
                    model.append(Polygon3d(
                        points[points_names[0]],
                        points[points_names[1]],
                        points[points_names[2]]
                    ))
        super().__init__(
            position,
            Rotation3d(0, 0, 0) if rotation is None else rotation,
            model
        )
