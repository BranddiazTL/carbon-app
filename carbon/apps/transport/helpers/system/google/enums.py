from enum import Enum


class GoogleMapsDirectionsMode(Enum):
    WALKING = "walking"
    DRIVING = "driving"
    TRANSIT = "transit"
    CYCLING = "cycling"


class GoogleMapsUnitsType(Enum):
    METRIC = "metric"
    IMPERIAL = "imperial"


class GoogleMapsRegion(Enum):
    US = "us"


class GoogleMapsCity(Enum):
    CHICAGO = "chicago"
