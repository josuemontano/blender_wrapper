from blender_wrapper.api import Scene
from blender_wrapper.api import Camera
from blender_wrapper.api import SunLamp
from blender_wrapper.api import ORIGIN


def main():
    scene = Scene(1500, 1000, filepath="~/Desktop/")
    scene.setup()

    camera = Camera((1, 0, 1), (90, 0, 0), view_align=True)
    camera.add_to_scene()

    lamp = SunLamp(10, (0, 0, 3), ORIGIN)
    lamp.add_to_scene()

    scene.render(resolution_percentage=100)


# Execute running:
#   blender --background -P ./test.py
if __name__ == "__main__":
    main()
