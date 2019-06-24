
class DoElement(object):
    """
    Base class for all animation actions.

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
            'effect': None,
            'linewidth': 1.0,
            'color': 'w'
        }

        if kwargs:
            self.args.update(kwargs)

    def set_cues(self, start, end):
        """
        This method is called by the function responsible for rendering the scene to inform this action object of its
        cues (i.e., the start and end frame numbers of this action's part, altered by this action object's
        start_after and end_at values).

        The number of the start frame, the number of the end frame, and the total number of frames are stored as
        fields.

        :param start: number of start frame of the part (wrt to the beginning of the scene)

        :param end: number of end frame of the part (wrt to the beginning of the scene)

        """

        # TODO: calculate start frame, end frame and duration, now taking into consideration start_after and end_at.
        #  Set self.start_frame_no, self.end_frame_no, self.total_no_of_frames

        self.start_frame_no = start
        self.end_frame_no = end
        self.total_no_of_frames = end - start

    def set_default_ax(self, ax):
        """
        Only if the axes were not specified at construction time, this method will set them.

        :param ax:
        """
        if self.args.get('ax') is None:
            self.args['ax'] = ax

    def init_effect(self):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        """
        Execute animation action: draw the element on the current frame, using the specified effect. This method will
        be called by the `render_scene` method once for each frame.

        **Attention:**

        The first positional argument will the current frame number, as counted from the beginning of the part (not
        from the beginning of the scene!!!). It does *not* matter to this element when in the scene it will be drawn,
        but it matters when in the *part* it will be drawn, because the element has to honor `start_after` and
        `end_at` times, which are specified by the user wrt to the beginning of the part.

        :param args: list of positional arguments.

        :param kwargs: list of keyword arguments. May be empty.

        """
        raise NotImplementedError
