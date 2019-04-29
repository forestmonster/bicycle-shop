"""The Gear class represents a Gear."""


class Gear(object):
    """Create a Gear."""

    def __init__(self, chainring, cog):
        """Construct a Gear.

        :chainring: Integer. Number of teeth on the forward (pedaled) gear.
        :cog: Integer. Number of teeth on the rear (wheel) cassette.

        """

        @property
        def chainring():
            self._chainring = chainring
            return chainring

        @property
        def cog():
            self._cog = cog
            return cog

        print(
            f"Creating Gear with a chainring of {self.chainring}, a cog of",
            f"{self.cog}.",
        )
        print(f"Ratio is {self.ratio()}.")

    def ratio(self):
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        return ratio


gear = Gear(chainring=52, cog=11)

gear = Gear(chainring=30, cog=27)
