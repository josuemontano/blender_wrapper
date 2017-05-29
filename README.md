Python wrapper for blender 3D software API.

## Installation

Clone this repo and make it available to blender's python interpreter. You can do it by creating a symbolic link, e.g.:

```sh
git clone git@github.com:josuemontano/blender_wrapper.git
ln -s $PWD/blender_wrapper /Applications/blender.app/Contents/Resources/2.78/python/lib/python3.5/site-packages
```

## Usage

```python
from blender_wrapper.api import Scene
from blender_wrapper.api import Camera
from blender_wrapper.api import SunLamp
from blender_wrapper.api.constants import ORIGIN, SUBSURF


def main():
    scene = Scene(1500, 1000, filepath="./")
    scene.setup()

    camera = Camera((1, 0, 1), (90, 0, 0), view_align=True)
    camera.add_to_current_scene()

    lamp = SunLamp(10, (0, 0, 3), ORIGIN)
    lamp.add_to_current_scene()

    monkey = Monkey(ORIGIN, (5, 0, 45), radius=1.25)
    monkey.add_to_current_scene()
    monkey.add_modifier(SUBSURF)
    monkey.shade_smooth()

    scene.render()


# Execute running:
#   blender --background -P ./test.py
if __name__ == "__main__":
    main()
```
