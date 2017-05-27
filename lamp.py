import bpy
from abc import ABCMeta

from .variables import ORIGIN, LAYER_1


class Lamp(metaclass=ABCMeta):
    """Base lamp object"""
    def __init__(self, type_, radius, location, rotation, view_align, layers, cast_shadow):
        """
        :param type_:
        :param radius: Radius
        :param location: Location for the newly added object
        :param rotation: Rotation for the newly added object
        :param view_align: Align to View, Align the new object to the view
        :param layers: Layer
        :param cast_shadow: Lamp casts shadow
        """
        self.type_ = type_
        self.radius = radius
        self.location = location
        self.rotation = rotation
        self.view_align = view_align
        self.layers = layers
        self.cast_shadow = cast_shadow

    def add_to_scene(self):
        bpy.ops.object.lamp_add(type=self.type_,
                                radius=self.radius,
                                location=self.location,
                                rotation=self.rotation,
                                view_align=self.view_align,
                                layers=self.layers)
        bpy.context.object.data.cycles.cast_shadow = self.cast_shadow



class PointLamp(Lamp):
    """Point lamp object"""
    def __init__(self, radius, location=ORIGIN, rotation=ORIGIN, view_align=False, layers=LAYER_1, cast_shadow=True):
        super(PointLamp, self).__init__('POINT', radius, location, rotation, view_align, layers, cast_shadow)


class SunLamp(Lamp):
    """Point lamp object"""
    def __init__(self, radius, location=ORIGIN, rotation=ORIGIN, view_align=False, layers=LAYER_1, cast_shadow=True):
        super(SunLamp, self).__init__('SUN', radius, location, rotation, view_align, layers, cast_shadow)
