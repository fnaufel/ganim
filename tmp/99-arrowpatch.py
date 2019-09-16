import math

import matplotlib.axes
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots()

ax: matplotlib.axes.Axes

ax.set_aspect('equal')
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

x_tail = 0
y_tail = 0

dx = 1
dy = 1
w = .25
arrow = mpatches.Arrow(x_tail, y_tail, dx, dy, width=w, color='r')#, transform=Affine2D().scale(0.5) + ax.transData)
ax.add_patch(arrow)

dx = 1
dy = 2
arrow2 = mpatches.Arrow(x_tail, y_tail, dx, dy, width=w, color='g')#, transform=Affine2D().scale(1.5) + ax.transData)
ax.add_patch(arrow2)

dx = 1
dy = 3
arrow3 = mpatches.Arrow(x_tail, y_tail, dx, dy, width=w, color='b')#, transform=Affine2D().scale(3) + ax.transData)
ax.add_patch(arrow3)

dx = 1
dy = 4
arrow4 = mpatches.Arrow(x_tail, y_tail, dx, dy, width=w, color='y')#, transform=Affine2D().scale(1) + ax.transData)
ax.add_patch(arrow4)

l = Line2D((2, 5), (0, 3), linewidth=2)
ax.add_line(l)

plt.show()
