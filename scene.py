import bpy


class Scene:
    """Scene object"""
    def __init__(self, resolution_x, resolution_y, filepath, render_engine='CYCLES'):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.filepath = filepath
        self.render_engine = 'CYCLES'

    def setup(self):
        self._cleanup()

        bpy.context.scene.render.filepath = self.filepath
        bpy.context.scene.render.engine = self.render_engine
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 1

        bpy.context.scene.render.resolution_x = self.resolution_x
        bpy.context.scene.render.resolution_y = self.resolution_y

    def render(self, samples=50, resolution_percentage=50):
        bpy.context.scene.render.resolution_percentage = resolution_percentage
        bpy.context.scene.cycles.samples = samples
        bpy.ops.render.render(animation=True)

    def _cleanup(self):
        """Delete everything"""
        bpy.ops.object.delete(use_global=False)
