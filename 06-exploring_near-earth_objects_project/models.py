"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False):
        """Create a new `NearEarthObject`.
        :param designation: designation of the NearEarthObject

        :param name:        registered IAU name for the the NearEarthObject
        :param diameter:    diameter of the NearEarthObject [km]
        :param hazardous:   status of hazardousness for the NearEarthObject
        """
        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name: return f'{self.designation} ({self.name})'
        return f'{self.designation}'

    def __str__(self):
        """Return `str(self)`."""
        def is_haz(cond):
            if cond: return 'is'
            else: return 'is not'
        return f'NearEarthObject {self.fullname} ' \
               f'with diameter {self.diameter:.2f} km ' \
               f'and {is_haz(self.hazardous)} potentially hazardous'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"

    def serialize(self):
        """Return a dictionary of attributes."""
        name    = self.name if self.name else ''
        return {'designation': self.designation, 'name': name, 
                'diameter_km': self.diameter, 'potentially_hazardous': self.hazardous}


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param designation: designation of the NearEarthObject
        :param time:        UTC datetime of the NearEarthObject's close approach
        :param distance:    distance of the NearEarthObject's close approach [au]
        :param velocity:    velocity of the NearEarthObject [km/s]
        """
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f'CloseApproach on {self.time_str} by {self.neo.fullname} will ' \
               f'approach Earth within {self.distance:.2f} au and {self.velocity:.2f}' \
               f' km/s.'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

    def serialize(self):
        """Return a dictionary of attributes."""
        return {'datetime_utc': datetime_to_str(self.time), 'distance_au': self.distance,
                'velocity_km_s': self.velocity}

