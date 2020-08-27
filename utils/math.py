
import numpy as np


def length(a, axis=0, keepdims=False):
    return (a**2).sum(axis, keepdims=keepdims)**.5


def norm(a, axis=0):
    return a/length(a, axis, keepdims=True)


def eval_tris(vertices, triangles):
    return [vertices[t] for t in triangles]


def tri_norm(vertices, center=None):
    '''
    Return the normal of the triangle defined by the vertices provided.

    Args:
        vertices: array (3,3)
            An array, the rows of which are the vertices of a triangle defined
            in a clockwise direction when viewed from outside the object.
    '''
    i, j, k = vertices
    n = norm(np.cross(k - i, j - i))
    if center is not None:
        if n.dot(i - center) < 0:
            return -n
    return n


def get_tri_norms(vertices, triangles, center=None):
    return [tri_norm(t, center) for t in eval_tris(vertices, triangles)]
