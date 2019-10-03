"""
Angles.
"""

import numpy as np
from matplotlib.colors import to_rgba
from matplotlib.patches import Wedge, Polygon
from matplotlib.transforms import Affine2D

from ganim.elements import DoElement


class DoAngle(DoElement):
    """
    Class to draw an angle.

    * **Positional arguments:**
    
        * `center`: tuple (x0, y0), center of angle

        * `seg1`: a line segment, instance of DoLineSegment

        * `seg2`: a line segment, instance of DoLineSegment

    * **Keyword arguments:**

        * `center`: (if not specified as a positional arg)

        * `seg1`: (if not specified as a positional arg)

        * `seg2`: (if not specified as a positional arg)

        * `effect`: 'None' | 'fadein' | 'fadeout'

        * `radius`

        * `edgecolor`

        * `facecolor`

        * `edgealpha`: default: 1.0.

        * `facealpha`: default: 0.5.

        * `linewidth`

    """

    def __init__(self, *args, **kwargs):

        # Default properties of angles
        self.default_artist_kwargs = {
            'facecolor': 'yellow',
            'edgecolor': 'w',
            'edgealpha': 1.0,
            'facealpha': 0.1,
            'linewidth': 2.0,
        }

        # super() will store kwargs in the self.args dictionary and in the
        # self.artist.kwargs dictionary
        super().__init__(*args, **kwargs)

        # Adjust alpha of line
        self.artist_kwargs['edgecolor'] = to_rgba(
                self.artist_kwargs['edgecolor'],
                float(self.artist_kwargs['edgealpha'])
        )

        # Adjust alpha of interior
        self.artist_kwargs['facecolor'] = to_rgba(
                self.artist_kwargs['facecolor'],
                float(self.artist_kwargs['facealpha'])
        )

        # Remove keys that matplotlib's Wedge artist does not understand
        del self.artist_kwargs['edgealpha'], self.artist_kwargs['facealpha']

        # Process args
        padded_args = args + (None, None, None)
        self.center, self.seg1, self.seg2 = padded_args[0:3]

        if self.center is None:
            self.center = self.args['center']

        if self.seg1 is None:
            self.seg1 = self.args['seg1']

        if self.seg2 is None:
            self.seg2 = self.args['seg2']

        # Default radius
        self.radius = 1.0
        if 'radius' in kwargs.keys():
            self.radius = kwargs['radius']

        # Get angles of segments wrt x axis
        self.theta1 = self.seg1.angle()
        self.theta2 = self.seg2.angle()

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

        if self.is_right_angle(self.theta1, self.theta2):
            # Right angle: draw square of side radius/2, rotated according to the segments' position
            vertices = np.array(
                    [
                        self.center,
                        (self.center[0] + self.radius / 2, self.center[1]),
                        (self.center[0] + self.radius / 2, self.center[1] + self.radius / 2),
                        (self.center[0], self.center[1] + self.radius / 2),
                    ]
            )
            return Polygon(
                    vertices,
                    closed=True,
                    fill=True,
                    transform=Affine2D().rotate_deg_around(*self.center, self.theta1) +
                              self.ax.transData,
                    **self.artist_kwargs
            )
        else:
            # Not right angle: draw wedge
            return Wedge(
                    self.center,
                    self.radius,
                    self.theta1,
                    self.theta2,
                    **self.artist_kwargs
            )

    @staticmethod
    def is_right_angle(theta1, theta2):
        """
        Check if the difference from theta1 to theta2 is 90 degrees.

        :param theta1: angle of first segment wrt to x axis (in degrees).

        :param theta2: angle of second segment wrt to x axis (in degrees).

        :return: True iff theta2 - theta1 == 90, accounting for the possibility that theta1 is in quadrant 4.

        """

        if theta1 < 270:
            return theta2 == theta1 + 90.0
        else:
            return theta2 == theta1 + 90.0 - 360.0
