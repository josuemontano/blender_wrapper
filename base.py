class BlenderObject:
    """Base blender object"""
    def add_to_scene(self):
        pass

    def clear_location(self, clear_delta=False):
        bpy.ops.object.location_clear(clear_delta)
