"""This is just for the torus but optimized"""

import math
from timeit import default_timer
from torus_lib.dicts import MarchConfig
from torus_lib.ray_marcher import Camera, march_ray
from torus_lib.screen import ConsoleDisplay
from torus_lib.sdf import TorusSDF
from torus_lib.util import clamp, remap
from torus_lib.vector import Vector3


def lum_to_char(lum: float) -> str:
    CHARS = (
        """ .'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
    )
    # CHARS = """ 0123456789"""
    # CHARS = """ .:-=+*#%@"""

    charIndex = int(lum * (len(CHARS) - 1))

    return CHARS[charIndex]


def main():
    display = ConsoleDisplay()
    H, W = display.get_resolution()

    cam = Camera(45 * math.pi / 180)
    cam.set_pixelaspect(display.get_pixel_ratio())
    cam.set_resolution(H, W)

    rays = cam.generate_rays_info()

    sdf = TorusSDF(
        Vector3(0, 0, 4.5),
        Vector3(0, 1, 2),
        1,
        0.5,
    )

    cfg: MarchConfig = {"max_iterations": 20, "d_max": 10, "d_min": 0.1}

    light_vector = Vector3(-1, -1, -1)
    ambient_light = 0.1

    while True:
        current_t = default_timer()
        sdf.set_dir(Vector3(0, 1, 2).rotate(Vector3.UP, current_t))
        sc = ""

        for h in range(0, H):
            for w in range(0, W):
                hit = march_ray(rays[h][w], sdf, cfg)

                if hit == None:
                    lum = 0

                else:
                    lum = clamp(0, 1, hit["normal"].dot(light_vector) + ambient_light)

                sc += lum_to_char(lum)
            sc += "\n"
        print(sc, end="")


if __name__ == "__main__":
    main()
