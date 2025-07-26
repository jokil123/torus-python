from torus_lib.sdf import SphereSDF
from torus_lib.vector import Vector3


sdf = SphereSDF(Vector3(0, 0, 2), 1)
pos = Vector3(0, 0, 0)


print(sdf.distance(pos), sdf.normal(pos))
