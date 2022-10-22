# -*- coding: utf-8 -*-
from enum import Enum


class GoogleMapsDirectionsMode(Enum):
    """
    Enum to specify the valid Transport Modes
    """

    WALKING = "walking"
    DRIVING = "driving"
    TRANSIT = "transit"
    CYCLING = "cycling"


class GoogleMapsUnitsType(Enum):
    """
    Enum to specify the Unit system to use
    """

    METRIC = "metric"
    IMPERIAL = "imperial"


class GoogleMapsRegion(Enum):
    """
    Enum to specify the region of the directions search
    """

    US = "us"


class GoogleMapsCity(Enum):
    """
    Enum to specify the supported cities
    """

    CHICAGO = "chicago"
