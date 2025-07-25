from random import random
import time
from torus_lib.screen import Color, ConsoleDisplay
from torus_lib.sdf import SphereSDF, TorusSDF
from torus_lib.vector import Vector3
from timeit import default_timer

d = ConsoleDisplay()

start = default_timer()

while True:
    t = default_timer() - start

    colors: list[list[Color]] = []

    H, W = d.get_resolution()

    # print(d.get_resolution())

    sdf = TorusSDF(
        Vector3(W / 2, H / (2 * d.get_pixel_ratio()), 00),
        Vector3.FORWARD.rotate(Vector3.UP, t / 2),
        30,
        10,
    )

    for h in range(0, H):
        colors.append([])
        for w in range(0, W):
            h_corrected = h / d.get_pixel_ratio()
            colors[h].append(
                Color.WHITE * -sdf.distance(Vector3(w, h_corrected, 0)) / 100
            )

    # print("screen before")
    d.draw(colors)
    # print("screen after")
    time.sleep(0.1)
