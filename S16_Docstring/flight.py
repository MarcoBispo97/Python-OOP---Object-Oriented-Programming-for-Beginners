class Flight:
    """
    A class to represent a commercial flight.

    Attributes:
        number (str): The flight number.
        origin (str): The departure location.
        destination (str): The arrival location.
        num_passengers (int): Number of passengers on the flight.
        _total_weight (float): Total weight of the aircraft (including cargo, fuel, passengers).
        _pilot (str): Name of the pilot.
        _crew (list): List of crew members.
    """

    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """
        Initializes a Flight object with all necessary attributes.

        Args:
            number (str): Flight number.
            origin (str): Flight origin.
            destination (str): Flight destination.
            num_passengers (int): Number of passengers.
            total_weight (float): Total weight of the aircraft.
            pilot (str): Pilot's name.
            crew (list): List of crew member names.
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot 
        self._crew = crew

    @property
    def total_weight(self):
        """float: Gets or sets the total weight of the flight."""
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        """
        Sets the total weight of the flight.

        Args:
            weight (float): The new total weight.

        Raises:
            ValueError: If weight is not a positive float.
        """
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """str: Gets or sets the name of the pilot."""
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        """
        Sets the name of the pilot.

        Args:
            new_pilot (str): New pilot's name.
        """
        se
