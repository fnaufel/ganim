
import matplotlib.axes
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.patches import Polygon
import numpy as np
from matplotlib.transforms import Affine2D

ax : matplotlib.axes.Axes

ax = plt.axes()
ax.set_aspect('equal')

vertices = np.array([(1/2, 1/2), (1/4, 1/2), (1/4, 1/4), (1/2, 1/4)])

square = Polygon(
        vertices,
        closed=True,
        facecolor=to_rgba('red', .5),
        edgecolor='blue',
        fill=True,
        transform=Affine2D().rotate_deg_around(1/2, 1/2, 30) + ax.transData
)

ax.add_artist(square)

plt.show()
