"""The Drivetrain class represents a Drivetrain."""

from typing import List


class Drivetrain:
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
        self._wheel = self.wheelify(rim=self._rim, tire=self._tire)

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
    def rim(self, rim: int = None):
        """Setter method for the 'rim' property."""
        self._rim = rim

    @property
    def tire(self) -> int:
        """Getter method for the 'tire' property."""
        pass

    @tire.setter
    def tire(self):
        """Setter method for the 'tire' property."""
        pass

    def wheelify(self, rim, tire) -> List:
        """For each wheel, calculate the diameter."""
        # Return an array of one wheel.
        result = [rim + (tire * 2)]
        return result

    def ratio(self) -> int:
        """Calculate the gear ratio."""
        ratio = self._chainring / self._cog
        return ratio

    def gear_inches(self) -> int:
        """Calculate the gear inches (commonly used in the US)."""
        ratio = (self._rim + (self._tire * 2)) * self.ratio()
        return ratio


gear = Drivetrain(chainring=52, cog=11, rim=26, tire=1.5)
print(f"Gear ratio is {gear.ratio()}, and gear inches is {gear.gear_inches()}.")

gear = Drivetrain(chainring=30, cog=27, rim=24, tire=1.25)
print(f"Gear ratio is {gear.ratio()}, and gear inches is {gear.gear_inches()}.")


class RevealingReferences:
    @property
    def wheels(self):
        """Getter method for the 'wheels' instance attribute."""
        return wheelify(data)

    def wheelify(self, data):
        wheel = Wheel(rim=5, tire=10)
        return wheel


class Wheel:
    """Bicycles have Wheels."""

    def __init__(self, rim: int = None, tire: int = None) -> None:
        """Construct a Wheel for a bicycle."""
        self._rim = rim
        self._tire = tire
        self._wheelsize = self._rim + (self._tire * 2)

    @property
    def size(self):
        return self._wheelsize
