import bpy

from .base import BlenderObject
from .variables import ORIGIN, LAYER_1


class Camera(BlenderObject):
    """Camera"""
    def __init__(self, location, rotation, view_align=False, layers=LAYER_1):
        self.location = location
        self.rotation = rotation
        self.view_align = view_align
        self.layers = layers

    def add_to_scene(self):
        bpy.ops.object.camera_add(location=self.location,
                                  rotation=self.rotation,
                                  view_align=self.view_align,
                                  layers=self.layers)
