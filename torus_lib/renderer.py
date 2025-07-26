from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypedDict
from torus_lib.dicts import MarchConfig
from torus_lib.ray_marcher import Camera, HitInfo, march_ray
from torus_lib.screen import Color, Display
from torus_lib.sdf import SDF
from torus_lib.shader import Shader


class Scene(ABC):
    @abstractmethod
    def get_camera(self) -> Camera:
        pass

    @abstractmethod
    def get_shader(self) -> Shader:
        pass

    @abstractmethod
    def get_sdf(self) -> SDF:
        pass

    @abstractmethod
    def update(self, dt: float):
        pass


class Renderer:
    def __init__(self, scene: Scene, display: Display, config: MarchConfig):
        self.scene = scene
        self.display = display
        self.config = config

    def render(self, dt: float):
        self.scene.update(dt)

        H, W = self.display.get_resolution()
        self.scene.get_camera().set_resolution(H, W)
        rays = self.scene.get_camera().generate_rays_info()

        c: list[list[Color]] = []

        for h in range(0, len(rays)):
            c.append([])
            for w in range(0, len(rays[h])):
                hit_info = march_ray(rays[h][w], self.scene.get_sdf(), self.config)
                color = self.scene.get_shader().render_hit(hit_info)

                c[h].append(color)

        self.display.draw(c)
