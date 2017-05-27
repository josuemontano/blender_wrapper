class BlenderObject:
    """Base blender object"""
    def add_to_scene(self):
        pass

    def clear_location(self, clear_delta=False):
        """
        Clear the object’s location

        :param clear_delta: Clear delta location in addition to clearing the normal location transform
        """
        bpy.ops.object.location_clear(clear_delta)

    def set_mode(self, mode, toggle=False):
        """Sets the object interaction mode

        :param mode: Mode, must be one of the following:
                     - OBJECT Object Mode.
                     - EDIT Edit Mode.
                     - POSE Pose Mode.
                     - SCULPT Sculpt Mode.
                     - VERTEX_PAINT Vertex Paint.
                     - WEIGHT_PAINT Weight Paint.
                     - TEXTURE_PAINT Texture Paint.
                     - PARTICLE_EDIT Particle Edit.
                     - GPENCIL_EDIT Edit Strokes, Edit Grease Pencil Strokes.
        :param toggle: Toggle
        """
        bpy.ops.object.mode_set(mode, toggle)
