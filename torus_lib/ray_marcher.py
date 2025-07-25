from typing import TypedDict
from torus_lib.renderer import MarchConfig
from torus_lib.sdf import SDF
from torus_lib.vector import Vector3


class HitInfo(TypedDict):
    position: Vector3
    normal: Vector3


class RayInfo(TypedDict):
    position: Vector3
    direction: Vector3


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


class Camera:
    """A class that helps creating rays"""

    def __init__(
        self,
        fov: float,
    ):
        self.fov = fov
        self.resolution = 1
        self.aspect_ratio = 1
        self.pixel_aspect = 1

    def generate_rays_info(self) -> list[list[RayInfo]]:
        rays: list[list[RayInfo]] = []
        rays_v = self.resolution
        rays_h = int(rays_v * self.aspect_ratio * self.pixel_aspect)

        fov_v = self.fov
        fov_h = fov_v * self.aspect_ratio

        dphi_v = self.fov / rays_v
        dphi_h = fov_h / rays_h

        for v in range(0, rays_v):
            rays.append([])
            for h in range(0, rays_h):
                phi_v = fov_v / 2 + dphi_v * v
                phi_h = fov_h / 2 + dphi_h * h

                dir = Vector3.FORWARD.rotate(Vector3.RIGHT, phi_v).rotate(
                    Vector3.UP, phi_h
                )

                ray: RayInfo = {"position": Vector3.ZERO, "direction": dir}

                rays[v].append(ray)

        return rays

    def set_resolution(self, h: int, w: int):
        if h < 0 or w < 0:
            raise ValueError("Height or width less than 0")

        self.resolution = h
        self.aspect_ratio = w / h

    def set_pixelaspect(self, a: float):
        self.pixel_aspect = a
