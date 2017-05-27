import bpy


class Scene:
    """Scene object"""
    def __init__(self, filepath, render_engine='CYCLES'):
        self.filepath = filepath
        self.render_engine = 'CYCLES'

    def setup(self):
        self._cleanup()

        bpy.context.scene.render.filepath = self.filepath
        bpy.context.scene.render.engine = self.render_engine
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 1

    def render(self):
        bpy.ops.render.render(animation=True)

    def _cleanup(self):
        """Delete everything"""
        bpy.ops.object.delete(use_global=False)
