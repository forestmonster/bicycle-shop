"""The Gear class represents a Gear."""


class Gear(object):
    """Create a Gear."""

    def __init__(self, chainring, cog, rim, tire):
        """Construct a Gear.

        :chainring: Integer. Number of teeth on the forward (pedaled) gear.
        :cog: Integer. Number of teeth on the rear (wheel) cassette.
        :rim: Integer. Rim diameter.
        :tire: Integer. Tire diameter.

        """
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire
        print(
            f"Creating Gear with a chainring of {self._chainring}, a cog of",
            f"{self._cog}, a rim of {self._rim}, and a tire diameter of",
            f"{self._tire}.",
        )
        self.ratio()
        self.gear_inches()

    def ratio(self):
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        print(f"Ratio is {ratio}.")
        return ratio

    def gear_inches(self):
        """Calculate the gear inches."""
        gear_inches = self.ratio() * (self._rim + (self._tire * 2))
        print(f"Gear inches is {gear_inches}.")
        return gear_inches


gear = Gear(chainring=52, cog=11, rim=26, tire=1.5)

gear = Gear(chainring=30, cog=27, rim=19, tire=1.5)
