# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Optional, Union

import requests

# Third Party Stuff
from django.conf import settings
from rest_framework.exceptions import ValidationError
from tenacity import Retrying, stop_after_attempt, wait_fixed

# Carbon Stuff
from carbon.apps.transport.helpers.system.google.enums import (
    GoogleMapsDirectionsMode,
    GoogleMapsRegion,
    GoogleMapsUnitsType,
)
from carbon.apps.transport.helpers.system.google.utils import (
    GOOGLE_PATH,
    _get_service_url,
)


def get(
    origin: str,
    destination: str,
    city: str,
    mode: GoogleMapsDirectionsMode,
    units: Optional[GoogleMapsUnitsType] = GoogleMapsUnitsType.METRIC.value,
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Returns the Google Maps Directions response corresponding to the
    specific Address + City. Including, Distance and Duration.

    In this case, we are assuming all users will put a valid Address

    Example:
        address: Dan Ryan Expy
        city: chicago
        origin = DAN RYAN EXPY CHICAGO

    :param origin: str
            the origin location of the user
    :param destination: str
            the destination location of the user
    :param city: str
            the city where the user resides
    :param mode: {'driving', 'walking', 'cycling', 'transit'}
            the mode of transport that the user will use
    :param units: {'metric', 'imperial'}
            the unit system that will be used for the response
    :return: json
            the Google Maps Directions payload
    """
    # Internally Set Params Definition
    key = settings.SYSTEM_GOOGLE_API_KEY
    region = GoogleMapsRegion.US.value

    if not all([origin, destination, mode]):
        raise ValidationError("origin, destination and mode are required")

    if not key:
        raise ValidationError(
            "You must use a Google API key to authenticate each request"
        )

    origin = " ".join([origin, city]).upper()
    destination = " ".join([destination, city]).upper()

    # all the params for the request
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "units": units,
        "key": key,
        "region": region,
    }

    # Params that depends of the Transport Mode
    if mode == GoogleMapsDirectionsMode.TRANSIT.value:
        params[
            "transit-mode"
        ] = "rail"  # This way we limit the transit options to trains, subways and rails

    if mode == GoogleMapsDirectionsMode.DRIVING.value:
        params[
            "departure_time"
        ] = "now"  # We set the departure time to get the traffic information

    response = {}

    # if there is any problem with the request we attempt to get the information 3
    # times before continuing
    for attempt in Retrying(stop=stop_after_attempt(3), wait=wait_fixed(2)):
        endpoint_path = GOOGLE_PATH.get("MAPS_API_DIRECTIONS")

        with attempt:
            response = requests.get(_get_service_url(endpoint_path), params=params)

        if not response.json()["status"] == "OK":
            raise Exception(
                "an unexpected error occurred while attempting to fetch maps directions."
            )

    return response.json()
