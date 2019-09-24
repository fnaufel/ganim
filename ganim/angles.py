"""
Angles.
"""

# Import necessary classes and functions (e.g., lines)
from matplotlib import lines
from matplotlib.patches import Wedge

from ganim.elements import DoElement
from ganim.util import segment_intersection


class DoAngle(DoElement):
    """
    Class to draw an angle.

    * **Positional arguments:**

        * `seg1`: a line segment, instance of DoLineSegment

        * `seg2`: a line segment, instance of DoLineSegment

    * **Keyword arguments:**

        * `seg1`: (if not specified as a positional arg)

        * `seg2`: (if not specified as a positional arg)

        * `effect`: 'None' | 'fadein' | 'fadeout'

        * `radius`

        * `edgecolor`

        * `facecolor`

        * `alpha`

        * `linewidth`

    """

    def __init__(self, *args, **kwargs):

        # super() will store kwargs in the self.args dictionary and in the
        # self.artist.kwargs dictionary
        super().__init__(*args, **kwargs)

        if len(args) == 2:
            self.seg1, self.seg2 = args[0:2]
        else:
            self.seg1 = self.args['seg1']
            self.seg2 = self.args['seg2']

        # Remove color property from kwargs (for angles, it overrides edgecolor and facecolor)
        del self.artist_kwargs['color']

        # Default radius
        self.radius = 1.0

        # Compute intersection point of segments (error if segments don't touch)
        self.center = segment_intersection(self.seg1, self.seg2)
        if self.center is None:
            raise ValueError('Segments do not intercept at an angle.')

    # TODO: continue



    def define_effects_dict(self):
        """
        Define effects dictionary.

        Keys are names of effects, values are methods to implement the effects ('init': method to initialize effect,
        'run': method to apply effect).

        'init' methods must return nothing. They should store information in fields.

        'run' methods must return the new artist to be drawn.

        """

        # Ask superclass to initialize effects dict
        super().define_effects_dict()

        # Create effects dict for this class.
        # Some effects are created and handled by the DoElement superclass, as such effects do not depend on the
        # nature of the element. Examples are fadein and fadeout. You don't have to worry about them
        element_effects = {
            'None': {'init': None, 'run': self.show},
        }

        # Update dictionary of effects with the effects created above
        self.effects.update(element_effects)

    def show(self, current_frame_in_part):
        """
        Make artist to be drawn.

        :return: artist to be drawn.

        """

        # If this method only draws the plain artist (the usual case), this is enough
        # The current_frame_in_part parameter value is not needed
        return self.make_new_artist()

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        Usually, this will mean creating a new artist and applying a transformation to it, based on the chosen effect.

        Sometimes, the element to be drawn will consist of a *list* of artists.

        :return: new artist --- or list of artists --- to be drawn.

        """

        return Wedge(
                self.center,
                self.radius,
                self.seg1_inclination,
                self.seg2_inclination,
                **self.artist_kwargs
        )

    def draw_element(self):
        """
        Remove previous form of the element, draw current form of the element, and update self.artist.

        The following implementation will usually be enough.

        If you don't need to change anything in this implementation, you may safely delete this method, as this is
        precisely the code the superclass implements for it.

        """

        self.remove_artist()
        self.artist = self.new_artist

        #  TODO: a specialized add method (e.g., add_line) may be used below instead of add_artist
        if isinstance(self.artist, list):
            for a in self.artist:
                self.ax.add_artist(a)
        else:
            self.ax.add_artist(self.artist)
