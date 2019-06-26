
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
            'ax': None,
            'start_after': None,
            'end_at': None,
            'stay': True,
            'effect': None,
            'linewidth': 2.0,
            'color': 'w'
        }

        if kwargs:
            self.args.update(kwargs)

        # Store the ax (possibly None) in a field
        # If None, the default ax will be provided elsewhere
        self.ax = self.args['ax']

    def init_effect(self, total_no_of_frames):
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

    def draw_element(self, new_artist):
        raise NotImplementedError

    def remove_artist(self):
        raise NotImplementedError
