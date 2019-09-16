from math import hypot

import matplotlib.axes
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots()

ax: matplotlib.axes.Axes

ax.set_aspect('equal')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

width_factor = 10

def compute_widths(dx, dy):

    if dx == 0:
        w = dy
    elif dy == 0:
        w = dx
    else:
        w = width_factor * hypot(dx, dy) / 500

    hw = 6 * w

    return w, hw

x_tail = 0
y_tail = 0

def make_vector(dx, dy, t=None):

    if t is None:
        t = ax.transData

    w, hw = compute_widths(dx, dy)

    arrow1 = mpatches.FancyArrow(
            x_tail,
            y_tail,
            dx,
            dy,
            length_includes_head=True,
            width=w,
            head_width=hw,
            color='b',
            transform=t
    )

    ax.add_patch(arrow1)


make_vector(1, 1)
make_vector(2, 3)
make_vector(5, 3, Affine2D().scale(.5) + ax.transData)


l = Line2D((0.1, 1.1), (0, 1), color='b', linewidth=2)
ax.add_line(l)

plt.show()
