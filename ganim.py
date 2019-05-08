import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

name = 'ganim'


def set_up_style():

    # TODO: math array lines and fraction lines are rendered very thin.

    # TODO:
    #   figure.dpi seems to have no effect on svg file.
    #   open in Image Magick to make sure.

    # TODO: add arrows to spines.

    # TODO: compare and set more params below.

    # my_style = {
    #     'axes.edgecolor': 'y',
    #     'axes.facecolor': 'k',
    #     'axes.formatter.use_mathtext': True,
    #     'axes.labelcolor': 'w',
    #     'axes.linewidth': 1.0,
    #     'axes.spines.right': False,
    #     'axes.spines.top': False,
    #     #    'figure.dpi': 300,
    #     'figure.edgecolor': 'k',
    #     'figure.facecolor': 'k',
    #     'figure.figsize': [16, 9],
    #     'font.family': ['serif'],  # use serif rather than sans-serif?
    #     #    'font.monospace': 'Hack',
    #     #    'font.sans-serif': [],  # Unset sans-serif?
    #     'font.serif': ['Computer Modern Roman'],
    #     #    'image.origin': 'lower',
    #     #    'pgf.preamble': [r'\usepackage[T1]{fontenc}', r'\usepackage{xcolor}', r'\usepackage{amsmath}',
    #     #    r'\usepackage{euler}',],
    #     #    'pgf.rcfonts': False,
    #     #    'pgf.texsystem': 'xelatex',
    #     'savefig.edgecolor': 'k',
    #     'savefig.facecolor': 'k',
    #     'text.color': 'w',
    #     'text.latex.preamble': [r'\usepackage{xcolor}', r'\usepackage{euler}', r'\usepackage{amsmath}', ],
    #     #    'text.latex.unicode': True,
    #     'text.usetex': True,
    #     'xtick.color': 'y',
    #     'xtick.direction': 'inout',
    #     'ytick.color': 'y',
    #     'ytick.direction': 'inout',
    # }

    my_style = {
        'axes.edgecolor': 'y',
        'axes.facecolor': 'k',
        'axes.formatter.use_mathtext': True,
        'axes.labelcolor': 'w',
        'axes.linewidth': 1.0,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.left': False,
        'axes.spines.bottom': False,
        'figure.dpi': 100,
        'figure.edgecolor': 'k',
        'figure.facecolor': 'k',
        'figure.figsize': [8, 4.5],
        'font.family': ['serif'],  # use serif rather than sans-serif?
        'font.serif': ['Computer Modern Roman'],
        'patch.edgecolor': 'white',
        'savefig.dpi': 100,
        'savefig.edgecolor': 'k',
        'savefig.facecolor': 'k',
        'text.color': 'w',
        'text.latex.preamble': [
            r'\usepackage{xcolor}',
            r'\usepackage{euler}',
            r'\usepackage{amsmath}',
        ],
        'text.usetex': True,
        'xtick.color': 'y',
        'xtick.direction': 'inout',
        'ytick.color': 'y',
        'ytick.direction': 'inout',
    }

    matplotlib.style.use(my_style)


def create_figure():
    """
    Create new figure.

    :return:
      (fig, ax): matplotlib figure and axes.
    """
    fig, ax = plt.subplots()
    ax.set_axis_off()
    return fig, ax


def animate_segment(ax, point_a, point_b, n_frames):
    """
    Generates an animation of a line segment.

    :param ax: axes where to draw.
    :param point_a: starting point.
    :param point_b: ending point.
    :param n_frames: amount of frames that compose the animation.

    :return:
      animate_segment_func: function to be called later by main animation function.
    """

    xa, ya = point_a
    xb, yb = point_b
    dx = (xb - xa) / n_frames
    dy = (yb - ya) / n_frames

    def animate_segment_func(i):
        x = xa + i * dx
        y = ya + i * dy
        ends = np.array([[xa, ya], [x, y]])
        segment = matplotlib.path.Path(ends)
        ax.add_patch(matplotlib.patches.PathPatch(segment))

    return animate_segment_func

def render_scene(fig, func, frames=100, interval=25):
    """
    Renders the scene.

    :param fig: figure.
    :param func: animation function
    :param frames:
    :param interval:
    :return:
    """
    scene = FuncAnimation(
            fig,
            func,
            frames=frames,
            interval=interval
    )

    return scene
