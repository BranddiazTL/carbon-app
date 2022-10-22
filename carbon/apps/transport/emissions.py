from .enums import TransportModeAverageEmissionPerKilometer
from .helpers.system.google import GoogleMapsDirectionsMode


def get_transport_carbon_emissions(distance, mode):
    emissions = 0

    driving_carbon_emissions = TransportModeAverageEmissionPerKilometer.DRIVING.value
    rail_carbon_emissions = TransportModeAverageEmissionPerKilometer.TRANSIT.value

    if mode == GoogleMapsDirectionsMode.DRIVING.value:
        emissions = distance * driving_carbon_emissions

    if mode == GoogleMapsDirectionsMode.TRANSIT.value:
        emissions = distance * rail_carbon_emissions

    return "%d g" % emissions
