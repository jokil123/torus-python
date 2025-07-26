from typing import TypedDict
from torus_lib.vector import Vector3


class HitInfo(TypedDict):
    position: Vector3
    normal: Vector3


class RayInfo(TypedDict):
    position: Vector3
    direction: Vector3


class MarchConfig(TypedDict):
    d_min: float
    d_max: float
    max_iterations: int
