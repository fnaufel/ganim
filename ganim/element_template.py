"""
This file contains a template for a developer to implement a new animation action (i.e., a new element to be drawn)
as a subclass of `ganim.elements.DoElement`.

"""

# Import necessary classes and functions (e.g., lines)
from matplotlib import lines

# Import transformations
from matplotlib.transforms import Affine2D

from ganim.elements import DoElement


class DoNewElement(DoElement):
    """
    Class to draw a <new element>, with various options of animation effects.

    * **Positional arguments:**

        * ...

    * **Keyword arguments:**

        * ...

        * `effect`: `None` | ...

        * `color`

        * `linewidth`

        * ...

    """

    def __init__(self, *args, **kwargs):

        # This command must be included: super() will store kwargs in self.args dictionary
        super().__init__(**kwargs)

        # More initialization commands go here...

    def define_effects_dict(self):
        """
        Define effects dictionary.

        Keys are names of effects, values are methods to implement the effects ('init': method to initialize effect,
        'run': method to apply effect).

        'init' methods must return nothing. They should store information in fields.

        'run' methods must return the new artist to be drawn.

        """

        self.effects = {
            'None': {'init': None, 'run': self.show},
            'effect1': {'init': self.init_effect1, 'run': self.run_effect1}
            # ...: ...
        }

    def show(self, current_frame_in_part):
        """
        Make artist to be drawn.

        :return: artist to be drawn.

        """

        # Default transform
        self.transform = self.ax.transData

        # If this method only draws the plain artist (the usual case), this is enough
        # The current_frame_in_part parameter value is not needed
        new_artist = self.make_new_artist()

        return new_artist

    def init_effect1(self):
        """
        Initialize this effect, using (1) information in self.args and in other fields and (2) information provided
        by the cueing:

        * self.start_frame_in_part

        * self.end_frame_in_part

        * self.total_no_of_frames

        Use fields to store information to be used by the effect.

        """

        pass

    def run_effect1(self, current_frame_in_part):
        """
        Apply this effect.

        This will usually involve (1) creating a new artist, (2) computing a transformation based on the current
        frame in part and on the desired effect, and (3) applying the transformation to the new artist.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        :return: new artist to be drawn.

        """

        pass

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        Usually, this will mean creating a new artist and applying a transformation to it, based on the chosen effect.

        :return: new artist to be drawn.

        """

        new_artist = ''  # implement creation of new artist

        return new_artist

    def draw_element(self):
        """
        Remove previous form of the element, draw current form of the element, and update self.artist.

        The following implementation will usually be enough.

        """

        self.remove_artist()
        self.artist = self.new_artist

        # More visual configuration can be applied below, if necessary
        self.artist.set_color(self.args['color'])
        self.artist.set_linewidth(self.args['linewidth'])

        # A specialized add method (e.g., add_line) may be used below instead of add_artist
        self.ax.add_artist(self.artist)
