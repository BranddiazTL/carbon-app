# -*- coding: utf-8 -*-
from .enums import TransportModeAverageEmissionPerKilometer
from .helpers.system.google import GoogleMapsDirectionsMode


def get_transport_carbon_emissions(
    distance: int, mode: GoogleMapsDirectionsMode
) -> str:
    """
    returns the carbon emissions for a specific distance and transport

    :param distance: int
            the distance between the origin and destination location
    :param mode: {'driving', 'walking', 'cycling', 'transit'}
            the mode of transport that the user will use
    :return: str
            the total amount of grams (g) of emissions
    """
    emissions = 0

    driving_carbon_emissions = TransportModeAverageEmissionPerKilometer.DRIVING.value
    rail_carbon_emissions = TransportModeAverageEmissionPerKilometer.TRANSIT.value

    if mode == GoogleMapsDirectionsMode.DRIVING.value:
        emissions = distance * driving_carbon_emissions

    if mode == GoogleMapsDirectionsMode.TRANSIT.value:
        emissions = distance * rail_carbon_emissions

    return "%d g" % emissions
