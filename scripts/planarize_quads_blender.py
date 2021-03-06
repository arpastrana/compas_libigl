import os
import numpy
import bpy
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_flatness
from compas.utilities import i_to_rgb
from compas_blender.artists import MeshArtist
import compas_libigl as igl


MAXDEV = 0.005
KMAX = 500

HERE = os.path.dirname(bpy.context.space_data.text.filepath)
FILE = os.path.join(HERE, '..', 'data', 'tubemesh.json')

mesh1 = Mesh.from_json(FILE)
vertices, faces = mesh1.to_vertices_and_faces()

V1 = numpy.array(vertices, dtype=numpy.float64)
F1 = numpy.array(faces, dtype=numpy.int32)
V2 = igl.planarize_quads(V1, F1, KMAX, MAXDEV)

mesh2 = Mesh.from_vertices_and_faces(V2, faces)
dev2 = mesh_flatness(mesh2, maxdev=MAXDEV)

mesh2.name = "Mesh2"

artist = MeshArtist(mesh2, layer="IGL")
colors = {fkey: i_to_rgb(dev2[fkey], normalize=True) for fkey in mesh2.faces()}
artist.draw_faces(colors=colors)
artist.draw_vertices()
