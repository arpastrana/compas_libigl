from itertools import groupby

import numpy

import compas

from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles
from compas.plotters import MeshPlotter
from compas.utilities import i_to_rgb

import iso

mesh = Mesh.from_json(compas.get('tubemesh.json'))
mesh_quads_to_triangles(mesh)

key_index = mesh.key_index()

v = mesh.get_vertices_attributes('xyz')
f = [[key_index[key] for key in mesh.face_vertices(fkey)] for fkey in mesh.faces()]
z = mesh.get_vertices_attribute('z')

V = numpy.array(v, dtype=numpy.float64)
F = numpy.array(f, dtype=numpy.int32)
Z = numpy.array(z, dtype=numpy.float64)
N = 30

result = iso.isolines(V, F, Z, N)

vertices = sorted(result.vertices, key=lambda v: v[2])
zmin = vertices[0][2]
zmax = vertices[-1][2]
zspn = zmax - zmin

edges = sorted(result.edges, key=lambda e: result.vertices[e[0]][2])
edges = groupby(result.edges, key=lambda e: result.vertices[e[0]][2])

lines = []
for z, group in edges:
    color = i_to_rgb((z - zmin) / zspn)
    for i, j in group:
        lines.append({
            'start' : result.vertices[i],
            'end'   : result.vertices[j],
            'color' : color
        })

plotter = MeshPlotter(mesh)
plotter.draw_faces()
plotter.draw_lines(lines)
plotter.show()
