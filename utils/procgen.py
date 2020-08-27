
from itertools import combinations, product

from panda3d.core import GeomVertexFormat, GeomVertexData, GeomVertexWriter, Geom, GeomNode, GeomTriangles

import numpy as np
from scipy.spatial import Delaunay, ConvexHull

from utils.colour import WHITE
from utils.math import *


def mesh(vertices, normals, colours, triangles):

    print(vertices)
    print()
    print(normals)
    # print(colours)
    # print(triangles)

    # TODO: Make this name meaningful in some way
    name = 'test'

    v3n3c4 = GeomVertexFormat.get_v3n3c4()
    data = GeomVertexData(name, v3n3c4, Geom.UHStatic)
    data.set_num_rows(len(vertices))

    vertex_writer = GeomVertexWriter(data, 'vertex')
    normal_writer = GeomVertexWriter(data, 'normal')
    colour_writer = GeomVertexWriter(data, 'color')

    for vertex in vertices:
        vertex_writer.add_data3(*vertex)

    for normal in normals:
        normal_writer.add_data3(*normal)

    for colour in colours:
        colour_writer.add_data4(*colour)

    prim = GeomTriangles(Geom.UHStatic)

    for triangle in triangles:
        prim.add_vertices(*triangle)

    geom = Geom(data)
    geom.add_primitive(prim)

    node = GeomNode(name)
    node.add_geom(geom)

    return node


def hull(vertices, colours):
    if len(colours) == 1:
        colours = len(vertices) * colours

    vertices = np.array(vertices)
    colours = np.array(colours)

    # calculate triangles
    triangles = ConvexHull(vertices).simplices

    # calculate normals
    center = vertices.mean(axis=0)
    normals = get_tri_norms(vertices, triangles, center)

    # convert to long format (repeated vertices)
    vertices = np.concatenate(eval_tris(vertices, triangles))
    normals = np.repeat(normals, 3, axis=0)
    colours = np.concatenate(eval_tris(colours, triangles))
    triangles = np.arange(len(vertices)).reshape(-1, 3)

    return mesh(vertices, normals, colours, triangles)


def simplex(vertices, colours=[WHITE]):
    if len(colours) == 1:
        colours = 4 * colours

    normals = 5 * [(0, 0, 1)]
    triangles = list(combinations(range(4), 3))
    return mesh(vertices, normals, colours, triangles)

def cube(size, colours=[WHITE]):
    if len(colours) == 1:
        colours = 8 * colours

    vertices = list(product(*[(-i/2, i/2) for i in size]))
    return hull(vertices, colours)
