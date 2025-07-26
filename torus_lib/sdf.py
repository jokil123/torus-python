from __future__ import annotations
from abc import ABC, abstractmethod
import sys
import numpy as np
from torus_lib.vector import Vector3


class SDF(ABC):
    def __init__(self, epsilon) -> None:
        super().__init__()
        self.epsilon = epsilon

    @abstractmethod
    def distance(self, sample_pos: Vector3) -> float:
        pass

    def normal(self, sample_pos: Vector3) -> Vector3:
        px = sample_pos.x
        py = sample_pos.y
        pz = sample_pos.z
        e = self.epsilon
        dist = self.distance

        """default implementation using ∇f"""
        nx = dist(Vector3(px + e, py, pz)) - dist(Vector3(px - e, py, pz))
        ny = dist(Vector3(px, py + e, pz)) - dist(Vector3(px, py - e, pz))
        nz = dist(Vector3(px, py, pz + e)) - dist(Vector3(px, py, pz - e))

        return Vector3(nx, ny, nz).normalized()


class TorusSDF(SDF):
    def __init__(self, pos: Vector3, dir: Vector3, R: float, r: float):
        super().__init__(0.01)
        self.pos = pos
        self.dir = dir.normalized()
        self.R = R
        self.r = r

    def distance(self, sample_pos: Vector3) -> float:
        deltaPos = sample_pos - self.pos

        dP_ortho = deltaPos - (self.dir * deltaPos.dot(self.dir))
        if dP_ortho.mag() == 0:
            dP_ortho, _ = dP_ortho.tangents()

        closest_ring_pos = (dP_ortho.normalized()) * self.R

        distance = (deltaPos - closest_ring_pos).mag() - self.r

        return distance


class SphereSDF(SDF):
    def __init__(self, pos: Vector3, radius: float):
        super().__init__(0.01)
        self.pos = pos
        self.radius = radius

    def distance(self, sample_pos: Vector3) -> float:
        return (
            np.sqrt(
                (self.pos.x - sample_pos.x) ** 2
                + (self.pos.y - sample_pos.y) ** 2
                + (self.pos.z - sample_pos.z) ** 2
            )
            - self.radius
        )


class UnionSDF(SDF):
    def __init__(self, sdfs: list[SDF]):
        self.sdfs = sdfs

    def distance(self, sample_pos: Vector3) -> float:
        min_distance = sys.maxsize

        for sdf in self.sdfs:
            min_distance = min(min_distance, sdf.distance(sample_pos))

        return min_distance
