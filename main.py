import math
import time
from timeit import default_timer
from torus_lib.ray_marcher import Camera, HitInfo
from torus_lib.renderer import MarchConfig, Renderer, Scene
from torus_lib.screen import Color, ConsoleDisplay
from torus_lib.sdf import SDF, SphereSDF, TorusSDF
from torus_lib.shader import PhongShader, Shader
from torus_lib.util import remap
from torus_lib.vector import Vector3


class TorusScene(Scene):
    def __init__(self):
        self.c = Camera(45 * math.pi / 180)
        # self.shader = BWShader()
        # self.shader = DepthShader(3 - 3.5, 3 + 3.5)
        self.shader = PhongShader(Vector3(-1, -1, -1), Color(0.1, 0.1, 0.1))
        self.t = 0

    def get_camera(self) -> Camera:
        return self.c

    def get_shader(self) -> Shader:
        return self.shader

    def get_sdf(self) -> SDF:
        return TorusSDF(
            Vector3(0, 0, 4.5),
            Vector3(0, 1, 2).rotate(Vector3.UP, self.t),
            1,
            0.5,
        )
        # return TorusSDF(
        #     Vector3(0, 0, 1), Vector3.RIGHT.rotate(Vector3.UP, self.t), 5, 1
        # )

        # return SphereSDF(Vector3(0, 0, 0), 10)

    def update(self, dt: float):
        self.t += dt


def main():
    display = ConsoleDisplay()
    scene = TorusScene()
    config: MarchConfig = {"max_iterations": 15, "d_max": 10, "d_min": 0.1}
    renderer = Renderer(scene, display, config)

    last_t = default_timer()
    while True:
        current_t = default_timer()
        dt = current_t - last_t

        renderer.render(dt)

        last_t = current_t

        # print("frame drawn")
        # time.sleep(0.1)


if __name__ == "__main__":
    main()
