"""The Gear class represents a Gear."""


class Gear(object):
    """Create a Gear."""

    def __init__(self, chainring: int = None, cog: int = None, rim: int = None, tire: int = None):
        """Construct a Gear.

        :chainring: Number of teeth on the forward (pedaled) gear.
        :cog: Number of teeth on the rear (wheel) cassette.

        """
        self._chainring = chainring
        self._cog = cog

        print(f"Constructing a Gear with a chainring of {chainring}, a cog of {cog}.")

    @property
    def chainring(self) -> int:
        """Getter method for the 'chainring' property."""
        return self._chainring

    @chainring.setter
    def chainring(self, chainring: int = None) -> None:
        """Setter method for the 'chainring' property."""
        self._chainring = chainring

    @property
    def cog(self) -> int:
        """Getter method for the 'cog' property."""
        return self._cog

    @cog.setter
    def cog(self, cog: int = None):
        """Setter method for the 'cog' property."""
        self._cog = cog

    def ratio(self) -> int:
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        # print(f"Ratio is {self.ratio()}.")
        return ratio

    # print(f"Ratio is {self.ratio()}.")


# __import__("pdb").set_trace()

gear = Gear(chainring=52, cog=11)
print(gear.ratio())

gear = Gear(chainring=30, cog=27)
print(gear.ratio())
