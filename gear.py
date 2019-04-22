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

    def ratio(self):
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        return ratio


gear = Gear(chainring=52, cog=11)
ratio = gear.ratio()
print(f"Creating Gear with a chainring of {gear._chainring} and a cog of {gear._cog}.")
print(f"Ratio is {ratio}.")

gear = Gear(chainring=30, cog=27)
ratio = gear.ratio()
print(f"Creating Gear with a chainring of {gear._chainring} and a cog of {gear._cog}.")
print(f"Ratio is {ratio}.")
