# -*- coding: utf-8 -*-
from .emissions import get_transport_carbon_emissions
from .helpers.system.google import (
    GoogleMapsCity,
    GoogleMapsDirectionsMode,
    get_google_maps_directions,
)


class Transport(object):
    """
    Transport object to set all the transport information that we need for the response
    """

    def __init__(self, **kwargs):
        for field in ("distance", "duration", "emissions", "mode"):
            setattr(self, field, kwargs.get(field, None))


def get_distance_and_time(
    origin: str, destination: str, mode: GoogleMapsDirectionsMode
) -> Transport:
    """
    Returns a Transport object with the calculated data for the Distance, Duration,
    and emissions of the travel between the origin and the destination of the user

    :param origin: str
            the origin location of the user
    :param destination: str
            the destination location of the user
    :param mode: {'driving', 'walking', 'cycling', 'transit'}
            the mode of transport that the user will use
    :return: object
            Transport object with the calculated data
    """
    directions = get_google_maps_directions(
        origin, destination, GoogleMapsCity.CHICAGO.value, mode
    )

    distance = directions["routes"][0]["legs"][0]["distance"]["text"]
    duration_in_seconds = directions["routes"][0]["legs"][0]["duration"]["value"]

    # if the transport mode is DRIVING them we also include the time in traffic to the calculation
    if mode == GoogleMapsDirectionsMode.DRIVING.value:
        duration_in_seconds += directions["routes"][0]["legs"][0][
            "duration_in_traffic"
        ]["value"]

    # we get the duration value in seconds and convert it to minutes (mins)
    duration = "%d mins" % round(duration_in_seconds / 60)

    distance_value = 0
    if mode == GoogleMapsDirectionsMode.TRANSIT.value:

        # we iterate for all the steps on the route
        for step in directions["routes"][0]["legs"][0]["steps"]:

            # for each different step on the route we check if the travel mode was a train
            if step["travel_mode"] == GoogleMapsDirectionsMode.TRANSIT.value.upper():
                distance_value += step["distance"]["value"]
    else:
        distance_value = directions["routes"][0]["legs"][0]["distance"]["value"]

    # we get the distance numerical value in meters and convert it to kilometers
    distance_value = distance_value / 1000
    emissions = get_transport_carbon_emissions(distance=distance_value, mode=mode)

    return Transport(
        distance=distance, duration=duration, emissions=emissions, mode=mode
    )
