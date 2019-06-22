import ganim as ga
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.transforms import Affine2D

ga.reset_default_style()

fig, ax = ga.create_scene()
ax: Axes

y = [0, 0, 0]
x = [1, 2, 3]
ax.plot(x, y, 'bo')

xline = [x[0], x[2]]
yline = [y[0], y[2]]

# Rotation works
# t = Affine2D().rotate_deg_around(x[0], y[0], 90) + ax.transData
# l = lines.Line2D(xline, yline, color='r')
# l.set_transform(t)
#
# ax.add_line(l)

# Scaling moves the line, because it moves the starting point!
# So I must follow the scaling with a translation
s = 1.5
a = xline[0]
b = yline[0]

t2 = Affine2D().scale(s) + Affine2D().translate(a * (1 - s), b * (1 - s)) + ax.transData
l2 = lines.Line2D(xline, yline, color='r', transform=t2)

ax.add_line(l2)


plt.show()
