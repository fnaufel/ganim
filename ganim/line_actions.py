"""
Actions involving lines: segments, vectors, curves.
"""

from matplotlib import lines
from matplotlib.transforms import Affine2D

from ganim.animation_actions import DoElement


class DoLineSegment(DoElement):
    """
    Class to draw a line segment, with various options of animation effects.

    * **Positional arguments:**

        * `(x0, y0)`: a tuple representing the initial point

        * `(x1, y1)`: a tuple representing the final point

    * **Keyword arguments:**

        * `point_a`: `(x0, y0)` (if not specified as a positional arg)

        * `point_b`: `(x1, y1)` (if not specified as a positional arg)

        * `effect`: `None` | `'grow'`

        * `color`

        * `linewidth`

    """

    def __init__(self, *args, **kwargs):

        # super() will store kwargs in self.args dictionary
        super().__init__(**kwargs)

        if len(args) == 2:
            # End points of the segment may be given as positional args...
            self.xa, self.ya = args[0]
            self.xb, self.yb = args[1]
        else:
            # ...or end points of the segment may be given as kwargs
            self.xa, self.ya = self.args['point_a']
            self.xb, self.yb = self.args['point_b']

        self.grow_factor = None

    def init_effect(self, total_no_of_frames):
        """
        Compute initial info necessary to implement animation affect.

        :param total_no_of_frames: duration of this action in frames.

        """

        if self.args['effect'] == 'grow':
            # During execution of this action, this factor will be multiplied by the current frame number to give the
            # current scale of the segment to be drawn
            self.grow_factor = 1 / total_no_of_frames

    def __call__(self, *args, **kwargs):

        current_frame_in_part = args[0]

        if self.args['effect'] is None:
            # Draw segment with no animation
            line = lines.Line2D([self.xa, self.xb], [self.ya, self.yb])
            self.draw_in_frame(line)

        elif self.args['effect'] == 'grow':
            self.grow(current_frame_in_part)

        else:
            raise ValueError(f'Unknown effect: {self.args["effect"]}')

    def grow(self, current_frame_in_part):
        """
        Draw part of the segment, from initial point to a point corresponding to the current frame.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        """

        scale = (current_frame_in_part + 1) * self.grow_factor
        transform = Affine2D().scale(scale) + \
                    Affine2D().translate(self.xa * (1 - scale), self.ya * (1 - scale)) + \
                    self.ax.transData

        line = lines.Line2D([self.xa, self.xb], [self.ya, self.yb], transform=transform)
        self.draw_in_frame(line)

    def draw_in_frame(self, line):
        """
        Draw a plain segment from point_a to point_b.

        :param line:

        """

        line.set_color(self.args['color'])
        line.set_linewidth(self.args['linewidth'])
        self.ax.add_line(line)
