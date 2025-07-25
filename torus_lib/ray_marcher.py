import itertools
from turtle import position
from typing import TypedDict
from torus_lib.sdf import SDF
from torus_lib.vector import Vector3


class HitInfo(TypedDict):
    position: Vector3
    normal: Vector3


def march_ray(
    position: Vector3,
    direction: Vector3,
    sdf: SDF,
    d_min: float,
    d_max: float,
    max_iterations: int,
) -> HitInfo | None:
    """Marches a single ray, returns None if nothing was hit, otherwise information about the hit"""

    pos = position

    for i in range(0, max_iterations):
        distance = sdf.distance(pos)
        # print(f"pos: {self.position}, distance: {distance}")
        pos += direction * distance

        if distance > d_max:
            return None

        if distance < d_min:
            return {"position": position, "normal": sdf.normal(position)}


class Ray:
    """Ray class"""

    def __init__(self, position: Vector3, direction: Vector3):
        self.start_position = position
        self.position = position
        self.direction = direction.normalized()

    def march(self, sdf: SDF):
        distance = sdf.distance(self.position)
        # print(f"pos: {self.position}, distance: {distance}")
        self.position = self.position + self.direction * distance
        return distance


class RayMarcher:
    """Ray marcher marches the rays"""

    def __init__(
        self,
        sdf: SDF,
        rays: list[Ray],
        max_iterations: int,
        d_min: float,
        d_max: float,
    ):
        self.sdf = sdf
        self.rays = rays
        self.max_iterations = max_iterations
        self.d_min = d_min
        self.d_max = d_max

    def march_all(self):
        for ray in self.rays:
            for i in range(0, self.max_iterations):
                d = ray.march(self.sdf)
                if not self.d_min < d < self.d_max:
                    print(f"Converged (or Diverged) in {i} Steps")
                    break


class Camera:
    """A class that helps creating rays"""

    def __init__(
        self,
        fov: float,
        resolution: int,
        aspect_ratio: float,
        pixel_aspect: float,
    ):
        self.fov = fov
        self.resolution = resolution
        self.aspect_ratio = aspect_ratio
        self.pixel_aspect = pixel_aspect

    def generate_rays(self) -> list[list[Ray]]:
        rays: list[list[Ray]] = []
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

                ray = Ray(Vector3.ZERO, dir)

                rays[v].append(ray)

        return rays

    # def get_rays(self) -> list[Ray]:
    #     return list(itertools.chain.from_iterable(self.rays))
