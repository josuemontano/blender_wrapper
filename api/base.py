from .variables import LAYER_1


class BlenderObject:
    """Base blender object"""
    def __init__(self, location, rotation, view_align=False, layers=LAYER_1):
        self.location = location
        self.rotation = rotation
        self.view_align = view_align
        self.layers = layers

    def add_to_scene(self):
        pass

    def clear_location(self, clear_delta=False):
        """
        Clear the object’s location

        :param clear_delta: Clear delta location in addition to clearing the normal location transform
        """
        bpy.ops.object.location_clear(clear_delta=clear_delta)

    def clear_origin(self):
        """Clear the object’s origin"""
        bpy.ops.object.origin_clear()

    def clear_rotation(self, clear_delta=False):
        """
        Clear the object’s rotation

        :param clear_delta: Clear delta rotation in addition to clearing the normal rotation transform
        """
        bpy.ops.object.rotation_clear(clear_delta=clear_delta)

    def clear_scale(self, clear_delta=False):
        """
        Clear the object’s scale

        :param clear_delta: Clear delta scale in addition to clearing the normal scale transform
        """
        bpy.ops.object.scale_clear(clear_delta=clear_delta)

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
        bpy.ops.object.mode_set(mode=mode, toggle=toggle)
