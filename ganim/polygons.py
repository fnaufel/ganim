"""
Polygons.
"""

from matplotlib.colors import to_rgba
from matplotlib.patches import Polygon

from ganim.elements import DoElement
from ganim.line_elements import DoLineSegment


class DoPolygon(DoElement):
    """
    Class to draw a polygon.

    """

    def __init__(self, *args, **kwargs):
        """
        * **Positional arguments:**

            * `vertex_list`: list or tuple of at least 3 points.

        * **Keyword arguments:**

            * `vertices`: (if not specified as positional arg).

            * TODO: `visible_vertices`: if True, draw points at vertices (default: False).

            * TODO: `vertex_colors`: if `visible_vertices` is True, a list of colors for the vertices. (default: 'w').

            * `edgecolor`: single color for all sides (default: 'w').

            * `facecolor`: color of interior of polygon (default: 'y').

            * `edgealpha`: default: 1.0.

            * `facealpha`: default: 0.5.

            * `fill`: if True, polygon is filled with `facecolor` (default: True).

            * `effect`: 'None' | ...

            * `linewidth`: default: 2.0.

        """

        self.default_artist_kwargs = {
            'facecolor': 'y',
            'edgecolor': 'w',
            'fill': True,
            'edgealpha': 1.0,
            'facealpha': 0.5,
            'linewidth': 2.0,
        }

        # This command must be included: super() will store kwargs in the self.args dictionary and in the
        # self.artist.kwargs dictionary
        super().__init__(*args, **kwargs)

        # Adjust alpha of edges
        self.artist_kwargs['edgecolor'] = to_rgba(
                self.artist_kwargs['edgecolor'],
                float(self.artist_kwargs['edgealpha'])
        )

        # Adjust alpha of face
        self.artist_kwargs['facecolor'] = to_rgba(
                self.artist_kwargs['facecolor'],
                float(self.artist_kwargs['facealpha'])
        )

        # Remove keys that matplotlib's Polygon artist does not understand
        del self.artist_kwargs['edgealpha'], self.artist_kwargs['facealpha']

        # Get vertices
        if len(args) == 1:
            self.vertices = args[0]
        else:
            self.vertices = kwargs['vertices']

        if len(self.vertices) < 3:
            raise ValueError('Polygon must have 3 or more vertices.')

        # Build line segments (not for drawing, but for other operations -- e.g., building angles)
        sides = zip(self.vertices, self.vertices[1:])
        self.sides = [DoLineSegment((a, b), (c, d)) for (a, b), (c, d) in sides]
        self.sides.append(DoLineSegment(self.vertices[0], self.vertices[-1]))

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

        # If this method only draws the plain artist (the usual case), this is enough.
        # The current_frame_in_part parameter value is not needed
        return self.make_new_artist()

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        Usually, this will mean creating a new artist and applying a transformation to it, based on the chosen effect.

        Sometimes, the element to be drawn will consist of a *list* of artists.

        :return: new artist --- or list of artists --- to be drawn.

        """

        polygon = Polygon(
                self.vertices,
                closed=True,
                **self.artist_kwargs
        )

        return polygon
