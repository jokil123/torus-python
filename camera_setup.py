import math
from torus_lib.ray_marcher import Camera
from torus_lib.vector import Vector3

camera = Camera(Vector3.FORWARD, 90 * math.pi / 180, 20, 1, 1)
camera.generate_rays()

print(len(camera.rays) * len(camera.rays[0]))
