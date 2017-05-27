Python wrapper for blender 3D software API.

## Usage

```python
from blender_wrapper.scene import Scene
from blender_wrapper.camera import Camera
from blender_wrapper.lamp import SunLamp
from blender_wrapper.variables import ORIGIN


def main():
    scene = Scene(filepath="~/Desktop/")
    scene.setup()

    camera = Camera((0, 0, 1.5), (30, 0, 0), view_align=True)
    camera.add_to_scene()

    lamp = SunLamp(10, (0, 0, 3), ORIGIN)
    lamp.add_to_scene()

    scene.render()


# Execute running:
#   blender --background -P ./test.py
if __name__ == "__main__":
    main()
```
