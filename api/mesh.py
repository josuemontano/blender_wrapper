import bpy

from .base import BlenderObject
from .variables import LAYER_1, NOTHING


class Mesh(BlenderObject):
    """Base mesh"""
    def __init__(self, location, rotation, view_align=False, layers=LAYER_1, radius=1.0):
        super(Mesh, self).__init__(location, rotation, view_align, layers)
        self.radius = radius

    def add_modifier(self, type):
        """Add a modifier to the active object

        :param type: Type of the modifier, must be one of the following:
                     - DATA_TRANSFER Data Transfer.
                     - MESH_CACHE Mesh Cache.
                     - MESH_SEQUENCE_CACHE Mesh Sequence Cache.
                     - NORMAL_EDIT Normal Edit.
                     - UV_PROJECT UV Project.
                     - UV_WARP UV Warp.
                     - VERTEX_WEIGHT_EDIT Vertex Weight Edit.
                     - VERTEX_WEIGHT_MIX Vertex Weight Mix.
                     - VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity.
                     - ARRAY Array.
                     - BEVEL Bevel.
                     - BOOLEAN Boolean.
                     - BUILD Build.
                     - DECIMATE Decimate.
                     - EDGE_SPLIT Edge Split.
                     - MASK Mask.
                     - MIRROR Mirror.
                     - MULTIRES Multiresolution.
                     - REMESH Remesh.
                     - SCREW Screw.
                     - SKIN Skin.
                     - SOLIDIFY Solidify.
                     - SUBSURF Subdivision Surface.
                     - TRIANGULATE Triangulate.
                     - WIREFRAME Wireframe, Generate a wireframe on the edges of a mesh.
                     - ARMATURE Armature.
                     - CAST Cast.
                     - CORRECTIVE_SMOOTH Corrective Smooth.
                     - CURVE Curve.
                     - DISPLACE Displace.
                     - HOOK Hook.
                     - LAPLACIANSMOOTH Laplacian Smooth.
                     - LAPLACIANDEFORM Laplacian Deform.
                     - LATTICE Lattice.
                     - MESH_DEFORM Mesh Deform.
                     - SHRINKWRAP Shrinkwrap.
                     - SIMPLE_DEFORM Simple Deform.
                     - SMOOTH Smooth.
                     - WARP Warp.
                     - WAVE Wave.
                     - CLOTH Cloth.
                     - COLLISION Collision.
                     - DYNAMIC_PAINT Dynamic Paint.
                     - EXPLODE Explode.
                     - FLUID_SIMULATION Fluid Simulation.
                     - OCEAN Ocean.
                     - PARTICLE_INSTANCE Particle Instance.
                     - PARTICLE_SYSTEM Particle System.
                     - SMOKE Smoke.
                     - SOFT_BODY Soft Body.
                     - SURFACE Surface.
        """
        bpy.ops.object.modifier_add(type)


class Cone(Mesh):
    def __init__(self, location, rotation, vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type=NOTHING, view_align=False, layers=LAYER_1):
        super(Cone, self).__init__(location, rotation, view_align, layers, 0.0)

        self.vertices = vertices
        self.radius1 = radius1
        self.radius2 = radius2
        self.depth = depth
        self.end_fill_type = end_fill_type

    def add_to_scene(self):
        bpy.ops.mesh.primitive_cone_add(vertices=self.vertices,
                                        radius1=self.radius1,
                                        radius2=self.radius2,
                                        depth=self.depth,
                                        end_fill_type=self.end_fill_type,
                                        location=self.location,
                                        rotation=self.rotation,
                                        view_align=self.view_align,
                                        layers=self.layers)
class Cube(Mesh):
    def add_to_scene(self):
        bpy.ops.mesh.primitive_cube_add(radius=self.radius,
                                        location=self.location,
                                        rotation=self.rotation,
                                        view_align=self.view_align,
                                        layers=self.layers)


class Cylinder(Mesh):
    def __init__(self, location, rotation, vertices=32, radius=1.0, depth=2.0, end_fill_type=NOTHING, view_align=False, layers=LAYER_1):
        super(Cylinder, self).__init__(location, rotation, view_align, layers, radius)

        self.vertices = vertices
        self.depth = depth
        self.end_fill_type = end_fill_type

    def add_to_scene(self):
        bpy.ops.mesh.primitive_cylinder_add(radius=self.radius,
                                            vertices=self.vertices,
                                            depth=self.depth,
                                            end_fill_type=self.end_fill_type,
                                            location=self.location,
                                            rotation=self.rotation,
                                            view_align=self.view_align,
                                            layers=self.layers)


class Plane(Mesh):
    def add_to_scene(self):
        bpy.ops.mesh.primitive_plane_add(radius=self.radius,
                                         location=self.location,
                                         rotation=self.rotation,
                                         view_align=self.view_align,
                                         layers=self.layers)
