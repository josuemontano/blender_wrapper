import bpy

from .base import BlenderObject


class Camera(BlenderObject):
    """Camera"""
    def add_to_scene(self):
        bpy.ops.object.camera_add(location=self.location,
                                  rotation=self.rotation,
                                  view_align=self.view_align,
                                  layers=self.layers)
