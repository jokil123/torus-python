from abc import ABC, abstractmethod
from torus_lib.dicts import HitInfo
from torus_lib.screen import Color
from torus_lib.util import remap
from torus_lib.vector import Vector3


class Shader(ABC):
    @abstractmethod
    def render_hit(self, hit: HitInfo | None) -> Color:
        pass


class BWShader(Shader):
    def render_hit(self, hit: HitInfo | None) -> Color:
        if hit:
            return Color.WHITE
        else:
            return Color.BLACK


class DepthShader(Shader):
    def __init__(self, near: float, far: float):
        self.near = near
        self.far = far

    def render_hit(self, hit: HitInfo | None) -> Color:
        if hit:
            return Color.WHITE * remap(self.near, self.far, 1, 0, hit["position"].mag())
        else:
            return Color.BLACK


class PhongShader(Shader):
    def __init__(self, light_vector: Vector3, ambient: Color):
        self.light_vector = light_vector.normalized()
        self.ambient = ambient

    def render_hit(self, hit: HitInfo | None) -> Color:
        if not hit:
            return Color.BLACK

        # print(hit["normal"])

        light_color = (Color.WHITE * hit["normal"].dot(self.light_vector)).clamp()

        return light_color + self.ambient
