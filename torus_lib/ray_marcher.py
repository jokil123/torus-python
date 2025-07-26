from __future__ import annotations
import math
from torus_lib.dicts import HitInfo, MarchConfig, RayInfo
from torus_lib.sdf import SDF
from torus_lib.vector import Vector3


def march_ray(ray_info: RayInfo, sdf: SDF, config: MarchConfig) -> HitInfo | None:
    """Marches a single ray, returns None if nothing was hit, otherwise information about the hit"""

    current_pos = ray_info["position"]

    for i in range(0, config["max_iterations"]):
        distance = sdf.distance(current_pos)
        # print(f"pos: {self.position}, distance: {distance}")
        current_pos += ray_info["direction"] * distance

        if distance > config["d_max"]:
            return None

        if distance < config["d_min"]:
            return {"position": current_pos, "normal": sdf.normal(current_pos)}

    return None


class Camera:
    """A class that helps creating rays"""

    def __init__(
        self,
        fov: float,
    ):
        self.fov = fov
        self.resolution: int = 1
        self.aspect_ratio: float = 1
        self.pixel_aspect: float = 1

    def generate_rays_info(self) -> list[list[RayInfo]]:
        rays: list[list[RayInfo]] = []
        rays_h = self.resolution
        rays_w = int(rays_h * self.aspect_ratio)

        z = rays_h / (2 * math.tan(self.fov / 2))

        for h in range(0, rays_h):
            rays.append([])
            for w in range(0, rays_w):
                # x = -(rays_w - 1) / 2 + w
                x = (-(rays_w - 1) / 2 + w) * self.pixel_aspect
                y = -(rays_h - 1) / 2 + h

                ray_info: RayInfo = {
                    "position": Vector3.ZERO,
                    "direction": Vector3(x, y, z).normalized(),
                }
                rays[h].append(ray_info)

        return rays

    def set_resolution(self, h: int, w: int):
        if h < 0 or w < 0:
            raise ValueError("Height or width less than 0")

        self.resolution = h
        self.aspect_ratio = w / h

    def set_pixelaspect(self, a: float):
        self.pixel_aspect = a
