
from panda3d.core import GeomVertexFormat, Geom, GeomNode

def make_mesh(name, vertices, normals, colors, triangles):

    v3n3c4 = GeomVertexFormat.get_v3n3c4()
    data = GeomVertexData(name, v3n3c4, Geom.UHStatic)
    data.setNumRows(len(vertices))

    vertex_writer = GeomVertexWriter(data, 'vertex')
    normal_writer = GeomVertexWriter(data, 'normal')
    color_writer = GeomVertexWriter(data, 'color')

    for vertex in vertices:
        vertex_writer.addData3(*vertex)

    for normal in normals:
        normal_writer.addData3(*normal)

    for color in colors:
        v_writer.addData3(*color)

    prim = GeomTriangles(Geom.UHStatic)

    for triangle in triangles:
        prim.addVertices(*triangle)

    geom = Geom(data)
    geom.addPrimitive(prim)

    node = GeomNode(name)
    node.addGeom(geom)

    return node
