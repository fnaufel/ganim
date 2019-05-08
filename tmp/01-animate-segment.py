import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import ganim as ga
from matplotlib.animation import FuncAnimation

print('Successfully imported', ga.name)

ga.set_up_style()

fig, ax = ga.create_figure()

f = ga.animate_segment(ax, (.2, .3), (.49, .49), 100)

anim = FuncAnimation(
        fig,
        f,
        frames=100,
        interval=25
)

#anim.save('segment.mp4')

plt.show()
