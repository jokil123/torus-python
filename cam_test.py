import math
from torus_lib.ray_marcher import Camera, march_ray
from torus_lib.screen import Color, ConsoleDisplay
from torus_lib.sdf import SphereSDF, TorusSDF
from torus_lib.vector import Vector3

display = ConsoleDisplay()

H, W = display.get_resolution()

print(display.get_resolution())

camera = Camera(45 * math.pi / 180)
camera.set_resolution(H, W)
# camera.set_resolution(21, 31)
camera.set_pixelaspect(display.get_pixel_ratio())
print(camera.aspect_ratio)

rays = camera.generate_rays_info()

# sdf = SphereSDF(Vector3(0, 0, 5), 1)
sdf = TorusSDF(Vector3(0, 0, 5), Vector3(0, 0, 1), 1, 0.5)

c: list[list[Color]] = []

print(len(rays), len(rays[0]))

print(rays[0][0])

for h in range(0, len(rays)):
    c.append([])
    for w in range(0, len(rays[h])):
        rays[h][w]["direction"] = rays[h][w]["direction"].normalized()

        hit = march_ray(
            rays[h][w],
            sdf,
            {"max_iterations": 100, "d_max": 100, "d_min": 0.01},
        )

        c[h].append(Color.WHITE if hit else Color(0.1, 0.1, 0.1))

        # print("X" if hit else ".", end="")

        # print(hit)
    # print("")

display.draw(c)
