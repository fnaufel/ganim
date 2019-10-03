"""
Points.
"""

# Import transformations
from matplotlib.lines import Line2D

from ganim.elements import DoElement


class DoPoint(DoElement):
    """
    Class to draw a 2D point, with various options of animation effects.

    """

    def __init__(self, *args, **kwargs):
        """
        * **Positional arguments:**

            * `(x0, y0)`: a tuple with the point's coordinates

        * **Keyword arguments:**

            * `coords`: `(x0, y0)` (if not specified as a positional arg)

            * `effect`: 'None' | 'fadein' | 'fadeout'

            * `color`

            * `markersize`

        """

        # Add default properties to artist
        self.default_artist_kwargs = {
            'color': 'w',
            'markersize': 4.0,
            'marker': 'o',
        }

        # This command must be included: super() will store kwargs in the self.args dictionary and in the
        # self.artist.kwargs dictionary
        super().__init__(*args, **kwargs)

        if len(args) == 1:
            # Coordinates may be given as positional args...
            self.x0, self.y0 = args[0]
        else:
            # ...or coordinates may be given as kwargs
            self.x0, self.y0 = self.args['coords']

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

        # Create effects dict for this class
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

        new_point = Line2D(
                [self.x0],
                [self.y0],
                **self.artist_kwargs
        )

        return new_point

    def draw_element(self):
        """
        Remove previous form of the element, draw current form of the element, and update self.artist.

        The following implementation will usually be enough.

        """

        self.remove_artist()
        self.artist = self.new_artist

        self.ax.add_line(self.artist)
