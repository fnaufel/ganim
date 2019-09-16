"""
Actions involving lines: segments, vectors etc
"""

from matplotlib import lines
from matplotlib.transforms import Affine2D

from ganim.elements import DoElement


class DoLineSegment(DoElement):
    """
    Class to draw a line segment, with various options of animation effects.

    * **Positional arguments:**

        * `(x0, y0)`: a tuple representing the initial point

        * `(x1, y1)`: a tuple representing the final point

    * **Keyword arguments:**

        * `point_a`: `(x0, y0)` (if not specified as a positional arg)

        * `point_b`: `(x1, y1)` (if not specified as a positional arg)

        * `effect`: 'None' | 'grow' | 'shrink' | 'fadein' | 'fadeout'

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

        # To be used by 'grow' and 'shrink' effects
        self.grow_factor = None

    def define_effects_dict(self):
        """
        Define dictionary. Keys are names of effects, values are methods to implement the effects ('init': method to
        initialize effect, 'run': method to apply effect).

        """

        super().define_effects_dict()

        line_effects = {
            'None': {'init': None, 'run': self.show},
            'grow': {'init': self.init_grow, 'run': self.grow},
            'shrink': {'init': self.init_grow, 'run': self.shrink},
        }

        self.effects.update(line_effects)

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        :return: new artist to be drawn.

        """

        return lines.Line2D([self.xa, self.xb], [self.ya, self.yb], **self.artist_kwargs)

    def draw_element(self):
        """
        Remove previous form of the element, draw current form of the element, and update self.artist.

        """

        self.remove_artist()
        self.artist = self.new_artist
        self.ax.add_line(self.artist)

    def show(self, current_frame_in_part):
        """
        Make entire line to be drawn.

        :return: artist (line) to be drawn.

        """

        # Default transform
        self.transform = self.ax.transData
        return self.make_new_artist()

    def init_grow(self):
        """
        Compute initial info necessary to implement grow effect.

        """

        # During execution of this action, this factor will be multiplied by the current frame number to give the
        # current scale of the segment to be drawn
        self.grow_factor = 1 / self.total_no_of_frames

    def grow(self, current_frame_in_part):
        """
        Make line: part of the segment, from initial point to a point corresponding to the current frame.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        :return: artist (line) to be drawn.
        """

        scale = (current_frame_in_part + 1) * self.grow_factor
        self.artist_kwargs['transform'] = Affine2D().scale(scale) + \
                    Affine2D().translate(self.xa * (1 - scale), self.ya * (1 - scale)) + \
                    self.ax.transData

        return self.make_new_artist()

    def shrink(self, current_frame_in_part):
        """
        Make line: part of the segment, from initial point to a point corresponding to the current frame.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        :return: artist (line) to be drawn.
        """

        scale = 1 - (current_frame_in_part + 1) * self.grow_factor
        self.artist_kwargs['transform'] = Affine2D().scale(scale) + \
                    Affine2D().translate(self.xa * (1 - scale), self.ya * (1 - scale)) + \
                    self.ax.transData

        return self.make_new_artist()
