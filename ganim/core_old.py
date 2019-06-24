import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Default values for global variables ####################################

# Frames per second
FPS_DEFAULT = 60

# Interval between frames (in milliseconds)
INTERVAL_DEFAULT = 1000 / FPS_DEFAULT

# Limits for x axis (in data coords)
XLIM_DEFAULT = (-1, 5)

# Limits for y axis (in data coords)
YLIM_DEFAULT = (-1, 5)

# Global variables #######################################################

FPS = FPS_DEFAULT
INTERVAL = INTERVAL_DEFAULT
XLIM = XLIM_DEFAULT
YLIM = YLIM_DEFAULT


##########################################################################

def reset_default_config():
    """
    Set global variables to default values.

    """

    global FPS
    global INTERVAL
    global XLIM
    global YLIM

    FPS = FPS_DEFAULT
    INTERVAL = INTERVAL_DEFAULT
    XLIM = XLIM_DEFAULT
    YLIM = YLIM_DEFAULT


def reset_default_style():
    """
    Define matplotlib style to be used.

    """

    # TODO: LaTeX: linhas de array e de fração estão finas demais.

    # TODO: Adicionar setas aos eixos (spines).

    # TODO: Completar parâmetros abaixo.

    default_style = {
        'axes.edgecolor': 'y',
        'axes.facecolor': 'k',
        'axes.formatter.use_mathtext': True,
        'axes.labelcolor': 'w',
        'axes.linewidth': 1.0,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'figure.dpi': 200,
        'figure.edgecolor': 'k',
        'figure.facecolor': 'k',
        'figure.figsize': [12.8, 7.15],
        'font.family': ['serif'],
        'font.serif': ['Computer Modern Roman'],
        'patch.edgecolor': 'white',
        'savefig.dpi': 200,
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

    matplotlib.style.use(default_style)


def create_scene(with_axes=False, xlim=XLIM, ylim=YLIM):
    """
    Create a new scene.

    :param with_axes: if True, draw the x and y axes (spines)

    :param xlim: a tuple (xmin, xmax)

    :param ylim: a tuple (ymin, ymax)

    :return:
      (fig, ax): instance of Figure and instance of Axes.

    """

    fig, ax = plt.subplots()
    if not with_axes:
        ax.set_axis_off()

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')

    return fig, ax


def render_scene(scene, fig):
    """
    Manage the rendering of the entire scene.

    Each scene corresponds to a table of the form

    ======== =======
    Duration Actions
    ======== =======
    d_1      [a_11, ..., a_1m]
    ...      ...
    d_n      [a_n1, ..., a_nm]
    ======== =======

    Each line of the table is a *part* of the scene.

    Each `d_i` is a duration in seconds.

    The `n` parts of the scene are executed *sequentially*.

    Each line of the `Actions` column is a list of actions *to be executed simultaneously*; i.e., `a_11, ...,
    a_1m` are executed concurrently in a part of the scene that lasts for `d_1` seconds.

    The total duration of the scene, then, is the sum of all durations `d_1 + ... + d_n`.

    TODO: Include example here.

    :param scene: The specification of the scene, as described above. The Python representation of a scene is as
    *a list of dictionaries*. Each line of the table is represented by a `dict` with keys `duration` and `actions`.
    The value of `actions` is a list of action objects -- i.e., instances of classes derived from the `DoAnimation`
    class.

    :param fig: The `Figure` instance where the scene is rendered.

    :return: An instance of `FuncAnimation` to render the scene. This instance can be used to show or to save the scene.

    """

    # Use the first axes of Figure instance as default
    default_ax = fig.get_axes()[0]

    # Inform actions of their cues etc.
    # Also, get number of last frame of this scene
    last_frame_no = cue_actions(default_ax, scene)

    # Build a function to be called by `FuncAnimation` to render the entire scene
    # Note that this uses lexical scoping to access the `scene` variable
    def animation_manager(current_frame):
        """
        Function to be called by `FuncAnimation`.

        Find which part of the scene must be executed at the current frame and call the corresponding action objects.

        **Attention:** this is the **first time** that frame numbers are converted from *scene* referential to *part*
        referential. The action objects are called with the converted frame numbers (i.e., wrt *part* referential).

        :param current_frame: number of current frame (wrt to the beginning of the scene), to be passed by
        `FuncAnimation`.

        """

        nonlocal scene

        # Determine which part must be executed at the current frame
        for part in scene:
            if part['end_frame_no'] > current_frame:
                current_part = part
                # Convert number of current frame in scene to number of current frame in part
                current_frame_in_part = current_frame - part['start_frame_no'] + 1
                break

        # Call action objects for the current part
        for action in current_part['actions']:
            action(current_frame_in_part)

    # Finally, call `FuncAnimation` with our `animation_manager` function
    rendered_scene = FuncAnimation(
            fig,
            animation_manager,
            interval=INTERVAL,
            frames=int(last_frame_no)
    )

    return rendered_scene


def cue_actions(default_ax, scene):
    """
    Calculate start and end frame numbers for each action in the scene. Inform actions of the default ax where to
    draw (in case the action object was created without one).

    :param default_ax:

    :param scene:

    :return: number of the last frame of the scene.

    """
    last_frame_no = 0
    for part in scene:

        # Calculate start_frame and end_frame for each part of the scene and store values in the dictionary for the part
        part['start_frame_no'] = last_frame_no + 1
        part['end_frame_no'] = part['start_frame_no'] + part['duration'] * FPS

        for action in part['actions']:
            # Inform the action object about the ax where to draw (if an ax was already specified when the action
            # object was created, then the action object will know to ignore this call)
            action.set_default_ax(default_ax)

            # Inform each action object about the start and end frames of the part where it is contained
            action.set_cues(
                    part['start_frame_no'],
                    part['end_frame_no']
            )

            # Make each action object initialize its effects, because those effects usually need info about start
            # frame, end frame, and duration of the part of the scene where they appear
            action.init_effect()

        last_frame_no = part['end_frame_no']
    return last_frame_no