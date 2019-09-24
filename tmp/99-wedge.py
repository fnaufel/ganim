import matplotlib.axes
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax: matplotlib.axes.Axes

ax.set_aspect('equal')

wedge = Wedge(
        (.5, .5),
        .2,
        0,
        45,
        alpha=.5,
        edgecolor='blue',
        fill=True,
        facecolor='red',
        linewidth=2,
)

ax.add_artist(wedge)

plt.show()
