from blender_wrapper.api import Scene
from blender_wrapper.api import Camera
from blender_wrapper.api import SunLamp
from blender_wrapper.api import Cone, Cube, Cylinder, Monkey, Plane

from blender_wrapper.api.constants import ORIGIN, SUBSURFz


def main():
    scene = Scene(1500, 1000, filepath="./")
    scene.setup()

    camera = Camera((1, 0, 1), (90, 0, 0), view_align=True)
    camera.add_to_current_scene()

    lamp = SunLamp(10, (0, 0, 3), ORIGIN)
    lamp.add_to_current_scene()

    floor = Plane(ORIGIN, ORIGIN, radius=5.0)
    floor.add_to_current_scene()

    cube = Cube((2.5, 2.5, 0), (0, 0, 45))
    cube.add_to_current_scene()

    monkey = Monkey((0, 0, 1.25), (10, 0, 45), radius=1.25)
    monkey.add_to_current_scene()
    monkey.add_modifier(SUBSURF)
    monkey.shade_smooth()

    scene.render(samples=75, resolution_percentage=5)
    scene.export_to_blend_file('./scene.blend')


# Execute running:
#   blender --background -P ./test.py
if __name__ == "__main__":
    main()
