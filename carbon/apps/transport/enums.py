# -*- coding: utf-8 -*-
from enum import Enum


class TransportModeAverageEmissionPerKilometer(Enum):
    """
    Enum to specify the values of the Carbon Emission generated
    by the different transport modes expressed in grams (g)
    """

    WALKING = 0
    DRIVING = 121
    TRANSIT = 35
    CYCLING = 0
