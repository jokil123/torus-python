import plotly.graph_objects as go
import numpy as np

from torus_lib.sdf import TorusSDF
from torus_lib.vector import Vector3

X, Y, Z = np.mgrid[-1:1:100j, -1:1:100j, -1:1:100j]

torus_sdf = TorusSDF(Vector3(0, 1, 0), Vector3.UP, 0.5, 0.15)

values = np.tanh(5 * torus_sdf.distance(Vector3(X, Y, Z)))

fig = go.Figure(
    data=go.Volume(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=values.flatten(),
        isomin=0.1,
        isomax=0.8,
        opacity=0.1,  # needs to be small to see through all surfaces
        surface_count=17,  # needs to be a large number for good volume rendering
    )
)
fig.show()
