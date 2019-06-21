from ganim.animation_actions import DoAnimation


class DoLineSegment(DoAnimation):
    """
    Class to draw a line segment, with various options of animation effects.

    """

    def __init__(self, **kwargs):

        super(DoLineSegment, self).__init__(**kwargs)

        # Initial point of the segment
        self.xa, self.ya = self.args['point_a']

        # End point of the segment
        self.xb, self.yb = self.args['point_b']

    def init_effect(self):
        """
        Compute initial info necessary to implement animation affect.

        """

        # TODO: calculate start frame, end frame and duration, now taking into consideration start_after and end_at.
        #  Set self.start_frame_no, self.end_frame_no, self.total_no_of_frames

        if self.args['effect'] == 'grow':
            # Segment will be drawn incrementally, starting at point A, growing towards point B

            # Compute horizontal increment (dx) and vertical increment (dy)
            self.dx = (self.xb - self.xa) / self.total_no_of_frames
            self.dy = (self.yb - self.ya) / self.total_no_of_frames

    def __call__(self, *args, **kwargs):
        """
        Execute animation action: draw the segment on the current frame, using the specified effect.

        This method will be called by `FuncAnimation` once for each frame.

        :param args: list of positional arguments. The first argument is the current frame number, as counted from
        the beginning of the part (not from the beginning of the scene!!!).

        :param kwargs: list of keyword arguments. May be empty.

        """

        current_frame = args[0]

        if self.args['effect'] is None:
            # Draw segment with no animation
            self.draw_plain(
                (self.xa, self.xb),
                (self.ya, self.yb)
            )
        elif self.args['effect'] == 'grow':
            self.grow(current_frame)
        else:
            raise ValueError(f'Unknown effect: {self.args["effect"]}')

    def grow(self, current_frame):
        """
        Draw part of the segment, from initial point to a point corresponding to the current frame.

        :param current_frame:

        """

        # Compute new coordinates of the end of the segment
        x = self.xa + current_frame * self.dx
        y = self.ya + current_frame * self.dy

        self.draw_plain(
            (self.xa, x),
            (self.ya, y)
        )

    def draw_plain(self, point_a, point_b):
        """
        Draw a plain segment from point_a to point_b.

        :param point_a:

        :param point_b:

        """

        self.args['ax'].plot(
                point_a,
                point_b,
                scalex=False,  # This is to prevent the axes size from changing as the segment grows
                scaley=False,  # This is to prevent the axes size from changing as the segment grows
                linewidth=self.args['linewidth'],
                color=self.args['color']
        )
