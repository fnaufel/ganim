import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

verts = np.array([[.1, .2], [.3, .4]])
l = matplotlib.path.Path(verts)

ax.add_patch(matplotlib.patches.PathPatch(l))

plt.show()
