import bpy

from .base import BlenderObject


class Mesh(BlenderObject):
    """Base mesh"""
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
