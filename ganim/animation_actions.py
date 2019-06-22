
class DoElement(object):
    """
    Base class for all animation actions.

    To be more flexible, all of the arguments are passed to the constructor as keyword arguments. Arguments common to
    all animation actions are dealt with here in this base class.

    Also to be more flexible, those arguments are stored in a field called `args`, of type `dict`. This allows us to
    use the `update` method to change keys and values.

    Each instance of this class and its derived classes has a `__call__` method, to make the execution of the
    animation action more straightforward. One of the advantages of this is that when this method is invoked multiple
    times during the animation, the execution can use the state saved in the fields.

    """

    def __init__(self, **kwargs):

        # Defaults for all animation actions
        self.args = {
            'effect': None,
            'linewidth': 1.0,
            'color': 'w'
        }

        if kwargs:
            self.args.update(kwargs)

    def set_part_cues(self, start, end):
        """
        The function responsible for rendering the scene will inform this action object of its cues (i.e.,
        the start and end frame numbers of the part) by calling this method.

        The number of the start frame, the number of the end frame, and the total number of frames are stored as
        fields.

        :param start: number of start frame.

        :param end: number of end frame.

        """

        self.start_frame_no = start
        self.end_frame_no = end
        self.total_no_of_frames = end - start

    def set_default_ax(self, ax):
        """
        Only if the axes where drawing should take place were not specified at construction time, this method must be
        called to do it.

        :param ax:
        """
        if self.args.get('ax') is None:
            self.args['ax'] = ax

    def init_effect(self):
        pass

    def __call__(self, *args, **kwargs):
        pass
