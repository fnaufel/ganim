import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import ganim as ga

ga.set_up_style()

fig, ax = ga.create_scene()

scene = ga.render_scene(
        fig,
        ga.animate_segment(
                ax,
                (.2, .3),
                (.49, -.49),
                color='r'
        )
)

# print('Salvando...')
# scene.save('segment.mp4', fps=24)
plt.show()
