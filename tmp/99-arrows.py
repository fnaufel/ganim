import matplotlib.axes
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

ax : matplotlib.axes.Axes

ax = plt.axes()
ax.set_aspect('equal')
ax.arrow(
        0,
        0,
        0.5,
        0.5,
        lw=2,
        head_width=0.05,
        head_length=0.1,
        fc='k',
        ec='k'
)

ax.arrow(
        0,
        0,
        0.2,
        0.5,
        lw=2,
        head_width=0.05,
        head_length=0.1,
        fc='k',
        ec='k',
        transform=Affine2D().scale(0.5) + ax.transData
)

ax.arrow(
        0,
        0,
        0.5,
        0.2,
        lw=2,
        head_width=0.05,
        head_length=0.1,
        fc='k',
        ec='k',
        transform=Affine2D().scale(1.5) + ax.transData
)

plt.show()
