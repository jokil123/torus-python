import math
from torus_lib.ray_marcher import Camera, Ray, RayMarcher
from torus_lib.sdf import SphereSDF
from torus_lib.vector import Vector3


sdf = SphereSDF(Vector3(0, 0, -10), 1)

camera = Camera(90 * math.pi / 180, 20, 1, 1)
camera.generate_rays()

marcher = RayMarcher(sdf, camera.get_rays(), 100, 0.01, 100)

marcher.march_all()
