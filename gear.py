"""The Drivetrain class represents a Drivetrain."""

from typing import List


class Drivetrain(object):
    """Create a Drivetrain."""

    def __init__(self, chainring: int = None, cog: int = None, rim: int = None, tire: int = None):
        """Construct a Drivetrain.

        :chainring: Number of teeth on the forward (pedaled) gear.
        :cog: Number of teeth on the rear (wheel) cassette.
        :rim: Rim diameter in inches.
        :tire: Tire diameter in inches.

        """
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

        print(
            f"Constructing a Drivetrain with a chainring of {chainring}, a cog of {cog}, a rim diameter of {rim} inches, and a tire diameter of {tire} inches."
        )

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

    @property
    def rim(self):
        """Getter method for the 'rim' property."""
        pass

    @rim.setter
    def rim(self):
        """Setter method for the 'rim' property."""
        pass

    @property
    def tire(self):
        """Setter method for the 'tire' property."""
        pass

    @tire.setter
    def tire(self):
        """Setter method for the 'tire' property."""
        pass

    def ratio(self) -> int:
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        return ratio

    def gear_inches(self) -> int:
        """Calculate the gear inches (commonly used in the US)."""
        ratio = (self._rim + (self._tire * 2)) * self.ratio()
        return ratio

    def diameters(self) -> List:
        """For each wheel, calculate the diameter."""
        # Can't iterate over Drivetrain objects...
        result = [self._rim + (self._tire * 2) for wheel in self]
        return result


gear = Drivetrain(chainring=52, cog=11, rim=26, tire=1.5)
print(f"Gear ratio is {gear.ratio()}, and gear inches is {gear.gear_inches()}.")

gear = Drivetrain(chainring=30, cog=27, rim=24, tire=1.25)
print(f"Gear ratio is {gear.ratio()}, and gear inches is {gear.gear_inches()}.")
