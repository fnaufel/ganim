from matplotlib import lines
from matplotlib.transforms import Affine2D

from ganim.animation_actions import DoElement


class DoLineSegment(DoElement):
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
        #  Actually, this should be done in superclass.

        if self.args['effect'] == 'grow':
            # This factor will be multiplied by the current frame number to give the current scale
            self.grow_factor = 1 / self.total_no_of_frames

    def __call__(self, *args, **kwargs):
        """
        Execute animation action: draw the segment on the current frame, using the specified effect.

        This method will be called by `FuncAnimation` once for each frame.

        :param args: list of positional arguments. The first argument is the current frame number, as counted from
        the beginning of the part (not from the beginning of the scene!!!).

        :param kwargs: list of keyword arguments. May be empty.

        """

        current_frame_in_part = args[0]

        if self.args['effect'] is None:
            # Draw segment with no animation
            line = lines.Line2D([self.xa, self.xb], [self.ya, self.yb])
            self.draw_plain(line)

        elif self.args['effect'] == 'grow':
            self.grow(current_frame_in_part)

        else:
            raise ValueError(f'Unknown effect: {self.args["effect"]}')

    def grow(self, current_frame_in_part):
        """
        Draw part of the segment, from initial point to a point corresponding to the current frame.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        """

        scale = current_frame_in_part * self.grow_factor
        transform = Affine2D().scale(scale) + \
                    Affine2D().translate(self.xa * (1 - scale), self.ya * (1 - scale)) + \
                    self.args['ax'].transData

        line = lines.Line2D([self.xa, self.xb], [self.ya, self.yb], transform=transform)
        self.draw_plain(line)

    def draw_plain(self, line):
        """
        Draw a plain segment from point_a to point_b.

        :param line:

        """

        line.set_color(self.args['color'])
        line.set_linewidth(self.args['linewidth'])
        self.args['ax'].add_line(line)
