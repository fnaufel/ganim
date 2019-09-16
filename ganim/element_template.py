"""
This file contains a template for a developer to implement a new animation action (i.e., a new element to be drawn)
as a subclass of `ganim.elements.DoElement`.

For a full implementation, see, e.g., class `ganim.line_elements.DoLineSegment`.

"""

# Import necessary classes and functions (e.g., lines)
from matplotlib import lines

# Import transformations
from matplotlib.transforms import Affine2D

from ganim.elements import DoElement


class DoNewElement(DoElement):
    """
    Class to draw a <new element>, with various options of animation effects.

    """

    def __init__(self, *args, **kwargs):
        """
        * **Positional arguments:**

            * ...

        * **Keyword arguments:**

            * ...

            * `effect`: 'None' | ...

            * `color`

            * `linewidth`

            * ...

        """

        # This command must be included: super() will store kwargs in the self.args dictionary and in the
        # self.artist.kwargs dictionary
        super().__init__(*args, **kwargs)

        # TODO: add more initialization commands here

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
            'effect1': {'init': self.init_effect1, 'run': self.run_effect1},
            # TODO: add other effects:
            # 'name': {'init': init_effect1, 'run': run_effect1},
            # ...
        }

        # Update dictionary of effects with the effects created above
        self.effects.update(element_effects)

    def show(self, current_frame_in_part):
        """
        Make artist to be drawn.

        :return: artist to be drawn.

        """

        # Default transform (do nothing, just convert data coordinates to pixel coordinates)
        self.transform = self.ax.transData

        # If this method only draws the plain artist (the usual case), this is enough
        # The current_frame_in_part parameter value is not needed
        return self.make_new_artist()

    def init_effect1(self):
        """
        Initialize this effect, using (1) information in self.args and in other fields and (2) information provided
        by the cueing:

        * self.start_frame_in_part

        * self.end_frame_in_part

        * self.total_no_of_frames

        Use fields to store information to be used by the effect.

        """

        # TODO: compute info that will be necessary for the effect. Save in instance fields

    def run_effect1(self, current_frame_in_part):
        """
        Apply this effect.

        This will usually involve (1) computing a transformation based on the current frame number in part and on the
        desired effect, (2) assigning the transformation to self.artist_kwargs['transform'], (3) adding other
        key-value pairs to the self.artist_kwargs dictionary, and (4) calling self.make_new_artist(),
        returning whatever it returns.

        :param current_frame_in_part: number of the current frame with respect to beginning of part.

        :return: new artist to be drawn.

        """

        # TODO: compute values for this frame, based on current_frame_in_part and instance fields pertaining to this
        #  effect

        # TODO: compute transformation, usually using self.ax.transData
        self.artist_kwargs['transform'] = None # TODO

        # Build and return new artist for this frame
        return self.make_new_artist()

    def make_new_artist(self):
        """
        Compute new form of the element to be drawn, using information from self's fields.

        Usually, this will mean creating a new artist and applying a transformation to it, based on the chosen effect.

        Sometimes, the element to be drawn will consist of a *list* of artists.

        :return: new artist --- or list of artists --- to be drawn.

        """

        return None
        # TODO: create and return artist --- or list of artists --- to be drawn on this frame. Will use instance fields
        #  and possibly **self.artist_kwargs

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
