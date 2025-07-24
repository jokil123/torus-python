from __future__ import annotations
from math import sqrt

from numpy import vectorize


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

    @staticmethod
    def fromTuple(t: tuple[float, float, float]) -> Vector3:
        """Alternative constructor from a tuple"""
        return Vector3(t[0], t[1], t[2])

    @staticmethod
    def fromList(l: list[float]) -> Vector3:
        """Alternative constructor from a list"""
        if len(l) != 3:
            raise ValueError("List must be length 3")

        return Vector3(l[0], l[1], l[2])

    def __eq__(self, o: Vector3) -> bool:
        if not isinstance(o, Vector3):
            return False

        return self.x == o.x and self.y == o.y and self.z == o.z

    def __add__(self, o: Vector3) -> Vector3:
        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o: Vector3) -> Vector3:
        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, s: float) -> Vector3:
        return Vector3(self.x * s, self.y * s, self.z * s)

    def __truediv__(self, s: float) -> Vector3:
        return Vector3(self.x / s, self.y / s, self.z / s)

    def dot(self, o: Vector3) -> float:
        return self.x * o.x + self.y * o.y + self.z * o.z

    def cross(self, o: Vector3) -> Vector3:
        cx = self.y * o.z - self.z * o.y
        cy = -(self.x * o.z - self.z * o.x)
        cz = self.x * o.y - self.y * o.x

        return Vector3(cx, cy, cz)

    def mag(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self) -> Vector3:
        return self / self.mag()

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
