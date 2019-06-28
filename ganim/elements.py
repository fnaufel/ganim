"""
Base classes for elements.

Elements are geometric entities endowed with animation effects.

"""


class DoElement(object):
    """
    Base class for all 2D animation actions.

    To be more flexible, arguments may be passed to the constructor as keyword arguments. Arguments common to all
    animation actions are dealt with here in this base class.

    Also to be more flexible, those arguments are stored in a field called `args`, of type `dict`. This allows us to
    use the `update` method to change keys and values.

    Each instance of this class and its derived classes has a `__call__` method, to make the execution of the
    animation action more straightforward. One of the advantages of this is that when this method is invoked multiple
    times during the animation, the execution can use the state saved in the instance's fields.

    """

    def __init__(self, *args, **kwargs):

        # Defaults for all animation actions
        self.args = {
            # Ax where to draw
            'ax': None,
            # How many seconds after beginning of part to wait before starting execution
            'start_after': None,
            # Time in seconds after beginning of part when execution must end
            'end_at': None,
            # Should the element stay in the figure after the end of the part?
            'stay': True,
            # Effect to apply to the element
            'effect': 'None',
            'linewidth': 2.0,
            'color': 'w'
        }

        if kwargs:
            self.args.update(kwargs)

        # Store the ax (possibly None) in a field
        # If None, the default ax will be provided elsewhere
        self.ax = self.args['ax']

        # Should element stay in the figure beyond the end of the part?
        self.stay = self.args['stay']

        # Dictionary of effects and their respective methods (to be defined by subclasses)
        self.effects = None

        # Define effects based on subclass implementation
        self.define_effects_dict()

        # Fields to be assigned to by the cue() method
        self.start_frame_in_part = None
        self.end_frame_in_part = None
        self.total_no_of_frames = None

        # Artist drawn in the current frame
        self.artist = None

        # Artist being constructed, to be drawn in the next frame
        self.new_artist = None

        # Transformation to be applied to the artist
        self.transform = None

    def define_effects_dict(self):
        """
        Define dictionary. Keys are names of effects, values are methods to implement the effects.

        Must be implemented by subclass.

        """

        raise NotImplementedError

    def init_effect(self):
        """
        Initialize the effect chosen by the user for this element, if an 'init' method is provided in self.effects.

        """

        method = self.effects[self.args['effect']]['init']
        if method is not None:
            method()

    def __call__(self, current_frame_in_part):
        """
        Execute animation action: draw the element on the current frame, using the specified effect. This method will
        be called once for each frame.

        **Attention:**

        The first argument will the current frame number, as counted from the beginning of the part (not from the
        beginning of the scene!!!). It does *not* matter to this element when in the scene it will be drawn,
        but it matters when in the *part* it will be drawn, because the element has to honor `start_after` and
        `end_at` times, which are specified by the user wrt to the beginning of the part.

        :param current_frame_in_part:

        """

        method = self.effects[self.args['effect']]['run']
        self.new_artist = method(current_frame_in_part)
        self.draw_element()

    def cue(self, start_frame_in_part, end_frame_in_part, default_ax):
        """
        Assign cueing and drawing information (frame numbers and default ax).

        :param int start_frame_in_part: number of the frame where the action should start drawing, already honoring a
            possible `start_after` value in the script.

        :param int end_frame_in_part: number of the frame where the action should stop drawing, already honoring a
            possible `end_at` value in the script.

        :param default_ax: instance of matplotlib.axes.Axes.

        """

        self.start_frame_in_part = start_frame_in_part
        self.end_frame_in_part = end_frame_in_part
        self.total_no_of_frames = end_frame_in_part - start_frame_in_part + 1

        # Now we have the information needed to initialize the action's effects, which may depend on the total number
        # of frames the action will take
        self.init_effect()

        # If the user did not specify an ax where the action should draw, we provide the default ax
        if self.ax is None:
            self.ax = default_ax

    def draw_element(self):
        """
        Remove previous form of the element, draw current form of the element, and update self.artist.

        """

        self.remove_artist()
        self.artist = self.new_artist
        self.artist.set_color(self.args['color'])
        self.artist.set_linewidth(self.args['linewidth'])
        self.ax.add_artist(self.artist)

    def remove_artist(self):
        """
        Remove the element from the ax (i.e., from the scene), if the element exists.

        """

        if self.artist:
            self.artist.remove()

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        Usually, this will mean creating a new artist and applying a transformation to it, based on the chosen effect.

        :return: new artist to be drawn.

        """

        raise NotImplementedError
