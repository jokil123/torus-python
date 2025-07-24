import math
import unittest
from torus_lib.vector import Vector3


class Vector3Tests(unittest.TestCase):
    """Tests for the Vector3 class"""

    def test_init(self):
        a = Vector3(1, 2, 3)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 2)
        self.assertEqual(a.z, 3)

        b = Vector3(-2, 0, 5)
        self.assertEqual(b.x, -2)
        self.assertEqual(b.y, 0)
        self.assertEqual(b.z, 5)

        self.assertEqual(Vector3.fromTuple((1, 2, 3)), a)
        self.assertEqual(Vector3.fromList([-2, 0, 5]), b)

        self.assertRaises(ValueError, lambda: Vector3.fromList([-2, 0]))

    def test_eq(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a, a)
        self.assertEqual(a, Vector3(1, 2, 3))
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, Vector3(1, 2, 4))

    def test_constants(self):
        s = (
            Vector3.UP
            + Vector3.DOWN
            + Vector3.LEFT
            + Vector3.RIGHT
            + Vector3.FORWARD
            + Vector3.BACK
        )

        self.assertEqual(s, Vector3(0, 0, 0))
        self.assertEqual(Vector3.ZERO - Vector3.ONE, Vector3(-1, -1, -1))

    def test_add(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)
        self.assertEqual(a + b, Vector3(-1, 2, 8))

    def test_sub(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)
        self.assertEqual(a - b, Vector3(3, 2, -2))

    def test_mul(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)
        self.assertEqual(a * 2, Vector3(2, 4, 6))
        self.assertEqual(b * 0.5, Vector3(-1, 0, 2.5))

    def test_truediv(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a / 2, Vector3(0.5, 1, 1.5))
        self.assertEqual(b / 0.5, Vector3(-4, 0, 10))

    def test_dot(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a.dot(Vector3.ONE), 6)
        self.assertEqual(b.dot(Vector3.RIGHT), -2)
        self.assertEqual(Vector3.ONE.dot(Vector3.ONE * -1), -3)

        self.assertEqual(Vector3.RIGHT.dot(Vector3.UP), 0)

        self.assertEqual(a.dot(b), 13)
        self.assertEqual(a.dot(a), 14)

    def test_cross(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a.cross(a), Vector3(0, 0, 0))
        self.assertEqual(b.cross(b), Vector3(0, 0, 0))
        self.assertEqual(a.cross(b), Vector3(10, -11, 4))

        self.assertEqual(Vector3.RIGHT.cross(Vector3.UP), Vector3.FORWARD)

    def test_mag(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a.mag(), math.sqrt(14))
        self.assertEqual(b.mag(), math.sqrt(29))

        self.assertEqual(Vector3.UP.mag(), 1)
        self.assertEqual(Vector3.ONE.mag(), math.sqrt(3))
        self.assertEqual(Vector3.ZERO.mag(), 0)

    def test_normalized(self):
        a = Vector3(1, 2, 3)
        b = Vector3(-2, 0, 5)

        self.assertEqual(a.normalized().x, 1 / math.sqrt(14))
        self.assertEqual(Vector3.UP.normalized().y, 1)
        self.assertEqual(Vector3.ONE.normalized().y, 1 / math.sqrt(3))
        self.assertRaises(ZeroDivisionError, lambda: Vector3.ZERO.normalized())


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
