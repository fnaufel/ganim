from math import hypot

import matplotlib.axes
import matplotlib.text
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots()

ax: matplotlib.axes.Axes

ax.set_aspect('equal')
ax.set_xlim(0, 5)
ax.set_ylim(0, 3)

def make_vector(dx, dy):

    ax.annotate(
            '',
            (dx, dy),
            xytext=(0, 0),
            arrowprops=dict(
                    color='red',
                    # edgecolor='blue',
                    linewidth=1,
                    width=1,
                    headwidth= 5 * hypot(dx, dy),
                    headlength=7.5 * hypot(dx, dy),
            )
    )

make_vector(1, 1)
make_vector(2, 3)
make_vector(5, 3)


l = Line2D((0.1, 1.1), (0, 1), color='b', linewidth=2)
ax.add_line(l)

plt.show()
