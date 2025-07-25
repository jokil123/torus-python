import math
from timeit import default_timer
from torus_lib.ray_marcher import Camera, HitInfo
from torus_lib.renderer import MarchConfig, Renderer, Scene, Shader
from torus_lib.screen import Color, ConsoleDisplay
from torus_lib.sdf import SDF, TorusSDF
from torus_lib.vector import Vector3


class BWShader(Shader):
    def render_hit(self, hit: HitInfo | None) -> Color:
        if hit:
            return Color.WHITE
        else:
            return Color.BLACK


class TorusScene(Scene):
    def __init__(self):
        self.c = Camera(90 * math.pi / 180)
        self.bw = BWShader()
        self.t = 0

    def get_camera(self) -> Camera:
        return self.c

    def get_shader(self) -> Shader:
        return self.bw

    def get_sdf(self) -> SDF:
        return TorusSDF(
            Vector3(0, 0, 5), Vector3.FORWARD.rotate(Vector3.UP, self.t), 5, 1
        )

    def update(self, dt: float):
        self.t += dt


def main():
    display = ConsoleDisplay()
    scene = TorusScene()
    config: MarchConfig = {"max_iterations": 100, "d_max": 100, "d_min": 0.01}
    renderer = Renderer(scene, display, config)

    last_t = default_timer()
    while True:
        current_t = default_timer()
        dt = current_t - last_t

        renderer.render(dt)

        last_t = current_t


if __name__ == "__main__":
    main()
