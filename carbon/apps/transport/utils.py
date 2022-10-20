from .helpers.system.google import (
    GoogleMapsCity,
    GoogleMapsDirectionsMode,
    get_google_maps_directions,
)


class Transport(object):
    def __init__(self, **kwargs):
        for field in ("distance", "duration", "emissions", "mode"):
            setattr(self, field, kwargs.get(field, None))


def get_distance_and_time(origin, destination, mode):
    directions = get_google_maps_directions(
        origin, destination, GoogleMapsCity.CHICAGO.value, mode
    )

    distance = directions["routes"][0]["legs"][0]["distance"]["text"]
    duration_in_seconds = directions["routes"][0]["legs"][0]["duration"]["value"]

    if mode == GoogleMapsDirectionsMode.DRIVING.value:
        duration_in_seconds += directions["routes"][0]["legs"][0][
            "duration_in_traffic"
        ]["value"]

    duration = "%d mins" % round(duration_in_seconds / 60)

    return Transport(distance=distance, duration=duration, emissions=0, mode=mode)
