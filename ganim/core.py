"""
Core module for ganim.

"""

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


class Scene(object):

    def __init__(self, with_axes=False, xlim=XLIM, ylim=YLIM):
        """
        Create a new, empty scene.

        :param bool with_axes: if True, draw the x and y axes (spines)

        :param xlim: a tuple (xmin, xmax)

        :param ylim: a tuple (ymin, ymax)

        """

        self.fig, self.ax = plt.subplots()

        if not with_axes:
            self.ax.set_axis_off()

        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_aspect('equal')

        self.last_part_no = -1
        self.parts = []
        self.last_frame_no = -1
        self.rendered_scene = None

    def add_part(self, script, duration):
        """
        Add a new part to this scene.

        A scene may have one or more parts, which are executed *sequentially*; i.e., part 0 must finish executing
        before part 1 begins execution.

        A part is specified by a *script*, which consists of a *list of actions* (i.e., instances of `DoElement` or
        its subclasses), all of which are executed *concurrently*. The specification of a part also has a *duration*
        in seconds.

        The first part is numbered 0.

        :param list script:

        :param int|float duration:

        """
        if not script:
            raise ValueError('Part must not be empty.')

        if duration <= 0:
            raise ValueError(f'Duration ({duration}) must be > 0.')

        self.last_part_no += 1

        # We must pass the ax, because the script may contain actions which will use this ax as the default
        part = Part(self.last_part_no, script, duration, self.ax)

        # Store this part in list
        self.parts.append(part)

    def cue_parts(self):
        """
        For each part in the scene: compute start and end frame numbers for the part and for all the actions in the
        part.

        """

        for part in self.parts:
            # Update part with start and end frame numbers for the actions in the part's script
            part.cue(self.last_frame_no)
            # Update last taken frame number of the scene with last frame number of the part we just cued
            self.last_frame_no = part.last_frame_no

    def scene_ticker(self):
        """
        Returns a list of tuples of the form (part number, frame number), one tuple for each frame of the scene.

        It does this by concatenating the tickers of the parts comprising the scene.

        :return list[tuple[int, int]]:

        """

        ticker = []

        for part in self.parts:
            ticker = ticker + part.get_ticker()

        return ticker

    def remove_artists_in_part(self, part_no):
        """
        Remove those elements that should not stay beyond the end of the part.

        :param part_no: part number to process.

        """
        for action in self.parts[part_no].cued_actions:
            if not action.stay:
                action.remove_artist()

    def render(self):
        """
        Render the scene.

        All parts must be cued first. Then we build an inner function --- the animation_manager --- to be passed to
        FuncAnimation, which does the actual rendering.

        """

        self.cue_parts()

        ################################################################################################################

        def animation_manager(tick):
            """
            A driver for the actions to be executed in the scene.

            Depending on the current value of the ticker (part number, frame number), it calls the appropriate actions.

            :param tuple[int, int] tick: (part number, frame number in part)

            """

            nonlocal self

            part_no, frame_no_in_part = tick

            current_part = self.parts[part_no]

            # Run actions for this part
            for cued_action in current_part.cued_actions:
                if cued_action.start_frame_in_part <= frame_no_in_part <= cued_action.end_frame_in_part:
                    # The action may have been specified with a nonzero `start_after` value. In this case, in order
                    # to preserve the timing of the action's effect, we must 'fool' the action to make it think the
                    # current frame value is 0 when it is actually the value of `start_after`. This is done by
                    # subtracting the `start_after` value from the current frame number and calling the action with
                    # the resulting value.
                    frame_no_since_start = frame_no_in_part - cued_action.start_frame_in_part
                    cued_action(frame_no_since_start)

            # Remove elements from the previous part that should not stay until the end of the scene
            if part_no > 0 and frame_no_in_part == 0:
                self.remove_artists_in_part(part_no - 1)

        ################################################################################################################

        # Do it!
        # For some obscure reason, things broke when I passed the ticker as an iterator, so now scene_ticker() is a list
        self.rendered_scene = FuncAnimation(
                self.fig,
                animation_manager,
                interval=INTERVAL,
                frames=self.scene_ticker()
        )

    def save(self, filename):
        """
        Save the rendered scene to a file.

        :param str filename:
        """

        self.rendered_scene.save(filename)


class Part(object):

    def __init__(self, number, script, duration, default_ax):
        """
        A part of the scene.

        :param int number: first part is 0.

        :param list script: list of actions to be executed concurrently in this part.

        :param float duration: in seconds.

        :param default_ax: instance of matplotlib.axes.Axes

        """

        self.number = number
        self.script = script
        self.duration = duration
        self.default_ax = default_ax

        self.start_frame_no = None
        self.last_frame_no = None
        self.cued_actions = []

    def cue(self, last_taken_frame_no):
        """
        Compute cues for this part and for the actions it contains.

        **NOTE:**

        * The cues for the *part* are frame numbers relative to the *beginning of the scene*.

        * The cues for the *actions* are frame numbers relative to the *beginning of the part*.

        :param int last_taken_frame_no: number of the last frame of the scene used by the previous part.

        """

        # Picking up after the last frame of previous part
        self.start_frame_no = last_taken_frame_no + 1

        # When computing the last frame number of this part, ignore the actions' `start_after` and `end_at`
        # attributes, because the part's total duration (as specified with the script) has precedence
        self.last_frame_no = self.start_frame_no + self.duration * FPS - 1

        for action in self.script:

            # Starting frame of this action (beginning of part is zero)
            if action.args['start_after'] is None:
                start_frame_in_part = 0
            else:
                start_frame_in_part = action.args['start_after'] * FPS

            # Ending frame of this action (beginning of part is zero)
            if action.args['end_at'] is None:
                end_frame_in_part = self.last_frame_no - self.start_frame_no
            else:
                end_frame_in_part = action.args['end_at'] * FPS - 1

            # Store cued action in list field
            # Again, note we need to pass the default ax, as the action may have been scripted without an explicit ax
            action.cue(start_frame_in_part, end_frame_in_part, self.default_ax)
            self.cued_actions.append(action)

    def get_ticker(self):
        """
        Returns the ticker for this part.

        The ticker is a list of tuples of the form (part number, frame number), to be used by FuncAnimation.

        :return list[tuple[int, int]]:

        """

        # Range from 0 to total of frames in part
        frames = range(self.last_frame_no - self.start_frame_no + 1)
        part_no = [self.number] * len(frames)

        return list(zip(part_no, frames))
