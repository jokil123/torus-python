from __future__ import annotations
import math
from typing import Self

import numpy as np


class Vector3:
    """Vector class with lots of utility functions"""

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

        """ Swizzling support """
        self.xy = (x, y)
        self.xz = (x, z)

        self.yx = (y, x)
        self.yz = (y, z)

        self.zx = (z, x)
        self.zy = (z, y)

        self.xyz = (x, y, z)

    @classmethod
    def fromTuple(cls, t: tuple[float, float, float]) -> Self:
        """Alternative constructor from a tuple"""
        return cls(t[0], t[1], t[2])

    @classmethod
    def fromList(cls, l: list[float]) -> Self:
        """Alternative constructor from a list"""
        if len(l) != 3:
            raise ValueError("List must be length 3")

        return cls(l[0], l[1], l[2])

    def __eq__(self, o: Vector3) -> bool:
        if not isinstance(o, Vector3):
            return False

        return self.x == o.x and self.y == o.y and self.z == o.z

    def __add__(self, o: Vector3) -> Self:
        return type(self)(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o: Vector3) -> Self:
        return type(self)(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, s: float) -> Self:
        return type(self)(self.x * s, self.y * s, self.z * s)

    def __truediv__(self, s: float) -> Self:
        return type(self)(self.x / s, self.y / s, self.z / s)

    def dot(self, o: Vector3) -> float:
        return self.x * o.x + self.y * o.y + self.z * o.z

    def cross(self, o: Vector3) -> Self:
        cx = self.y * o.z - self.z * o.y
        cy = -(self.x * o.z - self.z * o.x)
        cz = self.x * o.y - self.y * o.x

        return type(self)(cx, cy, cz)

    def mag(self) -> float:
        try:
            mag = math.sqrt((self.x**2) + (self.y**2) + (self.z**2))
            return mag
        except TypeError as e:
            mag = np.sqrt((self.x**2) + (self.y**2) + (self.z**2))
            return mag

    def normalized(self) -> Self:
        return self / self.mag()

    def rotate(self, axis: Vector3, angle: float) -> Vector3:
        """Rotate a vector around another vector by angle (in radians)"""
        """This Function uses Rodrigues formula (https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula)"""

        return (
            self * np.cos(angle)
            + axis.cross(self) * np.sin(angle)
            + axis * (axis.dot(self)) * (1 - np.cos(angle))
        )

    def tangents(self) -> tuple[Vector3, Vector3]:
        if self.dot(Vector3.UP) == 0:
            return (Vector3.FORWARD, Vector3.RIGHT)

        cotangent = self.cross(Vector3.UP)
        tangent = self.cross(cotangent)

        return (tangent, cotangent)

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

    ZERO: Vector3
    ONE: Vector3
    UP: Vector3
    DOWN: Vector3
    LEFT: Vector3
    RIGHT: Vector3
    FORWARD: Vector3
    BACK: Vector3


# Constants for the vectors
Vector3.ZERO = Vector3(0, 0, 0)
Vector3.ONE = Vector3(1, 1, 1)

Vector3.UP = Vector3(0, 1, 0)
Vector3.DOWN = Vector3(0, -1, 0)

Vector3.RIGHT = Vector3(1, 0, 0)
Vector3.LEFT = Vector3(-1, 0, 0)

Vector3.FORWARD = Vector3(0, 0, 1)
Vector3.BACK = Vector3(0, 0, -1)
