# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from carbon.apps.customers.models import Customer
from carbon.apps.transport.serializers import TransportSerializer

from .helpers.system.google import GoogleMapsDirectionsMode
from .utils import get_distance_and_time


class TransportViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = TransportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        """
        Returns a JSON response object with the Distance,
        Duration and Emissions between origin and destination

        origin: str
            the origin location of the user
        destination: str
            the destination location of the user
        transport-mode: {'driving', 'walking', 'cycling', 'transit', 'all'}
            the mode of transport that the user will use
        :return: JSON response
                with the calculated data for Distance,
                Duration and Emissions and the mode of transport

        Notes:
            if 'home' or 'work' are send as the origin/destination,
            the customer home/work address is used as the location

            if 'all' is send as the transport-mode, all different
            transport mode data will be returned at the same time
        """
        origin = request.query_params.get("origin")
        destination = request.query_params.get("destination")
        mode = request.query_params.get("transport-mode")

        user_addresses = ["home", "work"]

        if not all([origin, destination, mode]):
            return Response("Both Origin and Destination are needed", status=400)

        if origin == destination:
            return Response("Origin and Destination cannot be the same", status=422)

        if (
            any([origin in user_addresses, destination in user_addresses])
            and not request.user.is_authenticated
        ):
            return Response(
                "Origin/Destination cannot be home/work if you are not authenticated",
                status=403,
            )

        origin = origin.lower()
        destination = destination.lower()

        # we only let authenticated user use the 'home' and 'work' as origin/destination
        if request.user.is_authenticated:
            user = request.user
            customer = Customer.objects.filter(user=user).values().first()

            # if the user doesnt have a associated customer we return
            if not customer:
                return Response(
                    "User not associated with any Customer",
                    status=422,
                )

            # if the customer didnt set a work address the work param value cannot be used
            if any([origin == "work", destination == "work"]) and not customer.get(
                "work_address"
            ):
                return Response(
                    "Origin/Destination cannot be work if you haven't set a work address",
                    status=422,
                )

            if origin in user_addresses:
                origin = customer.get(f"{origin}_address").upper()

            if destination in user_addresses:
                destination = customer.get(f"{destination}_address").upper()

        # if the transport mode value is all, we return a response
        # with all the transport modes information
        if mode == "all":
            transports = {}

            # we loop through all the valid transport modes
            for transport_mode in GoogleMapsDirectionsMode:
                transports.update(
                    {
                        f"{transport_mode.value}": get_distance_and_time(
                            origin=origin,
                            destination=destination,
                            mode=transport_mode.value,
                        )
                    }
                )

                serializer = TransportSerializer(
                    instance=transports.values(), many=True
                )

            return Response(serializer.data)

        transport_data = get_distance_and_time(origin, destination, mode)
        serializer = TransportSerializer(instance=transport_data)

        return Response(serializer.data)
