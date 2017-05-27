import bpy
from abc import ABCMeta

from .variables import ORIGIN, LAYER_1


class Lamp(metaclass=ABCMeta):
    """Lamp object"""
    def __init__(self, type_, radius, location, rotation, view_align, layers):
        self.type_ = type_
        self.radius = radius
        self.location = location
        self.rotation = rotation
        self.view_align = view_align
        self.layers = layers

    def add_to_scene(self):
        bpy.ops.object.lamp_add(type=self.type_,
                                radius=self.radius,
                                location=self.location,
                                rotation=self.rotation,
                                view_align=self.view_align,
                                layers=self.layers)



class PointLamp(Lamp):
    """Point lamp object"""
    def __init__(self, radius, location=ORIGIN, rotation=ORIGIN, view_align=False, layers=LAYER_1):
        super(PointLamp, self).__init__('POINT', radius, location, rotation, view_align, layers)


class SunLamp(Lamp):
    """Point lamp object"""
    def __init__(self, radius, location=ORIGIN, rotation=ORIGIN, view_align=False, layers=LAYER_1):
        super(SunLamp, self).__init__('SUN', radius, location, rotation, view_align, layers)
