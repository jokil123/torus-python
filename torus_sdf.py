import matplotlib.pyplot as plt
import numpy as np
from torus_lib.vector import Vector3


def torus_sdf(x, y, z, R, r):
    pass


def f(x, y):
    r = 1
    return np.sqrt(x**2 + y**2) - r


x = np.linspace(-1, 1, 21)
y = np.linspace(-1, 1, 21)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(10, 5))
# The 'shading=' argument is important for aligning the pixels properly.
# 'gouraud' provides a smooth, interpolated look.
# 'auto' or 'nearest' are also good options.
im = plt.pcolormesh(X, Y, Z, shading="gouraud", cmap="PiYG")
cax = plt.contour(X, Y, Z, [0])

# 5. Add a colorbar to show the mapping of values to colors
cbar = plt.colorbar(im)
cbar.set_label("f(x, y) = sin(x) * cos(y)")

# 6. Add labels and a title for clarity
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x,y) as Color on the xy-Plane")


plt.show()
