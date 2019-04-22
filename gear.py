"""The Gear class represents a Gear."""


class Gear(object):
    """Create a Gear."""

    def __init__(self, chainring, cog):
        """Construct a Gear.

        :chainring: Integer. Number of teeth.
        :cog: Integer. Number of teeth.

        """
        self._chainring = chainring
        self._cog = cog
        pass
